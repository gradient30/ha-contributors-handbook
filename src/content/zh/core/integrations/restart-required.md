---
title: 请求重新启动
description: 告诉 Home Assistant 它需要一个重新启动来应用更改, 而不会引起修复问题 。
sidebarLabel: 需要重新启动
sidebarGroup: 融合特征
order: 6
---

# 请求重新启动 {#asking-for-a-restart}

一些更改只在 Home Assistant 重新启动后生效, 比如更新到自定义集成, 或者一个仅在启动时读到的设置 。 您的整合不需要 [修理](/core/integrations/repairs) 的问题 。 它要求重启,并且Home Assistant将所有这些请求收集到用户的一个指标中,并附上所请求的集成列表.

## 更新实体 {#update-entities}

对于 [更新实体](/core/entities/update),将 `restart_required` 设置为 `True` 。 一旦一个安装完成而不提升,更新实体会代表您的集成请求重启 。 安装失败不会 。

```python
class MyUpdate(UpdateEntity):
    """Updates that need a restart to apply."""

    _attr_restart_required = True
```

也可以将其设置在实体描述上,带有`UpdateEntityDescription(restart_required=True)`.

## 还有什么 {#anything-else}

对于所有不是更新实体的东西,请联系您整合领域的助手 2009年

```python
from homeassistant.helpers import system_state

system_state.async_set_home_assistant_restart_required(hass, DOMAIN)
```

域名向用户显示,这样他们就可以看到等待重启的是什么. 多次询问是罚款: 您的整合被列出一次 。 从事件循环中调用助手 。

只问一次变化实际上是在等待重启. 别事先问

## 没办法拿回来 {#there-is-no-way-to-take-it-back}

一旦被询问, 重新启动将一直持续到 Home Assistant 重新启动 。 没有API可以清除它。 重新启动本身就可以清除,然后应用您的更改 。

融合也无从要求重启宿主. Supervisor 追踪主机是否需要重启, 而 `hassio` 集成会传递给Home Assistant 。

## 319目读取状态 {#reading-the-state}

您的整合不需要读这个状态 。 这是为前端。 管理员用户可以用 `subscribe_system_state` 订阅它 [WebSocket](/core/internals/websocket-api)命令。 它立刻发出现在的状态,

```json
{
  "home_assistant_restart_dismissed": false,
  "home_assistant_restart_required": true,
  "home_assistant_restart_sources": ["demo", "hacs"],
  "host_reboot_dismissed": false,
  "host_reboot_required": false
}
```

## 把它关掉 {#putting-it-off}

管理员可以推迟 `dismiss_system_state` WebSocket 命令的等待 。 这只隐藏在界面中: 仍然需要重启或重启, 而 `*_dismissed` 字段告诉订阅者它被推迟了 。

一个被推迟的重启在另一个整合要求时又出现了. 再次要求同样的融合并不能使其恢复。 一个淇瑞被推迟的重启 只有在等待启动的重启消失 并且Supervisor 提出一个新的启动后 才会回来。 全部没有存储, 因此 Home Assistant 的重新启动会忘记它 。
