---
title: 按钮
description: 按钮会启动一个操作，例如保存表单或打开对话框。
sidebarGroup: 动作
sidebarGroup: 操作

---


# 按钮 {#button}
现场演示 `ha-button`。

```html
<ha-button>Save</ha-button>
<ha-button appearance="filled">Filled</ha-button>
<ha-button appearance="outlined">Outlined</ha-button>
<ha-button appearance="plain">Cancel</ha-button>
```

## 概述 {#overview}
按钮可以启动一个操作：当你选择它时，会发生某些事情，比如保存表单、打开对话框或删除项目。其外观表示操作的重要性，颜色表示操作的类型。

## 使用时机 {#when-to-use}
使用按钮适合：

- 改变某些内容的操作，比如 **保存**、**删除** 或 **启用**
- 确认或关闭一个 [对话框](/design/components/dialog)
- 打开对话框或菜单

不适合使用按钮的场景：

- 跳转到其他地方。应使用链接。
- 需要较长时间并显示进度的操作。应使用 [进度按钮](/design/components/progress-button)。
- 多个操作的列表。应放在 [下拉菜单](/design/components/dropdown) 中。
- 开关设置。应使用 [开关](/design/components/switch)。

## 解剖结构 {#anatomy}
1. **容器**：背景、边框和圆角
2. **开始**：标签前的可选内容，通常是图标
3. **标签**：按钮的文字
4. **结束**：标签后的可选内容，通常是图标
5. **加载动画**：在按钮加载时替换开始、标签和结束

## 变体 {#variants}
### 外观 {#appearance}
按钮有四种外观，它们决定按钮吸引注意力的程度：

- **强调** 是默认的，填充最醒目。
- **填充** 填充较柔和。当某个操作需要强调时使用。
- **轮廓** 无填充，仅有边框。
- **普通** 无填充也无边框，吸引注意力最少。用于取消或关闭操作。

`ha-button` 的实时演示。主操作使用强调，退出操作使用普通。

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](/design/components/button)。

```html
<ha-button appearance="plain">Cancel</ha-button>
<ha-button>Save</ha-button>
```

### 变体 {#variant}
变体设置颜色，从而赋予按钮含义：

- **品牌** 是默认，用于大多数操作。
- **危险** 用于破坏性操作，如删除某些内容。
- **警告** 和 **成功** 用于与警告或成功状态相关的操作。
- **中性** 用于不希望通过颜色传达任何意义的操作。

`ha-button` 的实时演示。

```html
<ha-button>Brand</ha-button>
<ha-button variant="danger">Danger</ha-button>
<ha-button variant="warning">Warning</ha-button>
<ha-button variant="success">Success</ha-button>
<ha-button variant="neutral">Neutral</ha-button>
```

### 尺寸 {#size}
按钮有四种尺寸：特小号、小号、中号和大号。中号为默认尺寸。

`ha-button` 的实时演示。

```html
<ha-button size="xs">Extra small</ha-button>
<ha-button size="s">Small</ha-button>
<ha-button size="m">Medium</ha-button>
<ha-button size="l">Large</ha-button>
```

## 行为 {#behavior}
- **启用**：静止状态，显示其外观和变体颜色。
- **悬停**：在带有悬停功能的指针设备上，背景会变为该变体的悬停填充色。颜色变化持续 150 毫秒。
- **聚焦**：键盘聚焦时显示一个 2px 的实线聚焦环，位于按钮外侧 2px 处。
- **按下**：按下时，背景变为该变体的激活填充色。
- **禁用**：按钮使用禁用颜色，无法被选中，并且在使用键盘浏览页面时会被跳过。
- **加载中**：一个加载动画替代标签和图标。按钮保持原有大小，选择它不会产生任何操作。

`ha-button` 的实时演示。

```html
<ha-button loading>Saving</ha-button>
<ha-button disabled>Disabled</ha-button>
<ha-button appearance="outlined" disabled>Disabled</ha-button>
```

长标签会换行。当标签无法换行时，会以省略号截断。

## 规格 {#specs}
### 尺寸 {#size-1}
| 尺寸 | 高度 | 左右内边距 | 字体大小 |
| --- | --- | --- | --- |
| 特小 | 24px | 8px (`--ha-space-2`) | 14px (`--ha-font-size-m`) |
| 小 | 32px | 12px (`--ha-space-3`) | 14px (`--ha-font-size-m`) |
| 中 | 40px | 16px (`--ha-space-4`) | 14px (`--ha-font-size-m`) |
| 大 | 48px | 16px (`--ha-space-4`) | 16px (`--ha-font-size-l`) |

