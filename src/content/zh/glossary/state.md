---
title: 状态
description: 实体的当前值, 如 `on` 、 `21.5` 或 `playing` 及其属性 。
sidebarGroup: 实体与设备
term:
  aliases:
  - states
  - state object
  code:
  - State
  - hass.states
  - native_value
  related:
  - entity
  - attribute
  - state-machine
  - unavailable
---

# 状态 {#state}

- 在代码中:`State`,`hass.states`,`native_value`
- 另外:状态、状态对象

国家生活在[状态机器](/glossary/state-machine)。 一个状态总是作为字符串存储,即使它是一个数字. 当它改变时, Home Assistant 发射 `state_changed` [事件](/glossary/event) , 录音员写给历史 。

两个州是特殊的:[不详](/glossary/unavailable).

## 相关条件 {#related-terms}

- [六方会谈](/glossary/entity):有一件事Home Assistant可以显示,测量,或者控制,比如灯光,温度传感器,或者开关. 每个实体都有国家。
- [属性](/glossary/attribute): 附加信息随状态而来, 如光亮度或它支持的效果列表.
- {L0促进实现 Home Assistant Core提供关于每个 非实体的状态。
- [不可用莹](/glossary/unavailable):一个实体的特殊状态,但目前Home Assistant无法到达。 其对应的,未知,表示可以达到,但还没有价值.
