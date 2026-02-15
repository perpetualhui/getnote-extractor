# Get 笔记提取工具 v2.0 - 快速使用指南

## 一分钟快速上手

### 1. 安装依赖

```bash
# 进入项目目录
cd getnote

# 安装 Python 依赖
pip install -r requirements.txt

# 安装 Playwright 浏览器驱动
python -m playwright install chrome
```

### 2. 配置 Chrome 路径

```bash
# 复制配置文件
cp config.example.json config.json

# 编辑 config.json，填入你的 Chrome 用户数据目录
```

**Windows 用户：**
1. 打开 Chrome，地址栏输入 `chrome://version`
2. 复制"个人资料路径"，删除最后的 `Default`
3. 粘贴到 `config.json` 的 `chrome_user_data_dir` 字段

**示例：**
```json
{
  "chrome_user_data_dir": "C:\\Users\\你的用户名\\AppData\\Local\\Google\\Chrome\\User Data"
}
```

### 3. 获取知识库 URL

1. 在 Get 笔记 APP 中订阅想提取的博主
2. 在浏览器打开 https://www.biji.com
3. 进入已订阅博主的知识库页面
4. 复制完整的浏览器地址栏 URL

**示例 URL：**
```
https://www.biji.com/subject/QYARpjM0/DEFAULT?followId=785142&followName=博主名称
```

### 4. 运行提取工具

```bash
# 使用完整 URL（推荐，自动以博主名命名文件夹）
python src/get_note.py "https://www.biji.com/subject/QYARpjM0/DEFAULT?followId=...&followName=..."

# 或者只使用知识库 ID
python src/get_note.py QYARpjM0
```

### 5. 首次运行

1. 确保 Chrome 浏览器已关闭
2. 运行上述命令
3. 等待 3 秒
4. 浏览器自动打开
5. 如未登录，在浏览器中登录 Get 笔记
6. 登录后自动开始提取

### 6. 查看结果

提取的文章会保存在以博主名称命名的文件夹中，每篇文章一个 Markdown 文件：

```
博主名称/
├── 001_第一篇文章标题.md
├── 002_第二篇文章标题.md
└── ...
```

## 高级用法

### 自定义输出目录

```bash
python src/get_note.py "URL" "我的自定义文件夹"
```

### 限制提取数量

```bash
# 只提取前 50 篇文章
python src/get_note.py "URL" "输出目录" 0 50
```

### 调整并发数（速度）

```bash
# 使用 5 个并发线程（更快，但可能被限流）
python src/get_note.py "URL" "输出目录" 0 0 5
```

### 限制提取页数

```bash
# 只提取前 3 页
python src/get_note.py "URL" "输出目录" 3
```

## 常用操作

### 停止提取

按 `Ctrl+C`，工具会等待当前批次完成后安全退出

### 继续提取

重新运行相同的命令，工具会自动跳过已提取的文章

### 查看进度

工具会实时显示：
- 当前处理的文章序号
- 已保存数量
- 平均速度（篇/分钟）

## 性能参考

| 并发数 | 速度 | 适用场景 |
|--------|------|----------|
| 1 | ~10 篇/分钟 | 网络不稳定或怕被限流 |
| 3（默认） | ~25-30 篇/分钟 | 推荐设置 |
| 5 | ~40-50 篇/分钟 | 网络好，追求速度 |

## 注意事项

1. ✅ 首次使用需要在浏览器中登录 Get 笔记
2. ✅ 需要在 Get 笔记 APP 中订阅目标知识库
3. ✅ 运行前请关闭所有 Chrome 窗口
4. ⚠️ 并发数不建议超过 5，避免被限流
5. ⚠️ 提取过程中请保持网络稳定

## 故障排查

### 问题：找不到 Chrome 浏览器

**解决方案：**
```bash
# Windows: 确保 Chrome 已安装到默认路径
# 或手动安装 Playwright 浏览器
python -m playwright install chrome
```

### 问题：用户数据目录被占用

**解决方案：**
1. 关闭所有 Chrome 窗口
2. 检查任务管理器，结束所有 Chrome 进程

### 问题：提取速度慢

**解决方案：**
1. 检查网络连接
2. 确保已登录 Get 笔记
3. 尝试降低并发数

## 完整参数说明

```bash
python src/get_note.py <知识库URL或ID> [输出目录] [最大页数] [最大文章数] [并发数]
```

| 参数 | 说明 | 默认值 | 示例 |
|------|------|--------|------|
| 知识库URL或ID | 必需 | - | `https://www.biji.com/subject/ABC/DEFAULT` 或 `ABC` |
| 输出目录 | 可选 | 自动从URL提取 | `"我的文件夹"` |
| 最大页数 | 可选 | 0（全部） | `3`（只提取前3页） |
| 最大文章数 | 可选 | 0（全部） | `50`（只提取前50篇） |
| 并发数 | 可选 | 3 | `5`（5个并发） |

## 示例命令

```bash
# 基本用法
python src/get_note.py https://www.biji.com/subject/ABC123/DEFAULT

# 自定义输出目录
python src/get_note.py https://www.biji.com/subject/ABC123/DEFAULT "我的笔记"

# 只提取前 100 篇，使用 5 个并发
python src/get_note.py https://www.biji.com/subject/ABC123/DEFAULT "我的笔记" 0 100 5

# 只提取前 2 页
python src/get_note.py ABC123 "输出" 2

# 使用 ID 而不是完整 URL
python src/get_note.py ABC123
```

祝使用愉快！🎉
