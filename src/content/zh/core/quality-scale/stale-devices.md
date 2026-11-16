---
title: 删除 stale 设备
description: '黄金规则 Stale-devices: 已消失的装置被移除,或者可以被用户移除.'
sidebarLabel: 固态设备
sidebarGroup: 黄金
order: 21
---

# 删除 stale 设备 {#remove-stale-devices}

这是黄金规则 在`quality_scale.yaml`中,它被称为`stale-devices`.

当一个设备从集线器或账号中移除集线器连接时,集线器也会将其从Home Assistant中移除. 只有在确定设备已消失时才删除设备,例如,由于枢机返回了完整的设备列表,并且已经不在其中.

当集成无法确定时,它会执行`async_remove_config_entry_device`,所以用户可以自己从设备页面中删除设备.

## 为什么这很重要 {#why-it-matters}

一个设备已经不存在, 但仍出现在 Home Assistant 中, 并且没有可用的实体, 它很复杂 。 它出现在设备列表,仪表板和Assist中,用户无法摆脱它.

删除一个设备也会移除其实体,因此集成在自己完全清理之后.

## 示例 {#example}

当服务返回所有设备时,将新列表与上一个列表进行比较,并删除丢失的设备. 启动 `previous_devices` 作为协调员的 `__init__` 中的空集, 因此第一次刷新有可以比较的东西 :

```python
def __init__(
    self, hass: HomeAssistant, config_entry: MyConfigEntry, client: MyClient
) -> None:
    """Initialize the coordinator."""
    super().__init__(
        hass,
        _LOGGER,
        config_entry=config_entry,
        name=DOMAIN,
        update_interval=timedelta(minutes=1),
    )
    self.client = client
    self.previous_devices: set[str] = set()

async def _async_update_data(self) -> dict[str, MyDevice]:
    """Fetch the devices, and remove the ones that are gone."""
    try:
        data = await self.client.get_devices()
    except MyConnectionError as err:
        raise UpdateFailed(
            translation_domain=DOMAIN,
            translation_key="update_failed",
        ) from err

    if stale_devices := self.previous_devices - set(data):
        device_registry = dr.async_get(self.hass)
        for device_id in stale_devices:
            if device := device_registry.async_get_device_by_identifier(
                (DOMAIN, device_id), self.config_entry.entry_id
            ):
                device_registry.async_remove_device(device.id)

    self.previous_devices = set(data)
    return data
```

设定生活在内存中,因此每次配置输入负载时都会开始空置. 在 Home Assistant 被停止时消失的设备不在其中, 这种比较不会删除它 。 要捕获这些, 请将列表与设备注册中配置项的设备进行比较, 例如来自 `dr.async_entries_for_config_entry` 。

当集成只得到设备的更新,且没有完整的列表时,让用户删除一个已经安静下来的设备.  Marshal Home Assistant 当 `__init__.py` 有 `async_remove_config_entry_device` 时, 在设备页面上显示删除选项 。 返回 `True` 允许删除 :

```python
async def async_remove_config_entry_device(
    hass: HomeAssistant,
    entry: MyConfigEntry,
    device_entry: dr.DeviceEntry,
) -> bool:
    """Allow removing a device that no longer reports."""
    known_devices = entry.runtime_data.data
    return not any(
        identifier[0] == DOMAIN and identifier[1] in known_devices
        for identifier in device_entry.identifiers
    )
```

## 如何检查 {#how-it-is-checked}

已检阅.

## 例外 {#exceptions}

与每个配置条目的单个固定设备的集成,即与配置条目同时存在并进行,不受此规则约束.

## 相关规则 {#related-rules}

- [动态设备](/core/quality-scale/dynamic-devices): 自动添加新设备 。
