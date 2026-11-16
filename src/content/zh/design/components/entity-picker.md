---
title: 实体选择器
description: 实体选择器让人们从他们家中的所有实体中选择一个实体，并可以搜索。
sidebarGroup: 采摘者
---


# 实体选择器 {#entity-picker}
Live demo of `ha-entity-picker`，连接到一个演示 Home Assistant。

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](/design/components/entity-picker)。

```html
<ha-entity-picker label="Entity" value="light.living_room_lamp"></ha-entity-picker>
<ha-entity-picker label="Entity"></ha-entity-picker>
```

## 概述 {#overview}
实体选择器是一个用于选择一个 [实体](/glossary/entity) 的字段：卡片显示的灯光、辅助工具读取的传感器、自动化监控的实体。选择该字段以打开可搜索的列表。每一行显示实体名称，并以其设备和区域作为上下文，这样人们就能区分两个名为 **Ceiling** 的灯。

实体选择器是前端使用最多的选择器，在大多数地方都是通过实体选择器使用。当你在表单之外构建自定义编辑器时，可以直接使用该元素。

## 何时使用 {#when-to-use}
使用实体选择器用于：

- 精确选择一个实体
- 表单之外的自定义编辑器

不要使用实体选择器用于：

- 选择多个实体。使用实体[选择器](/design/components/selector)，它可以允许多个实体。它会为每个实体渲染一个选择器，并在它们下方为下一个实体渲染一个选择器，一旦列表中有实体，这个选择器会变成**添加实体**按钮。
- 选择一个操作所作用的对象，例如要打开的灯。使用目标选择器：它在一个字段中接受实体、设备、区域、楼层和标签。
- 选择设备而不是其实体之一。使用[设备选择器](/design/components/device-picker)。
- 表单中的字段。不要自己放置选择器：在[ha-form](/design/components/form)模式中使用实体选择器，表单会为你渲染选择器。

## 解剖结构 {#anatomy}
1. **标签**：位于字段上方
2. **字段**：显示值并打开列表的按钮
3. **值或占位符**：实体的状态图标和名称，以及其设备和区域，或者在为空时显示 **选择实体**
4. **清除按钮**：移除值，当字段非必填时可用
5. **箭头**：显示字段可以打开列表
6. **辅助信息**：字段下方的可选文本
7. **列表**：带有搜索字段和实体的弹出框。每行显示状态图标、实体名称、其设备和区域，以及末尾的集成名称。

## 变体 {#variants}
### 已筛选 {#filtered}
只显示对该字段有意义的实体。你可以根据域、设备类型、计量单位，以及要包含或排除的实体 ID 列表进行筛选。

`ha-entity-picker` 的实时演示，连接到一个演示 Home Assistant。仅限灯和开关。

```html
<ha-entity-picker label="Entity" include-domains='["light", "switch"]'></ha-entity-picker>
```

`ha-entity-picker` 的实时演示，连接到一个演示 Home Assistant。仅限温度和湿度传感器。

```html
<ha-entity-picker label="Sensor" include-domains='["sensor"]' include-device-classes='["temperature", "humidity"]'></ha-entity-picker>
```

### 使用辅助工具 {#with-a-helper}
标签说明了实体的用途：**实体**、**温度传感器**、**待控制的灯**。当选项需要解释时，可以在字段下方添加辅助说明。

`ha-entity-picker` 的现场演示，连接到演示 Home Assistant。

```html
<ha-entity-picker label="Temperature sensor" include-domains='["sensor"]' include-device-classes='["temperature"]' helper="The card shows the temperature of this sensor."></ha-entity-picker>
```

### 显示实体 ID {#showing-entity-ids}
列表显示每个实体的集成信息，在行末显示。选择器可以在名称下方显示实体 ID。用户也可以在个人资料设置中为每个选择器开启此功能。在人们以实体 ID 为思维方式的地方使用它，比如高级或面向 YAML 的界面。

`ha-entity-picker` 的现场演示，连接到演示 Home Assistant。

```html
<ha-entity-picker label="Entity" show-entity-id></ha-entity-picker>
```

### 添加按钮 {#add-button}
在实体列表中，下一个实体的选择器可以显示为按钮。它会始终显示为按钮，而不会显示值。选择一个实体会报告该实体，以便你可以将其添加到你的列表中。按钮标签默认为 **添加实体**，可以更改。

`ha-entity-picker` 的实时演示，连接到演示 Home Assistant。

```html
<ha-entity-picker add-button></ha-entity-picker>
```

### 自定义实体 ID {#custom-entity-ids}
默认情况下，人们只能从列表中选择实体。选择器也可以接受尚不存在的输入实体 ID。输入的值仍必须看起来像一个实体 ID，例如 `light.attic`。

