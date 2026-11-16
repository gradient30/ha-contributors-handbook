---
title: 协调员
description: 一个同时为许多实体获取数据的帮助者,在一个时刻表上,所以一个设备或API被询问一次而不是每个实体一次.
sidebarGroup: 核心和一体化
term:
  aliases:
  - data update coordinator
  - update coordinator
  code:
  - DataUpdateCoordinator
  - CoordinatorEntity
  related:
  - polling
  - entity
  - unavailable
  autolink:
  - data update coordinator
---

# 协调员 {#coordinator}

- 代码:`DataUpdateCoordinator`,`CoordinatorEntity`
- 另外:数据更新协调员,更新协调员

在有新数据时,从协调员处获得数据的实体一起更新数据。 协调员还在一个地方处理错误: 获取失败时, 其实体变为 [无](/glossary/unavailable) 。

## 相关条件 {#related-terms}

- [投票](/glossary/polling):询问设备或服务在一个间隔上的新数据. 与此相反的是推,当某事发生变化时设备会在那里发送更新.
- [六方会谈](/glossary/entity):有一件事Home Assistant可以显示,测量,或者控制,比如灯光,温度传感器,或者开关. 每个实体都有国家。
- [不可用莹](/glossary/unavailable):一个实体的特殊状态,但目前Home Assistant无法到达。 其对应的,未知,表示可以达到,但还没有价值.
