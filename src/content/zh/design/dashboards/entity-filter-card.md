---
title: 实体筛选卡
description: 实体筛选卡片只显示与筛选条件匹配的列表中的实体，例如已开启的灯。它默认包裹另一个卡片，即实体卡片。
sidebarGroup: 实体卡
sidebarGroup: 实体卡片

---

# 实体筛选卡 {#entity-filter-card}

仪表板卡片的实时演示，来自Home Assistant 演示的嵌入，连接到本网站的示例首页。

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](https://contributors.home-assistant.io/design/dashboards/entity-filter-card/)。

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
        "type": "entity-filter",
        "entities": [
          "light.living_room_lamp",
          "light.hallway",
          "light.kitchen_ceiling"
        ],
        "conditions": [
          {
            "condition": "state",
            "state": "on"
          }
        ],
        "card": {
          "title": "Lights on"
        }
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

## 使用方法 {#usage}

实体过滤卡接收一个实体列表，并且只显示符合其过滤条件的实体。当状态发生变化时，列表也会随之变化。可用于答案会变化的问题：哪些灯亮着，哪些门开着，哪些房间没水了。

它本身并不显示任何内容。它将匹配的实体传递给另一张卡片，即 [实体卡](/design/dashboards/entities-card)，除非你选择了另一张卡片，比如 [概览卡](/design/dashboards/glance-card)。你放入 `card` 的任何内容都会传递到那张卡片中，比如 `title`。

仪表板卡的实时演示，来自 Home Assistant 演示的嵌入，连接到本网站的示例家庭。

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
        "type": "entity-filter",
        "entities": [
          "sensor.living_room_humidity",
          "sensor.outdoor_humidity",
          "sensor.monstera_moisture"
        ],
        "conditions": [
          {
            "condition": "numeric_state",
            "below": 50
          }
        ],
        "card": {
          "type": "glance",
          "title": "Running dry"
        }
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

要根据状态显示或隐藏整张卡片，请使用 [条件卡](/design/dashboards/conditional-card)，或在 sections 视图中使用卡片本身的可见性选项。

### 条件 {#conditions}

列表中的每个实体都会根据 `conditions` 进行检查，并在所有条件都满足时显示。条件与卡片的可见性条件相同，只是没有实体：卡片会为每个实体填充这些条件。`state` 条件检查状态，`numeric_state` 条件使用 `above` 和 `below` 检查数字。

每个实体可以有自己的 `conditions`，它会替代卡片中该实体的条件。

旧的 `state_filter` 选项仍然有效：状态列表，或者带有 `operator`、`value` 和可选 `attribute` 的映射列表。实体在匹配任何一个时会显示。卡片不能同时拥有 `conditions` 和 `state_filter`。

### 当没有匹配项时 {#when-nothing-matches}

当没有实体匹配时，卡片会显示没有行的包装卡片。设置 `show_empty: false` 可隐藏卡片。这通常是你想要的：一个“灯已开”卡，如果没有内容，会增加干扰。

### 内容 {#content}

- 给封装的卡片一个标题，说明筛选器的含义，例如“打开的窗口”。如果没有标题，人们只能看到一个列表，并且必须猜测这些实体为什么会在其中。
- 列出可能匹配的每个实体。卡片只是筛选；它不会为你查找实体。

## 配置 {#configuration}

- `entities`（列表，必填）：要过滤的实体。每个都是一个实体 ID，或者是一个包含 `entity`、其自己的 `conditions` 或 `state_filter` 以及该实体的卡片选项的映射，例如 `name`。
- `conditions`（列表）：实体必须满足的条件才能显示。必填，除非您使用 `state_filter` 。
- `state_filter`（列表）：较旧的过滤方式，基于状态或属性值。
- `card`（映射）：显示匹配实体的卡片。默认是实体卡片。
- `show_empty`（布尔值）：当没有实体匹配时显示该卡片。默认值是 `true` 。

```yaml
type: entity-filter
show_empty: false
entities:
  - light.living_room_lamp
  - light.hallway
  - light.kitchen_ceiling
conditions:
  - condition: state
    state: "on"
card:
  title: "Lights on"
```

## 在代码中 {#in-code}

卡片位于 [`src/panels/lovelace/cards/hui-entity-filter-card.ts`](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-entity-filter-card.ts)，元素是 `<hui-entity-filter-card>`。它用包裹的卡片渲染一个 `<hui-card>`，并在匹配的实体发生变化时给它一个新的 `entities` 列表。条件通过 `checkConditionsMet` 检查，旧状态通过 `evaluateStateFilter` 在 [`src/panels/lovelace/common/evaluate-filter.ts`](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/common/evaluate-filter.ts) 中过滤。

当卡片因为没有匹配项而隐藏自身时，它会触发 `card-visibility-changed`，这样该部分就可以关闭间隙。

[来源](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-entity-filter-card.ts)
