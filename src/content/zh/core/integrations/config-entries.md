---
title: 配置条目
description: 配置条目是如何设置、卸载、删除和迁移的,您的整合将保存运行时间数据。
sidebarGroup: 设置和配置
order: 1
---

# 配置条目 {#config-entries}

A [配置条目](/glossary/config-entry) 是一个集成的设置实例, 如一个惠桥或一个账户 。 存储它,并在每次开始时再次设置. 用户通过您的集成的 [配置流量](/core/integrations/config-flow) 创建配置项, 然后可以通过 [重组](/core/integrations/reauth-reconfigure) 或 [选项流动](/core/integrations/options-flow) 修改 。

配置条目控件 :

- `data`:连接所需的配置,如主机或API令牌. 正常使用期间不变.
- `options`: 设置用户可以通过选项流改变 。
- `subentries`:可重复的部分,如天气服务的地点. 见[子条目](/core/integrations/subentries).
- `unique_id`:什么是设备或账户的标识,所以没有设置两次 。
- `runtime_data` : 无论您在运行时的整合需要什么 。 它没有储存。

## 生命周期 {#lifecycle}

从 `homeassistant.config_entries.ConfigEntryState` 开始, 配置条目总是在其中的一个州 :

| 状态 | 含义 |
| --- | --- |
| `NOT_LOADED` | 未载. 配置条目创建时的状态, 以及 Home Assistant 何时开始 。 |
| `SETUP_IN_PROGRESS` | 被设置 |
| `LOADED` | 设置和运行 |
| `SETUP_ERROR` | 设置失败, 而 Home Assistant 不重试 |
| `SETUP_RETRY` | 设置失败, 因为有些东西还没有准备好 。 Home Assistant在与 `retry_after` 合并要求时, 以越来越大的延迟进行重试, 最多10分钟或更长 。 |
| `MIGRATION_ERROR` | 配置条目需要向新版本迁移, 失败了 |
| `UNLOAD_IN_PROGRESS` | 被卸载 |
| `FAILED_UNLOAD` | 卸载失败或不支持 |

您的代码最终在 `SETUP_ERROR` 或 `SETUP_RETRY` 中如何在 [设置失败和例外](/core/integrations/setup-failures) 中描述 。

## 确定其配置条目 {#set-up-a-config-entry}

当 {H极为重视} 开始时, 它首先运行您整合的正常设置 (`async_setup`, 如果您有的话) 。 然后它在您的 `__init__.py` 中为每个配置条目调用 `async_setup_entry`, 除了用户已禁用或忽略的除外 。 当用户添加新配置条目时, Home Assistant 立即为该条目调用 `async_setup_entry` 。

```python
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_HOST, Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .coordinator import ExampleCoordinator

PLATFORMS = [Platform.SENSOR, Platform.SWITCH]

type ExampleConfigEntry = ConfigEntry[ExampleCoordinator]

async def async_setup_entry(
    hass: HomeAssistant, entry: ExampleConfigEntry
) -> None:
    """Set up Example from a config entry."""
    client = ExampleClient(
        entry.data[CONF_HOST], session=async_get_clientsession(hass)
    )

    coordinator = ExampleCoordinator(hass, entry, client)
    await coordinator.async_config_entry_first_refresh()

    entry.runtime_data = coordinator

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
```

`async_setup_entry` 什么都没有。 返回时,设置成功,条目为`LOADED`. 当设置无法成功时, 则提出例外, 所以 Home Assistant 知道是重试,开始重修,还是放弃. 见[设置失败和例外](/core/integrations/setup-failures). `async_unload_entry`和`async_migrate_entry`也一样。

### 将运行时间数据保存在运行时间 数据 {#keep-runtime-data-in-runtimedata}

在 `entry.runtime_data` 中存储您运行时的集成需求, 如 API 客户端或 [协调员](/glossary/coordinator) 。 键入上方的别名类型, 如 `ExampleConfigEntry` , 并使用该别名 。 您的平台然后可以免费获得 `runtime_data` 。

