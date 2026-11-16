---
title: 选择菜单
description: 一个紧凑的下拉菜单，用于选择一个选项，比如风扇的预设或恒温器的模式。
sidebarGroup: 显示数值
sidebarGroup: 数值展示

---

# 选择菜单 {#select-menu}

实时演示 `ha-control-select-menu`，`ha-svg-icon`。

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](https://contributors.home-assistant.io/design/components/select-menu/)。

```html
<ha-control-select-menu label="Preset" value="eco" data-props='{"options": [{"value": "auto", "label": "Auto"}, {"value": "eco", "label": "Eco"}, {"value": "sleep", "label": "Sleep"}]}' style="width: 160px">
  <ha-svg-icon slot="icon" path="M8 13C6.14 13 4.59 14.28 4.14 16H2V18H4.14C4.59 19.72 6.14 21 8 21S11.41 19.72 11.86 18H22V16H11.86C11.41 14.28 9.86 13 8 13M8 19C6.9 19 6 18.1 6 17C6 15.9 6.9 15 8 15S10 15.9 10 17C10 18.1 9.1 19 8 19M19.86 6C19.41 4.28 17.86 3 16 3S12.59 4.28 12.14 6H2V8H12.14C12.59 9.72 14.14 11 16 11S19.41 9.72 19.86 8H22V6H19.86M16 9C14.9 9 14 8.1 14 7C14 5.9 14.9 5 16 5S18 5.9 18 7C18 8.1 17.1 9 16 9Z"></ha-svg-icon>
</ha-control-select-menu>
<ha-control-select-menu label="Oscillate" value="false" data-props='{"options": [{"value": "true", "label": "On", "iconPath": "M6 14H9L5 18L1 14H4C4 11.3 5.7 6.6 11 6.1V8.1C7.6 8.6 6 11.9 6 14M20 14C20 11.3 18.3 6.6 13 6.1V8.1C16.4 8.7 18 11.9 18 14H15L19 18L23 14H20Z"}, {"value": "false", "label": "Off", "iconPath": "M13 8.1V6.1C18.3 6.6 20 11.4 20 14H23L20.1 16.9L17.2 14H18C18 11.9 16.4 8.6 13 8.1M7.8 7.1L2.4 1.7L1.1 3L6.3 8.2C4.7 10 4 12.4 4 14H1L5 18L9 14H6C6 12.7 6.6 11 7.9 9.7L20.9 22.7L22.2 21.4L9.3 8.7L7.8 7.1M11 6.1L9.5 6.4L11 7.8V6.1Z"}]}' style="width: 160px"></ha-control-select-menu>
```

## 概述 {#overview}

选择菜单是一个按钮，用于显示设置及其当前值。选择它会打开包含选项的菜单。它属于 [控件](/design/components/controls) 系列：同样是圆角、带色调的外观，设计用于操作设备，而不是填写表单。

你可以在两个地方找到它：

- 在 **更多信息对话框** 中，位于主控件下方，用于设备的次要设置。例如风扇的预设、方向和摆动，或者恒温器的风扇和摆动模式。它们有几个排在一行，每个宽度为 120 到 160 像素。
- 在 **卡片功能** 中，作为模式功能的下拉样式。在那里，它占据整个卡片的宽度。

## 何时使用 {#when-to-use}

使用下拉菜单的情况：

- 设备设置中选项比一行能显示的更多时
- 用户不经常更改的设置

不使用下拉菜单的情况：

- 少量选项且用户经常切换的情况。应使用控制选择器，一次显示所有选项，参见 [控件](/design/components/controls)。
- 表单和设置。应使用常规下拉菜单。
- 动作列表。应使用 [下拉菜单](/design/components/dropdown)。

## 解剖结构 {#anatomy}

1. **容器**：带有色背景的圆形按钮
2. **图标**：所选选项的图标，或者设置的默认图标
3. **标签**：设置的名称，小号文字显示
4. **值**：所选选项的标签，位于标签下方
5. **箭头**：可选，在末端显示下拉箭头
6. **菜单**：按钮下方打开的选项列表，每个选项都有自己的图标。所选选项会被高亮显示。

## 变体 {#variants}

### 标签和值 {#label-and-value}

默认设置。标签显示设置名称，下面的值显示当前选择。

当没有值时，只显示标签，大小与值相同。

`ha-control-select-menu`、`ha-svg-icon` 的实时演示。

```html
<ha-control-select-menu label="Swing mode" data-props='{"options": [{"value": "off", "label": "Off"}, {"value": "vertical", "label": "Vertical"}, {"value": "horizontal", "label": "Horizontal"}]}' style="width: 160px">
  <ha-svg-icon slot="icon" path="M6 14H9L5 18L1 14H4C4 11.3 5.7 6.6 11 6.1V8.1C7.6 8.6 6 11.9 6 14M20 14C20 11.3 18.3 6.6 13 6.1V8.1C16.4 8.7 18 11.9 18 14H15L19 18L23 14H20Z"></ha-svg-icon>
</ha-control-select-menu>
```

### 在瓷砖卡片功能中 {#in-a-tile-card-feature}

在瓷砖卡片中，选择菜单会隐藏其标签并显示一个箭头。卡片已经说明了功能内容，因此只显示数值，末尾有一个箭头表示它会打开菜单。高度根据功能而定，为 42 像素。

`ha-control-select-menu`、`ha-svg-icon` 的现场演示。

```html
<ha-control-select-menu label="Fan mode" value="medium" hide-label show-arrow data-props='{"options": [{"value": "low", "label": "Low"}, {"value": "medium", "label": "Medium"}, {"value": "high", "label": "High"}]}' style="display: block; width: 320px; --control-select-menu-height: 42px">
  <ha-svg-icon slot="icon" path="M12,11A1,1 0 0,0 11,12A1,1 0 0,0 12,13A1,1 0 0,0 13,12A1,1 0 0,0 12,11M12.5,2C17,2 17.11,5.57 14.75,6.75C13.76,7.24 13.32,8.29 13.13,9.22C13.61,9.42 14.03,9.73 14.35,10.13C18.05,8.13 22.03,8.92 22.03,12.5C22.03,17 18.46,17.1 17.28,14.73C16.78,13.74 15.72,13.3 14.79,13.11C14.59,13.59 14.28,14 13.88,14.34C15.87,18.03 15.08,22 11.5,22C7,22 6.91,18.42 9.27,17.24C10.25,16.75 10.69,15.71 10.89,14.79C10.4,14.59 9.97,14.27 9.65,13.87C5.96,15.85 2,15.07 2,11.5C2,7 5.56,6.89 6.74,9.26C7.24,10.25 8.29,10.68 9.22,10.87C9.41,10.39 9.73,9.97 10.14,9.65C8.15,5.96 8.94,2 12.5,2Z"></ha-svg-icon>
</ha-control-select-menu>
```

## 行为 {#behavior}

- **悬停**：背景颜色会变为较深的中性色。
- **聚焦**：键盘聚焦时，按钮周围会显示2px的环，颜色为次文本色。
- **打开**：选择按钮会在其下方打开菜单。菜单的宽度至少与按钮一样宽。
- **已选择**：在菜单中，被选中的选项以中等粗细显示并使用主色，背景为浅主色。
- **禁用**：按钮的文本显示为禁用颜色，并且不会打开菜单。当实体不可用时，“更多信息”对话框会禁用按钮。

`ha-control-select-menu`、`ha-svg-icon` 的实时演示。

```html
<ha-control-select-menu label="Preset" value="eco" disabled data-props='{"options": [{"value": "eco", "label": "Eco"}]}' style="width: 160px">
  <ha-svg-icon slot="icon" path="M8 13C6.14 13 4.59 14.28 4.14 16H2V18H4.14C4.59 19.72 6.14 21 8 21S11.41 19.72 11.86 18H22V16H11.86C11.41 14.28 9.86 13 8 13M8 19C6.9 19 6 18.1 6 17C6 15.9 6.9 15 8 15S10 15.9 10 17C10 18.1 9.1 19 8 19M19.86 6C19.41 4.28 17.86 3 16 3S12.59 4.28 12.14 6H2V8H12.14C12.59 9.72 14.14 11 16 11S19.41 9.72 19.86 8H22V6H19.86M16 9C14.9 9 14 8.1 14 7C14 5.9 14.9 5 16 5S18 5.9 18 7C18 8.1 17.1 9 16 9Z"></ha-svg-icon>
</ha-control-select-menu>
```

选择一个选项不会自动改变数值。页面会设置新数值，通常是在实体发生变化之后。长标签和值会被省略号截断。开始处的图标在有选中选项的图标时显示该图标。否则，它会显示该设置的默认图标。

## 规格 {#specs}

| 属性 | 数值 | 代币 |
| --- | --- | --- |
| 高度 | 48px | `--control-select-menu-height` |
| 内边距 | 上下 6px，左右 10px | `--control-select-menu-padding` |
| 圆角半径 | 12px | `--ha-border-radius-lg`，通过 `--control-select-menu-border-radius` |
| 图标、文字与箭头之间的间距 | 10px | 无 |
| 图标大小 | 20px | `--mdc-icon-size` |
| 标签大小 | 12px，字母间距 0.4px | `--ha-font-size-s` |
| 数值大小 | 14px | `--ha-font-size-m` |
| 字重 | 400 | `--ha-font-weight-normal` |
| 行高 | 1.4 | 无 |
| 过渡 | 180ms，缓入缓出 | 无 |
| 菜单选项高度 | 至少 40px | `--ha-space-10` || 状态 | 背景 | 文本 |
| --- | --- | --- |
| 静止 | `--disabled-color` 透明度 20% | `--primary-text-color` |
| 悬停 | `--ha-color-on-neutral-quiet` 透明度 20% | `--primary-text-color` |
| 聚焦 | 静止背景，带有 `--secondary-text-color` 的 2px 环 | `--primary-text-color` |
| 禁用 | `--disabled-color` 透明度 20% | `--disabled-color` |
| 菜单中选中的选项 | `--ha-color-fill-primary-quiet-resting`，悬停时 `--ha-color-fill-primary-quiet-hover` | `--primary-color` |

## 指南 {#guidelines}

作为现场演示的注意事项。

**应做：** 保持标签和值简短。

```html
<ha-control-select-menu label="Preset" value="eco" data-props='{"options": [{"value": "eco", "label": "Eco"}]}' style="width: 160px">
    <ha-svg-icon slot="icon" path="M8 13C6.14 13 4.59 14.28 4.14 16H2V18H4.14C4.59 19.72 6.14 21 8 21S11.41 19.72 11.86 18H22V16H11.86C11.41 14.28 9.86 13 8 13M8 19C6.9 19 6 18.1 6 17C6 15.9 6.9 15 8 15S10 15.9 10 17C10 18.1 9.1 19 8 19M19.86 6C19.41 4.28 17.86 3 16 3S12.59 4.28 12.14 6H2V8H12.14C12.59 9.72 14.14 11 16 11S19.41 9.72 19.86 8H22V6H19.86M16 9C14.9 9 14 8.1 14 7C14 5.9 14.9 5 16 5S18 5.9 18 7C18 8.1 17.1 9 16 9Z"></ha-svg-icon>
  </ha-control-select-menu>
```

**不应做：** 使用在狭窄按钮中会被截断的长文本。

```html
<ha-control-select-menu label="Energy saving preset" value="eco" data-props='{"options": [{"value": "eco", "label": "Energy saving mode"}]}' style="width: 160px">
    <ha-svg-icon slot="icon" path="M8 13C6.14 13 4.59 14.28 4.14 16H2V18H4.14C4.59 19.72 6.14 21 8 21S11.41 19.72 11.86 18H22V16H11.86C11.41 14.28 9.86 13 8 13M8 19C6.9 19 6 18.1 6 17C6 15.9 6.9 15 8 15S10 15.9 10 17C10 18.1 9.1 19 8 19M19.86 6C19.41 4.28 17.86 3 16 3S12.59 4.28 12.14 6H2V8H12.14C12.59 9.72 14.14 11 16 11S19.41 9.72 19.86 8H22V6H19.86M16 9C14.9 9 14 8.1 14 7C14 5.9 14.9 5 16 5S18 5.9 18 7C18 8.1 17.1 9 16 9Z"></ha-svg-icon>
  </ha-control-select-menu>
```

- 仅在周围环境已经标明设置时隐藏标签，例如磁贴卡片。

## 可访问性 {#accessibility}

### 键盘 {#keyboard}

该按钮会打开一个 [下拉菜单](/design/components/dropdown)，菜单遵循以下键盘操作行为：

| 键 | 操作 |
| --- | --- |
| <kbd>Tab</kbd> | 将焦点移动到按钮。禁用的选择菜单会被跳过。 |
| <kbd>Enter</kbd> 或 <kbd>空格</kbd> | 打开菜单。在菜单中，选择当前聚焦的选项。 |
| <kbd>向下箭头</kbd> 和 <kbd>向上箭头</kbd> | 移动到下一个或上一个选项。 |
| <kbd>Home</kbd> 和 <kbd>End</kbd> | 移动到第一个或最后一个选项。 |
| 一个字母 | 移动到以所输入文本开头的第一个选项。 |
| <kbd>Escape</kbd> | 关闭菜单，并将焦点移回按钮。 |

### 焦点 {#focus}

键盘焦点会在按钮周围显示一个2像素的环，颜色为次要文本颜色。

### 目标尺寸 {#target-size}

按钮高度为48像素。其宽度由页面设置，在更多信息对话框中为120到160像素。

### 屏幕阅读器 {#screen-readers}

按钮会通过其标签和数值进行播报，并且作为一个可以打开菜单的按钮播报。如果没有标签，则只播报数值。选项会被播报为菜单项。被选中的选项看起来是选中的，但不会被播报为已选中。

### 在代码中 {#in-the-code}

- 按钮是一个本地 `<button>`，下拉菜单设置了 `aria-haspopup="menu"` 和 `aria-expanded`。
- 可访问名称是按钮内部的文本：标签和值。使用 `hide-label` 时，标签完全不被渲染，因此屏幕阅读器只能获取值。
- SVG 图标对屏幕阅读器隐藏。
- 菜单的角色是 `menu`，每个选项的角色是 `menuitem`。选中的选项只是视觉上标记的。

## 相关内容 {#related}

- [控件](/design/components/controls)：选择菜单所属的系列
- [下拉菜单](/design/components/dropdown)：它打开的菜单
- [卡片瓦片](/design/dashboards/tile-card)：它作为功能显示的位置

## 代码中 {#in-code}

该元素是 `<ha-control-select-menu>`。菜单是一个 [`ha-dropdown`](/design/components/dropdown)，在按钮下方打开，且至少和按钮一样宽。

```ts
html`<ha-control-select-menu
  .label=${"Preset"}
  .value=${this.stateObj.attributes.preset_mode}
  .options=${[
    { value: "eco", label: "Eco" },
    { value: "sleep", label: "Sleep" },
  ]}
  @wa-select=${this._presetChanged}
>
  <ha-svg-icon slot="icon" .path=${mdiTuneVariant}></ha-svg-icon>
</ha-control-select-menu>`
```

当选择一个选项时，该组件不会改变自身的值。它会触发 `wa-select`，然后你从那里设置 `value`，通常在实体更改之后。这也是本页示例保持其值的原因。

### 属性 {#attributes}

- `label`：设置的名称。
- `value`：所选选项的 `value`。
- `hide-label`：仅显示值，不显示标签。
- `show-arrow`：在末尾显示下拉箭头。
- `disabled`：禁用选择菜单，它不会打开。

### 属性 {#properties}

这些只能作为属性设置：

- `options`：一个选项数组。每个选项都有一个 `value` 和一个 `label`，并且可选一个图标：`iconPath` 表示 SVG 路径数据，或者 `icon` 表示图标名称，例如 `mdi:fan`。
- `renderIcon`：一个返回值图标的函数。用于没有 `iconPath` 或 `icon` 的选项，在菜单和按钮中使用。

### 插槽 {#slots}

- `icon`：按钮上的图标，当所选选项本身没有图标时显示。

### 事件 {#events}

- `wa-select`：选中了一个选项。`detail.item.value` 是其 `value`。

### 样式 {#styling}

- `--control-select-menu-height`：默认值为 `48px`。
- `--control-select-menu-padding`：默认值为 `6px 10px`。
- `--control-select-menu-border-radius`：默认值为 `var(--ha-border-radius-lg)`。
- `--control-select-menu-background-color`：默认值为 `var(--disabled-color)`。
- `--control-select-menu-background-opacity`：默认值为 `0.2`。
- `--control-select-menu-focus-color`：聚焦环。默认值为 `var(--secondary-text-color)`。
- `--mdc-icon-size`：图标大小。默认值为 `20px`。

该元素为 `inline-block`，宽度与其内容相等。设置 `width`，或 `display: block` 以填充容器，就像卡片瓦片功能那样。

来源：[`src/components/ha-control-select-menu.ts`](https://github.com/home-assistant/frontend/blob/dev/src/components/ha-control-select-menu.ts)
