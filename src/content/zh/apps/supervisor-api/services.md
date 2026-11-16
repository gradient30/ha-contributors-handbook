---
title: 服务、发现、认证和入口端点
description: Supervisor API 端点应用程序用于共享像 MQTT 这样的服务，向 Home Assistant 宣布自身，检查用户凭证，并与入口协作。
sidebarLabel: 服务、发现、认证和入口
order: 8
---

# 服务、发现、认证和入口端点 {#services-discovery-auth-and-ingress-endpoints}

这些端点是应用程序彼此协作以及与 Home Assistant 协作的方式。它们中的大多数不需要 `hassio_api` 权限：应用程序可以执行的操作由其 `config.yaml` 来设置，同时使用 `services`、`discovery` 和 `auth_api`。有关如何在应用中使用它们，请参见 [服务和发现](/apps/guides/services-discovery)。

## 服务 {#services}

服务是一个应用程序提供而其他应用程序使用的功能，比如一个 MQTT 代理。提供服务的应用程序会注册其连接详情，需要该服务的应用程序可以读取这些信息，因此用户无需输入主机名和密码。

有两种服务：`mqtt` 和 `mysql`。

| 方法 | 路径 | 描述 |
| --- | --- | --- |
| `GET` | `/services` | 列出服务 |
| `GET` | `/services/<service>` | 读取服务的连接详情 |
| `POST` | `/services/<service>` | 注册为服务提供者 |
| `DELETE` | `/services/<service>` | 删除服务的注册 |

你的应用程序需要在其配置的 `services` 选项中使用该服务。Supervisor 检查内容:- 阅读并注册服务的任何角色工作：`want`、`need` 或 `provide`。当另一个应用已注册为提供者时，注册会失败。
- 删除注册需要 `<service>:provide`。

在配置中，`provide` 是用于注册的应用角色。