不对属于配置项的数据使用 `hass.data`。 `runtime_data`被清理的条目, 和类型检查器理解它。

### 设置平台 {#set-up-the-platforms}

在 `runtime_data` 设定后, 将配置条目转发到您的 [体现出来](/glossary/platform) 和 `async_forward_entry_setups` 。 每个平台然后获得自己的`async_setup_entry`,它增加了实体:

```python
from homeassistant.helpers.entity_platform import (
    AddConfigEntryEntitiesCallback,
)

async def async_setup_entry(
    hass: HomeAssistant,
    entry: ExampleConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up the Example sensors."""
    coordinator = entry.runtime_data

    async_add_entities(
        ExampleSensor(coordinator, description)
        for description in SENSORS
    )
```

## 卸载配置项 {#unload-a-config-entry}

支持卸载,这样用户就可以重新装入或禁用一个条目而不重新启动Home Assistant. 执行 `async_unload_entry` , 卸下您转发的平台, 并清理其它的, 如连接和收听器 。 Home Assistant 在调用此函数之前, 将状态设置为 `UNLOAD_IN_PROGRESS` 。

```python
async def async_unload_entry(
    hass: HomeAssistant, entry: ExampleConfigEntry
) -> None:
    """Unload a config entry."""
    await hass.config_entries.async_unload_platforms_or_raise(entry, PLATFORMS)
```

当其中一个平台卸载失败时,`async_unload_platforms_or_raise`会用一个翻译消息提出`ConfigEntryError`,条目会转到`FAILED_UNLOAD`. 如果自己的清理失败, 也提高 `ConfigEntryError` 。

大部分清理不需要自己的代码. 设置时注册, 当输入卸载时运行 Home Assistant :

```python
entry.async_on_unload(client.disconnect)
entry.async_on_unload(
    async_track_time_interval(hass, refresh_token, timedelta(hours=1))
)
```

要清理实体后, 请执行 `async_will_remove_from_hass` 在 [实体](/core/entities) 上 。

