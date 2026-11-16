---
title: 小费
description: 提示是一种简短的、可选的提示，例如键盘快捷键或指向更多帮助的指针，位于其所属内容的下方居中。
sidebarGroup: 反馈与状态
---

# 小费 {#tip}

## 概览 {#overview}

提示是一行可以被人们安全忽略的帮助信息。它以一个灯泡图标和 **Tip!** 文字开头，后面跟着以较浅颜色显示的提示内容。你可以在 **设置** 页面底部、搜索对话框底部，以及创建新自动化的对话框中找到提示，其中提示会指向你可以找到更多蓝图的位置。

它需要 Home Assistant 的翻译来显示其前缀，因此此处没有实时演示。

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](https://contributors.home-assistant.io/design/components/tip/)。

## 何时使用 {#when-to-use}

使用提示用于：

- 可以加快操作的快捷方式，例如键盘快捷键
- 指向更多帮助或更多内容，例如社区或蓝图交流

不要使用提示用于：

- 完成任务所需的重要信息。将其放在正文中，或使用 [alert](/design/components/alert)。
- 警告或错误。使用 [alert](/design/components/alert)。
- 关于某个字段的提示。使用该字段的辅助文本。

## 解剖结构 {#anatomy}

1. **图标**：一个灯泡
2. **前缀**：单词 **提示！**，中等字重，已翻译
3. **文本**：提示信息，使用辅助文本颜色。可以包含链接或按钮。

整个提示居中显示。

## 变体 {#variants}

只有一个提示。变化在于内容：纯文本，或文本中包含链接或按钮。

在 **设置** 页面，前端每次选择一个随机提示。关于键盘快捷键的提示在窄屏上会被忽略。

## 行为 {#behavior}

提示本身不会执行任何操作。提示中的链接或按钮照常工作。

## 规格 {#specs}

| 属性 | 值 | 令牌 |
| --- | --- | --- |
| 对齐方式 | 居中 | 无 |
| 前缀权重 | 500 | `--ha-font-weight-medium` |
| 文字颜色 | 次要文字颜色 | `--secondary-text-color` |
| 前缀与文字间距 | 2px | 无 |

图标的默认大小为 24px (`--mdc-icon-size`)。文字跟随周围文字的大小。

## 指南 {#guidelines}

- 将其放在内容的末尾，不要挡住其他内容。这就是前端放置提示的位置：在 **设置** 页面卡片下方、搜索对话框底部，以及蓝图列表下方。

## 无障碍功能 {#accessibility}

### 键盘 {#keyboard}

提示自身没有键盘行为。提示中的链接或按钮在 Tab 顺序中，就像其他地方一样。

### 屏幕阅读器 {#screen-readers}

屏幕阅读器会像读取普通文本一样读取前缀和文本。图标是装饰性的。

### 在代码中 {#in-the-code}

提示没有角色。图标是 `ha-svg-icon`。编写文本时，使其在“提示！”之后阅读顺畅。

## 相关内容 {#related}

- [警报](/design/components/alert)：提供人们所需的信息
- [工具提示](/design/components/tooltip)：悬停或聚焦时显示的简短提示
- [界面文本](/design/ui-text)：如何编写提示

## 在代码中 {#in-code}

元素是 `<ha-tip>`。将提示放在它的默认插槽中：

```html
<ha-tip>
  <a href="..." target="_blank" rel="noreferrer">Discover more blueprints</a>
</ha-tip>
```

前缀来自翻译键 `ui.panel.config.tips.tip`。

### 插槽 {#slots}

- 默认：提示的文本。

来源：[[`src/components/ha-tip.ts`]](https://github.com/home-assistant/frontend/blob/dev/src/components/ha-tip.ts)
