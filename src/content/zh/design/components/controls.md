---
title: 控制
description: 大而易于触控的控件，用于操作设备，比如更多信息对话框中的切换开关和滑块。
sidebarGroup: 显示数值
sidebarGroup: 数值展示

---


# 控制 {#controls}
Live 演示 `ha-control-switch`、`ha-svg-icon`、`ha-control-slider`、`ha-control-circular-slider`。

```html
<ha-control-switch vertical reversed checked label="Light" style="height: 280px; --control-switch-thickness: 110px; --control-switch-border-radius: var(--ha-border-radius-6xl); --control-switch-padding: 6px; --mdc-icon-size: 24px">
  <ha-svg-icon slot="icon-on" path="M12,2A7,7 0 0,0 5,9C5,11.38 6.19,13.47 8,14.74V17A1,1 0 0,0 9,18H15A1,1 0 0,0 16,17V14.74C17.81,13.47 19,11.38 19,9A7,7 0 0,0 12,2M9,21A1,1 0 0,0 10,22H14A1,1 0 0,0 15,21V20H9V21Z"></ha-svg-icon>
  <ha-svg-icon slot="icon-off" path="M12,2C9.76,2 7.78,3.05 6.5,4.68L16.31,14.5C17.94,13.21 19,11.24 19,9A7,7 0 0,0 12,2M3.28,4L2,5.27L5.04,8.3C5,8.53 5,8.76 5,9C5,11.38 6.19,13.47 8,14.74V17A1,1 0 0,0 9,18H14.73L18.73,22L20,20.72L3.28,4M9,20V21A1,1 0 0,0 10,22H14A1,1 0 0,0 15,21V20H9Z"></ha-svg-icon>
</ha-control-switch>
<ha-control-slider vertical value="60" unit="%" label="Brightness" style="height: 280px; --control-slider-thickness: 110px; --control-slider-border-radius: var(--ha-border-radius-6xl)"></ha-control-slider>
<ha-control-circular-slider value="21" current="19" min="10" max="30" step="0.5" label="Target temperature" style="width: 240px"></ha-control-circular-slider>
```

## 概览 {#overview}
此控制系列旨在通过手工操作设备，无论是用手指还是鼠标。控件体积较大，具有较大的点击区域，并且对拖动和滑动有反应，而不仅仅是点击。你可以在两个地方找到它们：

- 在 **更多信息对话框** 中，一个大控件占据中心位置：灯光的垂直亮度滑块、圆形恒温器旋钮、开关的切换按钮。
- 在 **磁贴卡片的功能** 中，一个较小的水平版本位于实体下方，例如亮度滑块或一排模式按钮。

## 使用时机 {#when-to-use}
使用控件的场景：

- 屏幕的主要功能是改变设备状态
- 瓷贴卡片的一个功能

不要使用控件的场景：

- 表单和设置。请使用常规表单控件，例如 [按钮](/design/components/button)、[开关](/design/components/switch) 或 [滑块](/design/components/slider)。在设置表单中使用这个系列的控件显得不合适，占用空间远超所需。
- 具有多种选项的设备的二级设置。请使用 [选择菜单](/design/components/select-menu)。

## 解剖结构 {#anatomy}
所有控件的外观相同：

1. **轨道**：圆角形状，带有浅色调
2. **活跃部分**：全彩显示的部分，比如滑块的填充、开关的旋钮或选中的选项
3. **内容**：图标、数值或标签，取决于控件

它们的颜色可以设置，以匹配实体的状态，例如灯的颜色。

## 变体 {#variants}
### 控制按钮 {#control-button}
带有图标的方形按钮，用于单一操作，如 **打开**、**停止** 或 **锁定**。它是动作行的构建块，例如遮盖物的打开、停止和关闭按钮。

`ha-control-button`、`ha-svg-icon` 的实时演示。

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](/design/components/controls)。

