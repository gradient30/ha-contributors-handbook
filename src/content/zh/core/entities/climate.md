---
title: 气候实体
description: 为恒温器、空调器和控制温度、湿度和风扇的热泵建立一个气候实体。
sidebarLabel: 气候
sidebarGroup: 灯光和气候
---

# 气候实体 {#climate-entity}

一个 气候实体控制空间的气候:一个恒温器,一个空调,一个热泵,或者一个具有目标温度的散热阀. 也可以控制湿度和单元的风扇. 从`ClimateEntity` 继承到`homeassistant.components.climate` 。

如果设备只使空气干燥或潮湿,则使用[增湿器](/core/entities/humidifier). 如果加热水,请使用[显然是热水器](/core/entities/water-heater). 独立的扇子是[风扇](/core/entities/fan).

前端如何显示气候实体,见[气候更多信息视图](/design/more-info/climate)。

从 Home Assistant 演示中嵌入的仪表板卡的现场演示。 具有目标温度、HVAC模式和预置的气候实体,在瓦片卡和自动调温卡中。 卡片为直播:改变温度,模式,或预设.

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
        "entity_id": "climate.living_room",
        "state": "heat",
        "attributes": {
          "friendly_name": "Living room",
          "current_temperature": 19.5,
          "temperature": 21,
          "min_temp": 7,
          "max_temp": 30,
          "target_temp_step": 0.5,
          "hvac_modes": [
            "heat",
            "cool",
            "auto",
            "off"
          ],
          "preset_modes": [
            "home",
            "away",
            "eco"
          ],
          "preset_mode": "home",
          "supported_features": 401
        }
      }
    ]
  </script>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "tile",
        "entity": "climate.living_room",
        "features": [
          {
            "type": "target-temperature"
          },
          {
            "type": "climate-preset-modes"
          }
        ]
      }
    </script>
  </ha-embed-card>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "thermostat",
        "entity": "climate.living_room",
        "features": [
          {
            "type": "climate-hvac-modes"
          }
        ]
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

## 的临时议程 {#properties}

气候实体在[一般实体属性](/core/entities/entity-class)之上有这些属性。 每个属性都可以以其`_attr_`属性设定,如`_attr_hvac_mode`.

