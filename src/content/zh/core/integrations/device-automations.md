---
title: 设备自动化
description: 设备如何触发、条件和行动 目下已有的整合。
sidebarGroup: 集成功能
order: 3
---

# 设备自动化 {#device-automations}

> [!IMPORTANT]
> 目前正在探索设备自动化的替代办法。 现有的设备自动化继续工作,但新设备自动化不被接受. 此页用于维持现存的.

设备自动化让用户围绕一个设备构建自动化,而不知道状态,事件或动作. 他们选择一个设备,然后从一个触发器,条件,和动作的列表中选择,比如"按钮1按下"或"打开灯". 在引擎盖下,他们使用 相同的事件,状态,和行动 与一切。

他们来自两个地方:

- 设备的集成,对于没有绑在实体上的东西,如按键按在远程上(ZHA和deCONZ这样做).
- 实体集成, 对于一些与实体相连的东西, 就像灯光开启。 `light`的整合为每一个光提供了这些.

集成后加入了三个平台文件:`device_trigger.py`,`device_condition.py`,和`device_action.py`. 每个都定义了一个方案,一个列出一个设备所支持的函数,和一个进行工作的函数. 脚手架脚本有全部三个模板:`python3 -m script.scaffold device_trigger`,`device_condition`,或`device_action`.

## 设备触发器 {#device-triggers}

当设备出事时触发火,比如巴士上的事件或状态变化.

```python
import probatio

from homeassistant.components.device_automation import (
    DEVICE_TRIGGER_BASE_SCHEMA,
)
from homeassistant.components.homeassistant.triggers import event
from homeassistant.const import (
    CONF_DEVICE_ID,
    CONF_DOMAIN,
    CONF_PLATFORM,
    CONF_TYPE,
)

TRIGGER_TYPES = {"button_short_press", "button_long_press"}

TRIGGER_SCHEMA = DEVICE_TRIGGER_BASE_SCHEMA.extend(
    {probatio.Required(CONF_TYPE): probatio.In(TRIGGER_TYPES)}
)

async def async_get_triggers(
    hass: HomeAssistant, device_id: str
) -> list[dict[str, Any]]:
    """List the triggers of a device."""
    return [
        {
            CONF_PLATFORM: "device",
            CONF_DOMAIN: DOMAIN,
            CONF_DEVICE_ID: device_id,
            CONF_TYPE: trigger_type,
        }
        for trigger_type in TRIGGER_TYPES
    ]

async def async_attach_trigger(
    hass: HomeAssistant,
    config: ConfigType,
    action: TriggerActionType,
    trigger_info: TriggerInfo,
) -> CALLBACK_TYPE:
    """Attach a trigger to the event of the device."""
    event_config = event.TRIGGER_SCHEMA(
        {
            event.CONF_PLATFORM: "event",
            event.CONF_EVENT_TYPE: f"{DOMAIN}_event",
            event.CONF_EVENT_DATA: {
                CONF_DEVICE_ID: config[CONF_DEVICE_ID],
                CONF_TYPE: config[CONF_TYPE],
            },
        }
    )

    return await event.async_attach_trigger(
        hass, event_config, action, trigger_info, platform_type="device"
    )
```

- `TRIGGER_SCHEMA`验证一个触发器。 定义为模块中的常数, 并为您应用 Home Assistant 。 不要自己应用它。
- `async_get_triggers` 列出一个设备支持的触发器 。 这些是用户可以选择的。
- 使触发点火。 它返回解开它的函数 。

如果静态方案还不够, 请执行 `async_validate_trigger_config(hass, config)` 以动态验证 。

## 设备条件 {#device-conditions}

一个条件检查设备的某样东西,比如是否有灯亮.

- `CONDITION_SCHEMA`:从`homeassistant.helpers.config_validation`延伸`DEVICE_CONDITION_BASE_SCHEMA`。
- `async_get_conditions(hass, device_id)`: 列出设备支持的条件 。
- `async_condition_from_config(hass, config)`迭代:返回检查条件的函数,信守 `bool`。 从事件循环调用一定安全.

执行`async_validate_condition_config(hass, config)`进行动态验证。

## 设备动作 {#device-actions}

一个动作使设备做一些事情,比如打开灯或者重启设备.

- `ACTION_SCHEMA` : 从`homeassistant.helpers.config_validation` 延伸 `DEVICE_ACTION_BASE_SCHEMA` 。 Home Assistant 应用它, 不要自己应用它 。
- `async_get_actions(hass, device_id)`: 列出设备支持的动作 。
- `async_call_action_from_config(hass, config, variables, context)`:执行动作。

执行`async_validate_action_config(hass, config)`进行动态验证。

## 二级设备自动化 {#secondary-device-automations}

具有许多触发器,条件,或动作的设备可以压倒用户. 把不重要的标为次要的 它们仍然可以使用,但可能在其他的后面显示,或者在"显示更多"选项后面显示.

```python
{
    CONF_PLATFORM: "device",
    CONF_DOMAIN: DOMAIN,
    CONF_DEVICE_ID: device_id,
    CONF_TYPE: "button_long_press",
    "metadata": {"secondary": True},
}
```

如果设备自动化指一个具有 `entity_id` 的实体 键,当隐藏该实体时,或有一个 [实体类别](/glossary/entity-category) 时,它自动标记为次要。

## 文本 {#texts}

所见名称用户来自`strings.json`, 在`device_automation`下:

```json
{
  "device_automation": {
    "trigger_type": {
      "button_short_press": "Button pressed",
      "button_long_press": "Button held down"
    },
    "condition_type": {
      "is_on": "{entity_name} is on"
    },
    "action_type": {
      "reboot": "Reboot"
    }
  }
}
```

竞技竞技 竞技竞技 竞技竞技 竞技竞技 竞技竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞技 竞 竞技 竞技 竞技 竞技 竞 竞 竞技 竞技 竞 竞 竞 竞 竞 竞 竞 竞 竞 竞 竞 竞 竞 竞 竞 竞 竞 竞
