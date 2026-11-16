---
title: 禁用吵闹或不太流行的实体
description: 'Gold 规则实体 - 默认失效: 很少用户需要的实体默认失效.'
sidebarLabel: 实体因违约而伤残
sidebarGroup: 黄金
order: 15
---

# 禁用吵闹或不太流行的实体 {#disable-noisy-or-less-popular-entities}

这是黄金规则 在`quality_scale.yaml`中,它被称为`entity-disabled-by-default`.

大多数用户不需要或经常改变其状态的实体默认被禁用。 想要它们的用户可以在实体设置中启用它们.

这些实体没有固定的清单。 这取决于装置。 Bluetooth温度传感器的信号强度对大多数人用处不大,因此默认是禁用. 对于一个用于测量信号强度的设备来说,同一个实体是主要特性,并保持启用.

## 为什么这很重要 {#why-it-matters}

Home Assistant 记录每个启用实体的历史 。 每个状态变化都花费了一点CPU,内存,和磁盘空间,吵闹的实体变化很大. 乘以家用设备的数量,加起来,特别是像Raspberry Pi这样的小硬件上.

默认使这些实体丧失能力意味着只有需要它们的用户才能支付这一费用。 它还使实体清单便于其他人管理。

## 示例 {#example}

```python
class MySignalStrengthSensor(SensorEntity):
    """The signal strength of My device."""

    _attr_has_entity_name = True
    _attr_entity_category = EntityCategory.DIAGNOSTIC
    _attr_device_class = SensorDeviceClass.SIGNAL_STRENGTH
    _attr_native_unit_of_measurement = SIGNAL_STRENGTH_DECIBELS_MILLIWATT
    _attr_entity_registry_enabled_default = False
```

带有实体描述, 在描述上设置 `entity_registry_enabled_default=False` 。

设定仅在实体首次加入实体登记处时才适用。 稍后更改它不会禁用用户已经拥有的实体 。

## 如何检查 {#how-it-is-checked}

已检阅.

## 例外 {#exceptions}

如果合并没有实体,或其任何实体都不吵或很少使用,则这一规则不适用。

## 相关规则 {#related-rules}

- [适当定价](/core/quality-scale/appropriate-polling):在适当的间隔时间进行民调.
