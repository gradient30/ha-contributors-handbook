---
title: 表格
description: ha-form 根据一个模式渲染完整的表单，为每个值提供正确的字段，并返回数据。
sidebarGroup: 表格
sidebarGroup: 表单

---


# 表格 {#form}
Live 演示 `ha-form`，连接到演示 Home Assistant。

```html
<ha-form data-props='{"schema": [{"name": "Host", "required": true, "selector": {"text": {}}}, {"name": "Port", "selector": {"number": {"min": 1, "max": 65535, "mode": "box"}}}, {"name": "Use SSL", "selector": {"boolean": {}}}], "data": {"Host": "192.168.1.20", "Port": 8080, "Use SSL": false}}'></ha-form>
```

## 概述 {#overview}
表单组件将模式(schema)转换为表单。模式是字段的列表。每个字段都有一个名称，并说明它存储的值的类型。表单会为每个字段选择合适的控件，进行布局，并将数据作为一个对象返回，对象的键为字段名称。

你可以在 Home Assistant 的各个地方找到它：在集成的配置流程中，在助手选项中，在仪表板卡片的可视化编辑器中，以及在自动化和脚本的设置中。配置流程的表单直接来自集成，是后端发送的模式。前端使用相同的组件进行渲染。

本页的演示使用可读的名称，例如 **Host**，因为当没有其他内容时，名称就是标签。在实际代码中，名称是类似 `host` 的键，标签来自翻译。参见 [标签和助手](/design/components/form#labels-and-helpers)。

## 何时使用 {#when-to-use}
使用此表单的情况：

- 表单包含多个字段。你可以写更少的代码，并且你的表单看起来和行为方式都和 Home Assistant 中的其他表单一样：相同的间距、相同的控件、相同的验证。
- 一起保存的设置，例如辅助工具的选项或卡片的编辑器。

不适合使用此表单的情况：

- 单个控件具有独立功能的情况，例如立即应用设置的开关。直接使用该组件，例如 [switch](/design/components/switch) 或 [input](/design/components/input)。

## 解剖结构 {#anatomy}
1. **表单错误**：关于整个表单的错误，位于顶部
2. **字段错误或警告**：位于相关字段上方的[提醒](/design/components/alert)
3. **字段**：用于单个值的控件，包括其标签和辅助说明。大多数字段是[选择器](/design/components/selector)
4. **网格**：可选，字段相互并排排列
5. **可展开部分**：可选，位于可打开和关闭的标题下的字段

## 变体 {#variants}
### 字段是选择器 {#fields-are-selectors}
前端几乎每个字段都是一个选择器：一个值的简短描述，比如“来自灯光域的实体”或“0到100之间的数字”。选择器决定控件的类型。这些选择器与集成在其操作字段中使用的选择器相同，蓝图也在其输入中使用。 [选择器](/design/components/selector) 页面列出了所有选择器，并提供了每个选择器的演示。

`ha-form` 的实时演示，连接到一个演示 Home Assistant。

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](/design/components/form)。

```html
<ha-form data-props='{"schema": [{"name": "Light", "selector": {"entity": {"filter": {"domain": "light"}}}}, {"name": "Brightness", "selector": {"number": {"min": 0, "max": 100, "unit_of_measurement": "%"}}}, {"name": "Transition", "selector": {"duration": {}}}], "data": {"Light": "light.living_room_lamp", "Brightness": 70}}'></ha-form>
```

### 必填字段和默认值 {#required-fields-and-defaults}
必填字段会显示必填标记，且空值验证失败。默认值是在用户留下字段为空时的值。对于非必填字段，默认值将显示为占位符。

`ha-form` 的实时演示，连接到一个演示 Home Assistant。

```html
<ha-form data-props='{"schema": [{"name": "Name", "required": true, "selector": {"text": {}}}, {"name": "Scan interval", "default": 30, "selector": {"number": {"min": 5, "max": 3600, "mode": "box", "unit_of_measurement": "seconds"}}}], "data": {}}'></ha-form>
```

