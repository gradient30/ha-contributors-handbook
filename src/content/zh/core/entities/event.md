---
title: 事件实体
description: 将物理世界发生的事情,如傍按键或门铃环,变成一个你可以自动操作的实体.
sidebarLabel: 积极地濑子事件
sidebarGroup: 传感器与状态
---

# 事件实体 {#event-entity}

一个事件实体捕捉到一个瞬间发生的事情:一个遥控器上的按钮被按下,一个门铃环,一个运动传感器火. 它没有自己的持久状态。 你发射事件,和Home Assistant 跟踪上一个。 从`EventEntity`继承,从`homeassistant.components.event`导入。

使用一个事件实体来表示没有打开或关闭状态的瞬间信号 。 如果这东西保持一段时间, 就像检测到的动 一分钟后就可以清除, [二进制传感器](/core/entities/binary-sensor) 更合适。

## 的临时议程 {#properties}

| 名称 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- |
| `event_types` | `list[str]` | 要求数 | 此实体可以开火的事件类型 。 |
| `device_class` | `EventDeviceClass \| None` | `None` | 这些都是什么样的事件。 见[设备类](/core/entities/event#device-classes). |

每个实体的通用属性,如`name`或`available`,都在[实体类别](/core/entities/entity-class)上。 `event_types`列表是一个能力属性,没有记录在历史中.

## 支持的特性 {#supported-features}

该实体没有支持的特性。

## 设备类 {#device-classes}

| 设备类 | 用它 Is it for |
| --- | --- |
| `EventDeviceClass.BUTTON` | 遥控器或墙面开关上的按钮被按下. |
| `EventDeviceClass.DOORBELL` | 门铃的按钮 |
| `EventDeviceClass.MOTION` | 一个运动感应器探测到运动。 |

一个具有设备类而无名称的事件实体会以其设备类命名. 见[名称](/core/entities/naming).

### 标准事件类型 {#standard-event-types}

一些 妈的设备类有标准的事件类型,所以不管哪个集成提供了实体,一个自动化都会起作用. 它们是 `homeassistant.components.event` 的 enums 。

一个 `DOORBELL` 实体必须支持 `DoorbellEventType.RING`. Home Assistant 在不支持时登录一个警告, 从 Home Assistant 开始 2027.4,将停止工作。

`BUTTON` 实体可以使用这些 `ButtonEventType` 值 。 没有一个是强制的:只使用你的硬件可以制作的.

类型分为两层. 物理类型 `PRESS_START` 和 `PRESS_END` 描述按钮向下和向上运行 。 手势类型描述的是设备从新闻上得出的结论.

| 事件类型 | 层 | 含义 |
| --- | --- | --- |
| `PRESS_START` | 物质 | 按钮掉了 只有设备向每个媒体报告时才会使用. |
| `PRESS_END` | 物质 | 按钮在按下设备未分类的时间后发布. |
| `LONG_PRESS_START` | 手势 | 按钮到达了扣子阈值,仍在下方. 每架发射一次 |
| `LONG_PRESS_END` | 手势 | 按钮在按下被归类为长度的设备后发布. |
| `SINGLE_PRESS` | 手势 | 该装置的结论是,正好发生了一次短报。 |
| `MULTI_PRESS` | 手势 | 该设备完成了两个或两个以上按压系列的计数. 长篇大论从来不算 |

`MULTI_PRESS` 包含一个 `press_count` 属性( `ATTR_PRESS_COUNT` 常数 ) , 并带有按数 。 如果您还列出 `SINGLE_PRESS` , 只列出 `MULTI_PRESS` 。 一种报告双面媒体但从未解决过的单面媒体的设备,保持其双面媒体作为非标准事件类型.

当映射设备的事件时 :

- 将设备的一个事件映射到一个标准事件 。 不压制、延迟或综合事件,也不运行定时器。
- 在 `event_types` 中只列出一个类型, 如果该类型的含义对您以该名称开火的每个事件都有效 。
- 一个同时报告发布和解决的单次新闻火灾的设备,作为`PRESS_END`和`SINGLE_PRESS`.
- 一个设备,每个媒体发送一个事件 地图它是什么事件。 按钮落下时发送, 是 `PRESS_START` 。 按钮发布时发送, 是 `PRESS_END` 。 被报道为完成的报章,比如在解密后或通过云服务,它是`SINGLE_PRESS`. 疑时用`SINGLE_PRESS`.
- 达到阈值时报告为 `LONG_PRESS_START` 。 释放后报告的搁置是`LONG_PRESS_END`。
- 只保留本地状态,在 `LONG_PRESS_START` 后将发布分类为 `PRESS_END` 或 `LONG_PRESS_END`, 或当设备重复一次时发射 `LONG_PRESS_START` 。

对于一个从一个来源报告一个方向的按钮,像一个上下摇滚乐者,选择每个方向一个实体. 非标准`direction`属性在独立实体不实际时是可以接受的. 其他非标准事件类型也被允许.

## 方法 {#methods}

你不执行任何方法。 您拨打 `_trigger_event` 启动事件, 然后写下状态 。

### `_trigger_event` {#triggerevent}

```python
def _trigger_event(
    self, event_type: str, event_attributes: dict[str, Any] | None = None
) -> None:
```

`event_type`必须是在 `event_types`, 或调用 `ValueError` 。 可选 `event_attributes` 添加到状态属性中, 旁边是 `event_type` 。 在发布事件后立即拨打 `self.async_write_ha_state()` 。

事件实体在重启后自行恢复其最后一个嗓子: 是 `RestoreEntity` 。

## 状态 {#states}

状态是最后一个事件发射的时间,作为带有毫秒的ISO 8601倍戳. 在第一次活动之前是`unknown`. `event_type` 属性持有最后事件的类型, 以及您通过的任何属性 。

当两个事件在同一毫秒点火时,基级将第二个以毫秒移动向前,所以每个事件都是自己的状态变化.

## 示例 {#example}

听设备的门铃按钮 :

```python
from homeassistant.components.event import (
    DoorbellEventType,
    EventDeviceClass,
    EventEntity,
)
from homeassistant.core import callback

class ExampleDoorbell(EventEntity):
    """Doorbell button of an example device."""

    _attr_has_entity_name = True
    _attr_device_class = EventDeviceClass.DOORBELL
    _attr_event_types = [DoorbellEventType.RING]

    def __init__(self, device: ExampleDevice) -> None:
        """Initialize the event entity."""
        self._device = device
        self._attr_unique_id = f"{device.serial}_doorbell"

    async def async_added_to_hass(self) -> None:
        """Listen for rings."""
        self.async_on_remove(self._device.on_ring(self._handle_ring))

    @callback
    def _handle_ring(self) -> None:
        """Handle a ring from the device."""
        self._trigger_event(DoorbellEventType.RING)
        self.async_write_ha_state()
```

用 `async_on_remove` 注册收听器, 以确保它再次被删除 。 见[实体生命周期](/core/entities/lifecycle).
