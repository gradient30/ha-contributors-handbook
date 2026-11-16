---
title: 粉丝实体
description: 构建一个控制速度,方向,振荡,预设模式的扇形实体.
sidebarLabel: 风扇
sidebarGroup: 灯光和气候
---

# 粉丝实体 {#fan-entity}

风扇实体控制风扇:其速度,方向,无论是振荡,还是像`auto`或`breeze`这样的预设模式. 从`FanEntity`在`homeassistant.components.fan`中继承。 它建立在切换实体上,因此它有`is_on`,`turn_on`和`turn_off`.

属于空调或热泵的风扇属于[气候实体](/core/entities/climate),作为它的风扇模式. 使用风扇实体作为独立风扇,天花板风扇,或空气净化风扇.

前端如何显示风扇,请参见[扇形视图](/design/more-info/fan).

从 Home Assistant 演示中嵌入的仪表板卡的现场演示。 风扇有速度,预设,振荡,方向,呈瓦片卡状. 卡片为直播:改变速度或选择预设.

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
        "entity_id": "fan.bedroom",
        "state": "on",
        "attributes": {
          "friendly_name": "Bedroom fan",
          "percentage": 50,
          "percentage_step": 25,
          "preset_modes": [
            "auto",
            "sleep"
          ],
          "preset_mode": null,
          "oscillating": false,
          "direction": "forward",
          "supported_features": 63
        }
      }
    ]
  </script>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "tile",
        "entity": "fan.bedroom",
        "features": [
          {
            "type": "fan-speed"
          },
          {
            "type": "fan-preset-modes"
          },
          {
            "type": "fan-oscillate"
          },
          {
            "type": "fan-direction"
          }
        ]
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

## 的临时议程 {#properties}

扇形实体在 [一般实体属性](/core/entities/entity-class) 上方有这些属性 。 每个属性都可以以其`_attr_`属性设定,如`_attr_percentage`.

| 名称 | 类型 | 默认 | 说明 |
| ---- | ---- | ------- | ----------- |
| `is_on` | `bool \| None` | 计算 | 扇子开不开? 默认情况下,当 `percentage` 高于 0 或预设活动时, 风扇会打开 。 当你的装置知道得更清楚时,就取消它。 |
| `percentage` | `int \| None` | `0` | 目前的速度,从0(关闭)到100. |
| `speed_count` | `int` | `100` | 风扇的速率 Home Assistant 用它来计算 `percentage_step` 。 |
| `preset_mode` | `str \| None` | `None` | 活动预设, 或 `None` 当没有活动预设时 。 |
| `preset_modes` | `list[str] \| None` | `None` | 预设扇支持. |
| `current_direction` | `str \| None` | `None` | 风扇转方向:`DIRECTION_FORWARD`(`"forward"`)或`DIRECTION_REVERSE`(`"reverse"`). |
| `oscillating` | `bool \| None` | `None` | 风扇是否振荡. |

`percentage_step`从`speed_count`计算为 咱们100除以速度数。 你没有自己设置。

### 速度和百分比 {#speeds-and-percentages}

Home Assistant总是谈论风扇速度作为百分比。 如果您的设备有固定的速度数, 请设置 `speed_count` , 并在 `homeassistant.util.percentage` 中与助手在两者之间转换 :

- `ranged_value_to_percentage` 和`percentage_to_ranged_value` 数字范围, 如速度 1 到 6
- `ordered_list_item_to_percentage`和`percentage_to_ordered_list_item` 对于一个命名速度列表, 如`low`,`medium`和`high`

关闭不是范围或列表的一部分: 0 的百分比是关闭的 。

### 预设模式 {#preset-modes}

预设是风扇控制自身速度的一种模式,或者自行做别的事情. 常见的例子有`auto` 确实,`smart`,`eco`和`breeze`。 当未激活预设时, `preset_mode` 必须是`None` 。

命名的手动速度不是预设的:以百分比表示. 手设定速度必须结束活动预设 。 如果设备允许您在预设活动时设置一个速度, 则用单独的 [切换](/core/entities/switch) 来代表预设 。

## 支持的特性 {#supported-features}

将 `FanEntityFeature` 旗帜与 `|` 合并, 设置为 `supported_features`。 见 [支持的特性](/glossary/supported-features) 。

