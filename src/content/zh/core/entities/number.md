---
title: 数目实体
description: 构建一个允许人们在设备上设置数字值的数字实体,如目标关卡或超时.
sidebarLabel: 数目
sidebarGroup: 输入与助手
---

# 数目实体 {#number-entity}

以及向人设定一个数字值的数个实体:一个量级,分秒计时,温度抵消,或汽车充电器的最大充电流. 从`NumberEntity` 继承到`homeassistant.components.number` 。

用它来值人 set . 该设备只报告的一个值是 [传感器](/core/entities/sensor) 。 当一个更丰富的平台存在时,使用这个平台:一个恒温器的目标温度属于一个[气候](/core/entities/climate)实体,一个灯泡在[光线](/core/entities/light)上的亮度.

前端如何显示数字,请参见[数字更多信息视图](/design/more-info/number).

## 的临时议程 {#properties}

每个带有值的属性从`native_`开始. 您返回设备使用的单位中的值, 而基类将其转换为用户想要的单位 。 见[单位和改划](/core/entities/number#units-and-conversion).

| 名称 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- |
| `native_value` | `float \| None` | `None` | 当前值, 在 `native_unit_of_measurement` 中 。 |
| `native_min_value` | `float` | `0.0` | 被接受的最低价值,包容性。 |
| `native_max_value` | `float` | `100.0` | 被接受的最高价值,包容性。 |
| `native_step` | `float \| None` | `None` | 两个值之间的最小变化. 当 `None` 时, 基类从范围中选择一个, 见下文 。 |
| `native_unit_of_measurement` | `str \| None` | `None` | 值所在单位. 翻译单位的时候别管了 |
| `mode` | `NumberMode` | `NumberMode.AUTO` | 前端如何显示控制. |
| `device_class` | `NumberDeviceClass \| None` | `None` | 什么数字衡量。 见[设备类](/core/entities/number#device-classes). |

没有 `native_step`, 步骤开始于 `1.0` 。 当最小和最大之间的范围是 `1.0` 或更小,基类将步骤除以10,直到适合.

每个实体的通用属性,如`name`,`available`和`unique_id`,都在[实体类别](/core/entities/entity-class)上. 不要设置`unit_of_measurement`,`min_value`,`max_value`,`step`,或`value`:这些是最终的,由基类从`native_`属性计算.

## 支持的特性 {#supported-features}

该实体没有支持的特性。

## 模式 {#modes}

| 常数 | 说明 |
| --- | --- |
| `NumberMode.AUTO` | 让前端在滑动器和输入框之间选择。 使用这个除非你有理由不使用。 |
| `NumberMode.BOX` | 总是显示一个输入框。 |
| `NumberMode.SLIDER` | 总是显示滑块. |

## 设备类 {#device-classes}

数字设备类与[传感器设备类别](/core/entities/sensor)相同,但`date`,`enum`,`timestamp`和`uptime`除外. 它们是[`homeassistant/components/number/const.py`](https://github.com/home-assistant/core/blob/dev/homeassistant/components/number/const.py) 中的 `NumberDeviceClass` enum, 例如 `NumberDeviceClass.TEMPERATURE`, `NumberDeviceClass.POWER` 或 `NumberDeviceClass.DURATION` 。

设置设备类时,返回设备类接受的单位. 接受的单位在`DEVICE_CLASS_UNITS`,在同一文件中. 带有设备类且没有自己名称的编号会获得其设备类的翻译名称,如"Temperature". 见[命名实体](/core/entities/naming).

## 单位和改划 {#units-and-conversion}

对于许多设备类,基类在单位之间转换:在本地单位工作,用户看到自己的. 具有转换功能的设备类是`UNIT_CONVERTERS`在[`homeassistant/components/number/const.py`](https://github.com/home-assistant/core/blob/dev/homeassistant/components/number/const.py)中的键 。

- 在 Home Assistant 配置的温度单位中显示 `temperature` 的本地单位为 °C 或 °F 的编号 。
- 用户可以为其实体设置中的某个数字选择另一个单位,只要设备类支持转换,且两个单位都有效.
- 最小和最大也是转换的。 射程最小的下射和射程最高的上射,因此射程永远不会变窄. 该步骤未被转换: 您设置的 `native_step` 和用户单位一样被使用 。 如果没有一个,该步骤就是从转换范围衍生出来的.
- 当有人设定一个值, 你得到它回到你的本土单位。

如果单位是应该翻译的文本,如"presses",请离开`native_unit_of_measurement`,并在实体的翻译密钥下给出`strings.json`中的单位. 设置两者都会产生错误 。 见[43. 使您的字符串可转换](/translate/guides/developers).

## 方法 {#methods}

### 设定值 {#set-value}

当 当某人更改了UI中的值时调用,或者一个自动化或脚本调用`number.set_value`动作. 该值存在于您的本地单位中 。 实施其中之一。

```python
class MyNumber(NumberEntity):
    

# Implement one of these methods. {#states}

    def set_native_value(self, value: float) -> None:
        """Set a new value."""

    async def async_set_native_value(self, value: float) -> None:
        """Set a new value."""
```

不要执行`set_value`或`async_set_value`。 它们是最终的,来自一个旧的API;一个超越它们的子类会在日志中得到警告.

## 状态 {#restoring-the-value}

状态是 `native_value`, 当与本地单位不同时转换为用户单位 。 转换值会保留原值的小数。 它是`unknown` 当`native_value`是`None`时。

最小,最大,步骤,和模式是能力属性:它们被写入[非常大实体登记处](/core/entities/registry),并被从记录器历史中忽略.

## 在国际范围内恢复该值 {#example}

如果您的号码保留在 Home Assistant 中, 而不是设备上, 它需要在重启后返回 。 继承来自 `RestoreNumber` 而不是 `NumberEntity` 和 `RestoreEntity` 。 `RestoreEntity` 存储转换状态; `RestoreNumber` 存储 `native_` 值, 所以您恢复您设定的值 。

```python
from homeassistant.components.number import RestoreNumber

class MyNumber(RestoreNumber):
    async def async_added_to_hass(self) -> None:
        """Restore the last value."""
        await super().async_added_to_hass()
        if (data := await self.async_get_last_number_data()) is not None:
            self._attr_native_value = data.native_value
```

`async_get_last_number_data()` 返回最后一个 `native_value`, `native_min_value`, `native_max_value`, `native_step`, 和`native_unit_of_measurement`, 或`None` 当没有可以恢复时 。 见[实体生命周期](/core/entities/lifecycle) 当 `async_added_to_hass` 运行时 。

## 示例 {#示例}

```python
from homeassistant.components.number import (
    NumberDeviceClass,
    NumberEntity,
    NumberMode,
)
from homeassistant.const import EntityCategory, UnitOfElectricCurrent

class ExampleChargeCurrent(NumberEntity):
    """The maximum charge current of a car charger."""

    _attr_has_entity_name = True
    _attr_translation_key = "max_charge_current"
    _attr_device_class = NumberDeviceClass.CURRENT
    _attr_entity_category = EntityCategory.CONFIG
    _attr_mode = NumberMode.SLIDER
    _attr_native_min_value = 6
    _attr_native_max_value = 32
    _attr_native_step = 1
    _attr_native_unit_of_measurement = UnitOfElectricCurrent.AMPERE

    def __init__(self, device: ExampleCharger) -> None:
        """Initialize the number."""
        self._device = device
        self._attr_unique_id = f"{device.serial}_max_charge_current"
        self._attr_native_value = device.max_current

    async def async_set_native_value(self, value: float) -> None:
        """Set the maximum charge current."""
        await self._device.set_max_current(int(value))
        self._attr_native_value = value
        self.async_write_ha_state()
```
