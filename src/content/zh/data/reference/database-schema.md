---
title: 数据库模式
description: 记录器数据库的表格，它们包含的内容，以及它们如何连接。
order: 3
---


# 数据库模式 {#database-schema}
[recorder](/glossary/recorder) 集成将 Home Assistant 的历史存储在 SQL 数据库中。默认情况下，这是配置文件夹中的一个名为 `home-assistant_v2.db` 的 SQLite 文件。它也可以是 MariaDB、MySQL 或 PostgreSQL。如何设置以及数据保存多长时间，请参阅 [recorder 文档](https://www.home-assistant.io/integrations/recorder/)。

模式会随时间变化。当模式变化时，Home Assistant 会在更新期间自动迁移数据库。本页面描述的是模式版本 53。权威来源是核心中的 [`db_schema.py`](https://github.com/home-assistant/core/blob/dev/homeassistant/components/recorder/db_schema.py)。

> [!注意]
> 一些表仍然保留旧模式版本的列，例如 `states` 中的 `entity_id` 或 `events` 中的 `event_type`。这些列不再填充，并且在本页面中未列出。请使用此处列出的列。

## 概述 {#overview}
| 表 | 包含内容 |
| --- | --- |
| `states` | 每个实体状态更新的一行。 |
| `states_meta` | 实体ID，只存储一次。 |
| `state_attributes` | 状态的属性，每个唯一集合只存储一次。 |
| `events` | 每个事件一行，`state_changed` 除外。 |
| `event_types` | 事件类型，只存储一次。 |
| `event_data` | 事件的数据，每个唯一集合只存储一次。 |
| `statistics` | 每小时统计数据。 |
| `statistics_short_term` | 每5分钟统计数据。 |
| `statistics_meta` | 每个统计数据的内容。 |
| `statistics_runs` | 已编制统计数据的时间段。 |
| `recorder_runs` | 记录器每次启动和停止的时间。 |
| `schema_changes` 和 `migration_changes` | 模式迁移的历史记录。仅适用于 Home Assistant 本身。 |经常重复出现的值，如实体 ID、属性和事件类型，会存放在它们自己的表中，并通过 ID 引用。这能大大减少数据库的大小，但意味着大多数查询需要进行连接。有关示例，请参阅 [查询数据库](/data/guides/query-the-database)。

所有以 `_ts` 结尾的时间戳都是以秒为单位的 Unix 时间戳，使用 UTC，存储为浮点数。以 `_bin` 结尾的上下文 ID 是 16 字节的二进制数据。

## 州 {#states}
### `states` {#states-1}
| 列 | 类型 | 说明 |
| --- | --- | --- |
| `state_id` | 整数，主键 | 本行的ID。 |
| `metadata_id` | 整数，引用`states_meta` | 哪个实体。 |
| `state` | 字符串，最多255个字符 | 状态值。 |
| `last_updated_ts` | 时间戳 | 状态或其属性上次更改的时间。 |
| `last_changed_ts` | 时间戳 | 状态值上次更改的时间。`NULL` 当它与`last_updated_ts` 相同时。 |
| `last_reported_ts` | 时间戳 | 集成上次报告状态的时间。`NULL` 当它与`last_updated_ts` 相同时。 |
| `old_state_id` | 整数，引用`states` | 此实体的先前状态。 |
| `attributes_id` | 整数，引用`state_attributes` | 属性。 |
| `context_id_bin` | 二进制 | 更改的上下文。 |
| `context_user_id_bin` | 二进制 | 发起用户（如果已知）。 |
| `context_parent_id_bin` | 二进制 | 父上下文（如果有）。 |
| `origin_idx` | 整数 | 变更来源：`0` 表示本地，`1` 表示远程。 |

索引：`metadata_id` 使用 `last_updated_ts`，以及 `context_id_bin`。

### `states_meta` {#statesmeta}
| 列 | 类型 | 说明 |
| --- | --- | --- |
| `metadata_id` | 整数，主键 | `states` 使用的 ID。 |
| `entity_id` | 字符串 | 实体 ID，例如 `light.kitchen`。 |

当实体被重命名时，此处的行会被更新，因此其历史会随之移动。

### `state_attributes` {#stateattributes}
| 列 | 类型 | 说明 |
| --- | --- | --- |
| `attributes_id` | 整数，主键 | `states` 使用的 ID。 |
| `hash` | 整数 | 属性的哈希值，用于快速查找重复项。 |
| `shared_attrs` | 文本 | 属性，以 JSON 格式。 |

## 事件 {#events}
### `events` {#events-1}
| 列 | 类型 | 描述 |
| --- | --- | --- |
| `event_id` | 整数，主键 | 该行的ID。 |
| `event_type_id` | 整数，引用`event_types` | 事件的类型。 |
| `data_id` | 整数，引用`event_data` | 事件的数据。 |
| `time_fired_ts` | 时间戳 | 事件触发的时间。 |
| `origin_idx` | 整数 | 事件来源：`0`表示本地，`1`表示远程。 |
| `context_id_bin` | 二进制 | 事件的上下文。 |
| `context_user_id_bin` | 二进制 | 启动事件的用户（如果已知）。 |
| `context_parent_id_bin` | 二进制 | 父上下文（如果有）。 |

索引：`event_type_id` 使用 `time_fired_ts`，以及 `context_id_bin`。

`state_changed` 事件不在此表中。`states` 表包含它们的所有信息，其 `last_updated_ts` 是事件触发的时间。

### `event_types` {#eventtypes}
| 列 | 类型 | 描述 |
| --- | --- | --- |
| `event_type_id` | 整数，主键 | `events` 使用的 ID。 |
| `event_type` | 字符串 | 事件类型，例如 `automation_triggered`。 |

### `event_data` {#eventdata}
| 列 | 类型 | 描述 |
| --- | --- | --- |
| `data_id` | 整数，主键 | `events` 使用的 ID。 |
| `hash` | 整数 | 数据的哈希，用于快速查找重复项。 |
| `shared_data` | 文本 | 事件数据，格式为 JSON。 |

## 录制器运行 {#recorder-runs}
### `recorder_runs` {#recorderruns}
每次 Home Assistant 启动时，记录器都会开始一次新的运行。运行在 Home Assistant 关闭时结束。当你分析数据时，这可以告诉你 Home Assistant 何时未在运行，因此你不会把数据缺口误认为是没有变化的时期。

| 列 | 类型 | 说明 |
| --- | --- | --- |
| `run_id` | 整数，主键 | 运行的ID。 |
| `start` | 日期和时间 | 运行开始时间。 |
| `end` | 日期和时间 | 运行结束时间。 |
| `closed_incorrect` | 布尔值 | Home Assistant 是否在未正常关闭的情况下停止。 |
| `created` | 日期和时间 | 行创建时间。 |当 `closed_incorrect` 为真时，Home Assistant 未能干净地关闭，而 `end` 被设置为它再次启动的时间。那可能是几分钟或几天之后，因此在这种情况下不要信任 `end`。运行的最后事件或状态变化是判断它真正停止时间的更好依据。

## 统计 {#statistics}
统计表在它们自己的页面上进行了描述: [统计](/data/reference/statistics)。
