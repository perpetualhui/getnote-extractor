# GetNote Extractor

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Playwright](https://img.shields.io/badge/Playwright-Latest-orange.svg)

**[English](#english) | [中文](#中文)**

[Features](#features) • [Quick Start](#quick-start) • [Configuration](#configuration) • [Troubleshooting](#troubleshooting)

</div>

---

## 📋 Table of Contents / 目录

- [Project Introduction](#project-introduction) / [项目简介](#项目简介-1)
- [Core Features](#core-features) / [核心功能](#核心功能)
- [Who Should Use This](#who-should-use-this) / [适合谁用](#适合谁用)
- [System Requirements](#system-requirements) / [系统要求](#系统要求)
- [Installation](#installation) / [安装步骤](#安装步骤)
- [Configuration](#configuration) / [配置说明](#配置说明)
- [Usage](#usage) / [使用方法](#使用方法)
- [Troubleshooting](#troubleshooting) / [故障排查](#故障排查)
- [FAQ](#faq) / [常见问题](#常见问题)
- [Tech Stack](#tech-stack) / [技术栈](#技术栈)
- [License](#license) / [许可证](#许可证)
- [Contributing](#contributing) / [贡献指南](#贡献指南)

---

## English

## Project Introduction

GetNote Extractor is a Python automation tool built with Playwright, designed to help you export articles from Get Notes (biji.com) to your local computer. Simple to operate - even computer beginners can use it with ease.

### Core Features

- **Auto Login State Reuse**: Directly reads Chrome's logged-in session information, no need to enter account credentials repeatedly
- **Precise Content Extraction**: Accurately locates article titles and body text through CSS selectors, ensuring complete and clean exported content
- **Full Platform Support**: Compatible with all mainstream computer systems - Windows, macOS, and Linux
- **Flexible Customization**: Modify export location and extraction rules via JSON configuration files to suit your personal preferences
- **Local & Secure Operation**: Runs entirely on your own computer; note data is never uploaded to any third-party servers

### Who Should Use This

Users who need to backup Get Notes content locally or archive materials. No programming knowledge required - just follow the tutorial for one-click export, eliminating the need for manual copy-paste.

**Key Advantages:**
- ✅ **Automated Extraction** - No manual copy-paste needed
- ✅ **Preserved Login State** - Reuses Chrome's logged-in session
- ✅ **Cross-Platform Support** - Windows / macOS / Linux
- ✅ **Flexible Configuration** - Supports custom export paths and selectors

---

## 中文

## 项目简介

GetNote Extractor 是一个简单易用的 Python 脚本，可以帮助你自动提取并导出 [Get 笔记](https://www.biji.com) 平台的文章内容到本地文本文件。

### 核心功能

- **登录状态自动复用**：直接读取 Chrome 已登录的会话信息，不用重复输账号密码
- **精准内容提取**：通过 CSS 选择器准确定位文章标题和正文，导出内容完整不乱
- **全平台支持**：兼容 Windows、macOS、Linux 所有主流电脑系统
- **灵活自定义配置**：通过 JSON 文件修改导出位置、提取规则，适配个人使用习惯
- **本地安全运行**：全程只在你自己电脑上运行，笔记数据不会上传任何第三方服务器

### 适合谁用

需要把 Get 笔记内容备份到本地、做资料归档的用户，不用懂编程，跟着教程就能一键导出，不用手动复制粘贴。

**主要优势：**
- ✅ **自动化提取** - 无需手动复制粘贴
- ✅ **保留登录状态** - 复用 Chrome 已登录会话
- ✅ **跨平台支持** - Windows / macOS / Linux
- ✅ **配置灵活** - 支持自定义导出路径和选择器

---

## English / 中文

## Features / 功能特性

- 🔑 **Session Reuse** / **会话复用** - Automatically loads Chrome user data, no need to log in repeatedly / 自动加载 Chrome 用户数据，无需重复登录
- 🎯 **Smart Positioning** / **智能定位** - Uses CSS selectors to precisely locate article content / 使用 CSS 选择器精确定位文章内容
- 📝 **Formatted Export** / **格式化导出** - Automatically includes title and content with clear structure / 自动包含标题和内容，结构清晰
- 🛡️ **Secure & Reliable** / **安全可靠** - Runs locally, data is never uploaded to third-party servers / 本地运行，数据不上传至第三方服务器
- ⚙️ **Configurable** / **可配置** - Customize parameters through JSON configuration file / 通过 JSON 配置文件自定义参数

---

## English / 中文

## System Requirements / 系统要求

- **Python**: 3.8 or higher / 3.8 或更高版本
- **Browser**: Google Chrome (must be installed) / Google Chrome（必须已安装）
- **Operating System / 操作系统**:
  - Windows 10/11
  - macOS 10.15+
  - Linux (Ubuntu 20.04+, Debian 10+, etc.)

---

## Installation / 安装步骤

### 1. Clone Project / 克隆项目

```bash
git clone https://github.com/YOUR_USERNAME/getnote.git
cd getnote
```

### 2. Install Dependencies / 安装依赖

```bash
pip install -r requirements.txt
```

### 3. Configure Parameters / 配置参数

Copy the configuration example file and fill in your settings / 复制配置示例文件并填入你的配置：

```bash
cp config.example.json config.json
```

Edit the `config.json` file and enter your Chrome user data directory path (see [Configuration](#configuration) for details) / 编辑 `config.json` 文件，填入你的 Chrome 用户数据目录路径（详见 [配置说明](#配置说明)）。

---

## English / 中文

## Configuration / 配置说明

### config.json Configuration File / 配置文件

```json
{
  "getnote_url": "https://www.biji.com/chat",
  "chrome_user_data_dir": "C:\\Users\\YOUR_USERNAME\\AppData\\Local\\Google\\Chrome\\User Data",
  "export_path": "./data/getnote_articles.txt",
  "article_selector": ".article-content",
  "title_selector": ".article-title"
}
```

#### Parameter Description / 参数说明

| Parameter / 参数 | Description / 说明 | Example / 示例 |
|------|------|------|
| `getnote_url` | Get Notes official website / Get 笔记官网地址 | `"https://www.biji.com/chat"` |
| `chrome_user_data_dir` | Chrome user data directory path / Chrome 用户数据目录路径 | Windows: `C:\Users\YOUR_USERNAME\AppData\Local\Google\Chrome\User Data`<br>macOS: `~/Library/Application Support/Google/Chrome`<br>Linux: `~/.config/google-chrome` |
| `export_path` | Export file save path / 导出文件的保存路径 | `"./data/articles.txt"` |
| `article_selector` | CSS selector for article content / 文章内容的 CSS 选择器 | `".article-content"` |
| `title_selector` | CSS selector for article title / 文章标题的 CSS 选择器 | `".article-title"` |

#### How to Find Chrome User Data Directory? / 如何找到 Chrome 用户数据目录？

**Windows:**
1. Open Chrome browser / 打开 Chrome 浏览器
2. Enter in address bar / 地址栏输入: `chrome://version`
3. Check "Profile Path" / 查看"个人资料路径"一项
4. Copy the path (remove the final `Default` or other profile folder name, keep only `User Data`) / 复制路径（删除最后的 `Default` 或其他配置文件夹名，只保留到 `User Data`）

**macOS / Linux:**
```bash
echo ~/Library/Application\ Support/Google/Chrome  # macOS
echo ~/.config/google-chrome                       # Linux
```

---

## English / 中文

## Usage / 使用方法

### Run Script / 运行脚本

```bash
python src/get_note.py
```

### Usage Flow / 使用流程

1. **Before First Run** / **首次运行前**: Ensure you're logged into Get Notes in Chrome browser / 确保已在 Chrome 浏览器中登录 Get 笔记账号
2. **Run Script** / **运行脚本**: Execute the above command / 执行上述命令
3. **Close Chrome** / **关闭 Chrome**: Script will prompt to close all Chrome windows, wait 3 seconds after closing / 脚本会提示关闭所有 Chrome 窗口，关闭后等待 3 秒
4. **Auto Extract** / **自动提取**: Script automatically opens browser, visits page, extracts content / 脚本自动打开浏览器、访问页面、提取内容
5. **View Results** / **查看结果**: After export completes, text file will be generated at configured path / 导出完成后，会在配置的路径生成文本文件

### Sample Output / 示例输出

```
==================================================
  Get Note Content Extractor v1.0.0 / Get 笔记内容提取工具 v1.0.0
==================================================
✓ Found Chrome Browser / 找到 Chrome 浏览器: C:\Program Files\Google\Chrome\Application\chrome.exe

⚠️  Please ensure all Chrome windows are closed / 请确保已关闭所有 Chrome 窗口
Continuing in 3 seconds / 3 秒后继续...

Visiting / 正在访问: https://www.biji.com/chat
Waiting for content to load / 正在等待文稿内容加载...

✅ Extraction Successful / 提取成功！
📄 Title / 标题: Sample Article Title / 示例文章标题
💾 Export Path / 导出路径: ./data/getnote_articles.txt
```

---

## English / 中文

## 🚨 Troubleshooting / 故障排查

### 1. ModuleNotFoundError: No module named 'playwright'

**Error Message / 错误信息**：
```
ModuleNotFoundError: No module named 'playwright'
```

**Cause Analysis / 原因分析**：
The playwright module is not installed in the Python environment running the code, or was installed in a different Python environment / 运行代码的 Python 环境中没有安装 playwright 模块，或者安装到了不同的 Python 环境。

**Solution / 解决方案**：

```bash
# 1. Confirm current Python environment / 确认当前 Python 环境
python --version
where python  # Windows
which python  # macOS/Linux

# 2. Install playwright using current environment's pip / 使用当前环境的 pip 安装 playwright
python -m pip install --upgrade pip
python -m pip install playwright --force-reinstall

# 3. Verify installation / 验证安装
python -c "import playwright; from playwright.sync_api import sync_playwright; print('✅ Installation Successful / 安装成功')"
```

**VS Code Users / VS Code 用户**：
- Check the Python interpreter version in the bottom left corner / 检查左下角的 Python 解释器版本
- Click the interpreter version and select the correct Python environment / 点击解释器版本，选择正确的 Python 环境
- Restart VS Code terminal and reinstall / 重启 VS Code 终端后重新安装

---

### 2. Executable doesn't exist at ms-playwright/chromium-xxx

**Error Message / 错误信息**：
```
playwright._impl._errors.Error: BrowserType.launch: Executable doesn't exist at
C:\Users\...\AppData\Local\ms-playwright\chromium-1208\chrome-win64\chrome.exe
```

**Cause Analysis / 原因分析**：
Playwright's browser driver (executable) is not downloaded locally / Playwright 的浏览器驱动（可执行文件）未下载到本地。

**Solution / 解决方案**：

```bash
# Solution 1: Install Playwright browser driver / 安装 Playwright 浏览器驱动
python -m playwright install chrome

# Solution 2: If Chrome is already installed on system, specify system Chrome path / 如果系统已安装 Chrome，指定系统 Chrome 路径
# Use launch_persistent_context() parameter in code / 在代码中使用 launch_persistent_context() 参数：
# executable_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe"
```

**Note / 注意**: This project has built-in automatic system Chrome path detection (`get_system_chrome_path()`), manual specification is usually not needed / 本项目已内置自动查找系统 Chrome 路径的功能（`get_system_chrome_path()`），一般无需手动指定。

---

### 3. "chrome" is already installed on the system!

**Error Message / 错误信息**：
```
ATTENTION: "chrome" is already installed on the system!
"chrome" installation is not hermetic; installing newer version
requires *removal* of a current installation first.
```

**Cause Analysis / 原因分析**：
Chrome is already installed on the system, conflicting with Playwright's dedicated driver / 系统中已安装 Chrome，与 Playwright 专属驱动冲突。

**Solution / 解决方案**：

```bash
# 1. Close all Chrome windows and processes / 关闭所有 Chrome 窗口和进程
# Use Task Manager to end all chrome.exe processes / 使用任务管理器结束所有 chrome.exe 进程

# 2. Force reinstall Playwright driver / 强制重装 Playwright 驱动
python -m playwright install --force chrome
```

---

### 4. net::ERR_NAME_NOT_RESOLVED

**Error Message / 错误信息**：
```
playwright._impl._errors.Error: Page.goto: net::ERR_NAME_NOT_RESOLVED
at https://xn--get-x69d907a0c738ahj2dpuibukkj8a/
```

**Cause Analysis / 原因分析**：
The configured URL is invalid or incorrectly formatted / 配置的 URL 地址无效或格式错误。

**Solution / 解决方案**：

1. **Manually Verify URL / 手动验证 URL**:
   - Manually visit Get Notes official website in browser / 在浏览器中手动访问 Get 笔记官网
   - After confirming it opens normally, copy the complete URL from address bar / 确认能正常打开后，复制地址栏的完整 URL

2. **Check URL Format / 检查 URL 格式**:
```json
// ❌ Wrong: Missing protocol prefix / 错误：缺少协议前缀
"getnote_url": "www.biji.com"

// ❌ Wrong: Directly using Chinese / 错误：直接写中文
"getnote_url": "Get笔记官网"

// ✅ Correct: Complete HTTPS URL / 正确：完整的 HTTPS URL
"getnote_url": "https://www.biji.com/chat"
```

3. **Add Validation in Code / 在代码中添加验证**:
```python
if not getnote_url.startswith(("http://", "https://")):
    raise ValueError("URL must start with http:// or https:// / URL 必须以 http:// 或 https:// 开头")
```

---

### 5. User Data Directory Already in Use / 用户数据目录被占用

**Error Message / 错误信息**：
```
Error: User data directory is already in use
```

**Cause Analysis / 原因分析**：
Chrome user data directory is occupied by multiple processes simultaneously (Chrome windows were not closed when running the script) / Chrome 用户数据目录同时被多个进程占用（运行脚本时 Chrome 窗口未关闭）。

**Solution / 解决方案**：

```bash
# 1. Close all Chrome windows / 关闭所有 Chrome 窗口
# 2. Check for remaining Chrome processes / 检查是否有残留的 Chrome 进程
tasklist | findstr chrome  # Windows
ps aux | grep chrome      # macOS/Linux

# 3. Force kill remaining processes (optional) / 强制结束残留进程（可选）
taskkill /F /IM chrome.exe  # Windows
killall Chrome             # macOS
```

**Note in Code / 代码中的提示**：
When the script runs, it will automatically prompt "Please ensure all Chrome windows are closed, continuing in 3 seconds..." - please follow this prompt / 脚本运行时会自动提示"请确保已关闭所有 Chrome 窗口，3 秒后继续..."，请遵循提示操作。

---

### 6. TypeError: unexpected keyword argument

**Error Message / 错误信息**：
```
TypeError: BrowserType.launch_persistent_context() got an unexpected
keyword argument 'storage_state_persist'
```

**Cause Analysis / 原因分析**：
Using a parameter name not supported by Playwright (usually a spelling error) / 使用了 Playwright 不支持的参数名（通常是拼写错误）。

**Solution / 解决方案**：

```python
# ❌ Wrong parameter / 错误参数
browser = p.chromium.launch_persistent_context(
    user_data_dir=chrome_user_data_dir,
    storage_state_persist=True  # This parameter does not exist / 此参数不存在
)

# ✅ Correct: Remove error parameter / 正确写法：删除错误参数
browser = p.chromium.launch_persistent_context(
    user_data_dir=chrome_user_data_dir,
    executable_path=system_chrome_path,
    headless=False,
    args=["--start-maximized"]
)
```

**Common Error Parameters / 常见错误参数**：
- `storage_state_persist` → Should be removed (launch_persistent_context defaults to persistent) / 应删除（launch_persistent_context 默认持久化）
- `storage_state_persist=True` → Should be removed (spelling error) / 应删除（拼写错误）

---

### 7. CSS Selector Positioning Failure / CSS 选择器定位失败

**Error Message / 错误信息**：
```
TimeoutError: waiting for selector ".article-content" failed
```

**Cause Analysis / 原因分析**：
Page element selector does not match actual HTML structure / 页面元素选择器与实际 HTML 结构不匹配。

**Solution / 解决方案**：

1. **Use Browser Developer Tools to Inspect Elements / 使用浏览器开发者工具检查元素**:
   ```
   1. Open Get Notes page in Chrome / 在 Chrome 中打开 Get 笔记页面
   2. Press F12 to open Developer Tools / 按 F12 打开开发者工具
   3. Click "Element Picker" (arrow icon in top left) / 点击"元素选择器"（左上角箭头图标）
   4. Click article content on the page / 点击页面上的文章内容
   5. View HTML structure in Elements panel / 查看 Elements 面板中的 HTML 结构
   6. Copy correct class or id / 复制正确的 class 或 id
   ```

2. **Common Selector Formats / 常见选择器格式**:
```css
/* class selector / class 选择器 */
.article-content
.content-wrapper

/* id selector / id 选择器 */
#article
#main-content

/* combinator selector / 组合选择器 */
div.article-content > p
article.content-body
```

3. **Update Selector in config.json / 在 config.json 中更新选择器**:
```json
{
  "article_selector": ".actual-content-class",
  "title_selector": ".actual-title-class"
}
```

---

### 8. Cross-Platform Path Issues / 跨平台路径问题

**Problem / 问题现象**：
- Path not found on Windows / Windows 上提示路径不存在
- Chrome not found on macOS/Linux / macOS/Linux 上找不到 Chrome

**Solution / 解决方案**：

This project has built-in cross-platform path detection / 本项目已内置跨平台路径检测：

```python
# Auto-detect system Chrome path (src/get_note.py) / 自动检测系统 Chrome 路径
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

**Manual Path Lookup / 手动查找路径**：

| Platform / 平台 | Command / 命令 |
|------|------|
| Windows | Enter `chrome://version` in Chrome address bar / 在 Chrome 地址栏输入 `chrome://version` |
| macOS | `echo ~/Library/Application\ Support/Google/Chrome` |
| Linux | `echo ~/.config/google-chrome` |

---

## English / 中文

## FAQ / 常见问题

### Q1: Prompt "Chrome browser not found" during runtime / 运行时提示 "未找到 Chrome 浏览器"

**Solution / 解决方案**：
- Confirm Google Chrome is installed / 确认已安装 Google Chrome
- Windows users ensure installation to default path / Windows 用户确保安装到默认路径
- Or manually specify Chrome path (modify `get_system_chrome_path()` function in `src/get_note.py`) / 或手动指定 Chrome 路径（修改 `src/get_note.py` 中的 `get_system_chrome_path()` 函数）

### Q2: Prompt "User data directory does not exist" / 提示 "用户数据目录不存在"

**Solution / 解决方案**：
- Check if path in `config.json` is correct / 检查 `config.json` 中的路径是否正确
- Ensure path points to `User Data` folder (does not include final `Default`) / 确保路径指向 `User Data` 文件夹（不包含最后的 `Default`）
- Windows note: backslashes in paths need escaping: `\\` / Windows 注意路径中的反斜杠需要转义：`\\`

### Q3: Extraction fails, article content not found / 提取失败，找不到文章内容

**Possible Causes / 可能原因**：
1. Not logged into Get Notes account in Chrome / 未在 Chrome 中登录 Get 笔记账号
2. Page element selector has changed / 页面元素选择器已变化
3. Network connection issues / 网络连接问题

**Solution / 解决方案**：
- Ensure logged in Chrome / 确保已在 Chrome 中登录
- Try manually visiting URL to confirm it opens normally / 尝试手动访问 URL 确认可正常打开
- Use browser developer tools to check CSS selector / 使用浏览器开发者工具检查 CSS 选择器

### Q4: Windows Path Backslash Issues / Windows 路径中的反斜杠问题

In JSON files, backslashes need escaping / 在 JSON 文件中，反斜杠需要转义：

```json
// ❌ Wrong / 错误
"chrome_user_data_dir": "C:\Users\YOUR_USERNAME\AppData\Local\Google\Chrome\User Data"

// ✅ Correct / 正确
"chrome_user_data_dir": "C:\\Users\\YOUR_USERNAME\\AppData\\Local\\Google\\Chrome\\User Data"
```

---

## English / 中文

## Tech Stack / 技术栈

- **[Python](https://www.python.org/)** - Main programming language / 主要编程语言
- **[Playwright](https://playwright.dev/)** - Browser automation framework / 浏览器自动化框架
- **[Chromium](https://www.chromium.org/)** - Underlying browser engine / 底层浏览器引擎

---

## Project Structure / 项目结构

```
getnote/
├── src/
│   └── get_note.py          # Main program file / 主程序文件
├── data/                    # Export file directory (auto-created) / 导出文件目录（自动创建）
├── config.example.json      # Configuration example / 配置文件示例
├── config.json              # Actual configuration (create yourself) / 实际配置文件（需自行创建）
├── requirements.txt         # Python dependencies / Python 依赖
├── .gitignore              # Git ignore file / Git 忽略文件
├── LICENSE                 # MIT License / MIT 许可证
└── README.md               # Project documentation / 项目文档
```

---

## License / 许可证

This project uses the [MIT License](LICENSE) open source license / 本项目采用 [MIT License](LICENSE) 开源许可证。

```
MIT License

Copyright (c) 2025 GetNote Extractor Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation rights
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

## Contributing / 贡献指南

Contributions are welcome! Please follow these steps / 欢迎贡献代码！请遵循以下步骤：

1. Fork this repository / Fork 本仓库
2. Create feature branch / 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. Commit changes / 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch / 推送到分支 (`git push origin feature/AmazingFeature`)
5. Submit Pull Request / 提交 Pull Request

### Development Guidelines / 开发规范

- Follow PEP 8 code style / 遵循 PEP 8 代码风格
- Add appropriate comments and docstrings / 添加适当的注释和文档字符串
- Ensure code runs normally on all supported platforms / 确保代码在所有支持的平台上正常运行

---

## Disclaimer / 免责声明

This tool is for learning and personal use only. Please comply with Get Notes platform's terms of service, use this tool reasonably, and do not engage in any form of data abuse or commercial use / 本工具仅供学习和个人使用。请遵守 Get 笔记平台的服务条款，合理使用本工具，不要进行任何形式的数据滥用或商业用途。

---

## Contact / 联系方式

- Submit [Issue](https://github.com/YOUR_USERNAME/getnote/issues) / 提交 [Issue](https://github.com/YOUR_USERNAME/getnote/issues)
- Open [Pull Request](https://github.com/YOUR_USERNAME/getnote/pulls) / 发起 [Pull Request](https://github.com/YOUR_USERNAME/getnote/pulls)

---

<div align="center">

**⭐ If this project helps you, please give it a Star! / 如果这个项目对你有帮助，请给个 Star！**

Made with ❤️ by GetNote Extractor Contributors

</div>
