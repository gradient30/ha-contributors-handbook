---
title: 工厂状况卡
description: 植物状态卡显示一个植物的读数,如水分和光线,并指出需要注意的.
sidebarGroup: 信息
---

# 工厂状况卡 {#plant-status-card}

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
        "type": "plant-status",
        "entity": "plant.monstera"
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

## 使用量 {#usage}

植物状态卡是为一类实体制作的: 植物融合的植物. 该实体将植物的传感器捆绑在一起,如水分、温度、光度、导电率和电池,并知道每个设备的分布范围。 卡片连续显示所有读数,每个读数都有图标,值,单位.

其范围以外的读数以粗体显示,以错误颜色显示。 在演示中,怪兽的湿度太低. 这就是卡片的全部要点:你看一看哪个工厂需要水,光,或者一个新的电池。

选择读取会打开它背后的传感器的更多信息对话框, 以及它的历史 。

该卡只与植物实体合作. 对于单个的植物传感器,如没有植物融合的水分传感器,使用[平板卡](/design/dashboards/tile-card)或[sensor card](/design/dashboards/sensor-card).

### 图片 {#picture}

当植物实体有图片时,卡片显示为横幅,上面刻有名称. 没有图片,只显示名字,如在演示中.

### 内容 {#content}

- 卡片显示植物的读数. 你不能选哪一种,所以如果不应该在卡片上,在植物整合中留下一个传感器.
- 电池图标跟随关卡,并取电池关卡的颜色,如几乎是空的红色.
- 使用`name` 当植物实体名称不是人们用于植物的名称时.

## 配置 {#configuration}

- `entity`(字符串,需要):要显示的植物实体.
- `name` (字符串):要显示的名称. 默认实体名称。
- 5)),是属于该类,属于该类。

```yaml
type: plant-status
entity: plant.monstera
```

## 在代码中 {#in-code}

牌居于[`src/panels/lovelace/cards/hui-plant-status-card.ts`](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-plant-status-card.ts),元素为`<hui-plant-status-card>`. 它所显示的读数是它所知道的植物实体的属性:`moisture`,`temperature`,`brightness`,`conductivity`,和`battery`. 实体的 `problem` 属性 表示哪些是超出范围 。 `sensors` 属性将每次读取链接到它的传感器实体: 卡使用它来格式化这样的传感器的值,并打开它的更多信息对话框.

该卡片在泥瓦风景区有3个固定尺寸,并取一节全宽.

[来源](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-plant-status-card.ts)
