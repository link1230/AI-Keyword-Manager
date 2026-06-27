<p align="center">
  <img src="https://img.shields.io/badge/platform-Windows-blue?logo=windows">
  <img src="https://img.shields.io/badge/built%20with-Tauri-FFC131?logo=tauri">
  <img src="https://img.shields.io/badge/size-4.5MB-green">
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

- **分类树** — 嵌套分类，支持新增 / 改名 / 删除
- **标签 + AI 模型双筛选** — 内容标签 × AI 平台（ChatGPT / Claude / Gemini / DeepSeek / Kimi…），侧边栏一键切换
- **快速搜索** — `Ctrl+K` 全局模糊搜索，键盘上下键导航，回车选中
- **变量占位符** — `{语言}` `{风格}` `{主题}` 中文变量名原生支持，自动识别高亮，复制前一键填充，默认值自动记忆
- **图片支持** — 粘贴 / 拖拽 / 按钮插入图片，卡片缩略图 + 悬停放大预览，base64 内嵌，JSON 导入导出完整保留
- **中英双语界面** — 全界面一键切换，分类、按钮、弹窗全部翻译
- **深色 / 浅色主题** — 暖奶油色 editorial 风格 + 胶片颗粒纹理 + OLED 深色模式
- **启动封面** — 自定义封面图 + 淡入淡出过渡动画
- **导入 / 导出** — JSON 格式，含提示词、分类、标签、AI 模型、图片全部数据
- **本地存储** — IndexedDB，无容量限制，零云服务依赖

## 📦 安装

<<<<<<< HEAD
下载 [最新 Release](https://github.com/你的用户名/prompt-manager/releases/latest) 中的 `PromptManager_Setup.exe`（约 4.5 MB），双击安装。
=======
下载 [最新 Release](https://github.com/link1230/AI-Keyword-Manager/releases) 中的 `PromptManager_Setup.exe`（约 4.5 MB），双击安装。
>>>>>>> cff2a87479ec89698fc7df1194bafdf6eab7feaf

> Windows 10 / 11 自带 WebView2 运行时，无需额外安装依赖。

## 🚀 使用

| 操作 | 快捷键 |
|------|--------|
| 快速搜索 | `Ctrl` + `K` |
| 保存 | `Ctrl` + `S` |
| 新建提示词 | `Ctrl` + `N` |
| 关闭弹窗 | `Esc` |

**变量用法**：正文中写 `{变量名}`（支持中文），底部自动出现填充栏，预设默认值后一键复制。

**图片**：编辑弹窗中粘贴、拖拽或点击 🖼 插入，卡片上悬停 0.5 秒可预览大图。

## 🔨 从源码构建

```bash
# 环境: Node.js 18+, Rust 1.70+
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
| 存储 | IndexedDB |
| 图标 | [Phosphor Icons](https://phosphoricons.com) |
| 字体 | Geist Sans + Newsreader |

## 📄 许可证

MIT
