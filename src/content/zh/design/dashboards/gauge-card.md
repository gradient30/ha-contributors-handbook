---
title: 量规卡
description: 仪表卡在表盘上显示一个数值，并用颜色表示良好、值得担忧或不良的范围。
sidebarGroup: 信息
---

# 量规卡 {#gauge-card}

Home Assistant演示嵌入的仪表盘卡实时演示，连接到本网站的示例主页。

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](https://contributors.home-assistant.io/design/dashboards/gauge-card/)。

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
        "type": "gauge",
        "entity": "sensor.living_room_humidity"
      }
    </script>
  </ha-embed-card>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "gauge",
        "entity": "sensor.monstera_battery",
        "name": "Monstera sensor battery",
        "severity": {
          "red": 0,
          "yellow": 20,
          "green": 40
        }
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

## 用途 {#usage}

仪表卡显示已知范围内的一个数值，比如湿度、电池电量或服务器负载。拨盘一目了然告诉人们该值在该范围内的位置，中间的数字则准确告诉他们。

当区间位置重要时使用。对于没有自然极小和最大值的数值，比如设备消耗的功率，刻度表显示的信息很少，[传感器卡]（/design/dashboards/sensor-card/）或[磁贴卡]（/design/dashboards/tile-card/）更合适。对于时间趋势，使用[历史图卡]（/design/dashboards/history-graph-card/）。

旋钮本身就是[规范组件]（/design/components/gauge/），界面的其他部分也会用到它。

### 范围 {#range}

刻度从 `min` 到 `max`，默认是 0 到 100。这适合表示百分比。对于其他情况，请设置一个与人们预期数值相匹配的范围，例如室内温度为 10 到 30。超出范围的值仍会显示为数字，仪表盘指针保持在末端。

### 严重性 {#severity}

拨盘颜色可以显示值是好还是坏。使用 `severity`，您可以设置绿色、黄色和红色的起始位置。每种颜色的范围从其设置的值延伸到下一个颜色的起始值。如果没有设置严重性，拨盘将使用信息颜色(info color)，该颜色没有特定含义。

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
        "type": "gauge",
        "entity": "sensor.living_room_humidity",
        "severity": {
          "green": 30,
          "yellow": 60,
          "red": 70
        }
      }
    </script>
  </ha-embed-card>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "gauge",
        "entity": "sensor.outdoor_humidity",
        "severity": {
          "green": 30,
          "yellow": 60,
          "red": 70
        }
      }
    </script>
  </ha-embed-card>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "gauge",
        "entity": "sensor.monstera_moisture",
        "severity": {
          "red": 0,
          "yellow": 15,
          "green": 25
        }
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

绿色不一定要放在低端。对于电池或植物湿度，低值是坏的，所以红色应优先显示。

如果有三个以上的范围，或需要使用其他颜色，请改用 `segments`：一个范围列表，每个范围都有一个 `from` 值和一个 `color`。当两者都设置时，`segments` 优先。

### 指针 {#needle}

使用`needle: true`时，仪表盘同时显示所有范围，并且有一个指针指向数值。人们可以看到数值的位置，以及它离下一个范围有多近。可以将其与严重性或分段一起使用，如果没有这些，整个仪表盘只有一个颜色。

仪表盘卡片的实时演示，来自Home Assistant演示的嵌入，连接到本网站的示例主页。

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
        "type": "gauge",
        "entity": "sensor.living_room_humidity",
        "needle": true,
        "severity": {
          "green": 30,
          "yellow": 60,
          "red": 70
        }
      }
    </script>
  </ha-embed-card>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "gauge",
        "entity": "sensor.living_room_temperature",
        "needle": true,
        "min": 10,
        "max": 30,
        "segments": [
          {
            "from": 10,
            "color": "var(--info-color)"
          },
          {
            "from": 18,
            "color": "var(--success-color)"
          },
          {
            "from": 24,
            "color": "var(--warning-color)"
          },
          {
            "from": 27,
            "color": "var(--error-color)"
          }
        ]
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

一个分段可以有一个`label`。使用指针时，当数值在该分段内时，标签会替换中间的数字，比如**舒适**或**太热**。

### 内容 {#content}

- 选择颜色时考虑的是该数值对人们的意义，而不是它的大小。
- 在各个部分使用主题颜色，例如`var(--success-color)`。它们在亮色和暗色主题中都适用。
- 名称位于仪表下方。保持简短，因为该卡片通常会与其他卡片并排放置。

## 配置- `entity`（字符串，必填）：要显示的实体。其状态或属性必须是数字。 {#configuration}
- `attribute`（字符串）：显示实体的此属性，而不是其状态。
- `name`（字符串）：要显示的名称。默认为实体的名称。
- `unit`（字符串）：要显示的单位。默认为实体的单位。
- `min`（数字）：刻度开始值。默认为 `0`。
- `max`（数字）：刻度结束值。默认为 `100`。
- `severity`（映射）：`green`、`yellow` 和 `red` 的起始位置。
- `segments`（列表）：范围，每个范围包含 `from`、`color` 以及可选的 `label`。代替 `severity`。
- `needle`（布尔值）：在带有所有范围的仪表盘上显示指针。默认为 `false`。
- `theme`（字符串）：仅针对此卡片的主题。

- `tap_action`、`hold_action`、`double_tap_action`（操作）：当你选择、按住或双击卡片时会发生什么。默认情况下，选择它会打开更多信息对话框。

```yaml
type: gauge
entity: sensor.monstera_moisture
severity:
  red: 0
  yellow: 15
  green: 25
```

## 在代码中 {#in-code}

卡片位于 [`src/panels/lovelace/cards/hui-gauge-card.ts`](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-gauge-card.ts)，元素是 `<hui-gauge-card>`。它包装了 `<ha-gauge>`，来自 [`src/components/ha-gauge.ts`](https://github.com/home-assistant/frontend/blob/dev/src/components/ha-gauge.ts)。卡片根据严重性或分段计算拨盘的颜色，并将其作为 `--gauge-color` 传递。使用针时，它将它们作为 `levels` 传递。

该数值由 Home Assistant 格式化，方式与其他地方相同，因此可以获得正确的精度和单位。非数字值会在卡片上显示警告，而不是在拨盘上显示。

在分区视图中，卡片默认占据分区的全宽。

[源](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-gauge-card.ts)
