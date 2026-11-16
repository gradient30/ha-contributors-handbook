---
title: 热水器实体
description: 为将水加热到目标温度的锅炉和水箱建立热水器实体.
sidebarLabel: 热水器
sidebarGroup: 灯光和气候
---

# 热水器实体 {#water-heater-entity}

热水器实体控制一个能加热水的装置:锅炉,热水箱,或热泵热水器. 它具有目标温度,操作模式,以及可选的远离模式. 从`WaterHeaterEntity` 继承到`homeassistant.components.water_heater` 。

如果设备加热或冷却一个房间,则使用[气候实体](/core/entities/climate)代替.

前端如何显示热水器,请参见[热水器更多信息视图](/design/more-info/water-heater).

从 Home Assistant 演示中嵌入的仪表板卡的现场演示。 具有目标温度和操作模式的水热器,在瓦片卡中. 卡片为直播:改变温度或模式.

```html
<ha-embed-provider
  style="
    display: grid;
    grid-template-columns: repeat(12, minmax(0, 1fr));
    gap: 8px;
    align-items: start;
    max-width: 500px;
  "
>
  <script type="application/json">
    [
      {
        "entity_id": "water_heater.boiler",
        "state": "eco",
        "attributes": {
          "friendly_name": "Boiler",
          "current_temperature": 48,
          "temperature": 55,
          "min_temp": 40,
          "max_temp": 65,
          "target_temp_step": 1,
          "operation_list": [
            "eco",
            "electric",
            "performance",
            "off"
          ],
          "operation_mode": "eco",
          "supported_features": 11
        }
      }
    ]
  </script>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "tile",
        "entity": "water_heater.boiler",
        "features": [
          {
            "type": "target-temperature"
          },
          {
            "type": "water-heater-operation-modes"
          }
        ]
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

## 的临时议程 {#properties}

热水器实体在 [一般实体属性](/core/entities/entity-class) 之上有这些属性 。 每个属性都可以以其`_attr_`属性设定,如`_attr_current_operation`.

| 名称 | 类型 | 默认 | 说明 |
| ---- | ---- | ------- | ----------- |
| `native_temperature_unit` | `str` | 要求数 | 设备的单位报告温度为 `UnitOfTemperature.CELSIUS`、`UnitOfTemperature.FAHRENHEIT` 或`UnitOfTemperature.KELVIN` 。 |
| `current_operation` | `str \| None` | `None` | 当前操作模式 。 这是实体的状况。 |
| `operation_list` | `list[str] \| None` | `None` | 设备支持的操作模式 。 |
| `native_current_temperature` | `float \| None` | `None` | 测量水温,以`native_temperature_unit`表示。 |
| `native_target_temperature` | `float \| None` | `None` | 要达到的温度, 在`native_temperature_unit` 。 |
| `native_target_temperature_high` | `float \| None` | `None` | 目标范围的上限, 在 `native_temperature_unit` 中 。 |
| `native_target_temperature_low` | `float \| None` | `None` | 搁浅的目标范围, 以 `native_temperature_unit` 表示 。 |
| `target_temperature_step` | `float \| None` | `None` | 目标温度的阶梯大小, 在 `native_temperature_unit` 中 。 |
| `min_temp` | `float` | 110 °F | 最低目标温度,在`native_temperature_unit`。 默认值转换为您的单位 。 |
| `max_temp` | `float` | 140 °F | 最高目标温度,在`native_temperature_unit`。 默认值转换为您的单位 。 |
| `precision` | `float` | 摄氏十分之一,否则全数 | 精确温度以显示。 没有值,它遵循安装的单元系统已提交. |
| `is_away_mode_on` | `bool \| None` | `None` | 是否打开了 。 需要 `AWAY_MODE` 。 |

与气候实体一样,一个热水器报告设备单位的温度,Home Assistant将它们转换为安装的单位系统. 它与转换值的单位一起添加了 `temperature_unit` 状态属性 。 你不能推翻这个属性。 传到 `set_temperature` 的温度在您的方法被调用之前转换为 `native_temperature_unit` 。

> [!WARNING]
> 旧名没有`native_`,如`current_temperature`,`target_temperature`和`temperature_unit`(及其`_attr_`属性),则在Home Assistant2027.11中贬值并停止工作. 使用新代码中的 `native_` 名称 。

## 操作模式 {#operation-modes}

操作模式是字符串 。 Home Assistant 常数带有常见模式的内置翻译:

| 数值 | 说明 |
| ----- | ----------- |
| `STATE_ECO` | 节能模式,平衡性能和成本. |
| `STATE_ELECTRIC` | 只有电动元素的热量。 |
| `STATE_PERFORMANCE` | 性能最高,能耗较高. |
| `STATE_HIGH_DEMAND` | 为热水需求高而兴建. |
| `STATE_HEAT_PUMP` | 只加热泵的热量 |
| `STATE_GAS` | 只加气热. |
| `STATE_OFF` | 设备关闭了。 这个来自`homeassistant.const`。 |

您可以添加自己的模式, 并给它们一个翻译和图标, 并带有实体的 [翻译密钥](/core/entities/naming) (参见 [帖式图标](/core/entities/icons)) 。 Home Assistant 在调用 `operation_list` 之前检查模式 `operation_list` 的动作中, 当它不在列表中时, 则会出现一个验证错误 。

## 支持的特性 {#supported-features}

将 `WaterHeaterEntityFeature` 旗帜与 `|` 合并, 设置为 `supported_features`。 见 [支持的特性](/glossary/supported-features) 。

| 数值 | 说明 |
| ----- | ----------- |
| `TARGET_TEMPERATURE` | 目标温度可以设定. 执行`set_temperature`。 |
| `OPERATION_MODE` | 操作模式可以设定. 设定 `operation_list` 并执行 `set_operation_mode` 。 |
| `AWAY_MODE` | 该设备有一个离场模式. 执行`turn_away_mode_on`和`turn_away_mode_off`。 |
| `ON_OFF` | 设备可以打开或关闭. 执行`turn_on`和`turn_off`。 |

## 方法 {#methods}

执行岔或每种方法的同步变体,而不是两者。

| 就在那时 | Async 变体 | 特性 |
| ------ | ------------- | ------- |
| `set_temperature(**kwargs: Any)` | `async_set_temperature` | `TARGET_TEMPERATURE` |
| `set_operation_mode(operation_mode: str)` | `async_set_operation_mode` | `OPERATION_MODE` |
| `turn_away_mode_on()` | `async_turn_away_mode_on` | `AWAY_MODE` |
| `turn_away_mode_off()` | `async_turn_away_mode_off` | `AWAY_MODE` |
| `turn_on(**kwargs: Any)` | `async_turn_on` | `ON_OFF` |
| `turn_off(**kwargs: Any)` | `async_turn_off` | `ON_OFF` |

当动作同时设定模式时, `set_temperature` 在 `native_temperature_unit` 和 `ATTR_OPERATION_MODE` 中接收 `ATTR_TEMPERATURE` 。

## 状态 {#states}

状态是 `current_operation` 的值, 如 `eco`, `performance` 或 `off` , 或您自己的模式之一 。 当`current_operation`是`None`时,状态是`unknown`.

## 示例 {#example}

```python
from typing import Any

