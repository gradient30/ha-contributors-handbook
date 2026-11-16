---
title: 割草机实体
description: 为机械割草机建立一个割草机实体,用于割草,暂停,然后返回它的码头.
sidebarLabel: 割草机
sidebarGroup: 应用程序
---

# 割草机实体 {#lawn-mower-entity}

一个割草机实体控制一个机器人割草机:开始割草,暂停,停止,并把它送回它的码头. 从`LawnMowerEntity` 继承到`homeassistant.components.lawn_mower` 。 实体只覆盖这些命令. 剪切高度等设置会在同一设备的其他实体中进行, 例如 [编号](/core/entities/number) 或 [选择](/core/entities/select) 。

前端显示割草机的方式,请参见[剪草机更多信息视图](/design/more-info/lawn-mower).

从 Home Assistant 演示中嵌入的仪表板卡的现场演示。 剪草机开始,暂停,停靠,在瓷砖卡上。 卡片为直播:送出去割草,或回码头.

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
        "entity_id": "lawn_mower.garden",
        "state": "docked",
        "attributes": {
          "friendly_name": "Garden mower",
          "supported_features": 7
        }
      }
    ]
  </script>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "tile",
        "entity": "lawn_mower.garden",
        "features": [
          {
            "type": "lawn-mower-commands"
          }
        ]
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

## 的临时议程 {#properties}

割草机实体在[一般实体属性](/core/entities/entity-class)上方有这种财产。 设定为 `_attr_activity`, 或覆盖属性 。

| 名称 | 类型 | 默认 | 说明 |
| ---- | ---- | ------- | ----------- |
| `activity` | `LawnMowerActivity \| None` | `None` | 割草机现在在做什么。 见[国家](/core/entities/lawn-mower#states). |

## 支持的特性 {#supported-features}

将 `LawnMowerEntityFeature` 的值与位符或 (`|`) 运算符合并 。 Home Assistant 只提供您设定的特性的动作 。

| 数值 | 说明 |
| ----- | ----------- |
| `START_MOWING` | 割草机可以开始或恢复割草. 执行`start_mowing`。 |
| `PAUSE` | . 修剪机可以暂停。 . 执行`pause`。 |
| `STOP` | 割草机可以停止在它的位置。 执行`stop`。 |
| `DOCK` | 割草机可以返回其码头. 执行`dock`。 |

## 方法 {#methods}

每个方法都有同步变体和`async_`变体. 执行其中一项。

| 就在那时 | Async 变体 | 特性 |
| ------ | ------------- | ------- |
| `start_mowing()` | `async_start_mowing()` | `START_MOWING` |
| `pause()` | `async_pause()` | `PAUSE` |
| `stop()` | `async_stop()` | `STOP` |
| `dock()` | `async_dock()` | `DOCK` |

## 状态 {#states}

状态为割草机的`activity`,值为`LawnMowerActivity`. `state` 属性为 final: set `activity` 相反 。

| 数值 | 说明 |
| ----- | ----------- |
| `MOWING` | 割草机在割草头 |
| `PAUSED` | 割草机在割草,停了下来。 |
| `RETURNING` | 割草机正在返回码头的路上. |
| `DOCKED` | 割草机在 真该死 |
| `IDLE` | 割草机停了,但没有停靠,也没有暂停。 |
| `ERROR` | 割草机遇到了问题,需要帮助。 |

## 示例 {#example}

```python
from homeassistant.components.lawn_mower import (
    LawnMowerActivity,
    LawnMowerEntity,
    LawnMowerEntityFeature,
)

class MyLawnMower(MyEntity, LawnMowerEntity):
    """A robot lawn mower."""

    _attr_name = None
    _attr_supported_features = (
        LawnMowerEntityFeature.START_MOWING
        | LawnMowerEntityFeature.PAUSE
        | LawnMowerEntityFeature.DOCK
    )

    def __init__(self, coordinator: MyCoordinator) -> None:
        """Set up the entity."""
        super().__init__(coordinator)
        self._attr_unique_id = coordinator.mower.serial

    @property
    def activity(self) -> LawnMowerActivity:
        """Return what the mower is doing."""
        if self.coordinator.data.error:
            return LawnMowerActivity.ERROR
        if self.coordinator.data.mowing:
            return LawnMowerActivity.MOWING
        if self.coordinator.data.charging:
            return LawnMowerActivity.DOCKED
        return LawnMowerActivity.IDLE

    async def async_start_mowing(self) -> None:
        """Start mowing."""
        await self.coordinator.mower.start()
        await self.coordinator.async_request_refresh()

    async def async_pause(self) -> None:
        """Pause mowing."""
        await self.coordinator.mower.pause()
        await self.coordinator.async_request_refresh()

    async def async_dock(self) -> None:
        """Send the mower back to its dock."""
        await self.coordinator.mower.dock()
        await self.coordinator.async_request_refresh()
```

`MyEntity` 是集成的共享基础实体, 一个 `CoordinatorEntity` 设置 `_attr_has_entity_name = True` 和设备信息 。
