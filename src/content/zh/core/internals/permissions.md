---
title: 权限
description: 权限政策是如何构建和合并的,以及如何在动作中检查它们,HTTP视图和WebSocket命令.
sidebarGroup: 认证
order: 21
---

# 权限 {#permissions}

权限限制用户所能看到的和控制. 它们附属于组,一个用户获得所有组的合并权限. 拥有者是例外:许可从来不适用于拥有者,他总是可以做一切.

,                                                                                                                                                                                                                                                       第二部分是人们忘记的。

## 政策 {#policies}

政策是词平等原则。 其顶级有类别. 今天,政策只平等原则使用`entities`。

```python
{
    "entities": {
        "domains": {"switch": True},
        "entity_ids": {
            "light.kitchen": {"read": True, "control": True},
        },
    }
}
```

策略中的任意位置, 值可以是 `True` (允许) 或 `None` (使用默认值, 即拒绝) 。 缺失的类别被拒绝。

`entities` 分类有 `entity_ids` 、 `device_ids` 、 `area_ids` 、 `domains` 和 `all` 的子类别。 Home Assistant 按此顺序检查, 并使用第一个匹配的子类别 。 每个授权使用 `True` , 或每个授权使用 `read`,`control` 和`edit` 。

三个内设团体有这些政策:

| 组 | 政策 |
| --- | --- |
| 管理员 | `{"entities": True}` |
| 用户 | `{"entities": True}` |
| 只读 | `{"entities": {"all": {"read": True}}}` |

用户和管理员可以控制同样的实体. 将管理员分开的是什么 `user.is_admin`, 哪个代码会分别检查任何更改配置的东西 。

### 合并政策 {#merging-policies}

当用户分为若干组时,其政策被合并,按级别划分:

1. 如果轿车的值是 `True`,结果是 `True` 。
2. 如果任何值是字典,结果就是字典,与这些相同的规则合并.
3. 如果所有值都是`None`,结果就是`None`.

所以`{"entities": {"entity_ids": {"light.kitchen": True}}}`与`{"entities": {"entity_ids": True}}`合并后给`{"entities": {"entity_ids": True}}`。

## 上下文带有用户 {#the-context-carries-the-user}

每个动作呼吁,事件和状态都有`Context`,上下文有`user_id`. 这就是Home Assistant知道是谁干的 记录簿和许可检查

- 在动作处理器中,将 `call.context` 传递到任意你做什么。
- 在 HTTP 视图或 WebSocket 命令中, 为请求的用户创建上下文 。 两者都有一个帮助器:在视图中为`self.context(request)`,在WebSocket命令中为`connection.context(msg)`.

```python
await hass.services.async_call(
    "homeassistant",
    "restart",
    context=connection.context(msg),
    blocking=True,
)
```

## 检查权限 {#check-a-permission}

手持用户对象后,检查为一行:

```python
from homeassistant.auth.permissions.const import POLICY_CONTROL
from homeassistant.exceptions import Unauthorized

if not user.is_admin:
    raise Unauthorized()

if not user.permissions.check_entity(entity_id, POLICY_CONTROL):
    raise Unauthorized(entity_id=entity_id, permission=POLICY_CONTROL)
```

许可常数为`POLICY_READ`,`POLICY_CONTROL`和`POLICY_EDIT`.

当检查失败时, 请从 `homeassistant.exceptions` 升起 `Unauthorized` 。 它停止了你的行为,并告诉用户他们不被允许. 它的所有论据都是可选的 没成功的话帮助说:`context`,`user_id`,`entity_id`,`config_entry_id`,`perm_category` (当没有对象ID时,如创建配置条目时),和`permission`.

有些API向每个用户开放,但限制他们返回的内容,比如`get_states`在WebSocket上方 API,它只返回用户可能读取的实体.

## 在行动中 {#in-an-action}

为 `async_register_platform_entity_service` 实体注册的动作以及实体组件的动作, 请检查您的实体权限 。 对于只有管理员可以调用的动作,请在`async_register_admin_service`注册. 见[动作](/core/internals/actions).

如果您登记了对实体采取行动的简单动作,请自行检查:

```python
from homeassistant.auth.permissions.const import POLICY_CONTROL
from homeassistant.exceptions import Unauthorized, UnknownUser

async def async_handle_reset(call: ServiceCall) -> None:
    """Reset the given entities."""
    if call.context.user_id:
        user = await call.hass.auth.async_get_user(call.context.user_id)
        if user is None:
            raise UnknownUser(context=call.context)

        for entity_id in call.data["entity_id"]:
            if not user.permissions.check_entity(
                entity_id, POLICY_CONTROL
            ):
                raise Unauthorized(
                    context=call.context,
                    entity_id=entity_id,
                    permission=POLICY_CONTROL,
                )

    ...
```

不 `user_id` 表示该电话并非来自用户,而是来自 Home Assistant 本身, 如自动化 。

## 在 HTTP 视图中 {#in-an-http-view}

请求的用户位于 `request["hass_user"]` :

```python
from aiohttp import web

from homeassistant.helpers.http import KEY_HASS, HomeAssistantView
from homeassistant.exceptions import Unauthorized

class MyResetView(HomeAssistantView):
    """Reset everything, for admins only."""

    url = "/api/my_integration/reset"
    name = "api:my_integration:reset"

    async def post(self, request: web.Request) -> web.Response:
        """Handle the reset."""
        hass = request.app[KEY_HASS]
        user = request["hass_user"]
        if not user.is_admin:
            raise Unauthorized()

        hass.bus.async_fire(
            "my_integration_reset", context=self.context(request)
        )
        return self.json_message("Done.")
```

## 在 WebSocket 命令中 {#in-a-websocket-command}

用户为`connection.user`. 对于只管理命令,请使用 `require_admin` 装饰器 。 见[添加您自己的命令](/core/internals/websocket-api#add-your-own-command)在WebSocket API。
