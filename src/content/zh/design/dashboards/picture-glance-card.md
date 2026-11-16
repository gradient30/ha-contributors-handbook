---
title: 图片浏览卡
description: 图片透视卡在底部显示一行实体图标的图像,可以一目了然地看到并控制一个房间或相机视图.
sidebarGroup: 不用 页所提供的就有业已协商 为什么 就是的支持支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援
  支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援
  支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援
---

# 图片浏览卡 {#picture-glance-card}

## 使用量 {#usage}

图片透视卡将图片,往往是房间或相机,放在实体图标的栏杆后面. 栏坐于画面底部,左侧为标题,如果设置一个. 图标在实体不活动时是灰色的,在活动时变为白色,所以你可以看到哪些灯没有读到任何东西。

此页无生例. 这个网站的演示家没有图片或相机可以显示.

当一个图片是识别 ∮一个地方的最佳方法的时候使用它 人们想要对那个地方进行一些快速的控制:客厅的灯光在客厅照片上方,或者门铃相机上方的前门锁.

当图片涉及一个实体时,请使用[图片实体卡](/design/dashboards/picture-entity-card). 当图标属于图像上的特定位置时,如地板图上,使用[图片元素卡](/design/dashboards/picture-elements-card). 没有图片,[浏览卡](/design/dashboards/glance-card)会显示一行实体,[区域卡](/design/dashboards/area-card)会给房间一个概览.

### 切换和对话框图标 {#toggle-and-dialog-icons}

牌将实体分成两组. 可以被切换的实体,如灯光、开关和风扇,分成一组: 选择它们的图标切换它们。 其它所有实体,如传感器和锁,都进入另一组: 选择他们的图标打开更多info对话框. 每组在栏杆上都有自己的排位,在栏杆之间有空间分布,因此切片总是在栏杆的尾部坐在一起. 持有图标可打开两者的更多信息对话框 。

使用 `force_dialog: true` , 每个图标都会打开更多信息对话框 。 碰巧用它 是个问题 就像加热器一样

### 状态 {#state}

图标默认不显示文本 。 使用`show_state`,在卡片或每个实体上,状态显示在图标下方. 一个 per-entity `attribute` 显示一个属性代替, 有可选的 `prefix` 和 `suffix` 。 节制使用:栏小,少数图标用文字快速填充.

### 图片 {#the-picture}

图片功能与图片实体卡相同. 它可以是固定的 `image`, `image_entity`, `camera_image` 带有快照或`live` 溪流, 也可以是每个状态的 `entity` 图像 `state_image` 。 当 `entity` 关闭时, 且该状态没有图像时, 图片会变成灰色 。 选择图片会打开 `entity`,`image_entity` 或相机的更多信息对话框, 除非您另设置 `tap_action` 。

### 内容 {#content}

- 留于五实体或少. 酒吧是窄卡上的一行.
- 仅在图片不能说明问题时使用标题 。
- 取一尺,以平地平地处其下. 师曰.

## 配置 {#configuration}

- `entities`(列表,需要):要显示为图标的实体. 每个项目可以是实体ID,也可以是使用`entity`,`name`,`icon`,`show_state`,`attribute`,`prefix`,`suffix`和动作的映射.
- `title`(字符串):栏中的标题.
- `image`(字符串或介质):要显示的图像. 需要`image`、`image_entity`、`camera_image`或`state_image`中的一个。
- `image_entity`(字符串):拍摄照片的图像或人物实体.
- `camera_image`(字符串):作为图片显示的相机实体.
- `camera_view` (字符串): `auto` 用于快照, 或 `live` 用于直播流 。 默认为 `auto` 。
- `entity`的批准 `entity` (字符串): 图片如下的实体, 用于 `state_image`, `state_filter` 和灰色过滤器 。
- 听好了 `state_image` (地图): 每个状态的图像为`entity`。 需要`entity` 。
- `state_filter` (地图):每个状态的 `entity` 一个 CSS 过滤器 。
- `aspect_ratio`(字符串):图像的形状,如`16x9`或`50%`.
- {带来的好处}(字符串):`cover`、`contain`或`fill`。 默认为 `cover` 。
- `show_state` (boolean): 显示每个图标下的状态 。 默认为 `false` 。
- `force_dialog` (boolean): 使每个图标打开更多信息对话框 。 默认为 `false` 。
- `theme`(字符串):适用于卡片的主题.
- `tap_action`,`hold_action`,`double_tap_action`(动作):当你选择图片,持有,或双拍时会发生什么.

```yaml
type: picture-glance
title: "Living room"
image: "/local/living_room.jpg"
entities:
  - light.living_room_lamp
  - media_player.living_room_speaker
  - sensor.living_room_temperature
```

## 在代码中 {#in-code}

牌居于[`src/panels/lovelace/cards/hui-picture-glance-card.ts`](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-picture-glance-card.ts),元素为`<hui-picture-glance-card>`. 图片是 `<hui-image>`,每个图标是 `<ha-icon-button>` 里面有一个 `<ha-state-icon>` 。 实体切换是否来自`DOMAINS_TOGGLE` [`src/common/const.ts`](https://github.com/home-assistant/frontend/blob/dev/src/common/const.ts) 。 当实体活动时,图标获得 `state-on` 类 。 颜色来自`--ha-picture-icon-button-color`和`--ha-picture-icon-button-on-color`的各个字,以及`--ha-picture-card-background-color`和`--ha-picture-card-text-color`的栏。

该卡投出`Invalid configuration`没有`entities`,没有任何图像源,或者使用`state_image`但没有`entity`. 它没有自己的网格选项:在区块视图中,它取走所有12列,它的高度跟随图像.

[来源](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-picture-glance-card.ts)
