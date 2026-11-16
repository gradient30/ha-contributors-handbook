---
title: 轻卡
description: 灯卡显示一盏灯为大圆形按钮,周围有环状以设定亮度.
sidebarGroup: 控制
---

# 轻卡 {#light-card}

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
        "type": "light",
        "entity": "light.living_room_lamp"
      }
    </script>
  </ha-embed-card>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "light",
        "entity": "light.kitchen_ceiling"
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

## 使用量 {#usage}

灯卡是一个灯光的大控制. 中间是一个带有光线的按钮,环绕着它设置亮度. 在按钮下面,你可以看到亮度和名字. 选择切换光线的按钮, 握住它打开更多信息对话框 。 角落中的菜单按钮也打开了更多信息对话框.

图标取光的颜色,变得更明亮或沉淀. 关闭的灯是灰色的。 拖动戒指时,亮度会在移动时在卡片中间显示.

当一个灯光是仪表板或一节中的主要东西时使用灯卡,就像门旁边的壁板. 对于大多数灯光来说,带有亮度特征的[平板卡](/design/dashboards/tile-card)更适合:它需要四分之一的房间,并且坐在同一区域其他灯光的旁边很舒适.

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
</ha-embed-provider>
```

### 无亮光的灯 {#lights-without-brightness}

只能打开和关闭的灯光没有戒指. 该卡仍然显示按钮和名称,所以在您交换实体时不会跳转. 对于这样的灯光,一个瓦片卡或[按钮卡](/design/dashboards/button-card)在更小的房间里说同样的话.

### 内容 {#content}

- 保持名字的简短。 它坐落在按钮下,卡片中间,一个长名包或被切掉.
- 只有当灯的默认图标没有说出它是什么,比如地板灯或灯条时,才设置图标.
- 保留默认动作 。 人们期望一个水龙头来切换灯光, 和戒指来淡化它。

## 配置 {#configuration}

- `entity`(字符串,需要):要显示的光线. 只有`light`域的工作实体.
- `name` (字符串):要显示的名称. 默认实体名称。
- `icon` 实体图标的默认值。
- `theme`(字符串):只适用于此卡的主题.
- `tap_action` (动作): 当您选择按钮时会发生什么 。 默认为 `toggle` 。
- `hold_action`(动作):按住按钮后会发生什么. 默认为 `more-info` 。
- `double_tap_action` (动作): 双击按钮时会发生什么 。 默认为 `none` 。

```yaml
type: light
entity: light.living_room_lamp
name: "Reading lamp"
icon: "mdi:floor-lamp"
```

## 在代码中 {#in-code}

牌居于[`src/panels/lovelace/cards/hui-light-card.ts`](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-light-card.ts),元素为`<hui-light-card>`. 环是 [`<ha-control-circular-slider>`](/design/components/controls),同样的控制 恒温计卡使用, 在 `start` 模式中从1% 到100%。 只显示光支持亮度. 以 `brightness_pct` 设置亮度调用 `light.turn_on` 。

该卡没有自己的网格选项,协商中各段的视野中,它会占用该段的全宽和所需的 你好.

[来源](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-light-card.ts)
