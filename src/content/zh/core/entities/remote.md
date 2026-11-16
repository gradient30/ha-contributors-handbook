---
title: 远程实体
description: 将命令发送到其他设备,比如通用遥控器上的按钮,并在活动间切换.
sidebarLabel: 远程
sidebarGroup: 遥控与信号
---

# 远程实体 {#remote-entity}

远程实体向设备发送命令,即远程控制上按钮的方式. 它可以是物理遥控器或中枢器,如爆红外线密码的通用遥控器,也可以是虚拟遥控器,通过网络向电视或设置顶盒说话. 在单指令之上,一个远程可以知道活动:一个"Watch TV"宏,打开电视和接收器,并选择正确的输入.

从`RemoteEntity`继承,从`homeassistant.components.remote`导入。 它以`ToggleEntity`为基础,所以它有类似[切换](/core/entities/switch)的状态。 当用户想要发送任意命名命令时使用远程实体 。 如果只传送原始信号供其他集成使用,请查看[倡仪](/core/entities/infrared)和[无线电频率](/core/entities/radio-frequency)实体。

## 的临时议程 {#properties}

这些属性是远程实体特有的. 每个实体的通用属性都在 [实体类别](/core/entities/entity-class) 上 。

| 名称 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- |
| `is_on` | `bool \| None` | `None` | 日在遥控器或控制设备上 日在 `None` 表示未知 。 |
| `current_activity` | `str \| None` | `None` | 现在正在展开的活动。 |
| `activity_list` | `list[str] \| None` | `None` | 用户可以选择的活动. |
| `supported_features` | `RemoteEntityFeature` | `RemoteEntityFeature(0)` | 此远程支持的特性 。 见下文。 |

`current_activity` 和 `activity_list` 只有在实体支持 `RemoteEntityFeature.ACTIVITY` 时才会在状态属性中结束 。

## 支持的特性 {#supported-features}

将 `RemoteEntityFeature` 的旗帜与位符或 (`|`) 运算符合并 。

| 旗帜 | 说明 |
| --- | --- |
| `LEARN_COMMAND` | 远程可以从另一个远程学习新的指令. 执行`learn_command`。 |
| `DELETE_COMMAND` | 远程可以删除它学到的命令 。 执行`delete_command`。 |
| `ACTIVITY` | 遥控器有活动。 执行`current_activity`和`activity_list`,并在打开时处理`activity`参数。 |

## 活动 {#activities}

一个活动是在远程上预先定义的宏,比如"Watch TV"或"Listen to Music". 开始一个将数个设备同时处于已知状态.

`remote.turn_on`, `remote.turn_off` 和`remote.toggle` 动作可选 `activity` 。 它以 { 在这 `kwargs` 方法中到达 `kwargs.get("activity")` (常数是 `ATTR_ACTIVITY` 在 `homeassistant.components.remote` ) 。 报告使用 `current_activity` 运行的活动, 这样用户就可以在它上看到并自动化 。

## 方法 {#methods}

每种方法都有同步和Aync变体. 执行其中一项。

### 打开、关闭和切换 {#turn-on-turn-off-and-toggle}

```python
class MyRemote(RemoteEntity):
    async def async_turn_on(self, **kwargs: Any) -> None:
        """Turn the remote on, optionally starting an activity."""

    async def async_turn_off(self, **kwargs: Any) -> None:
        """Turn the remote off."""
```

同步变体为`turn_on`和`turn_off`. 切换来自 `ToggleEntity`: 它根据 `is_on`  你应该打开或关闭 。 只有在设备有真正的切换命令时执行 `async_toggle` 。

### 发送命令 {#send-command}

由 `remote.send_command` 动作调用 。 `command` 是命令名列表 。 `kwargs` 持有 `num_repeats` (默认 `1`) 和 `hold_secs` (默认 `0`) , 当用户给出时, `device` 和`delay_secs` 。 当用户退出`delay_secs`时,使用自己的默认值(常数`DEFAULT_DELAY_SECS`是`0.4`).

```python
class MyRemote(RemoteEntity):
    async def async_send_command(
        self, command: Iterable[str], **kwargs: Any
    ) -> None:
        """Send commands to a device."""
```

同步变体为`send_command`.

### 学习命令 {#learn-command}

只为有 `RemoteEntityFeature.LEARN_COMMAND` 的远程 。 由`remote.learn_command`动作调用,可在`kwargs`中通过`device`,`command`,`command_type`,`alternative`和`timeout`.

```python
class MyRemote(RemoteEntity):
    async def async_learn_command(self, **kwargs: Any) -> None:
        """Learn a command from a device."""
```

同步变体为`learn_command`.

### 删除命令 {#delete-command}

只为有 `RemoteEntityFeature.DELETE_COMMAND` 的远程 。 由 `remote.delete_command` 动作调用, 其中 `command` 和 `kwargs` 中的可选 `device` 。

```python
class MyRemote(RemoteEntity):
    async def async_delete_command(self, **kwargs: Any) -> None:
        """Delete a learned command."""
```

同步变体为`delete_command`.

## 状态 {#states}

州从`is_on`.

| 状态 | 何时 |
| --- | --- |
| `on` | `is_on` is `True`. |
| `off` | `is_on` is `False`. |
| `unknown` | `is_on` is `None`. |

## 示例 {#example}

具有活动的媒体枢纽网络远程。

```python
from collections.abc import Iterable
from typing import Any

from homeassistant.components.remote import (
    ATTR_ACTIVITY,
    RemoteEntity,
    RemoteEntityFeature,
)

class MyHubRemote(RemoteEntity):
    """Remote for a media hub."""

    _attr_has_entity_name = True
    _attr_name = None
    _attr_supported_features = RemoteEntityFeature.ACTIVITY

    def __init__(self, hub: MyHub) -> None:
        """Initialize the remote."""
        self._hub = hub
        self._attr_unique_id = hub.serial
        self._attr_activity_list = hub.activities

    @property
    def is_on(self) -> bool:
        """Return if an activity is running."""
        return self._hub.current_activity is not None

    @property
    def current_activity(self) -> str | None:
        """Return the running activity."""
        return self._hub.current_activity

    async def async_turn_on(self, **kwargs: Any) -> None:
        """Start an activity, or the default one."""
        activity = kwargs.get(ATTR_ACTIVITY) or self._hub.default_activity
        await self._hub.start_activity(activity)

    async def async_turn_off(self, **kwargs: Any) -> None:
        """Stop the running activity."""
        await self._hub.power_off()

    async def async_send_command(
        self, command: Iterable[str], **kwargs: Any
    ) -> None:
        """Send one or more commands."""
        for _ in range(kwargs.get("num_repeats", 1)):
            for single_command in command:
                await self._hub.press(single_command)
```
