<p align="center">
  <img src="https://img.shields.io/badge/platform-Windows-blue?logo=windows" alt="Windows">
  <img src="https://img.shields.io/badge/built%20with-Tauri-FFC131?logo=tauri" alt="Tauri">
  <img src="https://img.shields.io/badge/size-2.5MB-green" alt="Size">
  <img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="License">
</p>

# PromptManager / 提示词管理器

> AI 提示词管理器 — 本地桌面应用，帮你组织、搜索、复用 AI 提示词模板。  
> AI Prompt Manager — a native desktop app to organize, search, and reuse your AI prompt templates.

<p align="center">
  <b><a href="#-features">Features</a></b> ·
  <b><a href="#-安装">安装</a></b> ·
  <b><a href="#-installation">Install</a></b> ·
  <b><a href="#-usage">Usage</a></b> ·
  <b><a href="#-build">Build</a></b>
</p>

---

## ✨ Features

| | |
|---|---|
| 📁 **Category tree** | Organize prompts into nested categories |
| 🏷️ **Tag + AI Model filter** | Double filter system: content tags + AI platform (ChatGPT / Claude / Gemini / DeepSeek…) |
| 🔍 **Quick search** | `Ctrl+K` or `Ctrl+Shift+P` global fuzzy search with keyboard navigation |
| 🔧 **Variable placeholders** | `{language}` `{style}` `{topic}` — auto-detected, one-click fill before copy |
| 🖼️ **Image support** | Paste / drag-drop / insert images into prompts, stored as base64 |
| 🌐 **China-English bilingual** | Full UI switch, categories + menus all translated |
| 🌓 **Dark / Light theme** | Warm editorial monochrome palette + film grain texture |
| 📥 **Import / Export** | JSON (full data), Markdown, CSV |
| 💾 **Local-first** | All data in browser localStorage, zero cloud dependency |

## ✨ 功能

| | |
|---|---|
| 📁 **分类树** | 按嵌套分类组织提示词 |
| 🏷️ **标签+AI模型双筛选** | 内容标签 × AI 平台（ChatGPT / Claude / Gemini / DeepSeek…） |
| 🔍 **快速搜索** | `Ctrl+K` 或 `Ctrl+Shift+P` 全局模糊搜索，键盘导航 |
| 🔧 **变量占位符** | `{语言}` `{风格}` `{主题}` — 自动识别，复制前一键填充 |
| 🖼️ **图片支持** | 粘贴 / 拖拽 / 插入图片到提示词，base64 存储 |
| 🌐 **中英双语** | 全界面切换，分类菜单同步翻译 |
| 🌓 **深色/浅色主题** | 暖色调 editorial 配色 + 胶片颗粒纹理 |
| 📥 **导入/导出** | JSON（完整数据）、Markdown、CSV |
| 💾 **纯本地** | 数据存浏览器 localStorage，无需任何云服务 |

---

## 📦 安装 / Installation

下载 [最新 Release](https://github.com/你的用户名/prompt-manager/releases/latest) 中的 `PromptManager_Setup.exe`（~2.5 MB），双击安装即可。

Download `PromptManager_Setup.exe` (~2.5 MB) from the [latest Release](https://github.com/你的用户名/prompt-manager/releases/latest), double-click to install.

> ✅ Windows 10 / 11 自带 WebView2 运行时，无需额外安装依赖。  
> ✅ Windows 10/11 ships with WebView2 runtime — no extra dependencies.

---

## 🚀 Usage / 使用

```
双击桌面快捷方式 → 窗口打开即用
```

| 操作 | 快捷键 |
|------|--------|
| 快速搜索 | `Ctrl` + `K` |
| 保存 | `Ctrl` + `S` |
| 新建提示词 | `Ctrl` + `N` |
| 关闭弹窗 | `Esc` |

**变量用法**：在提示词正文中写 `{变量名}`（支持中文），编辑器底部自动出现填充栏，预设默认值后一键复制。

**Variable usage**: write `{variable_name}` anywhere in the prompt content (Chinese supported). The variable bar auto-appears at the bottom — set defaults and copy with one click.

---

## 🔨 Build from Source / 从源码构建

```bash
# Prerequisites: Node.js 18+, Rust 1.70+
git clone https://github.com/你的用户名/prompt-manager.git
cd prompt-manager
npm install
npx tauri build
```

Output in `src-tauri/target/release/bundle/`.

---

## 🛠 Tech Stack / 技术栈

| Layer | Choice |
|-------|--------|
| Desktop shell | [Tauri v2](https://tauri.app) (Rust) |
| UI | Vanilla HTML/CSS/JS (zero framework) |
| Icons | [Phosphor Icons](https://phosphoricons.com) |
| Fonts | Geist Sans + Newsreader (serif) |
| Data | localStorage + JSON import/export |

---

## 📄 License

MIT
