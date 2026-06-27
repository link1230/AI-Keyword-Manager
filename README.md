<p align="center">
  <img src="https://img.shields.io/badge/platform-Windows-blue?logo=windows">
  <img src="https://img.shields.io/badge/built%20with-Tauri-FFC131?logo=tauri">
  <img src="https://img.shields.io/badge/size-4.5MB-green">
  <img src="https://img.shields.io/badge/license-MIT-lightgrey">
</p>

<h1 align="center">PromptManager · 提示词管理器</h1>

<p align="center"><i>AI 提示词管理器 — Windows 原生桌面应用，帮你组织、搜索、复用 AI 提示词模板。</i></p>

<p align="center">
  <img src="./docs/poster.png" alt="PromptManager" width="800">
</p>

<p align="center">
  <b>简体中文</b> &nbsp;|&nbsp; <a href="./docs/README.en.md">English</a>
</p>

---

## 功能

<table>
<tr>
<td width="50%">

### 组织
- **分类树** — 嵌套分类，支持新增 / 改名 / 删除
- **标签筛选** — 内容标签，侧边栏一键切换
- **AI 模型标签** — ChatGPT / Claude / Gemini / DeepSeek / Kimi…

</td>
<td width="50%">

### 搜索
- **快速搜索** — `Ctrl+K` 全局模糊搜索
- **键盘导航** — 上下键选择，回车打开
- **全文匹配** — 标题、正文、标签同步搜索

</td>
</tr>
<tr>
<td>

### 编写
- **变量占位符** — `{语言}` `{风格}` 自动识别高亮
- **一键填充** — 复制前弹出变量面板，默认值自动记忆
- **图片插入** — 粘贴 / 拖拽 / 按钮，卡片缩略图 + 悬停放大预览

</td>
<td>

### 体验
- **中英双语** — 全界面一键切换
- **深色 / 浅色主题** — 暖奶油 editorial 风格 + OLED 深色
- **启动封面** — 自定义封面 + 淡入淡出过渡
- **导入 / 导出** — JSON 格式，含图片完整数据
- **本地存储** — IndexedDB，无容量限制

</td>
</tr>
</table>

## 安装

下载 [最新 Release](https://github.com/你的用户名/prompt-manager/releases/latest) 中的 `PromptManager_Setup.exe`（~4.5 MB），双击安装。

> Windows 10 / 11 自带 WebView2，无需额外依赖。

## 快捷键

| 操作 | 快捷键 |
|------|--------|
| 快速搜索 | `Ctrl` + `K` |
| 保存 | `Ctrl` + `S` |
| 新建提示词 | `Ctrl` + `N` |
| 关闭弹窗 | `Esc` |

## 从源码构建

```bash
# 环境: Node.js 18+ / Rust 1.70+
git clone https://github.com/你的用户名/prompt-manager.git
cd prompt-manager
npm install
npx tauri build
```

## 技术栈

| 层 | 选型 |
|----|------|
| 桌面框架 | [Tauri v2](https://tauri.app) |
| 界面 | HTML / CSS / JS |
| 存储 | IndexedDB |
| 图标 | [Phosphor Icons](https://phosphoricons.com) |
| 字体 | Geist Sans + Newsreader |

## 许可证

MIT
