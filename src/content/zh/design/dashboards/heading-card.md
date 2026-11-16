---
title: 标题卡
description: 标题卡在一组卡片上方放置标题，并可选择显示该组的状态徽章。
sidebarGroup: 分组与布局
---

# 标题卡 {#heading-card}

仪表板卡片的实时演示，从Home Assistant演示的嵌入中连接到本站的示例首页。

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](https://contributors.home-assistant.io/design/dashboards/heading-card/)。

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
        "type": "heading",
        "heading": "Living room",
        "icon": "mdi:sofa",
        "badges": [
          {
            "type": "entity",
            "entity": "sensor.living_room_temperature"
          },
          {
            "type": "entity",
            "entity": "sensor.living_room_humidity"
          }
        ]
      }
    </script>
  </ha-embed-card>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "tile",
        "entity": "light.living_room_lamp"
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

## 使用方法 {#usage}

标题卡用于为一组卡片命名。在分区视图中，新分区以标题卡开始，因此大多数分区顶部都有一个标题卡。它没有背景和边框：它看起来是页面的一部分，而不是卡片。

使用标题说明下面的卡片的共同点，如房间或主题。不要将其用于已经有自己名称的单张卡片。

### 标题和副标题 {#title-and-subtitle}

`title` 样式是默认样式，用于章节顶部。`subtitle` 样式较小且颜色较浅，用于章节内的分组。使用副标题可以分割长章节，比如同一房间的灯光和气候。

仪表盘卡片的实时演示，来自 Home Assistant 演示的嵌入，连接到本站的示例家居。

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
        "type": "heading",
        "heading": "Bedroom"
      }
    </script>
  </ha-embed-card>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "heading",
        "heading": "Climate",
        "heading_style": "subtitle"
      }
    </script>
  </ha-embed-card>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "tile",
        "entity": "climate.bedroom_air_conditioner"
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

### 徽章 {#badges}

徽章位于标题的另一侧，可以一目了然地总结该组内容，就像房间的温度或门是否开启一样。实体徽章显示实体的图标和状态。选中时不会执行任何操作，除非你为其设置了一个动作。按钮徽章显示图标或简短文本，并执行一个动作。

保持徽章数量在几个以内。当徽章数量过多时，它们会横向滚动，而视图外的徽章很容易被忽略。

仪表板卡的实时演示，来自Home Assistant演示的嵌入，连接到本站的示例家庭。

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
        "type": "heading",
        "heading": "Hallway",
        "heading_style": "subtitle",
        "badges": [
          {
            "type": "entity",
            "entity": "binary_sensor.front_door"
          },
          {
            "type": "entity",
            "entity": "lock.front_door"
          },
          {
            "type": "entity",
            "entity": "light.hallway",
            "show_state": false
          }
        ]
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

### 操作 {#action}

默认情况下，选中标题时不会执行任何操作。给它一个`tap_action`，就像导航到房间的仪表板一样，标题旁会出现一个箭头，表示它可以跳转到某个地方。

仪表板卡片的实时演示，来自Home Assistant演示的嵌入，连接到本网站的示例主页。

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
        "type": "heading",
        "heading": "Garden",
        "icon": "mdi:flower",
        "tap_action": {
          "action": "navigate",
          "navigation_path": "/dashboard-garden"
        }
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

### 内容 {#content}

- 保持标题一到两个词即可。只需说明区域或主题。
- 图标是可选的。当它有助于人们在滚动时找到某个部分时使用，并在视图的每个标题上使用，或者都不使用。
- 徽章显示状态，它们不是第二行控件。对于控件，请在标题下使用 [tile cards](/design/dashboards/tile-card)。

## 配置 {#configuration}

- `heading`（字符串）：标题的文本。
- `heading_style`（字符串）：`title` 或 `subtitle`。默认为 `title`。
- `icon`（字符串）：标题前的图标。
- `tap_action`、`hold_action`、`double_tap_action`（操作）：选择标题时会发生的操作。默认值为 `none`。
- `badges`（列表）：要显示的徽章。每个徽章都有一个 `type`：`entity`（默认）或 `button`。

一个实体徽章包含：- `entity`（字符串，必填）：要显示的实体。
- `name`（字符串）：实体的名称，用于徽章的工具提示。
- `icon`（字符串）：图标。默认为实体的图标。
- `color`（字符串）：图标的颜色。使用 `state` 表示状态的颜色。如果不设置，图标没有颜色。
- `show_state`（布尔值）：是否显示状态。默认为 `true`。
- `show_icon`（布尔值）：是否显示图标。默认为 `true`。
- `state_content`（字符串或列表）：作为状态显示的内容，如某个属性。
- `tap_action`、`hold_action`、`double_tap_action`（操作）：选择徽章时发生的操作。默认为 `none`。

按钮徽章接受 `text`、`icon`、`color` 以及相同的操作。

```yaml
type: heading
heading: "Living room"
icon: mdi:sofa
badges:
  - entity: sensor.living_room_temperature
  - entity: sensor.living_room_humidity
```

## 在代码中 {#in-code}

卡片位于 [`src/panels/lovelace/cards/hui-heading-card.ts`](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-heading-card.ts)，元素为 `<hui-heading-card>`。徽章是 `<hui-heading-badge>` 元素，它们为每种类型创建徽章，来源于 [`src/panels/lovelace/heading-badges/`](https://github.com/home-assistant/frontend/tree/dev/src/panels/lovelace/heading-badges)。

在分区视图中，标题总是占据分区的整个宽度，其高度随内容变化。标题和副标题样式可以使用 `--ha-heading-card-title-*` 和 `--ha-heading-card-subtitle-*` 变量进行主题设置。

[来源](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-heading-card.ts)
