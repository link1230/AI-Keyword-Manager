<p align="center">
  <a href="#english"><img src="https://img.shields.io/badge/lang-English-blue" alt="English"></a>
  <a href="#chinese"><img src="https://img.shields.io/badge/lang-中文-red" alt="中文"></a>
  <br>
  <img src="https://img.shields.io/badge/platform-Windows-blue?logo=windows">
  <img src="https://img.shields.io/badge/built%20with-Tauri-FFC131?logo=tauri">
  <img src="https://img.shields.io/badge/size-2.5MB-green">
  <img src="https://img.shields.io/badge/license-MIT-lightgrey">
</p>

---

<h1 id="english">🇬🇧 PromptManager</h1>

> AI Prompt Manager — a native Windows desktop app to organize, search, and reuse your AI prompt templates.

## ✨ Features

- **Category tree** — organize prompts into nested categories
- **Tag + AI Model filter** — double filter: content tags × AI platform (ChatGPT / Claude / Gemini / DeepSeek / Kimi…)
- **Quick search** — `Ctrl+K` or `Ctrl+Shift+P` global fuzzy search with keyboard navigation
- **Variable placeholders** — `{language}` `{style}` `{topic}` — auto-detected, one-click fill before copy
- **Image support** — paste / drag-drop / insert images into prompts (base64)
- **Bilingual UI** — full Chinese-English switch, categories + menus translated
- **Dark / Light theme** — warm editorial monochrome palette + film grain texture
- **Import / Export** — JSON (full data), Markdown, CSV
- **Local-first** — data in localStorage, zero cloud dependency

## 📦 Installation

Download `PromptManager_Setup.exe` (~2.5 MB) from the [latest Release](https://github.com/你的用户名/prompt-manager/releases/latest), double-click to install.

> Windows 10/11 ships with WebView2 runtime — no extra dependencies needed.

## 🚀 Usage

Double-click the desktop shortcut. The window opens ready to use.

| Action | Shortcut |
|--------|----------|
| Quick search | `Ctrl` + `K` |
| Save | `Ctrl` + `S` |
| New prompt | `Ctrl` + `N` |
| Close modal | `Esc` |

**Variables**: write `{variable_name}` anywhere in prompt content (Chinese supported). The variable bar auto-appears — preset defaults and copy with one click.

## 🔨 Build from Source

```bash
git clone https://github.com/你的用户名/prompt-manager.git
cd prompt-manager
npm install
npx tauri build
```

Output: `src-tauri/target/release/bundle/`

## 🛠 Tech Stack

| Layer | Choice |
|-------|--------|
| Desktop shell | [Tauri v2](https://tauri.app) (Rust) |
| UI | Vanilla HTML/CSS/JS |
| Icons | [Phosphor Icons](https://phosphoricons.com) |
| Fonts | Geist Sans + Newsreader |

## 📄 License

MIT

---

<h1 id="chinese">🇨🇳 PromptManager / 提示词管理器</h1>

> AI 提示词管理器 — Windows 原生桌面应用，帮你组织、搜索、复用 AI 提示词模板。

## ✨ 功能

- **分类树** — 按嵌套分类组织提示词
- **标签 + AI 模型双筛选** — 内容标签 × AI 平台（ChatGPT / Claude / Gemini / DeepSeek / Kimi…）
- **快速搜索** — `Ctrl+K` 或 `Ctrl+Shift+P` 全局模糊搜索，键盘导航
- **变量占位符** — `{语言}` `{风格}` `{主题}` — 自动识别，复制前一键填充
- **图片支持** — 粘贴 / 拖拽 / 插入图片到提示词（base64）
- **中英双语** — 全界面切换，分类菜单同步翻译
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
| 界面 | 原生 HTML/CSS/JS |
| 图标 | [Phosphor Icons](https://phosphoricons.com) |
| 字体 | Geist Sans + Newsreader |

## 📄 许可证

MIT
