---
title: 图片元素卡
description: 图片元素卡将图标,标签,徽章,以及按钮放置在图像上,就像地板图上的灯光一样.
sidebarGroup: 不用 页所提供的就有业已协商 为什么 就是的支持支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援
  支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援
  支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援
---

# 图片元素卡 {#picture-elements-card}

## 使用量 {#usage}

图片元素卡(英語:Pictual elements card)是一张上面有事物的图片. 每个元素坐落在您选择的位置,以图像的百分比表示: 客厅角落的灯的图标,窗口旁边的温度,一个关闭一切的按钮. 这张卡片是人们用来做地板图案的,也是用来拍一个房间的照片,上面有其装置的标记。

此页无生例. 这个网站的演示家没有图片或相机可以显示.

这也是最免费的卡片。 任何布局都不是为您决定的,所以结果只有建造它的人做出来时才那么清楚. 当图片上的位置带有意义时,如设备在屋里的地方,就伸手去确实是. 当它没有时,一个[图片浏览卡](/design/dashboards/picture-glance-card)或[纸牌](/design/dashboards/tile-card)的一节更容易制作,并且更容易在每个屏幕大小上使用.

### 要件 {#elements}

- 姻缘 `state-icon`:一个实体的图标,以它的状态为颜色. 选择它打开更多信息对话框 。
- `state-label`:一个实体作为文本的状态,或其属性之一,带有可选的`prefix`和`suffix`.
- `state-badge`:实体状态作为圆形标签徽章.
- `icon`:一个固定的图标,用于不与实体状态绑定的动作.
- `image`:图片上方的图像,可以跟随一个实体的状态与`state_image`和`state_filter`. 用它来画一盏能点亮的灯.
- `action-button`: 执行动作的文本按钮, 如 `light.turn_off` 。 旧名`service-button`,仍然有效.
- `conditional`:一组元素,仅在满足其条件时才会显示.

每个元素需要`style`, CSS属性的映射. 使用 `top` 和 `left` 来放置 。梢元素以该点为中心,因此`top: 50%`和`left: 50%`将其置于图像的中间. 风格还可以缩放,旋转,或涂色.

### 绘图元素 {#tapping-elements}

图标和标签很小,在繁忙的地板计划中,很难用手指打. 因此卡片将一个水龙头传递到最近的图标或标签上,最高可达24像素. 两盏灯间间隙的一盏水龙头往最靠近的一盏,两个重叠的元件不再互相盗取两盏水龙头.

默认情况下, 选择或持有一个元素会打开其实体的更多信息对话框 。 将 `tap_action` 设定为 `toggle` , 供元素使用, 如地板图上的灯光 。

### 黑暗模式 {#dark-mode}

一个为浅色背景绘制的地板图在黑暗主题中看起来很严酷. 使用 `dark_mode_image` , 该卡会在暗主题中显示另一个图像 。 在 `dark_mode_filter` 中, 它将 C 有些过滤器应用到同一个图像上, 如 `invert(1) hue-rotate(180deg)` 。

### 内容 {#content}

- 使用固定宽度比的图像,并按百分比设置元素。 然后元素在每一个屏幕大小上都保持原位.
- 将状态在图片本身上显示在您可以的地方,并带有状态图标或点亮的图像. 装满文字标签的地板图是一张伪装的桌子.
- 保持足够大的元素来挖掘.侬在样式中用 `--mdc-icon-size` 来缩放图标, 而不是把它们放在一起 。
- 给图标和按钮 `title` 。 这是工具提示, 和名称屏幕阅读器使用。

## 配置 {#configuration}

- `elements`(列表,需要):要放置的元素,每个元素都有`type`竺和`style`.
- `image`(字符串或介质):图片. 需要`image`、`image_entity`、`camera_image`或`state_image`中的一个。
- `image_entity`(字符串):拍摄照片的图像或人物实体.
- `camera_image`(字符串):作为图片显示的相机实体.
- `camera_view` (字符串): `auto` 用于快照, 或 `live` 用于直播流 。 默认为 `auto` 。
- `entity` (字符串): 图片如下 II `state_image` 和 `state_filter` 。
- 谐音 `state_image` (图): 每个状态的图片 `entity`. 需要 `entity` 。
- `state_filter` (地图):每个状态的 `entity` 一个 CSS 过滤器 。
- `dark_mode_image`(字符串或介质):黑暗主题中使用的图片.
- `dark_mode_filter`(字符串):暗主题中图片的 CSS 过滤器.
- `aspect_ratio`(字符串):图片的形状,如`16x9`或`50%`.
- `title`(字符串):图片上方的一个标题.
- `theme`(字符串):适用于卡片的主题.

```yaml
type: picture-elements
image: "/local/floor_plan.png"
dark_mode_filter: "invert(1) hue-rotate(180deg)"
elements:
  - type: state-icon
    entity: light.living_room_lamp
    tap_action:
      action: toggle
    style:
      top: "30%"
      left: "20%"
  - type: state-label
    entity: sensor.living_room_temperature
    style:
      top: "40%"
      left: "20%"
  - type: action-button
    title: "All off"
    action: light.turn_off
    target:
      entity_id: all
    style:
      top: "90%"
      left: "85%"
```

## 在代码中 {#in-code}

牌居于[`src/panels/lovelace/cards/hui-picture-elements-card.ts`](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-picture-elements-card.ts),元素为`<hui-picture-elements-card>`. 图片为`<hui-image>`. 元素活在[`src/panels/lovelace/elements/`](https://github.com/home-assistant/frontend/tree/dev/src/panels/lovelace/elements),每个类型一个,如`<hui-state-icon-element>`,和`create-styled-hui-element.ts`应用它们的`style`. `action-button` 创建为 `<hui-service-button-element>` 。 每个元素都绝对以 `transform: translate(-50%, -50%)` 定位, 这就是为什么它的核心是它的 `top` 和 `left` 。

水龙头到最接近元素的路径在 [`src/panels/lovelace/cards/picture-elements/nearest-hit.ts`](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/picture-elements/nearest-hit.ts) 中存在 。 参加设定的元素 `delegatedActions` 并以 `getHitInfo()` 报告其命中区域 。

牌投 `Image required` 没有图像来源, `Elements required` 没有元素列表 。 它没有自己的网格选项:在区块视图中,它取走所有12列,它的高度跟随图片.

[来源](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-picture-elements-card.ts)
