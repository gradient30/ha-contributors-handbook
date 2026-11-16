---
title: 和Home Assistant以及Supervisor谈谈
description: 通过内部网络和 API 代理，从你的应用访问 Home Assistant Core、Supervisor 以及其他应用。
order: 5
---


# 和Home Assistant以及Supervisor谈谈 {#talk-to-home-assistant-and-the-supervisor}
你的应用程序在内部网络中与Supervisor及其他应用程序一起运行，并获取令牌以调用它们的 API。本指南介绍了与每个应用程序通信的方法，以及每个应用程序所需的权限。

## 内部网络 {#the-internal-network}
每个应用通过主机名互相访问。Supervisor 在内部 DNS 中将每个应用注册为其应用 ID，同时将 `_` 替换为 `-`：

| 主机名 | 说明 |
| --- | --- |
| `supervisor` | Supervisor 及其 API，位于 `172.30.32.2` |
| `homeassistant` | Home Assistant Core |
| `core-mosquitto` | 官方 Mosquitto 中继应用 (`core_mosquitto`) |
| `local-hello-world` | 你的本地应用 `hello_world` |
| `a0d7b954-adguard` | 来自社区仓库的应用 |

应用 ID 以仓库 ID 开头：本地应用为 `local`，官方应用为 `core`，其他仓库为 URL 的哈希值。[应用工作原理](/apps/how-apps-work#names-and-ids) 解释了它是如何生成的。Supervisor API 的 `GET /addons` 端点列出了每个已安装应用的 `slug` 和 `repository`。

## 你的令牌 {#your-token}
Supervisor 为每个应用提供自己的令牌，存储在环境变量 `SUPERVISOR_TOKEN` 中。将其用于 Supervisor API 以及 Home Assistant Core API 代理，在 `Authorization: Bearer` 头中使用。令牌的功能取决于你 `config.yaml` 中的权限。

请记住，由 S6 覆盖启动的脚本需要 `#!/command/with-contenv bashio`（或 `with-contenv bash`）才能看到此变量。请参阅 [容器环境](/apps/guides/s6-overlay#the-container-environment)。

## Home Assistant Core {#home-assistant-core}
调用 Home Assistant 最简单的方法是通过 Supervisor 的代理。你不需要知道端口、SSL 是否开启，也不需要用户的访问令牌。将 `homeassistant_api: true` 添加到 `config.yaml`，并使用你的 `SUPERVISOR_TOKEN`：

```bash
curl -sSL \
  -H "Authorization: Bearer ${SUPERVISOR_TOKEN}" \
  -H "Content-Type: application/json" \
  http://supervisor/core/api/config
```

`http://supervisor/core/api/` 映射到 Home Assistant 的 REST API，`/api/` 在 Core 上。`/core/api/stream` 的事件流工作方式也相同。

WebSocket API 位于 `ws://supervisor/core/websocket`。像使用普通访问令牌一样，将你的 `SUPERVISOR_TOKEN` 作为 `access_token` 发送到身份验证消息中：

```json
{ "type": "auth", "access_token": "<your SUPERVISOR_TOKEN>" }
```

代理不会转发 `supervisor/` 和 `hassio/` 类型的命令，并且会阻止 REST API 的 `hassio` 端点。这些只能用于 Home Assistant 前端。> [!警告]
> 通过代理，你的应用程序将作为 Home Assistant 的管理员运行。管理员可以执行的所有其他操作，你的应用程序也可以执行，包括管理用户及其凭据。仅在你的应用程序需要 Home Assistant 时添加 `homeassistant_api: true`，并将你的 `SUPERVISOR_TOKEN` 视为管理员凭据。

你也可以直接通过 `homeassistant` 的 8123 端口连接到 Home Assistant，但那时你需要用户的访问令牌，并且必须了解用户如何配置 Home Assistant。代理几乎总是更好的选择。

## Supervisor API {#the-supervisor-api}
Supervisor API 位于 `http://supervisor/`，使用相同的令牌：

```bash
curl -sSL \
  -H "Authorization: Bearer ${SUPERVISOR_TOKEN}" \
  http://supervisor/addons/self/info
```

每个应用可以在没有额外权限的情况下调用几个端点：

- `/addons/self/...`：关于你自己应用的信息，包括其选项、日志和统计数据。你也可以启动、停止和重启它。更改其安全设置或更新它不包括在内：这需要 `hassio_api` 及允许的角色。
- `/info`：系统的一般信息。
- `/services` 和 `/discovery`：[/apps/guides/services-discovery/ 上的服务和发现]。
- `/auth`：用户认证，使用 `auth_api: true`。
- `/supervisor/ping`：完全不需要令牌。

对于其他任何操作，请添加 `hassio_api: true`。你之后可以调用的内容取决于 `hassio_role`：`default` 角色可以读取每个 `info` 端点，而其他角色会增加更多权限。角色信息在 [保护你的应用](/apps/guides/security#api-roles)，端点信息在 [Supervisor API 参考](/apps/supervisor-api) 中。使用 Bashio，这些大多数调用都是单个函数，而且 Bashio 会为你添加令牌：

```bash
#!/command/with-contenv bashio

hostname=$(bashio::info.hostname)
port=$(bashio::app.ingress_port)

# An endpoint without a function of its own. Bashio returns the "data" part. {#an-endpoint-without-a-function-of-its-own-bashio-returns-the-data-part}
info=$(bashio::api.supervisor GET /addons/self/info)
```

每个函数都在 [Bashio 参考文档](/apps/bashio) 中。

## 其他应用程序 {#other-apps}
应用程序之间通过内部网络互相通信，就像任何其他网络服务一样：使用另一个应用程序的主机名和它监听的端口。这里不涉及权限；另一个应用程序在网络内部暴露的内容都是可访问的。

对于一些常见服务，Supervisor 可以为你提供连接详情，因此用户无需手动输入。请参阅 [共享服务和发现集成](/apps/guides/services-discovery)。

## 向你的应用程序发送输入 {#send-input-to-your-app}
在 `config.yaml` 中使用 `stdin: true`，Home Assistant 可以通过 `hassio.app_stdin` 动作写入你的应用程序的标准输入：

```yaml
actions:
  - action: hassio.app_stdin
    data:
      app: local_hello_world
      input: "restart"
```

Home Assistant 在发送之前将 `input` 编码为 JSON，因此文本 `restart` 到达时为 `"restart"`，包括引号，而映射会作为 JSON 对象到达。Supervisor 会将数据原样写入你的应用程序的标准输入。
