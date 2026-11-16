---
title: 文本输入
description: 文本输入允许人们输入单行文本，例如姓名、数字或密码。
sidebarGroup: 输入
---


# 文本输入 {#text-input}
实时演示 `ha-input`。

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](/design/components/input)。

```html
<ha-input label="Name" value="Living room"></ha-input>
<ha-input label="Email" type="email" placeholder="you@example.com"></ha-input>
```

## 概述 {#overview}
文本输入允许用户在单行上输入简短的内容：姓名、地址、数字或密码。其类型告诉浏览器预期的值类型，为用户提供合适的手机键盘、正确的日期或时间选择器，并免费进行基本验证。

## 何时使用 {#when-to-use}
使用文本输入的场景：

- 用户需要输入的简短内容，例如姓名、电子邮件地址或端口
- 数字、日期、时间、网址或密码

不应使用文本输入的场景：

- 可以跨越多行的文本，例如描述。应使用 [textarea](/design/components/textarea)。
- 已知集合中的值。应让用户选择，使用 [select box](/design/components/select-box) 或 [picker](/design/components/entity-picker)。
- 范围内的值，确切的数字不如位置重要。应使用 [slider](/design/components/slider)。

## 解剖结构 {#anatomy}
1. **容器**：字段，底部有一条线，或有轮廓
2. **标签**：标示值的名称。它位于字段内部，当字段获得焦点或有值时会向上移动。
3. **开始**：值之前的可选内容，如图标或前缀
4. **值**：用户输入内容的本地输入框
5. **清除按钮**：可选，在字段有值时显示
6. **密码切换**：可选，显示或隐藏密码
7. **结束**：值之后的可选内容，如单位
8. **提示**：字段下方的可选帮助文本，当值无效时被验证信息替换

## 变体 {#variants}
### 外观 {#appearance}
有两种外观：

- **实心** 是默认样式：一个带底线的填充字段。在表单、对话框和设置中使用它。
- **轮廓** 周围有边框，当没有标签时会变得紧凑。前端主要在工具栏、列表和表格中的搜索和过滤字段中使用它，因为实心字段在这些场景中显得过于沉重。

`ha-input` 的实时演示。

```html
<ha-input label="Material" value="Living room"></ha-input>
<ha-input appearance="outlined" label="Outlined" value="Living room"></ha-input>
<ha-input appearance="outlined" placeholder="Search devices"></ha-input>
```

### 类型 {#type}
选择与值匹配的类型：数字字段用于数字，电子邮件字段用于电子邮件地址，URL字段用于网页地址，密码字段用于任何保密信息。给密码字段添加显示密码的按钮，这样人们可以检查自己输入的内容。

`ha-input` 的实时演示。

```html
<ha-input label="Volume" type="number" value="42"></ha-input>
<ha-input label="Website" type="url" placeholder="https://example.com"></ha-input>
<ha-input label="Password" type="password" value="correct horse" password-toggle></ha-input>
<ha-input label="Date" type="date"></ha-input>
```

### 提示 {#hint}
使用提示提供额外的上下文，帮助人们填写字段，例如预期格式或在哪里可以找到该值。保持在一句话内。

`ha-input` 的实时演示。

```html
<ha-input label="Port" type="number" value="8123" hint="The port Home Assistant listens on."></ha-input>
```

### 前缀和后缀 {#prefix-and-suffix}
在数值的前面或后面放置简短的文字或图标。数值后的单位是最常见的用法：秒、百分比或千克。它可以让人们不必猜测数字的含义，并且使单位不直接出现在数值本身中。

`ha-input` 的实时演示。

```html
<ha-input label="Delay" type="number" value="30">
  <span slot="end">s</span>
</ha-input>
<ha-input label="Brightness" type="number" value="80">
  <span slot="end">%</span>
</ha-input>
```

### 清除按钮 {#clear-button}
当人们经常希望从头开始时（例如在搜索字段中），可以添加一个清除按钮。只要有值时，它就会显示出来。

