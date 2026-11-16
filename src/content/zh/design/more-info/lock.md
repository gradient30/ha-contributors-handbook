---
title: 锁定
description: 锁的更多信息视图,有大锁开关和单独的确认按钮打开门.
sidebarGroup: 开幕和安全
sidebarGroup: 开合与安防

---

# 锁定 {#lock}

Live demo of `ha-demo-more-info`, 连接到一个 demo Home Assistant.

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](https://contributors.home-assistant.io/design/more-info/lock/)。

```html
<ha-demo-more-info entity="lock.front_door"></ha-demo-more-info>
```

## 取证结果 {#what-it-shows}

锁的主要控制是大垂直[控制开关](/design/components/controls). 锁在顶部,在底部解锁,以闭锁和开锁作为图标. 开关采用状态的颜色,如锁用的绿色.

锁在锁上或解锁时,图标脉冲,所以你可以看到,甚至在状态改变之前,事情正在发生.

一些锁也可以打开门,而不仅仅是打开门. 前门上方的锁支撑着这个,所以它得到一个**打开的门**开关下方的按钮. 开门并不是你无意中想做的 所以需要两个水龙头:

1. 选择**打开的门**。 按钮改为 ** 真的打开? **.
2. 在数秒内再次选择打开门. 按钮显示 ** 完成 ** 片刻,然后返回 ** 打开的门**。

当你等待太长,按钮会回到 ** 打开的门** 自己。

## 其他国家 {#other-states}

- **Jammed**:开关被卡住的锁的大型图标所取代,其下方有**Unlock**和**Lock**按钮,因此可以向任一方向再次尝试.
- **未知**:开关变为两个独立的按钮,**Lock**和**Unlock**,因为没有状态可以将开关放入.
- ** 打开、打开、锁定或解锁**: ** 打开的门** 已禁用,因为门已经打开或忙碌。

## 设计说明 {#design-notes}

- 当锁需要代码时, Home Assistant 在锁、 解锁或打开前, 在单独的对话框中询问它 。 存储在实体设置中的代码跳过这个问题 。
- 锁定和解锁是同一个开关上的一个手势. 打开门是分开的,作为带有自身确认的按钮,因为它不能通过把开关翻回来解除.

## 在代码中 {#in-code}

视图为 `more-info-lock` 在 [`src/dialogs/more-info/controls/more-info-lock.ts`](https://github.com/home-assistant/frontend/blob/dev/src/dialogs/more-info/controls/more-info-lock.ts) 。 开关是`ha-state-control-lock-toggle`在[`src/state-control/lock/`](https://github.com/home-assistant/frontend/tree/dev/src/state-control/lock)中。 帮助者,如`canOpen`和`callProtectedLockService`,和`LockEntityFeature`enum都在[`src/data/lock.ts`](https://github.com/home-assistant/frontend/blob/dev/src/data/lock.ts)。

来源:[`more-info-lock.ts`](https://github.com/home-assistant/frontend/blob/dev/src/dialogs/more-info/controls/more-info-lock.ts)
