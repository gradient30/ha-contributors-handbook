---
title: 使用单位( T)
description: 青铜规则有-实体-名称:实体设置有 实体 名称为True,并在其设备的上下文中命名.
sidebarLabel: 有实体名称
sidebarGroup: 铜
order: 16
---

# 使用单位( T) {#use-has_entity_name}

此是铜法. 在`quality_scale.yaml`中,它被称为`has-entity-name`.

整合的每个实体必须设置 `has_entity_name` 到 `True` 。 然后实体的名称只描述它是什么,比如"Temperature",和Home Assistant将[设备](/glossary/device)的名称放在它前面需要的地方. 设备的主要特征是获得名称`None`,因此它取了设备本身的名称.

## 为什么这很重要 {#why-it-matters}

与 `has_entity_name`, Home Assistant 一同知道名称的哪个部分是设备, 哪个部分是实体 。 它可以在设备页面上显示"Temperature",其中设备是显而易见的,还可以在所有实体列表中显示"生活室传感器温度". 命名在每一个集成中都以同样的方式起作用,重新命名设备的用户在其所有实体上看到新名称.

它也是翻译实体名称的基础,这是黄金规则。

## 示例 {#example}

一个名为"我的装置"的装置上的传感器,叫做"我的装置温度":

```python
class MyTemperatureSensor(SensorEntity):
    """Temperature sensor of a device."""

    _attr_has_entity_name = True
    _attr_translation_key = "temperature"

    def __init__(self, device: MyDevice) -> None:
        """Initialize the sensor."""
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, device.serial_number)},
            name=device.name,
        )
```

作为设备主要特征的锁,称为"我的设备":

```python
class MyLock(LockEntity):
    """The lock of the device."""

    _attr_has_entity_name = True
    _attr_name = None
```

设定 `_attr_has_entity_name` 一次, 在 `entity.py` 的基准实体中, 您的所有实体都遵循 。

## 如何检查 {#how-it-is-checked}

Pylint, 当规则是 `done` 时 : `home-assistant-missing-has-entity-name` 当一个实体类并不总是将 `has_entity_name` 设置到 `True` 时, 无论是在类上, 在方法的开始, 或通过实体描述 。 取决于条件的值不计算。

## 例外 {#exceptions}

如果合并没有任何实体,则不适用这一规则。

## 相关规则 {#related-rules}

- [实体翻译](/core/quality-scale/entity-translations): 翻译实体名称.
- [实体设备类](/core/quality-scale/entity-device-class): 使用设备类.
- [设备](/core/quality-scale/devices): 创建设备.
