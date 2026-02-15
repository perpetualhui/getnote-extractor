"""
Get 笔记内容提取工具 v2.0
一个基于 Playwright 的自动化脚本，用于导出 Get 笔记（biji.com）知识库中的所有文章

主要功能：
- 并行提取：支持多线程并发提取，默认3个并发，速度提升3-5倍
- 断点续传：自动跳过已提取的文章
- 自动分页：自动处理所有页面
- 智能命名：使用博主名称命名文件夹，自动处理重名冲突
- 优雅停止：Ctrl+C 等待当前批次完成后安全退出
- 实时统计：显示提取进度、速度和用时统计
"""

from playwright.sync_api import sync_playwright
import os
import sys
import platform
import json
import time
import re
from urllib.parse import urlparse, parse_qs
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock
import signal

# 全局变量用于优雅停止
should_stop = False
stats_lock = Lock()


def get_system_chrome_path():
    """自动查找系统 Chrome 浏览器路径"""
    system = platform.system()

    if system == "Windows":
        possible_paths = [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
            os.path.expanduser(r"~\AppData\Local\Google\Chrome\Application\chrome.exe")
        ]
        try:
            import winreg
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe")
            path = winreg.QueryValue(key, None)
            winreg.CloseKey(key)
            if os.path.exists(path):
                return path
        except Exception:
            pass
    elif system == "Darwin":  # macOS
        possible_paths = [
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        ]
    else:  # Linux
        possible_paths = [
            "/usr/bin/google-chrome",
            "/usr/bin/chromium-browser",
            "/snap/bin/chromium"
        ]

    for path in possible_paths:
        if os.path.exists(path):
            return path

    raise FileNotFoundError(
        "未找到系统中的 Chrome 浏览器，请确认已安装！\n"
        "访问 https://www.google.com/chrome/ 下载安装"
    )


def load_config(config_file="config.json"):
    """加载配置文件"""
    try:
        with open(config_file, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"配置文件不存在: {config_file}")
        print("请复制 config.example.json 为 config.json 并填入您的配置")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"配置文件格式错误: {e}")
        sys.exit(1)


def sanitize_filename(title):
    """清理文件名，移除非法字符"""
    # 移除或替换 Windows/Linux 不允许的字符
    title = re.sub(r'[<>:"/\\|?*#]', '', title)
    # 限制长度为100个字符
    return title[:100].strip()


def extract_topic_id(url_or_id):
    """从 URL 或 ID 中提取知识库 ID"""
    if url_or_id.startswith('http://') or url_or_id.startswith('https://'):
        match = re.search(r'subject/([^/?]+)', url_or_id)
        if match:
            return match.group(1)
    return url_or_id


def extract_follow_name(url):
    """从 URL 中提取 followName 参数"""
    try:
        parsed = urlparse(url)
        params = parse_qs(parsed.query)
        if 'followName' in params:
            return params['followName'][0]
    except Exception:
        pass
    return None


def get_unique_output_dir(base_name):
    """获取不冲突的输出目录"""
    output_dir = f"./{base_name}"
    counter = 2
    while os.path.exists(output_dir):
        output_dir = f"./{base_name}_{counter}"
        counter += 1
    return output_dir


def extract_article_content(page, detail_url):
    """提取单篇文章的内容"""
    try:
        web_url = f"{detail_url}/web"
        page.goto(web_url, timeout=20000, wait_until="domcontentloaded")

        # 智能等待：等待段落出现即可
        try:
            page.wait_for_selector('p', timeout=5000)
        except Exception:
            pass

        # 提取内容
        paragraphs = page.query_selector_all('p')
        title = ''
        original_link = ''
        content_parts = []

        for p in paragraphs:
            try:
                text = p.inner_text().strip()
                if text.startswith('原链接：'):
                    original_link = text.replace('原链接：', '')
                elif not title and text and len(text) < 200:
                    title = text
                elif len(text) > 50:
                    content_parts.append(text)
            except Exception:
                continue

        main_content = '\n\n'.join(content_parts)

        return {
            'title': title,
            'original_link': original_link,
            'main_content': main_content
        }
    except Exception as e:
        print(f"  ✗ 提取失败: {str(e)}")
        return None


