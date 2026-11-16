---
title: 自动调温卡
description: 自动调温卡显示一个气候或水热器实体作为拨号,以读取温度并设定目标.
sidebarGroup: 控制
---

# 自动调温卡 {#thermostat-card}

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
        "type": "thermostat",
        "entity": "climate.thermostat"
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

## 使用量 {#usage}

恒温计卡是一个气候或水热器实体的大拨号. 环显示目标温度,然后拖动它,或者使用减和加按钮来改变它. 中间的大数字是目标,以当前温度迄且设备正在做的事情,比如**Preheating**,围绕它. 角落中的菜单按钮打开了包含所有模式和设置的更多信息对话框.

拨号取出设备的用途颜色:加热时为橙色,冷却时为蓝色. 当设备关闭时,拨号为灰色,控制器退后.

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
        "type": "thermostat",
        "entity": "climate.bedroom_air_conditioner"
      }
    </script>
  </ha-embed-card>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "thermostat",
        "entity": "water_heater.water_heater"
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

在改变温度时使用自动调温卡是人们打开仪表板的原因,比如在气候景观上或者在走廊的平板上. 牌高:在片段视图中,需要五行. 当温度是房间里很多事情之一时,具有目标温度特征的[平板卡](/design/dashboards/tile-card)会采取一行并做同样的工作.

### 目前温度第一 {#current-temperature-first}

与 `show_current_as_primary: true` 相比, 大数字是当前温度, 目标移动到较小的线上 。 当人们大多想知道它有多温暖时使用它,只偶尔改变目标.

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
        "type": "thermostat",
        "entity": "climate.thermostat",
        "show_current_as_primary": true
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

### 特征 {#features}

与瓦片卡一样,自动调温卡在拨号下方具有特征. 设备的模式是很好的合拍方式:HVAC模式,预设,或风扇模式. 每个功能在片段视图的卡片中都添加了行,所以只添加人们经常改变的内容. 其余的是在多信息对话框中拍一个。

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
        "type": "thermostat",
        "entity": "climate.thermostat",
        "features": [
          {
            "type": "climate-hvac-modes",
            "hvac_modes": [
              "off",
              "heat",
              "cool",
              "auto"
            ]
          }
        ]
      }
    </script>
  </ha-embed-card>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "thermostat",
        "entity": "climate.bedroom_air_conditioner",
        "features": [
          {
            "type": "climate-fan-modes",
            "style": "icons"
          }
        ]
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

### 内容 {#content}

- 名字坐于牌头. 保持简洁,当部分已经说出是哪个房间时,就放出来.
- 选择匹配设备的特性 。 空调和散热阀有非常不同的模式.

## 配置 {#configuration}

- `entity`(字符串,需要):要显示的实体. 只有`climate`或`water_heater`域工作的实体.
- `name` (字符串):要显示的名称. 默认实体名称。
- `show_current_as_primary`(boolean):显示当前温度为大数字,其下的目标. 默认为 `false` 。
- `theme`(字符串):只适用于此卡的主题.
- {H0所发挥的作用}(列表):拨号下方要显示的特性,每个特性有一个`type`.

```yaml
type: thermostat
entity: climate.thermostat
features:
  - type: climate-hvac-modes
    hvac_modes:
      - "off"
      - "heat"
      - "cool"
      - "auto"
```

## 在代码中 {#in-code}

牌居于[`src/panels/lovelace/cards/hui-thermostat-card.ts`](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-thermostat-card.ts),元素为`<hui-thermostat-card>`. 它不会自己拨号 它重新使用比较信息对话框的控制:`<ha-state-control-climate-temperature>`用于气候实体,`<ha-state-control-water_heater-temperature>`用于热水器。 两者都建立在[`<ha-control-circular-slider>`](/design/components/controls)上. 在拨号里修好一些东西,卡片和对话框都得到它.

具有 `<hui-card-features>` 的特性, 与瓷砖卡所用的元素相同 。 在各段视图中,卡片取12列5行,可以缩到6列2行. 地物在上面添加行.

[来源](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-thermostat-card.ts)