```html
<ha-control-button label="Open" style="width: 64px; height: 64px; --control-button-border-radius: var(--ha-border-radius-xl); --mdc-icon-size: 24px">
  <ha-svg-icon path="M7,15L12,10L17,15H7Z"></ha-svg-icon>
</ha-control-button>
<ha-control-button label="Stop" style="width: 64px; height: 64px; --control-button-border-radius: var(--ha-border-radius-xl); --mdc-icon-size: 24px">
  <ha-svg-icon path="M18,18H6V6H18V18Z"></ha-svg-icon>
</ha-control-button>
<ha-control-button label="Close" style="width: 64px; height: 64px; --control-button-border-radius: var(--ha-border-radius-xl); --mdc-icon-size: 24px">
  <ha-svg-icon path="M7,10L12,15L17,10H7Z"></ha-svg-icon>
</ha-control-button>
<ha-control-button label="Disabled" disabled style="width: 64px; height: 64px; --control-button-border-radius: var(--ha-border-radius-xl); --mdc-icon-size: 24px">
  <ha-svg-icon path="M18,18H6V6H18V18Z"></ha-svg-icon>
</ha-control-button>
```

前端有一个单独的组组件，可将控制按钮排列成行或列。在这些演示中不可用。

### 控制开关 {#control-switch}
一个大型的开关。用于设备的主要切换。在更多信息对话框中，它直立显示并且方向相反，所以开的位置在顶部。在磁贴卡功能中，它是水平放置的。

`ha-control-switch`, `ha-svg-icon` 的实时演示。

```html
<ha-control-switch label="Power" style="width: 240px; height: 42px">
  <ha-svg-icon slot="icon-on" path="M7,2V13H10V22L17,10H13L17,2H7Z"></ha-svg-icon>
  <ha-svg-icon slot="icon-off" path="M17,10H13L17,2H7V4.18L15.46,12.64M3.27,3L2,4.27L7,9.27V13H10V22L13.58,15.86L17.73,20L19,18.73L3.27,3Z"></ha-svg-icon>
</ha-control-switch>
<ha-control-switch checked label="Power" style="width: 240px; height: 42px">
  <ha-svg-icon slot="icon-on" path="M7,2V13H10V22L17,10H13L17,2H7Z"></ha-svg-icon>
  <ha-svg-icon slot="icon-off" path="M17,10H13L17,2H7V4.18L15.46,12.64M3.27,3L2,4.27L7,9.27V13H10V22L13.58,15.86L17.73,20L19,18.73L3.27,3Z"></ha-svg-icon>
</ha-control-switch>
```

### 控制滑块 {#control-slider}
用于范围内数值的粗滑块，例如亮度、音量或封面的位移。当有人拖动它时，会显示一个数值提示。

模式设置数值的显示方式：

- **起始**（默认）：从起始位置填充。适用于量的显示，例如亮度。
- **结束**：从结束位置填充。封面位置滑块使用此模式，使滑块从顶部向下填充，就像封面本身。
- **光标**：仅显示一个标记，不填充。用于没有“更多”或“更少”的情况，例如色温或倾斜位置。

`ha-control-slider`的实时演示。

```html
<ha-control-slider vertical value="70" label="Start" style="height: 240px; --control-slider-thickness: 90px; --control-slider-border-radius: var(--ha-border-radius-6xl)"></ha-control-slider>
<ha-control-slider vertical mode="end" value="70" label="End" style="height: 240px; --control-slider-thickness: 90px; --control-slider-border-radius: var(--ha-border-radius-6xl)"></ha-control-slider>
<ha-control-slider vertical mode="cursor" value="70" label="Cursor" style="height: 240px; --control-slider-thickness: 90px; --control-slider-border-radius: var(--ha-border-radius-6xl)"></ha-control-slider>
```

横向版本是块卡片功能所使用的：

`ha-control-slider`的实时演示。

```html
<ha-control-slider value="40" unit="%" label="Brightness" style="width: 320px; --control-slider-thickness: 42px"></ha-control-slider>
```

### 控制圆形滑块 {#control-circular-slider}
一个底部开口的圆形刻度盘，用于目标值，例如温度或湿度。它还可以在轨道上显示当前值的小点，让人们看到当前的位置和目标位置。

刻度盘本身不显示文字。在更多信息对话框中，目标值和当前值由周围组件显示在刻度盘中央。

模式设置哪一部分轨道被填充，就像滑块一样。恒温器在加热时从起始位置填充，在制冷时从末端填充，当方向无关紧要时填充整个轨道。在双控版本中，刻度盘有两个滑柄，一个低值一个高值，用于同时表示加热和制冷的范围。

`ha-control-circular-slider` 的实时演示。

