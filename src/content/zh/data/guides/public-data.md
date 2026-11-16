---
title: 使用公共数据
description: 将分析数据集以 JSON 格式下载，或使用 Prometheus 抓取它们，并创建你自己的图表。
order: 1
---


# 使用公共数据 {#use-the-public-data}
在 [analytics.home-assistant.io](https://analytics.home-assistant.io/) 上的所有内容也可以作为数据文件获取，任何人都可以免费使用。它们只包含汇总数据，从不包含单个安装的数据。每次分析处理时，文件都会重新生成。

## 数据集 {#the-data-sets}
| 文件 | 内容 |
| --- | --- |
| [`/data.json`](https://analytics.home-assistant.io/data.json) | 所有内容：`current` 下的当前总数，以及 `history` 下的历史数据。 |
| [`/current_data.json`](https://analytics.home-assistant.io/current_data.json) | 仅包含当前总数。从这里开始。 |
| [`/custom_integrations.json`](https://analytics.home-assistant.io/custom_integrations.json) | 有多少安装使用每个自定义集成，以及使用的版本。 |
| [`/addons.json`](https://analytics.home-assistant.io/addons.json) | 有多少安装使用每个应用，以及使用的版本。文件名仍然使用应用的旧名称。 |

## 当前总计包含的内容 {#what-the-current-totals-contain}
`current_data.json` 包含以下内容，除此之外还有其他内容：- `active_installations`：过去60天内报告的安装数量。
- `installation_types`：按安装类型划分的安装数量。
- `versions`：按Home Assistant版本划分的安装数量。
- `countries`：按国家代码划分的安装数量。
- `integrations`：按集成域划分的安装数量。
- `operating_system`和`supervisor`：主板、操作系统版本和架构。
- `avg_automations`、`avg_integrations`、`avg_states`、`avg_users`和`avg_addons`：共享统计数据的安装的平均值。
- `reports_integrations`、`reports_addons`和`reports_statistics`：有多少安装共享使用数据和统计数据。使用这些，而不是`active_installations`，来计算集成、应用或数量的百分比。
- `energy`和`recorder`：有多少安装使用能源仪表板，以及使用了哪些数据库引擎。
- `last_updated`：数据上次处理的时间戳（以毫秒为单位）。

## 快速浏览 {#a-quick-look}
查看使用次数最多的十个集成，包含 `curl` 和 `jq`：

```bash
curl -s https://analytics.home-assistant.io/current_data.json \
  | jq '.integrations | to_entries | sort_by(-.value) | .[:10]'
```

或者在 Python 中：

```python
import json
from urllib.request import urlopen

URL = "https://analytics.home-assistant.io/current_data.json"

with urlopen(URL) as response:
    data = json.load(response)

total = data["reports_integrations"]
top = sorted(data["integrations"].items(), key=lambda item: -item[1])

for domain, count in top[:10]:
    print(f"{domain}: {count / total:.1%}")
```

## Prometheus {#prometheus}
相同的数据也以 Prometheus 文本格式发布，因此你可以将其抓取到自己的监控系统中：

- `/prometheus/base`
- `/prometheus/integrations`
- `/prometheus/custom_integrations`
- `/prometheus/addons`

例如，作为抓取任务：

```yaml
scrape_configs:
  - job_name: "homeassistant_analytics_integrations"
    scrape_interval: 1h
    metrics_path: /prometheus/integrations
    scheme: https
    static_configs:
      - targets:
          - "analytics.home-assistant.io"
```

数据只有在处理时才会改变，所以抓取频率高于每小时一次没有意义。

## 需要注意的事项 {#things-to-keep-in-mind}
- 这些数字只包括选择参与的安装。实际的安装数量更高，但具体高多少没人知道。
- 并非每个分享基础分析的用户也会分享使用情况或统计数据。始终用匹配的 `reports_*` 数字来除。
- 安装在最后一次报告后的 60 天会从数据中消失。

想更改网站或处理流程吗？代码在 [analytics.home-assistant.io 仓库](https://github.com/home-assistant/analytics.home-assistant.io) 中。pull request请针对 `dev` 分支。
