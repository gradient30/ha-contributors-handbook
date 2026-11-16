---
title: 日期实体
description: 构建逍遥实体,让人们在一个设备上设定日历日期,比如假日模式的开始.
sidebarLabel: 日期
sidebarGroup: 投入和帮助
---

# 日期实体 {#date-entity}

一个日期实体让人们在一个设备或服务上设定一个日历日期,没有时间. 想想节假日模式开始的日期, 或者下一个过滤器需要替换的日期 。 从`DateEntity` 继承到`homeassistant.components.date` 。

还需要一天的时间吗? 使用 [日期和时间](/core/entities/datetime) 实体 。 只是一天的时间? 使用 [时间](/core/entities/time) 实体 。 日期是设备只报告的东西吗? 就像安装的日期一样? 这是一个 [传感器](/core/entities/sensor) 设备类 `date` 。

## 的临时议程 {#properties}

| 名称 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- |
| `native_value` | `datetime.date \| None` | 要求数 | 目前的日期。 |

一个日期实体没有设备类,也没有状态属性:两者都是最终的,总是`None`. 每个实体的通用属性,如`name`,`available`和`unique_id`,都在[实体类别](/core/entities/entity-class)上.

## 支持的特性 {#supported-features}

该实体没有支持的特性。

## 方法 {#methods}

### 设定值 {#set-value}

当有人在UI中选择日期,或者一个自动化或脚本调用`date.set_value`动作时调用. 实施其中之一。

```python
class MyDate(DateEntity):
    

# Implement one of these methods. {#states}

    def set_value(self, value: date) -> None:
        """Set a new date."""

    async def async_set_value(self, value: date) -> None:
        """Set a new date."""
```

## 状态 {#example}

藜麦的状态为`native_value`,以ISO 8601格式,如`2026-12-24`. 这是`unknown` 当`native_value`是`None`。

## 示例 {#示例}

```python
from datetime import date

from homeassistant.components.date import DateEntity
from homeassistant.const import EntityCategory

class ExampleHolidayStart(DateEntity):
    """The first day of the holiday mode."""

    _attr_has_entity_name = True
    _attr_translation_key = "holiday_start"
    _attr_entity_category = EntityCategory.CONFIG

    def __init__(self, device: ExampleDevice) -> None:
        """Initialize the date entity."""
        self._device = device
        self._attr_unique_id = f"{device.serial}_holiday_start"
        self._attr_native_value = device.holiday_start

    async def async_set_value(self, value: date) -> None:
        """Set the first day of the holiday mode."""
        await self._device.set_holiday_start(value)
        self._attr_native_value = value
        self.async_write_ha_state()
```