`ha-input` 的实时演示。

```html
<ha-input label="Filter" value="kitchen" with-clear></ha-input>
```

## 行为- **空**：标签位于字段内部，大小与文本相同。 {#behavior}
- **悬停**：材质字段变为悬停背景。轮廓字段改变其边框颜色。
- **聚焦**：材质字段在底部获得更粗的主色线条，标签变为主色。轮廓字段获取主色边框。
- **已填充**：一旦字段有值或获得焦点，标签上移并变小。对于占位符、日期或颜色类型，标签始终上移。
- **必填**：标签带有`*`标记。字段必须有值，表单才能有效。
- **禁用**：材质字段获得禁用背景，字段和标签的不透明度减半，并且值无法更改或聚焦。

- **只读**：显示人们可以查看和复制的值，但无法更改。
- **无效**：标签和底部的线条会变为危险颜色，验证消息会替代提示。当代码将字段标记为无效、表单检查发现值无效，或者对于自检字段在失去焦点时，它会变为无效。只要人们输入有效值，它就会再次变为有效。

`ha-input` 的现场演示。

```html
<ha-input label="Name" required></ha-input>
<ha-input label="Disabled" value="Can't change this" disabled></ha-input>
<ha-input label="Read-only" value="Can't change this either" readonly></ha-input>
<ha-input label="Port" value="99999" invalid validation-message="Enter a port between 1 and 65535."></ha-input>
```

在字段中按 <kbd>回车</kbd> 会提交所在的表单。

## 规格 {#specs}
### 尺寸 {#size}
| 属性 | 材料 | 带标签的轮廓 | 无标签的轮廓 |
| --- | --- | --- | --- |
| 输入框高度 | 56px | 56px | 32px |
| 左右内边距 | 16px (`--ha-space-4`) | 16px (`--ha-space-4`) | 8px (`--ha-space-2`) |
| 圆角 | 顶部4px (`--ha-border-radius-sm`)，底部0 (`--ha-border-radius-square`) | 8px (`--ha-border-radius-md`) | 8px (`--ha-border-radius-md`) |
| 边框 | 底部1px，聚焦时2px | 四周1px | 四周1px |
| 组件下方间距 | 8px (`--ha-space-2`)，通过 `--ha-input-padding-bottom` | 无 | 无 |
| 清除和密码按钮 | 48px | 48px | 24px，图标18px |

### 类型 {#type-1}
| 部分 | 大小 | 令牌 |
| --- | --- | --- |
| 标签，位于字段内 | 14px | `--ha-font-size-m` |
| 标签，上移 | 10px | `--ha-font-size-xs` |
| 标签上方的间距 | 20px，上移时为12px | `--ha-space-5`, `--ha-space-3` |
| 值上方的间距 | 12px，无标签时无间距 | `--ha-space-3` |
| 提示和验证信息 | 12px | `--ha-font-size-s` |
| 提示最小高度 | 20px | `--ha-space-5` |
| 提示缩进 | 12px | `--ha-space-3` |

标签的字重为400 (`--ha-font-weight-normal`)，行高为1.2 (`--ha-line-height-condensed`)。颜色、边框和标签位置的变化耗时150毫秒。

### 颜色 {#color}
| 部位 | 状态 | 代币 |
| --- | --- | --- |
| 材料背景 | 静止 | `--ha-color-form-background` |
| 材料背景 | 悬停 | `--ha-color-form-background-hover` |
| 材料背景 | 禁用 | `--ha-color-form-background-disabled` |
| 描边背景 | 全部 | `--card-background-color` |
| 底部材料线 | 静止 | `--ha-color-border-neutral-loud` |
| 底部材料线 | 聚焦 | `--primary-color` |
| 底部材料线 | 无效 | `--ha-color-border-danger-normal` |
| 描边边框 | 静止 | `--ha-color-border-neutral-quiet` |
| 描边边框 | 悬停 | `--ha-color-border-neutral-normal` |
| 描边边框 | 聚焦 | `--primary-color` |
| 标签 | 静止 | `--secondary-text-color` |
| 标签 | 聚焦，材料 | `--primary-color` |
| 标签 | 无效 | `--ha-color-fill-danger-loud-resting` |
| 占位符 | 全部 | `--ha-color-neutral-60` |
| 提示 | 全部 | `--ha-color-text-secondary` |
| 验证消息 | 无效 | `--ha-color-on-danger-quiet` |
| 末端插槽 | 全部 | `--ha-color-text-secondary` |

