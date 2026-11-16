---
title: 哪些分析共享
description: 每个字段 Home Assistant 在你开启分析时发送，按选项分类，并附示例数据。
order: 1
---


# 哪些分析共享 {#what-analytics-shares}
分析被分成你可以单独开启的选项，在 **设置** > **系统** > **分析** 中。使用和统计数据需要启用基本分析。此页面列出了每个选项对报告的添加内容。信息来源以核心中的 [分析集成](https://github.com/home-assistant/core/tree/dev/homeassistant/components/analytics) 为准。

## 基本分析 {#basic-analytics}
当分析功能开启时，它总是报告的一部分。

| 字段 | 说明 |
| --- | --- |
| `uuid` | 对你的安装的随机标识符，在第一次发送分析时生成。它仅用于统计你的安装一次。 |
| `version` | Home Assistant 版本，例如 `2026.10.0`。 |
| `installation_type` | 安装类型，例如 `Home Assistant OS` 或 `Home Assistant Container`。 |
| `supervisor` | 仅在 Supervisor 中：安装是否 `healthy` 和 `supported`，及其架构 `arch`。 |
| `operating_system` | 仅在 Home Assistant OS 中：`board`，以及操作系统的 `version`。 |

接收方根据 IP 地址添加 `country`。对于美国，它还会添加 `region`，即州。 

```json
{
  "uuid": "12a3456bc78d90123ef4567a789012b3",
  "version": "2026.10.0",
  "installation_type": "Home Assistant OS",
  "supervisor": {
    "healthy": true,
    "supported": true,
    "arch": "amd64"
  },
  "operating_system": {
    "board": "odroid-n2",
    "version": "18.3"
  }
}
```

## 使用方法 {#usage}
按名称添加你的使用。

| 字段 | 含义 |
| --- | --- |
| `integrations` | 你使用的内置集成的域，例如 `hue` 或 `zha`。 |
| `custom_integrations` | 你使用的每个自定义集成的域和版本。 |
| `addons` | 仅适用于 Supervisor：对于每个应用，其 `slug`、`version` 以及 `protected` 模式和 `auto_update` 是否开启。 |
| `energy` | 能源仪表盘是否 `configured`。 |
| `recorder` | 录制器的数据库 `engine`，例如 `sqlite`，以及其 `version`。 |
| `certificate` | Home Assistant 是否使用自己的证书提供 HTTPS 服务。 |

当集成通过 UI 设置且未被禁用或忽略，通过 YAML 配置，或提供未被禁用的实体时，即算作已计入。

```json
{
  "integrations": ["hue", "zha"],
  "custom_integrations": [
    { "domain": "my_integration", "version": "1.2.0" }
  ],
  "addons": [
    {
      "slug": "core_mosquitto",
      "protected": true,
      "version": "6.5.1",
      "auto_update": false
    }
  ],
  "energy": { "configured": true },
  "recorder": { "engine": "sqlite", "version": "3.49.1" },
  "certificate": false
}
```

## 统计数据 {#statistical-data}
只添加数量，不添加名称。

| 字段 | 含义 |
| --- | --- |
| `state_count` | 实体数量。 |
| `automation_count` | 自动化数量。 |
| `integration_count` | 内置集成数量，按使用情况计数。 |
| `addon_count` | 仅在 Supervisor 下：应用数量。 |
| `user_count` | 用户数量，不包括系统用户。 |

## 诊断 {#diagnostics}
不会向报告中添加任何内容。它会为 Supervisor 和操作系统代理开启 [Sentry](https://sentry.io/) 的崩溃报告。请参阅 [分析是如何工作的](/data/how-it-works#diagnostics)。

## 设备 {#devices}
会向设备数据库发送你设备的单独快照，而不是发送给分析接收器。它不需要基础分析，但需要在 **设置** > **系统** > **实验室** 中启用 **设备数据库** 预览功能。开启此功能也会开启此选项。有关其内容，请参阅 [设备数据库](/data/how-it-works#the-device-database)。

## 保留时长 {#how-long-it-is-kept}
接收器为每次安装保留一个条目。当报告与存储内容不同或至少每 30 天（即使没有变化）会重写一次条目。连续 60 天未重写的条目将被删除。
