---
title: 轻实体
description: 构建一个开关,暗淡,变色或变色温度的灯光实体.
sidebarLabel: 光线
sidebarGroup: 灯光与气候
---

# 轻实体 {#light-entity}

一个光实体控制一个光源:打开和关闭,在硬件允许的地方,它的亮度,颜色,颜色温度,以及效果. 从`LightEntity` 继承到`homeassistant.components.light` 。 用于任何对房间里的人来说是灯光的东西,如灯泡,LED条,或驱动灯具的发光器. 一个普通的中继器,碰巧是电动的灯光, 通常仍然是灯光, 但是一个中继器, 电动其它的都是 [切换](/core/entities/switch).

前端如何显示灯光,请参见[显示更多信息视图](/design/more-info/light).

从 Home Assistant 演示中嵌入的仪表板卡的现场演示。 具有亮度和色温的灯光,在瓷片卡和灯卡中. 牌为直播:淡化,改变其颜色温度,或关闭.

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
        "entity_id": "light.living_room",
        "state": "on",
        "attributes": {
          "friendly_name": "Living room",
          "supported_color_modes": [
            "color_temp"
          ],
          "color_mode": "color_temp",
          "brightness": 180,
          "color_temp_kelvin": 3000,
          "min_color_temp_kelvin": 2000,
          "max_color_temp_kelvin": 6500
        }
      }
    ]
  </script>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "tile",
        "entity": "light.living_room",
        "features": [
          {
            "type": "light-brightness"
          },
          {
            "type": "light-color-temp"
          }
        ]
      }
    </script>
  </ha-embed-card>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "light",
        "entity": "light.living_room"
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

## 的临时议程 {#properties}

光实体在 [一般实体属性](/core/entities/entity-class) 上方有这些属性 。 Applexxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