高度可以通过 `--ha-button-height` 来更改。在代码中还有一个特大尺寸，但它没有自己的样式，看起来与中等尺寸相同。

### 形状和内容 {#shape-and-content}
| 属性 | 值 | 令牌 |
| --- | --- | --- |
| 圆角半径 | 9999px，完全圆角 | `--ha-border-radius-pill`，通过 `--ha-button-border-radius` |
| 边框宽度 | 1px | `--ha-border-width-sm` |
| 字体粗细 | 500 | `--ha-font-weight-medium` |
| 紧邻起始或结束图标的内边距 | 8px | `--ha-space-2` |
| 图标与标签之间的间隙 | 4px | `--ha-space-1` |
| 标签上下内边距 | 4px | `--ha-space-1` |
| 超小图标尺寸 | 16px | `--mdc-icon-size` |
| 焦点环 | 2px 实线，偏移 2px | `--ha-color-focus` |
| 悬停过渡 | 150ms，缓出 | `--ha-animation-duration-fast` |

### 颜色 {#color}
下面的令牌是针对品牌变体的。其他变体使用相同的令牌，只是将 `primary` 替换为 `neutral`、`success`、`warning` 或 `danger`。| 外观 | 状态 | 背景 | 文本 | 边框 |
| --- | --- | --- | --- | --- |
| 强调 | 静止 | `--ha-color-fill-primary-loud-resting` | `--ha-color-on-primary-loud` | 透明 |
| 强调 | 悬停 | `--ha-color-fill-primary-loud-hover` | `--ha-color-on-primary-loud` | 透明 |
| 强调 | 按下 | `--ha-color-fill-primary-loud-active` | `--ha-color-on-primary-loud` | 透明 |
| 强调 | 禁用 | `--ha-color-fill-disabled-loud-resting` | `--ha-color-on-disabled-loud` | 透明 |
| 填充 | 静止 | `--ha-color-fill-primary-normal-resting` | `--ha-color-on-primary-normal` | 透明 |
| 填充 | 悬停 | `--ha-color-fill-primary-normal-hover` | `--ha-color-on-primary-normal` | 透明 |
| 填充 | 按下 | `--ha-color-fill-primary-normal-active` | `--ha-color-on-primary-normal` | 透明 |
| 填充 | 禁用 | `--ha-color-fill-disabled-normal-resting` | `--ha-color-on-disabled-normal` | 透明 |
| 描边 | 静止 | 透明 | `--ha-color-on-primary-quiet` | `--ha-color-border-primary-loud` |
| 描边 | 悬停 | `--ha-color-fill-primary-quiet-hover` | `--ha-color-on-primary-quiet` | `--ha-color-border-primary-loud` |
| 描边 | 禁用 | 透明 | `--ha-color-on-disabled-quiet` | `--ha-color-on-disabled-quiet` |
| 纯色 | 静止 | 透明 | `--ha-color-on-primary-normal` | 透明 |
| 纯色 | 悬停 | `--ha-color-fill-primary-quiet-hover` | `--ha-color-on-primary-normal` | 透明 |
| 普通 | 按下 | `--ha-color-fill-primary-quiet-active` | `--ha-color-on-primary-quiet` | 透明 |
| 普通 | 禁用 | 透明 | `--ha-color-on-disabled-quiet` | 透明 |

中性普通按钮是唯一的例外：按下时，它使用 `--ha-color-fill-neutral-normal-active`。通过属性设置为禁用的按钮，其整体透明度也会被 Web Awesome 基础样式调暗到 50%。

## 指南 {#guidelines}
### 强调 {#emphasis}
演示示例中的可行与不可行。

**可行：** 使用普通按钮来取消或关闭。

```html
<ha-button appearance="plain">Cancel</ha-button>
<ha-button>Save</ha-button>
```

**不可行：** 给退出方式与主要操作同等的重视。

```html
<ha-button appearance="filled">Cancel</ha-button>
<ha-button>Save</ha-button>
```

演示示例中的可行与不可行。

**可行：** 对破坏性操作使用危险样式。

```html
<ha-button appearance="plain">Cancel</ha-button>
<ha-button variant="danger">Delete</ha-button>
```

**不可行：** 对删除操作使用品牌颜色。

```html
<ha-button appearance="plain">Cancel</ha-button>
<ha-button>Delete</ha-button>
```

### 标签 {#labels}
操作与禁用示例，作为实时演示。

**操作:** 说明当你选择按钮时会发生什么。

```html
<ha-button>Save</ha-button>
```

**禁用:** 使用可能含义不明的标签。

```html
<ha-button>OK</ha-button>
<ha-button>Submit</ha-button>
```

操作与禁用示例，作为实时演示。

