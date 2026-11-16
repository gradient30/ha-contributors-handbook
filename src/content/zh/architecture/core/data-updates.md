---
title: 获取数据
description: 集成如何通过推送或轮询从设备和服务获取新数据，以及协调器如何保持这一过程的高效。
order: 9
---


# 获取数据 {#getting-data}
一个集成必须知道设备上何时发生了变化：灯通过其自身的开关被打开，温度上升。有两种方法可以发现这一点，而区别对于集成的速度和轻量性非常重要。

本页面是概览。如何构建它，以及代码示例，请参见核心和集成部分的 [获取数据](/core/integrations/fetching-data) 。

## 简而言之 {#in-short}
- **推送**：当某些内容发生变化时，设备或服务会通知 Home Assistant。快速，并且在没有事件发生时不产生任何费用。当设备支持时使用它。
- **轮询**：Home Assistant 按间隔请求新数据。简单，但较慢，并且会增加设备和网络的负载。
- **协调器** 会为设备的所有实体获取数据，然后分发给它们。大多数轮询集成都使用一个协调器。
- 当获取失败时，实体会变为 [不可用](/glossary/unavailable)。它们从不显示虚构或过时的值。

## 推送或轮询 {#push-or-poll}
使用推送时，集成保持连接打开，或监听消息，并在有新的内容到达时写入实体的新状态。推送集成的 [IoT 类](/glossary/iot-class) 是 `local_push` 或 `cloud_push`。

当设备只能被询问时，Home Assistant 会按计划进行询问。单独轮询每个实体是浪费的，当它们都来自同一设备时：一个有十个传感器的设备会被询问十次以获取相同的数据。

## 协调器 {#the-coordinator}
`DataUpdateCoordinator` 会在每个时间间隔获取整个设备或账户的数据，并在有新数据时通知其实体。实体从协调器读取数据，它们自己不会进行获取。它还将错误处理集中在一个地方：当获取失败时，其所有实体将不可用，直到下次成功；登录问题会启动 [重新认证](/glossary/reauthentication) 流程。

协调器也适用于推送：接收数据的集成可以将数据交给协调器，实体以相同的方式更新。

## 做一个好邻居 {#being-a-good-neighbor}
尽可能少进行轮询，限制同时运行的请求数量，以及在每次尝试时只记录一次中断都是[集成质量标准](/glossary/quality-scale)的规则。请参见[适当的轮询](/core/quality-scale/appropriate-polling)、[并行更新](/core/quality-scale/parallel-updates)和[不可用时只记录一次](/core/quality-scale/log-when-unavailable)。

## 在代码中 {#in-the-code}
| 内容 | 位置 |
| --- | --- |
| `DataUpdateCoordinator`, `CoordinatorEntity`, `UpdateFailed` | [`homeassistant/helpers/update_coordinator.py`](https://github.com/home-assistant/core/blob/dev/homeassistant/helpers/update_coordinator.py) |
| 轮询, `SCAN_INTERVAL`, `PARALLEL_UPDATES` | [`homeassistant/helpers/entity_platform.py`](https://github.com/home-assistant/core/blob/dev/homeassistant/helpers/entity_platform.py) |

## 待做事项 {#work-on-this}
- 新加入 Core？先从[你在 Core 的第一次贡献](/core/first-contribution)开始。
- [获取数据](/core/integrations/fetching-data)：推送、轮询和协调器，附带代码。
- [更新状态](/core/entities/state-updates)：实体如何写入其新状态。
