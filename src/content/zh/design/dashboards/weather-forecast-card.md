---
title: 人种 .
description: 天气预报卡显示天气实体提供的当前天气和未来几天或几小时的预报。
sidebarGroup: 信息
---

# 人种 . {#weather-forecast-card}

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
        "type": "weather-forecast",
        "entity": "weather.home",
        "forecast_type": "daily"
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

## 使用量 {#usage}

天气预报卡显示一个天气实体. 顶部有当前条件,有图标,温度,还有一个值,如今天的最高和最低温度. 下部有预报:每日或每小时一列,并有图标和温度.

用一次在仪表盘上 人们在那里寻找天气  你到底想说什么? 光是室外温度,天气实体或温度传感器的[平板卡](/design/dashboards/tile-card) 占用的空间就更少了。 对于最后一天的温度,请使用[算法的算法是,](/design/dashboards/history-graph-card).

### 每日或小时 {#daily-or-hourly}

预测卡片的设定 : `daily`, `hourly` 或 `twice_daily` (日夜) 。 哪些取决于天气服务。 卡片编辑器只提供实体支持的类型.

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
        "type": "weather-forecast",
        "entity": "weather.home",
        "forecast_type": "hourly"
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

`forecast_slots`设定卡片显示的天数或小时,默认为5天.

### 目前天气或仅预报 {#current-weather-or-forecast-only}

`show_current: false` 离开当前天气, `show_forecast: false` 离开预测。 两者之一的牌比较短. 只使用已显示当前温度的卡片旁边的预测版本 。

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
        "type": "weather-forecast",
        "entity": "weather.home",
        "forecast_type": "daily",
        "show_current": false
      }
    </script>
  </ha-embed-card>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "weather-forecast",
        "entity": "weather.home",
        "show_forecast": false
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

### 窄牌 {#narrow-cards}

该卡适应其宽度. 随着越来越窄,当前天气得到一个较小的图标和较小的类型,在最窄的大小上,名称和附加值消失. 当卡片短时,预报也会变得紧凑. 因此卡片在半节工作,但以全宽显示较多.

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
  <ha-embed-card style="grid-column: span 6">
    <script type="application/json">
      {
        "type": "weather-forecast",
        "entity": "weather.home",
        "forecast_type": "daily",
        "forecast_slots": 3,
        "grid_options": {
          "columns": 6
        }
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

### 内容 {#content}

- 名称默认为天气实体名称,常为家名. 仅在显示多个位置时更改 。
- `secondary_info_attribute` 设置温度下的值, 如 `humidity` 或 `wind_speed` 。 默认情况下,它是当日最高和最低的气温,或降水量,或湿度,以实体有的为准.
- `round_temperature: true` 将小数点降低。 大多数预测都不够精确

## 配置 {#configuration}

- `entity`(字符串,需要):要显示的天气实体.
- `name` (字符串):要显示的名称. 默认实体名称。
- `forecast_type`(字符串):`daily`,`hourly`,或`twice_daily`。
- `show_current` (boolean): 显示当前天气. 默认为 `true` 。
- `show_forecast`(boolean):显示预测。 默认为 `true` 。
- `forecast_slots`(数目):预测显示的天数或小时。 默认为 `5` 。
- `secondary_info_attribute` (字符串):在温度下显示的属性.
- `round_temperature`(boolean):轮温到整数。 默认为 `false` 。
- `theme`(字符串):仅此牌的主题.
- `tap_action`,`hold_action`,`double_tap_action`(动作):选择,持有,或双拍卡时会发生什么. 默认情况下选择它打开更多信息对话框 。

```yaml
type: weather-forecast
entity: weather.home
forecast_type: hourly
show_current: false
```

## 在代码中 {#in-code}

牌居于[`src/panels/lovelace/cards/hui-weather-forecast-card.ts`](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-weather-forecast-card.ts),元素为`<hui-weather-forecast-card>`. 它与 `weather/subscribe_forecast` 订阅预测 WebSocket命令,所以预测更新 自己。 天气的帮助者,如图标和属性格式化,活在[`src/data/weather.ts`](https://github.com/home-assistant/frontend/blob/dev/src/data/weather.ts)中.

A `ResizeController` 度量卡, 并添加类, 如 `narrow`, `very-narrow` 和 `short` 。 风格使用这些类,而不是媒体查询,因为一张牌的宽度与屏幕的宽度无关.

在片段视图中,卡片会带一节的全宽. 它的高度取决于它所显示的内容:一行,外加当前天气的一行,外加预报的一行,外加每日预报的一行.

[来源](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-weather-forecast-card.ts)
