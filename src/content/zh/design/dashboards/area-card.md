---
title: 区域卡
description: 该区域卡总结了家中一个区域，包括其图片、传感器和警报，并且可以为其中的所有设备添加控制。
sidebarGroup: 分组与布局
---

# 区域卡 {#area-card}

仪表板卡片实时演示，来自Home Assistant演示的嵌入，连接到本站的示例主页。

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](https://contributors.home-assistant.io/design/dashboards/area-card/)。

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
        "type": "area",
        "area": "living_room",
        "sensor_classes": [
          "temperature",
          "humidity"
        ]
      }
    </script>
  </ha-embed-card>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "area",
        "area": "living_room",
        "display_type": "compact",
        "sensor_classes": [
          "temperature",
          "humidity"
        ],
        "features": [
          {
            "type": "area-controls"
          }
        ]
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

## 使用方法 {#usage}

区域卡片可一目了然地显示一个区域：其名称和图标、传感器的读数，以及当某些事项需要关注时的警报。在概览中使用，每个区域都有一张卡片，点击即可查看该区域的详细信息。

该卡片从区域注册表中工作。它会自动查找区域中的实体，因此在添加或移动设备时会保持最新状态。对于区域中的单个实体，请使用[tile card](/design/dashboards/tile-card)。

### 显示类型 {#display-type}

`display_type` 决定了卡片占用的空间大小：

- `picture`：默认类型。区域的图片填充卡片顶部。没有图片时，区域图标会替代图片显示在纯色背景上。
- `camera`：显示区域内摄像头的实时画面，而不是图片。
- `icon`：在纯色背景上显示与图片同样大小的区域图标。
- `compact`：完全没有图片。卡片像瓷砖一样小，图标在名称前显示。

来自 Home Assistant 演示嵌入的仪表板卡片实时演示，连接到本网站的示例家居。

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
        "type": "area",
        "area": "hallway",
        "display_type": "icon"
      }
    </script>
  </ha-embed-card>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "area",
        "area": "hallway",
        "display_type": "compact"
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

当用户能通过图片识别自己的房间时（比如在墙面平板上），可以使用图片类型。当概览中有许多区域时，使用紧凑类型以便在一个屏幕上显示。紧凑卡片可以是 `vertical`，例如垂直瓷砖。此页上的演示没有区域图片，因此图片类型显示的是图标。

### 传感器与警报 {#sensors-and-alerts}

使用 `sensor_classes`，卡片显示该区域传感器的读数，按设备类别分类。当一个区域有多个相同类别的传感器时，卡片显示它们的中位数，或者显示可以相加的类别的总和，如功率或能量。气候设备也会计算在内，通过它们的当前温度。设置在区域自身的温度或湿度传感器优先于所有其他传感器。

使用 `alert_classes`，卡片为该区域内有二进制传感器的每个类别显示一个图标，例如运动、窗户开启或漏水。在较大的类型中，警报位于图片的一列中。在紧凑类型中，仅显示第一个警报，作为图标上的徽章。警报仅在发生事件时出现，因此空白位置是好消息。仪表板卡片的实时演示，来自Home Assistant演示的嵌入，连接到本站的示例主页。

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
        "type": "area",
        "area": "kitchen",
        "display_type": "compact",
        "alert_classes": [
          "window",
          "moisture"
        ]
      }
    </script>
  </ha-embed-card>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "area",
        "area": "hallway",
        "display_type": "compact",
        "sensor_classes": [
          "illuminance"
        ],
        "alert_classes": [
          "motion",
          "door"
        ]
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

没有`sensor_classes`或`alert_classes`，卡片不会显示任何读数或警报。请选择对概览重要的少数类别，比如温度和湿度，以及运动和泄漏。

### 功能 {#features}

区域卡片具有功能，就像磁贴卡片一样。`area-controls` 功能添加按钮，用于同时开启或关闭区域的灯光、风扇和遮盖物。默认情况下，它显示最多四个按钮，针对该区域的设备类型。使用 `controls` 可以选择它们。

仪表板卡片的实时演示，来自 Home Assistant 演示的嵌入，连接到本网站的示例家庭。

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
        "type": "area",
        "area": "bedroom",
        "display_type": "compact",
        "features": [
          {
            "type": "area-controls",
            "controls": [
              "fan",
              "cover-blind"
            ]
          }
        ]
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

### 内容 {#content}

- 名称和图标来自区域注册表。只有在仪表板需要与 Home Assistant 其余部分不同的词时才覆盖它们。
- 使用 `exclude_entities` 排除可能导致读数错误的实体，例如冰箱内的温度传感器。
- 默认情况下，点击卡片不会执行任何操作。为其提供一个 `tap_action` 来导航到该区域，这样卡片就可以作为入口使用。

## 配置- `area`（字符串，必填）：区域的ID。 {#configuration}
- `name`（字符串）：显示的名称。默认为区域的名称。
- `color`（字符串）：图标的颜色。
- `display_type`（字符串）：`picture`、`camera`、`icon` 或 `compact`。默认为 `picture`。
- `vertical`（布尔值）：将图标放置在名称上方。仅适用于 `compact` 类型。默认为 `false`。
- `camera_view`（字符串）：`auto` 或 `live`，用于 `camera` 类型。
- `aspect_ratio`（字符串）：图片的形状，如 `16:9`。默认为 `16:9`。
- `sensor_classes`（列表）：要显示的传感器的设备类别。
- `alert_classes`（列表）：要作为警报显示的二进制传感器的设备类别。
- `exclude_entities`（列表）：在读数、警报和控制中排除的实体。
- `features`（列表）：要显示的功能，每个功能都有一个 `type`。
- `features_position`（字符串）：`bottom` 或 `inline`。默认为 `bottom`。

- `tap_action`（动作）：选择卡片时会发生的操作。默认值为 `none`。
- `image_tap_action`（动作）：选择图片时会发生的操作。对于 `camera` 类型，它会打开相机。

```yaml
type: area
area: living_room
display_type: compact
sensor_classes:
  - temperature
  - humidity
alert_classes:
  - motion
features:
  - type: area-controls
tap_action:
  action: navigate
  navigation_path: "/dashboard-rooms/living-room"
```

## 在代码中 {#in-code}

卡片位于 [`src/panels/lovelace/cards/hui-area-card.ts`](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-area-card.ts)，元素是 `<hui-area-card>`。它由与瓷砖卡相同的瓷砖部分构建，`<ha-tile-container>`、`<ha-tile-icon>` 和 `<ha-tile-info>`，警报是瓷砖徽章。区域控制功能是 [`src/panels/lovelace/card-features/hui-area-controls-card-feature.ts`](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/card-features/hui-area-controls-card-feature.ts)。

在分区视图中，区域卡占据 12 列中的 6 列。紧凑型占一行，就像瓷砖一样。图片、相机和图标类型会为图片增加两行。功能添加行的方式与在瓷砖卡上一样。

[来源](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-area-card.ts)
