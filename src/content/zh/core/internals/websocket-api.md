---
title: API (韩语)
description: 前端使用的API. 连接是如何工作的,核心命令,错误处理,以及如何从集成中添加你自己的命令.
sidebarGroup: 你说的
order: 31
---

# API (韩语) {#websocket-api}

Home Assistant 在 `/api/websocket` 服务 WebSocket API 。 它是主要的API:前端和伴生的应用程序几乎将它用于一切,可以随其发生而流变. 整合后会将自己的命令添加到其中,因此比这个页面列表还多得多的命令.

JavaScript 使用 [Home Assistant-js-websocket](https://github.com/home-assistant/home-assistant-js-websocket) 库 。 它处理认证,重新连接,和订阅,它是前端使用的.

## 连接如何运作 {#how-a-connection-works}

1. 客户端连接. 服务器发送`auth_required`.
2. 客户端发送`auth` 消息并带有访问符 。
3. 服务器 你在回答 `auth_ok` 或 `auth_invalid` 并关闭连接 。
4. 指挥阶段开始. 客户端发送命令,服务器发送结果和订阅消息.
5. 双方都关闭了连接.

每个消息都是带有 `type` 的 JSON 对象 。 在命令阶段,客户端的每条消息也有一个{H在现有资源范围内}:一个随每个命令而增加的数字. 服务器将 `id` 放在它发回的所有信件上, 这样您就可以匹配到命令的答案 。

## 4.a(a)的合格后得到过合格后后得到过合格后后得到过过合格后后后得到过过过过过过等等等等等等等等等等等的合格后后才能得到过合格的合格后后后后才能得到过。等等等等等等等等合格后后才能得到合格后后后才能得到合格后后后才能得到过。等等等等等等等等等等等等等等等等等等等等等等等等等等等等等等等等、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、等等、、、、、、、、、、、、、、、、、、、、、、、、、、、、 {#authentication}

连接后,服务器发送:

```json
{
  "type": "auth_required",
  "ha_version": "2026.10.0"
}
```

发送访问令牌。 如何获得一个,请参看[认证 API](/core/internals/auth-api)。

```json
{
  "type": "auth",
  "access_token": "ABCDEFGH"
}
```

如果该符号有效:

```json
{
  "type": "auth_ok",
  "ha_version": "2026.10.0"
}
```

如果没有,则使用 `message` 获得 `auth_invalid` , 而服务器断开 。

## 启用特性 {#enable-features}

在认证后,一个客户端可以打开带有`supported_features`的可选特性. 今天,唯一的功能是 `coalesce_messages`:服务器然后将信件捆绑成批发送,作为JSON列表,而不是逐个发送.

```json
{
  "id": 1,
  "type": "supported_features",
  "features": {
    "coalesce_messages": 1
  }
}
```

## 结果和错误 {#results-and-errors}

1995- 3⁄4 ̄ ̧漯B

```json
{
  "id": 6,
  "type": "result",
  "success": true,
  "result": null
}
```

当出错时,`success`是`false`,`error`有一个`code`和一个`message`:

```json
{
  "id": 12,
  "type": "result",
  "success": false,
  "error": {
    "code": "invalid_format",
    "message": "Message incorrectly formatted: required key not provided"
  }
}
```

错误代码包括`invalid_format`,`not_found`,`not_allowed`,`not_supported`,`unauthorized`,`unknown_command`,`id_reuse`,`home_assistant_error`,`service_validation_error`,`template_error`,`timeout`和`unknown_error`. 当错误来自有翻译信息的`HomeAssistantError`时,错误还有`translation_domain`,`translation_key`和`translation_placeholders`,所以前端可以用用户的语言显示.

## 核心命令 {#core-commands}

这些是`websocket_api`整合本身的命令.

### 订阅事件 {#subscribe-to-events}

```json
{
  "id": 18,
  "type": "subscribe_events",
  "event_type": "state_changed"
}
```

省略`event_type` 以获得所有事件 。 这,以及大多数事件类型,都需要一个管理员。 每个事件都作为`event`类型的信息出现,订阅的`id`:

```json
{
  "id": 18,
  "type": "event",
  "event": {
    "event_type": "state_changed",
    "data": {
      "entity_id": "light.kitchen",
      "old_state": {},
      "new_state": {}
    },
    "origin": "LOCAL",
    "time_fired": "2026-10-10T10:37:24.265429+00:00",
    "context": {
      "id": "01J9Z7K1M3S8TQ0Y6E4H2B5N7C",
      "parent_id": null,
      "user_id": null
    }
  }
}
```

各州在此缩短. 要跟随状态,`subscribe_entities`效率更高.

### 取消订阅 {#unsubscribe}

结束任何订阅。 `subscription` 是启动集体行动的命令的`id` 。

```json
{
  "id": 19,
  "type": "unsubscribe_events",
  "subscription": 18
}
```

### 订阅实体 {#subscribe-to-entities}

`subscribe_entities`是前端如何跟随状态。 它以紧凑的格式发送用户可以先读的所有状态,然后只发送更改. 通过`entity_ids`来限制它。

```json
{
  "id": 20,
  "type": "subscribe_entities",
  "entity_ids": ["light.kitchen"]
}
```

每个 `event` 建议将最多有 3 个密钥的 映射 : `a` 被添加的实体完全压缩状态, `c` 被更改的实体只改变什么( 在 `+` 下) , 在 `-` 下删除属性) , 以及 `r` 被删除实体的ID 。 在压缩状态下,`s`是状态,`a`是属性,`c`是上下文,`lc`是最后一次更改,`lu`是最后一次更新.

