---
title: 覆盖实体
description: 为百叶窗,遮荫窗,车库门,闸门,以及其他打开和关闭的东西建立掩蔽实体.
sidebarLabel: 覆盖
sidebarGroup: 开合与安防
---

# 覆盖实体 {#cover-entity}

一个封面实体控制着打开和关闭在开口上的东西:百叶窗、遮阳窗、窗帘、黄昏窗、车库门、大门和机动窗户。 它可以报告并设定位置,并倾斜用于有斜线的盲窗. 从`CoverEntity` 继承到`homeassistant.components.cover` 。

只能用一个盖子来掩护一个开口的地方 控制水或气流的设备是 [阀门](/core/entities/valve) 。 锁门和锁门是 [锁定](/core/entities/lock) 。 对于其他任何东西,使用另一个实体类型,比如[编号](/core/entities/number),即使旧的集成使用封面.

前端如何显示封面,请参见[覆盖更多信息视图](/design/more-info/cover).

从 Home Assistant 演示中嵌入的仪表板卡的现场演示。 一个盖子打开,关闭,停止,并设置一个位置,在瓷砖卡中. 卡片为直播:打开,关闭,或移动百叶窗.

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
        "entity_id": "cover.living_room_blinds",
        "state": "open",
        "attributes": {
          "friendly_name": "Living room blinds",
          "device_class": "blind",
          "current_position": 70,
          "supported_features": 15
        }
      }
    ]
  </script>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "tile",
        "entity": "cover.living_room_blinds",
        "features": [
          {
            "type": "cover-open-close"
          },
          {
            "type": "cover-position"
          }
        ]
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

## 的临时议程 {#properties}

覆盖实体在 [一般实体属性](/core/entities/entity-class) 之上有这些属性 。 每个属性都可以以其`_attr_`属性设定,如`_attr_is_closed`.

