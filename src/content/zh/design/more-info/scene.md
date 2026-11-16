---
title: 场景
description: 抨击场景的更多信息视图,带有激活按钮以及场景控制的实体.
sidebarGroup: 帮助者
sidebarGroup: 助手

---

# 场景 {#scene}

Live demo of `ha-demo-more-info`, 连接到一个 demo Home Assistant.

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](https://contributors.home-assistant.io/design/more-info/scene/)。

```html
<ha-demo-more-info entity="scene.movie_night"></ha-demo-more-info>
<ha-demo-more-info entity="scene.good_night"></ha-demo-more-info>
```

## 取证结果 {#what-it-shows}

一个场景没有变化的状态,只是一些事情:设置一组设备来保存它们. 因此它的视野是一个带有**Activate**按钮的状态行,在它的下面是作为场景一部分的实体.

一个场景的状态是它最后一次被激活的时刻,或者它从未被激活的时候未知. 美好的夜幕从未启用,因此其状态不明.

实体显示为瓦片卡,每行一张。 每个瓦片都显示实体的状态,当实体有一个适合时,如亮度滑动器用于可变亮的光线,则得到一个控制. 这样你就可以检查和微调 现场做了什么,而不离开对话。

## 设计说明 {#design-notes}

- ** Activate ** 是行尾的一个小文本[按钮](/design/components/button). 这是唯一的动作,所以不需要更多的重量。
- 砖块排除了所有成员的共同之处。 电影夜里的一切都在客厅里,所以它的瓷砖没有显示区域. 晚安,穿过客厅和走廊,所以它的瓷砖。
- 被隐藏的实体被排除在清单之外。
- 对话框显示信息视图中的场景没有历史 。 历史就是一拍即逝,在标题中的**历史**按钮后面。

## 在代码中 {#in-code}

状态行是 `state-card-scene` 在 [`src/state-summary/state-card-scene.ts`](https://github.com/home-assistant/frontend/blob/dev/src/state-summary/state-card-scene.ts) 。 法律依据: `more-info-content`在[`src/dialogs/more-info/more-info-content.ts`](https://github.com/home-assistant/frontend/blob/dev/src/dialogs/more-info/more-info-content.ts)中为任何拥有成员的实体提供实体名单。 它从场景的`entity_id`属性中构建了一块牌的网格.

来源:[`state-card-scene.ts`](https://github.com/home-assistant/frontend/blob/dev/src/state-summary/state-card-scene.ts)
