<p align="center">
  <img src="https://img.shields.io/badge/platform-Windows-blue?logo=windows">
  <img src="https://img.shields.io/badge/built%20with-Tauri-FFC131?logo=tauri">
  <img src="https://img.shields.io/badge/size-2.5MB-green">
  <img src="https://img.shields.io/badge/license-MIT-lightgrey">
</p>

# PromptManager / 提示词管理器

> AI 提示词管理器 — Windows 原生桌面应用，帮你组织、搜索、复用 AI 提示词模板。

<p align="center">
  <img src="./docs/poster.png" alt="PromptManager" width="800">
</p>

<p align="center">
    简体中文 | <a href="./docs/README.en.md">English</a>
</p>

## ✨ 功能

- **分类树** — 按嵌套分类组织提示词
- **标签 + AI 模型双筛选** — 内容标签 × AI 平台（ChatGPT / Claude / Gemini / DeepSeek / Kimi…）
- **快速搜索** — `Ctrl+K` 或 `Ctrl+Shift+P` 全局模糊搜索，键盘导航
- **变量占位符** — `{语言}` `{风格}` `{主题}` — 自动识别，复制前一键填充
- **图片支持** — 粘贴 / 拖拽 / 插入图片到提示词（base64）
- **中英双语界面** — 全界面切换，分类菜单同步翻译
- **深色/浅色主题** — 暖色调 editorial 配色 + 胶片颗粒纹理
- **导入/导出** — JSON（完整数据）、Markdown、CSV
- **纯本地** — 数据存浏览器 localStorage，无需任何云服务

## 📦 安装

下载 [最新 Release](https://github.com/你的用户名/prompt-manager/releases/latest) 中的 `PromptManager_Setup.exe`（约 2.5 MB），双击安装。

> Windows 10 / 11 自带 WebView2 运行时，无需额外安装依赖。

## 🚀 使用

双击桌面快捷方式，窗口打开即用。

| 操作 | 快捷键 |
|------|--------|
| 快速搜索 | `Ctrl` + `K` |
| 保存 | `Ctrl` + `S` |
| 新建提示词 | `Ctrl` + `N` |
| 关闭弹窗 | `Esc` |

**变量用法**：在提示词正文中写 `{变量名}`（支持中文），编辑器底部自动出现填充栏，预设默认值后一键复制。

## 🔨 从源码构建

```bash
git clone https://github.com/你的用户名/prompt-manager.git
cd prompt-manager
npm install
npx tauri build
```

构建产物：`src-tauri/target/release/bundle/`

## 🛠 技术栈

| 层 | 选型 |
|----|------|
| 桌面壳 | [Tauri v2](https://tauri.app)（Rust） |
| 界面 | 原生 HTML / CSS / JS |
| 图标 | [Phosphor Icons](https://phosphoricons.com) |
| 字体 | Geist Sans + Newsreader |

## 📄 许可证

MIT
