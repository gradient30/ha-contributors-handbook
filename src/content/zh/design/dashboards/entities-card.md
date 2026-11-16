---
title: 实体卡
description: 实体卡显示实体列表，每行一个，每个实体都有适合它的控件。这是在一张卡中显示多个实体的紧凑方式。
sidebarGroup: 实体卡
---

# 实体卡 {#entities-card}

仪表板卡片的实时演示，来自Home Assistant演示的嵌入，连接到本站的示例首页。

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](https://contributors.home-assistant.io/design/dashboards/entities-card/)。

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
        "type": "entities",
        "title": "Living room",
        "entities": [
          "light.living_room_lamp",
          "media_player.living_room_speaker",
          "climate.thermostat",
          "sensor.living_room_temperature",
          "sensor.living_room_humidity"
        ]
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

## 用法 {#usage}

实体卡是一个列表。每个实体都有一行，显示其图标、名称，以及在右侧显示其状态或适合该域的控件：灯光的开关、输入数字的滑块、下拉选择器、锁或窗帘的按钮。点击名称或图标可以打开更多信息对话框。

当你想在有限空间内显示许多实体时，可以使用它，例如设备的设置或例程的所有辅助实体。对于人们经常使用的少数实体，[瓦片卡片](/design/dashboards/tile-card)更易于阅读和操作。对于没有控件的一行状态，使用[概览卡片](/design/dashboards/glance-card)即可。

### 适合该实体的行 {#rows-that-fit-the-entity}

行由实体的域选择。您无需配置；实体卡会为您完成。

仪表板卡的实时演示，来自 Home Assistant 演示的嵌入，连接到本网站的示例主页。

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
        "type": "entities",
        "entities": [
          "input_boolean.guest_mode",
          "input_number.comfort_temperature",
          "input_select.house_mode",
          "lock.front_door",
          "cover.bedroom_blinds",
          "scene.movie_night",
          "timer.laundry"
        ]
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

### 标题和标题切换 {#title-and-header-toggle}

使用 `title`，卡片会有一个标题。当卡片至少有两个可以切换的实体时，标题会获得一个切换按钮，可以一次切换它们全部。对于不适合使用该切换的情况（例如混合了灯和锁的列表），请设置 `show_header_toggle: false`。

仪表板卡片的实时演示，来自 Home Assistant 演示的嵌入，连接到本站的示例家居。

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
        "type": "entities",
        "title": "Lights",
        "entities": [
          "light.living_room_lamp",
          "light.hallway",
          "light.kitchen_ceiling"
        ]
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

### 特殊行 {#special-rows}

并非每一行都是一个实体。特殊行包含 `type` 并用于组织列表，或添加非实体内容：

- `divider`：组间的分隔线。
- `section`：带标签的行，用于开始一个新组。
- `attribute`：作为独立行的实体属性。
- `weblink`：页面链接。
- `buttons`：每个实体对应一个小按钮的行。
- `text`：带固定文本的名称。
- `button`：带有可执行操作按钮的一行。
- `conditional`：仅在满足条件时显示的一行。
- `cast`：开始将仪表板投射到 Google Cast 设备。

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
        "type": "entities",
        "title": "Hallway",
        "show_header_toggle": false,
        "entities": [
          "light.hallway",
          "lock.front_door",
          {
            "type": "divider"
          },
          {
            "type": "attribute",
            "entity": "lock.front_door",
            "attribute": "changed_by",
            "name": "Last locked by"
          },
          {
            "type": "section",
            "label": "Sensors"
          },
          "binary_sensor.front_door",
          "binary_sensor.hallway_motion",
          {
            "type": "weblink",
            "name": "Smart lock manual",
            "url": "https://www.home-assistant.io/integrations/nuki/"
          }
        ]
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

请谨慎使用分隔线和分区。如果列表需要很多分区，那可能应该使用多个卡片。

### 页眉和页脚 {#header-and-footer}

卡片可以有页眉和页脚。`graph` 显示一个实体的历史，`buttons` 显示一排按钮，`picture` 显示一张图片。图表页脚将读数列表转换为小概览。

仪表板卡片的实时演示，来自 Home Assistant 演示的嵌入，连接到本网站的示例主页。

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
        "type": "entities",
        "title": "Office",
        "entities": [
          "switch.desk_plug",
          "sensor.desk_plug_power",
          "sensor.desk_plug_energy"
        ],
        "footer": {
          "type": "graph",
          "entity": "sensor.desk_plug_power",
          "hours_to_show": 12
        }
      }
    </script>
  </ha-embed-card>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "entities",
        "entities": [
          "input_select.house_mode",
          "input_boolean.guest_mode"
        ],
        "header": {
          "type": "buttons",
          "entities": [
            "scene.movie_night",
            "scene.good_night"
          ]
        }
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

