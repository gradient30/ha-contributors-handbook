---
title: Supervisor 端点
description: Supervisor 本身、系统信息、更新、作业、分辨率和安全设置的 API 端点。
sidebarLabel: Supervisor
order: 7
---


# Supervisor 端点 {#supervisor-endpoints}

这些端点涉及Supervisor和整个系统。`GET /info`适用于每个应用程序，无需额外权限。其他`/info`端点适用于任何角色。其余的需要`hassio_api: true`同时具备`manager`或`admin`角色。

## 系统 {#system}

| 方法 | 路径 | 描述 |
| --- | --- | --- |
| `GET` | `/info` | 系统概览 |
| `GET` | `/available_updates` | 可用更新 |
| `POST` | `/reload_updates` | 检查更新 |
| `POST` | `/refresh_updates` | 检查更新并重新加载商店 |
### `GET /info` {#get-info}

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `supervisor` | 字符串 | Supervisor 的版本 |
| `homeassistant` | 字符串 或 null | Home Assistant Core 的版本 |
| `hassos` | 字符串 或 null | Home Assistant OS 的版本，其他系统上为 `null` |
| `docker` | 字符串 | Docker 的版本 |
| `hostname` | 字符串 或 null | 主机名 |
| `operating_system` | 字符串 或 null | 操作系统名称 |
| `features` | 列表 | 主机支持的功能 |
| `machine` | 字符串 | 机器类型，如 `generic-x86-64` |
| `machine_id` | 字符串 或 null | 主机的机器 ID |
| `arch` | 字符串 | 主架构 |
| `supported_arch` | 列表 | 系统可以运行的所有架构 |
| `state` | 字符串 | Supervisor 的状态，如 `running` |
| `supported` | 布尔 | 如果安装受支持，`true` |
| `channel` | 字符串 | 更新通道：`stable`、`beta` 或 `dev` || `logging` | 字符串 | Supervisor 的日志级别 |
| `timezone` | 字符串 | 时区 |

```json
{
  "supervisor": "2026.10.0",
  "homeassistant": "2026.10.1",
  "hassos": "17.0",
  "docker": "28.3.3",
  "hostname": "homeassistant",
  "operating_system": "Home Assistant OS 17.0",
  "features": ["reboot", "shutdown", "services", "network", "hostname"],
  "machine": "generic-x86-64",
  "machine_id": "d4d2b9f5a6b84e2f9c3e1a7b8c9d0e1f",
  "arch": "amd64",
  "supported_arch": ["amd64"],
  "state": "running",
  "supported": true,
  "channel": "stable",
  "logging": "info",
  "timezone": "Europe/Amsterdam"
}
```

### `GET /available_updates` {#get-availableupdates}

返回可用于核心、Supervisor、操作系统和已安装应用的更新。旧路径 `/supervisor/available_updates` 返回相同内容。

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `available_updates` | 列表 | 每个更新一条记录，包含 `update_type`（`core`、`supervisor`、`os` 或 `addon`）、`panel_path` 和 `version_latest`。应用更新还包含 `name` 和 `icon` |

### `POST /reload_updates` {#post-reloadupdates}

检查核心、Supervisor、操作系统和插件的新版本。

### `POST /refresh_updates` {#post-refreshupdates}

