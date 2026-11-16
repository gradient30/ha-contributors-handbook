---
title: 媒体播放器
description: 发言者、 看电视或其他媒体播放器的更资讯的视角,
sidebarGroup: 媒体
---

# 媒体播放器 {#media-player}

Live demo of `ha-demo-more-info`, 连接到一个 demo Home Assistant.

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](https://contributors.home-assistant.io/design/more-info/media-player/)。

```html
<ha-demo-more-info entity="media_player.living_room_speaker"></ha-demo-more-info>
<ha-demo-more-info entity="media_player.living_room_tv"></ha-demo-more-info>
```

## 取证结果 {#what-it-shows}

媒体播放器的视线看起来就像现在播放音乐应用的屏幕,因为人们在控制正在播放的东西时会期望这样. 从上到下:

- **Cover art**:所演奏的画面,如专辑封面. 如果没有一个,一个带有音乐音符的灰色广场就取代它.
- **Title and artist**:媒体的名称,以及与其下方的艺术家或其他细节一致. 两部卷轴都使用 [颜色文字](/design/components/marquee-text) 时, 速度慢一些 。
- ** 进展**:一个[幻灯片](/design/components/slider),其位置和期限在下面。 当玩家支持时,你可以拖动它来寻找. 它只显示媒体有持续时间.
- ** Playback control**:前音轨和下音轨,中间有大充值播放或暂停[按钮](/design/components/button). 重复和洗牌坐在外端,当玩家支持它们时.
- **Volume**:一个哑巴按钮和一个音量滑动器. 仅将音量分级的玩家会降低音量,而将音量按下按钮。
- **更多动作**:一行图标按钮,用于浏览媒体,加入其他扬声器,选择源和声音模式,使玩家打开或关闭.

扬声器在播放音乐。 电视关机:只显示空封面和按钮来选择一个来源并打开.

## 设计说明 {#design-notes}

- 此视图在顶端没有较大的状态. 封面艺术,标题,以及剧情按钮已经告诉你发生了什么.
- 每个控制检查玩家的支持特性. 玩家不支持的控制被忽略. 在游戏按钮周围,一个缺失的控件会留下一个空位,所以游戏和暂停总是停留在中心.
- 音量只在玩家开机时显示,因为关机时没有声音.
- 207. 国家综合评估方案包括:
- 当一个发言者与其他发言者分组时,组合按钮会显示一个带有组合中发言者人数的小徽章.
- 当玩家无法使用时,视图只显示带有状态的空封面,没有控制.

## 在代码中 {#in-code}

视图为 `more-info-media_player` 在 [`src/dialogs/more-info/controls/more-info-media_player.ts`](https://github.com/home-assistant/frontend/blob/dev/src/dialogs/more-info/controls/more-info-media_player.ts) 。 哪些播放按钮由`computeMediaControls`在[`src/data/media-player.ts`](https://github.com/home-assistant/frontend/blob/dev/src/data/media-player.ts)中决定 。 其特征见于[`src/data/feature/media-player_entity_feature.ts`](https://github.com/home-assistant/frontend/blob/dev/src/data/feature/media-player_entity_feature.ts).

来源:[`more-info-media_player.ts`](https://github.com/home-assistant/frontend/blob/dev/src/dialogs/more-info/controls/more-info-media_player.ts)
