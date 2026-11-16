---
title: Supervisor API
description: Supervisor 向应用程序提供的 REST API、如何进行身份验证、您的应用程序被允许调用的内容以及响应的样子。
order: 40
---



# Supervisor API {#supervisor-api}
Supervisor 在内部网络上运行 REST API。Home Assistant Core 使用它，CLI 使用它，你的应用也可以使用它：读取自身配置、查找 MQTT 代理、进行备份或重启 Home Assistant。本节是该 API 的参考。

路径仍然使用旧名称：应用程序位于 `/addons` 和 `/store/addons` 下。这才是真正的 API，因此你调用的就是它。

## 基础 URL 和认证 {#base-url-and-authentication}

在应用容器内部，API 位于 `http://supervisor/`。Supervisor 为每个应用在 `SUPERVISOR_TOKEN` 环境变量中提供自己的令牌。每次请求都要发送它：

```bash
curl -sSL \
  -H "Authorization: Bearer ${SUPERVISOR_TOKEN}" \
  http://supervisor/info
```

Supervisor 接受以下任一请求头中的令牌，按此顺序检查：

- `X-Supervisor-Token: <token>`
- `X-Hassio-Key: <token>`（旧版）
- `Authorization: Bearer <token>`

相同的令牌也可通过 `HASSIO_TOKEN` 访问，这是变量的旧名称。在新代码中使用 `SUPERVISOR_TOKEN`。

如果你用 Bash 编写应用脚本，[Bashio](/apps/bashio) 将大部分 API 封装在类似 `bashio::app.option` 和 `bashio::services` 的函数中。它会为你处理令牌。

## 您的应用程序可能访问的内容 {#what-your-app-may-call}

您的应用程序可以访问哪些端点取决于其在 `config.yaml` 中的配置。有关完整信息，请参阅 [与 Home Assistant 和 Supervisor 通信](/apps/guides/communication)，以及查看选项的 [配置参考](/apps/reference/configuration)。

### 无需任何额外权限 {#without-any-extra-permission}

每个应用都可以使用其令牌调用这些端点，即使没有`hassio_api`：

