---
title: 警报
description: 提醒显示一条简短且重要的信息，不会打断某人的操作。
sidebarGroup: 反馈与状态
---


# 警报 {#alert}
Live 演示 `ha-alert`。

```html
<ha-alert alert-type="error">Could not connect to the device.</ha-alert>
<ha-alert alert-type="warning">This update requires a restart.</ha-alert>
<ha-alert alert-type="info">You can change this later in the settings.</ha-alert>
<ha-alert alert-type="success">Backup created.</ha-alert>
```

## 概述 {#overview}
警报用于吸引注意页面上的信息。它不会阻止任何操作：人们可以阅读信息并继续操作。警报的类型通过颜色和图标显示，表明信息的严重程度。

## 适用场景 {#when-to-use}
使用警报来：

- 通知用户某个错误及其处理方法
- 警告需要注意的事项，或可能出现的问题
- 提供有用的背景信息，如提示或需要注意的变更
- 确认某个操作已成功

不要使用警报来：

- 用户必须做出决定才能继续的情况。使用 [对话框](/design/components/dialog)。
- 位于某个元素旁边的简短标签或状态。使用 [徽章](/design/components/badge)。
- 仅在悬停时显示的额外帮助。使用 [工具提示](/design/components/tooltip)。

## 解剖结构 {#anatomy}
1. **容器**：带色背景，颜色与类型一致
2. **图标**：类型的图标，或你自己的图标
3. **标题**：可选，位于消息上方，用加粗显示
4. **消息**：警报的文本内容
5. **操作**：可选，一个关闭按钮或你自己的操作，比如按钮

## 变体 {#variants}
### 类型 {#type}
共有四种类型。每种都有自己的颜色和图标：

- **错误**：出现了问题。说明是什么问题，以及如何处理。
- **警告**：需要注意的事项，或者可能出错的情况。
- **信息**：有用的上下文，比如提示或需要注意的变化。这是默认类型。
- **成功**：操作按预期完成。

### 带标题 {#with-a-title}
标题会在消息上方添加一行加粗文字。它应与消息一起使用，不能单独使用。

`ha-alert` 的实时演示。

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](/design/components/alert)。

```html
<ha-alert alert-type="warning" title="Restart required">This update requires a restart.</ha-alert>
```

### 可关闭或带操作 {#dismissable-or-with-an-action}
可关闭警报有一个关闭按钮。你也可以在警报中放置自己的操作，比如撤销按钮。

`ha-alert`, `ha-button` 的实时演示，连接到演示 Home Assistant。

```html
<ha-alert alert-type="info" dismissable>You can change this later in the settings.</ha-alert>
<ha-alert alert-type="success">Backup created.<ha-button slot="action" appearance="plain">Undo</ha-button></ha-alert>
```

### 窄版 {#narrow}
在窄版中，操作会移到消息下方，而不是紧挨着。这有助于在小空间中使用，例如卡片。

## 行为 {#behavior}
- 警告本身没有悬停、聚焦或按下状态。只有其中的操作，如关闭按钮，才有这些状态。
- 选择关闭按钮不会移除警告。它会发送一个事件，显示警告的页面决定接下来发生什么，通常是隐藏它。
- 长文本会自动换行，长单词会断开，因此消息总能适应。
- 当没有标题时，图标会在消息旁居中显示。有标题时，图标会与标题对齐。
- 警告的布局是从左到右，除非其标题以希伯来文或阿拉伯文开头。那时，它会遵循页面的书写方向。

## 规格 {#specs}
| 属性 | 值 | 令牌 |
| --- | --- | --- |
| 内边距 | 8px | `--ha-alert-padding` |
| 图标大小 | 24px | `--ha-alert-icon-size` |
| 图标与信息之间的间距 | 8px | 无 |
| 圆角半径 | 4px | `--ha-border-radius-sm` |
| 背景 | 类型颜色的12%不透明度 | 见下文 |
| 标题字体粗细 | 700 | `--ha-font-weight-bold` |
| 关闭按钮大小 | 36px | `--ha-icon-button-size` |

