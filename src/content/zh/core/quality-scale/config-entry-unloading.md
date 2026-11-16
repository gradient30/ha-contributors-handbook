---
title: 支持卸载配置条目
description: 银规则配置-进场-卸载:整合可以卸载并重新装载,无需重启.
sidebarLabel: 配置- 输入- 卸载
sidebarGroup: 银
order: 2
---

# 支持卸载配置条目 {#support-unloading-the-config-entry}

这是Silver的规则 在`quality_scale.yaml`中,它被称为`config-entry-unloading`.

整合必须在 `__init__.py` 中执行 `async_unload_entry` 。已提交 [配置条目](/glossary/config-entry) 卸下后, 集成会卸下其平台并清理它所设置的一切: 收听器,订阅,背景任务,以及打开连接.

## 为什么这很重要 {#why-it-matters}

在 Home Assistant 持续运行时, 卸载是重新装入、 禁用或删除一个集成的可能性 。 没有它,用户必须重新启动Home Assistant来应用更改或摆脱集成. 而没有清理的东西 总是在背景中运行, 利用内存和连接白费力气。

## 示例 {#example}

卸载平台,并在成功时清理:

```python
async def async_unload_entry(
    hass: HomeAssistant, entry: MyConfigEntry
) -> None:
    """Unload a config entry."""
    await hass.config_entries.async_unload_platforms_or_raise(
        entry, PLATFORMS
    )
    await entry.runtime_data.client.disconnect()
```

`async_unload_platforms_or_raise` 当向它们提供平台卸货失败时, 升起 `ConfigEntryError`, 因此, 只有在卸货成功时才会进行清理 。

通常,你不需要跟踪 清理自己。 设置时用 `entry.async_on_unload` 注册, Home Assistant 给您打电话 :

```python
async def async_setup_entry(
    hass: HomeAssistant, entry: MyConfigEntry
) -> None:
    """Set up My integration from a config entry."""
    client = MyClient(entry.data[CONF_HOST])
    entry.async_on_unload(client.subscribe(_handle_event))
    ...
```

以 `entry.async_on_unload` 注册的回调在 `async_unload_entry` 成功时运行, 以及当 `async_setup_entry` 失败时运行: 当它升起时, 如 `ConfigEntryNotReady`, `ConfigEntryAuthFailed` 或 `ConfigEntryError` 。 您仍需要 `async_unload_entry` 本身 : 没有它, 无法卸载 。

## 如何检查 {#how-it-is-checked}

- Pylint, 当规则是 `done` 时 : `__init__.py` 必须定义 `async_unload_entry` (`home-assistant-missing-config-entry-unloading`) 。
- 在 [测试覆盖率](/core/quality-scale/test-coverage) 中显示测试从未运行的代码, 因此通常需要卸载条目的测试 。
- 检查是否清理了所有东西。

## 例外 {#exceptions}

这一规则没有例外。

## 相关规则 {#related-rules}

- [实体活动设置](/core/quality-scale/entity-event-setup):订阅实体生命周期中的事件.
