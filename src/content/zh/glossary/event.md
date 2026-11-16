---
title: 积极地濑子事件
description: 事件总线上的一条消息说发生了一些事情,比如状态变化或者按按钮. 任何代码都可以听到事件.
sidebarGroup: 实体和装置
term:
  aliases:
  - events
  - event bus
  code:
  - hass.bus
  - EVENT_STATE_CHANGED
  - EventEntity
  related:
  - state-machine
  - trigger
  - hass
  autolink:
  - event bus
---

# 积极地濑子事件 {#event}

- 在代码中:`hass.bus`,`EVENT_STATE_CHANGED`,`EventEntity`
- 此外:活动、活动总线

Home Assistant许多事情的火灾事件: 状态改变, 动作正在进行,Home Assistant开始。 自动化可以触发它们.

不可与事件实体混淆: `event` 类型的实体, 显示设备上发生的最后一件事, 如按键 。

## 相关条件 {#related-terms}

- {L0促进实现 Home Assistant Core提供关于每个 非实体的状态。
- [触发](/glossary/trigger):什么开始一个自动化,像状态变化,时间,或者事件.
- [隐藏对象](/glossary/hass) : `HomeAssistant` 集成得到的例子, 访问状态机器、 事件总线、 动作和配置 。
