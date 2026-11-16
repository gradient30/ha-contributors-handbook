---
title: 阀门实体
description: 为控制水或气流的设备建立阀门实体.
sidebarLabel: 阀门
sidebarGroup: 开合与安防
---

# 阀门实体 {#valve-entity}

阀门实体控制流体或气体通过管道的流量:水主闭塞、灌溉阀门或管道。 有些阀门只能打开和关闭,有些阀门可以设置在两者之间的位置. 从`ValveEntity` 继承到`homeassistant.components.valve` 。

打开和关闭一个开口的东西, 像一个盲人或车库的门, 是[覆盖](/core/entities/cover)。

前端如何显示阀门,参见[阀门更多信息视图](/design/more-info/valve)}.

从 Home Assistant 演示中嵌入的仪表板卡的现场演示。 一个水阀,打开,关闭,设置一个位置,在一个瓦片卡. 卡片为直播:关闭卡片,或设定开多远.

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
        "entity_id": "valve.garden_irrigation",
        "state": "open",
        "attributes": {
          "friendly_name": "Garden irrigation",
          "device_class": "water",
          "current_position": 60,
          "supported_features": 15
        }
      }
    ]
  </script>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "tile",
        "entity": "valve.garden_irrigation",
        "features": [
          {
            "type": "valve-open-close"
          },
          {
            "type": "valve-position"
          }
        ]
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

## 的临时议程 {#properties}

阀门实体在 [一般实体属性](/core/entities/entity-class) 上方有这些属性 。 每个属性都可以以其`_attr_`属性设定,如`_attr_is_closed`.

| 名称 | 类型 | 默认 | 说明 |
| ---- | ---- | ------- | ----------- |
| `reports_position` | `bool` | 要求数 | 阀门是否报告位置. 它决定国家是来自`current_valve_position`还是来自`is_closed`. 也可以设置在实体描述上, 它默认为 `False` 。 |
| `current_valve_position` | `int \| None` | `None` | 该职位从0(非公开)到100(完全开放)。 当 `reports_position` 是 `True` 时使用 。 |
| `is_closed` | `bool \| None` | `None` | 阀门是否关闭 。 当 `reports_position` 是 `False` 时使用 。 |
| `is_opening` | `bool \| None` | `None` | 阀门是否打开 |
| `is_closing` | `bool \| None` | `None` | 阀门是否关闭 |
| `device_class` | `ValveDeviceClass \| None` | `None` | 什么阀门控制。 见[设备类](/core/entities/valve#device-classes). |

如果您忘记设置 `reports_position`, 而实体没有实体描述, 写入状态会引起错误 。

## 设备类 {#device-classes}

适配时从 `ValveDeviceClass` 设置 [设备类](/glossary/device-class) 。

| 数值 | 说明 |
| ----- | ----------- |
| `WATER` | 阀门控制水流. |
| `GAS` | 阀门控制气流. |

## 支持的特性 {#supported-features}

将 `ValveEntityFeature` 旗帜与 `|` 合并, 设置为 `supported_features`。 见 [支持的特性](/glossary/supported-features) 。

| 数值 | 说明 |
| ----- | ----------- |
| `OPEN` | 阀门可以打开。 执行`open_valve`。 |
| `CLOSE` | 阀门可以关闭。 执行`close_valve`。 |
| `SET_POSITION` | 阀门可以移动到一个位置. 执行`set_valve_position`。 |
| `STOP` | 阀门在移动时可以停止. 执行`stop_valve`。 |

## 方法 {#methods}

执行岔或每种方法的同步变体,而不是两者。

| 就在那时 | Async 变体 | 特性 |
| ------ | ------------- | ------- |
| `open_valve()` | `async_open_valve` | `OPEN` |
| `close_valve()` | `async_close_valve` | `CLOSE` |
| `set_valve_position(position: int)` | `async_set_valve_position` | `SET_POSITION` |
| `stop_valve()` | `async_stop_valve` | `STOP` |

配置 `SET_POSITION` 的阀门不需要 `open_valve` 和 `close_valve` : 打开和关闭的动作, 然后用 100 和 0 调用 `set_valve_position` 。 仍然设置 `OPEN` 和 `CLOSE` , 动作只能使用这些旗帜 。 摇摆是为你处理的。 它在支持`STOP`时会停止移动阀门,打开一个封闭阀门,否则会从最后一个方向向另一方向移动.

## 状态 {#states}

州为`ValveState`. 一个移动的阀门报告`opening`或`closing`,来自`is_opening`和`is_closing`。 否则状态为翎(`closed`或`open`),从位置(0是关闭的)到`reports_position`是`True`,或者从`is_closed`是`False`.

| 数值 | 说明 |
| ----- | ----------- |
| `ValveState.OPENING` | 阀门打开了 |
| `ValveState.CLOSING` | 阀门关闭了 |
| `ValveState.CLOSED` | 阀门关闭了 |
| `ValveState.OPEN` | 阀门是开放的,全部或部分。 |

当它所依赖的值是`None`时,状态是`unknown`.

## 示例 {#example}

```python
from homeassistant.components.valve import (
    ValveDeviceClass,
    ValveEntity,
    ValveEntityFeature,
)

class MyWaterValve(ValveEntity):
    """A water shutoff valve that only opens and closes."""

    _attr_has_entity_name = True
    _attr_name = None
    _attr_device_class = ValveDeviceClass.WATER
    _attr_reports_position = False
    _attr_supported_features = (
        ValveEntityFeature.OPEN | ValveEntityFeature.CLOSE
    )

    def __init__(self, device: MyDevice) -> None:
        """Set up the valve."""
        self._device = device
        self._attr_unique_id = device.serial

    @property
    def is_closed(self) -> bool:
        """Return if the valve is closed."""
        return not self._device.is_open

    async def async_open_valve(self) -> None:
        """Open the valve."""
        await self._device.open()

    async def async_close_valve(self) -> None:
        """Close the valve."""
        await self._device.close()
```
