---
title: 属性
description: 附加信息随状态而来,比如光亮度或其支持的效果列表.
sidebarGroup: 实体与设备
term:
  aliases:
  - attributes
  - state attributes
  code:
  - extra_state_attributes
  related:
  - state
  - entity
  autolink:
  - state attribute
  - state attributes
---

# 属性 {#attribute}

- 代码 : `extra_state_attributes`
- 另外:属性、状态属性

属性描述状态,它们不是自己的价值. 用户想在图表中看到的东西,或者在自动化中自己使用的东西,像设备的电池水平一样,作为单独的实体更好.

## 相关条件 {#related-terms}

- [状态](/glossary/state):一个实体的当前值,如`on`,`21.5`,或`playing`,连同其属性.
- [六方会谈](/glossary/entity):有一件事Home Assistant可以显示,测量,或者控制,比如灯光,温度传感器,或者开关. 每个实体都有国家。