```html
<ha-control-circular-slider value="21" current="19" min="10" max="30" step="0.5" label="Heat to" style="width: 200px; --control-circular-slider-color: var(--state-climate-heat-color, #ff8100)"></ha-control-circular-slider>
<ha-control-circular-slider mode="end" value="23" current="26" min="10" max="30" step="0.5" label="Cool to" style="width: 200px; --control-circular-slider-color: var(--state-climate-cool-color, #2b9af9)"></ha-control-circular-slider>
<ha-control-circular-slider dual low="19" high="24" current="21" min="10" max="30" step="0.5" low-label="Heat to" high-label="Cool to" style="width: 200px; --control-circular-slider-low-color: var(--state-climate-heat-color, #ff8100); --control-circular-slider-high-color: var(--state-climate-cool-color, #2b9af9)"></ha-control-circular-slider>
```

### 控制数字按钮 {#control-number-buttons}
带有减号和加号按钮的数值，用于小而精确的调节。磁贴卡的目标温度功能就使用它。当人们通过一步或两步调整数值，而不是跨范围跳跃时使用它。

`ha-control-number-buttons` 的实时演示。

```html
<ha-control-number-buttons value="21" min="10" max="30" step="0.5" unit="°C" label="Target temperature" style="width: 220px; height: 42px"></ha-control-number-buttons>
<ha-control-number-buttons value="21" min="10" max="30" step="0.5" unit="°C" label="Target temperature" disabled style="width: 220px; height: 42px"></ha-control-number-buttons>
```

### 控制选择 {#control-select}
一行或一列选项，其中一个被选中，如风扇的速度或报警面板的模式。每个选项显示一个图标、一个标签或两者兼有。被选中的选项会填充颜色。

适用于用户经常切换的少量选项。在更多信息对话框中，它是竖直排列的，每步显示一个选项。对于具有更多选项的次要设置，例如温控器的预设或摆动模式，更信息对话框会使用[选择菜单](/design/components/select-menu)。

这些选项只能通过代码设置，因此这里没有实时演示。

## 行为- **悬停**：控件开关轨道的色调会增强，从 20% 增加到 40%。控件选择的选项会显示颜色的 20% 色调。 {#behavior}
- **聚焦**：键盘聚焦时在控件周围显示 2px 的环。控件开关、滑块和选择控件使用它们自己的颜色作为环色。控件按钮和数字按钮使用次要文本颜色。圆形滑块通过加粗聚焦的弧来显示聚焦，从 24px 增加到 28px。
- **按下**：当用户拖动滑块时，会显示带值的工具提示。松手后工具提示消失。使用键盘时，按键时显示，松开后半秒消失。
- **滑动**：控件开关可通过向对应方向滑动来开启或关闭，也可以通过点击切换。
- **禁用**：每个控件以自己的方式处理禁用状态：- 控件按钮将其图标变为禁用文本颜色，在禁用颜色的 20% 色调上显示。
- 控件开关的透明度降低到 50%。
- 控件选择将其文本和选中选项变为禁用颜色。
- 数字按钮的文本变为禁用颜色。减号和加号按钮的透明度降低到 40%。
- 圆形滑块仅显示轨道和当前值的点，不显示彩色弧线和滑块手柄。
- 控件滑块忽略拖动和点击，但外观没有变化。
- **限制**：减号和加号按钮在达到最小值和最大值时会禁用自身。当数字按钮宽度小于 100 像素时，单位会被隐藏。
- **非活动**：对于关闭的设备，圆形滑块可以隐藏彩色弧线。

- **只读**：只读循环滑块显示其数值，但忽略拖动和点击。键盘仍然可以改变数值。

大多数过渡持续180毫秒，缓入缓出。循环滑块的弧线移动时间为300毫秒。

## 规格 {#specs}
### 默认尺寸 {#default-sizes}
所有控件都填充其容器。以下默认值是在未设置尺寸时的效果。

| 控件 | 默认尺寸 | 圆角半径 | Token |
| --- | --- | --- | --- |
| 控件按钮 | 40px x 40px，8px 内边距 | 8px | `--ha-border-radius-md` 至 `--control-button-border-radius` |
| 控件开关 | 40px 厚 | 12px | `--ha-border-radius-lg` 至 `--control-switch-border-radius` |
| 控件滑块 | 40px 厚 | 8px | `--ha-border-radius-md` 至 `--control-slider-border-radius` |
| 控件圆形滑块 | 320px 宽 | 圆形轨道端 | 无 |
| 控件数字按钮 | 卡片功能的高度，按钮宽 35px | 8px | `--ha-border-radius-md` 至 `--control-number-buttons-border-radius` |
| 控件选择器 | 40px 厚，4px 内边距 | 10px | `--control-select-border-radius` |在更多信息对话框中，垂直控件厚度为130像素，高度可达320像素，角为36像素（`--ha-border-radius-6xl`）。在磁贴卡功能中，水平控件厚度为42像素。磁贴卡图标旁边的功能内联保持图标的高度36像素，除非该卡为其保留了一行。

