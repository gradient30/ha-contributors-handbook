---
title: 查询数据库
description: 读取 Home Assistant 数据库中的状态、事件和上下文的示例 SQL 查询，适用于 SQLite、MariaDB 和 PostgreSQL。
order: 3
---


# 查询数据库 {#query-the-database}
记录器将你家的历史存储在 SQL 数据库中。你可以使用任何 SQL 工具查询它，比如你电脑上的数据库客户端或 JupyterLab 中的笔记本。本页面提供了起始查询示例。

开始之前：

- 阅读 [数据模型](/data/reference/data-model) 和 [数据库模式](/data/reference/database-schema)。表格已经规范化：实体 ID、属性和事件数据存放在各自的表中，因此大多数查询需要使用连接。
- 仅可读取。在 Home Assistant 运行时写入数据库可能会破坏你的历史记录。
- 时间以 Unix 时间戳存储，自 1970 年起的秒数，使用 UTC 时区。下面的查询已将其转换为可读日期。

示例使用 SQLite，这是默认数据库。如果 MariaDB、MySQL 或 PostgreSQL 需要不同函数，会在文中说明。

## 状态 {#states}
### 一个实体的状态 {#the-states-of-one-entity}
```sql
SELECT
  states.state,
  DATETIME(states.last_updated_ts, 'unixepoch', 'localtime') AS updated
FROM states
JOIN states_meta ON states.metadata_id = states_meta.metadata_id
WHERE states_meta.entity_id = 'sensor.living_room_temperature'
ORDER BY states.last_updated_ts DESC
LIMIT 100;
```

在其他数据库中转换时间戳：

- MariaDB 和 MySQL: `FROM_UNIXTIME(states.last_updated_ts)`
- PostgreSQL: `TO_TIMESTAMP(states.last_updated_ts)`

### 仅实际状态更改 {#only-real-state-changes}
每次更新都会写入一个状态行，即使只是属性发生了变化，例如媒体播放器的歌曲或灯的颜色。当状态值本身发生变化时，`last_changed_ts` 与 `last_updated_ts` 相同，为了节省空间，它会以 `NULL` 的形式存储。因此，要获取仅状态值发生变化的行：

```sql
SELECT states_meta.entity_id, states.state, states.last_updated_ts
FROM states
JOIN states_meta ON states.metadata_id = states_meta.metadata_id
WHERE states.last_changed_ts IS NULL;
```

### 填充最后更改时间 {#fill-in-last-changed}
因为当 `last_changed_ts` 等于 `last_updated_ts` 时 `last_changed_ts` 是 `NULL`，所以回退到 `last_updated_ts` 来获取真实值：

```sql
SELECT
  states_meta.entity_id,
  states.state,
  COALESCE(states.last_changed_ts, states.last_updated_ts) AS last_changed_ts
FROM states
JOIN states_meta ON states.metadata_id = states_meta.metadata_id;
```

`COALESCE` 可在 SQLite、MariaDB、MySQL 和 PostgreSQL 中使用。

### 属性 {#attributes}
属性在 `state_attributes` 中存储一次，并被每个具有相同属性的状态行共享：

```sql
SELECT states_meta.entity_id, states.state, state_attributes.shared_attrs
FROM states
JOIN states_meta ON states.metadata_id = states_meta.metadata_id
LEFT JOIN state_attributes
  ON states.attributes_id = state_attributes.attributes_id
WHERE states_meta.entity_id = 'light.kitchen';
```

`shared_attrs` 是一个 JSON 字符串。

### 前一个状态 {#the-previous-state}
每个状态行通过 `old_state_id` 指向它之前的状态：

```sql
SELECT
  states_meta.entity_id,
  old_states.state AS old_state,
  states.state AS new_state,
  states.last_updated_ts
FROM states
JOIN states_meta ON states.metadata_id = states_meta.metadata_id
LEFT JOIN states AS old_states
  ON states.old_state_id = old_states.state_id;
```

## 事件 {#events}
### 所有事件及其数据 {#all-events-with-their-data}
`state_changed` 事件未存储在 `events` 表中：`states` 表中已经有该信息。其他所有事件都已存储。

```sql
SELECT
  events.event_id,
  DATETIME(events.time_fired_ts, 'unixepoch', 'localtime') AS fired,
  event_types.event_type,
  event_data.shared_data
FROM events
LEFT JOIN event_types
  ON events.event_type_id = event_types.event_type_id
LEFT JOIN event_data ON events.data_id = event_data.data_id
ORDER BY events.time_fired_ts DESC
LIMIT 100;
```

### 事件和状态变化一起查看 {#events-and-state-changes-together}
要按顺序查看所有内容，请将两个表结合起来：

```sql
SELECT event_types.event_type, events.time_fired_ts AS fired_ts
FROM events
JOIN event_types ON events.event_type_id = event_types.event_type_id
UNION ALL
SELECT 'state_changed', states.last_updated_ts
FROM states
ORDER BY fired_ts;
```

## 上下文 {#context}
上下文将因一个原因而发生的所有事件联系在一起。ID以二进制值存储。使用 `HEX()` 使其在 SQLite、MariaDB 和 MySQL 中可读。PostgreSQL 会显示其原始形式。

### 状态变化的上下文 {#the-context-of-state-changes}
```sql
SELECT
  states_meta.entity_id,
  states.state,
  HEX(states.context_id_bin) AS context_id,
  HEX(states.context_user_id_bin) AS user_id,
  HEX(states.context_parent_id_bin) AS parent_id
FROM states
JOIN states_meta ON states.metadata_id = states_meta.metadata_id;
```

### 具有相同上下文的所有内容 {#everything-with-the-same-context}
从上一个查询中选择一个上下文 ID，找到所有共享该上下文的事件和状态：

```sql
SELECT 'event', event_types.event_type, events.time_fired_ts
FROM events
JOIN event_types ON events.event_type_id = event_types.event_type_id
WHERE HEX(events.context_id_bin) = '0190A1B2C3D4E5F60718293A4B5C6D7E'
UNION ALL
SELECT 'state', states_meta.entity_id, states.last_updated_ts
FROM states
JOIN states_meta ON states.metadata_id = states_meta.metadata_id
WHERE HEX(states.context_id_bin) = '0190A1B2C3D4E5F60718293A4B5C6D7E';
```

## 统计数据 {#statistics}
具有长期统计的传感器的每小时平均值：

```sql
SELECT
  DATETIME(statistics.start_ts, 'unixepoch', 'localtime') AS hour,
  statistics.mean,
  statistics.min,
  statistics.max
FROM statistics
JOIN statistics_meta ON statistics.metadata_id = statistics_meta.id
WHERE statistics_meta.statistic_id = 'sensor.living_room_temperature'
ORDER BY statistics.start_ts DESC
LIMIT 48;
```

对于能量和其他计量器，请使用 `state` 和 `sum` 来替代 `mean`、`min` 和 `max`。参见 [Statistics](/data/reference/statistics)。
