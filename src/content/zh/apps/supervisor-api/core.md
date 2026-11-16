---
title: Home Assistant Core 端点
description: Supervisor API端点用于控制Home Assistant Core，以及您的应用用于访问Core REST和WebSocket
  API的代理。
sidebarLabel: Home Assistant Core
order: 4
---


# Home Assistant Core 端点 {#home-assistant-core-endpoints}

`/core` 下有两种端点。第一种端点控制 Home Assistant Core 容器：启动、停止、更新及其设置。第二种端点是 Home Assistant 本身 API 的代理，因此您的应用可以在不知晓密码或端口的情况下读取状态和调用操作。

大多数这些端点也可在 `/homeassistant` 下使用，而不是旧名称 `/core`。那里的代理没有 `DELETE`。请使用 `/core`。| 方法 | 路径 | 描述 |
| --- | --- | --- |
| `GET` | `/core/info` | 有关 Home Assistant Core 的信息 |
| `POST` | `/core/options` | 更改核心设置 |
| `POST` | `/core/update` | 更新 Home Assistant Core |
| `POST` | `/core/start` | 启动 Home Assistant Core |
| `POST` | `/core/stop` | 停止 Home Assistant Core |
| `POST` | `/core/restart` | 重启 Home Assistant Core |
| `POST` | `/core/rebuild` | 重建核心容器 |
| `POST` | `/core/check` | 检查配置 |
| `GET` | `/core/stats` | 核心的资源使用情况 |
| `GET` | `/core/logs` | 核心日志，以及其他 [日志端点](/apps/supervisor-api#log-endpoints) |
| `GET`, `POST`, `DELETE` | `/core/api/<path>` | 代理到 Home Assistant REST API |
| `GET` | `/core/api/stream` | 代理到事件流 |
| `GET` | `/core/websocket` | 代理到 Home Assistant WebSocket API |

## 控制 Home Assistant Core {#control-home-assistant-core}

要使用这些，您的应用需要 `hassio_api: true` 以及 `homeassistant`、`manager` 或 `admin` 角色。`GET /core/info` 可与任何角色一起使用。
### `GET /core/info` {#get-coreinfo}

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `version` | 字符串 | 已安装版本 |
| `version_latest` | 字符串 | 最新可用版本 |
| `update_available` | 布尔值 | 如果有更新，则为 `true` |
| `machine` | 字符串 | 机器类型，如 `generic-x86-64` 或 `raspberrypi5-64` |
| `ip_address` | 字符串 | Core 在内部网络上的 IP 地址 |
| `arch` | 字符串 | 架构 |
| `image` | 字符串 | 容器镜像 |
| `boot` | 布尔值 | 如果 Core 在启动时启动，则为 `true` |
| `port` | 整数 | Home Assistant Web 服务器的端口 |
| `ssl` | 布尔值 | 如果 Web 服务器使用 SSL，则为 `true` |
| `watchdog` | 布尔值 | 如果看门狗开启，则为 `true` |
| `audio_input` | 字符串或空值 | 选择的音频输入设备 |
| `audio_output` | 字符串或空值 | 选择的音频输出设备 |
| `backups_exclude_database` | 布尔值 | 如果备份默认不包含数据库，则为 `true` || `duplicate_log_file` | 布尔值 | `true` 如果 Core 也将其日志写入文件 | 

```json
{
  "version": "2026.10.1",
  "version_latest": "2026.10.1",
  "update_available": false,
  "machine": "generic-x86-64",
  "ip_address": "172.30.32.1",
  "arch": "amd64",
  "image": "ghcr.io/home-assistant/generic-x86-64-homeassistant",
  "boot": true,
  "port": 8123,
  "ssl": false,
  "watchdog": true,
  "audio_input": null,
  "audio_output": null,
  "backups_exclude_database": false,
  "duplicate_log_file": false
}
```

### `POST /core/options` {#post-coreoptions}

只发送你想要更改的键。

| 键 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `boot` | 布尔值 | 否 | 启动时启动 Core |
| `image` | 字符串或 null | 否 | 使用其他容器镜像。`null` 恢复到默认值 |
| `port` | 整数 | 否 | Home Assistant Web 服务器的端口 |
| `ssl` | 布尔值 | 否 | Web 服务器使用 SSL |
| `watchdog` | 布尔值 | 否 | 打开或关闭看门狗 |
| `refresh_token` | 字符串或 null | 否 | Supervisor 用于 Core 的刷新令牌 |
| `audio_input` | 字符串或 null | 否 | 音频输入设备 |
| `audio_output` | 字符串或 null | 否 | 音频输出设备 |
| `backups_exclude_database` | 布尔值 | 否 | 默认将数据库排除在备份之外 |
| `duplicate_log_file` | 布尔值 | 否 | 也将 Core 日志写入文件 |

### `POST /core/update` {#post-coreupdate}

更新 Home Assistant Core。当 Supervisor 仍在启动或恢复备份时，以及 Core 在运行数据库迁移时会失败。

| 键 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `version` | 字符串 | 否 | 要安装的版本。默认是最新版本 |
| `backup` | 布尔值 | 否 | 更新前进行备份。默认 `false` |
| `background` | 布尔值 | 否 | 立即返回 `job_id`，而不是等待。默认 `false` |

### `POST /core/start` {#post-corestart}

启动 Home Assistant Core。类似于重启和重建，当 Supervisor 仍在启动或恢复备份时会失败。

### `POST /core/stop` {#post-corestop}

停止 Home Assistant Core。

| 键 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `force` | 布尔值 | 否 | 即使 Core 正在运行数据库迁移也停止。默认 `false` |

### `POST /core/restart` {#post-corerestart}

重启 Home Assistant Core。

| 键 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `safe_mode` | 布尔值 | 否 | 以安全模式启动，关闭自定义集成。默认 `false` |
| `force` | 布尔值 | 否 | 即使 Core 正在运行数据库迁移也重启。默认 `false` |

### `POST /core/rebuild` {#post-corerebuild}

删除 Core 容器并从同一镜像重新创建。接受与 `POST /core/restart` 相同的键。

### `POST /core/check` {#post-corecheck}

检查 Home Assistant 配置。当配置有效时返回成功，当配置无效时返回检查的输出错误。

### `GET /core/stats` {#get-corestats}

返回 Home Assistant Core 的资源使用情况，作为一个 [统计模型](/apps/supervisor-api/models#stats)。添加 `one_shot` 查询参数以获取单个快速样本。

## Home Assistant Core API 代理 {#home-assistant-core-api-proxy}

该代理将您的请求转发到 Home Assistant Core 的 REST API 和 WebSocket API，使用您的应用令牌。在核心端，请求以 Home Assistant 管理员身份运行。您的应用在配置中需要 `homeassistant_api: true`。它不需要 `hassio_api` 或任何角色。请参阅 [联系 Home Assistant](/apps/guides/communication) 了解使用方法。

以 `hassio` 开头的路径通过代理被阻止。

### `GET /core/api/<path>` {#get-coreapi}

还 `POST` 和 `DELETE`。将请求转发到 Home Assistant Core 上的 `/api/<path>`，并按原样返回核心的响应。代理不会将其包装在 Supervisor 信封中。

```bash
curl -sSL \
  -H "Authorization: Bearer ${SUPERVISOR_TOKEN}" \
  http://supervisor/core/api/states/sun.sun
```

### `GET /core/api/stream` {#get-coreapistream}

转发 Home Assistant Core 的服务器发送事件流。

### `GET /core/websocket` {#get-corewebsocket}

打开到 Home Assistant Core 的 WebSocket 连接。`/core/api/websocket` 也可以。握手是普通的 Home Assistant 握手，使用你的应用令牌作为访问令牌：

```json
{
  "type": "auth",
  "access_token": "<your SUPERVISOR_TOKEN>"
}
```

在 `auth_ok` 之后，你像平常一样使用 WebSocket API。以 `supervisor/` 或 `hassio/` 开头的命令会被拒绝。
