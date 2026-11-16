---
title: 空气质量实体
description: 腐烂的空气质量实体, 以及用什么代替。
sidebarLabel: 空气质量
sidebarGroup: 传感器和状态
---

# 空气质量实体 {#air-quality-entity}

空气质量实体将若干空气质量读数,如微粒物质和臭氧,捆绑成一个实体。 它来源于`AirQualityEntity`,导入自`homeassistant.components.air_quality`.

> [!WARNING]
> 空气质量实体贬值。 不要在新代码中使用它。 为每次读取创建 [传感器](/core/entities/sensor) , 其设备类类似 `PM25`, `OZONE`, `CO2` 或 `AQI` 。 仍然使用空气质量实体的集成器应当移动到传感器上.

单独的传感器得到单位转换, 长期统计, 和他们自己的历史, 这实体从来没有。

## 的临时议程 {#properties}

此实体不支持 `_attr_` 的简称 。 作为属性执行每个值。

| 名称 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- |
| `particulate_matter_2_5` | `str \| int \| float \| None` | 要求数 | 分解物质2.5微米或较小。 此为州. |
| `particulate_matter_10` | `str \| int \| float \| None` | `None` | 还应分解10微米或较小的物质。 |
| `particulate_matter_0_1` | `str \| int \| float \| None` | `None` | 分解物质为0.1微米或较小。 |
| `air_quality_index` | `str \| int \| float \| None` | `None` | 空气质量指数. |
| `ozone` | `str \| int \| float \| None` | `None` | 臭氧(O3)。 |
| `carbon_monoxide` | `str \| int \| float \| None` | `None` | 一氧化碳(CO). |
| `carbon_dioxide` | `str \| int \| float \| None` | `None` | 二氧化碳(CO2). |
| `sulphur_dioxide` | `str \| int \| float \| None` | `None` | 二氧化硫(SO2). |
| `nitrogen_oxide` | `str \| int \| float \| None` | `None` | 氧化氮(N2O). |
| `nitrogen_monoxide` | `str \| int \| float \| None` | `None` | 一氧化氮(NO). |
| `nitrogen_dioxide` | `str \| int \| float \| None` | `None` | 二氧化氮(NO2). |

每个不是`None`的值都成为状态属性. 每个实体的通用属性都在 [实体类别](/core/entities/entity-class) 上 。

## 支持的特性 {#supported-features}

该实体没有支持的特性。

## 方法 {#methods}

没有执行方法。 将属性保持为 `update` 或 `async_update` 。

## 状态 {#states}

状态为`particulate_matter_2_5`,单位为μg/m3.

## 示例 {#example}

而不是空气质量实体,将每个读数描述为传感器:

```python
from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.const import UnitOfDensity

SENSORS = (
    SensorEntityDescription(
        key="pm25",
        device_class=SensorDeviceClass.PM25,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement=UnitOfDensity.MICROGRAMS_PER_CUBIC_METER,
    ),
    SensorEntityDescription(
        key="aqi",
        device_class=SensorDeviceClass.AQI,
        state_class=SensorStateClass.MEASUREMENT,
    ),
)
```

完整图片参见[传感器实体](/core/entities/sensor).
