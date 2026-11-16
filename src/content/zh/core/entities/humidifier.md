---
title: 湿润实体
description: 为对实现空气增加湿度或消除湿度的装置建造一个加湿实体。
sidebarLabel: 湿度
sidebarGroup: 灯光和气候
---

# 湿润实体 {#humidifier-entity}

湿度实体控制一个向目标湿度增加空气湿度(湿度器)或去除空气湿度(除湿器)的设备。 从`HumidifierEntity` 继承到`homeassistant.components.humidifier` 。 它建立在切换实体上,因此它有`is_on`,`turn_on`和`turn_off`.

如果设备同时加热或冷却,则使用 [气候实体](/core/entities/climate) 特性 `TARGET_HUMIDITY` 代替 。

前端如何显示加湿器,请参见[增湿器视图](/design/more-info/humidifier).

从 Home Assistant 演示中嵌入的仪表板卡的现场演示。 具有目标湿度和模式的加湿器,在瓦片卡和加湿器卡中. 卡片为直播:改变目标,模式,或关闭.

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
        "entity_id": "humidifier.bedroom",
        "state": "on",
        "attributes": {
          "friendly_name": "Bedroom humidifier",
          "device_class": "humidifier",
          "action": "humidifying",
          "current_humidity": 38,
          "humidity": 45,
          "min_humidity": 30,
          "max_humidity": 70,
          "available_modes": [
            "normal",
            "eco",
            "sleep"
          ],
          "mode": "normal",
          "supported_features": 1
        }
      }
    ]
  </script>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "tile",
        "entity": "humidifier.bedroom",
        "features": [
          {
            "type": "target-humidity"
          },
          {
            "type": "humidifier-modes"
          }
        ]
      }
    </script>
  </ha-embed-card>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "humidifier",
        "entity": "humidifier.bedroom",
        "features": [
          {
            "type": "humidifier-toggle"
          }
        ]
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

## 的临时议程 {#properties}

湿度实体在 [一般实体属性](/core/entities/entity-class) 之上有这些属性 。 每个属性都可以以其`_attr_`属性设定,如`_attr_target_humidity`.

| 名称 | 类型 | 默认 | 说明 |
| ---- | ---- | ------- | ----------- |
| `is_on` | `bool \| None` | `None` | 设备是否打开 。 |
| `device_class` | `HumidifierDeviceClass \| None` | `None` | 设备是加湿器还是除湿器. 见[设备类](/core/entities/humidifier#device-classes). |
| `action` | `HumidifierAction \| None` | `None` | 装置现在在做什么? 见[动作](/core/entities/humidifier#actions). |
| `current_humidity` | `float \| None` | `None` | 测量湿度. |
| `target_humidity` | `float \| None` | `None` | 要达到的湿度。 |
| `target_humidity_step` | `float \| None` | `None` | 目标湿度的阶梯大小. |
| `min_humidity` | `float` | `0` | 目标湿度最低. |
| `max_humidity` | `float` | `100` | 最高目标湿度. |
| `mode` | `str \| None` | 需要使用 `MODES` | 活动模式 。 |
| `available_modes` | `list[str] \| None` | 需要使用 `MODES` | 设备支持的模式 。 |

## 设备类 {#device-classes}

从 `HumidifierDeviceClass` 设置 [设备类](/glossary/device-class) , 因此前端和语音助理知道设备的运行方式 。

| 数值 | 说明 |
| ----- | ----------- |
| `HUMIDIFIER` | 增加空气的湿度。 |
| `DEHUMIDIFIER` | 消除空气中的湿度。 |

## 动作 {#actions}

`action` 告诉设备现在在做什么 。 使用 `HumidifierAction` enum 。 当设备关闭时, Home Assistant 报告`off` 给您, 不管 `action` 返回 。

| 数值 | 说明 |
| ----- | ----------- |
| `HumidifierAction.HUMIDIFYING` | 装置增加水分. |
| `HumidifierAction.DRYING` | 设备可以去除水分. |
| `HumidifierAction.IDLE` | 设备已经打开了,但现在什么都没做 |
| `HumidifierAction.OFF` | 设备关闭了。 |

只有设备报告时执行 `action` 。

## 模式 {#modes}

模式是弦. Home Assistant 常数带有常见模式的内置翻译: `MODE_NORMAL`,`MODE_ECO`,`MODE_AWAY`,`MODE_BOOST`,`MODE_COMFORT`,`MODE_HOME`,`MODE_SLEEP`,`MODE_AUTO`和`MODE_BABY`。 您可以添加自己的值, 并用实体的 [翻译密钥](/core/entities/naming) 给他们一个翻译和一个图标( 见 [帖式图标](/core/entities/icons)) 。

## 支持的特性 {#supported-features}

将 `HumidifierEntityFeature` 旗帜设置为 `supported_features`。 见 [支持的特性](/glossary/supported-features) 。

| 数值 | 说明 |
| ----- | ----------- |
| `MODES` | 设备有模式 。 设定 `mode` 和 `available_modes`, 并执行 `set_mode` 。 |

## 方法 {#methods}

执行岔或每种方法的同步变体,而不是两者。

| 就在那时 | Async 变体 | 说明 |
| ------ | ------------- | ----------- |
| `turn_on(**kwargs: Any)` | `async_turn_on` | 打开装置 |
| `turn_off(**kwargs: Any)` | `async_turn_off` | 关掉装置 |
| `set_humidity(humidity: int)` | `async_set_humidity` | 设定目标湿度. Home Assistant先对照`min_humidity`和`max_humidity`检查一下 |
| `set_mode(mode: str)` | `async_set_mode` | 设定模式 。 需要 `MODES` 。 |

## 状态 {#states}

状态为`on`或`off`,来自`is_on`. 当`is_on`是`None`时,状态是`unknown`.

## 示例 {#example}

```python
from typing import Any

from homeassistant.components.humidifier import (
    HumidifierDeviceClass,
    HumidifierEntity,
)

class MyDehumidifier(HumidifierEntity):
    """A dehumidifier with a target humidity."""

    _attr_has_entity_name = True
    _attr_name = None
    _attr_device_class = HumidifierDeviceClass.DEHUMIDIFIER
    _attr_min_humidity = 30
    _attr_max_humidity = 80

    def __init__(self, device: MyDevice) -> None:
        """Set up the dehumidifier."""
        self._device = device
        self._attr_unique_id = device.serial

    @property
    def is_on(self) -> bool:
        """Return if the device is on."""
        return self._device.is_on

    @property
    def target_humidity(self) -> float:
        """Return the target humidity."""
        return self._device.target

    async def async_set_humidity(self, humidity: int) -> None:
        """Set the target humidity."""
        await self._device.set_target(humidity)

    async def async_turn_on(self, **kwargs: Any) -> None:
        """Turn the device on."""
        await self._device.turn_on()

    async def async_turn_off(self, **kwargs: Any) -> None:
        """Turn the device off."""
        await self._device.turn_off()
```