## 指南 {#guidelines}
做与不做，如现场演示。

**做：** 总是给输入一个简短的标签。

```html
<ha-input label="Email" type="email" placeholder="you@example.com"></ha-input>
```

**不做：** 使用占位符作为标签。一旦有人输入，它就会消失。

```html
<ha-input type="email" placeholder="Email"></ha-input>
```

做与不做，如现场演示。

**做：** 说明哪里有问题，以及如何修复。

```html
<ha-input label="Port" value="99999" invalid validation-message="Enter a port between 1 and 65535."></ha-input>
```

**不做：** 只是说数值错误。

```html
<ha-input label="Port" value="99999" invalid validation-message="Invalid value."></ha-input>
```

做与不做，如现场演示。

**做：** 将单位放在数值后面。

```html
<ha-input label="Delay" type="number" value="30"><span slot="end">s</span></ha-input>
```

**不做：** 让人们在数值中输入单位。

```html
<ha-input label="Delay" value="30 seconds"></ha-input>
```

做与不做，如现场演示。

**做：** 标记必填字段。

```html
<ha-input label="Name" required></ha-input>
```

**不做：** 标记可选字段。

```html
<ha-input label="Name (optional)"></ha-input>
```

## 无障碍功能 {#accessibility}
### 键盘 {#keyboard}
| 键 | 操作 |
| --- | --- |
| <kbd>Tab</kbd> | 将焦点移动到输入框，然后移动到清除按钮和密码切换按钮（如果存在）。禁用的输入框会被跳过。 |
| <kbd>Enter</kbd> | 提交输入框所在的表单。在清除按钮或密码切换按钮上时，选择该按钮。 |
| <kbd>Space</kbd> | 在清除按钮或密码切换按钮上时，选择该按钮。 |

数字、日期和时间输入框保持浏览器对这些类型的键盘行为。

### 焦点 {#focus}
焦点通过底部线条的主色（材质风格）或边框（轮廓风格）显示，而不是单独的焦点环。

### 目标尺寸 {#target-size}
材质风格的输入框，以及带标签的轮廓风格输入框，高度为56像素。没有标签的轮廓风格输入框高度为32像素，其按钮高度为24像素。

### 屏幕阅读器 {#screen-readers}
屏幕阅读器会用标签来宣布字段，并将提示作为其描述进行读取。当字段变为无效时，会宣布验证消息。必填、禁用和只读字段也会被宣布。清除按钮会被宣布为“清除”，密码按钮会根据用户的语言宣布为“显示密码”或“隐藏密码”。没有标签的字段只有其占位符来描述，因此始终为其提供标签。

### 在代码中 {#in-the-code}
- 焦点被委托给组件内部的原生输入。
- 标签是一个原生`<label>`，与输入关联，因此它是可访问名称。
- 没有标签时，`<label>` 是空的，并且对辅助技术隐藏。此时占位符是唯一描述输入的文本。
- 提示和验证消息通过 `aria-describedby` 与输入关联，因此屏幕阅读器会将它们读取为描述。
- 验证消息位于实时区域中，并且在字段无效时具有 `alert` 角色，因此屏幕阅读器在消息出现时会朗读它。
- 必填、禁用和只读属性设置在原生输入上，因此辅助技术会按原样获取它们。
- 清除按钮和密码切换按钮会将翻译后的标签作为它们的可访问名称。

