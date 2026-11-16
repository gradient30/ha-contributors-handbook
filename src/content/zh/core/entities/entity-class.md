---
title: 实体类别
description: 实体的基类是每个实体所依赖的,是确定其属性的三种方法,也是每个实体的通用属性。
sidebarLabel: 实体类别
sidebarGroup: 基本情况
order: 1
---

# 实体类别 {#the-entity-class}

Home Assistant中每个实体都是Python在`homeassistant.helpers.entity`中继承`Entity`的对象。 您几乎从未直接继承 `Entity` 。 您继承了实体平台的基类, 如 `SwitchEntity` 或 `SensorEntity` 。 该类在此处描述的通用域之上,增加了其域的属性和方法.

## 最小实体 {#a-minimal-entity}

此开关保持其状态为内存. 它是其装置的主要特征,所以取装置的名称.

```python
from typing import Any

from homeassistant.components.switch import SwitchEntity
from homeassistant.helpers.device_registry import DeviceInfo

from .const import DOMAIN

class ExampleSwitch(SwitchEntity):
    """A switch that remembers if it is on."""

    _attr_has_entity_name = True
    _attr_name = None
    _attr_is_on = False

    def __init__(self, serial: str) -> None:
        """Initialize the switch."""
        self._attr_unique_id = serial
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, serial)},
            name="Garden pump",
        )

    async def async_turn_on(self, **kwargs: Any) -> None:
        """Turn the switch on."""
        self._attr_is_on = True
        self.async_write_ha_state()

    async def async_turn_off(self, **kwargs: Any) -> None:
        """Turn the switch off."""
        self._attr_is_on = False
        self.async_write_ha_state()
```

本页的其余部分,以及本组中的其他部分,都解释这个例子的每个部分.

## 设置属性 {#setting-properties}

Home Assistant 每次写状态时都会读取您实体的属性 。 你可以通过三种方式提供财产。 他们最终都在同一处 所以选一个读得最好的

### 带有 `_attr_` 前缀的属性 {#attributes-with-the-attr-prefix}

大多数属性在基类中有一个默认执行,返回一个同名属性和一个`_attr_`前缀. `device_class` 属性返回 `self._attr_device_class` , 开关返回 `self._attr_is_on` 的 `is_on` 属性等等 。 当它们永远不变时, 把它们设定为类属性, 或者当它们发生时, 设定为实例属性 。

```python
class ExampleSwitch(SwitchEntity):
    _attr_icon = "mdi:water-pump"

    def __init__(self, serial: str) -> None:
        self._attr_unique_id = serial
```

这是最常见的风格. 当您自己的代码需要值时,请读取属性(`self.available`),而不是属性({潇洒}). 并不是每个平台属性都有一个`_attr_`属性:每个平台的页面在不这样的时候都会这么说.

### 财产方法 {#property-methods}

当必须计算一个值时, 覆盖属性本身 。

```python
class ExampleSwitch(SwitchEntity):
    @property
    def is_on(self) -> bool:
        """Return if the pump is running."""
        return self._device.pump_speed > 0
```

> [!IMPORTANT]
> 属性必须返回内存中的数据 。 在属性中从不I/O,比如网络请求或读取文件. 在您的更新方法或 见下文 [协调员](/glossary/coordinator) 中获取数据, 并让属性读取已经存在的内容 。 属性召于每州之文,故令其便宜.

### 实体说明 {#entity-descriptions}

[实体描述](/glossary/entity-description) 是保存一种实体的静态属性的冻结数据类 。 每个平台都有自己的子类,比如`SensorEntityDescription`. 设置为`self.entity_description`,基类读取属性如`device_class`,`translation_key`和`entity_category`。

唯一需要的字段是`key`,这个字符串在您的平台中是独一无二的. 它是一个很好的构件 独特的ID。

当一个类服务于许多仅在设置上有所不同的实体时,描述就会闪耀. 你把他们打成一团,然后在布置期间循环。

```python
from collections.abc import Callable
from dataclasses import dataclass

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.const import UnitOfTemperature
from homeassistant.helpers.typing import StateType

@dataclass(frozen=True, kw_only=True)
class ExampleSensorEntityDescription(SensorEntityDescription):
    """Describes an Example sensor."""

    value_fn: Callable[[ExampleDevice], StateType]

SENSORS: tuple[ExampleSensorEntityDescription, ...] = (
    ExampleSensorEntityDescription(
        key="water_temperature",
        translation_key="water_temperature",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda device: device.water_temperature,
    ),
)

class ExampleSensor(SensorEntity):
    """A sensor of an Example device."""

    entity_description: ExampleSensorEntityDescription
    _attr_has_entity_name = True

    def __init__(
        self,
        device: ExampleDevice,
        description: ExampleSensorEntityDescription,
    ) -> None:
        """Initialize the sensor."""
        self._device = device
        self.entity_description = description
        self._attr_unique_id = f"{device.serial}_{description.key}"

    @property
    def native_value(self) -> StateType:
        """Return the value from the device."""
        return self.entity_description.value_fn(self._device)
```

