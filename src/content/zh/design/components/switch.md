---
title: 开关
description: 开关可以将单一设置打开或关闭。
sidebarGroup: 输入
---

# 开关 {#switch}

Live 演示 `ha-switch`。

```html
<ha-switch checked></ha-switch>
<ha-switch></ha-switch>
<ha-switch checked disabled></ha-switch>
<ha-switch disabled></ha-switch>
```

## 概述 {#overview}

开关可以开启或关闭某个设置，例如在启动时启动应用程序或启用自动更新。用户应该能够仅通过开关本身判断其状态，因此该设置需要在开启或关闭时都具有意义。

## 何时使用 {#when-to-use}

使用开关适用于：

- 具有两个状态的设置：开启和关闭
- 可立即生效的设置，这也是 Home Assistant 中大多数开关的工作方式

不适用开关的情况：

- 在两个或多个非开关状态之间进行选择。请使用 [选择框](/design/components/select-box) 或其他选择组件。
- 从列表中选择多个项目。请使用复选框。
- 执行某个动作，例如重新启动某个内容。请使用 [按钮](/design/components/button)。
- 在仪表板或更多信息对话框中控制设备。前端对此有更大的 `<ha-control-switch>`，参见 [控件](/design/components/controls)。

## 解剖结构 {#anatomy}

1. **轨道**：显示开关是否开启的圆形背景
2. **拇指**：当开关开启时移动到末端，当开关关闭时返回起点的圆圈
3. **标签**：开关旁边的可选文字
4. **提示**：开关下方的可选帮助文字

## 变体 {#variants}

该开关没有变体。它可以自带标签，或者位于一个包含标签的设置行中。

### 无标签 {#without-a-label}

在前端，大多数开关位于设置行的末端，左侧有设置名称和简短描述。行本身承担标签作用，因此开关本身没有文字。

### 有标签 {#with-a-label}

你也可以将标签放在开关内部，作为其内容。这样点击标签也会切换开关状态。