### 行选项 {#row-options}

一行可以覆盖其实体的名称和图标，并在名称下显示 `secondary_info`，比如最后一次更改的时间或一个属性。使用 `color: none` 时，一行的图标不再跟随状态。

仪表板卡片的实时演示，来自 Home Assistant 演示的嵌入，连接到本网站的示例主页。

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
        "type": "entities",
        "entities": [
          {
            "entity": "light.living_room_lamp",
            "secondary_info": "brightness"
          },
          {
            "entity": "binary_sensor.front_door",
            "secondary_info": "last_changed"
          },
          {
            "entity": "sensor.living_room_temperature",
            "name": "Temperature",
            "icon": "mdi:sofa"
          }
        ]
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

### 内容 {#content}

- 将属于同一组的行分组。混合房间和设备的列表很难浏览。
- 保持名称简短。右侧的控件占用房间空间，过长的名称会被截断。
- 让卡片选择行。仅在需要特殊行时才覆盖类型。

## 配置 {#configuration}

- `entities`（列表，必填）：行。每行可以是一个实体 ID，或者包含 `entity` 和选项的映射，或者带有 `type` 的特殊行。
- `title`（字符串）：卡片头部的标题。
- `icon`（字符串）：标题前的图标。
- `show_header_toggle`（布尔值）：显示头部中所有实体的切换按钮。默认情况下，当卡片有标题且至少有两个可切换实体时显示。
- `color`（字符串）：行图标的颜色方式。默认是 `state`，即状态的颜色。使用 `none` 表示默认图标颜色。
- `header`（映射）：类型为 `graph`、`buttons` 或 `picture` 的头部。
- `footer`（映射）：类型为 `graph`、`buttons` 或 `picture` 的页脚。
- `theme`（字符串）：此卡片使用的主题。

实体行的选项：- `entity`（字符串，必填）：行的实体。
- `name`（字符串）：显示的名称。默认为实体的名称。
- `icon`（字符串）：显示的图标。默认为实体的图标。
- `image`（字符串）：用一张图片代替图标显示。
- `secondary_info`（字符串或列表）：名称下方的额外信息。它的取值与[tile 卡片](/design/dashboards/tile-card)的 `state_content` 相同：`state`、`last_changed`、`last_updated`、`area_name`，或者一个属性的名称。旧的取值，如 `last-changed` 和 `position`，仍然可用。
- `color`（字符串）：图标的颜色。会覆盖卡片的颜色。
- `tap_action`、`hold_action`、`double_tap_action`（操作）：选择、长按或双击行时的行为。不是每种行类型都支持这些操作。

```yaml
type: entities
title: "Hallway"
show_header_toggle: false
entities:
  - light.hallway
  - lock.front_door
  - type: section
    label: "Sensors"
  - binary_sensor.front_door
  - entity: binary_sensor.hallway_motion
    secondary_info: last_changed
footer:
  type: graph
  entity: sensor.hallway_illuminance
```

## 在代码中 {#in-code}

卡片位于 [`src/panels/lovelace/cards/hui-entities-card.ts`](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-entities-card.ts)，元素是 `<hui-entities-card>`。行由 [`src/panels/lovelace/create-element/create-row-element.ts`](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/create-element/create-row-element.ts) 中的 `createRowElement` 创建，它将每个域映射到一行。实体行位于 [`src/panels/lovelace/entity-rows/`](https://github.com/home-assistant/frontend/tree/dev/src/panels/lovelace/entity-rows)，特殊行位于 [`src/panels/lovelace/special-rows/`](https://github.com/home-assistant/frontend/tree/dev/src/panels/lovelace/special-rows)，页眉和页脚位于 [`src/panels/lovelace/header-footer/`](https://github.com/home-assistant/frontend/tree/dev/src/panels/lovelace/header-footer)。

实体行共享 `<hui-generic-entity-row>`，它渲染图标、名称和次要信息，并将右侧留给该行。新的实体行从那里开始。

在分区视图中，卡片占据所有 12 列，并随其行增长。它可以缩小到 3 列。

[来源](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-entities-card.ts)
