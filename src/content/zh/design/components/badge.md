---
title: 徽章
description: 徽章在一个紧凑的胶囊中显示一小片状态信息，例如温度或灯的状态。
sidebarGroup: 反馈与状态
---


# 徽章 {#badge}
实时演示 `ha-badge`, `ha-svg-icon`。

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](/design/components/badge)。

```html
<ha-badge label="Living room">
  <ha-svg-icon slot="icon" path="M15 13V5A3 3 0 0 0 9 5V13A5 5 0 1 0 15 13M12 4A1 1 0 0 1 13 5V8H11V5A1 1 0 0 1 12 4Z"></ha-svg-icon>
  21.5 °C
</ha-badge>
<ha-badge type="button">
  <ha-svg-icon slot="icon" path="M12,2A7,7 0 0,0 5,9C5,11.38 6.19,13.47 8,14.74V17A1,1 0 0,0 9,18H15A1,1 0 0,0 16,17V14.74C17.81,13.47 19,11.38 19,9A7,7 0 0,0 12,2M9,21A1,1 0 0,0 10,22H14A1,1 0 0,0 15,21V20H9V21Z"></ha-svg-icon>
  On
</ha-badge>
<ha-badge icon-only type="button">
  <ha-svg-icon slot="icon" path="M12,15.5A3.5,3.5 0 0,1 8.5,12A3.5,3.5 0 0,1 12,8.5A3.5,3.5 0 0,1 15.5,12A3.5,3.5 0 0,1 12,15.5M19.43,12.97C19.47,12.65 19.5,12.33 19.5,12C19.5,11.67 19.47,11.34 19.43,11L21.54,9.37C21.73,9.22 21.78,8.95 21.66,8.73L19.66,5.27C19.54,5.05 19.27,4.96 19.05,5.05L16.56,6.05C16.04,5.66 15.5,5.32 14.87,5.07L14.5,2.42C14.46,2.18 14.25,2 14,2H10C9.75,2 9.54,2.18 9.5,2.42L9.13,5.07C8.5,5.32 7.96,5.66 7.44,6.05L4.95,5.05C4.73,4.96 4.46,5.05 4.34,5.27L2.34,8.73C2.21,8.95 2.27,9.22 2.46,9.37L4.57,11C4.53,11.34 4.5,11.67 4.5,12C4.5,12.33 4.53,12.65 4.57,12.97L2.46,14.63C2.27,14.78 2.21,15.05 2.34,15.27L4.34,18.73C4.46,18.95 4.73,19.03 4.95,18.95L7.44,17.94C7.96,18.34 8.5,18.68 9.13,18.93L9.5,21.58C9.54,21.82 9.75,22 10,22H14C14.25,22 14.46,21.82 14.5,21.58L14.87,18.93C15.5,18.67 16.04,18.34 16.56,17.94L19.05,18.95C19.27,19.03 19.54,18.95 19.66,18.73L21.66,15.27C21.78,15.05 21.73,14.78 21.54,14.63L19.43,12.97Z"></ha-svg-icon>
</ha-badge>
```

## 概览 {#overview}
徽章可以一眼显示一件事情：状态、数值或计数。它驱动仪表板顶部的徽章，例如实体徽章和能量总和徽章。它是一个紧凑的小胶囊，带有可选图标、可选标签和显示数值。

## 使用时机 {#when-to-use}
使用徽章的情况：

- 显示单一事实，例如温度、灯的状态或计数
- 紧凑地提供更多详情的快捷方式，例如打开实体的更多信息对话框

不要使用徽章的情况：

- 不止一个事实。请使用卡片。
- 需要阅读的信息，例如错误。请使用 [警报](/design/components/alert)。
- 与其显示的数值无关的操作。请使用 [按钮](/design/components/button)。

## 解剖结构 {#anatomy}
1. **容器**：胶囊，带有卡片的背景、边框和阴影
2. **图标**：可选，用徽章颜色填充。此处的图片会变为圆形图片。
3. **标签**：可选的小型辅助文字，位于内容上方
4. **内容**：数值或状态

## 变体 {#variants}
### 有标签或无标签 {#with-or-without-a-label}
标签位于内容上方，以小号次要文本显示。用它来说明值的含义，例如区域或实体名称。当图标和数值已经清晰表明含义时，可以省略标签。

`ha-badge` 的实时演示。

```html
<ha-badge>21.5 °C</ha-badge>
<ha-badge label="Living room">21.5 °C</ha-badge>
```

### 徽章或按钮 {#badge-or-button}
默认情况下，徽章是静态的。当选择徽章会触发某些操作时，例如打开实体的更多信息对话框，请将其作为按钮徽章。按钮徽章具有悬停和按压反馈、指针光标、键盘焦点，并且屏幕阅读器会将其宣布为按钮。

`ha-badge` 的实时演示。

```html
<ha-badge>Static</ha-badge>
<ha-badge type="button">Selectable</ha-badge>
```

### 仅图标 {#icon-only}
仅图标徽章会去掉标签和内容，变成圆形图标。仅在人们能够不依赖文字即可识别图标时使用。否则，请保留文本。

## 行为 {#behavior}
- **静态**：默认类型的徽章没有悬停、聚焦或按下状态。
- **悬停**：按钮徽章在徽章颜色上覆盖 4% 不透明度的覆盖层。
- **按下**：按钮徽章在徽章颜色上覆盖 12% 不透明度的覆盖层。
- **聚焦**：聚焦的按钮徽章在徽章颜色上有边框和 1px 光环。更改持续 180ms。

