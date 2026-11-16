---
title: 图片卡
description: 图片卡显示一个图像,在选择时可以做一些事情,比如打开另一个视图.
sidebarGroup: 不用 页所提供的就有业已协商 为什么 就是的支持支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援
  支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援
  支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援
---

# 图片卡 {#picture-card}

## 使用量 {#usage}

图片卡显示的是单一的图像,边缘到边缘,有圆角和别的东西:没有标题,没有名字,没有状态. 这是最简单的卡片。 使用它来给一个仪表盘一些字符,比如其部分上方的一个房间的照片,或者做一个巨大的视觉链接到另一个视图.

此页无生例. 这个网站的演示家没有图片或相机可以显示.

默认情况下, 选择图片无效 。 给它一个 `tap_action` 让它成为链接或按钮, 如 `navigate` 打开一个房间的视图 。 只有这样,卡片才能获得指针光标,并用键盘可以到达.

当图片需要显示某实体时,另选一张牌:

- [图片实体卡](/design/dashboards/picture-entity-card) 在图像上方显示一个实体的名称和状态 。
- [图片浏览卡](/design/dashboards/picture-glance-card) 在底部添加一行实体图标 。
- [图片元素卡](/design/dashboards/picture-elements-card) 将图标、 标签和按钮放置在图像的任何地方, 如地板图上 。

### 图像实体 {#image-entity}

而非固定的图像,卡片可以从一个拥有 `image_entity` 的实体拍照. 这对一个图像实体是有效的, 有很多的集成, 和一个人物, 人物的概况图片卡显示。 图片跟随实体:当图像实体获得新图像时,卡片会显示. 带有映像实体, 选择此卡会打开其更多信息对话框, 除非您另设置 `tap_action` 。

### 内容 {#content}

- 总是设定 `alt_text` 当图片意味着什么, 或者充当链接 。 屏幕阅读器没有别的事可做。 以 `image_entity` 表示实体名称为倒置 。
- 选择在光线和黑暗主题两方面都有效的图像. 牌上显示的是图像的原样.
- 图片取其片段的全宽度,其高度从画面上顺过来. 一个非常高的图像将一切推向下方,所以在使用它之前把它剪掉.

## 配置 {#configuration}

- `image`(字符串或介质):要显示的图像,作为URL或介质源项. 需要, 除非你设置 `image_entity` 。
- `image_entity`(字符串):拍摄照片的图像或人物实体.
- `alt_text` (字符串):图像的替代文本.蓓莉亚,如果有的话,默认为`image_entity`的名称。
- `theme`(字符串):适用于卡片的主题.
- `tap_action`(动作):选择牌时会发生什么. 那么默认为 `more-info` 用 `image_entity` , 而 `none` 不使用 。
- `hold_action`,`double_tap_action`}(动作):停机或双ondatrop的指标。 默认为 `none` 。

```yaml
type: picture
image: "/local/living_room.jpg"
alt_text: "Living room"
tap_action:
  action: navigate
  navigation_path: "/lovelace/living-room"
```

## 在代码中 {#in-code}

牌居于[`src/panels/lovelace/cards/hui-picture-card.ts`](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-picture-card.ts),元素为`<hui-picture-card>`. 它是一个平原 `<img>` 在 `<ha-card>` 里面,有 `overflow: hidden` 的圆角。 与其他图片卡不同的是,它不使用`<hui-image>`,因此它没有状态图像,过滤器,或宽比.

该卡没有自己的网格选项. 在片段视图中,它需要全部12列,其高度跟随图像.

[来源](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-picture-card.ts)