### 颜色 {#color}
| 部位 | 颜色 | 令牌 |
| --- | --- | --- |
| 轨迹色 | 禁用颜色，20% 不透明度（圆形滑块为 30%） | `--disabled-color` |
| 活动部分 | 主色 | `--primary-color`，通过每个控件的 color 属性 |
| 控件按钮图标 | 主要文本颜色 | `--primary-text-color`，通过 `--control-button-icon-color` |
| 控制开关的旋钮图标 | 白色 | 无 |
| 控件选择的已选选项文本 | 白色 | 无 |
| 滑块和圆形滑块的手柄 | 白色 | 无 |
| 圆形滑块的当前值点 | 主要文本颜色，50% 不透明度 | `--primary-text-color` |
| 滑块提示 | 透明背景，主要文本颜色，12px 圆角 | `--clear-background-color`，`--ha-border-radius-lg` |

### 其他部分 {#other-parts}
| 属性 | 值 | 令牌 |
| --- | --- | --- |
| 图标尺寸 | 20px，数字按钮为16px | `--mdc-icon-size` |
| 开关旋钮 | 轨道的一半，内嵌4px | `--control-switch-padding` |
| 开关最小触控区域 | 40px | `--control-switch-min-touch-size` |
| 圆形滑块轨道 | 24px 宽，270 度，底部开放 | 无 |
| 圆形滑块周围的额外点击区域 | 12px | `--control-circular-slider-interaction-margin` |
| 滑块手柄 | 4px 宽，带有 `show-handle` | 无 |

## 指南 {#guidelines}
为每个控件提供一个标签。大多数控件只显示图标或数值，而标签是屏幕阅读器会朗读的内容。

## 可访问性 {#accessibility}
### 键盘| 控件 | 键 | {#keyboard}
| --- | --- |
| 控件按钮 | <kbd>Tab</kbd> 聚焦，<kbd>Enter</kbd> 或 <kbd>Space</kbd> 选择。它是一个原生按钮。 |
| 控件开关 | <kbd>Enter</kbd> 或 <kbd>Space</kbd> 切换。沿其方向的箭头键可以开关，依据开关的方向和文本方向操作。 |
| 控件滑块 | 箭头键移动一步。<kbd>Page up</kbd> 和 <kbd>Page down</kbd> 移动范围的10%。<kbd>Home</kbd> 和 <kbd>End</kbd> 移动到最小值和最大值。在从右到左的语言中，左右键互换。 |
| 控件环形滑块 | 每个滑块都使用与控件滑块相同的按键。 |
| 控制数字按钮 | 与控制滑块相同的按键。减号和加号按钮不在标签顺序中：键盘操作作用于数值。 |
| 控制选择 | <kbd>Tab</kbd> 聚焦所选选项，如果没有选择则聚焦第一个。箭头键在选项之间移动焦点，<kbd>Enter</kbd> 或 <kbd>Space</kbd> 选择聚焦的选项。 |

只有控制滑块会在从右到左的语言中交换左箭头和右箭头键。圆形滑块和数字按钮不会。