## 相关内容 {#related}
- [多行文本框](/design/components/textarea)：多行文本输入
- [表单](/design/components/form)：从模式构建输入项
- [选择器](/design/components/selector)：文本和数值选择器显示该输入
- [界面文本](/design/ui-text)：如何编写标签、提示和错误信息

前端在这个基础上构建了一些特定用途的输入项。请使用它们，而不是重新构建相同的内容：

- `<ha-input-search>`：带有放大镜图标、清除按钮和本地化占位符的搜索字段。
- `<ha-input-copy>`：带有复制按钮的只读值，并可对敏感信息如 token 进行可选遮盖。
- `<ha-input-multi>`：一组文本输入，用于输入多个值，比如 URL 列表。

## 在代码中 {#in-code}
该元素是 `<ha-input>`。它基于 [Web Awesome 输入](https://webawesome.com/docs/components/input/)。

```html
<ha-input label="Name" value="Living room"></ha-input>
<ha-input label="Email" type="email" placeholder="you@example.com"></ha-input>
<ha-input label="Password" type="password" password-toggle></ha-input>
<ha-input label="Delay" type="number" min="0" step="1">
  <span slot="end">s</span>
</ha-input>
```

### 属性- `label`：标签。 {#attributes}
- `value`：当前值，作为字符串。
- `type`：`text`（默认）、`number`、`password`、`email`、`url`、`tel`、`search`、`date`、`datetime-local`、`time` 或 `color`。
- `appearance`：`material`（默认）或 `outlined`。
- `hint`：输入下方的帮助文本。
- `placeholder`：输入为空时显示的文本。
- `required`：将字段设置为必填，并在标签后添加标记。
- `disabled`：禁用输入。
- `readonly`：将输入设置为只读。
- `invalid`：将输入标记为无效。
- `validation-message`：输入无效时显示的消息。如果没有，将显示浏览器自己的消息。
- `auto-validate`：输入失去焦点时验证，而不是等待表单提交。
- `pattern`：值必须匹配的正则表达式。
- `minlength` 和 `maxlength`：值的最小和最大长度。

- `min`、`max` 和 `step`：数字、日期和时间输入的限制和粒度。
- `with-clear`：当输入有值时显示清除按钮。
- `password-toggle`：显示用于显示或隐藏密码的按钮。
- `password-visible`：将密码显示为明文。
- `without-spin-buttons`：隐藏数字输入框中的浏览器上下按钮。
- `inset-label`：即使 `start` 插槽中有内容，也将标签保留在字段内。
- `input-id`：组件内原生输入的 `id`，用于将其链接到外部。
- `name`、`autocomplete`、`autocapitalize`、`autocorrect`、`autofocus`、`spellcheck`、`inputmode` 和 `enterkeyhint`：传递给原生输入，并与普通 `<input>` 的效果相同。

### 插槽 {#slots}
- `start`：值前的内容，如图标或前缀。
- `end`：值后的内容，如单位。
- `label`：带标记的标签。此插槽中的内容会替换 `label` 属性的文本，包括必填标记。
- `hint`：带标记的提示，例如链接。仅在未设置 `hint` 属性时使用。
- `clear-button`：替换清除按钮。
- `password-toggle-button`：替换显示密码的按钮。

### 事件 {#events}
- `input`：在每次值变化时触发，例如输入时。
- `change`：在值被确认时触发，例如输入框失去焦点时。

从元素的 `value` 获取新值。

### 样式 {#styling}
- `--ha-input-padding-top`：输入框上方的间距。
- `--ha-input-padding-bottom`：输入框下方的间距。材料外观默认值为 `var(--ha-space-2)`。
- `--ha-input-text-align`：数值的对齐方式。默认值为 `start`。
- `--ha-input-required-marker`：必填字段标签后的标记。默认值为 `"*"`。

来源：[`src/components/input/ha-input.ts`](https://github.com/home-assistant/frontend/blob/dev/src/components/input/ha-input.ts)
