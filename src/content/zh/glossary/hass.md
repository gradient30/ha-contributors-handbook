---
title: hass 对象
description: '`HomeAssistant` 集成得到的例子, 访问状态机器、 事件总线、 动作和配置 。'
sidebarGroup: 核心与集成
term:
  aliases:
  - hass
  code:
  - HomeAssistant
  - hass
  related:
  - state-machine
  - event
  - action
  - event-loop
  autolink:
  - hass object
---

# 隐藏对象 {#the-hass-object}

- 代码:`HomeAssistant`,`hass`
- ئ 芦馅倡 genome茁萌苟 Rafael洙的

Home Assistant Core中几乎每个函数都以`hass`作为第一个参数.  哎,这是代码如何到达其他的:`hass.states`、`hass.bus`、`hass.services`和`hass.config`。

`hass` 你必须用代码来命名。 在文字中,写 你必须写Home Assistant.

## 相关条件 {#related-terms}

- {L0促进实现 Home Assistant Core提供关于每个 非实体的状态。
- 限制因素 瓮: 就这些事件总线上的消息, 例如状态更改或遽按 。 任何代码都可以听到事件.
- [行动](/glossary/action):有些事情Home Assistant可以做,比如打开灯或者发送通知. 自动化,脚本,和仪表板执行动作.
- [事件循环](/glossary/event-loop):运行Home Assistant Core的星环. 代码屏蔽它, 就像在网络上等待没有`await`, 停止其他一切。