## 行为 {#behavior}
- **启用**：选择字段会打开列表，并将焦点移动到其搜索字段。
- **悬停和按下**：字段会显示涟漪效果。
- **聚焦**：字段底部的线条变为2px厚，并显示主色。
- **搜索**：输入内容时列表会根据输入实时过滤。当没有匹配项时，列表会显示 **未找到匹配的实体**。
- **未知**：当值是不存在的实体（例如已删除的实体）时，字段会变为安静的警告色，并显示 **选择了未知实体**。用户可以选择其他实体，或清空字段。
- **禁用**：字段会变为50%不透明，并且无法打开。
- **窄屏**：当窗口宽度最多为870px或高度最多为500px时，列表会以底部弹出层的形式打开，而不是弹出窗口。选择一个实体会关闭列表。一旦列表关闭，会报告新值。

`ha-entity-picker` 的实时演示，连接到演示 Home Assistant。

```html
<ha-entity-picker label="Entity" value="light.attic"></ha-entity-picker>
<ha-entity-picker label="Entity" value="climate.thermostat" disabled></ha-entity-picker>
```

## 规格 {#specs}
实体选择器使用前端的共享选择字段和列表，`ha-picker-field` 和 `ha-generic-picker`。

### 字段 {#field}
| 属性 | 值 | 令牌 |
| --- | --- | --- |
| 标签与字段之间的间距 | 8px | 无 |
| 最小高度 | 56px | 无 |
| 起始内边距 | 16px | `--ha-space-4` |
| 结束内边距 | 8px | `--ha-space-2` |
| 部件间距 | 8px | `--ha-space-2` |
| 圆角 | 顶部4px，底部方形 | `--ha-border-radius-sm` |
| 背景 | 表单背景 | `--ha-color-form-background` |
| 底线 | 1px | `--ha-color-border-neutral-loud` |
| 聚焦时底线 | 2px | `--mdc-theme-primary` |
| 无效时底线 | 2px | `--error-color` |
| 占位文本 | 次要文本颜色 | `--secondary-text-color` |
| 清除按钮 | 32px | `--ha-icon-button-size` |
| 箭头图标 | 20px，在32px宽区域内 | `--mdc-icon-size` |
| 未知背景 | 微提示填充 | `--ha-color-fill-warning-quiet-resting` |
| 未知文本 | 提示文本 | `--ha-color-on-warning-normal` |
| 禁用 | 禁用表单背景50%不透明度 | `--ha-color-form-background-disabled` |
| 辅助文本上方间距 | 8px | `--ha-space-2` |

### 列表 {#list}
| 属性 | 值 | 令牌 |
| --- | --- | --- |
| 宽度 | 字段的宽度，至少250像素 | `--ha-generic-picker-width` |
| 最大宽度 | 宽度，除非已设置 | `--ha-generic-picker-max-width` |
| 最大高度 | 窗口高度的70%与500像素中较小者。当窗口高度最多为1000像素时，取70%与400像素中较小者 | 无 |
| 圆角 | 8像素 | `--ha-border-radius-md` |
| 阴影 | 中等阴影 | `--ha-box-shadow-m` |
| 行分隔线 | 行间1像素 | `--divider-color` |
| 底部弹出窗口圆角 | 20像素 | `--ha-border-radius-2xl` |
| 底部弹出窗口最大宽度 | 600像素 | 无 |

## 指南 {#guidelines}
- 仅显示对该字段有意义的实体。控制灯光的卡片应只提供灯光。
- 避免过于严格的筛选，否则人们可能会得到空列表而不知道原因。
- 仅在用户以实体 ID 思考时显示实体 ID。

通过现场演示说明该做与不该做。两个例子都连接到演示Home Assistant。

**该做:** 将列表筛选为字段所需的内容，并说明实体的用途。

```html
<ha-entity-picker label="Light to control" include-domains='["light"]'></ha-entity-picker>
```

**不该做:** 为仅能使用某一类型的字段提供家庭中的所有实体。

```html
<ha-entity-picker label="Entity"></ha-entity-picker>
```

## 无障碍功能 {#accessibility}
### 键盘 {#keyboard}
| 键 | 操作 |
| --- | --- |
| <kbd>Tab</kbd> | 将焦点移动到字段，如果有清除按钮则移动到清除按钮。禁用的字段将被跳过。 |
| <kbd>Enter</kbd> 或 <kbd>Space</kbd> | 当字段获得焦点时，打开列表。 |
| 输入 | 搜索列表。当列表打开时，焦点位于搜索字段。 |
| <kbd>向下箭头</kbd> 和 <kbd>向上箭头</kbd> | 在实体之间移动。 |
| <kbd>Home</kbd> 和 <kbd>End</kbd> | 跳转到第一个或最后一个实体。 |
| <kbd>Page up</kbd> 和 <kbd>Page down</kbd> | 列表中翻页。 |
| <kbd>Enter</kbd> | 选择高亮的实体。在搜索时，顶部匹配项会被高亮。如果列表中只有一个选项，<kbd>Enter</kbd>即可选择。 |
| <kbd>Escape</kbd> | 关闭列表。 |

