---
title: 录音机
description: 将国家历史和事件记录在一个数据库中的整合。
sidebarGroup: 数据
term:
  aliases:
  - database
  code:
  - recorder
  - home-assistant_v2.db
  related:
  - statistics
  - state
  - event
  autolink:
  - recorder
---

# 录音机 {#recorder}

- 代码:`recorder`,`home-assistant_v2.db`
- 此外:数据库

历史图表,日志,长期统计都从记录者数据库读取. 默认它保存了十天的历史.

## 相关条件 {#related-terms}

- [B. 长期统计](/glossary/statistics):记录器为长期保存的图和能量仪表板,如平均值、最小值和最大值,或运行总数,每小时汇总传感器值。
- [状态](/glossary/state):一个实体的当前值,如`on`,`21.5`,或`playing`,连同其属性.
- 限制因素 瓮: 就这些事件总线上的消息, 例如状态更改或遽按 。 任何代码都可以听到事件.
