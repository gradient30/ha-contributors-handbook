---
title: 割草机
description: 机器人割草机的更多信息视图,有动画状态图片和按钮开始,停止,停靠.
sidebarGroup: 应用程序
---

# 割草机 {#lawn-mower}

Live demo of `ha-demo-more-info`, 连接到一个 demo Home Assistant.

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](https://contributors.home-assistant.io/design/more-info/lawn-mower/)。

```html
<ha-demo-more-info entity="lawn_mower.lawn_mower"></ha-demo-more-info>
```

## 取证结果 {#what-it-shows}

割草机景点是[真空](/design/more-info/vacuum)景点的兄弟姐妹. 两者都是自行完成任务的机器人,因此两者都展示了机器人在它下面有一行指令的图片,而不是滑动器或开关.

图片是机器人割草机的图画,随状态而变化:割草,还原,暂停,停靠,或出错. 则取州色.

图片下方的 [控制按钮](/design/components/controls) 组持有命令 。 每个都只显示割草机支持它时:

- ** 开始割除**或**暂停**,在一个按钮中。 它显示在割草机割草时暂停,可以暂停,然后以其他方式开始。
- 页:1
- ** 返回码头**。

顶部的州是割草机的州,如**Docked**. 当设备有电池传感器时,电池电位显示在时间旁边,就像在真空上. 假家的割草机没有 所以这里没有

## 设计说明 {#design-notes}

- 现在没有道理的按钮被禁用。 上面的割草机是停靠的,所以**停止**和**返回停靠**是灰色的。
- 与真空不同,割草机视图在按钮下方没有二级设置.

## 在代码中 {#in-code}

视图为 `more-info-lawn_mower` 在 [`src/dialogs/more-info/controls/more-info-lawn_mower.ts`](https://github.com/home-assistant/frontend/blob/dev/src/dialogs/more-info/controls/more-info-lawn_mower.ts) 。 图片为 `ha-state-control-lawn_mower-status` 在 [`src/state-control/lawn_mower/`](https://github.com/home-assistant/frontend/tree/dev/src/state-control/lawn_mower) 。 `LawnMowerEntityFeature` enum 和 `canDock` 这样的助手在 [`src/data/lawn_mower.ts`](https://github.com/home-assistant/frontend/blob/dev/src/data/lawn_mower.ts) 中 。

来源:[`more-info-lawn_mower.ts`](https://github.com/home-assistant/frontend/blob/dev/src/dialogs/more-info/controls/more-info-lawn_mower.ts)
