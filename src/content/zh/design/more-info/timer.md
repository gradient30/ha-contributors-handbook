---
title: 计时器
description: 一个计时器帮助器的更多信息视图,包含实时倒计时,持续时间字段,以及启动,暂停,取消的按钮.
sidebarGroup: 帮助者
---

# 计时器 {#timer}

Live demo of `ha-demo-more-info`, 连接到一个 demo Home Assistant.

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](https://contributors.home-assistant.io/design/more-info/timer/)。

```html
<ha-demo-more-info entity="timer.laundry"></ha-demo-more-info>
<ha-demo-more-info entity="timer.tea"></ha-demo-more-info>
```

## 取证结果 {#what-it-shows}

计时器顶部的状态是倒计时. 当计时器运行时,它会滴滴下来,像**22:52**。 暂停时,添加状态,如**22:52(Paused)**. 当它是闲置的, 它显示 ** 闲置 **。

它下面是一个持续时间场,有小时,分,秒. 它从定时器设置的时间长度开始,在定时器运行时停留在那里,所以不会随倒数跳动. 更改为不同时间启动计时器.

字段下方有一行文本 [按钮](/design/components/button) 持有动作 。 哪些显示取决于状态:

- ** 工期**:开始**,从实地工期开始计时。
- ** 行动**:** 选择在现场重新开始工作,** 暂停**、** 取消** 和** 完成**。
- ** 暂停**:** 选择**、** 开始** 继续**、** 取消** 和** 完成**。

洗衣计时器在运行,所以它得到**Set**,**Pause**,**Cancel**,**Finish**。 茶定时器闲置,所以只能得到**Start**.

## 设计说明 {#design-notes}

- 动作是纯文本按钮,不是大控件. 计时器大约是时间,所以倒计时和场面得到关注.
- 当计时器在对话框打开时完成时,倒计时脉冲会两次,所以即使你不看数字,你也会注意到.
- 计时器可以有预设,在动作下方有一行固定持续时间,以一个水龙头启动计时器. 这些来自实体设置,不是这些演示的一部分。
- 您输入的时间长度鱿鱼会比设定的时间长度长。

## 在代码中 {#in-code}

视图为 `more-info-timer` 在 [`src/dialogs/more-info/controls/more-info-timer.ts`](https://github.com/home-assistant/frontend/blob/dev/src/dialogs/more-info/controls/more-info-timer.ts) 。 预设为`ha-more-info-timer-presets`在[`src/dialogs/more-info/components/timers/`](https://github.com/home-assistant/frontend/tree/dev/src/dialogs/more-info/components/timers)中. 倒计时文本来自`computeDisplayTimer`在[`src/data/timer.ts`](https://github.com/home-assistant/frontend/blob/dev/src/data/timer.ts)中.

来源:[`more-info-timer.ts`](https://github.com/home-assistant/frontend/blob/dev/src/dialogs/more-info/controls/more-info-timer.ts)