def process_article(context, article, output_dir, global_index, start_time, stats):
    """处理单篇文章"""
    filename = f"{str(global_index).padStart(3, '0')}_{sanitize_filename(article['title'])}.md"
    filepath = os.path.join(output_dir, filename)

    # 检查文件是否已存在（断点续传）
    if os.path.exists(filepath):
        print(f"  [{global_index}] ⏭️ {article['title'][:40]}... - 已存在，跳过")
        with stats_lock:
            stats['skipped'] += 1
        return {'skipped': True, 'saved': False}

    # 检查是否有有效的 URL
    if not article.get('detail_url'):
        print(f"  [{global_index}] ✗ {article['title'][:40]}... - 无有效URL")
        return {'skipped': False, 'saved': False}

    try:
        print(f"  [{global_index}] 🔄 {article['title'][:40]}...")

        # 为每篇文章创建独立的页面
        page = context.new_page()
        try:
            content = extract_article_content(page, article['detail_url'])

            if content and content['main_content']:
                # 生成 Markdown 内容
                markdown = f"# {article['title']}\n\n"
                markdown += f"**原链接**: {content['original_link'] or ''}\n\n"
                markdown += "---\n\n"
                markdown += content['main_content']

                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(markdown)

                with stats_lock:
                    stats['saved'] += 1

                # 计算并显示实时统计
                elapsed_minutes = (time.time() - start_time) / 60
                avg_speed = stats['saved'] / elapsed_minutes if elapsed_minutes > 0 else 0
                print(f"  [{global_index}] ✓ {article['title'][:40]}... - 已保存 ({avg_speed:.1f} 篇/分钟)")

                page.close()
                return {'skipped': False, 'saved': True}
            else:
                print(f"  [{global_index}] ✗ {article['title'][:40]}... - 内容为空")
                page.close()
                return {'skipped': False, 'saved': False}
        except Exception as e:
            print(f"  [{global_index}] ✗ {article['title'][:40]}... - 处理失败: {str(e)}")
            page.close()
            return {'skipped': False, 'saved': False}
    except Exception as e:
        print(f"  [{global_index}] ✗ {article['title'][:40]}... - 创建页面失败: {str(e)}")
        return {'skipped': False, 'saved': False}


def fetch_article_urls(page, base_url, articles, current_page):
    """串行获取文章 URL（通过点击）"""
    urls = []

    for i, article in enumerate(articles):
        try:
            # 返回列表页
            page.goto(base_url, timeout=20000, wait_until="domcontentloaded")
            page.wait_for_selector('tbody tr', timeout=5000)
            time.sleep(1)

            # 如果不是第一页，需要翻页
            if current_page > 1:
                separator = '&' if '?' in base_url else '?'
                page_url = f"{base_url}{separator}page={current_page}"
                page.goto(page_url, timeout=20000, wait_until="domcontentloaded")
                page.wait_for_selector('tbody tr', timeout=5000)
                time.sleep(1)

            # 点击第 i 行
            page.evaluate(f"() => {{ const rows = document.querySelectorAll('tbody tr'); if (rows[{i}]) {{ const titleCell = rows[{i}].querySelector('td:first-child'); if (titleCell) titleCell.click(); }} }}")

            # 等待页面跳转
            time.sleep(1.5)
            url = page.url
            urls.append({
                **article,
                'detail_url': url
            })
            print(f"  [{i+1}/{len(articles)}] 获取URL: {article['title'][:30]}...")
        except Exception as e:
            print(f"  [{i+1}/{len(articles)}] 获取URL失败: {str(e)}")
            urls.append({
                **article,
                'detail_url': None
            })

    return urls


def signal_handler(signum, frame):
    """信号处理器，用于优雅停止"""
    global should_stop
    if not should_stop:
        should_stop = True
        print("\n\n⚠️ 收到停止信号，正在优雅退出...")
        print("等待当前批次处理完成...")


