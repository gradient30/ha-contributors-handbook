---
title: 时间实体
description: 这里是时间op 15.
sidebarLabel: 时间
sidebarGroup: 投入和帮助
---

# 时间实体 {#time-entity}

一个时间实体允许人们在设备或服务上设定一天的时间,没有日期. 想想什么时候闹钟会响 或者什么时候暖气会转换成夜间模式 从`TimeEntity` 继承到`homeassistant.components.time` 。

需要具体时间吗? 使用 [日期和时间](/core/entities/datetime) 实体 。 只有约会? 使用[日期](/core/entities/date)实体 。

## 的临时议程 {#properties}

| 名称 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- |
| `native_value` | `datetime.time \| None` | `None` | 今时. |

一个时间实体没有设备类,也没有状态属性:两者都是最终的,总是`None`. 每个实体的通用属性,如`name`,`available`和`unique_id`,都在[实体类别](/core/entities/entity-class)上.

## 支持的特性 {#supported-features}

该实体没有支持的特性。

## 方法 {#methods}

### 设定值 {#set-value}

当有人在UI中选择一个时间,或者一个自动化或脚本调用`time.set_value`动作时调用. 实施其中之一。

```python
class MyTime(TimeEntity):
    

# Implement one of these methods. {#states}

    def set_value(self, value: time) -> None:
        """Set a new time."""

    async def async_set_value(self, value: time) -> None:
        """Set a new time."""
```

## 状态 {#example}

藜麦的状态为`native_value`,以ISO 8601格式,如`07:30:00`. 这是`unknown` 当`native_value`是`None`。

## 示例 {#示例}

```python
from datetime import time

from homeassistant.components.time import TimeEntity
from homeassistant.const import EntityCategory

class ExampleWakeUpTime(TimeEntity):
    """The time the alarm clock goes off."""

    _attr_has_entity_name = True
    _attr_translation_key = "wake_up_time"
    _attr_entity_category = EntityCategory.CONFIG

    def __init__(self, device: ExampleDevice) -> None:
        """Initialize the time entity."""
        self._device = device
        self._attr_unique_id = f"{device.serial}_wake_up_time"
        self._attr_native_value = device.wake_up_time

    async def async_set_value(self, value: time) -> None:
        """Set the wake-up time."""
        await self._device.set_wake_up_time(value)
        self._attr_native_value = value
        self.async_write_ha_state()
```