### 标签和辅助说明 {#labels-and-helpers}
每个字段都有一个标签，并且可以在其下方添加帮助文本。这些都来自翻译内容。没有翻译标签时，表单会显示字段的名称。对于快速测试这是可以的，但对于用户来说不行：名称是像 `scan_interval` 这样的键，并没有被翻译。字段内的值，例如下拉选项，也是经过翻译的。

### 网格 {#grids}
网格将字段并列放置。用于属于同一组的短字段，例如最小值和最大值。列的最小宽度为 200 像素，当没有足够空间时会换到新行，因此网格在手机上也会堆叠。

`ha-form` 的实时演示，连接到演示 Home Assistant。

```html
<ha-form data-props='{"schema": [{"name": "", "type": "grid", "schema": [{"name": "Minimum", "selector": {"number": {"mode": "box"}}}, {"name": "Maximum", "selector": {"number": {"mode": "box"}}}]}, {"name": "Step", "selector": {"number": {"mode": "box"}}}], "data": {"Minimum": 0, "Maximum": 100, "Step": 1}}'></ha-form>
```

### 可展开部分 {#expandable-sections}
可展开部分将字段归类在一个标题下，用户可以打开或关闭。使用它可以使长表单保持简洁：将大多数人需要的字段放在顶部，其余的隐藏起来，比如高级选项或卡片交互。

`ha-form` 的实时演示，连接到演示 Home Assistant。

```html
<ha-form data-props='{"schema": [{"name": "Name", "selector": {"text": {}}}, {"name": "advanced", "type": "expandable", "flatten": true, "title": "Advanced options", "schema": [{"name": "Scan interval", "selector": {"number": {"min": 5, "max": 3600, "mode": "box", "unit_of_measurement": "seconds"}}}, {"name": "Debug logging", "selector": {"boolean": {}}}]}], "data": {"Name": "Living room"}}'></ha-form>
```

标题文本是该部分的标题，如果没有，则使用其翻译标签。部分可以在标题前放置图标。部分初始状态为关闭，除非设置为初始打开。部分的帮助文本显示在其内容顶部作为描述。卡片编辑器经常使用这些部分，并带有图标，如 **内容** 和 **交互**。

### 基于条件的字段 {#fields-on-a-condition}
有些字段只有在另一个字段具有特定值时才重要。这样的字段只有在其条件匹配时才会显示。在这里，用户名和密码仅在启用身份验证时显示：

`ha-form` 的实时演示，连接到演示 Home Assistant。

```html
<ha-form data-props='{"schema": [{"name": "Use authentication", "selector": {"boolean": {}}}, {"name": "Username", "visible": {"field": "Use authentication", "value": true}, "selector": {"text": {}}}, {"name": "Password", "visible": {"field": "Use authentication", "value": true}, "selector": {"text": {"type": "password"}}}], "data": {"Use authentication": false}}'></ha-form>
```

### 其他字段类型 {#other-field-types}
在选择器之前，表单有自己的字段类型，并且它仍然会渲染它们。你大多在配置流程中看到它们，因为后端仍然会发送这些字段。在新表单中，请使用选择器。

`ha-form` 的实时演示，连接到演示 Home Assistant。

```html
<ha-form data-props='{"schema": [{"name": "Name", "type": "string"}, {"name": "Port", "type": "integer"}, {"name": "Mode", "type": "select", "options": [["auto", "Automatic"], ["manual", "Manual"]]}, {"name": "Enabled", "type": "boolean"}], "data": {"Name": "Living room", "Mode": "auto", "Enabled": true}}'></ha-form>
```

