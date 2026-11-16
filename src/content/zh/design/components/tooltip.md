---
title: 工具提示
description: 当你将鼠标悬停或聚焦在一个元素上时，工具提示会显示关于该元素的简短提示。
sidebarGroup: 反馈与状态
---

# 工具提示 {#tooltip}

Live演示 `ha-button`，`ha-tooltip`。

```html
<ha-button id="tooltip-demo-restart" appearance="filled">Restart</ha-button>
<ha-tooltip for="tooltip-demo-restart">Restarts Home Assistant. This takes about a minute.</ha-tooltip>
```

## 概述 {#overview}

当你将鼠标悬停在元素上或将键盘焦点移动到元素上时，工具提示会显示有关该元素的简短提示。它用于提供额外的信息，这些信息虽然有用，但不是完成任务所必需的。最常见的情况是：为图标按钮命名，或显示相对时间（如 **5分钟前**）背后的完整日期。

## 使用时机 {#when-to-use}

工具提示适用于：

- 为没有可见标签的图标命名
- 为简短的值提供额外细节，例如相对时间背后的完整日期

不应使用工具提示于：

- 任何重要内容，如说明或错误。工具提示仅在悬停或键盘聚焦时显示，在触摸屏上它们很难或无法访问。应将其直接显示在屏幕上，作为文本或 [警报](/design/components/alert)。
- 链接、按钮或其他互动内容。人们无法触及它们。

## 解剖学 {#anatomy}

1. **目标**：工具提示所针对的元素，用 `for` 指示
2. **主体**：带有工具提示文本的表面。默认情况下没有箭头。

## 变体 {#variants}

### 位置 {#placement}

工具提示默认显示在目标上方。它可以放置在其他位置，例如下方或右侧。当没有足够空间时，它会翻转到另一侧或移动。

