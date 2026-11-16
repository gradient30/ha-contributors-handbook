---
title: 测量仪
description: 仪表在半圆表盘上显示单个数值，并可以选择颜色来表示该数值的好坏。
sidebarGroup: 显示数值
---


# 测量仪 {#gauge}
Live demo of `ha-gauge`.

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](/design/components/gauge)。

```html
<ha-gauge value="21" min="0" max="40" label="°C" style="width: 200px; --gauge-color: var(--success-color)"></ha-gauge>
<ha-gauge value="78" label="%" style="width: 200px; --gauge-color: var(--warning-color)"></ha-gauge>
```

## 概述 {#overview}
仪表盘是仪表卡和类似自给自足这样的能源仪表卡的表盘。它以半圆的形式显示一个数值，数字显示在中间。表盘提供背景信息：数值在其范围内的位置，以及这一数值是好还是坏。

## 使用场景 {#when-to-use}
适合使用仪表盘的情况：

- 一个数值在已知范围内，而且该范围内的位置很重要，例如温度、电池电量或者百分比
- 一个具有严重性等级的数值，例如好、警告或差

不适合使用仪表盘的情况：

- 在设置行或列表中的层级。请使用[条形图](/design/components/bar)，它占用空间更少。
- 没有有意义的最小值和最大值的数值。此时表盘无法显示任何信息。

## 解剖结构 {#anatomy}
1. **轨道**：空的半圆形，从 `min` 到 `max` 的整个范围
2. **数值弧**：轨道中填充的部分，直到数值位置
3. **等级**：轨道的可选彩色分段
4. **指针**：在指针模式下，替代数值弧，并指向数值
5. **数值文本**：格式化的数值和单位，或当前位置等级的标签，位于中间

## 变体 {#variants}
### 带严重性色彩的填充弧 {#filled-arc-with-a-severity-color}
默认设置。弧线会填充到数值位置。仪表盘的颜色可以传达意义：根据数值所在位置显示成功、警告或错误颜色。如果未设置颜色，仪表盘的填充部分将没有颜色。当数值既不属于好也不属于坏时，使用信息颜色。

`ha-gauge` 的实时演示。

```html
<ha-gauge value="30" style="width: 160px; --gauge-color: var(--info-color)"></ha-gauge>
<ha-gauge value="30" style="width: 160px; --gauge-color: var(--success-color)"></ha-gauge>
<ha-gauge value="60" style="width: 160px; --gauge-color: var(--warning-color)"></ha-gauge>
<ha-gauge value="90" style="width: 160px; --gauge-color: var(--error-color)"></ha-gauge>
```

### 带等级的指针 {#needle-with-levels}
在指针版本中，表盘显示的是指针，而不是填充弧，可以按分段上色，这些分段称为等级。每个等级从它自己的数值开始，一直延伸到下一个等级。这可以一次显示整个刻度，因此人们既能看到数值，也能看到它离下一个分段的距离。

`ha-gauge` 的实时演示。

```html
<ha-gauge value="62" needle levels='[{"level":0,"stroke":"var(--success-color)"},{"level":50,"stroke":"var(--warning-color)"},{"level":80,"stroke":"var(--error-color)"}]' label="%" style="width: 200px"></ha-gauge>
```

一个等级可以有一个标签。当数值落在该分段内时，标签会替换仪表中间的数字。当一个词比数字表达的信息更多时，例如 **低** 或 **高**，就可以使用它。

如果第一个等级没有从最小值开始，仪表会在信息颜色中添加一个从最小值到第一个等级的分段。

## 行为 {#behavior}
- 仪表盘不可交互。它没有悬停、聚焦、按下或禁用状态。
- 当数值变化时，弧线或指针在 1 秒内移动到新位置，使用缓动曲线。
- 小于最小值或大于最大值的数值显示在刻度盘的起始或结束位置。文本仍显示实际数值。
- 数值文本会缩放以适应刻度盘内的空间：最大占仪表宽度的 55% 和高度的 40%。
- 百分号采用适合用户语言的间距。任何其他单位在空格后显示。
- 数值文本始终从左到右排布，即使在右到左语言环境中。

## 规格 {#specs}
计量表是一个随宽度缩放的 SVG。下面的尺寸以 SVG 单位表示，绘图尺寸为宽 100 单位，高 55 单位。

