---
title: 设备类
description: 什么是实体衡量或是什么,比如`temperature`或`door`。 它设置图标,单位,以及前端如何显示实体.
sidebarGroup: 实体与设备
term:
  aliases:
  - device classes
  code:
  - device_class
  - SensorDeviceClass
  - BinarySensorDeviceClass
  related:
  - entity
  - state-class
  autolink:
  - device class
  - device classes
---

# 设备类 {#device-class}

- 在代码中:`device_class`,`SensorDeviceClass`,`BinarySensorDeviceClass`
- 另外:设备类

使用 `door` 设备类的二进制传感器显示为打开和关闭而非打开和关闭 。 使用 `temperature` 设备类的传感器得到正确的图标, 并转换到用户选择的单位 。

## 相关条件 {#related-terms}

- [六方会谈](/glossary/entity):有一件事Home Assistant可以显示,测量,或者控制,比如灯光,温度传感器,或者开关. 每个实体都有国家。
- [国家等级](/glossary/state-class):一个传感器的值如何表现,比如`measurement`或`total_increasing`,所以Home Assistant可以为此保持长期的统计数据.
