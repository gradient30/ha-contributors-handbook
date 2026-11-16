---
title: 二进制传感器实体
description: 报告什么是打开或关闭, 像一个打开的门或被探测到的运动。
sidebarLabel: 二
sidebarGroup: 传感器与状态
---

# 二进制传感器实体 {#binary-sensor-entity}

二进制传感器报告两个状态中的一个:上或下。 何谓上下行取决于其装置等级:一扇门打开或关闭,烟雾探测器看到烟雾或清晰,电池低或正常. 从`BinarySensorEntity`继承,从`homeassistant.components.binary_sensor`导入。

使用二进制传感器,当值完全有两个状态且用户无法更改时. 如果用户可以打开和关闭,请使用[切换](/core/entities/switch). 如果它有两个以上状态,请使用 [传感器](/core/entities/sensor) 与 `enum` 设备类 。

从 Home Assistant 演示中嵌入的仪表板卡的现场演示。 一个打开的门感应器和一个关闭的移动感应器,在瓷砖卡片中. 设备类打开并关闭为 Open and Clear.

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
        "entity_id": "binary_sensor.front_door",
        "state": "on",
        "attributes": {
          "friendly_name": "Front door",
          "device_class": "door"
        }
      },
      {
        "entity_id": "binary_sensor.hallway_motion",
        "state": "off",
        "attributes": {
          "friendly_name": "Hallway motion",
          "device_class": "motion"
        }
      }
    ]
  </script>
  <ha-embed-card style="grid-column: span 6">
    <script type="application/json">
      {
        "type": "tile",
        "entity": "binary_sensor.front_door",
        "grid_options": {
          "columns": 6
        }
      }
    </script>
  </ha-embed-card>
  <ha-embed-card style="grid-column: span 6">
    <script type="application/json">
      {
        "type": "tile",
        "entity": "binary_sensor.hallway_motion",
        "grid_options": {
          "columns": 6
        }
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

## 的临时议程 {#properties}

| 名称 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- |
| `is_on` | `bool \| None` | 要求数 | 二进制传感器是否打开 。 `None`表示状态未知. |
| `device_class` | `BinarySensorDeviceClass \| None` | `None` | 二进制传感器能探测到什么 见[设备类](/core/entities/binary-sensor#device-classes). |

每个实体的通用属性,如`name`或`available`,都在[实体类别](/core/entities/entity-class)上。

一个二进制传感器永远不能有 `config` [实体类别](/glossary/entity-category): Home Assistant 拒绝添加它 。

## 支持的特性 {#supported-features}

该实体没有支持的特性。

## 设备类 {#device-classes}

[设备类](/glossary/device-class) 改变前端的显示方式 。 一个具有设备类的二进制传感器,没有名称以其设备类命名. 见[名称](/core/entities/naming)。 值列是您在 YAML 中设置的值, 例如 `device_class` 的 [MQTT 二进制传感器](https://www.home-assistant.io/integrations/binary_sensor.mqtt/) 或 [出版物](https://www.home-assistant.io/integrations/template/) 的 `device_class` 。

| 设备类 | 数值 | 关于手段 | 关闭表示 |
| --- | --- | --- | --- |
| `BATTERY` | `battery` | 低级 | 常规 |
| `BATTERY_CHARGING` | `battery_charging` | 充电 | 不收费 |
| `CO` | `carbon_monoxide` | 检测到一氧化碳 | 清除 |
| `COLD` | `cold` | 凉 | 常规 |
| `CONNECTIVITY` | `connectivity` | 已连接 | 断开连接 |
| `DOOR` | `door` | 打开 | 关闭 |
| `GARAGE_DOOR` | `garage_door` | 打开 | 关闭 |
| `GAS` | `gas` | 检测气体 | 清除 |
| `GLASS_BREAK` | `glass_break` | 检测到玻璃断层 | 清除 |
| `HEAT` | `heat` | 热 | 常规 |
| `LIGHT` | `light` | 检测光 | 无光 |
| `LOCK` | `lock` | 解锁 | 已锁定 |
| `MOISTURE` | `moisture` | 湿 | 干燥 |
| `MOTION` | `motion` | 检测到动议 | 清除 |
| `MOVING` | `moving` | 移动 | 已停止 |
| `OCCUPANCY` | `occupancy` | 占用 | 清除 |
| `OPENING` | `opening` | 打开 | 关闭 |
| `PLUG` | `plug` | 插进去了 | 无插件 |
| `POWER` | `power` | 检测功率 | 没有权力 |
| `PRESENCE` | `presence` | ư毗卢遮那 | 走开 |
| `PROBLEM` | `problem` | 发现的问题 | OK |
| `RUNNING` | `running` | 运行 | 未 baconn 运行 |
| `SAFETY` | `safety` | 不安全 | 保险 |
| `SMOKE` | `smoke` | 检测到的烟雾 | 清除 |
| `SOUND` | `sound` | 检测到声音 | 清除 |
| `TAMPER` | `tamper` | 检测到打探 | 清除 |
| `UPDATE` | `update` | 可更新 | 的国家之一 |
| `VIBRATION` | `vibration` | 检测到震动 | 无振动 |
| `WINDOW` | `window` | 打开 | 关闭 |

设备类在 `BinarySensorDeviceClass` , [`homeassistant/components/binary_sensor/const.py`](https://github.com/home-assistant/core/blob/dev/homeassistant/components/binary_sensor/const.py) 中 。

避开 `UPDATE` 设备类 。 要报告是否有新的固件或软件,请使用 [更新实体](/core/entities/update) 。

## 方法 {#methods}

一个二进制传感器没有动作,所以除了保持`is_on`的电流外,没有什么可以执行的. 在 `update` 或 `async_update` 中获取数据, 或用 `async_write_ha_state` 推动 。 见[更新状态](/core/entities/state-updates).

## 状态 {#states}

在此基类中, 状态由 `is_on` 设置 : `on` 用于 `True` , `off` 用于 `False` , `unknown` 用于 `None` 。 不要设定 `state` 自己 。

## 示例 {#example}

接收设备推速更新的运动探测器 :

```python
from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
)

class ExampleMotionSensor(BinarySensorEntity):
    """Motion detector of an example device."""

    _attr_has_entity_name = True
    _attr_device_class = BinarySensorDeviceClass.MOTION
    _attr_should_poll = False

    def __init__(self, device: ExampleDevice) -> None:
        """Initialize the binary sensor."""
        self._device = device
        self._attr_unique_id = f"{device.serial}_motion"

    async def async_added_to_hass(self) -> None:
        """Subscribe to motion updates."""
        self.async_on_remove(
            self._device.subscribe_motion(self._handle_motion)
        )

    def _handle_motion(self, detected: bool) -> None:
        """Handle a motion update from the device."""
        self._attr_is_on = detected
        self.async_write_ha_state()
```

该实体没有名称,因此以其设备类命名:"运动".
