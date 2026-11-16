---
title: 使用设备类
description: 黄金规则实体-device类:实体在任何适合的地方使用设备类.
sidebarLabel: 实体设备类
sidebarGroup: 黄金
order: 14
---

# 使用设备类 {#use-device-classes}

这是黄金规则 在`quality_scale.yaml`中,它被称为`entity-device-class`.

实体使用一个 [设备类](/glossary/device-class) 适合的地方 。 一个温度传感器使用`SensorDeviceClass.TEMPERATURE`,一个门接触`BinarySensorDeviceClass.DOOR`,一个固件更新`UpdateDeviceClass.FIRMWARE`. [实体页面](/core/entities) 列出每个平台的设备类 。

## 为什么这很重要 {#why-it-matters}

一个设备类告诉 Home Assistant 一个实体衡量或代表什么, 并且很多基于此:

- 用户只有在知道设备类时,才能将传感器切换到另一个单元,比如从°C到°F.
- 可回答"客厅的温度是多少?".
- Google Assist ant 和 Amazon Alexa 知道如何曝光实体.
- 前端选择合适的图标,并用正确的方式显示状态,如"打开"而不是"打开"作为门.
- 实体可以以其设备类命名,因此不需要自己翻译.

## 示例 {#example}

这种传感器使用温度设备类. 它没有自己的名称,因此以设备类命名:"我的设备温度".

```python
class MyTemperatureSensor(SensorEntity):
    """The temperature of My device."""

    _attr_has_entity_name = True
    _attr_device_class = SensorDeviceClass.TEMPERATURE
    _attr_native_unit_of_measurement = UnitOfTemperature.CELSIUS

    def __init__(self, device: MyDevice) -> None:
        """Initialize the sensor."""
        self._attr_unique_id = f"{device.serial}_temperature"
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, device.serial)},
            name="My device",
        )
```

## 如何检查 {#how-it-is-checked}

- 当一个翻译密钥只重复设备类已经提供的名称(`home-assistant-redundant-translation-key`)时, Pylint 警告.
- 设备类是否适合, 以及是否缺少, 将检查 。

## 例外 {#exceptions}

如果集成没有实体,或其实体在没有设备类的平台上,如`light`,`tts`,或`conversation`,则该规则不适用.

## 相关规则 {#related-rules}

- [有实体名称](/core/quality-scale/has-entity-name):使用有 实体 名称。
- [实体翻译](/core/quality-scale/entity-translations): 翻译实体名称.
- [图标翻译](/core/quality-scale/icon-translations): 使用图标翻译 。