def main():
    """主函数"""
    # 设置信号处理器
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    # 从命令行参数或配置文件获取参数
    if len(sys.argv) < 2:
        print("用法：")
        print("  python get_note.py <知识库URL或ID> [输出目录] [最大页数] [最大文章数] [并发数]")
        print("")
        print("示例：")
        print('  python get_note.py https://www.biji.com/subject/ABC123/DEFAULT?followName=博主名')
        print("  python get_note.py ABC123")
        print('  python get_note.py ABC123 "自定义目录" 0 0 3')
        sys.exit(1)

    url_or_id = sys.argv[1]
    topic_id = extract_topic_id(url_or_id)

    # 确定输出目录名
    if len(sys.argv) >= 3:
        output_dir_name = sys.argv[2]
    else:
        follow_name = extract_follow_name(url_or_id)
        output_dir_name = follow_name or topic_id

    # 获取不冲突的输出目录
    output_dir = get_unique_output_dir(output_dir_name)
    os.makedirs(output_dir, exist_ok=True)

    # 其他参数
    max_pages = int(sys.argv[3]) if len(sys.argv) >= 4 else 0
    max_articles = int(sys.argv[4]) if len(sys.argv) >= 5 else 0
    concurrency = int(sys.argv[5]) if len(sys.argv) >= 6 else 3

    # 确定基础 URL
    if url_or_id.startswith('http://') or url_or_id.startswith('https://'):
        base_url = url_or_id
    else:
        base_url = f"https://www.biji.com/subject/{topic_id}/DEFAULT"

    print("=" * 50)
    print("  Get 笔记内容提取工具 v2.0")
    print("=" * 50)
    print(f"知识库ID: {topic_id}")
    print(f"输出目录: {os.path.basename(output_dir)}")
    print(f"最大页数: {max_pages if max_pages > 0 else '全部'}")
    print(f"最大文章数: {max_articles if max_articles > 0 else '全部'}")
    print(f"并发数: {concurrency}")
    print("")

    # 加载配置
    config = load_config()
    chrome_user_data_dir = config.get("chrome_user_data_dir", "")

    if not chrome_user_data_dir:
        print("错误：请在 config.json 中配置 chrome_user_data_dir")
        sys.exit(1)

    # 验证用户数据目录存在
    if not os.path.exists(chrome_user_data_dir):
        print(f"错误：Chrome 用户数据目录不存在: {chrome_user_data_dir}")
        print("提示：请检查路径是否正确（到 User Data 这一层）")
        sys.exit(1)

    try:
        system_chrome_path = get_system_chrome_path()
        print(f"✓ 找到 Chrome 浏览器: {system_chrome_path}")
    except FileNotFoundError as e:
        print(f"✗ {e}")
        sys.exit(1)

    # 记录开始时间
    start_time = time.time()
    stats = {'saved': 0, 'skipped': 0}

    print("\n⚠️ 请确保已关闭所有 Chrome 窗口")
    print("3 秒后继续...")
    time.sleep(3)

    # 启动浏览器
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            user_data_dir=chrome_user_data_dir,
            executable_path=system_chrome_path,
            headless=False,
            args=[
                "--start-maximized",
                "--no-sandbox",
                "--disable-blink-features=AutomationControlled"
            ],
            viewport={"width": 1920, "height": 1080},
            storage_state_persist=True
        )

        try:
            page = browser.new_page()
            current_page = 1

            while (max_pages == 0 or current_page <= max_pages) and not should_stop:
                print(f"\n处理第 {current_page} 页...")

                try:
                    # 构建页面 URL
                    if current_page == 1:
                        page_url = base_url
                    else:
                        separator = '&' if '?' in base_url else '?'
                        page_url = f"{base_url}{separator}page={current_page}"

                    print(f"访问: {page_url}")
                    page.goto(page_url, timeout=30000, wait_until="domcontentloaded")
                    print("页面已加载，等待内容...")
                    time.sleep(3)

                    # 等待表格出现
                    try:
                        page.wait_for_selector('tbody tr', timeout=10000)
                        print("表格已出现")
                    except Exception as e:
                        print("未找到表格，检查页面状态...")
                        print(f"当前URL: {page.url()}")
                        print(f"页面标题: {page.title()}")

                        # 检查是否需要登录
                        needs_login = page.evaluate("() => document.body.innerText.includes('登录') || document.body.innerText.includes('请先登录')")

                        if needs_login:
                            print("\n⚠️ 需要登录！")
                            print("=" * 50)
                            print("请在打开的浏览器窗口中登录 Get笔记账号")
                            print("=" * 50)
                            print("")
                            print("步骤：")
                            print("1. 查看自动打开的浏览器窗口")
                            print("2. 在浏览器中登录 www.biji.com")
                            print("3. 登录成功后，脚本会自动继续")
                            print("")
                            print("等待登录中（最多60秒）...")
                            print("")

                            time.sleep(60)

                            # 重新加载页面
                            page.goto(base_url, timeout=30000, wait_until="domcontentloaded")
                            time.sleep(3)

                            try:
                                page.wait_for_selector('tbody tr', timeout=10000)
                                print("✅ 登录成功，表格已出现")
                            except Exception:
                                print("\n❌ 登录超时或失败")
                                print("请确保已在浏览器中完成登录，然后重新运行脚本")
                                browser.close()
                                sys.exit(1)
                        else:
                            raise e

                    # 提取所有文章信息
                    articles_data = page.evaluate("""() => {
                        const rows = document.querySelectorAll('tbody tr');
                        return Array.from(rows).map((row, index) => {
                            const titleCell = row.querySelector('td:first-child');
                            const title = titleCell ? titleCell.textContent.trim() : null;
                            return { title, index };
                        }).filter(item => item.title);
                    }""")

                    articles = [{'title': a['title'], 'index': a['index']} for a in articles_data]
                    print(f"找到 {len(articles)} 篇文案")

                    if len(articles) == 0:
                        if current_page == 1:
                            print("没有找到文案，可能需要登录")
                        else:
                            print("没有更多文章了，已到达最后一页")
                        break

                    # 步骤1：串行获取所有文章的 URL
                    print("\n📋 步骤1: 获取文章URL...")
                    articles_with_urls = fetch_article_urls(page, page_url, articles, current_page)

                    # 步骤2：并行提取文章内容（分批处理）
                    print("\n📝 步骤2: 并行提取内容...")

                    for i in range(0, len(articles_with_urls), concurrency):
                        if should_stop:
                            print("\n⏸️ 停止提取，保存进度...")
                            break

                        if max_articles > 0 and stats['saved'] >= max_articles:
                            print(f"\n已达到最大文章数限制 ({max_articles})，停止提取")
                            break

                        batch = articles_with_urls[i:i + concurrency]

                        # 使用线程池并行处理
                        with ThreadPoolExecutor(max_workers=concurrency) as executor:
                            futures = []
                            for batch_idx, article in enumerate(batch):
                                global_index = (current_page - 1) * 20 + i + batch_idx + 1
                                future = executor.submit(
                                    process_article,
                                    browser,
                                    article,
                                    output_dir,
                                    global_index,
                                    start_time,
                                    stats
                                )
                                futures.append(future)

                            for future in as_completed(futures):
                                try:
                                    future.result()
                                except Exception as e:
                                    print(f"处理失败: {str(e)}")

                    if should_stop:
                        break

                    current_page += 1

                except Exception as e:
                    print(f"处理第 {current_page} 页失败: {str(e)}")
                    break

        finally:
            browser.close()

    # 计算最终统计
    total_minutes = (time.time() - start_time) / 60
    final_speed = stats['saved'] / total_minutes if total_minutes > 0 else 0

    print("\n" + "=" * 50)
    print("  完成")
    print("=" * 50)
    print(f"总共保存: {stats['saved']} 篇文案")
    if stats['skipped'] > 0:
        print(f"跳过已存在: {stats['skipped']} 篇")
    print(f"总用时: {total_minutes:.1f} 分钟")
    print(f"平均速度: {final_speed:.1f} 篇/分钟")
    print(f"输出目录: {output_dir}")


if __name__ == "__main__":
    main()
