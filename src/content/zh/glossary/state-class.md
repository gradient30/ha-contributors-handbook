---
title: 状态类别
description: "How the value of a sensor behaves, like `measurement` or `total_increasing`, so Home Assistant can keep long-term statistics for it."
sidebarGroup: 实体与设备
term:
  aliases:
  - state classes
  code:
  - state_class
  - SensorStateClass
  related:
  - statistics
  - device-class
  - entity
  autolink:
  - state class
  - state classes
---

# 国家等级 {#state-class}

- 代码:`state_class`,`SensorStateClass`
- 州级课程

没有州级的传感器不会得到[交涉](/glossary/statistics). 能量仪表板只使用有传感器的传感器.

## 相关条件 {#related-terms}

- [B. 长期统计](/glossary/statistics):记录器为长期保存的图和能量仪表板,如平均值、最小值和最大值,或运行总数,每小时汇总传感器值。
- {为实现 [设备类](/glossary/device-class) : 实体衡量或是什么, 如 `temperature` 或 `door` 。 它设置图标,单位,以及前端如何显示实体.
- [六方会谈](/glossary/entity):有一件事Home Assistant可以显示,测量,或者控制,比如灯光,温度传感器,或者开关. 每个实体都有国家。