## 规格 {#specs}
| 属性 | 数值 | 令牌 |
| --- | --- | --- |
| 高度和最小宽度 | 36px | `--ha-badge-size` |
| 左右内边距 | 12px | 无 |
| 仅图标的左右内边距 | 0 | 无 |
| 圆角半径 | 高度的一半，18px | `--ha-badge-border-radius` |
| 图标与文字间距 | 8px | `--ha-space-2` |
| 图标大小 | 18px | `--ha-badge-icon-size` |
| 图标槽中的图片 | 30px，圆形 | `--ha-border-radius-circle` |
| 边框宽度 | 1px | `--ha-card-border-width` |
| 标签 | 10px，重量500，行高10px | `--ha-font-size-xs`, `--ha-font-weight-medium` |
| 内容 | 12px，重量500，行高1.2 | `--ha-font-size-s`, `--ha-font-weight-medium`, `--ha-line-height-condensed` |

| 部件 | 颜色 |
| --- | --- |
| 背景 | `--ha-card-background`，回退到 `--card-background-color` |
| 边框 | `--ha-card-border-color`，回退到 `--divider-color` |
| 阴影 | `--ha-card-box-shadow`，默认无 |
| 图标、聚焦边框和聚焦环 | `--badge-color`，默认值为 `--secondary-text-color` |
| 标签 | `--secondary-text-color` |
| 内容 | `--primary-text-color` |

## 指南 {#guidelines}
以现场演示的方式展示可做与不可做。

**可做：** 保持内容为带单位的数值，或为一个状态。

```html
<ha-badge label="Living room"><ha-svg-icon slot="icon" path="M15 13V5A3 3 0 0 0 9 5V13A5 5 0 1 0 15 13M12 4A1 1 0 0 1 13 5V8H11V5A1 1 0 0 1 12 4Z"></ha-svg-icon>21.5 °C</ha-badge>
```

**不可做：** 在徽章中放入一句完整的句子。

```html
<ha-badge><ha-svg-icon slot="icon" path="M15 13V5A3 3 0 0 0 9 5V13A5 5 0 1 0 15 13M12 4A1 1 0 0 1 13 5V8H11V5A1 1 0 0 1 12 4Z"></ha-svg-icon>The living room is 21.5 °C</ha-badge>
```

- 保持徽章只包含单一事实。如果需要更多空间，使用卡片。
- 只有在选择徽章会触发操作时，才将其设置为按钮徽章。不要让无法选择的徽章看起来可以选择。
- 请参阅 [UI 文本](/design/ui-text) 了解如何编写状态和单位。

## 无障碍功能 {#accessibility}
### 键盘 {#keyboard}
| 键 | 操作 |
| --- | --- |
| <kbd>Tab</kbd> | 将焦点移到按钮徽章。静态徽章不可聚焦。 |

徽章本身没有键盘处理程序。<kbd>Enter</kbd> 或 <kbd>Space</kbd> 在按钮徽章上的操作取决于页面添加的处理程序。

### 焦点 {#focus}
按钮徽章在获得焦点时会显示边框和徽章颜色的细环，但仅在使用键盘时显示。

### 目标大小 {#target-size}
徽章高度为 36 像素，宽度至少为 36 像素。

### 屏幕阅读器 {#screen-readers}
屏幕阅读器会读取标签和内容。按钮徽章会被宣布为按钮。仅有图标的徽章自身没有文本，因此需要页面提供名称。

### 代码中的实现 {#in-the-code}
- 按钮徽章具有角色 `button` 和 `tabindex="0"`。静态徽章没有角色，且不可聚焦。
- 焦点样式使用 `:focus-visible`。

## 相关 {#related}
- [标签徽章](/design/components/label-badge)：较旧的圆形徽章
- [状态图标](/design/components/state-icon)：实体徽章显示的图标
- [警报](/design/components/alert)：用于消息而非数值

## 在代码中 {#in-code}
该元素是 `<ha-badge>`。内容放在默认插槽，图标放在 `icon` 插槽。

```html
<ha-badge label="Living room">
  <ha-svg-icon slot="icon" path="..."></ha-svg-icon>
  21.5 °C
</ha-badge>

<ha-badge type="button">On</ha-badge>
```

### 属性 {#attributes}
- `type`: `badge`（默认）或 `button`。
- `label`: 内容上方的小文本。
- `icon-only`: 只显示图标。隐藏标签和内容。

### 插槽 {#slots}
- 默认: 徽章的内容。
- `icon`: 图标，通常是 `ha-svg-icon` 或 `ha-state-icon`。该插槽中的 `img` 显示为圆形 30 像素图片，类似实体图片。

### 样式 {#styling}
- `--badge-color`：图标颜色和焦点环颜色。默认为 `var(--secondary-text-color)`。仪表板徽章将其设置为实体的状态颜色。
- `--ha-badge-size`：高度和最小宽度。默认为 `36px`。
- `--ha-badge-border-radius`：圆角半径。默认为尺寸的一半，使其呈胶囊形。
- `--ha-badge-font-size`：内容文本大小。默认为 `var(--ha-font-size-s)`。
- `--ha-badge-icon-size`：图标大小。默认为 `18px`。

背景、边框和阴影遵循卡片变量 (`--ha-card-background`, `--ha-card-border-color`, `--ha-card-border-width`, `--ha-card-box-shadow`)，因此徽章与主题卡片匹配。

来源：[`src/components/ha-badge.ts`](https://github.com/home-assistant/frontend/blob/dev/src/components/ha-badge.ts)
