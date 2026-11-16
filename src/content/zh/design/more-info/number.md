---
title: 数目
description: 状态行中设备、滑动器或数字字段的多个实体的更多信息视图。
sidebarGroup: 帮助者
sidebarGroup: 助手

---

# 数目 {#number}

Live demo of `ha-demo-more-info`, 连接到一个 demo Home Assistant.

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](https://contributors.home-assistant.io/design/more-info/number/)。

```html
<ha-demo-more-info entity="number.living_room_speaker_bass"></ha-demo-more-info>
```

## 取证结果 {#what-it-shows}

数字实体(number activity)是指一个设备的设置,它占用一个数字,如扬声器的低音或运动传感器的灵敏度. 像[输入编号](/design/more-info/input-number)帮助者一样,他们没有更新的信息设计. 控制器位于对话框顶端的状态行:左侧的图标和名称,右侧的控制器.

集成选择数字模式 :

- ** Slider **: a [幻灯片](/design/components/slider),其旁边有值. 以上客厅扬声器的低音从-10到-10,作为滑动器.
- ** 框**:一个号码[文本输入](/design/components/input),单位在结尾尽可能广泛地显示。
- **Auto**::当范围有有限的步数时的滑动器,当它有太多的步数用滑动器选择时的字段.

在状态行下方,对话框显示实体的历史及其活动. 演示只显示状态行.

## 设计说明 {#design-notes}

- 滑动器和字段使用最小,最大,并步骤设备报告.
- 新值在您放开滑动器或确认字段时发送。
- 当实体不可用时,幻灯片和字段将被禁用。

## 在代码中 {#in-code}

状态行是 `state-card-number` 在 [`src/state-summary/state-card-number.ts`](https://github.com/home-assistant/frontend/blob/dev/src/state-summary/state-card-number.ts) 。 它是否显示滑动器由`showNumberSlider`在[`src/data/number.ts`](https://github.com/home-assistant/frontend/blob/dev/src/data/number.ts)中决定 。 没有 `more-info-number` : 域位在 `DOMAINS_HIDE_DEFAULT_MORE_INFO` [`src/dialogs/more-info/const.ts`](https://github.com/home-assistant/frontend/blob/dev/src/dialogs/more-info/const.ts) 。

来源:[`state-card-number.ts`](https://github.com/home-assistant/frontend/blob/dev/src/state-summary/state-card-number.ts)