| 属性 | 数值 | 令牌 |
| --- | --- | --- |
| 宽度 | 依据你给予元素的宽度，高度随之 | 无 |
| 弧半径 | 40 单位 | 无 |
| 弧及刻度厚度 | 12 单位 | 无 |
| 弧端 | 方形 | 无 |
| 缩放前的数值文字大小 | 16px | `--ha-font-size-l` |
| 数值文字区域 | 最多占宽度的 55% 和高度的 40%，距离底部 10% | 无 |
| 动画 | 1秒，缓动 | 无 |

| 部件 | 颜色 |
| --- | --- |
| 路径 | `--primary-background-color` |
| 数值弧 | `--gauge-color` |
| 新增的第一级 | `--info-color` |
| 指针 | `--primary-text-color`，边框 1 单位，颜色为 `--card-background-color` |
| 数值文字 | `--primary-text-color` |

## 指南 {#guidelines}
示例中的该做与不该做。

**该做：** 根据严重程度为仪表盘上色，这样颜色就有意义。

```html
<ha-gauge value="78" label="%" style="width: 160px; --gauge-color: var(--warning-color)"></ha-gauge>
```

**不该做：** 不要省略仪表盘的颜色。这样表盘的填充部分就没有颜色了。

```html
<ha-gauge value="78" label="%" style="width: 160px"></ha-gauge>
```

示例中的该做与不该做。

**该做：** 在标签中放置单位。

```html
<ha-gauge value="21" min="0" max="40" label="°C" style="width: 160px; --gauge-color: var(--info-color)"></ha-gauge>
```

**不该做：** 当数值有单位时，不要只显示数字而不显示单位。

```html
<ha-gauge value="21" min="0" max="40" style="width: 160px; --gauge-color: var(--info-color)"></ha-gauge>
```

## 可访问性 {#accessibility}
### 键盘 {#keyboard}
仪表盘不可聚焦，也没有键盘交互。

### 屏幕阅读器 {#screen-readers}
屏幕阅读器可以将数值和单位作为文本读取。仪表盘本身以及显示的严重程度没有文本替代：严重程度仅通过颜色显示。数值文本是不依赖颜色的部分。

### 在代码中 {#in-the-code}
仪表盘没有角色和 ARIA 属性。数值和单位是 SVG 文本。

## 相关 {#related}
- [栏](﻿/design/components/bar/)：用于行和列表的紧凑级别
- [控件](﻿/design/components/controls/)：当值可以更改时
- [仪表卡](﻿/design/dashboards/gauge-card/)：基于此拨盘构建的卡片
- [颜色](﻿/design/foundations/color/)：严重程度颜色

## 在代码中 {#in-code}
该元素是 `<ha-gauge>`。给它一个宽度；高度随之而来。

```html
<ha-gauge
  value="21"
  min="0"
  max="40"
  label="°C"
  style="width: 200px; --gauge-color: var(--success-color)"
></ha-gauge>
```

该值使用用户的 `locale` 格式化，因此从 `hass.locale` 设置 `locale` 属性。

### 属性 {#attributes}
- `value`：当前值。默认值为 `0`。
- `min`：刻度起点。默认值为 `0`。
- `max`：刻度终点。默认值为 `100`。
- `label`：单位，显示在数值后面。
- `needle`：显示指针而不是填充弧。
- `levels`：段的 JSON 数组，每段具有 `level`、`stroke` 颜色和可选的 `label`。如果第一层不以 `min` 开始，仪表会从 `min` 添加一个信息颜色段。

这些只能作为属性设置：

- `locale`：用于格式化数值的区域数据。
- `valueText`：显示文本替代格式化值。仪表卡使用它按 Home Assistant 格式显示状态。
- `formatOptions`：`Intl.NumberFormatOptions` 用于格式化数值。

### 样式 {#styling}
- `--gauge-color`：填充弧的颜色。在指针模式下不使用。
- `--primary-background-color`：表盘的空白部分。
- `--primary-text-color`：数值文本和指针。

来源: [`src/components/ha-gauge.ts`](https://github.com/home-assistant/frontend/blob/dev/src/components/ha-gauge.ts)
