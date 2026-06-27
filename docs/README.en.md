<p align="center">
  <img src="https://img.shields.io/badge/platform-Windows-blue?logo=windows">
  <img src="https://img.shields.io/badge/built%20with-Tauri-FFC131?logo=tauri">
  <img src="https://img.shields.io/badge/size-4.5MB-green">
  <img src="https://img.shields.io/badge/license-MIT-lightgrey">
</p>

<h1 align="center">PromptManager</h1>

<p align="center"><i>AI Prompt Manager — a native Windows desktop app to organize, search, and reuse your AI prompt templates.</i></p>

<p align="center">
  <img src="./poster.png" alt="PromptManager" width="800">
</p>

<p align="center">
  <a href="../README.md">简体中文</a> &nbsp;|&nbsp; <b>English</b>
</p>

---

## Features

<table>
<tr>
<td width="50%">

### Organize
- **Category tree** — nested categories, add / rename / delete
- **Tag filter** — content tags, one-click sidebar toggle
- **AI Model labels** — ChatGPT / Claude / Gemini / DeepSeek / Kimi…

</td>
<td width="50%">

### Search
- **Quick search** — `Ctrl+K` global fuzzy search
- **Keyboard nav** — arrow keys to select, Enter to open
- **Full-text** — title, content, and tags searched simultaneously

</td>
</tr>
<tr>
<td>

### Compose
- **Variables** — `{language}` `{style}` auto-detected and highlighted
- **One-click fill** — variable panel before copy, defaults auto-memorized
- **Images** — paste / drag-drop / insert, card thumbnails + hover preview

</td>
<td>

### Experience
- **Bilingual UI** — full Chinese-English switch
- **Themes** — warm cream editorial + OLED dark mode
- **Splash screen** — custom cover + fade transition
- **Import / Export** — JSON, full data including images
- **Storage** — IndexedDB, no quota limit

</td>
</tr>
</table>

## Installation

Download `PromptManager_Setup.exe` (~4.5 MB) from the [latest Release](https://github.com/你的用户名/prompt-manager/releases/latest), double-click to install.

> Windows 10/11 ships with WebView2 — no extra dependencies.

## Shortcuts

| Action | Keys |
|--------|------|
| Quick search | `Ctrl` + `K` |
| Save | `Ctrl` + `S` |
| New prompt | `Ctrl` + `N` |
| Close modal | `Esc` |

## Build from Source

```bash
# Prerequisites: Node.js 18+ / Rust 1.70+
git clone https://github.com/你的用户名/prompt-manager.git
cd prompt-manager
npm install
npx tauri build
```

## Tech Stack

| Layer | Choice |
|-------|--------|
| Desktop | [Tauri v2](https://tauri.app) |
| UI | HTML / CSS / JS |
| Storage | IndexedDB |
| Icons | [Phosphor Icons](https://phosphoricons.com) |
| Fonts | Geist Sans + Newsreader |

## License

MIT
