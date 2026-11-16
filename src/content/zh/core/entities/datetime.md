---
title: 日期和时间实体
description: 构建一个日期和时间实体,让人们在设备上设定一个时间点,就像充电会话开始时一样.
sidebarLabel: 日期和时间
sidebarGroup: 输入与助手
---

# 日期和时间实体 {#date-and-time-entity}

一个日期和时间实体让人们把一个完整的时刻设定在时间上,一个带有一天时间的日期,在一个设备或服务上. 想想充电会议何时开始 或者洗碗机何时必须完成 从`DateTimeEntity` 继承到`homeassistant.components.datetime` 。

只需要约会? 使用 [日期](/core/entities/date) 实体 。 一天只有一天,每天重复, 像唤醒时间? 使用 [时间](/core/entities/time) 实体 。 就像上次发射时一样 这是一个 [传感器](/core/entities/sensor) 设备类 `timestamp` 。

## 的临时议程 {#properties}

| 名称 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- |
| `native_value` | `datetime.datetime \| None` | 要求数 | 目前的日期和时间. 它必须包括一个时区。 |

一个日期和时间实体没有设备类和状态属性:两者都是最终的,总是`None`. 每个实体的通用属性,如`name`,`available`和`unique_id`,都在[实体类别](/core/entities/entity-class)上.

## 支持的特性 {#supported-features}

该实体没有支持的特性。

## 方法 {#methods}

### 设定值 {#set-value}

当有人在UI中选择日期和时间,或者一个自动化或脚本调用`datetime.set_value`动作时调用. 实施其中之一。

```python
class MyDateTime(DateTimeEntity):
    

# Implement one of these methods. {#states}

    def set_value(self, value: datetime) -> None:
        """Set a new date and time."""

    async def async_set_value(self, value: datetime) -> None:
        """Set a new date and time."""
```

你得到的价值总是有一个时区。 当动作获得一个没有日期和媳妇的时间时,它使用Home Assistant配置的时区.

## 状态 {#example}

状态为`native_value`,转换为UTC,以ISO 8601格式,有秒,如`2026-12-24T17:30:00+00:00`. 这是`unknown` 当`native_value`是`None`。

无时区 `native_value` 的 `ValueError` 当状态被写入时 。 使用 `homeassistant.util.dt` 中的助手来获取时区认知值, 如 `dt_util.as_local()` 或 `dt_util.utcnow()` 。

## 示例 {#示例}

```python
from datetime import datetime

from homeassistant.components.datetime import DateTimeEntity

class ExampleChargeStart(DateTimeEntity):
    """When the next charging session starts."""

    _attr_has_entity_name = True
    _attr_translation_key = "charge_start"

    def __init__(self, charger: ExampleCharger) -> None:
        """Initialize the date and time entity."""
        self._charger = charger
        self._attr_unique_id = f"{charger.serial}_charge_start"
        self._attr_native_value = charger.charge_start

    async def async_set_value(self, value: datetime) -> None:
        """Set when the next charging session starts."""
        await self._charger.set_charge_start(value)
        self._attr_native_value = value
        self.async_write_ha_state()
```
