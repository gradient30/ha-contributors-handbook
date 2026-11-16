---
title: 国家机器
description: 有利的 Home Assistant Core 中包含每个实体当前状态的部分 。
sidebarGroup: 实体与设备
term:
  code:
  - hass.states
  - StateMachine
  related:
  - state
  - hass
  - event
  autolink:
  - state machine
---

# 国家机器 {#state-machine}

- 代码:`hass.states`,`StateMachine`

集成书写到它,其他所有内容都从它读到:自动化,模板,仪表板. 写作通过实体,而不是直接到国家机器.

## 相关条件 {#related-terms}

- [状态](/glossary/state):一个实体的当前值,如`on`,`21.5`,或`playing`,连同其属性.
- [隐藏对象](/glossary/hass) : `HomeAssistant` 集成得到的例子, 访问状态机器、 事件总线、 动作和配置 。
- 限制因素 瓮: 就这些事件总线上的消息, 例如状态更改或遽按 。 任何代码都可以听到事件.
