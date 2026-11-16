---
title: 系统保健
description: 在系统信息页面上显示您整合的状态, 如服务器能否到达以及还剩多少配额 。
sidebarGroup: 融合特征
order: 5
---

# 系统保健 {#system-health}

系统信息页面显示 Home Assistant 如何进行, 每一个集成部分。 用户在 **Settings ** > **System ** > **Repairs **,菜单右上方,**System information **中查找. 他们将其复制到问题中,因此对于帮助排除故障的事实来说,这是一个好的地方:服务器是否可以被到达,集成的服务器是连接到的,或者请求配额还剩下多少.

## 增加系统健康 {#add-system-health}

创建 `system_health.py`,并登记返回信息的函数:

```python
from typing import Any

from homeassistant.components import system_health
from homeassistant.core import HomeAssistant, callback

@callback
def async_register(
    hass: HomeAssistant, register: system_health.SystemHealthRegistration
) -> None:
    """Register the system health info."""
    register.async_register_info(system_health_info)

async def system_health_info(hass: HomeAssistant) -> dict[str, Any]:
    """Return the system health info."""
    info: dict[str, Any] = {
        

# Checking the server can take a while, so pass the coroutine {#texts}
        "can_reach_server": system_health.async_check_can_reach_url(
            hass, API_ENDPOINT
        ),
    }

    entries: list[ExampleConfigEntry] = (
        hass.config_entries.async_loaded_entries(DOMAIN)
    )
    if entries:
        quota = await entries[0].runtime_data.client.get_quota()
        info["remaining_requests"] = quota.remaining

    return info
```

只计算装入的 `runtime_data` 条目 。 `async_entries` 还返回被忽略、禁用、设置失败或卸载的条目。 卸载移除 `runtime_data`, 而其他人可能从未拥有过 。 使用 `async_loaded_entries` , 并处理没有案件 。

值可以是任意一种,也可以是焦耳. 对于一个胸围,前端显示一个旋转器,完成后填写结果. `async_check_can_reach_url` 是是否可以到达 URL 的现成检查 。

`async_register_info` 也需要 `manage_url`, 链接到用户可以管理集成或账户的地方 。

## 文本 {#文本}

在 `strings.json` 中, 在 `system_health` 下给每个密钥一个标签 :

```json
{
  "system_health": {
    "info": {
      "can_reach_server": "Reach Example server",
      "remaining_requests": "Remaining allowed requests"
    }
  }
}
```
