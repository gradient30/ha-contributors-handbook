---
title: 滑块
description: 滑块让人们通过拖动从一个范围中选择一个数字。
sidebarGroup: 输入
---

# 滑块 {#slider}

Live 演示 `ha-slider`。

```html
<ha-slider min="0" max="100" value="60"></ha-slider>
```

## 概述 {#overview}

滑块允许人们通过拖动从一个范围中选择一个数字。人们可以立即看到该值在最小值和最大值之间的位置，并且可以通过一次拖动来更改它。

## 何时使用 {#when-to-use}

使用滑块用于：

- 数值范围比具体数字更重要的情况，例如音量、速度或百分比

不要使用滑块用于：

- 没有明确最小值和最大值的数值，或者人们需要精确输入的数值。使用带有 `type="number"` 的 [文本输入](/design/components/input)。
- 控制仪表板或“更多信息”对话框中的设备。前端对此有更大的 `<ha-control-slider>` 控件，详见 [控件](/design/components/controls)。本页的滑块用于设置、表单和紧凑行。

前端的数字选择器可以兼具两者：它显示一个滑块，旁边有数字输入框，人们可以拖动来获取大致数值，也可以输入精确数值。当没有最小值或最大值时，会只显示输入框。

## 解剖结构 {#anatomy}

1. **标签**：可选，位于滑块上方
2. **轨道**：整个范围，从最小值到最大值
3. **指示器**：轨道中已填充的部分，直到当前值
4. **标记**：可选，轨道上每个步骤的一个点
5. **滑块按钮**：用户拖动的圆形按钮，表示当前值
6. **工具提示**：在用户拖动或聚焦滑块时显示滑块上方的当前值
7. **提示**：可选的帮助文本，位于滑块下方

## 变体 {#variants}

### 尺寸 {#size}

有两种尺寸：小号（默认）和中号。它们在滑块按钮的大小上有所不同。小号适合用于行和表单中，这是大多数前端滑块所使用的场景。

