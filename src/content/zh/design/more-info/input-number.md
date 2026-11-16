---
title: 输入编号
description: 状态行中的数字帮助器、滑动器或数字字段的更多信息视图。
sidebarGroup: 帮助者
---

# 输入编号 {#input-number}

Live demo of `ha-demo-more-info`, 连接到一个 demo Home Assistant.

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](https://contributors.home-assistant.io/design/more-info/input-number/)。

```html
<ha-demo-more-info entity="input_number.comfort_temperature"></ha-demo-more-info>
<ha-demo-more-info entity="input_number.vacation_days"></ha-demo-more-info>
```

## 取证结果 {#what-it-shows}

一个数字帮助器(`input_number`)没有更新的更多信息设计. 它的控制生活在对话框顶端的状态行:左边的图标和名称,右边的控制.

控件遵循辅助器上的显示模式设置 :

- ** 滑翔机**:一个[幻灯片](/design/components/slider),其值和旁边的单位. 舒适温度采用滑动器,步数为0.5,从15°C到25°C.
- **输入字段**:数字[文本输入](/design/components/input),末端为单位. 休假日使用田园.

在状态行下方,对话框显示帮助者的历史及其活动,就像它对于任何没有自己视图的实体一样. 这些演示只显示状态行.

## 设计说明 {#design-notes}

- 滑动器和字段使用帮助器的最小,最大,和步骤.
- 新的值是当您放开滑动器时,或者当您确认字段时,而不是在每个键盘上发送的.
- 当帮助器无法使用时,滑动器和字段将被禁用.
- [编号](/design/more-info/number) [编号](/design/more-info/number)} 工具的單位( [编号](/design/more-info/number) ) 和 工具的單位( [编号](/design/more-info/number) ) , 取同列, 并列, 并列, 并列 。

## 在代码中 {#in-code}

状态行是 `state-card-input_number` 在 [`src/state-summary/state-card-input_number.ts`](https://github.com/home-assistant/frontend/blob/dev/src/state-summary/state-card-input_number.ts) 。 没有 `more-info-input_number` : 域在 `DOMAINS_HIDE_DEFAULT_MORE_INFO` [`src/dialogs/more-info/const.ts`](https://github.com/home-assistant/frontend/blob/dev/src/dialogs/more-info/const.ts) 中, 所以对话框只显示行和历史 。

来源:[`state-card-input_number.ts`](https://github.com/home-assistant/frontend/blob/dev/src/state-summary/state-card-input_number.ts)
