---
title: 实体卡
description: 实体卡显示一个实体的状态为一个大数值，并带有其名称和图标。它适用于你想一眼就能读取的数字。
sidebarGroup: 实体卡
sidebarGroup: 实体卡片

---

# 实体卡 {#entity-card}

仪表板卡片的实时演示，来自 Home Assistant 演示的嵌入，连接到本网站的示例主页。

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](https://contributors.home-assistant.io/design/dashboards/entity-card/)。

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
        "type": "entity",
        "entity": "sensor.outdoor_temperature"
      }
    </script>
  </ha-embed-card>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "entity",
        "entity": "sensor.desk_plug_power"
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

## 使用方法 {#usage}

实体卡片将某个实体的状态置于中心位置：顶部显示名称，角落显示图标，下方以大号字体显示数值。它最适合用于人们经常查看的读数，例如室外温度或设备当前消耗的功率。

实体卡片仅用于显示。它没有控制功能，点击它会打开详细信息对话框。若要显示用户也会操作的实体，例如灯，请使用 [tile card](/design/dashboards/tile-card)。若要显示数值随时间的变化，请使用 [sensor card](/design/dashboards/sensor-card)，它会在数值下方添加图表。

### 属性 {#attribute}

使用`attribute`，卡片显示一个属性而不是状态。当属性本身没有时，添加`unit`。自定义单元总是跟在数值之后。

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
        "type": "entity",
        "entity": "climate.thermostat",
        "attribute": "current_temperature",
        "name": "Living room",
        "unit": "°C"
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

### 状态颜色 {#state-color}

对于灯光，图标会采用状态颜色，例如灯亮时为琥珀色，或采用灯本身的颜色。对于其他实体，图标保持默认图标颜色。也可以设置 `state_color: true` 来根据状态为这些图标着色，或者设置 `state_color: false` 来关闭灯的状态颜色。

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
        "type": "entity",
        "entity": "light.living_room_lamp"
      }
    </script>
  </ha-embed-card>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "entity",
        "entity": "lock.front_door",
        "state_color": true
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

### 页脚 {#footer}

卡片可以有页脚，例如实体的图表或一排按钮。带有图表时，卡片会变为小型传感器卡，因此对于此类情况，建议使用 [传感器卡](/design/dashboards/sensor-card)。

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
        "type": "entity",
        "entity": "sensor.living_room_temperature",
        "footer": {
          "type": "graph",
          "entity": "sensor.living_room_temperature"
        }
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

### 内容 {#content}

- 用于数字和简短状态。较长的状态会被截断。
- 保持名称简短。区域或卡片上方的标题通常已经说明了数值来源，所以“温度”就足够了。

## 配置 {#configuration}

- `entity`（字符串，必填）：要显示的实体。
- `name`（字符串）：要显示的名称。默认为实体的名称。
- `icon`（字符串）：要显示的图标。默认为实体的图标。
- `attribute`（字符串）：显示此属性而非状态。
- `unit`（字符串）：值后显示的单位。默认为实体的单位。
- `state_color`（布尔值）：根据实体的状态为图标上色。默认为亮灯时为 `true`，其他情况为 `false`。
- `theme`（字符串）：用于此卡片的主题。
- `footer`（映射）：页脚，类型为 `graph`、`buttons` 或 `picture`。
- `tap_action`、`hold_action`、`double_tap_action`（操作）：当您选择、按住或双击卡片时会发生的操作。默认情况下，选择会打开详细信息对话框。

```yaml
type: entity
entity: climate.thermostat
attribute: current_temperature
name: "Living room"
unit: "°C"
```

## 在代码中 {#in-code}

该卡片位于 [`src/panels/lovelace/cards/hui-entity-card.ts`](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-entity-card.ts)，元素是 `<hui-entity-card>`。页脚由 `createHeaderFooterElement` 创建，与 [实体卡片](/design/dashboards/entities-card) 用于其页眉和页脚的相同。

在分区视图中，卡片占据 12 栏中的 6 栏和两行，并且不能小于此尺寸。

[来源](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-entity-card.ts)
