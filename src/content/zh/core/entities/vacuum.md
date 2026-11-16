---
title: 真空实体
description: 为机器人真空建立真空实体,可以进行清洁,停靠,并可以清理家庭的特定区域.
sidebarLabel: 真空
sidebarGroup: 家电
---

# 真空实体 {#vacuum-entity}

一个真空实体控制一个机器人真空清除器:开始和暂停清洁,送回它的码头,在机器人支持它的地方,设置吸力,找到它,或者清理特定的房间. 从`StateVacuumEntity` 继承到`homeassistant.components.vacuum` 。 机器人拖把和组合式真空和拖把机器人使用同一个实体.

前端如何显示真空,请参见[真空多信息视图](/design/more-info/vacuum).

从 Home Assistant 演示中嵌入的仪表板卡的现场演示。 一个机器人真空,它开始,暂停,停止,返回到它的不偏不倚的码头,并且有风扇速度,在瓷砖卡中. 卡片为直播:开始打扫,或改变风扇速度.

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
        "entity_id": "vacuum.downstairs",
        "state": "docked",
        "attributes": {
          "friendly_name": "Downstairs vacuum",
          "fan_speed_list": [
            "quiet",
            "standard",
            "max"
          ],
          "fan_speed": "standard",
          "supported_features": 12348
        }
      }
    ]
  </script>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "tile",
        "entity": "vacuum.downstairs",
        "features": [
          {
            "type": "vacuum-commands"
          },
          {
            "type": "vacuum-fan-speed"
          }
        ]
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

## 的临时议程 {#properties}

真空实体在 [一般实体属性](/core/entities/entity-class) 之上有这些属性 。 每个属性都可以以其`_attr_`属性设定,如`_attr_activity`.

