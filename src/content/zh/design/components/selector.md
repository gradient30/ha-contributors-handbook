---
title: 选择器
description: ha-selector 为选择器渲染正确的控件，这是一个值的简短描述，集成、蓝图和表单在 Home Assistant 中随处使用。
sidebarGroup: 表格
sidebarGroup: 表单

---

# 选择器 {#selector}

实时演示 `ha-selector`，连接到演示 Home Assistant。

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](https://contributors.home-assistant.io/design/components/selector/)。

```html
<ha-selector label="Light" data-props='{"selector": {"entity": {"filter": {"domain": "light"}}}, "value": "light.living_room_lamp", "required": false}'></ha-selector>
<ha-selector label="Brightness" data-props='{"selector": {"number": {"min": 0, "max": 100, "unit_of_measurement": "%"}}, "value": 70, "required": false}'></ha-selector>
<ha-selector label="Turn off when nobody is home" data-props='{"selector": {"boolean": {}}, "value": true, "required": false}'></ha-selector>
```

## 概述 {#overview}

选择器描述一个值：“来自灯光领域的实体”、“0到100之间的数字”、“这些选项中的一个”。选择器组件根据该描述显示匹配的控件。这就是为什么同类值在 Home Assistant 中到处看起来都一样的原因。

这些选择器在 Home Assistant 的其他部分也是共享的：

- 集成使用它们来处理其操作字段。当你为自动化添加操作时，生成的表单就是由它们构建的。
- 蓝图在输入中使用它们。
- 集成可以在其配置流程和选项流程的表单中使用它们。
- 前端在自己的表单中使用它们，例如仪表板卡片的可视化编辑器。

## 何时使用 {#when-to-use}

单独使用选择器组件的情况：

- 按顺序渲染各个字段，这些字段来自你从其他地方获得的选择器。前端就是这样处理操作、触发器和条件的字段，以及蓝图输入的。

不要单独用于：

- 表单。将选择器放入[表单](/design/components/form)的 schema 中，由表单渲染它，包括标签、帮助信息、错误提示和布局。这才是大多数情况下你真正需要的。

## 解剖结构 {#anatomy}

选择器本身没有独立的部件。它显示选择器类型的一个控件，并传递标签、辅助信息、值和其他设置。该控件通常是本站的其他组件之一，例如 [实体选择器](/design/components/entity-picker) 或 [开关](/design/components/switch)。

## 变体 {#variants}

每种选择器类型都是一个变体。这些是你最常遇到的。每一部分说明人们看到的内容，以及它们提供的值类型。每种类型的选项列在 [按类型的选项](/design/components/selector#options-per-type) 的代码部分下。

### 文本 {#text}

对于自由文本，在一个 [文本输入](/design/components/input) 中。对于较长的文本，它可以扩展到多行，隐藏人们输入的密码，检查电子邮件地址或网页地址，并在值的前后显示固定文本。它还可以接受一个值列表。

`ha-selector` 的现场演示，连接到一个演示 Home Assistant。

```html
<ha-selector label="Name" data-props='{"selector": {"text": {}}, "value": "Living room", "required": false}'></ha-selector>
<ha-selector label="Message" data-props='{"selector": {"text": {"multiline": true}}, "value": "The front door is open.", "required": false}'></ha-selector>
<ha-selector label="Password" data-props='{"selector": {"text": {"type": "password"}}, "required": false}'></ha-selector>
<ha-selector label="Address" data-props='{"selector": {"text": {"prefix": "https://", "suffix": "/api"}}, "value": "example.local", "required": false}'></ha-selector>
```

### 数值 {#number}

用于一个数字。若有范围，则显示一个 [滑块](/design/components/slider)，旁边有一个输入框可输入精确数字。也可以只显示输入框，这是没有范围时的情况。单位和步长是可选的。

`ha-selector` 的实时演示，连接到 Home Assistant 的演示。

```html
<ha-selector label="Volume" data-props='{"selector": {"number": {"min": 0, "max": 100, "unit_of_measurement": "%"}}, "value": 35, "required": false}'></ha-selector>
<ha-selector label="Target temperature" data-props='{"selector": {"number": {"min": 7, "max": 35, "step": 0.5, "mode": "box", "unit_of_measurement": "°C"}}, "value": 21, "required": false}'></ha-selector>
```

### 布尔值 {#boolean}

用于开启或关闭。它显示一个 [开关](/design/components/switch)，标签在其旁边。

`ha-selector` 的实时演示，连接到 Home Assistant 的演示。

```html
<ha-selector label="Show the state" helper="Shows the state below the name." data-props='{"selector": {"boolean": {}}, "value": true, "required": false}'></ha-selector>
```

### 选择 {#select}

用于从列表中选择一个选项。每个选项都有一个值和一个用户可见的标签。

当选项少于六个时，选项显示为单选按钮。当选项有六个或更多时，它们显示在下拉菜单中。选择器也可以被指定使用哪一种方式。

`ha-selector` 的实时演示，连接到 Home Assistant 演示。

```html
<ha-selector label="Mode" data-props='{"selector": {"select": {"options": [{"value": "single", "label": "Single"}, {"value": "restart", "label": "Restart"}, {"value": "queued", "label": "Queued"}, {"value": "parallel", "label": "Parallel"}]}}, "value": "single", "required": false}'></ha-selector>
<ha-selector label="Day" data-props='{"selector": {"select": {"mode": "dropdown", "options": [{"value": "mon", "label": "Monday"}, {"value": "tue", "label": "Tuesday"}, {"value": "wed", "label": "Wednesday"}, {"value": "thu", "label": "Thursday"}, {"value": "fri", "label": "Friday"}, {"value": "sat", "label": "Saturday"}, {"value": "sun", "label": "Sunday"}]}}, "value": "mon", "required": false}'></ha-selector>
```

选项也可以显示为 [选择框](/design/components/select-box)：大型方块，带有描述，并可选择性地添加图片。适用于需要解释的少量选项。

`ha-selector` 的实时演示，连接到 Home Assistant 演示。

```html
<ha-selector label="Layout" data-props='{"selector": {"select": {"mode": "box", "options": [{"value": "horizontal", "label": "Horizontal", "description": "The icon next to the name."}, {"value": "vertical", "label": "Vertical", "description": "The icon above the name."}]}}, "value": "horizontal", "required": false}'></ha-selector>
```

用户也可以选择多个选项。作为列表时，选项显示为复选框。作为下拉菜单时，被选的选项在上方显示为标签。选择器可以让用户输入自己的值，并按标签对选项排序。

`ha-selector` 的实时演示，连接到 Home Assistant 演示。

```html
<ha-selector label="Notify on" data-props='{"selector": {"select": {"multiple": true, "options": [{"value": "open", "label": "Open"}, {"value": "closed", "label": "Closed"}, {"value": "unavailable", "label": "Unavailable"}]}}, "value": ["open"], "required": false}'></ha-selector>
```

### 实体 {#entity}

用于实体。它显示 [实体选择器](/design/components/entity-picker)。它只能提供符合条件的实体，根据其域、设备类别、集成、支持的功能或单位。用户可以选择一个或多个实体。

`ha-selector` 的实时演示，连接到演示 Home Assistant。

```html
<ha-selector label="Temperature sensor" data-props='{"selector": {"entity": {"filter": {"domain": "sensor", "device_class": "temperature"}}}, "value": "sensor.living_room_temperature", "required": false}'></ha-selector>
<ha-selector label="Lights" data-props='{"selector": {"entity": {"multiple": true, "filter": {"domain": "light"}}}, "value": ["light.living_room_lamp"], "required": false}'></ha-selector>
```

### 设备 {#device}

用于设备。它显示 [设备选择器](/design/components/device-picker)。它可以根据设备本身进行过滤，如其集成或制造商，或者只提供具有匹配实体的设备。用户可以选择一个或多个设备。

`ha-selector` 的实时演示，连接到演示 Home Assistant。

```html
<ha-selector label="Speaker" data-props='{"selector": {"device": {"entity": {"domain": "media_player"}}}, "value": "speaker", "required": false}'></ha-selector>
```

### 区域 {#area}

用于区域。它显示 [区域选择器](/design/components/area-picker)。像设备选择器一样，它可以根据区域中的实体和设备进行过滤。用户可以选择一个或多个区域。

`ha-selector` 的实时演示，连接到演示 Home Assistant。

```html
<ha-selector label="Area" data-props='{"selector": {"area": {}}, "value": "kitchen", "required": false}'></ha-selector>
<ha-selector label="Areas" data-props='{"selector": {"area": {"multiple": true}}, "value": ["living_room", "bedroom"], "required": false}'></ha-selector>
```

### 楼层和标签 {#floor-and-label}

用于楼层或标签。它们的工作方式类似于区域选择器，虽然标签选择器没有过滤器。

`ha-selector` 的实时演示，连接到演示 Home Assistant。

```html
<ha-selector label="Floor" data-props='{"selector": {"floor": {}}, "value": "ground", "required": false}'></ha-selector>
<ha-selector label="Label" data-props='{"selector": {"label": {}}, "value": "energy", "required": false}'></ha-selector>
```

### 目标 {#target}

操作作用的对象。人们可以添加实体、设备、区域、楼层和标签，任意组合，操作会应用于所有这些对象。可添加的内容可以被筛选，就像实体和设备选择器一样。

`ha-selector` 的实时演示，连接到演示 Home Assistant。

```html
<ha-selector label="Targets" data-props='{"selector": {"target": {"entity": {"domain": "light"}}}, "value": {"area_id": ["living_room"], "entity_id": ["light.kitchen_ceiling"]}, "required": false}'></ha-selector>
```

### 时间和日期 {#time-and-date}

用于某个时间、日期或两者。时间选择器显示秒数，除非它们被关闭。

`ha-selector` 的实时演示，连接到演示 Home Assistant。

```html
<ha-selector label="Wake-up time" data-props='{"selector": {"time": {"no_second": true}}, "value": "07:30:00", "required": false}'></ha-selector>
<ha-selector label="Date" data-props='{"selector": {"date": {}}, "value": "2026-12-24", "required": false}'></ha-selector>
<ha-selector label="Date and time" data-props='{"selector": {"datetime": {}}, "value": "2026-12-24 07:30:00", "required": false}'></ha-selector>
```

### 持续时间 {#duration}

用于表示一段时间，如延迟或转换。它显示小时、分钟和秒。可以添加天和毫秒，也可以省略秒。

`ha-selector` 的实时演示，连接到 Home Assistant 演示。

```html
<ha-selector label="Delay" data-props='{"selector": {"duration": {}}, "value": {"hours": 0, "minutes": 5, "seconds": 0}, "required": false}'></ha-selector>
<ha-selector label="Keep the history for" data-props='{"selector": {"duration": {"enable_day": true, "enable_second": false}}, "value": {"days": 10, "hours": 0, "minutes": 0}, "required": false}'></ha-selector>
```

持续时间也可以为负值，例如在日照条件中作为日落的偏移。在偏移版本中，人们首先选择 **无偏移**、**之前** 或 **之后**，然后输入持续时间。

### 色温 {#color-temperature}

色温可以作为一个滑块，滑块背后有光的颜色显示，单位为开尔文或米雷德。

`ha-selector` 的实时演示，连接到 Home Assistant 示例。

```html
<ha-selector label="Color temperature" data-props='{"selector": {"color_temp": {"unit": "kelvin", "min": 2200, "max": 6500}}, "value": 2700, "required": false}'></ha-selector>
```

### 颜色 {#color}

RGB 颜色选择器用于选择颜色，可通过浏览器的取色器选择。

`ha-selector` 的实时演示，连接到 Home Assistant 示例。

```html
<ha-selector label="Color" data-props='{"selector": {"color_rgb": {}}, "value": [255, 160, 60], "required": false}'></ha-selector>
```

对于仪表盘上某个元素的颜色，请使用主题颜色选择器。它按名称提供主题颜色，使颜色保持与主题一致。

### 图标 {#icon}

图标选择器提供所有图标的可搜索列表。它可以显示当用户选择“无”时使用的图标。

`ha-selector` 的实时演示，连接到 Home Assistant 示例。

```html
<ha-selector label="Icon" data-props='{"selector": {"icon": {}}, "value": "mdi:sofa", "required": false}'></ha-selector>
```

### 状态 {#state}

对于一个实体的状态，例如恒温器的热量。选择器提供一个实体的可能状态及其翻译名称。在表单中，该实体通常来自其他字段。

`ha-selector` 的实时演示，连接到一个演示 Home Assistant。

```html
<ha-selector label="State" data-props='{"selector": {"state": {"entity_id": "climate.thermostat"}}, "value": "heat", "required": false}'></ha-selector>
```

### 没有演示的选择器 {#selectors-without-a-demo}

有些选择器需要比本页演示更多的 Home Assistant。位置选择器显示地图。模板和对象选择器是代码编辑器，而带字段的对象选择器是小表单的列表。动作、条件和触发器选择器显示其部分的完整自动化编辑器。媒体选择器可以浏览你的媒体播放器中的媒体。

总共有六十多种选择器类型。完整列表在代码部分的 [所有选择器类型](/design/components/selector#all-selector-types) 下。

## 行为 {#behavior}

- **变化**：当人们更改值时，选择器会报告新值。其形状取决于类型。
- **必填**：除非标记为可选，否则选择器是必填的。一个没有自身检查的必填选择器在为空时无效。
- **禁用**：禁用的选择器会禁用其控件。
- **旧选择器**：旧的名称和筛选选项在控件显示之前会转换为当前形式。

每个控件的状态，如悬停、聚焦和错误，都是其渲染组件的状态。

## 规格 {#specs}

选择器自身不绘制任何内容，因此它没有尺寸、间距或颜色。每种类型看起来都像它所显示的组件：请参阅[text input](/design/components/input)、[switch](/design/components/switch)、[slider](/design/components/slider)、[select box](/design/components/select-box)的规格，以及[entities](/design/components/entity-picker)、[devices](/design/components/device-picker)和[areas](/design/components/area-picker)的选择器。

## 指南 {#guidelines}

为值选择最具体的选择器。实体 ID 是文本，但实体选择器提供一个可搜索的列表，包含名称和图标，并且只提供符合条件的实体。选择器越具体，人们需要输入的内容就越少，出错的可能性也越小。

做与不做，作为实时演示。两者都与演示 Home Assistant 相关。

**做：** 使用实体选择器选择一个实体。

```html
<ha-selector label="Light" data-props='{"selector": {"entity": {"filter": {"domain": "light"}}}, "value": "light.living_room_lamp", "required": false}'></ha-selector>
```

**不做：** 让人们在文本框中输入实体 ID。

```html
<ha-selector label="Light" data-props='{"selector": {"text": {}}, "value": "light.living_room_lamp", "required": false}'></ha-selector>
```

- 将少量需要解释的选项显示为下拉框形式。
- 对于操作使用目标选择器，这样人们可以说“客厅的所有灯”，而不必逐个选择每盏灯。若要选择一个特定的实体，请使用实体选择器。

## 无障碍功能 {#accessibility}

### 键盘、焦点和屏幕阅读器 {#keyboard-focus-and-screen-readers}

该选择器自身不添加任何内容。键盘支持、焦点以及屏幕阅读器宣布的内容来自其显示的控件：参见每个组件的页面，如 [实体选择器](/design/components/entity-picker)、[开关](/design/components/switch) 或 [滑块](/design/components/slider)。

### 在代码中 {#in-the-code}

`ha-selector` 不添加自身的角色、标签或键。对其调用 `focus()` 会将焦点置于其渲染的控件上。

## 相关内容 {#related}

- [表单](/design/components/form)：从模式渲染选择器
- [实体选择器](/design/components/entity-picker)、[设备选择器](/design/components/device-picker) 和 [区域选择器](/design/components/area-picker)：实体、设备和区域选择器背后的控件
- [选择框](/design/components/select-box)：选择器的框模式
- [选择器文档](https://www.home-assistant.io/docs/blueprint/selectors/)：所有选项，以及集成和蓝图如何使用它们

## 在代码中 {#in-code}

该元素是 `<ha-selector>`。选择器和大多数值只能从代码中作为属性设置。

```ts
html`
  <ha-selector
    .hass=${this.hass}
    .selector=${{ number: { min: 0, max: 100, unit_of_measurement: "%" } }}
    .value=${this._brightness}
    .label=${"Brightness"}
    .required=${false}
    @value-changed=${this._brightnessChanged}
  ></ha-selector>
`;
```

在本网站的 HTML 中，这些属性放在 `data-props` 中，作为 JSON：

```html
<ha-selector label="Brightness" data-props='{"selector": {"number": {"min": 0, "max": 100}}, "value": 70}'></ha-selector>
```

### YAML 和代码中的选择器 {#selectors-in-yaml-and-code}

在 YAML 中，选择器是带有类型的键，以及其下的选项：

```yaml
brightness:
  selector:
    number:
      min: 0
      max: 100
      unit_of_measurement: "%"
```

在前端，它也是一样的，作为一个对象：

```js
{ number: { min: 0, max: 100, unit_of_measurement: "%" } }
```

有关每个选择器的所有选项，随着集成和蓝图的使用，请参见 [选择器文档](https://www.home-assistant.io/docs/blueprint/selectors/)。

### 每种类型的选项 {#options-per-type}

每种类型最常用的选项。home-assistant.io 上的 [选择器文档](https://www.home-assistant.io/docs/blueprint/selectors/) 包含了所有选项。

- `text`: `multiline` 用于较长的文本，`type` 用于另一种输入类型，如 `password`、`email` 或 `url`，`prefix` 和 `suffix` 用于围绕值的文本，`multiple` 用于列表。值是字符串或字符串列表。
- `number`: `min`、`max`、`step` 和 `unit_of_measurement`。`mode` 是 `slider` 或 `box`。没有范围时，它是一个框。值是数字。
- `boolean`: 无选项。值是 `true` 或 `false`。
- `select`: `options`，作为字符串或带有 `value` 和 `label` 的对象。`mode` 是 `list`、`dropdown` 或 `box`。没有模式时，少于六个选项为列表。`multiple`、`custom_value` 和 `sort`。值是所选选项的 `value`，或者是带有 `multiple` 的列表。
- `entity`: `filter`，可在 `domain`、`device_class`、`integration`、`supported_features` 或 `unit_of_measurement` 上使用，以及 `multiple`。值是实体 ID，或者是实体 ID 列表。

- `device`: `filter`，在设备本身，例如它的 `integration` 或 `manufacturer`，`entity`，只提供与实体匹配的设备，以及 `multiple`。该值是设备 ID，或设备 ID 列表。
- `area` 和 `floor`：`entity` 和 `device`，只提供与实体或设备匹配的选项，以及 `multiple`。`label`：仅 `multiple`。该值是 ID，或 ID 列表。
- `target`：`entity` 和 `device`，过滤可以添加的内容。该值是一个对象，包含 `entity_id`、`device_id`、`area_id`、`floor_id` 和 `label_id`，每个都是 ID 或 ID 列表，并且仅包含正在使用的。
- `time`：`no_second` 隐藏秒数。该值是一个类似 `07:30:00` 的字符串。`date` 给出 `2026-12-24`，`datetime` 给出 `2026-12-24 07:30:00`。

- `duration`：`enable_day`、`enable_millisecond` 和 `enable_second`（设置为 `false` 以去掉秒数）。`mode` 设置为 `signed` 允许负持续时间，而 `mode` 设置为 `offset` 会先询问 **无偏移**、**之前** 或 **之后**。该值是一个对象，包含 `hours`、`minutes` 和 `seconds`，以及启用时的 `days` 和 `milliseconds`。
- `color_temp`：`unit` 设置为 `kelvin`，以及使用 `min` 和 `max` 的范围。没有单位时，它以 mired 为单位。该值是一个数字。
- `color_rgb`：没有选项。该值是红、绿、蓝值的列表，范围从 0 到 255。
- `ui_color`：主题的颜色，以名称表示。
- `icon`：`placeholder`，当用户选择无时使用的图标。该值是图标名称，如 `mdi:sofa`。

- `state`: `entity_id`，该实体提供其状态。在一种形式中，该实体通常来自另一个领域，通过`context`。值是状态。

### 所有选择器类型 {#all-selector-types}

前端了解这些选择器类型：- `action`：一系列动作，就像脚本中的动作。
- `addon`：一个应用程序。`app` 选择器的旧名称。
- `app`：一个应用程序。
- `area`：一个区域。
- `areas_display`：区域的顺序，以及哪些是隐藏的。
- `assist_pipeline`：一个 Assist 管道。
- `attribute`：实体的一个属性。
- `automation_behavior`：自动化如何处理多个触发器或条件。
- `backup_location`：存储备份的位置。
- `boolean`：开或关。
- `button_toggle`：几个选项中的一个，作为一排按钮。
- `choose`：让人们在几个选择器之间进行选择，比如数字或实体。
- `color_rgb`：一种颜色，如红色、绿色和蓝色。
- `color_temp`：色温。
- `condition`：一系列条件。
- `config_entry`：一个集成条目。
- `constant`：一个固定值，以文本形式显示。
- `conversation_agent`：一个会话代理。
- `country`：一个国家。
- `date`：一个日期。
- `datetime`：日期和时间。

- `device`: 一个设备。
- `device_class`: 一个领域的设备类别。
- `duration`: 一段时间。
- `entity`: 一个实体。
- `entity_name`: 实体名称在仪表板上的显示方式。
- `file`: 要上传的文件。
- `floor`: 一层楼。
- `icon`: 一个图标。
- `label`: 一个标签。
- `language`: 一种语言。
- `location`: 地图上的一个地点，可选带半径。
- `media`: 媒体浏览器中的一个媒体项。
- `navigation`: Home Assistant 中的路径，比如仪表板视图。
- `number`: 一个数字。
- `numeric_threshold`: 一个阈值，如高于或低于某个数字或实体的状态。
- `object`: 任何数据，以 YAML 形式，或具有固定字段的条目列表。
- `period`: 一段时间，如今天或本周。
- `qr_code`: 显示二维码。它不接受输入。
- `select`: 从列表中选择一个或多个选项。

- `selector`：选择器，用于那些自己构建选择器的编辑器，如蓝图编辑器。
- `serial_port`：串口，如 USB 设备。
- `state`：实体的状态。
- `state_class`：传感器的状态类别。
- `statistic`：统计数据。
- `stt`：语音转文本引擎。
- `target`：用于操作的实体、设备、区域、楼层和标签。
- `template`：代码编辑器中的模板。
- `text`：文本。
- `theme`：主题。
- `time`：一天中的时间。
- `timezone`：时区。
- `trigger`：触发器列表。
- `tts`：文本转语音引擎。
- `tts_voice`：文本转语音引擎的语音。
- `ui_action`：当用户点击卡片时发生的操作。
- `ui_clock_date_format`：时钟卡片的日期格式。
- `ui_color`：主题颜色。
- `ui_state_content`：卡片显示的实体状态。
- `ui_time_format`：时间格式。
- `unit_of_measurement`：计量单位。以`ui_`开头的选择器是为仪表板卡片的编辑器设计的。

### 属性 {#properties}

这些只能通过代码设置：

- `selector`：选择器。必填。
- `hass`：Home Assistant 对象。大多数选择器需要它。
- `context`：来自其他地方的值，一些选择器会使用，比如状态选择器的实体。`ha-form` 会从字段的 `context` 填充它。
- `localizeValue`：一个获取翻译键并返回文本的函数。带有 `translation_key` 的选择器会使用它来显示选项的标签。

### 属性 {#attributes}

- `value`：值。对于非字符串的内容使用此属性。
- `label`：标签。
- `helper`：帮助文本，位于控件下方。
- `placeholder`：在没有值时显示的值。`ha-form` 将其设置为字段的默认值。
- `name`：字段的名称。
- `required`：标记字段为必填。注意：默认情况下这是 `true`。对于可选字段，将属性设置为 `false`。
- `disabled`：禁用控件。
- `narrow`：告知控件它处于窄屏状态。

### 方法 {#methods}

- `reportValidity()`：检查值，当值有效时返回 `true`。
- `focus()`：聚焦控件。

### 事件 {#events}

- `value-changed`：当用户更改值时触发。新值在 `event.detail.value` 中。其形状取决于选择器类型。

来源: [`src/components/ha-selector/ha-selector.ts`](https://github.com/home-assistant/frontend/blob/dev/src/components/ha-selector/ha-selector.ts)。选择器类型在 [`src/data/selector.ts`](https://github.com/home-assistant/frontend/blob/dev/src/data/selector.ts) 中，每种类型在 [`src/components/ha-selector/`](https://github.com/home-assistant/frontend/tree/dev/src/components/ha-selector) 中都有其组件。
