---
title: 统计
description: 如何 Home Assistant 将传感器数据汇总为 5 分钟和每小时的统计数据，以及这些数据如何存储。
order: 4
---


# 统计 {#statistics}
`states` 表格会精确记录每一次状态变化，但仅保留有限时间：默认 10 天。为了保持更长时间的历史记录，Home Assistant 还会汇总 [统计数据](/glossary/statistics)：按时间段汇总的传感器数值。这些数据驱动能源仪表盘、统计图表卡以及长期历史图表。用户文档在 [长期统计](https://www.home-assistant.io/docs/configuration/long-term-statistics/) 中有详细解释。

## 短期与长期 {#short-term-and-long-term}
- **短期统计** 每 5 分钟汇总一次，基于该时间段的状态。它们会和状态一起被清除。
- **长期统计** 每小时汇总一次，基于该小时的短期统计。它们不会被清除。每个传感器每天 24 行数据，体量够小，可以永久保存。

## 哪些实体会获取统计数据 {#which-entities-get-statistics}
统计数据会为具有[state class](/glossary/state-class)的传感器保存。存储内容取决于该类：

| 状态类 | 示例 | 每周期存储 |
| --- | --- | --- |
| `measurement` | 温度，或当前的功率使用情况。 | `mean`、`min` 和 `max`。 |
| `measurement_angle` | 风向。 | 一个圆形 `mean`，因此 350 度和 10 度的平均为 0，而不是 180。 |
| `total` 或 `total_increasing` | 能源计量器，或水表。 | `state`、`sum` 和 `last_reset_ts`。 |

对于计量器：

- `state` 是该周期结束时传感器的数值。
- `sum` 是自从首次为该传感器编译统计数据以来的累计总量。两个周期的 `sum` 之差就是中间使用量，即使计量器在此期间被重置。
- `last_reset_ts` 是计量器上一次开始新周期的时间（如果已知）。集成如何为其传感器启用统计的说明见 [传感器实体](/core/entities/sensor#long-term-statistics)。

统计数据也可以从外部来源导入，例如能源供应商的历史数据。它们在 ID 中使用 `:` 而不是 `.`，例如 `energy_provider:electricity_import`。

## 表格 {#the-tables}
### `statistics_meta` {#statisticsmeta}
每行代表一个统计数据，描述它是什么。

| 列 | 类型 | 含义 |
| --- | --- | --- |
| `id` | 整数，主键 | 数据表使用的ID。 |
| `statistic_id` | 字符串 | 对于实体，实体ID；对于导入的统计数据，类似 `domain:name` 的ID。重命名实体会更新它。 |
| `source` | 字符串 | 数据来源：实体为 `recorder`，或导入它的集成域。 |
| `unit_of_measurement` | 字符串 | 统计数据的单位。 |
| `unit_class` | 字符串 | 单位类型，例如 `energy` 或 `temperature`，用于单位之间的转换。 |
| `mean_type` | 整数 | `0` 表示无平均值，`1` 表示普通平均值，`2` 表示循环平均值。 |
| `has_sum` | 布尔值 | 统计数据是否有 `sum`。 |
| `name` | 字符串 | 名称，主要用于导入的统计数据。 |还有一列 `has_mean`，它正被 `mean_type` 取代。

### `statistics` 和 `statistics_short_term` {#statistics-and-statisticsshortterm}
两个表都有相同的列。`statistics` 每小时保存一行，`statistics_short_term` 每 5 分钟保存一行。

| 列 | 类型 | 说明 |
| --- | --- | --- |
| `id` | 整数，主键 | 该行的ID。 |
| `metadata_id` | 整数，引用 `statistics_meta` | 哪个统计值。 |
| `start_ts` | 时间戳 | 该时间段的起始时间。 |
| `created_ts` | 时间戳 | 该行写入的时间。 |
| `mean` | 数字 | 时间加权平均值。 |
| `mean_weight` | 数字 | 用于组合循环平均的权重。 |
| `min` | 数字 | 该时间段的最小值。 |
| `max` | 数字 | 该时间段的最大值。 |
| `state` | 数字 | 对于计量器：该时间段结束时的值。 |
| `sum` | 数字 | 对于计量器：累积总和。 |
| `last_reset_ts` | 时间戳 | 对于计量器：最后一个周期开始的时间。 |每个表在 `metadata_id` 上都有一个 `start_ts` 索引。

### `statistics_runs` {#statisticsruns}
跟踪哪些时间段的统计数据已经被编译过，这样不会重复编译，同时在重启后补上错过的时间段。

| 列 | 类型 | 说明 |
| --- | --- | --- |
| `run_id` | 整数，主键 | 此行的 ID。 |
| `start` | 日期和时间 | 已编译时间段的开始时间。 |

## 可以查看统计数据的地方 {#where-you-see-statistics}
- [历史记录](https://www.home-assistant.io/integrations/history/) 面板，用于查看比保存状态更久的时间段。
- [统计图表卡片](https://www.home-assistant.io/dashboards/statistics-graph/) 和 [统计卡片](https://www.home-assistant.io/dashboards/statistic/)。
- [能源仪表板](https://www.home-assistant.io/docs/energy/)。
- `recorder.get_statistics` 动作，可在脚本和自动化中使用它们。