| 名称 | 类型 | 默认 | 说明 |
| ---- | ---- | ------- | ----------- |
| `is_on` | `bool \| None` | `None` | 是否开灯. |
| `supported_color_modes` | `set[ColorMode] \| None` | 要求数 | 颜色模式支持光线。 见[颜色模式](/core/entities/light#color-modes). |
| `color_mode` | `ColorMode \| None` | `None` | 颜色模式 光是现在。 灯亮时需要 |
| `brightness` | `int \| None` | `None` | 亮度从1到255 |
| `color_temp_kelvin` | `int \| None` | `None` | Kelvin的颜色温度。 仅在 `ColorMode.COLOR_TEMP` 中使用 。 |
| `min_color_temp_kelvin` | `int` | `2000` | 光线支撑的最温暖的颜色温度,以克尔文计算. |
| `max_color_temp_kelvin` | `int` | `6535` | 墅里最冷的颜色温度 以克尔文为单位 |
| `hs_color` | `tuple[float, float] \| None` | `None` | 色调(0至360)和饱和度(0至100). 仅在`ColorMode.HS`中使用. |
| `xy_color` | `tuple[float, float] \| None` | `None` | CIE xy 颜色. 仅在 `ColorMode.XY` 中使用 。 |
| `rgb_color` | `tuple[int, int, int] \| None` | `None` | 红色,绿色,蓝色,每个0到255个. 仅在 `ColorMode.RGB` 中使用 。 |
| `rgbw_color` | `tuple[int, int, int, int] \| None` | `None` | 红色,绿色,蓝色,白色 仅在 `ColorMode.RGBW` 中使用 。 |
| `rgbww_color` | `tuple[int, int, int, int, int] \| None` | `None` | 红,绿,蓝,冷白,温白. 仅在 `ColorMode.RGBWW` 中使用 。 |
| `effect_list` | `list[str] \| None` | `None` | 光能显示的效果. 需要 `LightEntityFeature.EFFECT` 。 |
| `effect` | `str \| None` | `None` | 现在的效应。 当光支持效果但无运行时使用 `EFFECT_OFF` (`"off"`). |

颜色属性只有在匹配当前 `color_mode` 时才会在状态中结束 。 在 `ColorMode.HS` 中同样返回 `rgb_color` 的光线被忽略 。 Home Assistant 填写您的其他颜色格式( `hs_color`, `rgb_color` 和`xy_color`), 从匹配颜色模式的颜色格式转换 。

在`ColorMode.RGB`,`ColorMode.RGBW`和`ColorMode.RGBWW`中,亮度生活在两个地方:在`brightness`,和颜色本身. 亮度为128,颜色为(192,64,32),总体亮度为128/255×192/255,约占38%.

## 颜色模式 {#color-modes}

每一道光必须设定 `supported_color_modes`,每一道光必须报告 `color_mode`。 两者都使用`ColorMode`enum. 如果一个光线离开 `supported_color_modes` 空, 设置无效的组合, 或报告它没有列出的颜色模式, 写入它的状态会引起错误 。

| 数值 | 说明 |
| ----- | ----------- |
| `ColorMode.ONOFF` | 灯光只能打开和关闭。 必须是唯一支持的模式 。 |
| `ColorMode.BRIGHTNESS` | 光能暗淡,无更无更. 必须是唯一支持的模式 。 |
| `ColorMode.COLOR_TEMP` | 光线可以暗淡,其白色的色温也会改变,通过`color_temp_kelvin`读取. |
| `ColorMode.HS` | 光线可以变暗,其颜色设定为hue和饱和,通过`hs_color`. |
| `ColorMode.XY` | 光线可以暗化,其颜色在CIE xy中设定,通过`xy_color`. |
| `ColorMode.RGB` | 光线可以变暗,其颜色设定为RGB,通过`rgb_color`. |
| `ColorMode.RGBW` | 如RGB,带有额外的白色通道,通过`rgbw_color`. |
| `ColorMode.RGBWW` | 与RGB一样,带有冷白和暖白通道,通过`rgbww_color`. |
| `ColorMode.WHITE` | 光线可以用 `white` 参数切换为纯白模式 。 没有 `white` 属性 。 仅与至少一个颜色模式(`HS`,`XY`,`RGB`,`RGBW`,或`RGBWW`一起有效). |
| `ColorMode.UNKNOWN` | 颜色模式目前尚不得而知. 只有 `color_mode` 有效, 绝不在 `supported_color_modes` 中 。 |

两个白色模式的区别: {藜H0} 让你调整颜色温度, 通常用暖白色的库和冷白色的LED的库. `ColorMode.WHITE`有一个单一的,固定的白色。

### 效果运行时的颜色模式 {#color-mode-while-an-effect-runs}

当效果运行时, 报告匹配效果仍然允许调整的颜色模式 。 如果效果不允许调整,请使用`ColorMode.ONOFF`. 如果只允许亮度, 请使用 `ColorMode.BRIGHTNESS` 。 Home Assistant 接受 `ColorMode.ONOFF` 效果时, 即使它不是在 `supported_color_modes` , 而`ColorMode.BRIGHTNESS` 当您支持的颜色模式至少有一种具有亮度 。 这只适用于具有`EFFECT`特性的灯,而`effect`是设定的,而不是`EFFECT_OFF`.

## 支持的特性 {#supported-features}

将 `LightEntityFeature` 旗帜与 `|` 合并, 设置为 `supported_features`。 见 [支持的特性](/glossary/supported-features) 。

| 数值 | 说明 |
| ----- | ----------- |
| `EFFECT` | 光能示现功德. 设置 `effect_list` 和 `effect` 。 |
| `FLASH` | 光能闪烁. 您的 `turn_on` 用 `short` 或 `long` 接收 `flash` 。 |
| `TRANSITION` | 光可以在各州之间消逝。 關 關 關 |

未设置的特性参数在调用方法前会被删除 。

## 方法 {#methods}

### 打开 {#turn-on}

```python
def turn_on(self, **kwargs: Any) -> None:
    """Turn the light on."""

async def async_turn_on(self, **kwargs: Any) -> None:
    """Turn the light on."""
```

关键词参数使用来自`homeassistant.components.light`的常数,如`ATTR_BRIGHTNESS`,`ATTR_COLOR_TEMP_KELVIN`,`ATTR_HS_COLOR`,`ATTR_RGB_COLOR`,`ATTR_WHITE`,`ATTR_EFFECT`,`ATTR_FLASH`和`ATTR_TRANSITION`。

你从未收到过一个颜色模式。 相反,你得到最多一个颜色属性, 它总是一个你的光支持。 当一个动作以格式请求颜色时, 您的光线不支持, Home Assistant 首先转换它 。 例如,一个 `hs_color` 变成 `rgb_color` 对于只支持 `ColorMode.RGB` 的光线来说。 亮度作为百分比或步骤也转换为`ATTR_BRIGHTNESS` 在它到达你之前。 对于支持 `ColorMode.WHITE` 的光线, `ATTR_WHITE` 带有白色模式的亮度 : 当一个动作同时设置 `white` 和 `brightness`时, 您只接收 `ATTR_WHITE`, 带有亮度的值 。 当亮度, 或 `white` 最终为 0 时, 就像从暗光下台后, Home Assistant 调用您的 `turn_off` 而不是 `turn_on` 。

### 关机 {#turn-off}

```python
def turn_off(self, **kwargs: Any) -> None:
    """Turn the light off."""

async def async_turn_off(self, **kwargs: Any) -> None:
    """Turn the light off."""
```

`turn_off`可以在光线支持时收到`ATTR_TRANSITION`和`ATTR_FLASH`.

### 切换 {#toggle}

`light.toggle`动作呼叫`async_toggle`。 默认情况下,它会录像带在灯光关闭时调用您的 `turn_on`, 否则则调用您的 `turn_off`, 转换方式与动作相同 。 你不需要执行它。 如果设备有自己的切换命令,可以覆盖`async_toggle`. 没有同步 `toggle` : Home Assistant 从不调用它 。

```python
async def async_toggle(self, **kwargs: Any) -> None:
    """Toggle the light."""
```

### 缩放亮度 {#scaling-brightness}

许多设备使用1至255的另一个范围. 在 `homeassistant.util.color` 中帮助 `value_to_brightness` 和 `brightness_to_value` 的转换 。

```python
import math

from homeassistant.util.color import brightness_to_value, value_to_brightness

BRIGHTNESS_SCALE = (1, 1023)

brightness = value_to_brightness(BRIGHTNESS_SCALE, device_value)
device_value = math.ceil(brightness_to_value(BRIGHTNESS_SCALE, brightness))
```

## 状态 {#states}

状态为`on`或`off`,来自`is_on`. 当`is_on`是`None`时,状态是`unknown`.

## 示例 {#example}

```python
from typing import Any

from homeassistant.components.light import (
    ATTR_BRIGHTNESS,
    ColorMode,
    LightEntity,
)

class MyLight(LightEntity):
    """A dimmable light."""

    _attr_has_entity_name = True
    _attr_name = None
    _attr_color_mode = ColorMode.BRIGHTNESS
    _attr_supported_color_modes = {ColorMode.BRIGHTNESS}

    def __init__(self, device: MyDevice) -> None:
        """Set up the light."""
        self._device = device
        self._attr_unique_id = device.serial

    @property
    def is_on(self) -> bool:
        """Return if the light is on."""
        return self._device.is_on

    @property
    def brightness(self) -> int:
        """Return the brightness, 1 to 255."""
        return self._device.brightness

    async def async_turn_on(self, **kwargs: Any) -> None:
        """Turn the light on."""
        brightness = kwargs.get(ATTR_BRIGHTNESS, self.brightness)
        await self._device.turn_on(brightness)

    async def async_turn_off(self, **kwargs: Any) -> None:
        """Turn the light off."""
        await self._device.turn_off()
```
