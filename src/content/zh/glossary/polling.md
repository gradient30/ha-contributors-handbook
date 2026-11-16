---
title: 投票
description: 询问设备或服务在间隔上的新数据 。 与此相反的是推,当某事发生变化时设备会在那里发送更新.
sidebarGroup: 核心与集成
term:
  aliases:
  - poll
  - push
  code:
  - should_poll
  - SCAN_INTERVAL
  - update_interval
  related:
  - coordinator
  - iot-class
  autolink:
  - polling
---

# 投票 {#polling}

- 在代码中:`should_poll`,`SCAN_INTERVAL`,`update_interval`
- 还有:民意测验,推

推力较快,对设备和网络的负载较少,因此在设备支持时集成使用. 否则,一个[协调员](/glossary/coordinator)投票在一个固定的间隔。

## 相关条件 {#related-terms}

- [协调员](/glossary/coordinator):一个在时间表上一次为许多实体获取数据的帮助者,所以一个设备或API被询问一次而不是每个实体一次.
- [IOT 类](/glossary/iot-class):整合如何获得其数据:本地或从云,通过投票或推. 设于表里.
