---
title: Thread安全
description: 当您的代码运行在事件环路之外时, 要呼叫哪个 API, 以及如何修复线程安全错误 Home Assistant 报告 。
sidebarGroup: 自动同步
order: 11
---

# Thread安全 {#thread-safety}

几乎Ayncio中的所有东西都不安全,而且Home Assistant的核心对象也不安全. 从另一个线程调用 `async_` 方法会腐蚀事件循环的内部状态 。 其结果不是干净的错误,而是随机的错误行为和重启,这非常难以追溯.

所以,Home Assistant检查。 许多 `async_` API 验证它们是从事件循环线索调用 。 如果不是,Home Assistant用堆栈跟踪报告呼叫,并屏蔽它以保持系统的稳定. 如果你从这样的报告到这里: 堆积的追踪点 在发出呼叫的代码。

## 规则 {#the-rule}

- 在事件循环中,在coroutine或`@callback`中:呼叫`async_`版本.
- 在另一个线程中, 如执行器任务或同步库的调回: 调用版本而不使用 `async_`, 或者在事件循环上安排工作 。

## 通常的原因: 缺失@ callback {#the-usual-cause-a-missing-callback}

承担某项功能的帮助者通过查看来决定如何运行. Coroutine 函数或以 `@callback` 装饰的函数在事件循环中运行 。 任何其它东西都被假定是阻断和运行在执行器中.

```python
from homeassistant.const import STATE_UNAVAILABLE, STATE_UNKNOWN
from homeassistant.core import Event, EventStateChangedData, callback
from homeassistant.helpers.event import async_track_state_change_event

async def async_added_to_hass(self) -> None:
    """Start tracking the other light."""
    self.async_on_remove(
        async_track_state_change_event(
            self.hass, ["light.other"], self._async_light_changed
        )
    )

@callback
def _async_light_changed(
    self, event: Event[EventStateChangedData]
) -> None:
    """Follow the state of the other light."""
    new_state = event.data["new_state"]
    if new_state is None or new_state.state in (
        STATE_UNAVAILABLE,
        STATE_UNKNOWN,
    ):
        return

    self.async_write_ha_state()
```

没有 `@callback`, `_async_light_changed` 运行在一个线程中, 而`async_write_ha_state` 是从错误线程调用 。 修行为一.

## 从线程: 取而代之的是什么 {#from-a-thread-what-to-call-instead}

| 如果出现循环 | 从另一线索 |
| --- | --- |
| `hass.async_create_task` | `hass.create_task` |
| `hass.bus.async_fire` | `hass.bus.fire` |
| `hass.services.async_register` | `hass.services.register` |
| `hass.services.async_remove` | `hass.services.remove` |
| `hass.states.async_set` | `hass.states.set` |
| `self.async_write_ha_state()` | `self.schedule_update_ha_state()` |
| `async_dispatcher_send` | `dispatcher_send` |
| `issue_registry.async_create_issue` | `issue_registry.create_issue` |
| `issue_registry.async_delete_issue` | `issue_registry.delete_issue` |

一些API根本没有线程安全版本:

- 区域、类别、设备、实体、地板和标签登记册,包括`async_get_or_create`、`async_update_entity`】、`async_update_device`和`async_remove`。
- `hass.config_entries.async_update_entry` 和 `hass.config_entries.async_update_subentry` 。
- 渲染模板, 如 `async_render_to_info` 。
- 忽略 `issue_registry.async_ignore_issue` 的问题 。
- 用 `issue_registry.async_refresh_issues` 刷新一组问题, 并且保留 `issue_registry.async_keep_issue` 的问题 。 见[从另一线索刷新](/core/integrations/repairs#refresh-from-another-thread).

对于这些,在事件循环上安排一个函数来发出呼叫. `hass.add_job`从任何线程中都这样做 :

```python
from homeassistant.core import callback

@callback
def _async_update_title(entry: ConfigEntry, title: str) -> None:
    """Update the title of the config entry."""
    hass.config_entries.async_update_entry(entry, title=title)

# In a thread: {#in-a-thread}
hass.add_job(_async_update_title, entry, "New title")
```

最好还是问问自己 为什么代码会成线运行 通常它是一个同步库,可以被包裹一次,在边缘,所以其余的整合都生活在事件循环中.

## 提前查找错误 {#find-errors-early}

开发时打开调试模式, 在 `configuration.yaml` 下启用 `debug: true` 。 然后检查更多电话 立即报告 见[显示在 Home Assistant](/core/internals/asyncio#find-mistakes-early).
