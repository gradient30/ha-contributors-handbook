---
title: 共享服务并发现集成
description: 向其他应用提供 MQTT 代理或 MySQL 数据库，使用时无需向用户询问详细信息，并让 Home Assistant 为你的应用设置集成。
order: 7
---


# 共享服务并发现集成 {#share-services-and-discover-integrations}
Supervisor 帮助应用程序互相找到对方，并且 Home Assistant 可以找到你的应用程序，因此用户不必输入主机名、端口和密码。有两种机制：

- **服务**：提供服务的应用程序，例如 MQTT 代理，会注册其连接详细信息。其他应用程序可以读取这些信息。
- **发现**：应用程序告诉 Home Assistant 它正在运行，Home Assistant 会提供设置匹配 [集成](/glossary/integration) 的选项。

## 服务 {#services}
支持两种服务：`mqtt` 和 `mysql`。在 `config.yaml` 中列出你的应用程序可以使用的服务，并标明角色：

```yaml
services:
  - mqtt:want
```

| 角色 | 含义 |
| --- | --- |
| `provide` | 你的应用程序提供此服务 |
| `want` | 你的应用程序可以使用此服务，但无需依赖它也能工作 |
| `need` | 你的应用程序需要此服务才能工作 |

你的应用程序只能读取或写入它列出的服务。一次只能有一个应用程序提供某项服务。

### 使用服务 {#use-a-service}
从 Supervisor API、在 `GET /services/mqtt` 或使用 Bashio 读取连接详细信息：

```bash
#!/command/with-contenv bashio

if bashio::services.available "mqtt"; then
  mqtt_host=$(bashio::services mqtt "host")
  mqtt_port=$(bashio::services mqtt "port")
  mqtt_user=$(bashio::services mqtt "username")
  mqtt_password=$(bashio::services mqtt "password")
else
  bashio::log.warning "No MQTT broker found"
fi
```

提供这些详细信息的选项也是一种良好做法，这样用户就可以连接到未作为应用程序运行的代理。

### 提供服务 {#provide-a-service}
当你的应用启动时，会使用 `POST /services/mqtt` 注册其详细信息，当不再提供服务时，会使用 `DELETE /services/mqtt` 移除这些信息。在 `config.yaml` 中使用 `provide` 列出服务：移除注册需要该角色。

| 服务 | 键 |
| --- | --- |
| `mqtt` | `host` 和 `port`（必填），`username`，`password`，`ssl`（默认 `false`），以及 `protocol`（`3.1` 或 `3.1.1`，默认值） |
| `mysql` | `host` 和 `port`（必填），`username`，以及 `password` |

使用 Bashio：

```bash
#!/command/with-contenv bashio

config=$(bashio::var.json \
  host "$(hostname)" \
  port "^1883" \
  username "app" \
  password "${password}")

bashio::services.publish "mqtt" "${config}"
```

为使用你的服务的应用创建一个单独的用户，而不是共享管理员账户。官方的 Mosquitto broker 应用完全遵循这一做法，是一个很好的示例可供参考。

## 发现 {#discovery}
发现功能让你的应用向 Home Assistant 说“我在这里，这是联系我的方式”。然后，Home Assistant 会在 **设置** > **设备与服务** 下显示已发现的集成，用户只需进行一次确认即可设置。

### 发送发现消息 {#send-a-discovery-message}
在 `config.yaml` 中按域列出你的应用发送发现的集成：

```yaml
discovery:
  - adguard
```

然后，当你的应用启动后，向 `POST /discovery` 发送一条消息，域为 `service`，连接详情在 `config` 中：

```bash
#!/command/with-contenv bashio

config=$(bashio::var.json \
  host "$(hostname)" \
  port "^3000")

if bashio::discovery "adguard" "${config}" > /dev/null; then
  bashio::log.info "Sent discovery information to Home Assistant"
else
  bashio::log.error "Discovery message to Home Assistant failed!"
fi
```

Supervisor 会拒绝不在你的 `discovery` 列表中的域的消息。响应中包含 `uuid`，你可以使用它通过 `DELETE /discovery/<uuid>` 再次删除该消息。当应用被卸载时，其消息会被删除。

### 在集成中接收它 {#receive-it-in-the-integration}
在 Home Assistant 端，与该域的集成需要一个名为 `hassio` 的 [配置流程](/glossary/config-flow) 步骤。它会接收你发送的 `config` 所包含的 `HassioServiceInfo`、你应用的 `name` 和 `slug`，以及消息的 `uuid`：

```python
async def async_step_hassio(
    self, discovery_info: HassioServiceInfo
) -> ConfigFlowResult:
    """Handle discovery from an app."""
    await self._async_handle_discovery_without_unique_id()
    self._config = discovery_info.config
    return await self.async_step_hassio_confirm()
```

像 AdGuard Home、ESPHome、Matter、MQTT 和 Z-Wave 这样的集成已经有了这个步骤。要为新的集成添加发现功能，请参阅 [核心和集成](/core) 部分。
