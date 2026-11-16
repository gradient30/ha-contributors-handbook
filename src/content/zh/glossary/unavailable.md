---
title: 不可用莹
description: 一个虱子 Home Assistant 现在无法到达的实体的特殊状态 。 其对应的,未知,表示可以达到,但还没有价值.
sidebarGroup: 实体和装置
term:
  aliases:
  - unknown
  code:
  - STATE_UNAVAILABLE
  - STATE_UNKNOWN
  - available
  related:
  - state
  - coordinator
---

# 不可用莹 {#unavailable}

- 在代码中:`STATE_UNAVAILABLE`,`STATE_UNKNOWN`,`available`
- 还:未知

当设备离线或 API 失败时, 集成标记其实体为不可用, 设置 `available` 到 `False` 。 它从来没有报告一个化妆值代替。

## 相关条件 {#related-terms}

- [状态](/glossary/state):一个实体的当前值,如`on`,`21.5`,或`playing`,连同其属性.
- [协调员](/glossary/coordinator):一个在时间表上一次为许多实体获取数据的帮助者,所以一个设备或API被询问一次而不是每个实体一次.
