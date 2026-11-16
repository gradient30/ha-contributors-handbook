---
title: 媒体控制卡
description: 媒体的整个控制卡都显示媒体玩家在玩什么,包括艺术品、控件和进展。
sidebarGroup: 控制
---

# 媒体控制卡 {#media-control-card}

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
        "type": "media-control",
        "entity": "media_player.living_room_speaker"
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

## 使用量 {#usage}

媒体控制卡显示一名媒体玩家. 顶部是玩家的图标和名字,然后是正在播放的作品的标题和艺术家,然后是控件,比如播放,暂停,以及下一曲目. 当玩家知道长度和位置时,一个进步栏会沿着底部运行. 显示按钮取决于玩家支持什么,比如浏览媒体或关闭玩家的按钮.

这张卡片的颜色来自艺术品。 图像坐落在右侧,背景取出图像的主色调,文字的颜色保持可读性. 没有艺术品,卡片使用主色调. 当玩家关机时,卡片是灰色的,只保留动力按钮.

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
        "type": "media-control",
        "entity": "media_player.living_room_tv"
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

播放时使用媒体控制卡是值得的,就像客厅的扬声器一样. 对于一个玩家来说,人们大多会打开和关闭,或者只改变一个 [平板卡](/design/dashboards/tile-card) 的音量,带有播放或音量特性的音量较小.

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
        "entity": "media_player.living_room_speaker",
        "features": [
          {
            "type": "media-player-playback"
          }
        ]
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

### 窄牌 {#narrow-cards}

该卡会测量它自己的宽度, 并降低一些不合适的东西。 低于350像素, 进步栏去。 300像素以下,控制器也会运行,同时有东西在播放. 将卡片放入窄柱或网格时记住这一点.

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
  <ha-embed-card style="grid-column: span 8">
    <script type="application/json">
      {
        "type": "media-control",
        "entity": "media_player.living_room_speaker",
        "grid_options": {
          "columns": 8
        }
      }
    </script>
  </ha-embed-card>
  <ha-embed-card style="grid-column: span 7">
    <script type="application/json">
      {
        "type": "media-control",
        "entity": "media_player.living_room_speaker",
        "grid_options": {
          "columns": 7
        }
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

### 内容 {#content}

- 标题和艺术家来自玩家. 当您盘旋时, 标题不符合卷轴 。
- 1929n),保持玩家名字的简短. 它 1929n与菜单按钮共享上行.

## 配置 {#configuration}

- `entity`(字符串,需要):要显示的媒体播放器. 只有`media_player`域的工作实体.
- `name` (字符串):要显示的名称. 默认实体名称。
- `theme`(字符串):只适用于此卡的主题.

```yaml
type: media-control
entity: media_player.living_room_speaker
```

## 在代码中 {#in-code}

牌居于[`src/panels/lovelace/cards/hui-media-control-card.ts`](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-media-control-card.ts),元素为`<hui-media-control-card>`. 控件来自 `computeMediaControls` 在 [`src/data/media-player.ts`](https://github.com/home-assistant/frontend/blob/dev/src/data/media-player.ts) 中的 `computeMediaControls` , 更多信息对话框也使用它, 所以卡片和对话框提供相同的按钮 。 颜色来自 `extractColors` [`src/common/image/extract_color.ts`](https://github.com/home-assistant/frontend/blob/dev/src/common/image/extract_color.ts) 的 `extractColors` , 它从艺术品中选择它们 。

该卡以 `ResizeObserver` 观察自己的大小, 并设定其狭小和非常狭小的布局 。 进步栏是 [`<ha-slider>`](/design/components/slider) , 在媒体播放时不断更新 。

[来源](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-media-control-card.ts)