执行与 `POST /reload_updates` 相同的操作，并且还会重新加载应用商店。优先使用 `POST /reload_updates` 和 [`POST /store/reload`](/apps/supervisor-api/store#post-storereload)。

## Supervisor {#supervisor}

| 方法 | 路径 | 描述 |
| --- | --- | --- |
| `GET` | `/supervisor/ping` | 检查 Supervisor 是否运行。无需令牌 |
| `GET` | `/supervisor/info` | 有关 Supervisor 的信息 |
| `POST` | `/supervisor/options` | 更改 Supervisor 设置 |
| `POST` | `/supervisor/update` | 更新 Supervisor |
| `POST` | `/supervisor/reload` | 重新加载版本、密钥和系统检查 |
| `POST` | `/supervisor/restart` | 重启 Supervisor |
| `POST` | `/supervisor/repair` | 修复安装 |
| `GET` | `/supervisor/stats` | Supervisor 的资源使用情况 |
| `GET` | `/supervisor/logs` | Supervisor 的日志，以及其他 [日志端点](/apps/supervisor-api#log-endpoints)。当日志无法提供时，你将获得容器的 Docker 日志 |

### `GET /supervisor/ping` {#get-supervisorping}

当 Supervisor 启动时返回成功。它不需要令牌，因此你可以在其他任何操作之前调用它。
### `GET /supervisor/info` {#get-supervisorinfo}

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `version` | 字符串 | 已安装版本 |
| `version_latest` | 字符串 | 可用的最新版本 |
| `update_available` | 布尔值 | 如果有更新，则为 `true` |
| `channel` | 字符串 | `stable`、`beta` 或 `dev` |
| `arch` | 字符串 | 架构 |
| `supported` | 布尔值 | 如果安装受支持，则为 `true` |
| `healthy` | 布尔值 | 如果安装正常，则为 `true` |
| `ip_address` | 字符串 | 内部网络上 Supervisor 的 IP 地址 |
| `timezone` | 字符串 或 空值 | 时区 |
| `logging` | 字符串 | 日志级别 |
| `debug` | 布尔值 | 如果调试模式开启，则为 `true` |
| `debug_block` | 布尔值 | 如果 Supervisor 启动时等待调试器，则为 `true` |
| `diagnostics` | 布尔值 或 空值 | 如果共享诊断信息，则为 `true` |
| `auto_update` | 布尔值 | 如果 Supervisor 自动更新，则为 `true` || `detect_blocking_io` | 布尔值 | `true` 如果检测到阻塞 I/O 是否开启 |
| `country` | 字符串或空值 | 国家代码 |
| `feature_flags` | 字典 | 开发功能标志及其是否开启 |
| `wait_boot` | 整数 | 已弃用 |
| `addons` | 列表 | 已弃用。已安装的应用，包括 `name`、`slug`、`version`、`version_latest`、`update_available`、`state`、`repository` 和 `icon`。使用 [`GET /addons`](/apps/supervisor-api/apps#get-addons) |
| `addons_repositories` | 列表 | 已弃用。代码仓库，包括 `name` 和 `slug`。使用 [`GET /store/repositories`](/apps/supervisor-api/store#get-storerepositories) |
### `POST /supervisor/options` {#post-supervisoroptions}

| 键 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `channel` | 字符串 | 否 | `stable`、`beta` 或 `dev` |
| `timezone` | 字符串 | 否 | 时区，例如 `Europe/Amsterdam`。在 Home Assistant OS 16.2 或更高版本中，也会设置主机的时区 |
| `logging` | 字符串 | 否 | `debug`、`info`、`warning`、`error` 或 `critical` |
| `debug` | 布尔值 | 否 | 调试模式 |
| `debug_block` | 布尔值 | 否 | 启动时等待调试器 |
| `diagnostics` | 布尔值 | 否 | 共享诊断信息 |
| `auto_update` | 布尔值 | 否 | 自动更新 Supervisor |
| `detect_blocking_io` | 字符串 | 否 | `on`、`off` 或 `on-at-startup` |
| `country` | 字符串 | 否 | 国家代码 |
| `feature_flags` | 字典 | 否 | 用于开启或关闭的开发功能标志，例如 `{"supervisor_v2_api": true}`。未包含的标志保持其原有值 |
| `wait_boot` | 整数 | 否 | 已弃用 || `addons_repositories` | 列表 | 否 | 已弃用。替代存储库列表。请使用 [存储库端点](/apps/supervisor-api/store#repositories) |

### `POST /supervisor/update` {#post-supervisorupdate}

将 Supervisor 更新到最新版本。如果没有更新则会失败。`version` 密钥仅在 Supervisor 开发环境中有效，此时 `SUPERVISOR_DEV` 为 `1`。在其他任何地方，Supervisor 都会忽略它并安装最新版本。

### `POST /supervisor/reload` {#post-supervisorreload}

检查新版本，重新加载 Home Assistant 的密钥，并再次检查系统。

### `POST /supervisor/restart` {#post-supervisorrestart}

重启 Supervisor。

### `POST /supervisor/repair` {#post-supervisorrepair}

修复安装：在可能的情况下修复缺失的镜像、容器和文件。

### `GET /supervisor/stats` {#get-supervisorstats}

以 [stats model](/apps/supervisor-api/models#stats) 的形式返回 Supervisor 的资源使用情况。

## 任务 {#jobs}

Supervisor 将长时间运行的任务（如安装、更新和备份）作为作业运行。作业形成一棵树：例如，一个备份作业会有每个应用的子作业。

| 方法 | 路径 | 描述 |
| --- | --- | --- |
| `GET` | `/jobs/info` | 所有作业 |
| `GET` | `/jobs/<job_id>` | 单个作业 |
| `DELETE` | `/jobs/<job_id>` | 删除已完成的作业 |
| `POST` | `/jobs/options` | 更改作业设置 |
| `POST` | `/jobs/reset` | 重置作业设置 |

### `GET /jobs/info` {#get-jobsinfo}

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `ignore_conditions` | 列表 | Supervisor 在开始工作之前忽略的条件 |
| `jobs` | 列表 | [作业模型](/apps/supervisor-api/models#job)，最新的在前 |

### `GET /jobs/<job_id>` {#get-jobs}

返回一个 [作业模型](/apps/supervisor-api/models#job)，及其子作业。用于跟踪您通过 `background: true` 启动的工作。

```json
{
  "name": "backup_manager_partial_backup",
  "reference": "a1b2c3d4",
  "uuid": "e2b7a9c4f1d34e5a8b6c0d1e2f3a4b5c",
  "progress": 0,
  "stage": "addons",
  "done": false,
  "errors": [],
  "created": "2026-10-01T09:30:00.000000+00:00",
  "extra": null,
  "child_jobs": []
}
```

除非 `supervisor_websocket_v2_api` 开发功能标志开启，否则某些作业在此处仍使用旧名称。备份和恢复作业报告的阶段如 `addons` 而不是 `apps`，更新应用的作业为 `addon_manager_update`。

### `DELETE /jobs/<job_id>` {#delete-jobs}

从列表中删除作业。当作业未完成时将失败。

### `POST /jobs/options` {#post-jobsoptions}

| 键 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| `ignore_conditions` | 列表 | 否 | 在开始任务之前要忽略的条件，例如 `healthy` 或 `internet_host`。会替换当前列表。可能会导致问题，所以仅用于调试 |

### `POST /jobs/reset` {#post-jobsreset}

将作业设置重置为默认值，因此不再忽略任何条件。

## 解析 {#resolution}

解析中心查找系统中的问题并建议修复方案。问题是指某个问题，建议是针对该问题的修复方案，而检查是发现这些问题的测试。

| 方法 | 路径 | 描述 |
| --- | --- | --- |
| `GET` | `/resolution/info` | 问题、建议和检查 |
| `GET` | `/resolution/issue/<issue>/suggestions` | 针对某个问题的建议 |
| `DELETE` | `/resolution/issue/<issue>` | 驳回一个问题 |
| `POST` | `/resolution/suggestion/<suggestion>` | 应用建议 |
| `DELETE` | `/resolution/suggestion/<suggestion>` | 驳回建议 |
| `POST` | `/resolution/check/<check>/options` | 打开或关闭检查 |
| `POST` | `/resolution/check/<check>/run` | 运行检查 |
| `POST` | `/resolution/healthcheck` | 运行所有检查，并应用可自动执行的修复 |

`<issue>` 和 `<suggestion>` 是 UUID。`<check>` 是检查的标识符。

### `GET /resolution/info` {#get-resolutioninfo}

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `unsupported` | 列表 | 安装不受支持的原因 |
| `unhealthy` | 列表 | 安装不健康的原因 |
| `issues` | 列表 | [问题模型](/apps/supervisor-api/models#issue) |
| `suggestions` | 列表 | [建议模型](/apps/supervisor-api/models#suggestion) |
| `checks` | 列表 | [检查模型](/apps/supervisor-api/models#check) |

这里一些问题类型和检查标识仍然使用它们的旧名称，比如 `deprecated_addon` 和 `addon_pwned`。

### `GET /resolution/issue/<issue>/suggestions` {#get-resolutionissuesuggestions}

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `suggestions` | 列表 | 修复此问题的 [建议模型](/apps/supervisor-api/models#suggestion) |

### `POST /resolution/check/<check>/options` {#post-resolutioncheckoptions}

| 键 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `enabled` | 布尔值 | 否 | 打开或关闭检查 |

## 安全性 {#security}

| 方法 | 路径 | 描述 |
| --- | --- | --- |
| `GET` | `/security/info` | 安全设置 |
| `POST` | `/security/options` | 更改安全设置 |
| `POST` | `/security/integrity` | 已移除。始终返回 `410` |

### `GET /security/info` {#get-securityinfo}

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `pwned` | 布尔值 | 如果应用密码会被检查是否泄露 `true` |
| `force_security` | 布尔值 | 如果不允许启动使用泄露密码的应用 `true` |

### `POST /security/options` {#post-securityoptions}

| 键 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `pwned` | 布尔值 | 否 | 检查应用密码是否泄露 |
| `force_security` | 布尔值 | 否 | 阻止使用泄露密码的应用 |
