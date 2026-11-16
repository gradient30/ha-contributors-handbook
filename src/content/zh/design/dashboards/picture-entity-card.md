---
title: 图片实体卡
description: 图片实体卡显示一个实体为图像,其名称和状态位于下方的一个栏. 这是相机的卡片。
sidebarGroup: 媒体与图片
  
  
---

# 图片实体卡 {#picture-entity-card}

## 使用量 {#usage}

图片实体卡显示一个实体为图片. 图像填充卡片,底部的一个暗色的透视栏显示左边的实体名称和右边的状态. 选择此卡会打开实体的更多信息对话框 。

此页无生例. 这个网站的演示家没有图片或相机可以显示.

用于相机:卡片显示其最新快照,或直播流. 用于图像实体,或带有剖面图的人. 并将其用于一个从图片中比从图标中更容易识别的实体,如灯,门铃,或花园.

对其它事物来说,[平板卡](/design/dashboards/tile-card)在更少的空间里告诉更多的人. 当图片显示多个实体时, 请使用 [图片浏览卡](/design/dashboards/picture-glance-card) 。 对于没有实体的图片,请使用[图片卡](/design/dashboards/picture-card).

### 照片从何而来 {#where-the-picture-comes-from}

卡片按此顺序选择其图像:

1. 实体本身的图片,当 `show_entity_picture` 正在运行时, 实体有一个, 就像一个媒体播放器的专辑艺术 。
2. `image`你准备好了。
3. 图像实体的图像,或者人物的剖面图片.

相机实体总是显示相机, 而`camera_image` 显示任何其它实体的相机 。 使用 `camera_view: live` , 该卡会播放直播流而不是刷新快照 。 直播流使用更多的带宽,所以保持`auto`,除非人们需要看到运动.

### 状态图像和过滤器 {#state-images-and-filters}

画面随州而变化. `state_image`将状态映射到一个图像上,如为`on`点燃的灯光照片,为`off`在暗处的灯光照片. `state_filter` 将状态映射到 CSS 过滤器, 如 `brightness(50%)` 。

当实体关闭,或无法使用,且没有该状态的图像时,卡片会使图片变灰. 人们一眼就看到灯关了,没有读到州里.

### 名称和状态 {#name-and-state}

使用 9⁄4 ̄ ̧漯B 以其中之一为文字中心. 两者都一样,酒吧都不见了,卡片就是照片. 只在图片已经显示时才隐藏状态, 就像用相机一样.

### 内容 {#content}

- 使用底部有平静区域的照片 。 栏杆是透视的,后面忙碌的细节使得文本难以阅读.
- 当数张牌的图像大小不同时设置 `aspect_ratio`, 所以牌排成一行 。 使用 `fit_mode` 决定图像如何填充形状 : `cover` 庄稼 `contain` 信箱 `fill` 伸缩 。

## 配置 {#configuration}

- `entity`(字符串,需要):要显示的实体.
- `name` (字符串):要显示的名称. 默认实体名称。
- `image`(字符串或介质):要显示的图像,作为URL或介质源项. 对大多数实体的要求,见上文。
- `show_entity_picture` (boolean): 使用实体的图片, 当它有一个。 默认为 `false` 。
- `camera_image`(字符串):作为图片显示的相机实体.
- `camera_view` (字符串): `auto` 用于快照, 或 `live` 用于直播流 。 默认为 `auto` 。
- `state_image`(图):每个州的图像.
- `state_filter` (地图):咀嚼每个状态的 CSS 过滤器 。
- `aspect_ratio`(字符串):图像的形状,如`16x9`或`50%`. 当卡片在分区视图中有固定的行数时被忽略.
- {带来的好处}(字符串):`cover`、`contain`或`fill`。 默认为 `cover` 。
- `show_name` (boolean): 显示名称. 默认为 `true` 。
- `show_state`(boolean):显示状态. 默认为 `true` 。
- `theme`(字符串):适用于卡片的主题.
- {图表H0}(动作):选择牌时会发生什么. 默认缔结一项 `more-info` 。
- `hold_action`,`double_tap_action`}(动作):停机或双ondatrop的指标。 默认为 `none` 。

```yaml
type: picture-entity
entity: light.living_room_lamp
image: "/local/floor_lamp.jpg"
tap_action:
  action: toggle
```

## 在代码中 {#in-code}

牌居于[`src/panels/lovelace/cards/hui-picture-entity-card.ts`](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-picture-entity-card.ts),元素为`<hui-picture-entity-card>`. 该图片为`<hui-image>`([`src/panels/lovelace/components/hui-image.ts`](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/components/hui-image.ts)),与图片透视和图片元素卡共享. 该元素处理相机的快照和流,状态图像,滤镜,一个关闭的实体的灰色滤镜,以及宽比.

当实体不是相机,图像,或个人时,卡片会掷出`No image source configured`,没有`image`,`state_image`,`camera_image`,或`show_entity_picture`.

栏从 `--ha-picture-card-background-color` 和 `--ha-picture-card-text-color` 取其颜色 。 该卡没有自己的网格选项:在各段视图中,它将所有12列,其高度跟随图像.

[来源](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-picture-entity-card.ts)
