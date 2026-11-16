---
title: 警报器实体
description: 为警笛和鸣笛建立警笛实体,发出声调、音量和持续时间。
sidebarLabel: 警报器
sidebarGroup: 开合与安防
---

# 警报实体 {#siren-entity}

一个警报器实体控制着一个发出响亮的声音来引起注意的东西:一个警报器,一个响亮的警报器,或者一个门铃鸣笛. 其开关不通,可取声调,音量,及长短. 从`SirenEntity` 继承到`homeassistant.components.siren` 。 它建立在切换实体上,因此它有`is_on`,`turn_on`和`turn_off`.

警报器所属的安全系统是 [提醒控制面板](/core/entities/alarm-control-panel) 。 播放任何音频的扬声器为[媒体播放器](/core/entities/media-player).

## 的临时议程 {#properties}

警报实体在 [一般实体属性](/core/entities/entity-class) 上方有这些属性 。 每个属性都可以以其`_attr_`属性设定,如`_attr_available_tones`.

| 名称 | 类型 | 默认 | 说明 |
| ---- | ---- | ------- | ----------- |
| `is_on` | `bool \| None` | `None` | 警笛是否响起? |
| `available_tones` | `list[int \| str] \| dict[int, str] \| None` | `None` | 警报器能演奏的音量 需要使用 `TONES` 。 也可以设置在实体描述上 。 |

`available_tones`是声调名称或数字列表,或从声调数字到声调名称的词典. 使用词典,动作可以按其名称选择音调,Home Assistant通过匹配的编号.

## 支持的特性 {#supported-features}

将 `SirenEntityFeature` 旗帜与 `|` 合并, 设置为 `supported_features`。 见 [支持的特性](/glossary/supported-features) 。

| 数值 | 说明 |
| ----- | ----------- |
| `TURN_ON` | 警笛可以打开 执行`turn_on`。 |
| `TURN_OFF` | 警报器可以关闭。 执行`turn_off`。 |
| `TONES` | 警笛可以演奏不同的音调. 设定`available_tones`. |
| `VOLUME_SET` | 当警报响起时可以设定音量. |
| `DURATION` | 警笛开启时可以设定持续时间. |

## 方法 {#methods}

执行岔或每种方法的同步变体,而不是两者。

| 就在那时 | Async 变体 | 特性 |
| ------ | ------------- | ------- |
| `turn_on(**kwargs: Any)` | `async_turn_on` | `TURN_ON` |
| `turn_off(**kwargs: Any)` | `async_turn_off` | `TURN_OFF` |

`turn_on` 只能收到這些关键字參數, 只因為您所設定的功能 :

- `ATTR_TONE`: 播放的音调, 请检查 `available_tones` 首先是
- `ATTR_VOLUME_LEVEL`:音量,从0到1
- `ATTR_DURATION`: 音长, 秒

## 状态 {#states}

状态为`on`或`off`,来自`is_on`. 当`is_on`是`None`时,状态是`unknown`.

`available_tones`是一个能力属性。 只有在警报器支持`TONES`时,它才在那里,并且从记录器的历史中被忽略.

## 示例 {#example}

```python
from typing import Any

from homeassistant.components.siren import (
    ATTR_TONE,
    SirenEntity,
    SirenEntityFeature,
)

class MySiren(SirenEntity):
    """A siren with a few tones."""

    _attr_has_entity_name = True
    _attr_name = None
    _attr_available_tones = {1: "fire", 2: "intruder", 3: "doorbell"}
    _attr_supported_features = (
        SirenEntityFeature.TURN_ON
        | SirenEntityFeature.TURN_OFF
        | SirenEntityFeature.TONES
    )

    def __init__(self, device: MyDevice) -> None:
        """Set up the siren."""
        self._device = device
        self._attr_unique_id = device.serial

    @property
    def is_on(self) -> bool:
        """Return if the siren sounds."""
        return self._device.sounding

    async def async_turn_on(self, **kwargs: Any) -> None:
        """Sound the siren."""
        await self._device.sound(tone=kwargs.get(ATTR_TONE, 1))

    async def async_turn_off(self, **kwargs: Any) -> None:
        """Silence the siren."""
        await self._device.silence()
```
