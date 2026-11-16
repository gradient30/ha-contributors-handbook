---
title: 一览卡
description: 一目卡显示多个实体的状态，并排展示，每个实体包括名称、图标和状态。这是一个你一眼就能看懂的概览。
sidebarGroup: 实体卡
sidebarGroup: 实体卡片

---

# 一览卡 {#glance-card}

仪表板卡片的实时演示，取自 Home Assistant 演示的嵌入，连接到本网站的示例首页。

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](https://contributors.home-assistant.io/design/dashboards/glance-card/)。

```html
<ha-embed-provider
  style="
    display: grid;
    grid-template-columns: repeat(12, minmax(0, 1fr));
    gap: 8px;
    align-items: start;
    max-width: 500px;
  "
>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "glance",
        "entities": [
          "binary_sensor.front_door",
          "lock.front_door",
          "binary_sensor.hallway_motion",
          "light.hallway"
        ]
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

## 使用方法 {#usage}

概览卡片将少量实体放在列中：顶部是名称，中间是图标，底部是状态。它可以一目了然地回答一个问题，比如“房子关闭了吗？”或“谁在家？”。

概览卡片没有控件。选择一个实体会打开其详细信息对话框，长按也会打开。当人们需要操作实体时，请使用 [瓦片卡片](/design/dashboards/tile-card) 或 [实体卡片](/design/dashboards/entities-card)。对于单个重要数值，请使用 [实体卡片](/design/dashboards/entity-card)。

### 列 {#columns}

卡片每行最多容纳五个实体，多余的实体会换到下一行。设置 `columns` 可以自行选择数量。列数较少会给较长名称留出更多空间。

仪表盘卡片的现场演示，来自 Home Assistant 演示的嵌入，连接到本站的示例主页。

```html
<ha-embed-provider
  style="
    display: grid;
    grid-template-columns: repeat(12, minmax(0, 1fr));
    gap: 8px;
    align-items: start;
    max-width: 500px;
  "
>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "glance",
        "title": "Climate",
        "columns": 3,
        "entities": [
          "sensor.living_room_temperature",
          "sensor.living_room_humidity",
          "sensor.monstera_temperature",
          "sensor.outdoor_temperature",
          "sensor.outdoor_humidity"
        ]
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

### 显示较少 {#showing-less}

使用 `show_name`、`show_icon` 和 `show_state` 来隐藏所有实体的一部分。当图标本身已经足够表达意思时（比如门和窗户），一行没有名称的图标及其状态效果很好。

仪表板卡片的实时演示，来自 Home Assistant 演示的嵌入，连接到本站的示例家庭。

```html
<ha-embed-provider
  style="
    display: grid;
    grid-template-columns: repeat(12, minmax(0, 1fr));
    gap: 8px;
    align-items: start;
    max-width: 500px;
  "
>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "glance",
        "show_name": false,
        "entities": [
          "binary_sensor.front_door",
          "binary_sensor.kitchen_window",
          "cover.garage_door",
          "lock.front_door"
        ]
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

### 最近更改 {#last-changed}

在实体上使用 `show_last_changed: true` 时，它显示状态改变的时间，而不是状态本身。可用于像门之类的事物，因为“何时”往往比“是什么”更有趣。

仪表板卡片的实时演示，来自 Home Assistant 演示的嵌入，连接到本站的示例家庭。

```html
<ha-embed-provider
  style="
    display: grid;
    grid-template-columns: repeat(12, minmax(0, 1fr));
    gap: 8px;
    align-items: start;
    max-width: 500px;
  "
>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "glance",
        "entities": [
          {
            "entity": "binary_sensor.front_door",
            "show_last_changed": true
          },
          {
            "entity": "binary_sensor.hallway_motion",
            "show_last_changed": true
          },
          "person.alex",
          "person.sam"
        ]
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

### 内容 {#content}

- 名称保持在一两个字以内。每一列都很窄，长名称会被截断。
- 将回答同一问题的实体分组。混合了电池、门和天气的卡片不是一眼就能看明白的。
- 当仅凭实体无法清楚表示问题时，使用 `title`。

## 配置 {#configuration}

- `entities` (列表，必填)：要显示的实体。每个实体可以是实体ID，或者带有 `entity` 和选项的映射。
- `title` (字符串)：卡片标题栏中的标题。
- `columns` (数字)：列数。默认为实体数量，最多为五列。
- `show_name` (布尔值)：是否显示名称。默认为 `true`。
- `show_icon` (布尔值)：是否显示图标。默认为 `true`。
- `show_state` (布尔值)：是否显示状态。默认为 `true`。
- `color` (字符串)：图标的颜色方式。默认为 `state`，即状态颜色。使用 `none` 设置默认图标颜色。
- `theme` (字符串)：此卡片使用的主题。

实体的选项：- `entity`（字符串，必填）：要显示的实体。
- `name`（字符串）：要显示的名称。默认显示实体的名称。
- `icon`（字符串）：要显示的图标。默认显示实体的图标。
- `image`（字符串）：显示的图片，替代图标。
- `show_state`（布尔值）：显示该实体的状态。默认`true`。
- `show_last_changed`（布尔值）：显示自上次更改以来的时间，而不是状态。默认`false`。
- `color`（字符串）：图标的颜色。会覆盖卡片的颜色。
- `tap_action`、`hold_action`、`double_tap_action`（操作）：选择、长按或双击实体时会发生的操作。默认选择和长按会打开更多信息对话框。

```yaml
type: glance
title: "Climate"
columns: 3
entities:
  - sensor.living_room_temperature
  - sensor.living_room_humidity
  - entity: sensor.outdoor_temperature
    name: "Outside"
```

## 在代码中 {#in-code}

该卡片位于 [`src/panels/lovelace/cards/hui-glance-card.ts`](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-glance-card.ts)，元素是 `<hui-glance-card>`。列的宽度通过 `--glance-column-width` 自定义属性设置，从 `columns` 计算得出。图标是 `<state-badge>`。

[来源](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-glance-card.ts)
