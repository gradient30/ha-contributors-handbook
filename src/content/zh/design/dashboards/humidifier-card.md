---
title: 加湿器卡
description: 加湿器卡片将加湿器或除湿器显示为一个拨盘，用于读取湿度并设置目标值。
sidebarGroup: 控制
---

# 加湿器卡 {#humidifier-card}

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
        "type": "humidifier",
        "entity": "humidifier.bedroom_humidifier"
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

## 使用量 {#usage}

湿度卡是[自动调温卡](/design/dashboards/thermostat-card)的兄弟姐妹,用于湿度. 戒指显示目标湿度,你拖动它,或者用减和加按钮来改变它. 中间的大数字是目标,有电流湿度和装置正在做的事情,比如**Humidifying**,周围. 角落中的菜单按钮打开了更多信息对话框 。

拨号会使用设备的颜色,像蓝色一样,同时进行湿化. 当设备关闭时,拨号是灰色的.

在湿度是一节中的主要事物时使用湿度卡,比如在卧室或地下室. 当它是一个房间里许多事情之一时,带有目标湿度特征的[平板卡](/design/dashboards/tile-card)取一排而不是五排.

### 目前湿度第一 {#current-humidity-first}

有了`show_current_as_primary: true`,大数字就是当前湿度,目标移动到较小的线上.

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
        "type": "humidifier",
        "entity": "humidifier.bedroom_humidifier",
        "show_current_as_primary": true
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

### 特征 {#features}

湿度卡在拨号下取特征. 拨号没有打开或关闭设备的按钮,所以在仪表盘编辑器中添加卡片时,会带有切换功能. 模式特征是另一个合适的。

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
        "type": "humidifier",
        "entity": "humidifier.bedroom_humidifier",
        "features": [
          {
            "type": "humidifier-toggle"
          },
          {
            "type": "humidifier-modes",
            "style": "icons"
          }
        ]
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

### 内容 {#content}

- 保持名字的简短,或者在片段已经说出是哪个房间时,不写出来.
- 添加切换特性 。 没有它,关闭设备需要前往更信息对话框。

## 配置 {#configuration}

- `entity`(字符串,需要):要显示的实体. 只有`humidifier`域的工作实体.
- `name` (字符串):要显示的名称. 默认实体名称。
- `show_current_as_primary`(boolean):将当前湿度显示为大数,其下的目标. 默认为 `false` 。
- `theme`(字符串):只适用于此卡的主题.
- {H0所发挥的作用}(列表):拨号下方要显示的特性,每个特性有一个`type`.

```yaml
type: humidifier
entity: humidifier.bedroom_humidifier
features:
  - type: humidifier-toggle
  - type: humidifier-modes
    style: "icons"
```

## 在代码中 {#in-code}

牌居于[`src/panels/lovelace/cards/hui-humidifier-card.ts`](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-humidifier-card.ts),元素为`<hui-humidifier-card>`. 和自动调温卡一样,它可以重用基于 [`<ha-control-circular-slider>`](/design/components/controls) 的 `<ha-state-control-humidifier-humidity>` 的 更多info 对话框的控制 `<ha-state-control-humidifier-humidity>` 。

特性以 `<hui-card-features>` 渲染 。 在各段视图中,卡片取12列5行,可以缩到6列2行. 地物在上面添加行.

[来源](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-humidifier-card.ts)
