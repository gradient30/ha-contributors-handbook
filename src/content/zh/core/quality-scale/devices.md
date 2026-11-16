---
title: 创建设备
description: 黄金规则设备:实体被分组在设备中,有完整的设备信息.
sidebarLabel: 设备
sidebarGroup: 黄金
order: 1
---

# 创建设备 {#create-devices}

这是黄金规则 在`quality_scale.yaml`中,它被称为`devices`.

集成创建 [设备](/glossary/device) 并添加其实体 。 一种装置代表一种物理装置,或一种服务。 完全填写设备信息,如集成可以:名称,制造商,型号,序列号,软件和硬件版本,以及使设备可以识别的连接和标识符.

## 为什么这很重要 {#why-it-matters}

人们在设备中思考,而不是在实体中思考. 他们给Home Assistant添加了恒温器或气象服务,而不是传感器列表. 设备将这些实体组合在一个地方,有一个设备页面,显示设备是什么以及它运行的固件.

完整的设备信息在别处也有效果. 序列号和模型帮助用户和支持找到正确的设备,类似MAC地址的连接让其他集成和发现识别到相同的设备.

## 示例 {#example}

在实体上设定 `_attr_device_info` 。 具有相同识别特征的实体最终会在同一设备上:

```python
class MySensor(SensorEntity):
    """A sensor of My device."""

    _attr_has_entity_name = True

    def __init__(self, device: MyDevice) -> None:
        """Initialize the sensor."""
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, device.serial)},
            connections={(CONNECTION_NETWORK_MAC, device.mac)},
            name=device.name,
            manufacturer="My Company",
            model="My Sensor",
            model_id="ABC-123",
            serial_number=device.serial,
            sw_version=device.firmware,
            hw_version=device.revision,
        )
```

一个坐落在中枢后面的设备可以指向中枢使用`via_device_id`,中枢的设备注册ID. 当设备是服务而不是物理设备时,如天气服务或云账户,添加`entry_type=DeviceEntryType.SERVICE`.

大多数集成器一次设置设备信息,在 `entity.py` 中的共享基实体中. 见[常用模块](/core/quality-scale/common-modules).

## 如何检查 {#how-it-is-checked}

已检阅. 设备信息必须是`DeviceInfo`,而不是普通词典. Home Assistant 目前仍然接受一个词典,但只有 mypy 拒绝它,并且只有在集成输入时才会接受. 见[通过实体注册设备](/core/integrations/device-registry#register-a-device-through-an-entity).

## 例外 {#exceptions}

这一规则没有例外。

## 相关规则 {#related-rules}

- [有实体名称](/core/quality-scale/has-entity-name):使用有 实体 名称。
