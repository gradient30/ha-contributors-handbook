---
title: 选择框
description: 选择框让人们从几个选项中选择一个，这些选项以卡片形式并排显示，可以容纳描述或图片。
sidebarGroup: 输入
---

# 选择框 {#select-box}

Live demo of `ha-select-box`.

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](https://contributors.home-assistant.io/design/components/select-box/)。

```html
<ha-select-box data-props='{"options": [{"value": "single", "label": "Single", "description": "Do not start a new run. Issue a warning."}, {"value": "restart", "label": "Restart", "description": "Start a new run after first stopping the previous run."}, {"value": "queued", "label": "Queued", "description": "Start a new run after all previous runs complete."}], "value": "single"}' style="display: block; width: 100%"></ha-select-box>
```

## 概览 {#overview}

下拉选择框让人们从少量选项中选择一个，当选项需要解释时使用。每个选项都是一个卡片，包含一个单选按钮、一个标签，以及可选的描述和图片。所有选项同时可见，因此人们可以在选择之前进行比较。

前端在以下选择中使用它：

- 常规设置中的单位系统：公制或美国习惯制，并附带每种单位的示例。
- 自动化的模式，其中每种模式都有描述，说明当自动化在运行时再次启动会发生什么。
- 语音助手处理语音的方式，在设置过程中。

## 何时使用 {#when-to-use}

使用下拉框的情况：

- 从一小组选项中选择一个，其中选项需要描述或图片

不使用下拉框的情况：

- 选项本身易于理解的情况。下拉框占用空间过多。此时应使用普通下拉列表或单选列表。
- 长列表。应使用下拉列表。
- 简单的开关设置。应使用[开关](/design/components/switch)。
- 选择多个选项。应使用复选框。

## 结构 {#anatomy}

1. **卡片**：选项的带边框容器。整个卡片都可以被选择。
2. **单选按钮**：显示哪个选项被选中
3. **标签**：选项的名称
4. **描述**：可选，在标签下方的简短说明
5. **图片**：可选，位于文本下方，或与文本同列并排显示

## 变体 {#variants}

### 列 {#columns}

默认情况下，选项并排显示，每行最多三个。更多选项时，会换到下一行。设置最大列数以适应内容：列数少时，较长的描述有更多空间。

### 单列 {#single-column}

在单列布局下，每个选项成为一行，图片位于文本旁边。当图片需要占满整个宽度时，例如宽幅预览，可将其堆叠在文本下方。

`ha-select-box` 的实时演示。

```html
<ha-select-box max_columns="1" data-props='{"options": [{"value": "single", "label": "Single", "description": "Do not start a new run. Issue a warning."}, {"value": "restart", "label": "Restart", "description": "Start a new run after first stopping the previous run."}], "value": "restart"}' style="display: block; width: 100%"></ha-select-box>
```

## 行为 {#behavior}

- **悬停**：卡片会呈现分隔线颜色的浅色调。
- **已选择**：单选按钮被选中，卡片会呈现主色的 20% 色调。
- **禁用**：禁用选项会以 50% 不透明度显示其内容和图片，且无法被选择。你也可以禁用整个选择框。
- 选择一个选项不会自行更改值。页面会根据事件设置新的值。
- 过长的标签会以省略号显示。描述内容会自动换行。
- 在暗色主题下，选项可以使用其自己的图片。在从右到左的语言环境中，图片可以进行镜像翻转。

## 规格 {#specs}

| 属性 | 数值 | 令牌 |
| --- | --- | --- |
| 选项之间的间距 | 12px | `--ha-space-3` |
| 卡片内边距 | 12px | 无 |
| 卡片边框 | 1px | `--divider-color` |
| 卡片圆角半径 | 12px | `--ha-border-radius-lg`，通过 `--ha-card-border-radius` |
| 单选按钮与文本之间以及内容与图片之间的间距 | 8px | `--ha-space-2` |
| 标签与描述之间的间距 | 4px | `--ha-space-1` |
| 标签 | 14px，字重 400，`--primary-text-color` | `--ha-font-size-m`，`--ha-font-weight-normal` |
| 描述 | 12px，字重 400，`--secondary-text-color` | `--ha-font-size-s`，`--ha-font-weight-normal` |
| 行高 | 1.2 | `--ha-line-height-condensed` |
| 图片尺寸 | 最大 96px x 96px。堆叠时：全宽，最大高度 96px。 | `--ha-select-box-image-size` |
| 最大列数 | 3 | `max_columns` |

| 状态 | 卡片颜色 |
| --- | --- |
| 静止 | 无 |
| 悬停 | `--divider-color` 透明度 20% |
| 选中 | `--primary-color` 透明度 20% |
| 禁用 | `--disabled-color` 透明度 5%，内容透明度 50% |颜色在180毫秒内变化，缓入缓出。

## 指南 {#guidelines}

- 保持标签简短：用一两个词来命名选项，例如 **Single** 或 **Restart**。
- 使用描述来解释选项的含义，用一两句话说明。
- 当图片比文字更快地说明选项时使用图片，比如卡片的布局。图片是装饰性的：标签本身仍需能独立理解。

以现场演示的方式展示做与不做。

**做：** 用一两词命名选项，并在描述中进行解释。

```html
<ha-select-box max_columns="1" data-props='{"options": [{"value": "single", "label": "Single", "description": "Do not start a new run. Issue a warning."}], "value": "single"}' style="display: block; width: 100%"></ha-select-box>
```

**不做：** 将整个解释放在标签中。

```html
<ha-select-box max_columns="1" data-props='{"options": [{"value": "single", "label": "Do not start a new run and issue a warning"}], "value": "single"}' style="display: block; width: 100%"></ha-select-box>
```

## 可访问性 {#accessibility}

### 键盘 {#keyboard}

| 键 | 动作 |
| --- | --- |
| <kbd>Tab</kbd> | 将焦点移入组、到选中的选项、然后再移出。 |
| 方向键 | 移动到下一个或上一个选项并选择它。禁用的选项会被跳过。 |
| <kbd>Space</kbd> | 选择当前焦点的选项。 |

### 焦点 {#focus}

焦点会移动到组中选定的选项。箭头键同时移动焦点和选择。

### 目标尺寸 {#target-size}

整个卡片都是目标，而不仅仅是单选按钮。

### 屏幕阅读器 {#screen-readers}

这些选项被宣布为一组单选按钮，每个都有其标签和描述，以及是否已选中或已禁用。该组本身没有名称，因此在其上方放置一个标题或标签来命名选择。图片会被跳过。

### 在代码中 {#in-the-code}

- 选项在一个角色为 `radiogroup` 的组中。每个单选按钮的角色为 `radio`，具有 `aria-checked` 和 `aria-disabled`。
- 每个单选按钮由其标签命名，并通过 `aria-labelledby` 和 `aria-describedby` 描述其描述。
- 下拉框本身没有标签，因此该组没有可访问名称。
- 图片有一个空的 `alt`。

## 相关 {#related}

- [开关](/design/components/switch)：一个可以开或关的设置
- [选择菜单](/design/components/select-menu)：为设备选择一个选项
- [选择器](/design/components/selector)：表单中显示选择框的地方

## 在代码中 {#in-code}

该元素是 `<ha-select-box>`。选项和所选值只能通过代码以属性的方式设置：

```ts
html`
  <ha-select-box
    .options=${[
      {
        value: "single",
        label: "Single",
        description: "Do not start a new run. Issue a warning.",
      },
      {
        value: "restart",
        label: "Restart",
        description: "Start a new run after first stopping the previous run.",
      },
    ]}
    .value=${this._mode}
    @value-changed=${this._modeChanged}
  ></ha-select-box>
`;
```

该下拉框本身没有标签。在其上方放置标题或标签，以标明选择内容。

### 属性 {#properties}

这些只能通过代码设置：

- `options`：选项列表。每个选项包含：
  - `value`：选项的值。必填。
  - `label`：标签。
  - `description`：短描述，显示在标签下方。
  - `image`：图片的 URL，或者一个对象，包含 `src`、`src_dark`（用于暗色主题）以及 `flip_rtl`（用于右到左语言镜像图片）。
  - `disabled`：禁用此选项。
- `value`：所选选项的值。

### 属性 {#attributes}

- `disabled`：禁用所有选项。
- `max_columns`：每行的最大选项数。默认为 `3`。使用 `1` 时，每个选项为一行，图片在文本旁边。
- `stacked_image`：使用 `max_columns="1"` 时，图片显示在文本下方，全宽显示，而不是在旁边。

注意下划线：这两个属性是 `max_columns` 和 `stacked_image`，不是 `max-columns` 和 `stacked-image`。

### 事件 {#events}

- `value-changed`：当人们选择一个选项时触发。新值在 `event.detail.value` 中。选择框不会更新其自身的 `value`：需要从事件中再次设置。

### 样式 {#styling}

- `--ha-select-box-image-size`：图像的最大宽度和高度。默认为 `96px`。

来源：[`src/components/ha-select-box.ts`](https://github.com/home-assistant/frontend/blob/dev/src/components/ha-select-box.ts)