### 焦点 {#focus}
焦点显示为字段下方更粗的线，而不是焦点环。当列表以弹出框形式打开时，焦点保持在其中。在列表中，焦点保持在搜索字段，而方向键移动高亮显示。

### 目标尺寸 {#target-size}
该字段高度至少为56像素，并填充其获得的宽度。清除按钮的尺寸为32像素乘32像素。

### 屏幕阅读器 {#screen-readers}
- 该字段会被宣布为一个按钮，由其标签和其中的实体命名。
- 列表会被宣布为带有选项列表的对话框，以及被选中的实体。
- 清除按钮会被宣布为“清除”，使用用户的语言。

### 在代码中 {#in-the-code}
- 焦点被委托给字段中的原生 `<button>`。弹出层会捕获焦点。列表中高亮的行标记有 `active` 属性。列表没有设置 `aria-activedescendant`。
- 字段上方的标签是一个 `<label>` 元素，并未与字段关联。该字段是一个原生 `<button>`，通过 `aria-labelledby` 将标签作为其可访问名称的一部分，与字段中的文本一起。
- 列表在一个具有 `dialog` 和 `aria-modal="true"` 角色的元素中打开，并以标签命名。
- 列表的角色为 `listbox`，每个实体的角色为 `option`，选定的实体具有 `aria-selected`。
- 清除按钮的可访问名称为“Clear”，已翻译为用户的语言。

## 相关内容 {#related}
- [设备选择器](/design/components/device-picker)：选择一个设备
- [区域选择器](/design/components/area-picker)：选择一个区域
- [选择器](/design/components/selector)：实体选择器，用于选择一个或多个实体
- [表单](/design/components/form)：根据模式渲染选择器
- [状态图标](/design/components/state-icon)：每一行的图标

## 在代码中 {#in-code}
该元素是 `<ha-entity-picker>`。它从应用提供的上下文中读取状态、注册表和翻译，因此你不需要向它传递 `hass`。

```ts
html`
  <ha-entity-picker
    .label=${"Light"}
    .value=${this._entityId}
    .includeDomains=${["light"]}
    @value-changed=${this._entityChanged}
  ></ha-entity-picker>
`;
```

在 HTML 中，列表属性使用 JSON：

```html
<ha-entity-picker label="Light" include-domains='["light"]'></ha-entity-picker>
```

### 属性- `label`: 字段上方的标签。 {#attributes}
- `value`: 选定实体的实体ID。
- `helper`: 字段下方的帮助文本。
- `placeholder`: 空字段中的文本。默认值为**选择一个实体**。
- `search-label`: 列表中搜索字段的占位符。
- `include-domains`: 仅显示这些域的实体。
- `exclude-domains`: 隐藏这些域的实体。
- `include-device-classes`: 仅显示具有这些设备类别的实体。
- `include-unit-of-measurement`: 仅显示具有这些单位的实体。
- `include-entities`: 仅显示这些实体。
- `exclude-entities`: 隐藏这些实体。
- `show-entity-id`: 在列表中显示每个实体的实体ID。
- `allow-custom-entity`: 接受列表中不存在的已输入实体ID。
- `add-button`: 显示一个按钮而不是字段。
- `add-button-label`: 该按钮的标签。默认值为**添加实体**。
- `hide-clear-icon`: 隐藏清除值的按钮。
- `required`: 将字段标记为必填。

- `disabled`：禁用选择器。
- `autofocus`：在选择器呈现时将焦点置于选择器上。

### 属性 {#properties}
这些只能通过代码设置：

- `entityFilter`：一个获取每个实体状态对象的函数，并返回 `true` 来显示它。用于过滤属性无法表达的内容，例如支持的功能。
- `extraOptions`：实体上方的额外行。每一行都有一个 `id`（被选中时的值，不需要是实体 ID）、一个 `primary` 文本，且可选地有一个 `secondary` 文本、一个 `icon`、一个 `icon_path` 或一个 `entity_id` 来显示图标。设置 `hide_clear` 可在该选项被选中时隐藏清除按钮。
- `createDomains`：用户可以为辅助域创建新实体，直接从列表中选择。选择一个辅助域会打开创建辅助实体的对话框，并在创建后选择新实体。在本页的演示中无法创建辅助实体。

### 方法 {#methods}
- `open()`：打开列表。

### 事件 {#events}
- `value-changed`：当人们选择或清除一个实体时触发。新实体 ID 在 `event.detail.value` 中，或清除时在 `undefined` 中。
- `change`：在 `value-changed` 之后触发。

### 样式 {#styling}
- `--ha-generic-picker-width`：列表的宽度。默认为字段的宽度，且至少为 `250px`。
- `--ha-generic-picker-max-width`：列表的最大宽度。

在窄屏幕上，列表会作为底部弹出板打开，而不是在字段下方显示。

来源：[`src/components/entity/ha-entity-picker.ts`](https://github.com/home-assistant/frontend/blob/dev/src/components/entity/ha-entity-picker.ts)
