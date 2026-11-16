---
title: 控制擦洗器
description: 一个水平控件，其数值显示在固定窗口下方，而你拖动其背后的条。适用于循环范围，例如灯光的色相。
sidebarGroup: 显示数值
---


# 控制擦洗器 {#control-scrubber}
## 概述 {#overview}
控件滑块（control scrubber）是 [control](/design/components/controls) 系列的一个成员。在普通滑块中，滑块手柄沿固定轨道移动。而在滑块条中，则相反：窗口保持在中间，背后的条带移动。拖动条带以更改数值，或点击条带上的某个点将其移到窗口下方。

条带可以比控件更宽，因此一次只能看到部分范围。这使得每像素拖动更改的数值更小，有助于在小空间内精确选择。条带还可以重复，用于循环范围，例如色相。

[tile card](/design/dashboards/tile-card) 的 **灯光颜色（Light color）** 功能使用它来选择灯光的色相。

它尚未成为本站的实时组件，因此此处没有演示。

## 何时使用 {#when-to-use}
使用控制擦拭器的情况：

- 值在循环范围内，如色相，其中结束与开始相接
- 在小空间内的值范围很广，而普通的控制滑块会太粗糙

不要使用控制擦拭器的情况：

- 量值，如亮度或音量。请使用 [控制滑块](/design/components/controls#control-slider)，其填充显示量的多少。
- 表单和设置。请使用常规 [滑块](/design/components/slider)。

## 解剖结构 {#anatomy}
1. **轨道**：控件的背景，浅色调
2. **条带**：移动的背景，如所有色调的渐变
3. **窗口**：中间的框架，用于指向当前值。它是可选的。

## 变体 {#variants}
### 循环 {#wrapping}
开启循环时，条带会重复，值在两端会循环。拖动超过360度的色相会重新回到0。不开启循环时，值会在最小值和最大值处停止。

### 有窗口和无窗口 {#with-and-without-a-window}
当有当前值需要指示时显示窗口。当没有值时关闭，如灯光关闭或者尚未有颜色时。

### 条宽 {#strip-width}
默认情况下，条的宽度与控件相同。可以将其加宽，以一次只显示部分范围。浅色功能使色调条的宽度至少是控件高度的三倍。

## 行为 {#behavior}
- **拖动**：拖动滑条会改变数值。将其向左拖动会移动滑条，使更高的数值出现在窗口下方。拖动在水平移动超过10像素后开始，因此页面的垂直滚动仍然有效。
- **点击**：点击滑条上的某一点会将该点移到窗口下方。
- **步进**：当有人拖动时，数值会跟随手指。当他们松开时，数值会自动对齐到最近的步长。
- **取消**：当系统取消拖动时，数值会恢复到原来的状态。
- **移动**：滑条会在180毫秒内以缓入缓出方式移动到新数值。当有人拖动时，滑条会立即跟随。
- **禁用**：拖动、点击和键盘操作都无效。光标会显示不允许操作。

## 规格 {#specs}
| 属性 | 数值 | 令牌 |
| --- | --- | --- |
| 高度 | 40px | `--control-scrubber-thickness` |
| 圆角 | 8px | `--ha-border-radius-md`，至 `--control-scrubber-border-radius` |
| 滑轨 | 禁用颜色，透明度 20% | `--disabled-color`，至 `--control-scrubber-rail-color` 和 `--control-scrubber-rail-opacity` |
| 条带 | 禁用颜色，或你设置的背景 | `--control-scrubber-background` |
| 条带宽度 | 控件的宽度 | `--control-scrubber-track-width` |
| 窗口 | 2px 白色边框，高度除以 2.5（默认 16px），带有小阴影 | 无 |
| 焦点环 | 2px，颜色为控件颜色 | `--control-scrubber-color`，默认 `--primary-color` |
| 动画 | 180ms，缓入缓出 | 无 |

## 指南 {#guidelines}
- 给它一个标签，并在有单位时标明单位，例如色调的度数。值没有可见文本，所以屏幕阅读器会朗读标签和单位。
- 当没有当前值时隐藏窗口，而不是指向不存在的值。

## 可访问性 {#accessibility}
### 键盘 {#keyboard}
| 键 | 操作 |
| --- | --- |
| <kbd>Tab</kbd> | 将焦点移动到滑块 |
| <kbd>右</kbd> 或 <kbd>上</kbd> | 值增加一步 |
| <kbd>左</kbd> 或 <kbd>下</kbd> | 值减少一步 |
| <kbd>向上翻页</kbd> 和 <kbd>向下翻页</kbd> | 移动范围的 10%，如果更多则移动一步 |
| <kbd>Home</kbd> | 到最小值 |
| <kbd>End</kbd> | 到最大值。 如果为循环，则在最大值之前一步，因为最大值与最小值相同 |

按键释放时会发送该值。箭头键在从右到左的语言中不会交换。

### 焦点 {#focus}
键盘焦点会在控件周围显示一个2像素的环，颜色为控件的颜色。即使被禁用，滑块仍然可以获得焦点。

### 目标尺寸 {#target-size}
整个控件都是目标，默认高度为40像素。

### 屏幕阅读器 {#screen-readers}
滑块会被读取为一个滑动条，并带有其标签和数值，数值格式包含单位，如“200°”。

### 在代码中 {#in-the-code}
滑块的角色是 `slider`，并且具有来自 `label` 的 `aria-label`、`aria-valuenow`、`aria-valuemin`、`aria-valuemax`、带格式化值和单位的 `aria-valuetext`、`aria-orientation="horizontal"` 和 `aria-disabled`。

## 相关内容 {#related}
- [控件](/design/components/controls)：其余控件家族，如控制滑块
- [颜色选择器](/design/components/color-picker)：用于色相和饱和度的色轮
- [卡片瓦片](/design/dashboards/tile-card)：滑块出现的地方，在浅色功能中

## 在代码中 {#in-code}
元素是 `<ha-control-scrubber>`。使用 CSS 自定义属性设置条带的背景：

```html
<ha-control-scrubber
  wrap
  show-handle
  min="0"
  max="360"
  unit="°"
  label="Hue"
  style="--control-scrubber-track-width: 200%"
></ha-control-scrubber>
```

```css
ha-control-scrubber {
  --control-scrubber-background: linear-gradient(
    to right,
    hsl(0 100% 50%),
    hsl(120 100% 50%),
    hsl(240 100% 50%),
    hsl(360 100% 50%)
  );
}
```

### 属性 {#attributes}
- `value`: 当前值。
- `min` 和 `max`: 范围。默认值为 `0` 和 `100`。
- `step`: 步长。默认值为 `1`。
- `wrap`: 重复条，值在两端循环。
- `show-handle`: 显示窗口。
- `round-value`: 四舍五入屏幕阅读器宣布的值。
- `label`: 可访问名称。
- `unit`: 单位，用于屏幕阅读器宣布的值。
- `disabled`: 忽略拖动、点击和键盘操作。
- `touch-action`: 条的触摸操作。默认值为 `pan-y`，因此页面仍然可以垂直滚动。

### 属性 {#properties}
- `locale`: 用于格式化值的语言环境。

### 事件 {#events}
- `value-changed`: 当拖动、点击或释放键后选择了值。
- `slider-moved`: 当有人拖动或按住键时的值。当释放键时，会触发且无值。

### 样式 {#styling}
- `--control-scrubber-color`：焦点环。默认值为 `var(--primary-color)`。
- `--control-scrubber-background`：条带。默认值为 `var(--disabled-color)`。
- `--control-scrubber-rail-color` 和 `--control-scrubber-rail-opacity`：轨道。默认值为 `var(--disabled-color)` 和 `0.2`。
- `--control-scrubber-thickness`：高度。默认值为 `40px`。
- `--control-scrubber-border-radius`：圆角。默认值为 `var(--ha-border-radius-md)`。
- `--control-scrubber-track-width`：条带的宽度。默认值为 `100%`，且不能小于此值。
- `--control-scrubber-inset-shadow`：内阴影。默认值为 `none`。

来源：[`src/components/ha-control-scrubber.ts`](https://github.com/home-assistant/frontend/blob/dev/src/components/ha-control-scrubber.ts)
