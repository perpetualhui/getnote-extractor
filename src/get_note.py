"""
Get 笔记内容提取工具
一个基于 Playwright 的自动化脚本，用于导出 Get 笔记（biji.com）的文章内容
"""

from playwright.sync_api import sync_playwright
import os
import sys
import platform
import json

# 根据操作系统自动查找系统 Chrome 路径
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

def get_getnote_articles_and_export():
    """提取 Get 笔记文章内容并导出到本地文件"""
    config = load_config()

    # 从配置文件读取参数
    getnote_url = config.get("getnote_url", "https://www.biji.com/chat")
    chrome_user_data_dir = config.get("chrome_user_data_dir", "")
    export_path = config.get("export_path", "./getnote_articles.txt")
    article_selector = config.get("article_selector", ".article-content")
    title_selector = config.get("title_selector", ".article-title")

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

    # ========== 关键：配置复用已登录的 Chrome 环境 ==========
    with sync_playwright() as p:
        # 提示用户关闭 Chrome 窗口
        print("\n⚠️  请确保已关闭所有 Chrome 窗口")
        print("3 秒后继续...")
        import time
        time.sleep(3)

        # 启动 Chrome，加载已登录的用户数据目录
        browser = p.chromium.launch_persistent_context(
            user_data_dir=chrome_user_data_dir,
            executable_path=system_chrome_path,
            headless=False,  # 显示浏览器窗口
            args=[
                "--start-maximized",
                "--no-sandbox",
                "--disable-blink-features=AutomationControlled"
            ],
            viewport={"width": 1920, "height": 1080},
            storage_state_persist=True
        )

        try:
            # 打开新页面（直接是已登录状态）
            page = browser.new_page()
            print(f"\n正在访问: {getnote_url}")
            page.goto(getnote_url, timeout=30000, wait_until="networkidle")

            # 提取文稿内容
            print("正在等待文稿内容加载...")
            page.wait_for_selector(article_selector, timeout=15000)

            article_title = page.locator(title_selector).inner_text() if page.locator(title_selector).count() > 0 else "无标题"
            article_content = page.locator(article_selector).inner_text()

            # 导出到本地文件
            os.makedirs(os.path.dirname(export_path) if os.path.dirname(export_path) else ".", exist_ok=True)
            with open(export_path, "w", encoding="utf-8") as f:
                f.write(f"===== {article_title} =====\n\n")
                f.write(article_content)

            print(f"\n✅ 提取成功！")
            print(f"📄 标题: {article_title}")
            print(f"💾 导出路径: {export_path}")

        except Exception as e:
            print(f"\n❌ 提取失败: {str(e)}")
            print("\n故障排查建议:")
            print("  1. 确认 Get 笔记已在 Chrome 中登录")
            print("  2. 检查网页元素选择器是否正确")
            print("  3. 确认 URL 地址是否有效")
            print("  4. 确保网络连接正常")
        finally:
            browser.close()

if __name__ == "__main__":
    print("=" * 50)
    print("  Get 笔记内容提取工具 v1.0.0")
    print("=" * 50)
    get_getnote_articles_and_export()