| 名称 | 类型 | 默认 | 说明 |
| ---- | ---- | ------- | ----------- |
| `activity` | `VacuumActivity \| None` | `None` | 真空现在在做什么。 见[国家](/core/entities/vacuum#states). |
| `fan_speed` | `str \| None` | `None` | 目前风扇速度. 需要 `VacuumEntityFeature.FAN_SPEED` 。 |
| `fan_speed_list` | `list[str]` | 需要使用 `FAN_SPEED` | 楠风加速真空支撑. |

较老的真空实体报告了电池级别和状态文本。 这些属性已经消失: 将电池暴露为 [传感器](/core/entities/sensor) 设备类的 `battery`, 以及错误或详细状态的 单独传感器 或 [事件](/core/entities/event) 。

## 支持的特性 {#supported-features}

将 `VacuumEntityFeature` 的值与位符或 (`|`) 运算符合并 。 Home Assistant 只提供您设定的特性的动作 。

| 数值 | 说明 |
| ----- | ----------- |
| `STATE` | 真空报告它的活动。 放在每个真空实体上 |
| `START` | 真空可以开始或恢复清洁. 执行`start`。 |
| `PAUSE` | 真空能暂停清扫. 执行`pause`。 |
| `STOP` | 真空能止其处. 执行`stop`。 |
| `RETURN_HOME` | 真空可以返回它的码头。 执行`return_to_base`。 |
| `FAN_SPEED` | 真空有扇速. 执行`set_fan_speed`并提供`fan_speed`和`fan_speed_list`。 |
| `LOCATE` | 真空可以让自己知道,通常用声音. 执行`locate`。 |
| `CLEAN_SPOT` | 真空可以清理它所在的位置。 执行`clean_spot`。 |
| `CLEAN_AREA` | 真空可以清理特定区域. 执行`async_get_segments`和`clean_segments`。见[清洁区](/core/entities/vacuum#cleaning-areas)。 |
| `SEND_COMMAND` | 真空接受原始命令. 执行`send_command`。 |
| `MAP` | 真空有图. Home Assistant没有方法,所以这面旗帜只是信息. |

`TURN_ON`, `TURN_OFF`和`STATUS` 都已经贬值了, 并且没有为`StateVacuumEntity`做什么。

宁可在 `SEND_COMMAND` 上进行专门整合行动 。 `vacuum.send_command` 动作采用免费的形式输入, 这很难使用, 无法很好地记录 。

## 清洁区 {#cleaning-areas}

使用`CLEAN_AREA`,用户可以告诉真空来清理Home Assistant[区域](/glossary/area),就像厨房,而不是制造商的应用软件中的房间. 机器人知道自己的房间,叫这里的部分。 用户在实体设置中将区域映射到分区一次, 在实体注册选项中存储 Home Assistant 。

你该做的是:

- `async_get_segments()` 返回机器人知道的分区, 作为 `Segment(id, name, group)` 的列表 。 `id`必须是实体内独有的。 `group` 映射对话框中只有分组块, 如每层或每张映射 。 Home Assistant当用户打开映射时调用它,所以返回新鲜数据.
- `clean_segments(segment_ids)` 或 `async_clean_segments(segment_ids)` 清除给定的片段 。 Home Assistant从 `vacuum.clean_area` 动作中调用它, 在它将区域翻译为片段之后 。

机器人更换地图:新房间出现,两个房间合并. 为了抓住这一点,将机器人现在的报告内容与`last_seen_segments`进行比较,即用户上次保存映射时存在的片段. 出现分歧时,请拨`async_create_segments_issue()`. 创建 [修理](/glossary/repair) 请用户更新映射 。 `last_seen_segments` 是 `None` , 直到保存一个映射; 不要提出问题 。

## 方法 {#methods}

每个方法都有同步变体和`async_`变体. 执行其中之一, 取决于您的库是屏蔽还是同步 。

| 就在那时 | Async 变体 | 特性 |
| ------ | ------------- | ------- |
| `start()` | `async_start()` | `START` |
| `pause()` | `async_pause()` | `PAUSE` |
| `stop(**kwargs)` | `async_stop(**kwargs)` | `STOP` |
| `return_to_base(**kwargs)` | `async_return_to_base(**kwargs)` | `RETURN_HOME` |
| `set_fan_speed(fan_speed, **kwargs)` | `async_set_fan_speed(fan_speed, **kwargs)` | `FAN_SPEED` |
| `locate(**kwargs)` | `async_locate(**kwargs)` | `LOCATE` |
| `clean_spot(**kwargs)` | `async_clean_spot(**kwargs)` | `CLEAN_SPOT` |
| `clean_segments(segment_ids, **kwargs)` | `async_clean_segments(segment_ids, **kwargs)` | `CLEAN_AREA` |
| | `async_get_segments()` | `CLEAN_AREA` |
| `send_command(command, params, **kwargs)` | `async_send_command(command, params, **kwargs)` | `SEND_COMMAND` |

## 状态 {#states}

状态是真空的`activity`,值为`VacuumActivity`. `state` 属性为 final: set `activity` 相反 。

| 数值 | 说明 |
| ----- | ----------- |
| `CLEANING` | 真空清净. |
| `DOCKED` | 真空在它的码头。 道克通常也意味着充电. |
| `IDLE` | 真空不清洁,不暂停,不停靠,无差错. |
| `PAUSED` | 真空在清理,被暂停,没有返回码头。 |
| `RETURNING` | 真空正在返回码头途中. |
| `ERROR` | 真空遇到了问题,需要帮助。 |

## 示例 {#example}

```python
from typing import Any

from homeassistant.components.vacuum import (
    StateVacuumEntity,
    VacuumActivity,
    VacuumEntityFeature,
)

ACTIVITIES = {
    "cleaning": VacuumActivity.CLEANING,
    "charging": VacuumActivity.DOCKED,
    "paused": VacuumActivity.PAUSED,
    "returning": VacuumActivity.RETURNING,
}

class MyVacuum(MyEntity, StateVacuumEntity):
    """A robot vacuum."""

    _attr_name = None
    _attr_fan_speed_list = ["quiet", "standard", "max"]
    _attr_supported_features = (
        VacuumEntityFeature.STATE
        | VacuumEntityFeature.START
        | VacuumEntityFeature.PAUSE
        | VacuumEntityFeature.RETURN_HOME
        | VacuumEntityFeature.FAN_SPEED
    )

    def __init__(self, coordinator: MyCoordinator) -> None:
        """Set up the entity."""
        super().__init__(coordinator)
        self._attr_unique_id = coordinator.robot.serial

    @property
    def activity(self) -> VacuumActivity:
        """Return what the robot is doing."""
        return ACTIVITIES.get(
            self.coordinator.data.status, VacuumActivity.IDLE
        )

    @property
    def fan_speed(self) -> str:
        """Return the current fan speed."""
        return self.coordinator.data.fan_speed

    async def async_start(self) -> None:
        """Start or resume cleaning."""
        await self.coordinator.robot.start()
        await self.coordinator.async_request_refresh()

    async def async_pause(self) -> None:
        """Pause cleaning."""
        await self.coordinator.robot.pause()
        await self.coordinator.async_request_refresh()

    async def async_return_to_base(self, **kwargs: Any) -> None:
        """Send the robot back to its dock."""
        await self.coordinator.robot.dock()
        await self.coordinator.async_request_refresh()

    async def async_set_fan_speed(
        self, fan_speed: str, **kwargs: Any
    ) -> None:
        """Set the fan speed."""
        await self.coordinator.robot.set_fan_speed(fan_speed)
        await self.coordinator.async_request_refresh()
```

`MyEntity` 是集成的共享基础实体, 一个 `CoordinatorEntity` 设置 `_attr_has_entity_name = True` 和设备信息 。
