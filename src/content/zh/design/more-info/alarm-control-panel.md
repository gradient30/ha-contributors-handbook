---
title: 警报控制面板
description: 提醒系统的更多信息视图, 带有垂直选择器用于其武装模式 。
sidebarGroup: 开幕和安全
---

# 警报控制面板 {#alarm-control-panel}

Live demo of `ha-demo-more-info`, 连接到一个 demo Home Assistant.

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](https://contributors.home-assistant.io/design/more-info/alarm-control-panel/)。

```html
<ha-demo-more-info entity="alarm_control_panel.home_alarm"></ha-demo-more-info>
```

## 取证结果 {#what-it-shows}

一个提醒总是完全在一个模式中,所以主控是一个高大的垂直 [选择控件](/design/components/controls):每个模式一个按钮,堆叠,当前一个突出显示. 每个模式都有一个图标和一个短标签,如**Home**,**Away**,**Night**,以及**Disarmed**.

**的学生总是在那里。 其他的学生只有在提醒支持时才会显示:

- ** Home**、**Away**和**Night**。
- ** 评论**。
- ** Custom**,用于自定义绕行。

上面的警报支持家,离,夜,所以它得到四个按钮. 选择器随模式数而增加。

当警报解除,等待,或触发时,没有模式可选择. 选择器为状态的大型图标提供空间,其下方有一个**Disarm**按钮.

## 设计说明 {#design-notes}

- 所选模式取了状态的颜色,所以一个解除的警报看起来很平静,一个武装的警报则突出.
- 当提醒需要代码时, Home Assistant 在更改模式前在单独的对话框中询问它 。 对于武装,它只问 当警报说需要一个代码来武装。 对于解除武器,它总是问警报何时有密码. 存储在实体设置中的代码跳过这个问题 。
- 选择立即移动到新模式。 当更改失败时,例如因为代码错误,它会向后移动.

## 在代码中 {#in-code}

视图为 `more-info-alarm_control_panel` 在 [`src/dialogs/more-info/controls/more-info-alarm_control_panel.ts`](https://github.com/home-assistant/frontend/blob/dev/src/dialogs/more-info/controls/more-info-alarm_control_panel.ts) 。 模式选择器为`ha-state-control-alarm_control_panel-modes`在[`src/state-control/alarm_control_panel/`](https://github.com/home-assistant/frontend/tree/dev/src/state-control/alarm_control_panel)中. 242. 韦斯韦特(签名)

来源:[`more-info-alarm_control_panel.ts`](https://github.com/home-assistant/frontend/blob/dev/src/dialogs/more-info/controls/more-info-alarm_control_panel.ts)
