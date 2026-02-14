# GetNote Extractor

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Playwright](https://img.shields.io/badge/Playwright-Latest-orange.svg)

**一个基于 Playwright 的自动化工具，用于导出 Get 笔记（biji.com）的文章内容**

[功能特性](#功能特性) • [快速开始](#快速开始) • [配置说明](#配置说明) • [常见问题](#常见问题)

</div>

---

## 📋 目录

- [项目简介](#项目简介)
- [功能特性](#功能特性)
- [系统要求](#系统要求)
- [安装步骤](#安装步骤)
- [配置说明](#配置说明)
- [使用方法](#使用方法)
- [常见问题](#常见问题)
- [技术栈](#技术栈)
- [许可证](#许可证)
- [贡献指南](#贡献指南)

---

## 项目简介

GetNote Extractor 是一个简单易用的 Python 脚本，可以帮助你自动提取并导出 [Get 笔记](https://www.biji.com) 平台的文章内容到本地文本文件。

**主要优势：**
- ✅ **自动化提取** - 无需手动复制粘贴
- ✅ **保留登录状态** - 复用 Chrome 已登录会话
- ✅ **跨平台支持** - Windows / macOS / Linux
- ✅ **配置灵活** - 支持自定义导出路径和选择器

---

## 功能特性

- 🔑 **会话复用** - 自动加载 Chrome 用户数据，无需重复登录
- 🎯 **智能定位** - 使用 CSS 选择器精确定位文章内容
- 📝 **格式化导出** - 自动包含标题和内容，结构清晰
- 🛡️ **安全可靠** - 本地运行，数据不上传至第三方服务器
- ⚙️ **可配置** - 通过 JSON 配置文件自定义参数

---

## 系统要求

- **Python**: 3.8 或更高版本
- **浏览器**: Google Chrome（必须已安装）
- **操作系统**:
  - Windows 10/11
  - macOS 10.15+
  - Linux (Ubuntu 20.04+, Debian 10+, 等)

---

## 安装步骤

### 1. 克隆项目

```bash
git clone https://github.com/YOUR_USERNAME/getnote.git
cd getnote
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 配置参数

复制配置示例文件并填入你的配置：

```bash
cp config.example.json config.json
```

编辑 `config.json` 文件，填入你的 Chrome 用户数据目录路径（详见 [配置说明](#配置说明)）。

---

## 配置说明

### config.json 配置文件

```json
{
  "getnote_url": "https://www.biji.com/chat",
  "chrome_user_data_dir": "C:\\Users\\YOUR_USERNAME\\AppData\\Local\\Google\\Chrome\\User Data",
  "export_path": "./data/getnote_articles.txt",
  "article_selector": ".article-content",
  "title_selector": ".article-title"
}
```

#### 参数说明

| 参数 | 说明 | 示例 |
|------|------|------|
| `getnote_url` | Get 笔记官网地址 | `"https://www.biji.com/chat"` |
| `chrome_user_data_dir` | Chrome 用户数据目录路径 | Windows: `C:\Users\YOUR_USERNAME\AppData\Local\Google\Chrome\User Data`<br>macOS: `~/Library/Application Support/Google/Chrome`<br>Linux: `~/.config/google-chrome` |
| `export_path` | 导出文件的保存路径 | `"./data/articles.txt"` |
| `article_selector` | 文章内容的 CSS 选择器 | `".article-content"` |
| `title_selector` | 文章标题的 CSS 选择器 | `".article-title"` |

#### 如何找到 Chrome 用户数据目录？

**Windows:**
1. 打开 Chrome 浏览器
2. 地址栏输入: `chrome://version`
3. 查看"个人资料路径"一项
4. 复制路径（删除最后的 `Default` 或其他配置文件夹名，只保留到 `User Data`）

**macOS / Linux:**
```bash
echo ~/Library/Application\ Support/Google/Chrome  # macOS
echo ~/.config/google-chrome                       # Linux
```

---

## 使用方法

### 运行脚本

```bash
python src/get_note.py
```

### 使用流程

1. **首次运行前**：确保已在 Chrome 浏览器中登录 Get 笔记账号
2. **运行脚本**：执行上述命令
3. **关闭 Chrome**：脚本会提示关闭所有 Chrome 窗口，关闭后等待 3 秒
4. **自动提取**：脚本自动打开浏览器、访问页面、提取内容
5. **查看结果**：导出完成后，会在配置的路径生成文本文件

### 示例输出

```
==================================================
  Get 笔记内容提取工具 v1.0.0
==================================================
✓ 找到 Chrome 浏览器: C:\Program Files\Google\Chrome\Application\chrome.exe

⚠️  请确保已关闭所有 Chrome 窗口
3 秒后继续...

正在访问: https://www.biji.com/chat
正在等待文稿内容加载...

✅ 提取成功！
📄 标题: 示例文章标题
💾 导出路径: ./data/getnote_articles.txt
```

---

## 🚨 故障排查

### 1. ModuleNotFoundError: No module named 'playwright'

**错误信息**：
```
ModuleNotFoundError: No module named 'playwright'
```

**原因分析**：
运行代码的 Python 环境中没有安装 playwright 模块，或者安装到了不同的 Python 环境。

**解决方案**：

```bash
# 1. 确认当前 Python 环境
python --version
where python  # Windows
which python  # macOS/Linux

# 2. 使用当前环境的 pip 安装 playwright
python -m pip install --upgrade pip
python -m pip install playwright --force-reinstall

# 3. 验证安装
python -c "import playwright; from playwright.sync_api import sync_playwright; print('✅ 安装成功')"
```

**VS Code 用户**：
- 检查左下角的 Python 解释器版本
- 点击解释器版本，选择正确的 Python 环境
- 重启 VS Code 终端后重新安装

---

### 2. Executable doesn't exist at ms-playwright/chromium-xxx

**错误信息**：
```
playwright._impl._errors.Error: BrowserType.launch: Executable doesn't exist at
C:\Users\...\AppData\Local\ms-playwright\chromium-1208\chrome-win64\chrome.exe
```

**原因分析**：
Playwright 的浏览器驱动（可执行文件）未下载到本地。

**解决方案**：

```bash
# 方案1：安装 Playwright 浏览器驱动
python -m playwright install chrome

# 方案2：如果系统已安装 Chrome，指定系统 Chrome 路径
# 在代码中使用 launch_persistent_context() 参数：
# executable_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe"
```

**注意**：本项目已内置自动查找系统 Chrome 路径的功能（`get_system_chrome_path()`），一般无需手动指定。

---

### 3. "chrome" is already installed on the system!

**错误信息**：
```
ATTENTION: "chrome" is already installed on the system!
"chrome" installation is not hermetic; installing newer version
requires *removal* of a current installation first.
```

**原因分析**：
系统中已安装 Chrome，与 Playwright 专属驱动冲突。

**解决方案**：

```bash
# 1. 关闭所有 Chrome 窗口和进程
# 使用任务管理器结束所有 chrome.exe 进程

# 2. 强制重装 Playwright 驱动
python -m playwright install --force chrome
```

---

### 4. net::ERR_NAME_NOT_RESOLVED

**错误信息**：
```
playwright._impl._errors.Error: Page.goto: net::ERR_NAME_NOT_RESOLVED
at https://xn--get-x69d907a0c738ahj2dpuibukkj8a/
```

**原因分析**：
配置的 URL 地址无效或格式错误。

**解决方案**：

1. **手动验证 URL**：
   - 在浏览器中手动访问 Get 笔记官网
   - 确认能正常打开后，复制地址栏的完整 URL

2. **检查 URL 格式**：
```json
// ❌ 错误：缺少协议前缀
"getnote_url": "www.biji.com"

// ❌ 错误：直接写中文
"getnote_url": "Get笔记官网"

// ✅ 正确：完整的 HTTPS URL
"getnote_url": "https://www.biji.com/chat"
```

3. **在代码中添加验证**：
```python
if not getnote_url.startswith(("http://", "https://")):
    raise ValueError("URL 必须以 http:// 或 https:// 开头")
```

---

### 5. 用户数据目录被占用

**错误信息**：
```
Error: User data directory is already in use
```

**原因分析**：
Chrome 用户数据目录同时被多个进程占用（运行脚本时 Chrome 窗口未关闭）。

**解决方案**：

```bash
# 1. 关闭所有 Chrome 窗口
# 2. 检查是否有残留的 Chrome 进程
tasklist | findstr chrome  # Windows
ps aux | grep chrome      # macOS/Linux

# 3. 强制结束残留进程（可选）
taskkill /F /IM chrome.exe  # Windows
killall Chrome             # macOS
```

**代码中的提示**：
脚本运行时会自动提示"请确保已关闭所有 Chrome 窗口，3 秒后继续..."，请遵循提示操作。

---

### 6. TypeError: unexpected keyword argument

**错误信息**：
```
TypeError: BrowserType.launch_persistent_context() got an unexpected
keyword argument 'storage_state_persist'
```

**原因分析**：
使用了 Playwright 不支持的参数名（通常是拼写错误）。

**解决方案**：

```python
# ❌ 错误参数
browser = p.chromium.launch_persistent_context(
    user_data_dir=chrome_user_data_dir,
    storage_state_persist=True  # 此参数不存在
)

# ✅ 正确写法：删除错误参数
browser = p.chromium.launch_persistent_context(
    user_data_dir=chrome_user_data_dir,
    executable_path=system_chrome_path,
    headless=False,
    args=["--start-maximized"]
)
```

**常见错误参数**：
- `storage_state_persist` → 应删除（launch_persistent_context 默认持久化）
- `storage_state_persist=True` → 应删除（拼写错误）

---

### 7. CSS 选择器定位失败

**错误信息**：
```
TimeoutError: waiting for selector ".article-content" failed
```

**原因分析**：
页面元素选择器与实际 HTML 结构不匹配。

**解决方案**：

1. **使用浏览器开发者工具检查元素**：
   ```
   1. 在 Chrome 中打开 Get 笔记页面
   2. 按 F12 打开开发者工具
   3. 点击"元素选择器"（左上角箭头图标）
   4. 点击页面上的文章内容
   5. 查看 Elements 面板中的 HTML 结构
   6. 复制正确的 class 或 id
   ```

2. **常见选择器格式**：
```css
/* class 选择器 */
.article-content
.content-wrapper

/* id 选择器 */
#article
#main-content

/* 组合选择器 */
div.article-content > p
article.content-body
```

3. **在 config.json 中更新选择器**：
```json
{
  "article_selector": ".actual-content-class",
  "title_selector": ".actual-title-class"
}
```

---

### 8. 跨平台路径问题

**问题现象**：
- Windows 上提示路径不存在
- macOS/Linux 上找不到 Chrome

**解决方案**：

本项目已内置跨平台路径检测：

```python
# 自动检测系统 Chrome 路径（src/get_note.py）
def get_system_chrome_path():
    system = platform.system()

    if system == "Windows":
        possible_paths = [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        ]
    elif system == "Darwin":  # macOS
        possible_paths = [
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        ]
    else:  # Linux
        possible_paths = [
            "/usr/bin/google-chrome",
            "/usr/bin/chromium-browser"
        ]
```

**手动查找路径**：

| 平台 | 命令 |
|------|------|
| Windows | 在 Chrome 地址栏输入 `chrome://version` |
| macOS | `echo ~/Library/Application\ Support/Google/Chrome` |
| Linux | `echo ~/.config/google-chrome` |

---

## 常见问题

### Q1: 运行时提示 "未找到 Chrome 浏览器"

**解决方案**：
- 确认已安装 Google Chrome
- Windows 用户确保安装到默认路径
- 或手动指定 Chrome 路径（修改 `src/get_note.py` 中的 `get_system_chrome_path()` 函数）

### Q2: 提示 "用户数据目录不存在"

**解决方案**：
- 检查 `config.json` 中的路径是否正确
- 确保路径指向 `User Data` 文件夹（不包含最后的 `Default`）
- Windows 注意路径中的反斜杠需要转义：`\\`

### Q3: 提取失败，找不到文章内容

**可能原因**：
1. 未在 Chrome 中登录 Get 笔记账号
2. 页面元素选择器已变化
3. 网络连接问题

**解决方案**：
- 确保已在 Chrome 中登录
- 尝试手动访问 URL 确认可正常打开
- 使用浏览器开发者工具检查 CSS 选择器

### Q4: Windows 路径中的反斜杠问题

在 JSON 文件中，反斜杠需要转义：

```json
// ❌ 错误
"chrome_user_data_dir": "C:\Users\YOUR_USERNAME\AppData\Local\Google\Chrome\User Data"

// ✅ 正确
"chrome_user_data_dir": "C:\\Users\\YOUR_USERNAME\\AppData\\Local\\Google\\Chrome\\User Data"
```

---

## 技术栈

- **[Python](https://www.python.org/)** - 主要编程语言
- **[Playwright](https://playwright.dev/)** - 浏览器自动化框架
- **[Chromium](https://www.chromium.org/)** - 底层浏览器引擎

---

## 项目结构

```
getnote/
├── src/
│   └── get_note.py          # 主程序文件
├── data/                    # 导出文件目录（自动创建）
├── config.example.json      # 配置文件示例
├── config.json              # 实际配置文件（需自行创建）
├── requirements.txt         # Python 依赖
├── .gitignore              # Git 忽略文件
├── LICENSE                 # MIT 许可证
└── README.md               # 项目文档
```

---

## 许可证

本项目采用 [MIT License](LICENSE) 开源许可证。

```
MIT License

Copyright (c) 2025 GetNote Extractor Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 贡献指南

欢迎贡献代码！请遵循以下步骤：

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 提交 Pull Request

### 开发规范

- 遵循 PEP 8 代码风格
- 添加适当的注释和文档字符串
- 确保代码在所有支持的平台上正常运行

---

## 免责声明

本工具仅供学习和个人使用。请遵守 Get 笔记平台的服务条款，合理使用本工具，不要进行任何形式的数据滥用或商业用途。

---

## 联系方式

- 提交 [Issue](https://github.com/YOUR_USERNAME/getnote/issues)
- 发起 [Pull Request](https://github.com/YOUR_USERNAME/getnote/pulls)

---

<div align="center">

**⭐ 如果这个项目对你有帮助，请给个 Star！**

Made with ❤️ by GetNote Extractor Contributors

</div>