### `GET /services` {#get-services}

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `services` | 列表 | 一个 [服务模型](/apps/supervisor-api/models#service) 的列表 |

### `GET /services/<service>` {#get-services-1}

返回提供者注册的连接详细信息。当没有应用提供该服务时会失败。

```json
{
  "addon": "core_mosquitto",
  "host": "core-mosquitto",
  "port": 1883,
  "ssl": false,
  "protocol": "3.1.1",
  "username": "addons",
  "password": "Ahng5Ohghahy"
}
```

### `POST /services/mqtt` {#post-servicesmqtt}

将您的应用注册为 MQTT 代理。

| 键 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `host` | 字符串 | 是 | 代理的主机名 |
| `port` | 整数 | 是 | 代理的端口 |
| `username` | 字符串 | 否 | 其他应用使用的用户名 |
| `password` | 字符串 | 否 | 其他应用使用的密码 |
| `ssl` | 布尔值 | 否 | 代理使用 TLS。默认 `false` |
| `protocol` | 字符串 | 否 | `3.1` 或 `3.1.1`。默认 `3.1.1` |

### `POST /services/mysql` {#post-servicesmysql}

将您的应用程序注册为 MySQL 服务器。

| 键 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| `host` | 字符串 | 是 | 服务器主机名 |
| `port` | 整数 | 是 | 服务器端口 |
| `username` | 字符串 | 否 | 其他应用程序的用户名 |
| `password` | 字符串 | 否 | 其他应用程序的密码 |

### `DELETE /services/<service>` {#delete-services}

移除服务的注册。当服务提供应用停止提供服务时从该应用调用它。Supervisor 不会检查哪个应用进行了注册：它会移除当前的注册。

## 发现 {#discovery}

通过发现，您的应用告知 Home Assistant 它正在运行，以及如何访问它。然后 Home Assistant 会提供设置匹配集成的选项。您的应用只能发送其配置中 `discovery` 选项列出的集成的发现信息。

| 方法 | 路径 | 描述 |
| --- | --- | --- |
| `POST` | `/discovery` | 发送发现消息 |
| `DELETE` | `/discovery/<uuid>` | 移除发现消息 |
| `GET` | `/discovery` | 列出发现消息。只有 Home Assistant Core 可以调用此方法 |
| `GET` | `/discovery/<uuid>` | 单条发现消息。只有 Home Assistant Core 可以调用此方法 |

### `POST /discovery` {#post-discovery}

| 键 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `service` | 字符串 | 是 | 集成的域，例如 `mqtt` |
| `config` | 字典 | 是 | 集成需要连接的内容，如主机和端口 |

```json
{
  "service": "mqtt",
  "config": {
    "host": "core-mosquitto",
    "port": 1883
  }
}
```

响应包含消息的 `uuid`。保留它，以便稍后可以删除该消息。

### `DELETE /discovery/<uuid>` {#delete-discovery}

移除发现消息。您的应用只能移除自己的消息。

### `GET /discovery` {#get-discovery}

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `discovery` | 列表 | 正在运行的应用的[发现模型](/apps/supervisor-api/models#discovery) |
| `services` | 字典 | 每个集成可以发送发现的应用的标识符 |

## 认证 {#auth}

在其配置中使用 `auth_api: true`，你的应用可以检查 Home Assistant 用户的用户名和密码。使用它允许用户使用他们的 Home Assistant 账户登录你的应用。

`auth_api` 仅涵盖 `/auth` 本身。其他认证端点属于账户管理，需要具有 [角色](/apps/guides/security#api-roles) 的 `hassio_api: true`：`admin` 适用于 `/auth/list` 和 `/auth/reset`，`manager` 或 `admin` 适用于 `/auth/cache`。

| 方法 | 路径 | 描述 |
| --- | --- | --- |
| `GET`, `POST` | `/auth` | 检查用户凭据 |
| `GET` | `/auth/list` | 列出用户 |
| `POST` | `/auth/reset` | 更改用户密码 |
| `DELETE` | `/auth/cache` | 清除凭据缓存 |

### `POST /auth` {#post-auth}

检查用户名和密码。有三种方式发送它们：

- 一个 `Authorization: Basic` 头。然后在 `X-Supervisor-Token` 中发送你的令牌。
- 一个包含 `username` 和 `password` 的 JSON 主体。
- 一个表单主体（`application/x-www-form-urlencoded`）包含 `username` 和 `password`。

当凭证正确时返回成功，当凭证不正确时返回 `401`。Supervisor 会缓存正确的凭证一段时间，所以 Home Assistant 并不会在每次登录时都发出请求。

任何 `Authorization` 头都算作第一种方式，因此 Supervisor 会尝试将其作为 `Basic` 凭证读取。在这里发送你的令牌到 `X-Supervisor-Token`，而不是 `Authorization: Bearer`：

```bash
curl -sSL -X POST \
  -H "X-Supervisor-Token: ${SUPERVISOR_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"username": "jane", "password": "secret"}' \
  http://supervisor/auth
```

### `GET /auth/list` {#get-authlist}

返回 Home Assistant 中具有用户名的用户。

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `users` | 列表 | [用户模型](/apps/supervisor-api/models#user) 的列表 |

### `POST /auth/reset` {#post-authreset}

| 键 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `username` | 字符串 | 是 | 用户名 |
| `password` | 字符串 | 是 | 新密码 |

### `DELETE /auth/cache` {#delete-authcache}

清除正确凭证的缓存。

## 入口 {#ingress}

[入口](/apps/guides/ingress) 显示 Home Assistant 内应用的网页界面。Supervisor 代理请求，因此您的应用无需自行登录或开放端口。Home Assistant Core 使用这些端点来设置入口会话。您的应用本身不会调用它们。

| 方法 | 路径 | 描述 |
| --- | --- | --- |
| `GET` | `/ingress/panels` | 使用入口的应用的侧边栏面板。应用需要 `admin` 角色 |
| `POST` | `/ingress/session` | 创建入口会话。仅 Home Assistant Core 可以调用此 |
| `POST` | `/ingress/validate_session` | 检查入口会话。仅 Home Assistant Core 可以调用此 |

### `GET /ingress/panels` {#get-ingresspanels}

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `panels` | 字典 | 每个应用 slug 的 [面板模型](/apps/supervisor-api/models#panel) |

### `POST /ingress/session` {#post-ingresssession}

| 键 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `user_id` | 字符串 | 否 | Home Assistant 用户的 ID。Supervisor 在请求头中将用户传递给应用 |

返回新的会话作为 `session`。浏览器通过 `ingress_session` Cookie 将其发送给 Supervisor。

### `POST /ingress/validate_session` {#post-ingressvalidatesession}

| 键 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `session` | 字符串 | 是 | 要检查的会话 |

当会话有效时返回成功，当会话无效时返回 `401`。
