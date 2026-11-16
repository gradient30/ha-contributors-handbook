---
title: 历史图表卡
description: 历史图表卡显示一个或多个实体在过去几小时的状态如何变化，以折线图显示数值，以时间轴显示其他所有内容。
sidebarGroup: 信息
---

# 历史图表卡 {#history-graph-card}

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
        "type": "history-graph",
        "entities": [
          "sensor.living_room_temperature",
          "sensor.outdoor_temperature"
        ]
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

## 使用量 {#usage}

历史图表卡解题"发生了什么事?". 它显示一个时期内的实体状态,默认为24小时. 与[sensor card](/design/dashboards/sensor-card)的小图不同的是,它有轴,一个传说,以及一个随时都有精确值的工具提示.

用它来比较实体,比如内外的温度,或者看发生什么的时候,比如前门打开的时候. 对于只有趋势才重要的单一数字,[sensor card](/design/dashboards/sensor-card)占用空间较少. 在很长一段时间里,就像一个月或一年,统计图表卡更适合:它从小时长期统计而不是每一个州来工作.

### 线路图和时间表 {#line-charts-and-timelines}

纸卡的绘制方式取决于一个实体的状态,其名称和名称取决于其名称。

- 具有数态和单位的实体,如温度,会得到一个行图. 共享一个单位的实体共享一个图表,所以属于一起的值坐落在同一个轴上. 气候、加湿剂和水热器实体也获得带有其电流和目标值的线路图。
- 其他一切,如门,灯,锁,都得到了一个时间线:每个实体一个条,按州色.

当混合两种时,卡片会显示时间线和下方的行图. 有效,但牌会飞快 将人们比较的实体放入一张牌中,然后将其余的牌分给更多的牌.

有了 `split_device_classes: true` , 线条图表也会按照设备类来划分, 因此一个温度和一个共享单元的露点会得到一个图表 。

### 时间范围 {#time-range}

设定卡片后退多远. 大值使卡慢化,特别是对于经常变化的实体. 当范围比历史Home Assistant所保持的时间长时,卡片会用长期统计填充较老的部分,这些统计为小时平均.

### 轴 {#axes}

默认情况下,垂直轴跟随数值. 设定 `min_y_axis` 和 `max_y_axis` 的固定比例尺, 如 0 到 100 的百分数, 所以小的变化看起来并不戏剧化 。 `fit_y_data` 当数据需要时, 让轴向这些界限以外扩展 。 `logarithmic_scale` 当值覆盖的范围非常广泛时会有所帮助 。

### 内容 {#content}

- 当卡片有多个实体时,给予其`title`. 标题链接到同一实体的历史面板。
- 名称默认为设备和实体,如**Thermostat** ** **Living room 温度**. 当上下文清晰时给一个实体一个较短的 `name` 。
- 仅在默认颜色很难区分时,或当一个颜色带有意义时,每个实体设置 `color` 。

## 配置 {#configuration}

- `entities`(列表,需要):要显示的实体. 每一个都是实体ID,或带有`entity`的映射,可选的`name`和`color`.
- `hours_to_show`(数字):卡片显示的小时数. 默认为 `24` 。
- `title`(字符串):卡片的标题.
- `show_names` (boolean): 显示实体的名称 。 默认为 `true` 。
- `logarithmic_scale` (boolean):使用对数垂直轴. 默认为 `false` 。
- `min_y_axis`(数字):垂直 没线轴的下限。
- `max_y_axis`(数字):垂直轴的上方。
- `fit_y_data` (boolean):让轴线超越界限生长以适应数据. 默认为 `false` 。
- {(Boogle) ):(Boogle) ):(Boogle)  split(Boogle)  split(Boogle)  split(Boogle)  split(Boogle)  split(Boogle)  split(Boogle)  split(Boogle)  split(Boogle)  split(Boogle)  split(Boogle)  split(Boogle)  split(Boogle)  split(Boogle)  (Baget)   (Baget) s(Bag)   (Bag)  (Bag)   (Bag)  (Bag)  (Bag)  (Bag)  (Bag s(Bag) s(Bag)  (Bag)  (Bag)  split(Bag)  (Bag) )  split(Bag ) 默认为 `false` 。
- `expand_legend`(boolean):从头显示传说的所有项目. 默认为 `false` 。

```yaml
type: history-graph
title: "Temperature"
hours_to_show: 12
entities:
  - entity: sensor.living_room_temperature
    name: "Inside"
  - entity: sensor.outdoor_temperature
    name: "Outside"
```

## 在代码中 {#in-code}

牌居于[`src/panels/lovelace/cards/hui-history-graph-card.ts`](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-history-graph-card.ts),元素为`<hui-history-graph-card>`. 它订阅其实体的历史,增加记录历史以外的部分的长期统计,并将结果传递到`<state-history-charts>`在[`src/components/chart/`](https://github.com/home-assistant/frontend/tree/dev/src/components/chart)中. 这个组件与历史面板共享,所以卡片和面板看起来是一样的.

在区段视图中,卡片会带一个区段的全宽,并可缩小到一半. 它的高度跟随内容,除非网格选项设置了一些行.

[来源](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-history-graph-card.ts)
