---
title: 切换实体
description: 构建一个开关实体,用于您可以打开或关闭的东西,比如继电器或智能插件.
sidebarLabel: 开关
sidebarGroup: 输入与助手
---

# 切换实体 {#switch-entity}

一个开关实体打开或关闭一些东西:继电器,智能插件,或者像"孩子锁"或"LED指示器"这样的设备上的设置. 从`SwitchEntity` 继承到`homeassistant.components.switch` 。

选一个平台 匹配的东西是:

- 它有运行状态和关闭状态,但Home Assistant不能改变它,就像只报告的一个墙开关:使用[二进制传感器](/core/entities/binary-sensor).
- 它没有状态,只触发某种东西,比如重启一个设备:使用[按钮](/core/entities/button).
- 这是一个按键, 人们按: 使用 [事件](/core/entities/event) 实体 。
- 它是一个灯光,一个风扇,或者一个阀门:使用那个平台. 它赋予用户正确的控制,语音助理正确的设备类型,以及你正确的功能.

前端如何显示开关,请参见[切换更多信息视图](/design/more-info/switch).

从 Home Assistant 演示中嵌入的仪表板卡的现场演示。 瓷砖卡中的智能插座. 牌是直播:关了又关.

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
        "entity_id": "switch.coffee_machine",
        "state": "on",
        "attributes": {
          "friendly_name": "Coffee machine",
          "device_class": "outlet"
        }
      }
    ]
  </script>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "tile",
        "entity": "switch.coffee_machine",
        "features": [
          {
            "type": "toggle"
          }
        ]
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

## 的临时议程 {#properties}

| 名称 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- |
| `is_on` | `bool \| None` | `None` | 是否打开开关 。 `None`表示状态未知. |
| `device_class` | `SwitchDeviceClass \| None` | `None` | 这是什么样的开关。 见[设备类](/core/entities/switch#device-classes). |

每个实体的通用属性,如`name`,`available`和`unique_id`,都在[实体类别](/core/entities/entity-class)上.

## 支持的特性 {#supported-features}

该实体没有支持的特性。

## 设备类 {#device-classes}

| 常数 | 说明 |
| --- | --- |
| `SwitchDeviceClass.OUTLET` | 电源插座,如智能插座或电源带上的插座. |
| `SwitchDeviceClass.SWITCH` | 通用开关. |

语音助理使用设备类来选择匹配设备类型.

## 方法 {#methods}

### 打开和关闭 {#turn-on-and-off}

既执行同步,又执行同步变体。 Home Assistant 通过额外的参数作为关键词参数,所以在签名中保留`**kwargs`.

```python
class MySwitch(SwitchEntity):
    

# Implement one of each pair. {#toggle}

    def turn_on(self, **kwargs: Any) -> None:
        """Turn the switch on."""

    async def async_turn_on(self, **kwargs: Any) -> None:
        """Turn the switch on."""

    def turn_off(self, **kwargs: Any) -> None:
        """Turn the switch off."""

    async def async_turn_off(self, **kwargs: Any) -> None:
        """Turn the switch off."""
```

### 切换 {#states}

你通常不需要这个 基础类已经执行 `async_toggle` : 当 `is_on` 是真的时, 它会调用您的关闭方法, 否则则调用方法 。 当设备有本地切换命令时, 只能覆盖 `async_toggle` 。 同步 `toggle` 是最终的 : Home Assistant 从不调用, 所以不要执行它 。

## 状态 {#example}

基准类从 `is_on` 建立状态 :

| 状态 | 何时 |
| --- | --- |
| `on` | `is_on` is `True` |
| `off` | `is_on` is `False` |
| `unknown` | `is_on` is `None` |

你自己不设州. `unavailable`来自`available`财产,就像每个实体一样。

## 示例 {#示例}

```python
from typing import Any

from homeassistant.components.switch import (
    SwitchDeviceClass,
    SwitchEntity,
)

class ExampleOutlet(SwitchEntity):
    """A smart plug."""

    _attr_has_entity_name = True
    _attr_name = None
    _attr_device_class = SwitchDeviceClass.OUTLET

    def __init__(self, device: ExampleDevice) -> None:
        """Initialize the outlet."""
        self._device = device
        self._attr_unique_id = device.serial
        self._attr_is_on = device.is_on

    async def async_turn_on(self, **kwargs: Any) -> None:
        """Turn the outlet on."""
        await self._device.turn_on()
        self._attr_is_on = True
        self.async_write_ha_state()

    async def async_turn_off(self, **kwargs: Any) -> None:
        """Turn the outlet off."""
        await self._device.turn_off()
        self._attr_is_on = False
        self.async_write_ha_state()
```

插头是其设备的主要特征,因此`_attr_name = None`给实体以设备的名称. 见[命名实体](/core/entities/naming).
