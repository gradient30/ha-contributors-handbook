---
title: 平台
description: 一个集成是如何提供一类实体的,比如Hue集成的`light`平台. 也用于集成平台,插入另一个集成的文件.
sidebarGroup: 核心和一体化
term:
  aliases:
  - platforms
  - entity platform
  - integration platform
  code:
  - Platform.LIGHT
  - light.py
  related:
  - integration
  - entity
  - domain
  autolink:
  - entity platform
  - integration platform
---

# 平台 {#platform}

- 代码:`Platform.LIGHT`,`light.py`
- 另外:平台,实体平台,集成平台.

**实体平台**是提供一种类型实体的整合的一部分。 胡埃集成有一个 `light.py` 用于它的灯光和 `sensor.py` 用于它的传感器:它的 `light` 和 `sensor` 平台 。

一个**整合平台**是一个让集成插件插到另一个集成平台的文件,比如`diagnostics.py`用于[诊断](/glossary/diagnostics)或`repairs.py`修复.

## 相关条件 {#related-terms}

- [一体化](/glossary/integration):将Home Assistant连接到设备,服务,或协议,或添加自动化等特性的代码包.
- [六方会谈](/glossary/entity):有一件事Home Assistant可以显示,测量,或者控制,比如灯光,温度传感器,或者开关. 每个实体都有国家。
- [域名](/glossary/domain):一个集成的短而独特的标识符,如`hue`或`light`. 它也是每个实体身份证的第一部分。