`ha-slider` 的实时演示。

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](https://contributors.home-assistant.io/design/components/slider/)。

```html
<ha-slider size="s" min="0" max="100" value="40"></ha-slider>
<ha-slider size="m" min="0" max="100" value="40"></ha-slider>
```

### 步长和标记 {#steps-and-markers}

步长设置值的精细程度。步数少时，滑块可以在轨道上显示每个步骤的标记。

`ha-slider` 的实时演示。

```html
<ha-slider min="0" max="8" step="1" value="4" with-markers></ha-slider>
```

### 带标签 {#with-a-label}

滑块旁边不显示数字。它可以在上方有一个标签。

`ha-slider` 的实时演示。

```html
<ha-slider label="Volume" min="0" max="100" value="30"></ha-slider>
```

## 行为 {#behavior}

- **启用**：指示器和滑块按钮为主颜色，轨道的其余部分为禁用颜色。
- **聚焦**：键盘聚焦时，滑块按钮周围显示 2px 的实线聚焦环，并打开显示数值的工具提示。
- **拖动**：滑块按钮跟随指针移动，数值会吸附到最近的步长，并在工具提示中显示数值。
- **禁用**：轨道透明度减半。滑块显示数值，但不能更改或聚焦。
- **只读**：显示数值，不允许更改。

`ha-slider` 的实时演示。

```html
<ha-slider min="0" max="100" value="60" disabled></ha-slider>
```

滑块遵循页面的文字方向：在从右到左的语言中，最小值在右侧。

## 规格 {#specs}

| 属性 | 值 | 令牌 |
| --- | --- | --- |
| 宽度 | 200px，至少100px | 无 |
| 轨道厚度 | 4px | `--ha-slider-track-size` |
| 轨道圆角半径 | 9999px，完全圆角 | 无 |
| 拇指尺寸，小号 | 16px | 无 |
| 拇指尺寸，中号 | 20px | 无 |
| 拇指边框 | 无 | 无 |
| 标记尺寸 | 2px，轨道厚度的一半 | 无 |
| 禁用轨道不透明度 | 0.5 | 无 |
| 焦点环 | 2px 实线，围绕拇指 | `--ha-color-focus` |
| 提示距离拇指的距离 | 8px | `tooltip-distance` |

| 部件 | 颜色 |
| --- | --- |
| 轨道 | `--disabled-color`，通过 `--ha-slider-track-color` |
| 指示器 | `--primary-color`，通过 `--ha-slider-indicator-color` |
| 拇指 | `--primary-color`，通过 `--ha-slider-thumb-color` |
| 标记 | `--card-background-color` |

提示没有箭头，并使用与 [tooltip](/design/components/tooltip) 组件相同的令牌:| 属性 | 值 | 令牌 |
| --- | --- | --- |
| 背景 | 次要背景 | `--secondary-background-color`，到 `--ha-tooltip-background-color` |
| 文字 | 主要文字 | `--primary-text-color`，到 `--ha-tooltip-text-color` |
| 字体大小 | 12px | `--ha-font-size-s` |
| 内边距 | 8px | `--ha-space-2` |
| 圆角半径 | 4px | `--ha-border-radius-sm` |

## 指南 {#guidelines}

- 给滑块一个标签，标明它控制的内容，例如 **音量** 或 **速度**。
- 确保在重要时刻可以在其他地方看到当前值，例如在行中或旁边的输入框中。工具提示只在人们拖动或聚焦滑块时显示。

## 无障碍 {#accessibility}

### 键盘 {#keyboard}

| 键 | 操作 |
| --- | --- |
| <kbd>Tab</kbd> | 将焦点移到滑块上，并从滑块移开。禁用的滑块会被跳过。 |
| <kbd>向右箭头</kbd> 或 <kbd>向上箭头</kbd> | 将值增加一个步长。在从右到左的语言中，<kbd>向左箭头</kbd> 增加值。 |
| <kbd>向左箭头</kbd> 或 <kbd>向下箭头</kbd> | 将值减少一个步长。在从右到左的语言中，<kbd>向右箭头</kbd> 减少值。 |
| <kbd>向上翻页</kbd> | 将值增加范围的十分之一，至少增加一个步长。 |
| <kbd>向下翻页</kbd> | 将值减少范围的十分之一，至少减少一个步长。 |
| <kbd>Home</kbd> | 设置为最小值。 |
| <kbd>End</kbd> | 设置为最大值。 |

当滑块被禁用或只读时，按键无效。

### 焦点 {#focus}

键盘焦点在滑块上显示一个 2px 的实线焦点环，并打开显示数值的提示框。

### 目标尺寸 {#target-size}

滑块在轨道上下各有 14px 的额外触控区域，使触控目标高度为 32px。

### 屏幕阅读器 {#screen-readers}

滑块会用其标签和数值进行朗读，并根据用户语言格式化。没有标签时，它没有名称。提示会被作为描述朗读。

### 在代码中 {#in-the-code}

- 滑块的角色是 `slider`，具有 `aria-valuemin`、`aria-valuemax`、`aria-valuenow` 和 `aria-valuetext`。值文本是根据用户语言格式化的数字，或者是在设置时 `valueFormatter` 的结果。
- 可访问名称来自标签，通过 `aria-labelledby`。没有标签时，滑块没有名称。
- 提示通过 `aria-describedby` 连接。
- 工具提示中的值对屏幕阅读器是隐藏的。它们从值文本中获取。
- `aria-disabled` 遵循 `disabled`。`aria-readonly` 也遵循 `disabled`，而不是 `readonly`。

## 相关 {#related}

- [控件](/design/components/controls)：仪表板上设备使用的较大滑块
- [文本输入](/design/components/input)：用于输入精确数字
- [选择器](/design/components/selector)：数字选择器显示一个带有输入框的滑块
- [工具提示](/design/components/tooltip)：外观与数值工具提示相同

## 在代码中 {#in-code}

该元素是 `<ha-slider>`。它基于 [Web Awesome 滑块](https://webawesome.com/docs/components/slider/)。

```html
<ha-slider min="0" max="100" value="60"></ha-slider>
<ha-slider min="0" max="8" step="1" value="4" with-markers></ha-slider>
<ha-slider size="m" label="Volume"></ha-slider>
```

### 属性- `value`：当前值。默认为 `0`。 {#attributes}
- `min`：最小值。默认为 `0`。
- `max`：最大值。默认为 `100`。
- `step`：值的粒度。默认为 `1`。
- `size`：`s`（默认）或 `m`。
- `with-markers`：在每个步骤显示标记。
- `with-tooltip`：在拖动或聚焦时在工具提示中显示值。默认在 `<ha-slider>` 中启用，因此要隐藏它，请从代码中将 `withTooltip` 属性设置为 `false`。
- `tooltip-placement`：`top`（默认）、`right`、`bottom` 或 `left`。
- `tooltip-distance`：工具提示与滑块拇指的距离，以像素为单位。默认为 `8`。
- `label`：滑块上方的标签。
- `hint`：滑块下方的帮助文本。
- `disabled`：禁用滑块。
- `readonly`：显示值，但不允许用户更改。
- `orientation`：`horizontal`（默认）或 `vertical`。

- `indicator-offset`：轨道有色部分的起始值。当范围跨越零点上下时非常有用。
- `range`、`min-value` 和 `max-value`：将滑块变为具有两个滑块手柄的范围滑块。目前前端尚未使用。
- `name`：随表单提交。

工具提示显示的是普通数字。若要格式化，例如添加单位，请将 `valueFormatter` 属性设置为代码中的函数。

### 插槽 {#slots}

- `label`：带有标记的标签。仅在未设置`label`属性时使用。
- `hint`：带有标记的提示。仅在未设置`hint`属性时使用。
- `reference`：显示在轨道下方的标签，如最小值和最大值。

### 事件 {#events}

- `input`：在用户拖动时会持续触发。
- `change`：在用户释放时触发，并提交值。

从元素上的`value`读取新值。前端的大多数滑块仅作用于`change`，并在用户释放后应用该值。

### 样式 {#styling}

- `--ha-slider-track-size`：滑轨的厚度。默认值为 `4px`。
- `--ha-slider-track-color`：滑轨的颜色。默认值为 `var(--disabled-color)`。
- `--ha-slider-indicator-color`：滑轨已填充部分的颜色。默认值为 `var(--primary-color)`。
- `--ha-slider-thumb-color`：滑块的颜色。默认值为 `var(--primary-color)`。

滑块默认宽度为 200 像素，最小宽度为 100 像素。设置元素的 `width` 可以更改宽度。

来源: [`src/components/ha-slider.ts`](https://github.com/home-assistant/frontend/blob/dev/src/components/ha-slider.ts)
