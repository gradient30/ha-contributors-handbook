---
title: 自动添加新设备
description: '已启动的 " 标码 " : " 标码 " : "标码 " : "标码 " : "标码 " : "标码 " : "标码 " : "标码 "
  : "标码 " : "标码 " : "标码 " : "标码 " : "标码 " : "标码 " : "标码 "'
sidebarLabel: 动态设备
sidebarGroup: 黄金
order: 12
---

# 自动添加新设备 {#add-new-devices-automatically}

这是黄金规则 在`quality_scale.yaml`中,它被称为`dynamic-devices`.

当一个新设备在集成建立后出现时,如新光对接到一个枢纽或者在云账户中添加到一个新的设备,集成会自己创建其实体. 用户不需要重新装入集成或重新启动Home Assistant.

## 为什么这很重要 {#why-it-matters}

用户在他们的枢机或账户中添加一个设备,并期望它在Home Assistant中出现. 要知道需要重新装填, 在哪里找到它, 是那种摩擦 戈德是要去除的。

这是[固态设备](/core/quality-scale/stale-devices)的另一面:设备来去,Home Assistant跟着。

## 示例 {#example}

使用 [协调员](/glossary/coordinator) 跟踪平台已经知道的设备 。  b. 我说过:

```python
async def async_setup_entry(
    hass: HomeAssistant,
    entry: MyConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up the sensors of My integration."""
    coordinator = entry.runtime_data
    known_devices: set[str] = set()

    @callback
    def _add_new_devices() -> None:
        new_devices = set(coordinator.data) - known_devices
        if not new_devices:
            return

        known_devices.update(new_devices)
        async_add_entities(
            MySensor(coordinator, device_id) for device_id in new_devices
        )

    _add_new_devices()
    entry.async_on_unload(coordinator.async_add_listener(_add_new_devices))
```

配置条目卸载时, 通过 `entry.async_on_unload` 将收听器删除 。

在此示例中, `known_devices` 只在条目加载时才会增长 。 当集成还移除了像[固态设备](/core/quality-scale/stale-devices)描述的已消失的设备时,一个后来返回的设备仍然在`known_devices`中,其实体在条目重新加载之前不会再次添加. 也从`known_devices`中丢弃被移除的设备,所以在返回时被作为新设备处理.

## 如何检查 {#how-it-is-checked}

已检阅.

## 例外 {#exceptions}

与每个配置条目的单个固定设备的集成,即与配置条目同时存在并进行,不受此规则约束.

## 相关规则 {#related-rules}

- [固态设备](/core/quality-scale/stale-devices) : 删除 Stale 设备 。
