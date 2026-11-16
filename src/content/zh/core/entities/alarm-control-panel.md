---
title: 警报控制面板实体
description: 建立一个警报控制面板实体,武装、解除和触发一个安全系统。
sidebarLabel: 警报控制面板
sidebarGroup: 开合与安防
---

# 警报控制面板实体 {#alarm-control-panel-entity}

一个警报控制面板实体控制一个安全系统:它以一个或多个模式武装系统,解除它,并且可以触发警报. 它可以要求一个代码。 从`AlarmControlPanelEntity` 继承到`homeassistant.components.alarm_control_panel` 。

系统的传感器,如门接触器与社会运动探测器一样,是[二进制传感器](/core/entities/binary-sensor). 属于系统的警报器是 [警报](/core/entities/siren) 。

前端如何显示提醒控制面板, 请参见 [提醒控制面板更多信息视图](/design/more-info/alarm-control-panel) 。

从 Home Assistant 演示中嵌入的仪表板卡的现场演示。 一个警报控制面板,用瓷砖卡和警报面板 武装回家,离开,晚上。 牌是直播的:手臂或解除其中之一。

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
        "entity_id": "alarm_control_panel.home_alarm",
        "state": "disarmed",
        "attributes": {
          "friendly_name": "Home alarm",
          "code_arm_required": false,
          "supported_features": 15
        }
      }
    ]
  </script>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "tile",
        "entity": "alarm_control_panel.home_alarm",
        "features": [
          {
            "type": "alarm-modes"
          }
        ]
      }
    </script>
  </ha-embed-card>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "alarm-panel",
        "entity": "alarm_control_panel.home_alarm"
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

## 的临时议程 {#properties}

提醒控制面板实体在 [一般实体属性](/core/entities/entity-class) 上方有这些属性 。 每个属性都可以以其`_attr_`属性设定,如`_attr_alarm_state`.

| 名称 | 类型 | 默认 | 说明 |
| ---- | ---- | ------- | ----------- |
| `alarm_state` | `AlarmControlPanelState \| None` | 要求数 | 警报状态 见[国家](/core/entities/alarm-control-panel#states). |
| `code_format` | `CodeFormat \| None` | `None` | 面板要求的代码类型 : `CodeFormat.NUMBER` 或 `CodeFormat.TEXT`. `None` 表示没有代码 。 |
| `code_arm_required` | `bool` | `True` | 武装是否需要代码 。 解除武装总是通过 代码,当有一个。 |
| `changed_by` | `str \| None` | `None` | 是谁或者什么改变了最后的警报。 |

`code_format` 告诉要显示的前端键盘: `NUMBER` 的数字垫, `TEXT` 的文本字段 。

## 代码 {#codes}

您的方法收到代码为 `code` 参数, 或者当没有时为 `None` 。 用户可以在实体设置中存储默认代码. 当一个解除或武装动作没有代码时,Home Assistant使用默认代码. 触发动作不会: `alarm_trigger` 只能从动作中获得代码 。 它从 [实体登记选项](/core/entities/registry) 为您读取设置 。

当 `code_arm_required` 是 `True` 而一个臂动作没有代码也没有默认代码时, Home Assistant 在它叫你之前, 会产生一个验证错误 。 设定 `code_arm_required` 到 `False` 当面板挂上没有代码时 。

## 支持的特性 {#supported-features}

将 `AlarmControlPanelEntityFeature` 旗帜与 `|` 合并, 设置为 `supported_features`。 见 [支持的特性](/glossary/supported-features) 。 解除武装总是可以的。

| 数值 | 说明 |
| ----- | ----------- |
| `ARM_HOME` | 警报器可以在家庭模式中解除. 执行`alarm_arm_home`。 |
| `ARM_AWAY` | 警报可以隐蔽 执行 . |
| `ARM_NIGHT` | 警报器可以在夜间模式下解除. 执行`alarm_arm_night`。 |
| `ARM_VACATION` | 警报器可以在休假模式下解除. 执行`alarm_arm_vacation`。 |
| `ARM_CUSTOM_BYPASS` | 注意, 注意, 注意  Implement  Implement } |
| `TRIGGER` | 提醒可以从 Home Assistant 触发 。 执行`alarm_trigger`。 |

## 方法 {#methods}

执行每种方法的同步或同步变体,而不是两者。 每一种方法都需要`code: str | None = None`。

| 就在那时 | Async 变体 | 特性 |
| ------ | ------------- | ------- |
| `alarm_disarm` | `async_alarm_disarm` | 总是 |
| `alarm_arm_home` | `async_alarm_arm_home` | `ARM_HOME` |
| `alarm_arm_away` | `async_alarm_arm_away` | `ARM_AWAY` |
| `alarm_arm_night` | `async_alarm_arm_night` | `ARM_NIGHT` |
| `alarm_arm_vacation` | `async_alarm_arm_vacation` | `ARM_VACATION` |
| `alarm_arm_custom_bypass` | `async_alarm_arm_custom_bypass` | `ARM_CUSTOM_BYPASS` |
| `alarm_trigger` | `async_alarm_trigger` | `TRIGGER` |

## 状态 {#states}

状态是`alarm_state`的值,来自`AlarmControlPanelState`enum. 当`alarm_state`是`None`时,状态是`unknown`.

| 数值 | 说明 |
| ----- | ----------- |
| `DISARMED` | 警报解除了 |
| `ARMED_HOME` | 警报器以家用模式布置. |
| `ARMED_AWAY` | 警报器装在离线模式下 |
| `ARMED_NIGHT` | 警报器以夜间模式布置. |
| `ARMED_VACATION` | 警报器装在度假模式下 |
| `ARMED_CUSTOM_BYPASS` | 警报器装有一个或多个区域或传感器绕过,其组合与家、离家或夜晚不匹配。 不要用它来信号断开、断裂或电池低的传感器。 报告那些有自己传感器实体的人 |
| `PENDING` | 警报即将启动 让你有时间解除它 |
| `ARMING` | 警报正在解除,通常在退出延迟期间。 |
| `DISARMING` | 不间断警报解除了 |
| `TRIGGERED` | 警报启动 |

## 示例 {#example}

```python
from homeassistant.components.alarm_control_panel import (
    AlarmControlPanelEntity,
    AlarmControlPanelEntityFeature,
    AlarmControlPanelState,
    CodeFormat,
)

class MyAlarm(AlarmControlPanelEntity):
    """An alarm panel that arms home and away."""

    _attr_has_entity_name = True
    _attr_name = None
    _attr_code_format = CodeFormat.NUMBER
    _attr_supported_features = (
        AlarmControlPanelEntityFeature.ARM_HOME
        | AlarmControlPanelEntityFeature.ARM_AWAY
    )

    def __init__(self, panel: MyPanel) -> None:
        """Set up the alarm panel."""
        self._panel = panel
        self._attr_unique_id = panel.serial

    @property
    def alarm_state(self) -> AlarmControlPanelState:
        """Return the state of the alarm."""
        return AlarmControlPanelState(self._panel.state)

    async def async_alarm_disarm(self, code: str | None = None) -> None:
        """Disarm the alarm."""
        await self._panel.disarm(code)

    async def async_alarm_arm_home(self, code: str | None = None) -> None:
        """Arm the alarm in home mode."""
        await self._panel.arm("home", code)

    async def async_alarm_arm_away(self, code: str | None = None) -> None:
        """Arm the alarm in away mode."""
        await self._panel.arm("away", code)
```