from homeassistant.components.water_heater import (
    STATE_ECO,
    STATE_PERFORMANCE,
    WaterHeaterEntity,
    WaterHeaterEntityFeature,
)
from homeassistant.const import ATTR_TEMPERATURE, UnitOfTemperature

class MyWaterHeater(WaterHeaterEntity):
    """A boiler with two modes."""

    _attr_has_entity_name = True
    _attr_name = None
    _attr_native_temperature_unit = UnitOfTemperature.CELSIUS
    _attr_min_temp = 40
    _attr_max_temp = 75
    _attr_operation_list = [STATE_ECO, STATE_PERFORMANCE]
    _attr_supported_features = (
        WaterHeaterEntityFeature.TARGET_TEMPERATURE
        | WaterHeaterEntityFeature.OPERATION_MODE
    )

    def __init__(self, device: MyDevice) -> None:
        """Set up the water heater."""
        self._device = device
        self._attr_unique_id = device.serial

    @property
    def current_operation(self) -> str:
        """Return the current mode."""
        return self._device.mode

    @property
    def native_current_temperature(self) -> float:
        """Return the water temperature."""
        return self._device.temperature

    @property
    def native_target_temperature(self) -> float:
        """Return the target temperature."""
        return self._device.setpoint

    async def async_set_temperature(self, **kwargs: Any) -> None:
        """Set the target temperature."""
        await self._device.set_setpoint(kwargs[ATTR_TEMPERATURE])

    async def async_set_operation_mode(self, operation_mode: str) -> None:
        """Set the mode."""
        await self._device.set_mode(operation_mode)
```