| 路径 | 用途 |
| --- | --- |
| `/addons/self/<endpoint>` | 位于您自己的应用下一层的路径，例如 `info`、`options`、`logs`、`stats`、`start` 或 `restart`。不包括 `security` 和 `update`，也不包括更深层的路径如 `logs/follow` |
| `/addons/self/options/config` | 您自己验证过的选项 |
| `/info` | 系统的一般信息 |
| `/services` 及其下的所有内容 | [服务](/apps/supervisor-api/services) 例如 MQTT |
| `/discovery` 及其下的所有内容 | [发现](/apps/supervisor-api/services#discovery) 消息 |
| `/auth` | 检查用户凭证，需要 `auth_api: true` |

`self` 是一个别名：无论哪个路径需要应用标识符，您的应用都可以使用 `self` 来表示自身。

### 与 `hassio_api: true` {#with-hassioapi-true}

在 `config.yaml` 中设置 `hassio_api: true` 以获取更多 API 的访问权限。具体取决于您使用 `hassio_role` 设置的角色：

| 角色 | 可调用 |
| --- | --- |
| `default` | 所有以 `/info` 结尾的路径，例如 `/core/info` 或 `/os/info` |
| `homeassistant` | `default` 的所有内容，以及 `/core/` 和 `/homeassistant/` 下的所有内容 |
| `backup` | `default` 的所有内容，以及 `/backups` 下的所有内容 |
| `manager` | `default` 的所有内容，加上 `/addons`（除其他应用的 `security` 端点外）、`/addons/reload`、`/audio`、`/auth/cache`、`/available_updates`、`/backups`、`/cli`、`/core`、`/dns`、`/docker`、`/hardware`、`/homeassistant`、`/host`、`/jobs`、`/mounts`、`/multicast`、`/network`、`/observer`、`/os`（除了 `/os/datadisk/wipe`）、`/refresh_updates`、`/resolution`、`/security`、`/store`、`/supervisor` 和 `/time` |
| `admin` | 全部 |只请求您的应用所需的角色。`manager` 和 `admin` 角色会降低您应用的 [安全评级](/apps/guides/security)。

### 绝不能通过应用程序访问 {#never-from-an-app}

有些路径对于任何应用程序都是禁止的，不管其角色如何：

- `/addons/<app>/sys_options` 和 `/os/ssh/authorized_keys` 只接受来自 Home Assistant Core 的调用。
- `/core/api/hassio...` 和 `/homeassistant/api/hassio...` 对所有人都被阻止。通过这些核心端点，调用者的行为相当于 Supervisor 本身。
- 通过 [WebSocket 代理](/apps/supervisor-api/core#get-corewebsocket)，以 `supervisor/` 或 `hassio/` 开头的命令会被拒绝。

### 没有令牌 {#without-a-token}

`GET /supervisor/ping` 不需要令牌。对 [Home Assistant Core 代理](/apps/supervisor-api/core#home-assistant-core-api-proxy) 的调用也不会检查你的角色：代理会自行检查你的令牌，并且只有在你的应用具有 `homeassistant_api: true` 权限时才允许通过。

## 响应 {#responses}

大多数端点都会在相同的封装中以 JSON 格式响应。一次成功的调用：

```json
{
  "result": "ok",
  "data": {}
}
```

`data` 保存了端点的响应。本参考中的响应表描述了 `data` 内部的内容。仅执行动作的端点（如重启）会返回一个空的 `data`。

一次失败的调用：

```json
{
  "result": "error",
  "message": "App my_app does not exist",
  "error_key": "app_not_found_error",
  "extra_fields": {}
}
```

| 键 | 描述 |
| --- | --- |
| `result` | `ok` 或 `error` |
| `data` | 响应，仅在成功时存在 |
| `message` | 可读的人类错误信息 |
| `error_key` | 错误的稳定键，当错误存在时使用它。在代码中使用它而不是解析 `message` |
| `extra_fields` | 与 `error_key` 相关的值（如有） |
| `job_id` | 失败的 [job](/apps/supervisor-api/supervisor#jobs) 的 ID，当错误来源于该 job 时 |有些端点不使用信封。日志、变更日志和文档以纯文本形式返回。图标和徽标以 PNG 图片形式返回。备份下载以 tar 文件形式返回。当这些操作失败时，错误也是纯文本。

### 状态码 {#status-codes}

| 代码 | 含义 |
| --- | --- |
| `200` | 成功 |
| `400` | 请求失败。请阅读 `message` 了解原因。当 Supervisor 仍在启动时，也会得到此结果 |
| `401` | 没有令牌，或令牌未被此端点接受 |
| `403` | 您的应用没有访问此路径的权限 |
| `404` | 应用、备份、任务或其他对象不存在 |
| `409` | 冲突，例如已在运行的操作 |
| `500` | Supervisor 内部出现问题。检查 Supervisor 日志 |

### 后台任务 {#background-jobs}

像安装应用或进行备份这样的长时间操作，会作为 [任务](/apps/supervisor-api/supervisor#jobs) 运行。多个端点接受 `background` 选项。使用 `background: true` 时，调用会立即返回一个 `job_id`，您可以通过 `GET /jobs/<job_id>` 跟踪进度。

## 日志端点 {#log-endpoints}

应用程序、Home Assistant Core、Supervisor、插件以及主机都有以相同方式工作的日志端点。它们从主机的 systemd 日志中读取并返回纯文本。

| 路径 | 返回内容 |
| --- | --- |
| `<base>/logs` | 最新的日志行 |
| `<base>/logs/follow` | 最近的行，然后保持连接打开并流式传输新的日志行 |
| `<base>/logs/latest` | 自容器上次启动以来的所有行 |
| `<base>/logs/boots/<bootid>` | 一次启动的日志行 |
| `<base>/logs/boots/<bootid>/follow` | 一次启动的日志行，然后流式传输新的日志行 |

`<bootid>` 可以是来自 [`GET /host/logs/boots`](/apps/supervisor-api/host#get-hostlogsboots) 的启动 ID，或者是一个偏移量：`0` 表示当前启动，`-1` 表示前一次启动，依此类推。正数从日志仍然保存的最早启动开始计数。

日志端点支持以下查询参数和头信息：| 参数 | 描述 |
| --- | --- |
| `lines` | 查询参数。要返回的行数。默认值为100，最小值为2 |
| `verbose` | 查询参数，无需值。向每行添加时间戳、主机名和进程 |
| `no_colors` | 查询参数，无需值。去除ANSI颜色代码 |
| `Accept` | 头部。`text/plain`（默认）或`text/x-log`。`text/x-log` 的输出与 `verbose` 相同 |
| `Range` | 头部。[systemd-journal-gatewayd](https://www.freedesktop.org/software/systemd/man/latest/systemd-journal-gatewayd.service.html) 范围，如 `entries=cursor[[:num_skip]:num_entries]`。设置 `lines` 时忽略 |

响应中包含一个 `X-First-Cursor` 头部，带有第一行的日志游标。将其传递到 `Range` 头部中，以分页浏览较早的行。

## 示例 {#examples}

检查 Supervisor 是否正常运行。这一个不需要令牌：

```bash
curl -sSL http://supervisor/supervisor/ping
```

```json
{
  "result": "ok",
  "data": {}
}
```

获取主机的网络配置。你的应用需要 `hassio_api: true` 来执行此操作，任何角色都可以：

```bash
curl -sSL \
  -H "Authorization: Bearer ${SUPERVISOR_TOKEN}" \
  http://supervisor/network/info
```

读取你自己应用的选项，并根据其架构进行验证：

```bash
curl -sSL \
  -H "Authorization: Bearer ${SUPERVISOR_TOKEN}" \
  http://supervisor/addons/self/options/config
```

```json
{
  "result": "ok",
  "data": {
    "name": "world",
    "beer": true
  }
}
```

## 端点 {#the-endpoints}

- [应用](/apps/supervisor-api/apps)：已安装的应用、它们的选项、状态和日志。
- [商店](/apps/supervisor-api/store)：可以安装的应用，以及应用仓库。
- [备份](/apps/supervisor-api/backups)：创建、还原和管理备份。
- [Home Assistant Core](/apps/supervisor-api/core)：控制核心，以及它的 REST 和 WebSocket API 的代理。
- [主机和操作系统](/apps/supervisor-api/host)：主机、Home Assistant OS、硬件、网络、时间、挂载点和 Docker。
- [插件](/apps/supervisor-api/plugins)：音频、CLI、DNS、多播和观察者。
- [Supervisor](/apps/supervisor-api/supervisor)：Supervisor 本身、更新、任务、解析和安全性。
- [服务、发现、认证和入口](/apps/supervisor-api/services)：应用用来协作以及与 Home Assistant 交互的功能。
- [模型](/apps/supervisor-api/models)：多个端点返回的对象。

## API 版本 2 {#api-version-2}

Supervisor 也在 `/v2` 下提供了该 API 的第二个版本，其中应用位于 `/apps` 和 `/store/apps`，而不是 `/addons` 和 `/store/addons`。它仅在 `supervisor_v2_api` 开发功能标志开启时存在，并且仍在变化中。本参考文档涵盖不带 `/v2` 的 API，这是每个安装都会有的版本。
