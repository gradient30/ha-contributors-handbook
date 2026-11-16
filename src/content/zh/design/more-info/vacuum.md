---
title: 真空
description: 我们必须从一个机器人真空中获取更多的信息,其中包含一个动画状态图和一行命令按钮.
sidebarGroup: 应用程序
sidebarGroup: 家电

---

# 真空 {#vacuum}

Live demo of `ha-demo-more-info`, 连接到一个 demo Home Assistant.

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](https://contributors.home-assistant.io/design/more-info/vacuum/)。

```html
<ha-demo-more-info entity="vacuum.robot_vacuum"></ha-demo-more-info>
```

## 取证结果 {#what-it-shows}

机器人真空大多靠自己运行. 你不引导它,你发送它的命令。 因此,这个视图的主要部分不是滑动器或开关,而是机器人显示它在做什么的图片,下面有一行命令按钮.

图片是机器人真空的图画,从上面可以看到. 它随状态而变化:它在清洗时会移动和刷子旋转,在对接,返回,暂停,或出现错误时看起来不同. 则取州色. 当有人要求其系统减少运动时,画面就静止不动.

图片下方的 [控制按钮](/design/components/controls) 组持有命令 。 每个都只显示真空支撑它:

- ** 开始**或**暂停**,在一个按钮中,在两者之间切换。
- 页:1
- ** 回国**。
- {\fn华文楷体\fs16\1cHE0E0E0}让机器人鸣叫
- ** 净点**。

在按钮下方,一行持有次要设置:一个**Fan速度**菜单,和一个**Cleaning:按区域**键,用于真空,可以清理特定区域. 这个按钮打开了一个视图 在那里你选择区域清理。

最上面的状态显示真空报告的状况,当它报告一个。 在时间旁边,当设备有电池传感器时,它会显示电池电位,带有图标. 上面的真空被对接并充电

## 设计说明 {#design-notes}

- 现在没有道理的按钮被禁用。 逍遥的真空被关闭,所以**停止**是灰色的。 已经回到家的真空不能再被送回家
- 不报告状态的老真空会得到一个合并的开始和暂停按钮,并带有播放和暂停图标.
- 电池来自同一个设备的电池 但现在不是来自真空实体本身 当设备有充电传感器时,图标也会显示这一点.

## 在代码中 {#in-code}

视图为 `more-info-vacuum` 在 [`src/dialogs/more-info/controls/more-info-vacuum.ts`](https://github.com/home-assistant/frontend/blob/dev/src/dialogs/more-info/controls/more-info-vacuum.ts) 。 图片为 `ha-state-control-vacuum-status` 在 [`src/state-control/vacuum/`](https://github.com/home-assistant/frontend/tree/dev/src/state-control/vacuum) 。 按区域显示的干净度在 [`src/dialogs/more-info/components/vacuum/`](https://github.com/home-assistant/frontend/tree/dev/src/dialogs/more-info/components/vacuum) 。 `VacuumEntityFeature` enum 和 `canReturnHome` 这样的助手在 [`src/data/vacuum.ts`](https://github.com/home-assistant/frontend/blob/dev/src/data/vacuum.ts) 中 。

来源:[`more-info-vacuum.ts`](https://github.com/home-assistant/frontend/blob/dev/src/dialogs/more-info/controls/more-info-vacuum.ts)
