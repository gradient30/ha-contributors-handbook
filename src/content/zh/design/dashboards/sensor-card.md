---
title: 传感器卡
description: 感应卡显示一个大类型的数字感应器正在努力值,下面有其近代历史的可选行图.
sidebarGroup: 信息
---

# 传感器卡 {#sensor-card}

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
        "type": "sensor",
        "entity": "sensor.living_room_temperature",
        "graph": "line"
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

## 使用量 {#usage}

感应卡的各项内容为人们想一眼看就看的一个数字,并看到以下趋势:温度,设备使用的动力,房间的湿度. 它在顶部显示名称和图标,大类型的值,以及最后24小时底部的行图.

你自己需要感应器、数字、输入数字和计数器。 你自己看,这个值必须用数字来表示

使用 [平板卡](/design/dashboards/tile-card) 当值是一节中许多值之一而趋势并不重要时。 当值在一个范围内的位置比它的历史更重要时使用 [测量卡](/design/dashboards/gauge-card) 。 使用 [算法的算法是,](/design/dashboards/history-graph-card) 来比较几个实体, 或者当人们需要轴和过去的确切值时 。

### 有无图 {#with-or-without-a-graph}

加上`graph: line`,卡片会添加图表. 没有它,卡只显示值. 这个简单的版本和[实体卡](/design/dashboards/entity-card)一样,所以如果你不想图,就用那张牌代替.

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
        "type": "sensor",
        "entity": "sensor.desk_plug_power",
        "graph": "line"
      }
    </script>
  </ha-embed-card>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "sensor",
        "entity": "sensor.outdoor_humidity"
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

图是火花线:没有轴,没有标签,没有工具提示. 它显示了趋势的形状,而不是数字. 这让卡片保持平静,它起作用了,因为当前值就在它上面。

### 时间范围和 我只是说 {#time-range-and-detail}

`hours_to_show` 设定图的后退有多远 。 短距离显示快速变化, 就像一个刚刚打开的设备的力量。 长距离显示了规律,就像一天的温度。

与 `detail: 2` 一起, 图表使用更多的点数, 并跟踪每个变化 。 默认值 `detail: 1`, 平均每小时值, 这给出了更平滑的线条 。 选择平滑线,除非高峰是点.

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
        "type": "sensor",
        "entity": "sensor.desk_plug_power",
        "graph": "line",
        "hours_to_show": 6,
        "detail": 2
      }
    </script>
  </ha-embed-card>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "sensor",
        "entity": "sensor.desk_plug_power",
        "graph": "line",
        "hours_to_show": 6
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

### 内容 {#content}

- 名字来源于实体. 保持短,卡片有半节宽.
- 别管部队了 实体提供,卡片格式为用户语言的值. 覆盖`unit`只针对一个没有自己的单位的实体.
- 设定 `limits` 仅当图形的默认缩放隐藏重要内容时, 如温度的微小变化 永不低于18 度 。

## 配置 {#configuration}

- `entity`(字符串,需要):一个传感器,号码,输入号,或计数实体.
- `name` (字符串):要显示的名称. 默认实体名称。
- `icon` (字符串):要显示的图标. 实体图标的默认值。
- `graph`(字符串):`line` 添加图,`none` 将其删除。 默认为 `none` 。
- `unit`(字符串):要显示的单位. 默认为实体的单位.
- `detail`(数字):`1`一个小时平均值,`2`更详细。 默认为 `1` 。
- `hours_to_show`(数字):图显示的小时数。 默认为 `24` 。
- `limits` (图): `min` 和 `max` 用于图的垂直比例 。 默认情况下,比例跟随数值.
- `theme`(字符串):仅此牌的主题.

```yaml
type: sensor
entity: sensor.desk_plug_power
graph: line
hours_to_show: 6
```

## 在代码中 {#in-code}

牌居于[`src/panels/lovelace/cards/hui-sensor-card.ts`](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-sensor-card.ts),元素为`<hui-sensor-card>`. 它扩展实体卡(`hui-entity-card.ts`):它将自己的选项转换成实体卡配置,并增加图作为页脚. 图是[`src/panels/lovelace/header-footer/hui-graph-header-footer.ts`](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/header-footer/hui-graph-header-footer.ts)中的图头和页脚元素,实体卡也可以作为页脚使用.

片段视图中,卡片取12列中的6列,2列. 它不能变小了。

[来源](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-sensor-card.ts)
