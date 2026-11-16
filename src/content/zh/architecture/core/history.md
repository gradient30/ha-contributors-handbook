---
title: 历史与统计
description: 记录器如何将每个状态变化写入数据库，以及历史、日志册和长期统计如何将其读回。
order: 11
---


# 历史与统计 {#history-and-statistics}
在Home Assistant中发生的所有事情都可以回顾：门何时打开，昨天的温度多么温暖，上个月房子使用了多少能量。[记录器](/glossary/recorder)使这一切成为可能。它将状态和事件写入数据库，并且其他集成可以读取这些数据。

## 简而言之 {#in-short}
- 记录器在自己的线程中运行，因此写入数据库从不会阻塞[事件循环](/core/internals/asyncio)。
- 它存储每一次状态变化和事件，默认情况下保存10天。
- 对于具有[状态类别](/glossary/state-class)的传感器，它还会保存统计数据：五分钟汇总保存与历史长度相同，小时汇总长期保存。
- 历史图表、日志簿和能量仪表盘都从记录器的数据库中读取数据。

## 记录器 {#the-recorder}
记录器监听事件总线上的每一个事件，并每隔 5 秒将其批量写入数据库。默认情况下，它使用 SQLite 数据库，在配置文件夹中是一个名为 `home-assistant_v2.db` 的文件。也支持 MariaDB、MySQL 和 PostgreSQL，详见 [ADR-0018](https://github.com/home-assistant/architecture/blob/master/adr/0018-supported-databases.md)。

状态及其属性是分开存储的，相同的属性只存储一次。即使同一盏灯每天多次报告相同的属性，这也能保持数据库小巧。

每晚，记录器会删除比 `purge_keep_days` 更早的数据，默认是 10 天。

## 统计数据 {#statistics}
十天的历史数据不足以将这个冬季与上一个冬季进行比较，而且如果永久保存每一次状态变化，会占满硬盘。统计数据解决了这个问题。对于每个具有状态类别的传感器，记录器会编译：

- **短期统计**，每五分钟一次：平均值、最小值和最大值，电表则为总和。这些数据会随历史数据一同清理。
- **长期统计**，每小时一次，永久保存。

没有状态类别的传感器则没有任何统计数据。这就是状态类别对传感器非常重要的原因，也是为什么能源仪表板只适用于具有状态类别的传感器。

## 谁会读取它 {#who-reads-it}
| 集成 | 显示内容 |
| --- | --- |
| `history` | 随时间变化的状态，用于图表 |
| `logbook` | 发生了什么，用文字表示：“前门已打开” |
| `energy` | 能耗和产能，来自长期统计 |

## 不要记录的内容 {#what-not-to-record}
并非所有内容都适合放入数据库。那些经常变化的属性，或者体积大的属性，比如所有支持效果的列表，会使数据库迅速膨胀。实体可以使用 `_unrecorded_attributes` 来省略属性，而实体类型则对从不变化的属性采取相同的做法。

用户可以在他们的配置中排除整个实体。

## 在代码中 {#in-the-code}
| 什么 | 位置 |
| --- | --- |
| 记录器 | [`homeassistant/components/recorder/`](https://github.com/home-assistant/core/tree/dev/homeassistant/components/recorder) |
| 数据库表 | 记录器中的 `db_schema.py` |
| 统计编译 | 记录器中的 `statistics.py` |
| 历史和日志簿 | [`homeassistant/components/history/`](https://github.com/home-assistant/core/tree/dev/homeassistant/components/history), [`homeassistant/components/logbook/`](https://github.com/home-assistant/core/tree/dev/homeassistant/components/logbook) |

## 进行这些工作 {#work-on-this}
- 新接触 Core？从 [你对 Core 的第一次贡献](/core/first-contribution) 开始。
- [传感器实体](/core/entities/sensor)：状态类，决定传感器是否获取统计数据。
- 想查看自己家的数据？在数据区域 [探索你自己的数据](/data/guides/explore-your-data)。
