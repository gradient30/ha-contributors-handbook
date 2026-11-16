---
title: 订阅实体生命周期中的事件
description: 青铜规则实体-事件设置:实体以aync add to has订阅,删除时不订阅.
sidebarLabel: 实体活动设置
sidebarGroup: 青铜
order: 14
---

# 订阅实体生命周期中的事件 {#subscribe-to-events-in-the-entity-lifecycle}

此是铜法. 在`quality_scale.yaml`中,它被称为`entity-event-setup`.

当 [实体](/glossary/entity) 订阅事件时, 例如要更新由整合库驱动, 它必须在 `async_added_to_hass` 中订阅, 并在删除时取消订阅 。 不要订阅 `__init__` 。

## 为什么这很重要 {#why-it-matters}

Home Assistant在实体平台注册后拨打`async_added_to_hass`。 从那一刻起,实体拥有它所需要的一切,比如`self.hass`和`self.async_write_ha_state`. 点火前的回击 并试图写一个状态,失败。

解约之事亦复如是. 一个被移除的实体,或者其配置条目被卸下但仍被订阅的实体,不断接收事件. 这样会泄露记忆,并且可以为一个已经不存在的实体写状态.

## 示例 {#example}

最简单的方式是`async_on_remove`. 它需要未订阅的功能,在实体被移除时调用它,所以你不必亲自跟踪它:

```python
class MySensor(SensorEntity):
    """A sensor that gets pushed updates."""

    def __init__(self, client: MyClient) -> None:
        """Initialize the sensor."""
        self.client = client

    async def async_added_to_hass(self) -> None:
        """Subscribe to updates when added to Home Assistant."""
        await super().async_added_to_hass()
        self.async_on_remove(
            self.client.events.subscribe("update", self._handle_update)
        )

    @callback
    def _handle_update(self, event: MyEvent) -> None:
        """Handle an update from the device."""
        self._attr_native_value = event.value
        self.async_write_ha_state()
```

如果您需要更多的控制, 请在 `async_will_remove_from_hass` 中取消订阅 。 基于 `CoordinatorEntity` 的实体已经为它们的协调员这样做了, 所以您只需要它来订阅自己的文件 。

## 如何检查 {#how-it-is-checked}

已检阅.

## 例外 {#exceptions}

如果集成实体不订阅事件,则不适用本规则.

## 相关规则 {#related-rules}

- [配置- 输入- 卸载](/core/quality-scale/config-entry-unloading): 支持卸载配置条目 。