| 类型 | 图标 | 图标和背景颜色 |
| --- | --- | --- |
| 错误 | 警告圆圈轮廓 | `--error-color`, `#db4437` |
| 警告 | 警告轮廓 | `--warning-color`, `#ffa600` |
| 信息 | 信息轮廓 | `--info-color`, `#039be5` |
| 成功 | 已勾选圆圈轮廓 | `--success-color`, `#43a047` |

信息文本本身没有颜色：它使用周围页面的文本颜色。

## 指南 {#guidelines}
作为现场演示的做与不做。

**做:** 说明出了什么问题，以及如何解决。

```html
<ha-alert alert-type="error">Could not connect to the device. Check that it is turned on and connected to your network.</ha-alert>
```

**不做:** 仅仅说出了问题。

```html
<ha-alert alert-type="error">An error occurred.</ha-alert>
```

作为现场演示的做与不做。

**做:** 使用标题和消息。

```html
<ha-alert alert-type="warning" title="Restart required">This update requires a restart.</ha-alert>
```

**不做:** 仅使用标题而没有消息。

```html
<ha-alert alert-type="warning" title="Restart required"></ha-alert>
```

## 可访问性 {#accessibility}
### 键盘 {#keyboard}
警报本身不会获取焦点，其操作会：

| 键 | 操作 |
| --- | --- |
| <kbd>Tab</kbd> | 将焦点移到关闭按钮或你自己的操作。 |
| <kbd>Enter</kbd> 或 <kbd>Space</kbd> | 选择当前聚焦的按钮。 |

### 目标尺寸 {#target-size}
关闭按钮的尺寸为 36px x 36px。

### 屏幕阅读器 {#screen-readers}
- 当警报出现在已打开的页面上时，大多数屏幕阅读器会立即朗读它。页面加载时已存在的警报不会被宣布。
- 使用屏幕阅读器的人无法感知颜色和图标，因此文本必须自行清楚地表明类型。
- 关闭按钮会被宣布为“关闭警报”，使用用户的语言。

### 在代码中 {#in-the-code}
- 警报的角色是 `alert`。
- 图标是一个 `ha-svg-icon`，通过 `aria-hidden="true"` 对屏幕阅读器隐藏。
- 关闭按钮是一个图标按钮，其可访问名称为已翻译标签 `ui.common.dismiss_alert`。

## 相关 {#related}
- [对话](/design/components/dialog)：当有人必须在继续之前回应时
- [徽章](/design/components/badge)：某物旁的简短状态
- [颜色](/design/foundations/color)：类型背后的颜色
- [界面文字](/design/ui-text)：如何编写消息

## 代码中 {#in-code}
该元素是 `<ha-alert>`，类型通过 `alert-type` 设置：

```html
<ha-alert alert-type="error">Could not connect to the device.</ha-alert>
<ha-alert alert-type="warning" title="Restart required">
  This update requires a restart.
</ha-alert>
<ha-alert alert-type="success" dismissable>Backup created.</ha-alert>
```

### 属性 {#attributes}
- `alert-type`：`info`（默认）、`warning`、`error` 或 `success`。
- `title`：标题，显示在消息上方加粗。
- `dismissable`：显示关闭按钮。
- `narrow`：将操作放在消息下方。

### 插槽 {#slots}
- 默认：消息内容。
- `icon`：替换类型的图标。
- `action`：你自己的操作，如按钮。它会替换关闭按钮。

### 事件 {#events}
- `alert-dismissed-clicked`：当选择关闭按钮时触发。响应时移除或隐藏警告。

### 样式 {#styling}
- `--ha-alert-padding`：内边距。默认值为 8px。
- `--ha-alert-icon-size`：图标的大小。默认值为 24px。

来源：[`src/components/ha-alert.ts`](https://github.com/home-assistant/frontend/blob/dev/src/components/ha-alert.ts)