输入卸载时不要删除修复问题 。 重新装入条目也会卸下,一个被删除并再次创建的问题不再被忽略. 设置他们的 [`config_entry_id`](/core/integrations/repairs#issues-that-belong-to-a-config-entry) 而不是: 它们被隐藏在禁用条目时, 并在删除时删除 。

## 删除配置项 {#remove-a-config-entry}

如果当用户删除配置项时需要发生什么, 如删除服务中的 Webhook, 则执行 `async_remove_entry` 。 该条目在运行时已经从 `hass.config_entries` 中删除 。

```python
async def async_remove_entry(
    hass: HomeAssistant, entry: ExampleConfigEntry
) -> None:
    """Handle removal of an entry."""
```

您不需要 `async_remove_entry` 来清理条目的设备和实体, 或 [属于它的修理问题](/core/integrations/repairs#issues-that-belong-to-a-config-entry) 。 Home Assistant为您移除它们。

## 更改配置条目 {#change-a-config-entry}

遵照 `ConfigEntry` 的属性, 拨打`async_update_entry`代替。遵照规定,

```python
hass.config_entries.async_update_entry(
    entry, data={**entry.data, CONF_HOST: new_host}
)
```

要重新装入条目, 例如更改后, 请拨打 `hass.config_entries.async_schedule_reload(entry.entry_id)` 。

## 移动一个配置条目 {#migrate-a-config-entry}

当您在配置条目中存储的数据改变形状时, 将您配置流程的版本撞上并迁移旧条目 。 每个配置条目都有一个主 `VERSION` 和一个 `MINOR_VERSION`, 这两个都默认为 `1` 。

- ** minor** 版本的凸起是相容的。 只添加旧代码可以忽略的东西,如默认的新密钥. 如果只有小版本的不同, Home Assistant 即使没有迁移也会设置条目 。 回到旧的Home Assistant版本的用户可以继续使用.
- ** 主要** 版本折叠不是。 当旧代码无法再读取条目时使用,如重命名或删除的密钥. 旧的 Home Assistant 版本无法设置迁移的条目, 除非用户恢复备份 。

设置您配置流程上的新版本 :

```python
class ExampleConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Example."""

    VERSION = 2
    MINOR_VERSION = 2
```

然后在 `__init__.py` 中执行 `async_migrate_entry`. Home Assistant 当存储的主要版本比您的配置流长时, 或者当主版本相同而小版本不同时, 在设置前调用它 。 包括一个 newer 次要版本,当用户降级Home Assistant时留下. 所以在每个步骤之前检查一下版本,留下你不知道的条目. 一个比您的配置流更新的主要版本的条目无法设置而不调用您的代码 。

在这个例子中,第2版将`ip_address`更名为`host`,旧的代码无法读取,所以这是一个大的凸起. 2.2版本增加了一个端口,旧的代码忽略了这个端口,所以是一个小的凸起:

```python
async def async_migrate_entry(
    hass: HomeAssistant, entry: ExampleConfigEntry
) -> None:
    """Migrate an old config entry."""
    if entry.version == 1:
        data = {**entry.data}
        data[CONF_HOST] = data.pop("ip_address")
        hass.config_entries.async_update_entry(
            entry, data=data, version=2, minor_version=1
        )

    if entry.version == 2 and entry.minor_version < 2:
        hass.config_entries.async_update_entry(
            entry,
            data={**entry.data, CONF_PORT: DEFAULT_PORT},
            minor_version=2,
        )
```

被更新的 Home Assistant 版本存储为 2. 3 的条目, 既通过未检查, 也按原样设置 。

您的移民返回或提高决定 接下来会发生什么:

| 结果下列方面: | 发生什么事 |
| --- | --- |
| 返回 `None` | 移民成功,设置仍在继续 |
| 提高 `ConfigEntryNotReady` | 设置停止, Home Assistant 稍后重试 |
| 提高 `ConfigEntryError` 或任何其他例外 | 设置停止, 条目为 `MIGRATION_ERROR` |

给 `ConfigEntryNotReady` 和`ConfigEntryError` 翻译信件, 这样您就可以告诉用户出错 。

`MIGRATION_ERROR`没有自己恢复。 如果用户可以修复原因,则创建[修理](/core/integrations/repairs),并在修复后从修复流中调用`hass.config_entries.async_retry_migration(entry_id)`.

## 自定义集成中的返回值 {#return-values-in-custom-integrations}

自定义集成可能仍然会像以前一样从 `async_setup_entry`, `async_unload_entry` 和 `async_migrate_entry` 返回布尔值, 并且不会贬值 。 这就是它的作用:

- `True`表示成功,如`None`.
- 问题以及"未能设置配置条目"等通用信息,成为`ConfigEntryError`. 该条目为`SETUP_ERROR`,`FAILED_UNLOAD`或`MIGRATION_ERROR`,用户会看到该消息.

切换到{H0有关方面} 和例外仍然值得: 以翻译消息提升自己的`ConfigEntryError`, 用户看到实际出错. 背景位于[结构讨论](https://github.com/home-assistant/architecture/discussions/1463)中.

## 跟踪状态变化 {#follow-state-changes}

要在一个条目更改状态时得到通知, 例如从 `LOADED` 到 `UNLOAD_IN_PROGRESS`, 请用 `async_on_state_change` 注册回调 。 它返回一个删除收听器的函数,这样您就可以听到条目卸载:

```python
entry.async_on_unload(entry.async_on_state_change(notify_me))
```

## 背景任务 {#background-tasks}

启动属于配置项的长运行任务 `entry.async_create_background_task(hass, coroutine, name)` 。 Home Assistant在输入卸下时取消它们,所以它们不会超过输入.
