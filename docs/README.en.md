<p align="center">
  <img src="https://img.shields.io/badge/platform-Windows-blue?logo=windows">
  <img src="https://img.shields.io/badge/built%20with-Tauri-FFC131?logo=tauri">
  <img src="https://img.shields.io/badge/size-4.5MB-green">
  <img src="https://img.shields.io/badge/license-MIT-lightgrey">
</p>

# PromptManager

> AI Prompt Manager — a native Windows desktop app to organize, search, and reuse your AI prompt templates.

<p align="center">
  <img src="./poster.png" alt="PromptManager" width="800">
</p>

<p align="center">
    <a href="../README.md">简体中文</a> | English
</p>

## ✨ Features

- **Category tree** — nested categories with add / rename / delete
- **Tag + AI Model filter** — content tags × AI platform (ChatGPT / Claude / Gemini / DeepSeek / Kimi…), one-click sidebar toggle
- **Quick search** — `Ctrl+K` global fuzzy search, arrow-key navigation, Enter to select
- **Variable placeholders** — `{language}` `{style}` `{topic}` supports Chinese names, auto-detected & highlighted, one-click fill before copy, defaults auto-memorized
- **Image support** — paste / drag-drop / button insert, card thumbnails + hover-to-preview, base64 embedded, fully preserved in JSON import/export
- **Bilingual UI** — full Chinese-English switch, categories, buttons, modals all translated
- **Dark / Light theme** — warm cream editorial palette + film grain texture + OLED dark mode
- **Splash screen** — custom cover image with fade-in/out transition
- **Import / Export** — JSON format with prompts, categories, tags, AI models, images — complete data portability
- **Local storage** — IndexedDB, no quota limit, zero cloud dependency

## 📦 Installation

Download `PromptManager_Setup.exe` (~4.5 MB) from the [latest Release](https://github.com/你的用户名/prompt-manager/releases/latest), double-click to install.

> Windows 10/11 ships with WebView2 runtime — no extra dependencies needed.

## 🚀 Usage

| Action | Shortcut |
|--------|----------|
| Quick search | `Ctrl` + `K` |
| Save | `Ctrl` + `S` |
| New prompt | `Ctrl` + `N` |
| Close modal | `Esc` |

**Variables**: write `{variable_name}` anywhere (Chinese supported). The variable bar auto-appears — preset defaults and copy with one click.

**Images**: paste, drag-drop, or click 🖼 in the edit modal. Hover over card thumbnails for 0.5s to preview.

## 🔨 Build from Source

```bash
# Prerequisites: Node.js 18+, Rust 1.70+
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
| Storage | IndexedDB |
| Icons | [Phosphor Icons](https://phosphoricons.com) |
| Fonts | Geist Sans + Newsreader |

## 📄 License

MIT