**操作:** 使用句子式大小写。

```html
<ha-button>Create automation</ha-button>
```

**禁用:** 每个单词都大写。

```html
<ha-button>Create Automation</ha-button>
```

操作与禁用示例，作为实时演示。

**操作:** 对可以重新添加的内容使用“移除”，比如仪表板上的卡片。

```html
<ha-button appearance="filled">Remove from dashboard</ha-button>
```

**禁用:** 对不会永久删除的内容使用“删除”。

```html
<ha-button appearance="filled">Delete from dashboard</ha-button>
```

更多内容请参见 [UI 文本](/design/ui-text) 和 [移除、删除、添加或创建](/design/ui-text/remove-delete)。

### 图标 {#icons}
避免在超小按钮中使用图标。在 24px 时，标签本身就能传达含义，而 16px 的图标放在旁边会增加干扰而不增加信息。仅在按钮需要在密集布局中一目了然时使用图标，并且只使用人们仅凭形状就能识别的常用图标，例如关闭、添加或设置。

实时示例中的做与不做。

**做：** 让标签自己在超小按钮中表达作用。

```html
<ha-button size="xs">Delete</ha-button>
```

**不做：** 在超小按钮中添加详细图标。

```html
<ha-button size="xs"><ha-svg-icon slot="start" path="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z"></ha-svg-icon>Delete</ha-button>
```

## 无障碍 {#accessibility}
### 键盘 {#keyboard}
| 键 | 操作 |
| --- | --- |
| <kbd>Tab</kbd> | 将焦点移至按钮或离开按钮。禁用按钮会被跳过。 |
| <kbd>Enter</kbd> 或 <kbd>Space</kbd> | 选择按钮。在加载时不执行任何操作。 |

### 焦点 {#focus}
焦点环仅在键盘聚焦时显示，而在使用鼠标或触摸选择按钮时不会显示。

### 目标尺寸 {#target-size}
高度为：超小尺寸 24px，小尺寸 32px，中尺寸 40px，大尺寸 48px。宽度根据标签加上内边距决定。

### 屏幕阅读器 {#screen-readers}
屏幕阅读器会根据按钮的标签朗读按钮。如果按钮仅有图标，没有文本可朗读，则需要在代码中提供名称。在加载时，按钮会被朗读为繁忙状态。禁用的按钮会被朗读为已禁用。

### 在代码中 {#in-the-code}
- 焦点被委托给组件内部的原生 `<button>`，所以在 `<ha-button>` 上调用 `focus()` 会聚焦按钮。焦点环使用 `:focus-visible`。
- 角色是 `button`。可访问名称是标签文本。通过在 `<ha-button>` 上设置 `aria-label` 可以赋予它另一个名称：该名称会传递给原生按钮。
- 仅有图标而没有文本的按钮需要 `aria-label`。
- 加载时，按钮具有 `aria-busy="true"`。
- 禁用按钮是原生禁用的 `<button>`。

## 相关内容 {#related}
- [进度按钮](/design/components/progress-button)：显示其操作结果的按钮
- [下拉菜单](/design/components/dropdown)：可打开操作菜单的按钮
- [对话框](/design/components/dialog)：大多数按钮对都位于此处
- [界面文本](/design/ui-text)：如何编写标签

## 在代码中 {#in-code}
该元素是 `<ha-button>`。它基于 [Web Awesome 按钮](https://webawesome.com/docs/components/button/)。

```html
<ha-button>Save</ha-button>
<ha-button appearance="plain">Cancel</ha-button>
<ha-button variant="danger">Delete</ha-button>
<ha-button size="s">Small</ha-button>
```

在对话框中，将主要操作放在 `primaryAction` 插槽，将次要操作放在 `secondaryAction` 插槽的 `ha-dialog-footer` 中。

### 属性 {#attributes}
- `appearance`：`accent`（默认）、`filled`、`outlined`或`plain`。
- `variant`：`brand`（默认）、`neutral`、`success`、`warning`或`danger`。
- `size`：`xs`、`s`、`m`（默认）或`l`。该值也接受`xl`，并且看起来与`m`相同。
- `loading`：显示加载指示器而不是标签，并阻止选择按钮。
- `disabled`：禁用按钮。

### 插槽 {#slots}
- 默认：标签。
- `start`：标签前的内容，通常是图标。
- `end`：标签后的内容，通常是图标。

### 样式 {#styling}
- `--ha-button-height`：按钮的高度。
- `--ha-button-border-radius`：圆角半径。默认为 `var(--ha-border-radius-pill)`。

来源：[`src/components/ha-button.ts`](https://github.com/home-assistant/frontend/blob/dev/src/components/ha-button.ts)
