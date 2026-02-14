<div align="center">

# 📝 GetNote Extractor | Get笔记提取器

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Playwright](https://img.shields.io/badge/Playwright-Latest-orange.svg)

**A Python automation tool to export Get Notes articles locally**
**基于 Playwright 的自动化工具，导出 Get 笔记文章到本地**

[Features](#features) • [Quick Start](#quick-start) • [Troubleshooting](#troubleshooting)

---

**⭐ If this project helps you, please give it a Star! 如果这个项目对你有帮助，请给个 Star！**

</div>

---

## 📖 About | 关于

GetNote Extractor is a Python automation tool built with Playwright that helps you export articles from Get Notes (biji.com) to your local computer. Simple to use - no programming knowledge required!

Get笔记提取器是一个基于 Playwright 开发的 Python 自动化工具，帮助你将 Get 笔记（biji.com）的文章导出到本地电脑。简单易用 - 无需编程知识！

---

## 🚀 Quick Links | 快速链接

| English | 中文 |
|---------|------|
| [English Documentation](#english-documentation) | [中文文档](#中文文档) |

---

<details>
<summary><h2 id="english-documentation">📘 English Documentation</h2></summary>

### 🎯 Project Overview

GetNote Extractor automatically exports your Get Notes articles to local text files by reusing your logged-in Chrome browser session. No manual copy-paste needed!

#### Key Features

- ✅ **Auto Login Reuse** - Uses Chrome's existing session, no need to log in again
- 🎯 **Precise Extraction** - CSS selectors accurately locate article titles and content
- 🌍 **Cross-Platform** - Works on Windows, macOS, and Linux
- ⚙️ **Flexible Configuration** - Customize export paths and selectors via JSON
- 🔒 **Secure & Local** - All data stays on your computer, nothing uploaded to cloud

#### Who Should Use This

Perfect for users who need to:
- Backup Get Notes articles locally
- Archive important content
- Export notes without manual copy-paste
- Automate article extraction workflow

### 📋 System Requirements

- **Python**: 3.8 or higher
- **Browser**: Google Chrome (must be installed)
- **Operating System**:
  - Windows 10/11
  - macOS 10.15+
  - Linux (Ubuntu 20.04+, Debian 10+, etc.)

### 🔧 Installation

#### 1. Clone the Repository

```bash
git clone https://github.com/perpetualhui/getnote-extractor.git
cd getnote-extractor
```

#### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 3. Configure Settings

```bash
cp config.example.json config.json
```

Edit `config.json` and fill in your Chrome user data directory path (see [Configuration](#configuration) below).

### ⚙️ Configuration

#### config.json File

```json
{
  "getnote_url": "https://www.biji.com/chat",
  "chrome_user_data_dir": "C:\\Users\\YOUR_USERNAME\\AppData\\Local\\Google\\Chrome\\User Data",
  "export_path": "./data/getnote_articles.txt",
  "article_selector": ".article-content",
  "title_selector": ".article-title"
}
```

#### Parameters

| Parameter | Description | Example |
|-----------|-------------|----------|
| `getnote_url` | Get Notes official website URL | `"https://www.biji.com/chat"` |
| `chrome_user_data_dir` | Chrome user data directory path | Windows: `C:\Users\YOUR_USERNAME\AppData\Local\Google\Chrome\User Data`<br>macOS: `~/Library/Application Support/Google/Chrome`<br>Linux: `~/.config/google-chrome` |
| `export_path` | Local file path for exported articles | `"./data/articles.txt"` |
| `article_selector` | CSS selector for article content | `".article-content"` |
| `title_selector` | CSS selector for article title | `".article-title"` |

#### How to Find Chrome User Data Directory

**Windows:**
1. Open Chrome browser
2. Type in address bar: `chrome://version`
3. Look for "Profile Path" entry
4. Copy the path (remove final `Default` or profile folder, keep only `User Data`)

**macOS / Linux:**
```bash
echo ~/Library/Application\ Support/Google/Chrome  # macOS
echo ~/.config/google-chrome                       # Linux
```

### 🚀 Usage

#### Run the Script

```bash
python src/get_note.py
```

#### Usage Flow

1. **Before First Run**: Ensure you're logged into Get Notes in Chrome browser
2. **Run Script**: Execute the command above
3. **Close Chrome**: Script will prompt you to close all Chrome windows, wait 3 seconds
4. **Auto Extract**: Script opens browser, visits page, extracts content automatically
5. **View Results**: Text file generated at configured path

#### Sample Output

```
==================================================
  Get Note Content Extractor v1.0.0
==================================================
✓ Found Chrome Browser: C:\Program Files\Google\Chrome\Application\chrome.exe

⚠️  Please ensure all Chrome windows are closed
Continuing in 3 seconds...

Visiting: https://www.biji.com/chat
Waiting for content to load...

✅ Extraction Successful!
📄 Title: Sample Article Title
💾 Export Path: ./data/getnote_articles.txt
```

### 🚨 Troubleshooting

#### 1. ModuleNotFoundError: No module named 'playwright'

**Error**:
```
ModuleNotFoundError: No module named 'playwright'
```

**Solution**:
```bash
# Confirm Python environment
python --version

# Install Playwright
python -m pip install --upgrade pip
python -m pip install playwright --force-reinstall

# Verify installation
python -c "import playwright; print('✅ Installation successful')"
```

#### 2. BrowserType.launch: Executable doesn't exist

**Error**:
```
playwright._impl._errors.Error: BrowserType.launch: Executable doesn't exist
```

**Solution**:
```bash
# Install Playwright browser driver
python -m playwright install chrome
```

**Note**: This project includes automatic system Chrome path detection, manual specification usually not needed.

#### 3. net::ERR_NAME_NOT_RESOLVED

**Error**:
```
playwright._impl._errors.Error: Page.goto: net::ERR_NAME_NOT_RESOLVED
```

**Solution**:
1. Manually verify URL works in browser
2. Check URL format in `config.json`:

```json
// ❌ Wrong
"getnote_url": "www.biji.com"

// ✅ Correct
"getnote_url": "https://www.biji.com/chat"
```

#### 4. User data directory already in use

**Error**:
```
Error: User data directory is already in use
```

**Solution**:
1. Close all Chrome windows
2. Check for remaining Chrome processes:
```bash
tasklist | findstr chrome  # Windows
ps aux | grep chrome     # macOS/Linux
```
3. Terminate processes if needed:
```bash
taskkill /F /IM chrome.exe  # Windows
killall Chrome             # macOS
```

#### 5. CSS Selector Positioning Failure

**Error**:
```
TimeoutError: waiting for selector ".article-content" failed
```

**Solution**:
1. Open Get Notes page in Chrome
2. Press F12 to open Developer Tools
3. Click Element Picker (arrow icon in top left)
4. Click article content on page
5. View HTML structure in Elements panel
6. Copy correct class or id
7. Update selector in `config.json`:

```json
{
  "article_selector": ".actual-content-class",
  "title_selector": ".actual-title-class"
}
```

### 🏗️ Project Structure

```
getnote-extractor/
├── src/
│   └── get_note.py          # Main program
├── data/                    # Export directory (auto-created)
├── config.example.json      # Configuration example
├── config.json              # Your configuration (create this)
├── requirements.txt         # Python dependencies
├── .gitignore              # Git ignore file
├── LICENSE                 # MIT License
└── README.md               # This file
```

### 🛠️ Tech Stack

- **[Python](https://www.python.org/)** - Main programming language
- **[Playwright](https://playwright.dev/)** - Browser automation framework
- **[Chromium](https://www.chromium.org/)** - Underlying browser engine

### 📄 License

This project is licensed under the [MIT License](LICENSE).

### 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork this repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Submit Pull Request

### 📧 Contact

- Submit [Issue](https://github.com/perpetualhui/getnote-extractor/issues)
- Open [Pull Request](https://github.com/perpetualhui/getnote-extractor/pulls)

### ⚠️ Disclaimer

This tool is for learning and personal use only. Please comply with Get Notes platform's terms of service, use this tool reasonably, and do not engage in any form of data abuse or commercial use.

</details>

---

<details>
<summary><h2 id="中文文档">📙 中文文档</h2></summary>

### 🎯 项目简介

Get笔记提取器是一个基于 Playwright 开发的 Python 自动化工具，帮助你将 Get 笔记（biji.com）的文章自动导出到本地文本文件。简单易用 - 无需编程知识！

#### 核心功能

- ✅ **登录状态自动复用** - 直接使用 Chrome 已登录会话，无需重复登录
- 🎯 **精准内容提取** - 使用 CSS 选择器精确定位文章标题和正文
- 🌍 **全平台支持** - 兼容 Windows、macOS 和 Linux
- ⚙️ **灵活自定义配置** - 通过 JSON 文件自定义导出路径和选择器
- 🔒 **本地安全运行** - 所有数据保留在你的电脑上，不会上传到云端

#### 适合谁用

完美适合以下用户：
- 需要备份 Get 笔记文章到本地
- 归档重要内容
- 无需手动复制粘贴导出笔记
- 自动化文章提取工作流程

### 📋 系统要求

- **Python**: 3.8 或更高版本
- **浏览器**: Google Chrome（必须已安装）
- **操作系统**:
  - Windows 10/11
  - macOS 10.15+
  - Linux (Ubuntu 20.04+, Debian 10+, 等)

### 🔧 安装步骤

#### 1. 克隆项目

```bash
git clone https://github.com/perpetualhui/getnote-extractor.git
cd getnote-extractor
```

#### 2. 安装依赖

```bash
pip install -r requirements.txt
```

#### 3. 配置参数

```bash
cp config.example.json config.json
```

编辑 `config.json` 文件，填入你的 Chrome 用户数据目录路径（详见[配置说明](#配置说明-1)）。

### ⚙️ 配置说明

#### config.json 配置文件

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

#### 如何找到 Chrome 用户数据目录

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

### 🚀 使用方法

#### 运行脚本

```bash
python src/get_note.py
```

#### 使用流程

1. **首次运行前**：确保已在 Chrome 浏览器中登录 Get 笔记账号
2. **运行脚本**：执行上述命令
3. **关闭 Chrome**：脚本会提示关闭所有 Chrome 窗口，关闭后等待 3 秒
4. **自动提取**：脚本自动打开浏览器、访问页面、提取内容
5. **查看结果**：导出完成后，会在配置的路径生成文本文件

#### 示例输出

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

### 🚨 故障排查

#### 1. ModuleNotFoundError: No module named 'playwright'

**错误信息**:
```
ModuleNotFoundError: No module named 'playwright'
```

**解决方案**:
```bash
# 确认 Python 环境
python --version

# 安装 Playwright
python -m pip install --upgrade pip
python -m pip install playwright --force-reinstall

# 验证安装
python -c "import playwright; print('✅ 安装成功')"
```

#### 2. BrowserType.launch: Executable doesn't exist

**错误信息**:
```
playwright._impl._errors.Error: BrowserType.launch: Executable doesn't exist
```

**解决方案**:
```bash
# 安装 Playwright 浏览器驱动
python -m playwright install chrome
```

**注意**：本项目已内置自动查找系统 Chrome 路径的功能，一般无需手动指定。

#### 3. net::ERR_NAME_NOT_RESOLVED

**错误信息**:
```
playwright._impl._errors.Error: Page.goto: net::ERR_NAME_NOT_RESOLVED
```

**解决方案**:
1. 手动在浏览器中验证 URL 可以正常访问
2. 检查 `config.json` 中的 URL 格式：

```json
// ❌ 错误
"getnote_url": "www.biji.com"

// ✅ 正确
"getnote_url": "https://www.biji.com/chat"
```

#### 4. 用户数据目录被占用

**错误信息**:
```
Error: User data directory is already in use
```

**解决方案**:
1. 关闭所有 Chrome 窗口
2. 检查是否有残留的 Chrome 进程：
```bash
tasklist | findstr chrome  # Windows
ps aux | grep chrome     # macOS/Linux
```
3. 如需结束进程：
```bash
taskkill /F /IM chrome.exe  # Windows
killall Chrome             # macOS
```

#### 5. CSS 选择器定位失败

**错误信息**:
```
TimeoutError: waiting for selector ".article-content" failed
```

**解决方案**:
1. 在 Chrome 中打开 Get 笔记页面
2. 按 F12 打开开发者工具
3. 点击"元素选择器"（左上角箭头图标）
4. 点击页面上的文章内容
5. 查看 Elements 面板中的 HTML 结构
6. 复制正确的 class 或 id
7. 在 `config.json` 中更新选择器：

```json
{
  "article_selector": ".实际内容类名",
  "title_selector": ".实际标题类名"
}
```

### 🏗️ 项目结构

```
getnote-extractor/
├── src/
│   └── get_note.py          # 主程序
├── data/                    # 导出目录（自动创建）
├── config.example.json      # 配置示例
├── config.json              # 你的配置文件（需创建）
├── requirements.txt         # Python 依赖
├── .gitignore              # Git 忽略文件
├── LICENSE                 # MIT 许可证
└── README.md               # 本文件
```

### 🛠️ 技术栈

- **[Python](https://www.python.org/)** - 主要编程语言
- **[Playwright](https://playwright.dev/)** - 浏览器自动化框架
- **[Chromium](https://www.chromium.org/)** - 底层浏览器引擎

### 📄 许可证

本项目采用 [MIT License](LICENSE) 开源许可证。

### 🤝 贡献指南

欢迎贡献代码！请遵循以下步骤：

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 提交 Pull Request

### 📧 联系方式

- 提交 [Issue](https://github.com/perpetualhui/getnote-extractor/issues)
- 发起 [Pull Request](https://github.com/perpetualhui/getnote-extractor/pulls)

### ⚠️ 免责声明

本工具仅供学习和个人使用。请遵守 Get 笔记平台的服务条款，合理使用本工具，不要进行任何形式的数据滥用或商业用途。

</details>

---

<div align="center">

**🎉 Thank you for using GetNote Extractor! 感谢使用 Get 笔记提取器！**

Made with ❤️ by [perpetualhui](https://github.com/perpetualhui)

</div>