| 名称 | 类型 | 默认 | 说明 |
| ---- | ---- | ------- | ----------- |
| `is_closed` | `bool \| None` | 要求数 | 封面是否关闭 。 为州所用. |
| `is_opening` | `bool \| None` | `None` | 封面是否打开 。 为州所用. |
| `is_closing` | `bool \| None` | `None` | 封好运是不是关了? 为州全盘用. |
| `current_cover_position` | `int \| None` | `None` | 该职位从0(非公开)到100(完全开放)。 |
| `current_cover_tilt_position` | `int \| None` | `None` | 0(封闭或无倾斜)至100(开放或最大倾斜)的倾斜. |
| `device_class` | `CoverDeviceClass \| None` | `None` | 何等为盖. 见[设备类](/core/entities/cover#device-classes). |
| `supported_speeds` | `list[str] \| None` | `None` | 当封面打开、关闭或移动到一个位置时,其速度可以移动。 `None` 或空列表表示没有速度选择 。 使用 `CoverSpeed.FAST` 、 `CoverSpeed.MEDIUM` 和 `CoverSpeed.SLOW` 从 `homeassistant.components.cover` 开始的标准速度 。 一个没有速度的动作以设备的默认速度移动封面. |

当您将 `supported_speeds` 设置为列表时, Home Assistant 把它添加为 `supported_speeds` 属性, 并在它召唤你之前检查 `speed` 。 一个不在列表中的速度被放弃,封面以默认速度移动. 没有速度, 动作中的 `speed` 会被丢弃 。

## 设备类 {#device-classes}

从 `CoverDeviceClass` 设置一个 [设备类](/glossary/device-class) 。 它设置了图标,前端各州的措辞,以及语音助理如何谈论封面.

| 数值 | 说明 |
| ----- | ----------- |
| `AWNING` | 像可收回的窗子 门 或院子 |
| `BLIND` | 盲窗:连接的线条,可膨胀,倒塌,或倾斜以覆盖开口,如窗窗盲. |
| `CURTAIN` | 窗帘或帘 妈妈经常挂在窗或门上,拉开和关闭 |
| `DAMPER` | 减少气流,声音,或光线的机械坝体. |
| `DOOR` | 门可以进入一个地区,通常是建筑物的一部分。 |
| `GARAGE` | 车库门 |
| `GATE` | 通往车道或其他地区的大门,在建筑物外,一般是栅栏的一部分。 |
| `SHADE` | 阴影(Shades):一个连续的块材料或相连的细胞,在开口处膨胀或坍塌,如窗荫. |
| `SHUTTER` | 百叶窗:向外或向内或向外倾斜的连结斜拉窗,以覆盖一个开口,如窗百叶窗. |
| `WINDOW` | 一个打开、关闭或倾斜的窗口。 |

## 支持的特性 {#supported-features}

将 `CoverEntityFeature` 旗帜与 `|` 合并, 设置为 `supported_features`。 见 [支持的特性](/glossary/supported-features) 。

| 数值 | 说明 |
| ----- | ----------- |
| `OPEN` | 盖能开. 执行`open_cover`。 |
| `CLOSE` | 封面可以关闭。 执行`close_cover`。 |
| `SET_POSITION` | 封面可以移动到一个位置. 执行`set_cover_position`。 |
| `STOP` | 封面可以在移动时停止. 执行`stop_cover`。 |
| `OPEN_TILT` | 封面可以倾斜开. 执行`open_cover_tilt`。 |
| `CLOSE_TILT` | 封面可以倾斜关闭. 执行`close_cover_tilt`。 |
| `STOP_TILT` | 哺育罩可以在倾斜时停止.哺育`stop_cover_tilt`。 |
| `SET_TILT_POSITION` | 封面可以倾斜到一个位置. 执行`set_cover_tilt_position`。 |
| `SPEED` | 封面可以以不同的速度移动. 设定`supported_speeds`. |

如果您根本不设置 `supported_features`, Home Assistant 猜测 : `OPEN`, `CLOSE` 和 `STOP`, 加上 `SET_POSITION` 当封面报告位置时, 当它报告倾斜时所有倾斜的特性, 当它有速度时, `SPEED` 。 自己设定特征,所以前端只显示封面能够真正做什么.

## 方法 {#methods}

执行岔或每种方法的同步变体,而不是两者。

| 就在那时 | Async 变体 | 特性 |
| ------ | ------------- | ------- |
| `open_cover(**kwargs: Any)` | `async_open_cover` | `OPEN` |
| `close_cover(**kwargs: Any)` | `async_close_cover` | `CLOSE` |
| `set_cover_position(**kwargs: Any)` | `async_set_cover_position` | `SET_POSITION` |
| `stop_cover(**kwargs: Any)` | `async_stop_cover` | `STOP` |
| `open_cover_tilt(**kwargs: Any)` | `async_open_cover_tilt` | `OPEN_TILT` |
| `close_cover_tilt(**kwargs: Any)` | `async_close_cover_tilt` | `CLOSE_TILT` |
| `set_cover_tilt_position(**kwargs: Any)` | `async_set_cover_tilt_position` | `SET_TILT_POSITION` |
| `stop_cover_tilt(**kwargs: Any)` | `async_stop_cover_tilt` | `STOP_TILT` |

`set_cover_position`收到`ATTR_POSITION`,和`set_cover_tilt_position`收到`ATTR_TILT_POSITION`,都从0到100 `open_cover`,`close_cover`,和`set_cover_position`都可以收到`ATTR_SPEED`,当封面有`supported_speeds`.

摇摆是为你处理的。 `toggle` 支持 `STOP` 时停止移动封面, 打开一个关闭或关闭封面, 关闭一个打开或完全打开的封面 。 一个部分停止开放的封面从它报告的最后一个方向向另一方向移动,在它从未报告一个方向时关闭. `toggle_tilt`在0时打开倾斜,否则关闭.

## 状态 {#states}

状态来自`is_opening`,`is_closing`和`is_closed`,依此顺序,作为`CoverState`:

| 数值 | 说明 |
| ----- | ----------- |
| `CoverState.OPENING` | 封面打开了 |
| `CoverState.CLOSING` | 封面快关了 |
| `CoverState.CLOSED` | 盖已闭韵. |
| `CoverState.OPEN` | 封面是开放的,全部或部分. |

当封面不动而`is_closed`为`None`时,状态为`unknown`.

## 示例 {#example}

```python
from typing import Any

from homeassistant.components.cover import (
    ATTR_POSITION,
    CoverDeviceClass,
    CoverEntity,
    CoverEntityFeature,
)

class MyBlind(CoverEntity):
    """A blind that moves to a position."""

    _attr_has_entity_name = True
    _attr_name = None
    _attr_device_class = CoverDeviceClass.BLIND
    _attr_supported_features = (
        CoverEntityFeature.OPEN
        | CoverEntityFeature.CLOSE
        | CoverEntityFeature.STOP
        | CoverEntityFeature.SET_POSITION
    )

    def __init__(self, device: MyDevice) -> None:
        """Set up the blind."""
        self._device = device
        self._attr_unique_id = device.serial

    @property
    def current_cover_position(self) -> int:
        """Return the position, 0 is closed."""
        return self._device.position

    @property
    def is_closed(self) -> bool:
        """Return if the blind is closed."""
        return self._device.position == 0

    async def async_open_cover(self, **kwargs: Any) -> None:
        """Open the blind."""
        await self._device.move_to(100)

    async def async_close_cover(self, **kwargs: Any) -> None:
        """Close the blind."""
        await self._device.move_to(0)

    async def async_set_cover_position(self, **kwargs: Any) -> None:
        """Move the blind to a position."""
        await self._device.move_to(kwargs[ATTR_POSITION])

    async def async_stop_cover(self, **kwargs: Any) -> None:
        """Stop the blind."""
        await self._device.stop()
```