一个`_attr_`属性胜过描述. 这样您就可以共享一个描述, 并且仍然覆盖一个单一实体的一个值 。

## 一般属性 {#generic-properties}

每个实体都有这些属性。 皆是可选.

| 名称 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- |
| `assumed_state` | `bool` | `False` | `True`当状态是猜测时,因为设备无法报告. 前端然后显示分开的按键,而不是切换. 见[假设状态](/core/entities/state-updates#assumed-state). |
| `attribution` | `str \| None` | `None` | 数据提供者要求您显示的标志文本 。 |
| `available` | `bool` | `True` | 当 Home Assistant 无法读取或控制设备时 。 状态变为`unavailable`。见[更新状态](/core/entities/state-updates#availability)。 |
| `device_class` | `str \| None` | `None` | 实体是什么或措施,从其领域清单中列出。 见[设备类](/glossary/device-class). |
| `device_info` | `DeviceInfo \| ChildDeviceInfo \| None` | `None` | 此实体所属的设备 。 见[实体登记册](/core/entities/registry#linking-to-a-device). |
| `entity_category` | `EntityCategory \| None` | `None` | 标记一个配置或诊断实体。 见[实体登记册](/core/entities/registry#entity-categories). |
| `entity_picture` | `str \| None` | `None` | 要显示图片而不是图标的 URL 。 |
| `entity_registry_enabled_default` | `bool` | `True` | 实体在首次注册时是否开始启用 。 |
| `entity_registry_visible_default` | `bool` | `True` | 实体在首次注册时是否开始可见 。 |
| `extra_state_attributes` | `Mapping[str, Any] \| None` | `None` | 您的整合的额外属性 。 见[状态和属性](/core/entities/state-attributes). |
| `force_update` | `bool` | `False` | 写每个更新到州机器, 即使没有改变。 见[更新状态](/core/entities/state-updates#force-update). |
| `has_entity_name` | `bool` | `False` | `True` 当`name`只描述实体,而不是设备时. 需要新的整合。 见[命名实体](/core/entities/naming). |
| `icon` | `str \| None` | `None` | 一个固定的图标。 偏爱图标翻译. 见[帖式图标](/core/entities/icons). |
| `name` | `str \| None` | 未设置 | 实体名. `None`表示实体是其设备的主要特征. 见[命名实体](/core/entities/naming). |
| `should_poll` | `bool` | `True` | Home Assistant是否投票 实体。 设定为 `False` 用于推. 见[更新状态](/core/entities/state-updates). |
| `supported_features` | `int \| None` | `None` | 实体支持的特性的也已标出 `EntityFeature` enum 。 见[支持的特性](/glossary/supported-features). |
| `translation_key` | `str \| None` | `None` | `strings.json` 和 `icons.json` 中翻译的名称、 状态、 状态属性和图标的密钥 。 |
| `translation_placeholders` | `Mapping[str, str]` | `{}` | 译名中的占位符值。 |
| `unique_id` | `str \| None` | `None` | 一个稳定的ID,在您的整合和领域中独一无二. 要求使用该登记簿。 见[实体登记册](/core/entities/registry#unique-id). |

请离开 `name` 当实体从它的翻译密钥或设备类中获取名称时, 请不要设置 。 设置  đó `_attr_name = None`殆不同: 它明确地说“ 这个实体没有它自己的名字”。

### 不断变化的能力 {#changing-capabilities}

您可以更改 `device_class`, `supported_features`, 以及实体运行时域的能力属性, 但很少这样做 。 每一次更改都会更新实体注册,一些消费者,如语音助理,在看到云服务时会重新同步. Home Assistant 当一个实体在一个小时内更新其能力超过100次时登录一个警告.

## 不覆盖属性 {#properties-you-dont-override}

一些属性属于平台基类或Home Assistant本身.

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| `state` | `StateType` | 州书写州机. 每个平台基类都从自己的属性执行,比如`is_on`或`native_value`. 只设置在直接的 `Entity` 子类 。 |
| `state_attributes` | `dict[str, Any] \| None` | 域的标准属性,如光的亮度. 由平台基类实施. |
| `capability_attributes` | `dict[str, Any] \| None` | 描述实体所能做的属性,猥亵效果列表等. 它们也存放在实体登记处。 由平台基类实施. |
| `unit_of_measurement` | `str \| None` | 国家单位. `sensor`和`number`等平台从自己的`native_unit_of_measurement`中计算出来. |
| `enabled` | `bool` | `True` 除非注册从一开始就被禁用。 由 Home Assistant从一开始就管理。 |

## 建议是谁修改实体模式 {#proposing-changes-to-an-entity-model}

每个域的属性,特征和状态被每一个执行它的集成共享,所以改变它们比改变一个集成要大. 如果您想要在域中添加一些东西, 请在 [结构讨论](https://github.com/home-assistant/architecture/discussions) 中首先提出 。 添加在几个品牌之间是常见的,而不是服务于一个设备时考虑.