| 名称 | 类型 | 默认 | 说明 |
| ---- | ---- | ------- | ----------- |
| `hvac_mode` | `HVACMode \| None` | 要求数 | 设备设定的操作模式 。 这是实体的状况。 |
| `hvac_modes` | `list[HVACMode]` | 要求数 | 设备支持的操作模式 。 |
| `native_temperature_unit` | `str` | 要求数 | 设备的单位报告温度为 `UnitOfTemperature.CELSIUS` 或 `UnitOfTemperature.FAHRENHEIT` 。 |
| `hvac_action` | `HVACAction \| None` | `None` | 装置现在在做什么? 见[HVAC行动](/core/entities/climate#hvac-actions). |
| `native_current_temperature` | `float \| None` | `None` | 测量温度 `native_temperature_unit` 。 |
| `native_target_temperature` | `float \| None` | `None` | 要达到的温度, 在`native_temperature_unit` 。 需要 `TARGET_TEMPERATURE` 。 |
| `native_target_temperature_high` | `float \| None` | 需要使用 `TARGET_TEMPERATURE_RANGE` | 目标范围的上限, 在 `native_temperature_unit` 中 。 |
| `native_target_temperature_low` | `float \| None` | 需要使用 `TARGET_TEMPERATURE_RANGE` | 搁浅的目标范围, 以 `native_temperature_unit` 表示 。 |
| `target_temperature_step` | `float \| None` | `None` | 目标温度的阶梯大小, 在 `native_temperature_unit` 中 。 |
| `min_temp` | `float` | 7 °C | 最低目标温度,在`native_temperature_unit`。 默认值转换为您的单位 。 |
| `max_temp` | `float` | 35 °C | 最高目标温度,在`native_temperature_unit`。 默认值转换为您的单位 。 |
| `precision` | `float` | 摄氏十分之一,否则全数 | 精确温度以 `PRECISION_TENTHS`, `PRECISION_HALVES` 或 `PRECISION_WHOLE` 显示 。 没有值,它遵循安装的单元系统. |
| `current_humidity` | `float \| None` | `None` | 测量湿度. |
| `target_humidity` | `float \| None` | `None` | 湿度达到。 需要 `TARGET_HUMIDITY` 。 |
| `target_humidity_step` | `int \| None` | `None` | 目标湿度的阶梯大小. |
| `min_humidity` | `float` | `30` | 目标湿度最低. |
| `max_humidity` | `float` | `99` | 最高目标湿度. |
| `preset_mode` | `str \| None` | 需要使用 `PRESET_MODE` | 活动预设 。 |
| `preset_modes` | `list[str] \| None` | 需要使用 `PRESET_MODE` | 可用预设. |
| `fan_mode` | `str \| None` | 需要使用 `FAN_MODE` | 当前风扇模式 。 |
| `fan_modes` | `list[str] \| None` | 需要使用 `FAN_MODE` | 可用的风扇模式 。 |
| `swing_mode` | `str \| None` | 需要使用 `SWING_MODE` | 目前摆动模式. |
| `swing_modes` | `list[str] \| None` | 需要使用 `SWING_MODE` | 可用的摇摆模式 。 |
| `swing_horizontal_mode` | `str \| None` | 需要使用 `SWING_HORIZONTAL_MODE` | 目前水平摆动模式. |
| `swing_horizontal_modes` | `list[str] \| None` | 需要使用 `SWING_HORIZONTAL_MODE` | 可用的水平摆动模式 。 |

### 温度单位 {#temperature-units}

报告设备单位的每个温度,并设置 `native_temperature_unit` 以匹配 。 气候实体在写入状态前将温度转换为安装的单位系统,并与转换值的单位添加`temperature_unit`状态属性. 你不能推翻这个属性。

效果也相反: 温度传递到 `set_temperature` 转换到 `native_temperature_unit` 并在调用方法之前与 `min_temp` 和 `max_temp` 核对 。

> [!WARNING]
> 旧名没有`native_`,如`current_temperature`,`target_temperature`和`temperature_unit`(及其`_attr_`属性),则在Home Assistant2027.11中贬值并停止工作. 使用新代码中的 `native_` 名称 。

## HVAC 模式 {#hvac-modes}

HVAC模式是设备被要求做的. 只使用 `HVACMode` enum 的模式 。 当一个设备有一个 October 选项来改变一个模式的行为方式时,使它成为一个预设而不是一个新的模式.

| 数值 | 说明 |
| ----- | ----------- |
| `HVACMode.OFF` | 设备关闭了。 |
| `HVACMode.HEAT` | 装置加热Addi到目标温度. |
| `HVACMode.COOL` | 设备冷却到目标温度. |
| `HVACMode.HEAT_COOL` | 设备加热或冷却以停留在目标范围内. |
| `HVACMode.AUTO` | 设备遵循一个时间表,学到的行为,或者它自己的逻辑. 您无法在此模式中设置温度 。 |
| `HVACMode.DRY` | 装置使空气干燥. |
| `HVACMode.FAN_ONLY` | 只有风扇运行,没有加热或冷却. |

## HVAC行动 {#hvac-actions}

HVAC动作是设备正在做的,以达到它的模式和预设,这是它自己的控制逻辑决定的. 只使用 `HVACAction` enum 的动作 。

| 数值 | 说明 |
| ----- | ----------- |
| `HVACAction.OFF` | 设备关闭, 除非其模式改变, 什么都不做 。 |
| `HVACAction.IDLE` | 设备现在什么也做不了,但条件变化时可以开始. |
| `HVACAction.HEATING` | 装置加热. |
| `HVACAction.PREHEATING` | 热源运行,但尚未达到运行温度. |
| `HVACAction.COOLING` | 器能除热. |
| `HVACAction.DRYING` | 该装置能消除空气中的湿度. |
| `HVACAction.FAN` | 只有风扇运行,循环或通风空气. |
| `HVACAction.DEFROSTING` | 设备去除积冰. |

诚实对待`hvac_action`。 具有歇斯底里作用的恒温器,或者在达到目标后一直低功率运行的可变电源装置,并不总是知道是加热还是闲置. 如果设备不能告诉你它在做什么, 请离开 `hvac_action` 。

## 预设、风扇模式和摇摆模式 {#presets-fan-modes-and-swing-modes}

预设,风扇模式,和摇摆模式是字符串列表. Home Assistant 具有内置翻译的常数用于常见值, 您可以添加自己的值 。 在 `state_attributes` (参见 [帖式图标](/core/entities/icons)) 下, 给自定义的翻译值和实体的 [翻译密钥](/core/entities/naming) 图标 。

- 你还好么?
- **Fan模式**:  如果我们在其中出现,则会发现: `FAN_ON`,`FAN_OFF`,`FAN_AUTO`,`FAN_LOW`,`FAN_MEDIUM`,`FAN_HIGH`,`FAN_TOP`,`FAN_MIDDLE`,`FAN_FOCUS`和`FAN_DIFFUSE`。
- ** 旋转模式**:`SWING_ON`,`SWING_OFF`,`SWING_BOTH`,`SWING_VERTICAL`,和`SWING_HORIZONTAL`。
- ** Horizontal 摇摆模式**:`SWING_HORIZONTAL_ON`和`SWING_HORIZONTAL_OFF`。

仅在设备分别控制垂直和水平摆动时执行水平摆动. 然后`swing_modes`覆盖垂直方向和`swing_horizontal_modes`水平方向。 否则,将每个选项输入`swing_modes`。

Home Assistant 在您被调用之前, 对照您的列表检查模式, 当它不在里面时, 则会出现校验错误 。

## 支持的特性 {#supported-features}

将 `ClimateEntityFeature` 旗帜与 `|` 合并, 设置为 `supported_features`。 见 [支持的特性](/glossary/supported-features) 。

| 数值 | 说明 |
| ----- | ----------- |
| `TARGET_TEMPERATURE` | 该装置具有单一的目标温度. 执行`set_temperature`。 |
| `TARGET_TEMPERATURE_RANGE` | 该设备有一个目标范围,由`HVACMode.HEAT_COOL`使用. 执行`set_temperature`。 |
| `TARGET_HUMIDITY` | 该装置具有时光标本湿度. 执行{时光}。 |
| `FAN_MODE` | 实情是, 实情如下: |
| `PRESET_MODE` | 设备有预设. 执行`set_preset_mode`。 |
| `SWING_MODE` | 设备有摇摆模式. 执行`set_swing_mode`。 |
| `SWING_HORIZONTAL_MODE` | 该设备有单独的水平摆动模式. 执行`set_swing_horizontal_mode`。 |
| `TURN_ON` | 设备可以打开。 执行`turn_on`,或依赖默认(见下文). |
| `TURN_OFF` | 设备可以关闭。 执行`turn_off`,或依赖默认(见下文). |

您未设置的特性动作在到达您的实体之前被拒绝 。

## 方法 {#methods}

执行岔或每种方法的同步变体,而不是两者。

| 就在那时 | Async 变体 | 请求 |
| ------ | ------------- | ---------- |
| `set_hvac_mode(hvac_mode: HVACMode)` | `async_set_hvac_mode` | 更改 HVAC 模式 。 总是可用。 |
| `set_temperature(**kwargs: Any)` | `async_set_temperature` | `TARGET_TEMPERATURE` or `TARGET_TEMPERATURE_RANGE`. |
| `set_humidity(humidity: int)` | `async_set_humidity` | `TARGET_HUMIDITY`. |
| `set_fan_mode(fan_mode: str)` | `async_set_fan_mode` | `FAN_MODE`. |
| `set_preset_mode(preset_mode: str)` | `async_set_preset_mode` | `PRESET_MODE`. |
| `set_swing_mode(swing_mode: str)` | `async_set_swing_mode` | `SWING_MODE`. |
| `set_swing_horizontal_mode(swing_horizontal_mode: str)` | `async_set_swing_horizontal_mode` | `SWING_HORIZONTAL_MODE`. |
| `turn_on()` | `async_turn_on` | `TURN_ON`. |
| `turn_off()` | `async_turn_off` | `TURN_OFF`. |
| `toggle()` | `async_toggle` | `TURN_ON` 和 `TURN_OFF` 。 |

`set_temperature`为单个目标收到`ATTR_TEMPERATURE`,或`ATTR_TARGET_TEMP_LOW`和`ATTR_TARGET_TEMP_HIGH`为某个范围,全部在`native_temperature_unit`中. 当动作同时设定模式时,它也可以收到`ATTR_HVAC_MODE`.

您并不一定必须执行 `turn_on` 和 `turn_off` 。 没有它们, `turn_off` 在设备支持时设置 `HVACMode.OFF` 。 `turn_on` 当设备有两个模式且一个是`OFF`时,选择唯一的其他模式,否则则选择`HEAT_COOL`、`HEAT`和`COOL`中的第一个模式。 如果设备有它自己的打开和关闭, 执行它们, 并设定 `hvac_mode` 到它降落的方式 。 根据`hvac_mode`是否为`OFF`,拨打`turn_on`或`turn_off`。

## 状态 {#states}

状态是`hvac_mode`的值:`off`,`heat`,`cool`,`heat_cool`,`auto`,`dry`,或`fan_only`. 当`hvac_mode`是`None`时,州是`unknown`.

## 恢复温度 {#restoring-temperatures}

如果您实体在重启后恢复温度, 请不要从 `RestoreEntity` 给予您的最后一个状态的属性读取 。 这些设备被转换成装置的单元系统,并四舍五入显示。 转而从`RestoreClimate`继承,并在`async_added_to_hass`中呼叫`async_get_last_climate_data()`。

它返回存储的 `native_current_temperature`, `native_target_temperature`,`native_target_temperature_high` 和`native_target_temperature_low`, 转换成您的当前 `native_temperature_unit` , 或`None` 当没有恢复时 。 一个不是有效数字的温度会回到 `None` 。

传`validate_range=True` 当您将恢复的目标发送到设备时, 就像当设备无法报告自己的状态时一样. `min_temp` 和`max_temp` 以外的一个目标, 然后作为 `None` 回来, 然后返回到默认状态 。 射程外最多半度的目标,如四舍五入,则被夹在射程上。 半度是储存在温度的单位中,因此在目前使用°C的实体上,在°F中存储的值得到约0.28 °C的房间.

```python
from homeassistant.components.climate import RestoreClimate

class MyThermostat(RestoreClimate):
    async def async_added_to_hass(self) -> None:
        """Restore the target temperature."""
        await super().async_added_to_hass()
        if (
            data := await self.async_get_last_climate_data(validate_range=True)
        ) is not None and data.native_target_temperature is not None:
            self._attr_native_target_temperature = (
                data.native_target_temperature
            )
```

## 示例 {#example}

```python
from typing import Any

from homeassistant.components.climate import (
    ClimateEntity,
    ClimateEntityFeature,
    HVACMode,
)
from homeassistant.const import ATTR_TEMPERATURE, UnitOfTemperature

class MyThermostat(ClimateEntity):
    """A thermostat that heats, or is off."""

    _attr_has_entity_name = True
    _attr_name = None
    _attr_hvac_modes = [HVACMode.OFF, HVACMode.HEAT]
    _attr_native_temperature_unit = UnitOfTemperature.CELSIUS
    _attr_target_temperature_step = 0.5
    _attr_supported_features = (
        ClimateEntityFeature.TARGET_TEMPERATURE
        | ClimateEntityFeature.TURN_ON
        | ClimateEntityFeature.TURN_OFF
    )

    def __init__(self, device: MyDevice) -> None:
        """Set up the thermostat."""
        self._device = device
        self._attr_unique_id = device.serial

    @property
    def hvac_mode(self) -> HVACMode:
        """Return the current mode."""
        return HVACMode.HEAT if self._device.heating else HVACMode.OFF

    @property
    def native_current_temperature(self) -> float:
        """Return the measured temperature."""
        return self._device.temperature

    @property
    def native_target_temperature(self) -> float:
        """Return the target temperature."""
        return self._device.setpoint

    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None:
        """Set the mode."""
        await self._device.set_heating(hvac_mode == HVACMode.HEAT)

    async def async_set_temperature(self, **kwargs: Any) -> None:
        """Set the target temperature."""
        await self._device.set_setpoint(kwargs[ATTR_TEMPERATURE])
```

用 `TURN_ON` 和 `TURN_OFF` 设定, 并且只有 `OFF` 和 `HEAT` 作为模式, 默认的 `turn_on` 和 `turn_off` 给您打电话 `async_set_hvac_mode` 。
