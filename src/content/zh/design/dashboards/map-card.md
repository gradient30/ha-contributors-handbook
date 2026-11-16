---
title: 地图卡
description: 地图卡显示在交互式地图上的人、装置和区的位置,可选的线索显示他们曾去过的地方。
sidebarGroup: 信息
---

# 地图卡 {#map-card}

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
        "type": "map",
        "entities": [
          "person.alex",
          "person.sam",
          "zone.home",
          "zone.work"
        ]
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

## 使用量 {#usage}

地图卡回答一个问题:每个人在哪里? 它在地图上为每一个有位置的实体设置标记,比如人,设备跟踪器,或者区. 选择标记打开实体的更多信息对话框 。 人们可以平整和放大地图,侧面的按钮可以重置视图并打开或关闭集群.

当位置本身重要时使用. 如果人们只想知道某人是否在家,那么个人实体的[平板卡](/design/dashboards/tile-card)或[浏览卡](/design/dashboards/glance-card)就会在更小的空间里说这句话. 一张地图需要很多空间来获取一个信息,所以给它一个存在的理由.

该地图默认遵循Home Assistant的主题. 在光线主题中,地图是光线,在黑暗主题中,地图是暗线.

### 标记 {#markers}

一个人或设备跟踪器以圆标显示,其名称首字母,或者其图片在拥有时显示. 区域显示为它的图标 。 使用 `label_mode` 在一个实体上, 标记显示状态, 属性, 或者图标而不是名称 。

力行大乘经. 当您只有几个实体时, 用 `cluster: false` 关闭它 。

### 以往地点的路径 {#path-of-previous-locations}

使用 `hours_to_show` , 地图会绘制一条线, 穿过每个实体在那个小时的时间 。 它可以用来移动的东西,比如汽车或割草机. 保持低时数:一周的地点变成一个不告诉任何人的缠圈.

### 主题模式 {#theme-mode}

有了`theme_mode`,地图总是`light`或者总是`dark`,不管主题是什么. 默认的 `auto` 遵循主题 。 深色的地图可以在夜间的墙板上发挥良好的作用,但强迫一个模式意味着它不再与其余的仪表板匹配.

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
        "type": "map",
        "entities": [
          "person.alex",
          "person.sam"
        ],
        "theme_mode": "dark"
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

### 地图样式 {#map-style}

该地图有一些内置外观,以 `map_style` 选用 `default`, `colorful`, `natural`, `muted`,`gray` 和`toner` 。 每个都有一个灯光和一个暗版,主题模式选择哪个显示. 默认样式使用符合Home Assistant主题的颜色. 在YAML中,`map_style`也可以是一种从其中一种样式开始并改变其颜色的映射.

### 内容 {#content}

- 添加需要在地图上的实体, 仅此而已 。 每个额外的标记都让一个人更难找
- 当他们给标记赋予意义时,像家和办公室一样,添加区域. 一个区旁边的标记一看就知道了
- 在实体首字母模棱两可时使用`name`,比如两个名字以同一个字母开头的人.

## 配置 {#configuration}

- `entities`(列表):要显示的实体. 每个都是实体ID,或者用`entity`和下面的选项进行映射. 需要,除非您使用 `show_all` 或 `geo_location_sources` 。
- `geo_location_sources`(列表):显示所有实体的地理定位变态源,如地震或来自种子的野火。 对每个来源使用`all`。
- `show_all` (boolean): 显示每个有位置的实体. 不能与`entities`或`geo_location_sources`结合. 默认为 `false` 。
- `title`(字符串):地图上方的标题.
- `aspect_ratio`(字符串):地图与其宽度相比的高度,如`16:9`或`50%`.
- `default_zoom`(数字):地图打开时的缩放级别。 默认为 `14` 。
- {带来的好处}(字符串):`auto`、`light`或`dark`。 默认为 `auto` 。
- `map_style`(字符串或绘图):地图的外观. 默认为 `default` 。
- `hours_to_show`(数字):前几小时要画。 默认为 `0`, 没有路径 。
- `auto_fit` (boolean): 当一个实体移动时, 移动和缩放地图, 所以它们都留在视野中 。 默认为 `false` 。
- `fit_zones` (boolean): 当地图符合实体时, 也注意区域。 默认为 `false` 。
- `show_zone_radius` (boolean): 总是绘制显示一个区域大小的圆形. 默认为 `false` 。
- `cluster` (boolean):结合了紧密在一起的标记. 默认为 `true` 。
- `scale_ruler` (boolean): 显示带有地图比例尺的标尺 。 默认为 `false` 。
- { 我还}( 列表): 仅在满足所有条件时显示实体 。

`entities` 中一个实体的选项 :

- `entity`(字符串,需要):要显示的实体.
- 秘书长的报告 `name` (字符串):标记上的标签。
- `color`(字符串):标记的颜色及其路径.
- `label_mode`(字符串):标记显示的内容:`name`,`state`,`attribute`,或`icon`. 默认为 `name` 。
- `attribute` (字符串):要显示的属性,带有`label_mode: attribute`.
- `unit` (字符串):在属性后显示的单位.
- `focus` (boolean): 当地图适合时, 请查看此实体 。 默认为 `true` 。

```yaml
type: map
hours_to_show: 24
entities:
  - person.alex
  - entity: person.sam
    color: "#93c47d"
  - zone.home
  - zone.work
```

## 在代码中 {#in-code}

牌居于[`src/panels/lovelace/cards/hui-map-card.ts`](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-map-card.ts),元素为`<hui-map-card>`. 地图本身在 [`src/components/map/`](https://github.com/home-assistant/frontend/tree/dev/src/components/map) 中为 `<ha-map>`, 个人的更多信息对话框以及设置中的位置编辑器也使用此功能 。 它绘制了带有MapLibre的矢量映射图,在无法显示矢量映射图的设备上返回到Leaflet. 风格生活于[`src/common/map/map-styles.ts`](https://github.com/home-assistant/frontend/blob/dev/src/common/map/map-styles.ts).

在部分视图中,地图取全宽和4行. 它可以缩到6列和2排.

[来源](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-map-card.ts)