完整的字段类型列表在[其他字段类型](/design/components/form#other-field-types-in-code)的代码部分。

## 行为- **更改**：任何字段的更改都会更新表单数据，并一次性报告所有更改。 {#behavior}
- **错误**：表单错误显示在顶部的错误提示中。字段错误显示在该字段正上方的错误提示中。错误列表以项目符号列表的形式显示在提示中。
- **警告**：字段警告在字段上方显示警告提示（当字段没有错误时）。整个表单没有警告。
- **验证**：检查表单会检查每个可见字段，并将焦点移到第一个无效字段。
- **隐藏字段**：条件不匹配的字段不会渲染，并在检查表单时被跳过。其值不再计入其他字段的条件。
- **禁用**：禁用的表单会禁用其所有字段。单个字段也可以被禁用。`ha-form` 的实时演示，已连接到演示 Home Assistant。

```html
<ha-form data-props='{"schema": [{"name": "Host", "required": true, "selector": {"text": {}}}, {"name": "Port", "selector": {"number": {"min": 1, "max": 65535, "mode": "box"}}}], "data": {"Host": "192.168.1.200", "Port": 8080}, "error": {"base": "Could not connect to the device.", "Host": "No device answers on this address."}}'></ha-form>
```

## 规格 {#specs}
该表单仅设置其各部分之间的间距。每个字段都有其组件自身的规格。

| 属性 | 值 | 标记 |
| --- | --- | --- |
| 字段之间的间距 | 24px | 无 |
| 字段警告与字段之间的间距 | 4px | 无 |
| 网格列间距 | 8px | `--ha-space-2` |
| 网格行间距 | 24px | `--ha-space-6` |
| 网格最小列宽 | 200px | `--form-grid-min-width` |
| 网格列数 | 适合的尽量多 | `--form-grid-column-count` |
| 可展开部分 | 描边 [展开面板](/design/components/expansion-panel)，8px 圆角 | `--ha-border-radius-md` |
| 可展开部分内容填充 | 12px | 无 |
| 部分描述下方间距 | 24px | 无 |
| 部分图标颜色 | 次要文本颜色 | `--secondary-text-color` |

## 指南 {#guidelines}
- 在合理的情况下使字段可选，并为其提供合适的默认值。一个好的默认值可以帮助用户，同时不会妨碍那些想要其他选项的人。
- 为每个字段提供合适的标签、必要时的辅助文本，以及清晰的验证反馈。有关用词，请参见 [UI 文本](/design/ui-text)。

作为实时演示的示例和禁忌。两者都与演示 Home Assistant 相关。

**示例:** 说明出了什么问题，以及人们可以采取什么措施。

```html
<ha-form data-props='{"schema": [{"name": "Host", "required": true, "selector": {"text": {}}}], "data": {"Host": "192.168.1.200"}, "error": {"Host": "No device answers on this address. Check that the device is turned on."}}'></ha-form>
```

**禁忌:** 显示含糊的错误，让人摸不着头脑。

```html
<ha-form data-props='{"schema": [{"name": "Host", "required": true, "selector": {"text": {}}}], "data": {"Host": "192.168.1.200"}, "error": {"Host": "Invalid input."}}'></ha-form>
```

## 无障碍功能 {#accessibility}
### 键盘和焦点 {#keyboard-and-focus}
表单本身不添加任何按键：每个字段处理自己的键盘输入。<kbd>Tab</kbd> 按键按模式顺序移动焦点。聚焦表单会聚焦第一个字段。检查表单时，会将焦点移到第一个无效字段。

### 屏幕阅读器 {#screen-readers}
每个字段都会通过其自身的标签宣布，如其组件页面所述。已经打开的表单上出现的错误和警告会被大多数屏幕阅读器立即读取，但它们并未与字段关联。可展开部分的标题会被宣布为标题。

### 在代码中 {#in-the-code}
- 表单委托焦点，因此聚焦 `<ha-form>` 会聚焦其第一个字段。
- 表单不是 `<form>` 元素，并且本身没有角色。
- 每个字段的标签来自 `computeLabel`，字段组件将其转换为可访问名称。请参阅每个组件的页面了解具体方法。
- 错误和警告是具有 `alert` 角色的提示。当它们出现在已打开的表单上时，大多数屏幕阅读器会立即朗读它们。它们没有通过 `aria-describedby` 与其字段连接。
- 可展开部分的标题具有 `heading` 角色，默认为级别 3。

## 相关内容 {#related}
- [选择器](/design/components/selector)：表单的字段
- [展开面板](/design/components/expansion-panel)：可展开部分的基础
- [警告](/design/components/alert)：错误和警告的显示方式
- [界面文本](/design/ui-text)：如何编写标签、帮助文本和错误信息

## 在代码中 {#in-code}
该元素是 `<ha-form>`。模式、数据和函数只能通过代码以属性的方式设置。

```ts
const SCHEMA = [
  { name: "host", required: true, selector: { text: {} } },
  { name: "port", selector: { number: { min: 1, max: 65535, mode: "box" } } },
  { name: "ssl", selector: { boolean: {} } },
] as const satisfies readonly HaFormSchema[];

html`
  <ha-form
    .hass=${this.hass}
    .data=${this._data}
    .schema=${SCHEMA}
    .error=${this._errors}
    .computeLabel=${this._computeLabel}
    .computeHelper=${this._computeHelper}
    @value-changed=${this._valueChanged}
  ></ha-form>
`;
```

在本网站的 HTML 中，这些属性以 JSON 形式放在 `data-props` 中：

```html
<ha-form data-props='{"schema": [{"name": "Host", "selector": {"text": {}}}], "data": {}}'></ha-form>
```

### 字段 {#fields}
字段看起来像这样：

```js
{ name: "brightness", selector: { number: { min: 0, max: 100, unit_of_measurement: "%" } } }
```

每个字段还可以有：

- `required`：字段需要一个值。它会得到一个必填标记，空值会验证失败。
- `default`：当人们留空字段时的值。对于非必填字段，默认值会显示为占位符。
- `disabled`：显示字段，但人们无法更改它。
- `description`：一个对象，包含 `suggested_value`，在表单打开时填写，以及 `suffix`，显示在旧文本和数字字段的末尾。
- `visible`：何时显示字段。见 [条件](/design/components/form#conditions)。
- `context`：将另一个字段的值传递给此字段。见 [上下文](/design/components/form#context)。

### 标签、帮助信息和数值 {#labels-helpers-and-values}
在实际代码中，传递 `computeLabel`。它会获取每个字段的 schema，并返回标签。大多数表单会在翻译中查找名称：

```ts
private _computeLabel = (schema: SchemaUnion<typeof SCHEMA>) =>
  this.hass.localize(`ui.panel.config.my_feature.fields.${schema.name}`);
```

`computeHelper` 的工作原理相同，并返回字段下方的帮助文本。对于不需要帮助的字段，返回空。

对于字段内的值，例如 select 的选项，传递 `localizeValue`。带有 `translation_key` 的选择器会通过它查找选项标签。

### 错误和警告 {#errors-and-warnings}
设置 `error` 以显示出了什么问题。它是一个对象，以字段名为键。键 `base` 用于与整个表单相关的错误，例如连接失败。

错误信息会按原样显示，除非你传递 `computeError`。配置流程以错误的形式发送翻译键，并使用 `computeError` 将它们转换为文本。

`warning` 的功能相同，只是警告替代了错误，并使用 `computeWarning` 将其转换为文本。它没有 `base`。

### 网格 {#grids-1}
```js
{
  name: "",
  type: "grid",
  schema: [
    { name: "min", selector: { number: { mode: "box" } } },
    { name: "max", selector: { number: { mode: "box" } } },
  ],
}
```

如果名称为空，网格的字段将写入表单本身的数据。如果有名称，它们将写入该名称下的嵌套对象，除非你设置了 `flatten: true`。设置 `column_min_width` 以更改最小列宽。

### 可展开的部分 {#expandable-sections-1}
一个部分有 `type: "expandable"` 和它自己的 `schema`。在标题前添加 `icon` 或 `iconPath` 以显示图标。设置 `expanded: true` 可从一开始就打开部分。像网格一样，部分的字段将写入嵌套对象，除非你设置了 `flatten: true`。设置 `headingLevel` 可更改标题的标题级别，默认值为 3。

### 条件 {#conditions}
在字段上设置 `visible` 以仅在满足条件时显示它。它可以是 `true` 或 `false`，一个条件，或者必须全部匹配的条件列表。

```js
{
  name: "password",
  visible: { field: "use_auth", value: true },
  selector: { text: { type: "password" } },
}
```

一个条件比较 `field` 与 `value`。`operator` 默认为 `eq`，也可以是 `not_eq`、`in`、`not_in`（带值列表）、`exists` 或 `not_exists`。要组合条件，请使用 `condition: "and"`、`"or"` 或 `"not"`，以及 `conditions` 列表。

### 上下文 {#context}
有些选择器需要另一个值才能工作：状态选择器需要知道列出哪个实体的状态。在字段上设置 `context`，将选择器的上下文键映射到另一个字段的名称。例如，状态选择器从 `filter_entity` 键读取实体：

```js
{ name: "state", selector: { state: {} }, context: { filter_entity: "entity" } }
```

### 代码中的其他字段类型 {#other-field-types-in-code}
- `string`：文本字段。将 `format` 设置为 `email` 或 `url` 时，它使用该输入类型。名称中包含 `password`、`secret` 或 `token` 的字段会被掩码。
- `integer`：整数。既设置 `valueMin` 又设置 `valueMax` 时，它会显示一个滑块。
- `float`：小数。
- `boolean`：复选框。
- `select`：从值和标签配对列表中选择一个选项。
- `multi_select`：多个选项，可以是复选框，也可以在列表很长时作为下拉菜单。
- `positive_time_period_dict`：以小时、分钟和秒表示的持续时间。
- `constant`：显示标签和固定的 `value`，作为文本。

类型 `grid`、`expandable`、`optional_actions` 和 `divider` 用于布局。`optional_actions` 将其字段隐藏在添加按钮后面，因此用户只添加他们需要的字段。`divider` 在字段之间绘制一条线。

### 属性 {#properties}
这些只能通过代码设置：- `schema`: 字段列表。必填。
- `data`: 值，以字段名称为键的对象。
- `hass`: Home Assistant 对象。大多数选择器需要它。
- `error`: 要显示的错误，以字段名称为键，对于整个表单使用 `base`。
- `warning`: 要显示的警告，以字段名称为键。
- `computeLabel`: 一个函数，获取字段的模式和数据，并返回标签。
- `computeHelper`: 一个函数，获取字段的模式，并返回帮助文本。
- `computeError`: 一个函数，获取错误和模式，并返回要显示的文本。
- `computeWarning`: 同上，用于警告。
- `localizeValue`: 一个函数，获取翻译键，并返回文本。选择器使用它来显示选项的标签。
- `context`: 传递给表单中每个选择器的值，与每个字段的上下文合并。

### 属性 {#attributes}
- `disabled`：禁用所有字段。
- `narrow`：告诉选择器该表单在窄屏上。

### 方法 {#methods}
- `reportValidity()`：检查每个可见字段，将焦点移到第一个无效字段，并在表单有效时返回 `true`。保存前调用它。

### 事件 {#events}
- `value-changed`：在任何字段的每次变化时触发。`event.detail.value` 包含表单的所有数据，而不仅仅是更改的字段。表单也会更新其自身的 `data`。

### 样式 {#styling}
- `--form-grid-column-count`：网格中的列数。默认情况下，尽可能多。
- `--form-grid-min-width`：网格列的最小宽度。默认值为 `200px`。

字段周围的包装器暴露为 `root` 部分。

来源: [`src/components/ha-form/ha-form.ts`](https://github.com/home-assistant/frontend/blob/dev/src/components/ha-form/ha-form.ts)