### 焦点 {#focus}
键盘焦点在控件周围显示2像素的环，或在圆形滑块上显示更厚的弧线。有关颜色，请参见 [行为](/design/components/controls#behavior)。

禁用的控件开关或数字按钮仍然保留在 Tab 顺序中。禁用的控件选择框保留一个选项在 Tab 顺序中，但忽略键盘操作和选择。滑块控件在禁用时仍可聚焦，并继续响应键盘操作。

### 目标大小 {#target-size}
控件按钮、开关、滑块和选择框在默认情况下在其最小方向上为 40px。控件开关保持至少 40px × 40px 的触控区域。圆形滑块在其轨道周围增加 12px 的命中区域。

### 屏幕阅读器 {#screen-readers}
每个控件都会通过其标签、类型和值进行提示：例如按钮、开关（开或关）、带有格式化值的滑块、带有值及单位的旋钮按钮，或带有选中选项的一组单选按钮。数字按钮的减号和加号按钮会以英语进行提示，分别为“decrement”和“increment”。在双圆形滑块上，两个滑块手柄都会提示低标签。

### 在代码中| 控件 | 角色 | 名称和状态 | {#in-the-code}
| --- | --- | --- |
| 控件按钮 | `button` | `label` 作为 `aria-label`，并作为本地工具提示 |
| 控件开关 | `switch` | `label` 作为 `aria-label`，`aria-checked`。旋钮及其图标对屏幕阅读器隐藏。 |
| 控件滑块 | `slider` | `label` 作为 `aria-label`，`aria-valuenow`，`aria-valuemin`，`aria-valuemax`，`aria-orientation`，以及 `aria-valuetext` 与格式化值 |
| 控件圆形滑块 | `slider` 在每个手柄上 | `low-label`，或当没有 `low-label` 时为 `label`，作为 `aria-label` 在两个手柄上 (`high-label` 未使用)，`aria-valuenow` 从 `value`（带 `dual` 时无），`aria-valuemin`，`aria-valuemax`，`aria-disabled`，和 `aria-readonly` |
| 控件数字按钮 | `spinbutton` | `label` 作为 `aria-label`，`aria-valuenow`，`aria-valuemin`，`aria-valuemax`，以及 `aria-valuetext` 带有值和单位。减号和加号按钮被命名为“减小”和“增加”。 |
| 控制选择 | `radiogroup`，每个选项都有一个 `radio` | `label` 命名该组。每个选项由其 `ariaLabel` 或 `label` 命名，并具有 `aria-checked`。 |

## 相关内容 {#related}
- [选择菜单](/design/components/select-menu)：控件系列的下拉菜单
- [控件滑块](/design/components/control-scrubber)：适用于环状范围（如色相）的系列成员
- [滑块](/design/components/slider)、[开关](/design/components/switch)、[按钮](/design/components/button)：常规表单控件
- [瓦片卡片](/design/dashboards/tile-card)：较小控件显示为功能的位置

## 在代码中 {#in-code}
所有控件默认填充它们的容器。使用 CSS 调整其大小：在元素上设置 `height` 和 `width`，以及有自定义属性的那部分厚度。垂直控件的宽度由厚度决定，需要设置高度。

在更多信息对话框中，垂直控件厚130像素，高度最高为320像素，角为 `--ha-border-radius-6xl`。在瓦片卡片功能中，水平控件厚42像素。

### ha-control-button {#ha-control-button}
```html
<ha-control-button label="Open">
  <ha-svg-icon path="..."></ha-svg-icon>
</ha-control-button>
```

属性：

- `label`: 可访问名称，也显示为本地工具提示。
- `disabled`: 禁用按钮。

插槽：

- 默认：内容，通常是 `ha-svg-icon`。

事件：监听常规的 `click` 事件。

样式：

- `--control-button-icon-color`: 默认值为 `var(--primary-text-color)`。
- `--control-button-background-color`: 默认值为 `var(--disabled-color)`。
- `--control-button-background-opacity`: 默认值为 `0.2`。
- `--control-button-border-radius`: 默认值为 `var(--ha-border-radius-md)`。
- `--control-button-focus-color`: 焦点环。默认值为 `var(--secondary-text-color)`。
- `--control-button-padding`: 默认值为 `8px`。
- `--control-button-font-weight`: 用于文本标签。默认值为 `var(--ha-font-weight-medium)`。
- `--mdc-icon-size`: 图标大小。默认值为 `20px`。

默认大小为 40 x 40 像素。

### ha-control-switch {#ha-control-switch}
```html
<ha-control-switch vertical reversed checked label="Light">
  <ha-svg-icon slot="icon-on" path="..."></ha-svg-icon>
  <ha-svg-icon slot="icon-off" path="..."></ha-svg-icon>
</ha-control-switch>
```

属性：

- `checked`：开关已开启。
- `label`：可访问名称。
- `vertical`：开关保持竖直。
- `reversed`：翻转方向。竖直和反转时顶部为开。
- `disabled`：禁用开关。
- `touch-action`：滑动的 CSS `touch-action`。默认值为 `pan-y`，垂直时为 `pan-x`。

这些只能作为属性设置：

- `pathOn` 和 `pathOff`：图标的 SVG 路径数据。使用这些，或者使用插槽。

插槽：

- `icon-on`：开启时的图标。
- `icon-off`：关闭时的图标。

事件：

- `change`：开关被切换，通过选择、滑动或键盘操作。新状态可从 `checked` 获取。

样式:- `--control-switch-on-color`：默认为 `var(--primary-color)`。
- `--control-switch-off-color`：默认为 `var(--disabled-color)`。
- `--control-switch-background-opacity`：滑轨的色调。默认为 `0.2`。
- `--control-switch-hover-background-opacity`：悬停时的色调。默认为 `0.4`。
- `--control-switch-thickness`：默认为 `40px`。
- `--control-switch-min-touch-size`：默认为 `40px`。
- `--control-switch-border-radius`：默认为 `var(--ha-border-radius-lg)`。
- `--control-switch-padding`：旋钮周围的间距。默认为 `4px`。
- `--mdc-icon-size`：图标大小。默认为 `20px`。

### ha-control-slider {#ha-control-slider}
```html
<ha-control-slider vertical value="60" unit="%" label="Brightness"></ha-control-slider>
```

属性：- `value`：当前值。
- `min`：默认值为 `0`。
- `max`：默认值为 `100`。
- `step`：默认值为 `1`。
- `label`：可访问名称。
- `unit`：在工具提示中值后显示。
- `mode`：`start`（默认）、`end` 或 `cursor`。
- `vertical`：使滑块直立。
- `inverted`：翻转值的方向。
- `show-handle`：在填充末端显示手柄。
- `tooltip-mode`：`interaction`（默认）在拖动时显示值，`always` 保持可见，`never` 隐藏。
- `tooltip-position`：`top`、`bottom`、`left` 或 `right`。默认值为 `top`，垂直时为 `left`。
- `round-value`：将显示和宣布的值舍入为整数，而手柄仍会吸附到 `step`。当 `step` 是小数，但实际值是整数时使用。

- `touch-action`: CSS `touch-action`。默认值为 `pan-y`，垂直时为 `pan-x`。
- `disabled`: 禁用滑块。

`locale` 属性用于格式化值，只能通过代码设置。

插槽：

- `background`: 绘制在轨道上的内容，位于填充层后面。色温滑块使用它来显示渐变。

事件：

- `value-changed`: 值已设置，在释放时触发。`detail.value` 是新的值。
- `slider-moved`: 拖动时滑块手柄移动。`detail.value` 是手柄下的值，`undefined` 在释放时。

样式：

- `--control-slider-color`: 填充层。默认值为 `var(--primary-color)`。
- `--control-slider-background`: 轨道。默认值为 `var(--disabled-color)`。
- `--control-slider-background-opacity`: 默认值为 `0.2`。
- `--control-slider-thickness`: 默认值为 `40px`。
- `--control-slider-border-radius`: 默认值为 `var(--ha-border-radius-md)`。
- `--control-slider-inset-shadow`: 默认值为 `none`。
- `--control-slider-tooltip-font-size`: 默认值为 `var(--ha-font-size-m)`。

### ha-control-circular-slider {#ha-control-circular-slider}
```html
<ha-control-circular-slider value="21" current="19" min="10" max="30" step="0.5" label="Target temperature"></ha-control-circular-slider>

<ha-control-circular-slider dual low="19" high="24" min="10" max="30" low-label="Heat to" high-label="Cool to"></ha-control-circular-slider>
```

属性：- `value`：目标值，适用于单个滑块。
- `low` 和 `high`：两个值，配合 `dual` 使用。
- `current`：当前值，在轨道上显示为一个点。
- `min`：默认为 `0`。
- `max`：默认为 `100`。
- `step`：默认为 `1`。
- `mode`：`start`、`end` 或 `full`。设置轨道的填充部分。
- `dual`：显示两个滑块，分别用于 `low` 和 `high`。
- `label`：滑块的可访问名称。
- `low-label`：设置后，用作两个滑块的可访问名称，而不是 `label`。
- `high-label`：可接受，但未使用。
- `inactive`：隐藏彩色弧线，用于设备关闭时。
- `readonly`：显示值，但用户无法通过指针更改。键盘仍可操作。
- `disabled`：禁用旋钮。

- `prevent-interaction-on-scroll`: 在触摸屏上，只有滑块手柄会响应，并且仅在短按后才会响应，因此滑过拨盘会滚动页面而不是改变数值。

事件，每个事件在 `detail.value` 中都有新值：

- `value-changing` 和 `value-changed`: 拖动时，以及释放时。
- `low-changing` 和 `low-changed`: 低手柄的情况相同。
- `high-changing` 和 `high-changed`: 高手柄的情况相同。

样式：

- `--control-circular-slider-color`: 填充。默认值为 `var(--primary-color)`。
- `--control-circular-slider-low-color` 和 `--control-circular-slider-high-color`: 两个带 `dual` 的填充。默认值为上面的颜色。
- `--control-circular-slider-background`: 轨道。默认值为 `var(--disabled-color)`。
- `--control-circular-slider-background-opacity`: 默认值为 `0.3`。
- `--control-circular-slider-interaction-margin`: 轨道周围的额外点击区域。默认值为 `12px`。

默认宽度为 320 像素。

### ha-control-number-buttons {#ha-control-number-buttons}
```html
<ha-control-number-buttons value="21" min="10" max="30" step="0.5" unit="°C" label="Target temperature"></ha-control-number-buttons>
```

属性：

- `value`：当前值。
- `min` 和 `max`：范围。两者都是可选的。
- `step`：默认为 `1`。
- `unit`：显示在数值之后。
- `label`：无障碍名称。
- `disabled`：禁用控件。

这些只能作为属性设置：

- `locale`：用于格式化数值的本地化数据。
- `formatOptions`：`Intl.NumberFormatOptions`，例如总是显示一个小数位。

事件：

- `value-changed`：数值更改，来源于按钮或键盘。`detail.value` 是新值。

样式：

- `--control-number-buttons-background-color`：默认为 `var(--disabled-color)`。
- `--control-number-buttons-background-opacity`：默认为 `0.2`。
- `--control-number-buttons-border-radius`：默认为 `var(--ha-border-radius-md)`。
- `--control-number-buttons-focus-color`：焦点环。默认为 `var(--secondary-text-color)`。
- `--mdc-icon-size`：减号和加号图标的大小。默认为 `16px`。高度来自`--feature-height`，即卡片功能的高度。在卡片功能之外，设置`height`。

### ha-control-select {#ha-control-select}
```ts
html`<ha-control-select
  .options=${[
    { value: "low", label: "Low", path: mdiFanSpeed1 },
    { value: "high", label: "High", path: mdiFanSpeed3 },
  ]}
  .value=${"low"}
  .label=${"Fan speed"}
  @value-changed=${this._speedChanged}
></ha-control-select>`
```

属性：

- `value`：所选选项的`value`。
- `label`：组的可访问名称。
- `vertical`：以列显示选项。
- `hide-option-label`：仅显示图标。标签仍作为可访问名称使用。
- `disabled`：禁用控件。

这些只能作为属性设置：

- `options`：选项数组。每个选项都有一个`value`，可选择地有`label`、`ariaLabel`、作为SVG的图标`path`或`icon`模板。

事件：

- `value-changed`：已选择一个选项。`detail.value`是它的`value`。

样式:- `--control-select-color`：所选的选项。默认为 `var(--primary-color)`。
- `--control-select-background`：轨道。默认为 `var(--disabled-color)`。
- `--control-select-background-opacity`：默认为 `0.2`。
- `--control-select-selected-opacity`：默认为 `1`。
- `--control-select-focused-opacity`：默认为 `0.2`。
- `--control-select-thickness`：默认为 `40px`。
- `--control-select-border-radius`：默认为 `10px`。
- `--control-select-padding`：选项周围的空间。默认为 `4px`。
- `--control-select-button-border-radius`：每个选项的角。遵循边框半径和内边距。
- `--mdc-icon-size`：默认为 `20px`。

来源：[`ha-control-button.ts`](https://github.com/home-assistant/frontend/blob/dev/src/components/ha-control-button.ts)，[`ha-control-switch.ts`](https://github.com/home-assistant/frontend/blob/dev/src/components/ha-control-switch.ts)，[`ha-control-slider.ts`](https://github.com/home-assistant/frontend/blob/dev/src/components/ha-control-slider.ts)，[`ha-control-circular-slider.ts`](https://github.com/home-assistant/frontend/blob/dev/src/components/ha-control-circular-slider.ts)，[`ha-control-number-buttons.ts`](https://github.com/home-assistant/frontend/blob/dev/src/components/ha-control-number-buttons.ts)，[`ha-control-select.ts`](https://github.com/home-assistant/frontend/blob/dev/src/components/ha-control-select.ts)，均来自 [`src/components/`](https://github.com/home-assistant/frontend/tree/dev/src/components)。
