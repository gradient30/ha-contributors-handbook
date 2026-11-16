---
title: 网格和堆叠卡片
description: 网格卡片、水平堆叠卡片和垂直堆叠卡片可以容纳其他卡片，将它们并排或上下放置在同一张卡片中。
sidebarGroup: 分组与布局
---

# 网格和堆叠卡片 {#grid-and-stack-cards}

仪表板卡片的实时演示，来自Home Assistant 演示的嵌入，连接到本网站的示例首页。

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](https://contributors.home-assistant.io/design/dashboards/grid-card/)。

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
        "type": "grid",
        "columns": 2,
        "square": false,
        "cards": [
          {
            "type": "button",
            "entity": "light.living_room_lamp"
          },
          {
            "type": "button",
            "entity": "light.hallway"
          },
          {
            "type": "button",
            "entity": "switch.desk_plug"
          },
          {
            "type": "button",
            "entity": "lock.front_door"
          }
        ]
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

## 使用方法 {#usage}

这三张卡片本身没有内容。它们用于容纳其他卡片并进行布局：

- 网格卡将卡片按列排列，一行接一行。
- 水平堆叠卡将卡片并排放置在一行中。
- 垂直堆叠卡将卡片一个接一个地向下排列。

它们来源于砖石视图，在该视图中每张卡占据一列，视图决定其位置。堆叠是一种将卡片保持在一起的方式，比如标题下的卡片，或者两张仪表并排放置。

在分区视图中，你很少需要它们。分区本身已经是由12列组成的网格，每张卡片在其中都有自己的大小。可以直接将卡片放置在分区中，这样每张卡片都可以单独移动、调整大小和隐藏。仅在卡片必须在每种布局、每个屏幕上保持在一起时才使用堆叠。

### 网格 {#grid}

网格卡默认有三列。设置 `columns` 可以更改此数量。默认情况下，每个单元格都是正方形，这适用于像 [按钮卡](/design/dashboards/button-card) 这样的小卡片。设置 `square: false` 可以让每行的高度根据其最高的卡片来调整。

仪表板卡片的实时演示，来自 Home Assistant 演示的嵌入，连接到本站的示例主页。

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
        "type": "grid",
        "cards": [
          {
            "type": "button",
            "entity": "light.living_room_lamp"
          },
          {
            "type": "button",
            "entity": "light.hallway"
          },
          {
            "type": "button",
            "entity": "light.kitchen_ceiling"
          }
        ]
      }
    </script>
  </ha-embed-card>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "grid",
        "columns": 2,
        "square": false,
        "cards": [
          {
            "type": "tile",
            "entity": "binary_sensor.front_door"
          },
          {
            "type": "tile",
            "entity": "lock.front_door"
          },
          {
            "type": "tile",
            "entity": "binary_sensor.kitchen_window"
          },
          {
            "type": "tile",
            "entity": "binary_sensor.bathroom_leak"
          }
        ]
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

### 水平堆叠 {#horizontal-stack}

水平堆叠会将其宽度均分给卡片。保持在两到三张卡片。屏幕很窄时，堆叠中的每张卡片也会变窄，因为堆叠从不换行。

仪表板卡片的实时演示，来自 Home Assistant 演示的嵌入，连接到本站的示例主页。

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
        "type": "horizontal-stack",
        "cards": [
          {
            "type": "gauge",
            "entity": "sensor.living_room_humidity",
            "name": "Inside"
          },
          {
            "type": "gauge",
            "entity": "sensor.outdoor_humidity",
            "name": "Outside"
          }
        ]
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

### 垂直堆叠 {#vertical-stack}

垂直堆叠将卡片一个接一个地放置，就像一张卡片。将其与水平堆叠结合使用，可以构建自己的小布局。

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
        "type": "vertical-stack",
        "cards": [
          {
            "type": "tile",
            "entity": "media_player.living_room_speaker"
          },
          {
            "type": "horizontal-stack",
            "cards": [
              {
                "type": "tile",
                "entity": "light.living_room_lamp"
              },
              {
                "type": "tile",
                "entity": "climate.thermostat"
              }
            ]
          }
        ]
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

### 标题 {#title}

三者都可以选择性地使用 `title`，显示在卡片上方。在区块视图中，请改用 [标题卡](/design/dashboards/heading-card)，这样标题看起来与视图的其余部分一致。

### 内容 {#content}

- 堆叠中的堆叠的堆叠很难编辑和修改。如果布局需要如此，区块可能更适合。
- 网格或堆叠中的卡片保持自己的边框和背景。容器只添加它们之间的间距，不做其他处理。

## 配置 {#configuration}

三种卡片都支持：

- `cards`（列表，必填）：要显示的卡片，每个卡片都有自己的配置。
- `title`（字符串）：卡片上方的标题。

网格卡片还支持：

- `columns`（数字）：列数。默认为 `3`。
- `square`（布尔值）：使每个单元格保持正方形。默认为 `true`。

```yaml
type: grid
columns: 2
square: false
cards:
  - type: tile
    entity: binary_sensor.front_door
  - type: tile
    entity: lock.front_door
```

```yaml
type: horizontal-stack
cards:
  - type: gauge
    entity: sensor.living_room_humidity
  - type: gauge
    entity: sensor.outdoor_humidity
```

## 在代码中 {#in-code}

这些卡片位于 [`src/panels/lovelace/cards/`](https://github.com/home-assistant/frontend/tree/dev/src/panels/lovelace/cards)：`hui-grid-card.ts`、`hui-horizontal-stack-card.ts` 和 `hui-vertical-stack-card.ts`。元素为 `<hui-grid-card>`、`<hui-horizontal-stack-card>` 和 `<hui-vertical-stack-card>`。三者都继承于 `hui-stack-card.ts` 中的共享基础，这为列表中的每张卡片创建了一个 `<hui-card>` 并渲染标题。每张卡片只在此基础上添加它自己的布局样式。

堆叠的大小取决于其中的卡片：垂直堆叠会将它们的大小相加，而水平堆叠则取最大值。

[来源](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-stack-card.ts)
