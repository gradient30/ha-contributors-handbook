---
title: 旨在使命令添加 WebSocket
description: 将来自您集成的数据以 WebSocket 命令在 Core 中提供给前端, 从前端调用 。
order: 3
---

# 旨在使命令添加 WebSocket {#add-a-websocket-command}

前端通过 WebSocket 连接与 Core 交谈 。 当您的集成有数据前端需要时, 它不是一个实体状态或属性时, 添加 WebSocket 命令 。 命令可以回答一次,或者继续发送更新作为订阅.

## 在核心中 {#in-core}

一个命令是一个带有装饰器的函数,它可以设置其消息类型和数据计划. 该类型前缀为您的整合域 。

```python
from typing import Any

import probatio

from homeassistant.components import websocket_api
from homeassistant.core import HomeAssistant, callback

@websocket_api.websocket_command(
    {
        probatio.Required("type"): "example/get_status",
        probatio.Required("device_id"): str,
    }
)
@callback
def ws_get_status(
    hass: HomeAssistant,
    connection: websocket_api.ActiveConnection,
    msg: dict[str, Any],
) -> None:
    """Return the status of a device."""
    status = hass.data[DOMAIN].get(msg["device_id"])
    if status is None:
        connection.send_error(msg["id"], "not_found", "Device not found")
        return

    connection.send_result(msg["id"], {"status": status})
```

设置整合时注册命令 :

```python
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the example integration."""
    websocket_api.async_register_command(hass, ws_get_status)
    return True
```

您的整合在表单中不需要 `websocket_api` 作为依赖 。 命令以两种方式注册,一旦WebSocket即可使用。 API运行.

用 `@callback` 装饰的函数在 [事件循环](/glossary/event-loop) 中运行, 所以它不能做任何 I/O 。 当您的命令需要等待时, 需要等待设备或网络, 使它变成 `async` 并在 `websocket_command` 下方添加 `@websocket_api.async_response` :

```python
@websocket_api.websocket_command(
    {probatio.Required("type"): "example/refresh"}
)
@websocket_api.async_response
async def ws_refresh(
    hass: HomeAssistant,
    connection: websocket_api.ActiveConnection,
    msg: dict[str, Any],
) -> None:
    """Refresh all devices."""
    await hass.data[DOMAIN].async_refresh()
    connection.send_result(msg["id"])
```

添加 `@websocket_api.require_admin` 到只有管理员才能使用的命令 。

### 订阅 {#subscriptions}

对于更改的数据,发送第一个结果,然后发送每个更改上带有相同消息ID的事件. 存储一个在 `connection.subscriptions` 中停止更新的函数, 当前端不订阅或断开时 Core 调用它 :

```python
@websocket_api.websocket_command(
    {probatio.Required("type"): "example/subscribe_status"}
)
@callback
def ws_subscribe_status(
    hass: HomeAssistant,
    connection: websocket_api.ActiveConnection,
    msg: dict[str, Any],
) -> None:
    """Send status updates to the frontend."""

    @callback
    def on_update(status: dict[str, Any]) -> None:
        connection.send_event(msg["id"], status)

    connection.subscriptions[msg["id"]] = hass.data[DOMAIN].subscribe(
        on_update
    )
    connection.send_result(msg["id"])
```

[WebSocket API 参考](/core/internals/websocket-api) 覆盖 Core 的 WebSocket API 更深入 。

## 在前门 {#in-the-frontend}

将命令的类型 我们已经添加到 [`src/data/`](https://github.com/home-assistant/frontend/tree/dev/src/data) 中的模块中, 以您的整合命名 。 组件调用此函数, 绝不是原始消息 :

```ts
export interface ExampleStatus {
  status: string;
}

export const fetchExampleStatus = (
  hass: HomeAssistant,
  deviceId: string
) =>
  hass.callWS<ExampleStatus>({
    type: "example/get_status",
    device_id: deviceId,
  });

export const subscribeExampleStatus = (
  conn: Connection,
  onChange: (status: ExampleStatus) => void
) =>
  conn.subscribeMessage<ExampleStatus>(onChange, {
    type: "example/subscribe_status",
  });
```

`hass.callWS()` 返回一个承诺, 当 Core 发送一个时, 用错误拒绝 。 `subscribeMessage()` 返回未订阅函数的许诺 。 在一个组件中,从 `hassSubscribe()` 和 `SubscribeMixin` 返回它 清理它 。 [数据已为层](/frontend/architecture/data)解释模式。

自定义卡片和面 你不可以用相同的方式调用命令,使用`hass.callWS()`或`hass.connection.subscribeMessage()`。
