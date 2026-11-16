---
title: 标签徽章
description: 圆形的经典州徽，中间有数值，边缘有简短标签。
sidebarGroup: 反馈与状态
---


# 标签徽章 {#label-badge}
即时演示 `ha-label-badge`, `ha-svg-icon`。

```html
<ha-label-badge label="°C" description="Living room">21</ha-label-badge>
<ha-label-badge label="%" description="Humidity" style="--ha-label-badge-color: var(--info-color)">48</ha-label-badge>
<ha-label-badge label="Error" description="Not found" style="--ha-label-badge-color: var(--error-color)">
  <ha-svg-icon path="M13 14H11V9H13M13 18H11V16H13M1 21H23L12 2L1 21Z"></ha-svg-icon>
</ha-label-badge>
```

## 概述 {#overview}
标签徽章是旧的圆形徽章样式：一个圆圈中的数值，底边有一个简短标签，下方有描述。今天，它仅用于图片元素卡片的状态徽章元素。

## 何时使用 {#when-to-use}
使用标签徽章来：

- 在图片元素卡片的状态徽章元素上工作

不要使用标签徽章来：

- 仪表板上的徽章。这类徽章使用 [badge](/design/components/badge)，具有当前仪表板样式。

## 结构 {#anatomy}
1. **圆圈**：圆形容器，有彩色边框，可选择性使用背景图像
2. **数值**：圆圈中的内容，可以是文本或图标
3. **标签**：可选，在圆圈底边的彩色标签，使用大写字母
4. **描述**：徽章下方的可选文本

## 变体 {#variants}
### 标签长度 {#label-length}
标签超过五个字符会使用较小的字体。

`ha-label-badge` 的实时演示。

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](/design/components/label-badge)。

```html
<ha-label-badge label="kWh">3.2</ha-label-badge>
<ha-label-badge label="Unavailable">?</ha-label-badge>
<ha-label-badge description="Kitchen">22</ha-label-badge>
```

## 行为 {#behavior}
- 标签徽章是静态的：它没有悬停、聚焦、按下或禁用状态。
- 对于圆圈过宽的数值，将使用省略号截断。标签过宽也会被截断。
- 描述宽度超过 5em 时将被截断。
- 边框和标签颜色的变化会在 0.3 秒内渐变显示。

## 规格 {#specs}
所有尺寸都相对于字体大小，因此徽章会随周围文本缩放。

| 属性 | 值 | 令牌 |
| --- | --- | --- |
| 圆形大小 | 2.5em | `--ha-label-badge-size` |
| 圆形字体大小 | 1.5em | `--ha-label-badge-font-size` |
| 圆角半径 | 50%，一个圆 | `--ha-label-badge-border-radius` |
| 边框 | 0.1em 实线 | `--ha-label-badge-color` |
| 标签字体大小 | 圆形的 0.5em，字符超过五个时为其 90% | 无 |
| 标签圆角半径 | 12px | `--ha-border-radius-lg` |
| 标签字重 | 500 | `--ha-font-weight-medium` |
| 描述字体大小 | 0.9em | `--ha-label-badge-title-font-size` |
| 描述宽度 | 5em | `--ha-label-badge-title-width` |
| 描述上方间距 | 1em | 无 |
| 部分 | 颜色 |
| --- | --- |
| 边框和标签背景 | `--ha-label-badge-color`，默认值为 `--primary-color` |
| 标签文字 | `--ha-label-badge-label-color`，默认值为白色 |
| 圆形背景 | `--label-badge-background-color`，由主题设置为 `--card-background-color` |
| 数值 | `--label-badge-text-color`，由主题设置为主文本颜色的 80% 不透明度 |

## 指南 {#guidelines}
现场演示的注意事项。

**做:** 保持数值在几个字符以内。

```html
<ha-label-badge label="°C">21</ha-label-badge>
```

**不要:** 在圆圈里放长数值，会被截断。

```html
<ha-label-badge label="°C">21.5432</ha-label-badge>
```

现场演示的注意事项。

**做:** 使用简短的描述。

```html
<ha-label-badge description="Kitchen">22</ha-label-badge>
```

**不要:** 使用长名称。描述大约在五个字符宽时会被截断。

```html
<ha-label-badge description="Downstairs living room">22</ha-label-badge>
```

## 无障碍 {#accessibility}
### 键盘 {#keyboard}
标签徽章不可聚焦，也没有键盘交互功能。

### 屏幕阅读器 {#screen-readers}
屏幕阅读器会以纯文本读出数值、标签和描述。标签看起来是大写字母，但会按原样读出。作为数值的图标会被跳过。

### 在代码中 {#in-the-code}
- 标签徽章没有角色。
- 标签仅通过 CSS 变为大写。
- 当图标作为数值并且是 `ha-svg-icon` 时，它是装饰性的，并且具有 `aria-hidden="true"`。

## 相关 {#related}
- [徽章](/design/components/badge)：当前徽章
- [状态图标](/design/components/state-icon)：实体的图标

## 代码中 {#in-code}
该元素是 `<ha-label-badge>`：

```html
<ha-label-badge label="°C" description="Living room">21</ha-label-badge>
```

### 属性 {#attributes}
- `label`：圆边上的简短文本。
- `description`：徽章下方的文本。
- `image`：圆形的背景图片 URL，例如实体图片。

### 插槽 {#slots}
- 默认：圆内的值。文本或图标。

### 样式 {#styling}
- `--ha-label-badge-color`：边框和标签背景。默认值为 `var(--primary-color)`。
- `--ha-label-badge-label-color`：标签文本。默认值为白色。
- `--ha-label-badge-size`：圆的大小。默认值为 `2.5em`。
- `--ha-label-badge-font-size`：值的字体大小。默认值为 `1.5em`。
- `--ha-label-badge-border-radius`：默认值为 `50%`，一个圆。
- `--ha-label-badge-padding`：整个徽章的内边距。
- `--ha-label-badge-label-text-transform`：默认值为 `uppercase`。
- `--ha-label-badge-title-font-size`、`--ha-label-badge-title-font-weight` 和 `--ha-label-badge-title-width`：徽章下方的描述。
- `--label-badge-background-color` 和 `--label-badge-text-color`：圆背景和数值颜色。这些是主题变量。

来源：[`src/components/ha-label-badge.ts`](https://github.com/home-assistant/frontend/blob/dev/src/components/ha-label-badge.ts)