| 数值 | 说明 |
| ----- | ----------- |
| `SET_SPEED` | 风扇可以改变速度. 执行`set_percentage`。 |
| `PRESET_MODE` | 风扇有预设模式. 执行`set_preset_mode`。 |
| `OSCILLATE` | 风扇能 o. 执行`oscillate`。 |
| `DIRECTION` | 风扇可以改变方向. 执行`set_direction`。 |
| `TURN_ON` | 扇子可以打开. 执行`turn_on`。 |
| `TURN_OFF` | 扇子可以关机. 执行`turn_off`。 |

您未设置的特性动作在到达您的实体之前被拒绝 。

## 方法 {#methods}

执行岔或每种方法的同步变体,而不是两者。

| 就在那时 | Async 变体 | 特性 |
| ------ | ------------- | ------- |
| `turn_on(percentage: int \| None = None, preset_mode: str \| None = None, **kwargs: Any)` | `async_turn_on` | `TURN_ON` |
| `turn_off(**kwargs: Any)` | `async_turn_off` | `TURN_OFF` |
| `set_percentage(percentage: int)` | `async_set_percentage` | `SET_SPEED` |
| `set_preset_mode(preset_mode: str)` | `async_set_preset_mode` | `PRESET_MODE` |
| `set_direction(direction: str)` | `async_set_direction` | `DIRECTION` |
| `oscillate(oscillating: bool)` | `async_oscillate` | `OSCILLATE` |

问 题

- `turn_on`可以收到一个百分数,一个预设,两者兼而有之,或者两者无之. 当它没有得到两个, 打开风扇的速度 设备选择。
- 百分之零意味着关闭。 默认的 `async_set_percentage` 调用 `async_turn_off` , 然后仍然将 0 传给 `set_percentage` 。 当您覆盖 `async_set_percentage` 时, 请自己处理 0 。 减速到最低步以下 也最终达到0。
- Home Assistant 在调用 `set_preset_mode` 或 `turn_on` 之前对照 `preset_modes` 检查一个预设, 当它不在列表中时, 则引起验证错误 。
- `toggle` 是为你处理的: 它根据`is_on`调用`turn_on`或`turn_off`。
- `increase_speed`和`decrease_speed`都是为你处理的。 注意,他们先先到,先到 当设备有它自己的命令时, 您只覆盖 `async_increase_speed` 和 `async_decrease_speed` 。

## 状态 {#states}

状态为`on`或`off`,来自`is_on`. 当`is_on`是`None`时,状态是`unknown`.

## 示例 {#example}

```python
import math
from typing import Any

from homeassistant.components.fan import FanEntity, FanEntityFeature
from homeassistant.util.percentage import (
    percentage_to_ranged_value,
    ranged_value_to_percentage,
)

SPEED_RANGE = (1, 3)

class MyFan(FanEntity):
    """A fan with three speeds."""

    _attr_has_entity_name = True
    _attr_name = None
    _attr_speed_count = 3
    _attr_supported_features = (
        FanEntityFeature.SET_SPEED
        | FanEntityFeature.TURN_ON
        | FanEntityFeature.TURN_OFF
    )

    def __init__(self, device: MyDevice) -> None:
        """Set up the fan."""
        self._device = device
        self._attr_unique_id = device.serial

    @property
    def percentage(self) -> int:
        """Return the speed as a percentage."""
        if not self._device.speed:
            return 0
        return ranged_value_to_percentage(SPEED_RANGE, self._device.speed)

    async def async_set_percentage(self, percentage: int) -> None:
        """Set the speed."""
        if percentage == 0:
            await self._device.turn_off()
            return

        

# Round up, so 1% is the lowest speed and not off {#round-up-so-1-is-the-lowest-speed-and-not-off}
        speed = math.ceil(percentage_to_ranged_value(SPEED_RANGE, percentage))
        await self._device.set_speed(speed)

    async def async_turn_on(
        self,
        percentage: int | None = None,
        preset_mode: str | None = None,
        **kwargs: Any,
    ) -> None:
        """Turn the fan on."""
        if percentage is not None:
            await self.async_set_percentage(percentage)
            return
        await self._device.turn_on()

    async def async_turn_off(self, **kwargs: Any) -> None:
        """Turn the fan off."""
        await self._device.turn_off()
```
