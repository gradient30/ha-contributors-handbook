---
title: 在运行时间数据中存储运行时间数据 data
description: 青铜规则运行时数据:运行时数据存储于ConfigEntry. 运行时间 数据,带有一个输入的配置条目。
sidebarLabel: 运行时间数据
sidebarGroup: 铜
order: 17
---

# 在运行时间数据中存储运行时间数据 data {#store-runtime-data-in-runtime_data}

此是铜法. 在`quality_scale.yaml`中,它被称为`runtime-data`.

数据 [配置条目](/glossary/config-entry) 装入时需要集成, 如 API 客户端 或 [协调员](/glossary/coordinator) , 必须存储在 `entry.runtime_data` 中 。 不在`hass.data`中。 给配置条目一个显示 `runtime_data` 内容的类型 。 当集成也跟随 [严格打字](/core/quality-scale/strict-typing) 时, 需要输入的配置项, 您可以在任何地方使用 。

## 为什么这很重要 {#why-it-matters}

`runtime_data`属于一个配置条目,当该条目卸下时它就不见了. 没有共享的词典可以保持清洁,也没有与其他集成相撞的密钥. 因为配置条目是打字的,所以你的编辑器和 mypy完全知道`entry.runtime_data`是什么,并且在用户之前捕捉错误. 而每一个集成都以同样的方式存储其数据,这使得代码更容易为下一个人读取.

## 示例 {#example}

定义输入的配置حير ,并在 `async_setup_entry` 中指定 `runtime_data` :

```python
type MyConfigEntry = ConfigEntry[MyClient]

async def async_setup_entry(hass: HomeAssistant, entry: MyConfigEntry) -> None:
    """Set up My integration from a config entry."""
    client = MyClient(entry.data[CONF_HOST])
    entry.runtime_data = client

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
```

一个平台读回来,完全输入:

```python
async def async_setup_entry(
    hass: HomeAssistant,
    entry: MyConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up the sensors."""
    client = entry.runtime_data
```

获得配置项的协调员也应使用输入项:

```python
class MyCoordinator(DataUpdateCoordinator[MyData]):
    """Fetch data from the device."""

    config_entry: MyConfigEntry
```

当多个对象需要生活在 `runtime_data` 时, 把它们放在数据类中, 并将其作为类型使用 。

## 如何检查 {#how-it-is-checked}

- Hassfest, 当规则为 `done` 时: `async_setup_entry` 在 `__init__.py` 中必须指定 `entry.runtime_data` 。
- Hassfest, 当 [严格打字](/core/quality-scale/strict-typing) 也是 `done` 时: 配置项必须打字, 并且有别名, 其名称结束于 `ConfigEntry` 。 此检查在 `__init__.py` 中的 `async_setup_entry` 、 `async_unload_entry` 、 `async_migrate_entry` 、 `async_remove_entry` 和 `async_remove_config_entry_device` 中, 检查每个平台的 `async_setup_entry` 、 诊断功能 和 `async_get_options_flow` 。
- Pylint, 对于每个配置流的集成 : `home-assistant-use-runtime-data` 当集成存储数据在 `hass.data[DOMAIN]` 时警告 。
- Pylint : `home-assistant-coordinator-untyped-config-entry` 当一个协调员不使用其集成的已打入的配置条目时警告.

## 例外 {#exceptions}

如果集成没有任何运行时间数据可存储,则本规则不适用.

## 相关规则 {#related-rules}

- [严格打字](/core/quality-scale/strict-typing):使用严格的打字.
- [设置前测试](/core/quality-scale/test-before-setup):在设置时检查连接.
