---
title: 纸牌
description: 平板卡显示一个实体,并带有其图标,名称,状态,并可以为其添加控件. 它几乎是一切的默认牌。
sidebarGroup: 实体卡
sidebarGroup: 实体卡片

---

# 纸牌 {#tile-card}

盘 联卡的现场演示,从Home Assistant演示的嵌入,连接到这个站点的样本主场.

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
        "type": "tile",
        "entity": "light.living_room_lamp",
        "features": [
          {
            "type": "light-brightness"
          }
        ]
      }
    </script>
  </ha-embed-card>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "tile",
        "entity": "climate.thermostat"
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

## 使用量 {#usage}

瓦片卡是你开始的地方。 它显示了一个实体:一个图标,一个名字,以及状态. 选择此卡会打开实体的更多信息对话框 。 选择图标对于该实体来说是最明显的一件事:它切换一个灯光,一个开关,或者一个扇子,它激活一个场景或者按下一个按钮. 对于没有快速动作的实体,像传感器一样,图标什么都不做.

当 Home Assistant 为您构建一个仪表板时, 当您在一节中添加一个实体时, 它就变成了一个瓦片卡 。 仅在兀术不能完成工作时再选一张牌,如随着时间推移与[算法的算法是,](/design/dashboards/history-graph-card)的图,或用[自动调温卡](/design/dashboards/thermostat-card)的大控制.

瓦片卡跟随实体状态. 图标及其背景采用状态的颜色,如琥珀为亮光,或光本身的颜色. 当实体关闭或无法使用时,卡片为灰色.

### 特征 {#features}

特征在瓦片中添加了控件:亮度滑动器,打开并关闭封面的按钮,目标温度,一组模式. 一个特性只为支持它的实体出现. 添加人们使用最多的特征,而不是实体拥有的每个特征. 大部分瓷砖都有一两块

盘 联卡的现场演示,从Home Assistant演示的嵌入,连接到这个站点的样本主场.

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
        "type": "tile",
        "entity": "cover.bedroom_blinds",
        "features": [
          {
            "type": "cover-open-close"
          },
          {
            "type": "cover-position"
          }
        ]
      }
    </script>
  </ha-embed-card>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "tile",
        "entity": "climate.thermostat",
        "features": [
          {
            "type": "target-temperature"
          }
        ]
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

相同的特性在 [区域卡](/design/dashboards/area-card) , [自动调温卡](/design/dashboards/thermostat-card) 和 [增湿卡](/design/dashboards/humidifier-card) 中工作 。 一个特性是一次构建的,每个支持特性的卡片都可以使用.

### 内含特性 {#features-inline}

与 `features_position: inline` , 特性坐落在名字旁边, 而不是下面 。 瓦片保持单行的高度,但需要一节若全宽. 它以一个单一的,紧凑的特征,像滑轮一样,效果最好.

盘 联卡的现场演示,从Home Assistant演示的嵌入,连接到这个站点的样本主场.

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
        "type": "tile",
        "entity": "fan.bedroom_fan",
        "features": [
          {
            "type": "fan-speed"
          }
        ],
        "features_position": "inline"
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

### 垂直 {#vertical}

与`vertical: true`,图标坐于名称和状态之上. 垂直的瓦片可以缩小,降至四分之一的区段. 用它来做一排小瓷砖 人们大多会把它切掉

盘 联卡的现场演示,从Home Assistant演示的嵌入,连接到这个站点的样本主场.

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
  <ha-embed-card style="grid-column: span 3">
    <script type="application/json">
      {
        "type": "tile",
        "entity": "light.living_room_lamp",
        "vertical": true,
        "grid_options": {
          "columns": 3
        }
      }
    </script>
  </ha-embed-card>
  <ha-embed-card style="grid-column: span 3">
    <script type="application/json">
      {
        "type": "tile",
        "entity": "light.hallway",
        "vertical": true,
        "grid_options": {
          "columns": 3
        }
      }
    </script>
  </ha-embed-card>
  <ha-embed-card style="grid-column: span 3">
    <script type="application/json">
      {
        "type": "tile",
        "entity": "light.kitchen_ceiling",
        "vertical": true,
        "grid_options": {
          "columns": 3
        }
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

### 国家内容 {#state-content}

默认情况下,瓦片会显示实体的状态. 在 `state_content` 绽放时, 您选择它显示的内容, 如属性, 或上次更改后的时间 。 列表显示多个, 以点分隔 。 使用 `hide_state` 只显示名称 。

盘 联卡的现场演示,从Home Assistant演示的嵌入,连接到这个站点的样本主场.

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
        "type": "tile",
        "entity": "climate.thermostat",
        "state_content": [
          "state",
          "current_temperature"
        ]
      }
    </script>
  </ha-embed-card>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "tile",
        "entity": "lock.front_door",
        "hide_state": true
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

### 内容 {#content}

- 保持名字的简短。 瓦片狭小,长名会断. 顽强设备的名称往往足够,因为区域已经给出了上下文.
- 仅在图标添加意义时魅影或颜色被覆盖 。 默认的图标和颜色魅影随州,人们学习读取.
- 瓦片是一个实体。 对于一组实体,每个实体使用一块瓦,或[实体卡](/design/dashboards/entities-card)。

## 配置 {#configuration}

- `entity`(字符串,需要):要显示的实体.
- `name` (字符串):要显示的名称. 默认实体名称。
- `icon` (字符串):要显示的图标. 默认为实体的图标,其状态可以改变.
- `color` (字符串):实体活动时图标的颜色,如`amber`或`primary`. 默认为`state`, 状态的颜色 。
- `show_entity_picture`(boolean):显示实体的图片,比如媒体播放的封面,而不是图标. 默认为 `false` 。
- `vertical` (boole) : 将图标置于此名称之上。 默认为 `false` 。
- `hide_state`(boolean):隐藏状态. 默认为 `false` 。
- `state_content`(字符串或列表):要显示什么为状态 `state`,`last_changed`,`last_updated`,或属性名称.
- {图表H0}(动作):选择牌时会发生什么. 默认缔结一项 `more-info` 。
- `icon_tap_action`(动作):选择图标时会发生什么. 可切换的实体默认为 `toggle`, 其余为 `none` 。
- `hold_action`, `double_tap_action`, `icon_hold_action`, `icon_double_tap_action`(动作): 暂停或双拍时会发生什么 。 默认为 `none` 。
- {H0 这就是我要显示的特性,每个都有一个`type`。
- `features_position` (字符串):`bottom`或`inline`。默认为`bottom`。

```yaml
type: tile
entity: cover.bedroom_blinds
features:
  - type: cover-open-close
  - type: cover-position
```

## 在代码中 {#in-code}

牌居于[`src/panels/lovelace/cards/hui-tile-card.ts`](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-tile-card.ts),元素为`<hui-tile-card>`. 瓷砖本身是从`<ha-tile-container>`,`<ha-tile-icon>`和`<ha-tile-info>`中共享的组件在[`src/components/tile/`](https://github.com/home-assistant/frontend/tree/dev/src/components/tile)中构建的. 特征活在[`src/panels/lovelace/card-features/`](https://github.com/home-assistant/frontend/tree/dev/src/panels/lovelace/card-features)中,每个特征类型有一个元素.

在部分视图中,瓦片取十二列中的六根,一行. 每行特征都增加了一行. 内置特性需要全部12列,垂直的瓦片会增加一行,并可以缩到3列.

[来源](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-tile-card.ts)
