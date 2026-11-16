---
title: 地理定位实体
description: 在地图上显示来自外部种子的有位置的事件,如地震或野火.
sidebarLabel: 地理位置
sidebarGroup: 传感器与状态
---

# 地理定位实体 {#geolocation-entity}

一个地理定位实体代表一个有位置的外部事件:地震,野火,洪水警告,或来自饲料的另一个兴趣点. 每个实体都有坐标,前端显示为地图上的标记. 从`GeolocationEvent`继承,从`homeassistant.components.geo_location`导入。

与大多数实体不同,一个地理定位实体不代表一个设备. 其住随事供养.

## 的临时议程 {#properties}

| 名称 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- |
| `source` | `str` | 要求数 | 事件来自何处,通常是您整合的领域. |
| `distance` | `float \| None` | `None` | 从主位置到活动距离, 在`unit_of_measurement`. 此为州. |
| `latitude` | `float \| None` | `None` | 事件的纬度. |
| `longitude` | `float \| None` | `None` | 事件的经度. |

用通用 `unit_of_measurement` 属性设置距离的单位 。 `source`,`latitude`和`longitude`成为状态属性,坐标四舍五入为小数五。 每个实体的通用属性都在 [实体类别](/core/entities/entity-class) 上 。

## 支持的特性 {#supported-features}

该实体没有支持的特性。

## 管理活动 {#managing-events}

集成会随着种子的改变而添加并删除地理定位实体. 一个常见的模式是管理者订阅以提供更新,并在每次更新时:

1. 为每个新事件添加实体。
2. 更新仍在主持了的事件的实体。
3. 删除已删除的事件的实体, 方法是拨打 `await entity.async_remove(force_remove=True)` 。

`force_remove`旗完全删除州. 没有它,一个注册实体就无法进入。对上述实体进行识别时,如果实体有唯一的ID,请从 [非常大实体登记处](/core/entities/registry) 中删除其条目。

[GDACS 整合](https://github.com/home-assistant/core/blob/dev/homeassistant/components/gdacs/geo_location.py) 遵循这个模式, 而[演示平台](https://github.com/home-assistant/core/blob/dev/homeassistant/components/demo/geo_location.py) 是它的最小版本 。

## 方法 {#methods}

没有执行方法。 当种子改变时更新属性并呼叫 `async_write_ha_state` 。 见[更新状态](/core/entities/state-updates)和[实体生命周期](/core/entities/lifecycle)。

## 状态 {#states}

状态为 `distance`,四舍五入为小数点之一,或当没有距离时为 `unknown`. 基础类设置: 不要设置 `state` 自己 。

## 示例 {#example}

一个来自种子的地震实体:

```python
from homeassistant.components.geo_location import GeolocationEvent
from homeassistant.const import UnitOfLength

class ExampleQuakeEvent(GeolocationEvent):
    """An earthquake from the example feed."""

    _attr_has_entity_name = True
    _attr_should_poll = False
    _attr_source = "example_quakes"
    _attr_unit_of_measurement = UnitOfLength.KILOMETERS

    def __init__(self, quake: ExampleQuake) -> None:
        """Initialize the event."""
        self._attr_unique_id = quake.id
        self._attr_name = quake.title
        self.update_from_feed(quake)

    def update_from_feed(self, quake: ExampleQuake) -> None:
        """Copy the latest data from the feed."""
        self._attr_distance = quake.distance_km
        self._attr_latitude = quake.latitude
        self._attr_longitude = quake.longitude
```

名从供养故不译. 见[名称](/core/entities/naming).