### 订阅到触发器 {#subscribe-to-a-trigger}

页:1 订阅一个或多个 [触发](/glossary/trigger),格式与自动化相同. 每次触发点火时都会收到`event`信息,并带有触发变量。

```json
{
  "id": 2,
  "type": "subscribe_trigger",
  "trigger": {
    "trigger": "state",
    "entity_id": "binary_sensor.motion",
    "to": "on"
  }
}
```

### 要求行动 {#call-an-action}

```json
{
  "id": 24,
  "type": "call_service",
  "domain": "light",
  "service": "turn_on",
  "service_data": {
    "brightness": 255
  },
  "target": {
    "entity_id": "light.kitchen"
  }
}
```

`service_data`和`target`是可选的。 结果有 `context` 调用。 要获得[响应数据](/core/integrations/actions#return-response-data),请添加`"return_response": true`。 结果还有 `response` :

```json
{
  "id": 24,
  "type": "result",
  "success": true,
  "result": {
    "context": {
      "id": "01J9Z7K1M3S8TQ0Y6E4H2B5N7C",
      "parent_id": null,
      "user_id": "31ddb597e03147118cf8d2f8fbea5553"
    },
    "response": {}
  }
}
```

### 启动一个事件 {#fire-an-event}

页:1 启动一个事件, 可选的 `event_data` 。 结果有`context`。

```json
{
  "id": 25,
  "type": "fire_event",
  "event_type": "my_integration_button_pressed",
  "event_data": {
    "button_id": "front_door"
  }
}
```

### 去拿东西 {#get-things}

每个都只需一个 `id` 和一个 `type`, 并在 `result` 中返回数据 :

- `get_states`:用户可以读到的所有状态 。
- 求助于 `get_config`: [核心配置作出有效调整](/core/internals/hass#the-core-configuration)。
- `get_services`:所有动作,都有它们的描述.
- `get_panels`:注册的面板。 这个来自`frontend`整合。

### ing {#ping}

衲子发送 `{"id": 19, "type": "ping"}` 和服务器回答 `{"id": 19, "type": "pong"}`.衲子用作为心跳来检查连接是活的.

### 校验配置 {#validate-configuration}

`validate_config` 检查 `triggers`, `conditions` 和`actions` 仿佛是自动化的一部分。 每个密钥都是可选的,只有你发送的密钥才会回来.

```json
{
  "id": 30,
  "type": "validate_config",
  "triggers": [],
  "conditions": [],
  "actions": []
}
```

```json
{
  "id": 30,
  "type": "result",
  "success": true,
  "result": {
    "triggers": {"valid": true, "error": null},
    "conditions": {"valid": false, "error": "Invalid condition"},
    "actions": {"valid": true, "error": null}
  }
}
```

### 与目标合作 {#work-with-targets}

这些命令采用与动作调用相同的 `target` 格式,其中 `entity_id`, `device_id`, `area_id`, `floor_id` 和 `label_id` :

- `extract_from_target`:将目标解决为`referenced_entities`,`referenced_devices`和`referenced_areas`,并列出`missing_devices`,`missing_areas`,`missing_floors`和`missing_labels`中不存在的东西. 以 `"expand_group": true` 组合替换为成员 。 默认为 `false` 。
- {H0在以下方面:},`get_conditions_for_target`和`get_services_for_target`: 返回至少适用于目标实体之一的触发器、条件或动作, 如`light.turn_on`。 这里, `expand_group` 默认为`true` 。

### 更多命令 {#more-commands}

核心指令还包括`render_template`,`subscribe_condition`,`test_condition`,`execute_script`,`entity/source`,`manifest/list`,`manifest/get`和`integration/setup_info`. 除了这些之外,几乎所有与UI注册的整合都属于自己的命令. 以下在 [集成命令](/core/internals/websocket-api#integration-commands) 下描述一些所依赖的应用程序和其他客户端。 其余部分,前端的源头是查看其名称的最佳地点.

## 整合命令 {#integration-commands}

这些命令不是ضر `websocket_api` 本身,而是来自前端时总是加载的集成. companyion应用软件和其他客户端使用它们,所以其格式是合同.

### 列出要显示的实体 {#list-entities-for-display}

`config/entity_registry/list_for_display`来自`config`的集成。 它以紧凑的格式返回实体注册:就是客户端需要显示的实体,带有短密钥以保持消息小. 任何经认证的用户都可以调用. 它不需要参数。

```json
{
  "id": 40,
  "type": "config/entity_registry/list_for_display"
}
```

```json
{
  "id": 40,
  "type": "result",
  "success": true,
  "result": {
    "entity_categories": {"0": "config", "1": "diagnostic"},
    "entities": [
      {
        "ei": "light.living_room",
        "pl": "hue",
        "ai": "living_room",
        "lb": [],
        "di": "a1b2c3d4e5f6",
        "np": "area",
        "hn": true,
        "en": "Ceiling"
      },
      {
        "ei": "sensor.living_room_signal",
        "pl": "esphome",
        "lb": [],
        "di": "f6e5d4c3b2a1",
        "np": "device",
        "tk": "signal",
        "ec": 1,
        "hn": true,
        "dp": 0
      }
    ]
  }
}
```

`entity_categories` 将数字映射到 [实体类别](/core/entities/registry) 。 实体在 `ec` 中用这个号码指其类别,而不是重复字符串。 JSON 密钥总是字符串,所以数字的到来是`"0"`和`"1"`.

`entities` 拥有登记册中未禁用的所有实体。 残疾实体被排除在外,无论谁残疾。 没有登记记录的实体,如没有独特身份证明的实体,也不在名单上。 每个实体都有这些钥匙。 只有`ei`,`pl`和`lb`总是在那里。 其他的则在没有价值时被忽略.

| 密钥 | 类型 | 含义 |
| --- | --- | --- |
| `ei` | 字符串 | 实体身份 |
| `pl` | 字符串 | 平台:提供实体的集成,如`hue`. |
| `lb` | 字符串列表 | 实体标签的ID. 无空列表 。 |
| `ai` | 字符串 | 实体本身所指定区域的ID 。 未设定当实体仅从其设备中获取其区域时 。 |
| `di` | 字符串 | 实体所属设备的ID. |
| `np` | 字符串 | 当建立实体的全名时下一个名称: `area` 当实体有自己的区域时, 否则`device` 当它属于一个设备时。 |
| `ic` | 字符串 | 用户选择的图标, 如 `mdi:lightbulb` 。 它覆盖了国家的图标。 |
| `tk` | 字符串 | 实体的翻译密钥,用于翻译其名称和状态. |
| `ec` | 编号 | 实体类别,作为`entity_categories`的密钥. |
| `hb` | 布尔 | `true`当实体被隐藏时,由用户或集成. |
| `hn` | 布尔 | 当实体 [使用 `has_entity_name`](/core/entities/naming) 时, 其名称不包括设备名称 。 |
| `en` | 字符串 | 实体名. 用户设置的名称,否则就是集成后的名称. 对于一个不使用`has_entity_name`的集成,从集成开始的名称蓉从它开始的时候,设备名称被剥离. |
| `dp` | 编号 | 只有传感器:要显示的小数。 用户设定的精度,否则整合暗示的精度. |

对于完整的注册条目,包含所有字段,使用`config/entity_registry/list`(所有条目)或`config/entity_registry/get_entries` (`entity_ids`的列表条目).

### 向语音助理介绍实体 {#expose-entities-to-voice-assistants}

{促进发展中国家}的集成 追踪哪些实体接触到哪个语音助理。 这些命令管理着它。 他们都需要一个管理员

助理由这些身份识别,命令不接受其他人:

- `conversation`: Assist
- `cloud.alexa`: 亚马逊 Alexa通过 Home Assistant Link
- `cloud.google_assistant`: Google Assist通过 Home Assistant Link 提供

#### 曝光或未曝光实体 {#expose-or-unexpose-entities}

`homeassistant/expose_entity`将实体暴露于或未暴露于一个或多个助手. 变化立即适用。

```json
{
  "id": 41,
  "type": "homeassistant/expose_entity",
  "assistants": ["conversation", "cloud.alexa"],
  "entity_ids": ["light.living_room", "sensor.outside"],
  "should_expose": true
}
```

| 外地 | 类型 | 含义 |
| --- | --- | --- |
| `assistants` | 字符串列表 | 要求。 助理来改变设置 |
| `entity_ids` | 字符串列表 | 要求。 要改变的实体。 身份证没有对现有实体进行检查。 |
| `should_expose` | 布尔 | 要求。 `true`要曝光,`false`不要暴露。 |

结果为`null`.

#### 列出已披露实体 {#list-exposed-entities}

`homeassistant/expose_entity/list` 不取参数并返回至少接触到一个助手的实体 。 每个实体向它所接触到的助手映射,总是带有`true`的值. 实体未接触的助手被排除在外,没有接触的实体也是如此。

```json
{
  "id": 42,
  "type": "homeassistant/expose_entity/list"
}
```

```json
{
  "id": 42,
  "type": "result",
  "success": true,
  "result": {
    "exposed_entities": {
      "light.living_room": {
        "conversation": true,
        "cloud.alexa": true
      },
      "sensor.outside": {
        "conversation": true
      }
    }
  }
}
```

列表中包含所储存的东西. Home Assistant 当某人曝光或未曝光时, 存储一个实体的设置, 以及第一次助理询问它是否使用该实体 。 在此之前,一个实体不在列表中,即使下面的缺省规则会暴露它.

#### 默认曝光新实体 {#expose-new-entities-by-default}

每个助理都有一个设置,可以决定新实体是否自动接触到它. `homeassistant/expose_new_entities/get`读一个`assistant`:

```json
{
  "id": 43,
  "type": "homeassistant/expose_new_entities/get",
  "assistant": "conversation"
}
```

```json
{
  "id": 43,
  "type": "result",
  "success": true,
  "result": {
    "expose_new": true
  }
}
```

在更改之前, 设置为 `true` `conversation` 和 `false` 其他助手 。

`homeassistant/expose_new_entities/set`改变它。 需要 `assistant` 和 `expose_new` (布尔语) 。 结果是`null`。

```json
{
  "id": 44,
  "type": "homeassistant/expose_new_entities/set",
  "assistant": "cloud.alexa",
  "expose_new": true
}
```

随着设置,并不是每个新的实体都会暴露出来. 当一个实体没有实体类别且没有隐藏时,它默认会暴露出来,其中一个是真实的:

- 其域为`climate`,`cover`,`fan`,`humidifier`,`light`,`media_player`,`scene`,`switch`,`todo`,`vacuum`,或`water_heater`。
- 它是具有设备类`door`,`garage_door`,`lock`,`motion`,`opening`,`presence`或`window`的二进制传感器.
- 它是设备类的传感器 {对这种设备, `aqi`,`carbon_monoxide`,`carbon_dioxide`,`humidity`,`pm10`,`pm25`,`temperature`,或`volatile_organic_compounds`。

## 添加您自己的命令 {#add-your-own-command}

包含 `websocket_api.async_register_command` 的集成注册命令, 通常在 `async_setup` 中 。 命令以域名命名, 如 `my_integration/devices` 。

```python
from typing import Any

import probatio

from homeassistant.components import websocket_api
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.typing import ConfigType

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up my integration."""
    websocket_api.async_register_command(hass, websocket_list_devices)
    return True

@websocket_api.websocket_command(
    {
        probatio.Required("type"): "my_integration/devices",
        probatio.Optional("include_offline", default=False): bool,
    }
)
@websocket_api.async_response
async def websocket_list_devices(
    hass: HomeAssistant,
    connection: websocket_api.ActiveConnection,
    msg: dict[str, Any],
) -> None:
    """Return the devices of my integration."""
    devices = await async_get_devices(hass, msg["include_offline"])
    connection.send_result(msg["id"], {"devices": devices})
```

- 设定计划。 您的处理器运行前, 信件已被验证 。
- `async_response`是给那些属于Coroutine函数的处理者的。 不等待的处理器可以是`@callback`而不是`async_response`。
- 苟将命令限制为管理员 。 苟置于其他装饰者之上.
- `connection.user` 是用户。 使用 `connection.context(msg)` 作为您代表它们所做的任何事的上下文 。 见[权限](/core/internals/permissions).
- `connection.send_result(msg["id"], result)` 响应命令。 `connection.send_error(msg["id"], code, message)` 报告出错, 其中一条代码来自`websocket_api`, 如`websocket_api.ERR_NOT_FOUND` 。

### 订阅 {#subscriptions}

对于流更新的命令,将结束订阅的函数存储在 `connection.subscriptions[msg["id"]]` 中. Home Assistant 当客户端不订阅或断开时调用它 。 以 `connection.send_message(websocket_api.event_message(msg["id"], data))` 发送更新 。

```python
@callback
@websocket_api.websocket_command(
    {probatio.Required("type"): "my_integration/subscribe"}
)
def websocket_subscribe(
    hass: HomeAssistant,
    connection: websocket_api.ActiveConnection,
    msg: dict[str, Any],
) -> None:
    """Send updates of my integration to the client."""

    @callback
    def forward(data: dict[str, Any]) -> None:
        connection.send_message(
            websocket_api.event_message(msg["id"], data)
        )

    connection.subscriptions[msg["id"]] = async_dispatcher_connect(
        hass, SIGNAL_UPDATE, forward
    )
    connection.send_result(msg["id"])
```