`ha-switch` 的实时演示。

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](https://contributors.home-assistant.io/design/components/switch/)。

```html
<ha-switch checked>Start on boot</ha-switch>
<ha-switch>Automatic updates</ha-switch>
```

## 行为 {#behavior}

- **关闭**：滑块位于轨道起点，轨道使用安静的中性色填充。
- **开启**：滑块位于轨道末端，轨道使用主色。
- **悬停**：轨道和滑块变为悬停颜色。键盘聚焦使用相同颜色。
- **聚焦**：键盘聚焦时在轨道周围显示 2px 实线聚焦环，环位于轨道外 2px。
- **禁用**：轨道和滑块的透明度降低到 30%，标签颜色变为禁用文本颜色。但标签本身不变暗，因此保持可读。
- **必填**：必填开关必须开启才能使表单有效。其标签带有 `*` 标记。

滑块在 150ms 内从一端滑动到另一端。在从右到左的语言中，开启和关闭是镜像的：开启在左侧。开关表示更改会立即生效。如果更改仅在**保存**后生效，请明确说明，例如将开关放在带有明显保存按钮的表单中。

在支持的设备上，切换开关时还可以提供轻微振动反馈。

`ha-switch` 的现场演示。

```html
<ha-switch checked disabled>Start on boot</ha-switch>
<ha-switch disabled>Automatic updates</ha-switch>
```

## 规格 {#specs}

| 属性 | 值 | 令牌 |
| --- | --- | --- |
| 滑轨高度 | 24像素 | `--ha-switch-size` |
| 滑轨宽度 | 48像素 | `--ha-switch-width` |
| 滑轨圆角 | 完全圆角，与滑轨高度相等 | 无 |
| 拇指大小 | 18像素 | `--ha-switch-thumb-size` |
| 拇指阴影 | 小阴影 | `--ha-box-shadow-s`，通过 `--ha-switch-thumb-box-shadow` |
| 滑轨和拇指边框宽度 | 1像素 | `--ha-border-width-sm` |
| 开关与标签之间的间距 | 0.5em | 无 |
| 触控目标 | 至少40像素乘40像素 | `--ha-switch-min-touch-size` |
| 不可用状态的滑轨和拇指不透明度 | 0.3 | `--ha-switch-disabled-opacity` |
| 聚焦环 | 2像素实线，偏移2像素 | `--ha-color-focus` |
| 拇指动画 | 150毫秒，缓动 | `--ha-animation-duration-fast` || 状态 | 轨道 | 轨道边框 | 滑块及滑块边框 |
| --- | --- | --- | --- |
| 关闭 | `--ha-color-fill-disabled-quiet-resting` | `--ha-color-border-neutral-normal` | `--ha-color-on-neutral-normal` |
| 关闭，悬停或聚焦 | `--ha-color-fill-disabled-quiet-hover` | `--ha-color-border-neutral-normal` | `--ha-color-on-neutral-normal` |
| 打开 | `--ha-color-fill-primary-normal-resting` | `--ha-color-border-primary-loud` | `--ha-color-on-primary-normal` |
| 打开，悬停或聚焦 | `--ha-color-fill-primary-normal-hover` | `--ha-color-border-primary-loud` | `--ha-color-on-primary-normal` |

这些颜色都可以通过 `--ha-switch-*` 属性覆盖，详情请参见 [样式](/design/components/switch#styling)。

## 指南 {#guidelines}

- 仅在更改立即生效时让开关振动。当用户仍需保存时不要振动。

## 无障碍功能 {#accessibility}

### 键盘 {#keyboard}

| 键 | 操作 |
| --- | --- |
| <kbd>Tab</kbd> | 将焦点移动到开关，并移出开关。禁用的开关会被跳过。 |
| <kbd>Space</kbd> | 切换开关。 |
| <kbd>Arrow right</kbd> | 打开开关。在从右到左的语言环境中，会关闭开关。 |
| <kbd>Arrow left</kbd> | 关闭开关。在从右到左的语言环境中，会打开开关。 |

### 焦点 {#focus}

焦点环显示在轨道周围，仅在使用键盘时出现。

### 目标大小 {#target-size}

轨道为 48px x 24px。其周围的不可见区域使触摸目标至少为 40px x 40px。

### 屏幕阅读器 {#screen-readers}

屏幕阅读器会宣布一个开关、它的标签，以及它是开启还是关闭状态。提示会作为其描述被读取。没有自己标签的开关，例如位于设置行末尾的开关，需要在代码中命名，见下文。

### 在代码中 {#in-the-code}

- 焦点被委托给组件内的原生复选框。
- 原生复选框的角色是 `switch`，并且 `aria-checked` 设置为 `true` 或 `false`。
- 默认插槽中的文本是可访问名称，因为它与复选框位于同一个 `<label>`。
- 如果默认插槽中没有文本，该开关就没有自己的名称。`title` 属性会传递给复选框，然后它就是复选框的唯一名称。
- 提示通过 `aria-describedby` 连接到复选框。

## 相关内容 {#related}

- [控件](/design/components/controls)：仪表板上设备的更大开关
- [选择框](/design/components/select-box)：在选项之间进行选择
- [按钮](/design/components/button)：执行操作而不是设置
- [选择器](/design/components/selector)：布尔选择器显示为开关

## 在代码中 {#in-code}

该元素是 `<ha-switch>`。它基于 [Web Awesome 开关](https://webawesome.com/docs/components/switch/)。

```html
<ha-switch checked></ha-switch>
<ha-switch disabled></ha-switch>
<ha-switch haptic>Start on boot</ha-switch>
```

### 属性 {#attributes}

- `checked`：打开开关。
- `disabled`：禁用开关。
- `required`：使开关为必填：表单要有效，开关必须打开。
- `haptic`：切换开关时发出轻微振动。仅在变化立即生效时使用。
- `hint`：开关下方的帮助文本。
- `name` 和 `value`：随表单提交，就像原生复选框一样。

### 插槽 {#slots}

- 默认: 标签。
- `hint`: 带标记的提示。此插槽中的内容将替换 `hint` 属性的文本。

### 事件 {#events}

- `change`: 当开关切换时触发。从元素的 `checked` 读取新的状态。
- `input`: 当开关收到输入时触发。

### 样式 {#styling}

默认颜色遵循主题，因此在大多数情况下你不需要这些。

- `--ha-switch-size`：轨道的高度。默认为 `24px`。
- `--ha-switch-width`：轨道的宽度。默认为 `48px`。
- `--ha-switch-thumb-size`：滑块的大小。默认为 `18px`。
- `--ha-switch-thumb-box-shadow`：滑块的阴影。默认为 `var(--ha-box-shadow-s)`。
- `--ha-switch-disabled-opacity`：开关被禁用时的透明度。默认为 `0.3`。
- `--ha-switch-min-touch-size`：开关周围触控目标的最小尺寸。默认为 `40px`。
- `--ha-switch-required-marker`：必填开关标签后的标记。默认为 `"*"`。
- `--ha-switch-required-marker-offset`：必填标记前的间距。默认为 `0.1rem`。

轨道、滑块和边框的颜色。每个都有一个 `-hover` 的版本，用于指针悬停在开关上时，`--ha-switch-border-color` 除外：

- 关闭：`--ha-switch-background-color`、`--ha-switch-border-color`、`--ha-switch-thumb-background-color` 和 `--ha-switch-thumb-border-color`。
- 打开：`--ha-switch-checked-background-color`、`--ha-switch-checked-border-color`、`--ha-switch-checked-thumb-background-color` 和 `--ha-switch-checked-thumb-border-color`。来源: [`src/components/ha-switch.ts`](https://github.com/home-assistant/frontend/blob/dev/src/components/ha-switch.ts)
