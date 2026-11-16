---
title: B. 长期统计
description: 小时总结感应值,如记录器长期保存的平均值、最小值和最大值,或运行总量,用于图表和能量仪表板。
sidebarGroup: 数据
term:
  aliases:
  - statistics
  - LTS
  code:
  - statistics
  - state_class
  related:
  - recorder
  - state-class
  autolink:
  - long-term statistics
---

# B. 长期统计 {#long-term-statistics}

- 代码:`statistics`,`state_class`
- 此外:统计,长期技术服务

Home Assistant 用 [州级](/glossary/state-class) 保存每个传感器的统计数据 。 与历史不同的是,它们十天后不被清理. 5分钟的总结也保留下来,但只保留历史。

## 相关条件 {#related-terms}

- [录音机](/glossary/recorder) : 将州史和事件的历史存储在一个数据库中的整合 。
- [国家等级](/glossary/state-class):一个传感器的值如何表现,比如`measurement`或`total_increasing`,所以Home Assistant可以为此保持长期的统计数据.