`ha-svg-icon`、`ha-tooltip` 的实时演示。

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](https://contributors.home-assistant.io/design/components/tooltip/)。

```html
<ha-svg-icon id="tooltip-demo-info" path="M11,9H13V7H11M12,20C7.59,20 4,16.41 4,12C4,7.59 7.59,4 12,4C16.41,4 20,7.59 20,12C20,16.41 16.41,20 12,20M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M11,17H13V11H11V17Z" tabindex="0"></ha-svg-icon>
<ha-tooltip for="tooltip-demo-info" placement="right">Measured every 30 seconds</ha-tooltip>
```

## 行为 {#behavior}

- **悬停**：指针进入目标后 350ms 显示工具提示，离开 150ms 后隐藏。从目标移动到工具提示指针会保持其显示。
- **聚焦**：当目标获得焦点时显示工具提示，失去焦点时隐藏。
- **关闭**：<kbd>Esc</kbd> 可以隐藏打开的工具提示。点击目标外任意位置也会关闭。
- **禁用**：禁用的工具提示不会显示。
- 工具提示显示和消失时无动画效果。
- 文本在 30 个字符处换行。

## 规格 {#specs}

| 属性 | 值 | 令牌 |
| --- | --- | --- |
| 背景 | 默认表面颜色 | `--ha-color-surface-default`, 到 `--ha-tooltip-background-color` |
| 文字颜色 | 主要文字颜色 | `--primary-text-color`, 到 `--ha-tooltip-text-color` |
| 字体大小 | 14px | `--ha-font-size-m`, 到 `--ha-tooltip-font-size` |
| 字体粗细 | 500 | `--ha-font-weight-medium`, 到 `--ha-tooltip-font-weight` |
| 行高 | 1.2 | `--ha-line-height-condensed`, 到 `--ha-tooltip-line-height` |
| 内边距 | 上下 0.25em, 左右 0.5em | 无 |
| 圆角 | 8px | `--ha-border-radius-md`, 到 `--ha-tooltip-border-radius` |
| 阴影 | 中等阴影 | `--ha-box-shadow-m`, 到 `--ha-tooltip-box-shadow` |
| 边框 | 无, 0px | 无 |
| 箭头 | 无, 0px | `--ha-tooltip-arrow-size` |
| 与目标的距离 | 8px | 无 |
| 最大宽度 | 30ch | 无 |
| 堆叠顺序 | 1000 | 无 |
| 显示和隐藏延迟 | 350ms 和 150ms | 无 |

## 指南 {#guidelines}

示例中的行为与避免的行为。

**做:** 使用工具提示为没有标签的图标命名。

```html
<ha-svg-icon id="tooltip-do-info" path="M11,9H13V7H11M12,20C7.59,20 4,16.41 4,12C4,7.59 7.59,4 12,4C16.41,4 20,7.59 20,12C20,16.41 16.41,20 12,20M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M11,17H13V11H11V17Z" tabindex="0"></ha-svg-icon>
<ha-tooltip for="tooltip-do-info">Measured every 30 seconds</ha-tooltip>
```

**别:** 重复可见标签。没有任何附加价值。

```html
<ha-button id="tooltip-dont-save">Save</ha-button>
<ha-tooltip for="tooltip-dont-save">Save</ha-tooltip>
```

- 保持在一句简短的句子或几个词。
- 永远不要在工具提示中放置任何重要内容，如说明或错误信息。
- 不放置链接、按钮或其他交互内容。

## 可访问性 {#accessibility}

### 键盘 {#keyboard}

| 键 | 操作 |
| --- | --- |
| <kbd>Tab</kbd> | 移动焦点到目标显示工具提示。移开焦点隐藏工具提示。 |
| <kbd>Escape</kbd> | 隐藏已打开的工具提示。 |

对于键盘用户来说，目标需要可以聚焦才能查看工具提示。图标自身不可聚焦。

### 屏幕阅读器 {#screen-readers}

工具提示文本会成为其目标的名称。这对于没有标签的图标效果很好。在有可见标签的目标上，屏幕阅读器会读取工具提示文本，而不是该标签。

### 在代码中 {#in-the-code}

- 本页的演示在图标上添加 `tabindex="0"` 以使其可聚焦。
- 提示框将其自己的 `id` 添加到目标的 `aria-labelledby`。这使提示文本成为目标的可访问名称，对于没有标签的图标效果很好。在具有可见标签的目标上，屏幕阅读器会读取提示文本而不是该标签。
- 提示框主体本身没有角色。

## 相关内容 {#related}

- [警报](/design/components/alert)：用于人们需要的信息
- [按钮](/design/components/button)：提示框的常见目标

## 在代码中 {#in-code}

该元素是 `<ha-tooltip>`。它基于 [Web Awesome tooltip](https://webawesome.com/docs/components/tooltip/)。给目标一个 `id`，并使用 `for` 将提示框指向它：

```html
<ha-svg-icon id="help-icon" path="..."></ha-svg-icon>
<ha-tooltip for="help-icon">Measured every 30 seconds</ha-tooltip>
```

### 属性 {#attributes}

- `for`：目标元素的 `id`。目标必须在同一个文档或影子根中。
- `placement`：`top`（默认）、`bottom`、`left`、`right`，或包含 `-start` 或 `-end` 的其中之一，如 `top-start`。
- `distance`：提示工具与目标之间的间距，单位为像素。默认值为 `8`。
- `show-delay`：显示之前的毫秒数。默认值为 `350`。
- `hide-delay`：隐藏之前的毫秒数。默认值为 `150`。
- `trigger`：触发提示工具打开的方式。默认值为 `hover focus`。也接受 `click` 和 `manual`。
- `disabled`：阻止提示工具显示。
- `open`：显示提示工具。

### 插槽 {#slots}

- 默认：提示文本。

### 样式 {#styling}

- `--ha-tooltip-background-color`：默认为 `var(--ha-color-surface-default)`。
- `--ha-tooltip-text-color`：默认为 `var(--primary-text-color)`。
- `--ha-tooltip-font-size`：默认为 `var(--ha-font-size-m)`。
- `--ha-tooltip-line-height`：默认为 `var(--ha-line-height-condensed)`。
- `--ha-tooltip-border-radius`：默认为 `var(--ha-border-radius-md)`。
- `--ha-tooltip-arrow-size`：默认为 `0px`，因此没有箭头。
- `--ha-tooltip-box-shadow`：默认为 `var(--ha-box-shadow-m)`。
- `--ha-tooltip-animation-duration`：默认为 `0`，因此显示时没有动画。

`ha-tooltip` 还在 Web Awesome 提示上设置 `--ha-tooltip-font-family`、`--ha-tooltip-font-weight` 和 `--ha-tooltip-padding`。当前使用的 Web Awesome 版本不读取它们提供的变量，因此没有可见效果。

来源：[`src/components/ha-tooltip.ts`](https://github.com/home-assistant/frontend/blob/dev/src/components/ha-tooltip.ts)
