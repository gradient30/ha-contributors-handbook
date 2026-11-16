---
title: 书记官处
description: Where Home Assistant 保存它所知道的关于实体,设备,区域,地板和标签的内容,以及用户对他们的改变.
sidebarGroup: 实体和装置
term:
  aliases:
  - registries
  - entity registry
  - device registry
  code:
  - er.async_get
  - dr.async_get
  - entity_registry
  - device_registry
  related:
  - unique-id
  - device
  - area
  - label
  autolink:
  - entity registry
  - device registry
  - area registry
---

# 书记官处 {#registry}

- 在代码中:`er.async_get`,`dr.async_get`,`entity_registry`,`device_registry`
- 登记册、实体登记册、装置登记册

每个登记册各有一个:实体登记册、设备登记册、区域登记册等等。 它们被存储在 `.storage` 中, 在重新启动中幸存 。

用户的变更在登记册中直播,而不是在集成中。 当用户重命名一个实体时,整合不需要知道.

## 相关条件 {#related-terms}

- [独一无二的ID](/glossary/unique-id):一个集成给一个实体或配置项的ID,它永远不会改变,所以Home Assistant在重启后承认它.
- [设备](/glossary/device):一个物理设备,或一种服务,一个一个或多个实体属于它,就像一个带有温度传感器和湿度传感器的恒温器.
- 目 录 [区域](/glossary/area):  那我们家的房子或空间, 和厨房一样, 是设备和实体的。
- [标签](/glossary/label):一个标签用户在实体,设备,区域,自动化,等等上,将它们自己的方式分组,就像所有使用大量能量的东西.
