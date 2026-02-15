# GetNote Extractor

<div align="center">

**Get笔记知识库批量提取工具**

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://badge.fuchsia.io/badge/License-MIT-green.svg)
![Playwright](https://img.shields.io/badge/Playwright-Latest-orange.svg)

[功能特点](#功能特点) &centerdot; [快速开始](#快速开始) &centerdot; [使用方法](#使用方法) &centerdot; [常见问题](#常见问题)

</div>

---

## 功能特点

- **并行提取** - 多线程并发，默认3个并发，速度提升3-5倍
- **断点续传** - 自动跳过已提取的文章，支持随时中断和继续
- **Markdown 输出** - 保存为结构化的 Markdown 文件，便于阅读和管理
- **自动分页** - 自动处理所有页面，无需手动翻页
- **智能命名** - 使用博主名称命名文件夹，自动处理重名冲突
- **优雅停止** - Ctrl+C 等待当前批次完成后安全退出
- **实时统计** - 显示提取进度、速度和用时统计

---

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
playwright install chrome
```

### 2. 配置

```bash
cp config.example.json config.json
```

编辑 `config.json`，填入 Chrome 用户数据目录：

**Windows:**
```json
{
  "chrome_user_data_dir": "C:\\Users\\你的用户名\\AppData\\Local\\Google\\Chrome\\User Data"
}
```

**macOS:**
```json
{
  "chrome_user_data_dir": "/Users/你的用户名/Library/Application Support/Google/Chrome"
}
```

**Linux:**
```json
{
  "chrome_user_data_dir": "/home/你的用户名/.config/google-chrome"
}
```

### 3. 获取知识库 URL

1. 在 Get笔记 APP 中订阅想提取的博主
2. 浏览器打开 https://www.biji.com
3. 进入博主的知识库页面
4. 复制完整的浏览器地址：

```
https://www.biji.com/subject/QYARpjM0/DEFAULT?followId=785142&followName=博主名称
```

### 4. 运行

```bash
python src/get_note.py "https://www.biji.com/subject/QYARpjM0/DEFAULT?followId=...&followName=..."
```

首次运行需要在浏览器中登录 Get 笔记账号。

---

## 使用方法

### 基本用法

```bash
# 使用完整 URL（推荐，自动以博主名命名文件夹）
python src/get_note.py "知识库URL"

# 或者只使用知识库 ID
python src/get_note.py ABC123
```

### 高级用法

```bash
# 自定义输出目录
python src/get_note.py "URL" "我的文件夹"

# 限制提取数量（只提取前 50 篇）
python src/get_note.py "URL" "输出" 0 50

# 调整并发数（5 个并发，更快）
python src/get_note.py "URL" "输出" 0 0 5

# 限制页数
python src/get_note.py "URL" "输出" 3
```

### 参数说明

```bash
python src/get_note.py <知识库URL或ID> [输出目录] [最大页数] [最大文章数] [并发数]
```

| 参数 | 说明 | 默认值 |
|------|------|--------|
| 知识库URL或ID | 必需 | - |
| 输出目录 | 可选 | 自动从URL提取 |
| 最大页数 | 可选 | 0（全部） |
| 最大文章数 | 可选 | 0（全部） |
| 并发数 | 可选 | 3 |

---

## 输出结构

```
博主名称/
├── 001_第一篇文章.md
├── 002_第二篇文章.md
└── ...
```

每篇文章包含：
- 文章标题
- 原始链接
- 完整正文内容（Markdown 格式）

---

## 性能参考

| 并发数 | 速度 | 适用场景 |
|--------|------|----------|
| 1 | ~10 篇/分钟 | 网络不稳定 |
| 3（默认） | ~25-30 篇/分钟 | 推荐设置 |
| 5 | ~40-50 篇/分钟 | 追求速度 |

---

## 停止和继续

**停止提取**：按 `Ctrl+C`，工具会等待当前批次完成后安全退出

**继续提取**：重新运行相同的命令，工具会自动跳过已提取的文章

---

## 常见问题

### Chrome 用户数据目录在哪？

**Windows:**
1. 打开 Chrome，地址栏输入 `chrome://version`
2. 复制"个人资料路径"
3. 删除最后的 `Default` 或其他配置文件夹名
4. 只保留到 `User Data`

**macOS / Linux:**
```bash
echo ~/Library/Application\ Support/Google/Chrome  # macOS
echo ~/.config/google-chrome                       # Linux
```

### 提示"用户数据目录被占用"？

1. 关闭所有 Chrome 窗口
2. 检查任务管理器，结束所有 Chrome 进程

### 提取速度慢？

- 检查网络连接
- 确保 Chrome 已登录 Get 笔记
- 尝试调整并发数

---

## 系统要求

- Python 3.8+
- Google Chrome 浏览器
- Windows 10/11、macOS 10.15+ 或 Linux

---

## 技术栈

- Python
- Playwright
- Chromium

---

## 许可证

MIT License - 仅供学习交流使用

---

<div align="center">

Made with ❤️ by [perpetualhui](https://github.com/perpetualhui)

</div>
