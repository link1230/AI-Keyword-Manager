<p align="center">
  <img src="https://img.shields.io/badge/platform-Windows-blue?logo=windows">
  <img src="https://img.shields.io/badge/built%20with-Tauri-FFC131?logo=tauri">
  <img src="https://img.shields.io/badge/size-2.5MB-green">
  <img src="https://img.shields.io/badge/license-MIT-lightgrey">
</p>

# PromptManager

> AI Prompt Manager — a native Windows desktop app to organize, search, and reuse your AI prompt templates.

<p align="center">
    <a href="../README.md">简体中文</a> | English
</p>

## ✨ Features

- **Category tree** — organize prompts into nested categories
- **Tag + AI Model filter** — double filter: content tags × AI platform (ChatGPT / Claude / Gemini / DeepSeek / Kimi…)
- **Quick search** — `Ctrl+K` or `Ctrl+Shift+P` global fuzzy search with keyboard navigation
- **Variable placeholders** — `{language}` `{style}` `{topic}` — auto-detected, one-click fill before copy
- **Image support** — paste / drag-drop / insert images into prompts (base64)
- **Bilingual UI** — full Chinese-English switch, categories + menus translated
- **Dark / Light theme** — warm editorial monochrome palette + film grain texture
- **Import / Export** — JSON (full data), Markdown, CSV
- **Local-first** — data stored in browser localStorage, zero cloud dependency

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
| UI | Vanilla HTML / CSS / JS |
| Icons | [Phosphor Icons](https://phosphoricons.com) |
| Fonts | Geist Sans + Newsreader |

## 📄 License

MIT
