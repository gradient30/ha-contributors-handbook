---
title: B. 触发因素和条件
description: 以触发和条件平台提供您集成时的自动化触发器和条件,并命名它们以便用户可以预测它们.
sidebarGroup: 集成功能
order: 2
---

# B. 触发因素和条件 {#triggers-and-conditions}

一个集成可以向自动化提供自己的[触发](/glossary/trigger)和[他们是条件](/glossary/condition),比如"灯光开启","燃料变得低",或者"月亮处于阶段". 用户在自动化编辑器中选择,在内置编辑器旁边,并填写您描述的字段. 您在 `trigger.py` 和 `condition.py` 平台中提供 。

> [!IMPORTANT]
> 这个API正在使用中,但它很年轻,仍然经常变化. 今天大多数执行是实体域,如`light`和`lock`,有`fumis`,`moon`和`zwave_js`等少数整合. 在最近发布的版本中,帮助者移动到 [`homeassistant/helpers/trigger/`](https://github.com/home-assistant/core/tree/dev/homeassistant/helpers/trigger) 和[`homeassistant/helpers/condition/`](https://github.com/home-assistant/core/tree/dev/homeassistant/helpers/condition) 包中, 触发跑者获得了新的参数 。 在此之前,请先阅读目前的代码和现有的执行,并期望随修改而来.

寻找每个设备所选的触发器和条件,比如"按钮1按下"?. 这些是[设备自动化](/core/integrations/device-automations),一个不接受新执行的旧机制。

## 用户写的 {#what-users-write}

触发器或条件由您的整合领域及其密钥确定。 在 YAML 中,设置在 `options` 中, 以及它适用于 `target` 中的实体、 设备或区域 :

```yaml
triggers:
  - trigger: light.turned_on
    target:
      area_id: living_room
  - trigger: fumis.fuel_became_low
    options:
      device_id: 0c5ac1d9e3f8a4b2c6d7e8f9a0b1c2d3
conditions:
  - condition: moon.is_phase
    options:
      phase: full_moon
```

## 触发器 {#triggers}

### 触发类 {#the-trigger-class}

触发器从 {H方面也扩展 `Trigger` , 并且执行两种方法 :

- `async_validate_config`:验证配置的类方法. 它得到一个带有触发器的`options`和`target`的字典,并返回已验证的版本.
- `async_attach_runner`:开始听。 每次触发点火时,用触发数据和描述拨打`run_action`. 退回一个停止听话的回话

构造器得到一个 `TriggerConfig`, 带有 `key`, `target` 和 `options` 触发器 。

```python
from typing import override

import probatio

from homeassistant.const import ATTR_DEVICE_ID, CONF_OPTIONS
from homeassistant.core import CALLBACK_TYPE, HomeAssistant, callback
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.dispatcher import async_dispatcher_connect
from homeassistant.helpers.trigger import (
    Trigger,
    TriggerActionRunner,
    TriggerConfig,
    TriggerNotTriggeredReporter,
)
from homeassistant.helpers.typing import ConfigType

from .const import SIGNAL_BUTTON_PRESSED

_CONFIG_SCHEMA = probatio.Schema(
    {
        probatio.Required(CONF_OPTIONS): {
            probatio.Required(ATTR_DEVICE_ID): probatio.All(
                cv.ensure_list, [cv.string]
            ),
        },
    }
)

class ButtonPressedTrigger(Trigger):
    """Trigger when a button on the hub is pressed."""

    @classmethod
    @override
    async def async_validate_config(
        cls, hass: HomeAssistant, config: ConfigType
    ) -> ConfigType:
        """Validate the trigger config."""
        return _CONFIG_SCHEMA(config)

    def __init__(self, hass: HomeAssistant, config: TriggerConfig) -> None:
        """Initialize the trigger."""
        super().__init__(hass, config)
        assert config.options is not None
        self._device_ids: list[str] = config.options[ATTR_DEVICE_ID]

    @override
    async def async_attach_runner(
        self,
        run_action: TriggerActionRunner,
        did_not_trigger: TriggerNotTriggeredReporter | None = None,
    ) -> CALLBACK_TYPE:
        """Start listening for button presses."""

        @callback
        def async_button_pressed(device_id: str) -> None:
            """Run the automation for a watched device."""
            if device_id in self._device_ids:
                run_action({ATTR_DEVICE_ID: device_id}, "button pressed")

        return async_dispatcher_connect(
            self._hass, SIGNAL_BUTTON_PRESSED, async_button_pressed
        )
```

`run_action`的第一个参数被添加到`trigger`变量中,自动化可以在它的动作中使用. 第二个是简要描述发生的事情,在自动化追踪和日志中显示. `run_action` 返回任务, 如果您需要等待动作完成, 您可以等待它 。

`did_not_trigger`是可选的。 触发器可以使用 `NotTriggeredInfo` 来称呼它, 当他们看着一个变化,但决定不开火, 这在跟踪中出现.

### 登记册触发器 {#register-triggers}

从 `async_get_triggers` 在 `trigger.py` 中返回您的触发器, 用它们的密钥键键 。 密钥相对您的域名 : `button_pressed` 成为 `example.button_pressed` 。

```python
TRIGGERS: dict[str, type[Trigger]] = {
    "button_pressed": ButtonPressedTrigger,
}

async def async_get_triggers(
    hass: HomeAssistant,
) -> dict[str, type[Trigger]]:
    """Return the triggers of the Example integration."""
    return TRIGGERS
```

### 描述触发 {#describe-triggers}

`triggers.yaml` 告诉自动编辑器, 触发器的字段是用 `services.yaml` 对 [动作](/core/integrations/actions#describe-actions-in-servicesyaml) 的同样方式。 扳机有`target`,`fields`,或两者兼有. 每个字段都可以有一个`selector`,`required`,`default`,和`example`.

```yaml
button_pressed:
  fields:
    device_id:
      required: true
      selector:
        device:
          filter:
            - integration: example
          multiple: true
```

以 `.` 开头的顶级密钥被忽略, 这样您就可以用它们来锁定多个触发共享的 YAML 锁定 。 无字段的触发符写为 `button_pressed: {}` 。

### 文本和图标 {#text-and-icons}

每个触发器的名称和描述,以及每个字段的名称,在 `strings.json` 下 `triggers` 中 。 见[翻译](/core/integrations/translations#triggers-and-conditions).

```json
{
  "triggers": {
    "button_pressed": {
      "name": "Button pressed",
      "description": "Triggers when one or more buttons are pressed.",
      "fields": {
        "device_id": {
          "name": "Buttons",
          "description": "The buttons to watch."
        }
      }
    }
  }
}
```

每个核心集成的触发器也需要在`icons.json`中有一个图标:

```json
{
  "triggers": {
    "button_pressed": {
      "trigger": "mdi:gesture-tap-button"
    }
  }
}
```

Hassfest 检查这一切: 注册触发的集成需要 `triggers.yaml`, 在核心集成中, 每个集成需要名称, 描述和图标 。

### 基于实体国家的触发器 {#triggers-based-on-entity-states}

实体域提供与其实体状态相适应的触发器. `homeassistant.helpers.trigger` 拥有这些基础课程和工厂, 如`make_entity_target_state_trigger`, 它建立了一个触发器, 当一个实体到达状态时, 发射:

```python
TRIGGERS: dict[str, type[Trigger]] = {
    "turned_off": make_entity_target_state_trigger(DOMAIN, STATE_OFF),
    "turned_on": make_entity_target_state_trigger(DOMAIN, STATE_ON),
}
```

这些触发器为您使用 `target` 处理 `behavior` 和 `for` 。 见[`homeassistant/components/light/trigger.py`](https://github.com/home-assistant/core/blob/dev/homeassistant/components/light/trigger.py)及其`triggers.yaml`的完整示例,包括亮度的数值触发符。

## 条件 {#conditions}

### 条件类 {#the-condition-class}

条件从 `homeassistant.helpers.condition` 延伸 `Condition` 并执行 :

- `async_validate_config`:一种类方法,可以验证配置,比如用于触发器.
- `_async_check`: 返回是否满足条件 。 每次检查情况都叫它,所以保持速度,不要做I/O.

构造器获得一个 `ConditionConfig`, 带有条件的 `options` 和 `target` 。 这个例子,从`moon`集成,测试月球的相位:

```python
from typing import Unpack, cast, override

import probatio

from homeassistant.const import CONF_OPTIONS
from homeassistant.core import HomeAssistant
from homeassistant.helpers.condition import (
    Condition,
    ConditionCheckParams,
    ConditionConfig,
)
from homeassistant.helpers.typing import ConfigType

from .const import CONF_PHASE
from .helpers import MOON_PHASES, moon_phase

_IS_PHASE_SCHEMA = probatio.Schema(
    {
        probatio.Required(CONF_OPTIONS, default=dict): {
            probatio.Required(CONF_PHASE): probatio.In(MOON_PHASES),
        }
    }
)

class IsPhaseCondition(Condition):
    """Test if the moon is in a specific phase."""

    @classmethod
    @override
    async def async_validate_config(
        cls, hass: HomeAssistant, config: ConfigType
    ) -> ConfigType:
        """Validate the condition config."""
        return cast(ConfigType, _IS_PHASE_SCHEMA(config))

    def __init__(self, hass: HomeAssistant, config: ConditionConfig) -> None:
        """Initialize the condition."""
        super().__init__(hass, config)
        assert config.options is not None
        self._phase: str = config.options[CONF_PHASE]

    @override
    def _async_check(self, **kwargs: Unpack[ConditionCheckParams]) -> bool:
        """Check the condition."""
        return moon_phase() == self._phase
```

### 登记和说明情况 {#register-and-describe-conditions}

条件像触发器 从这里:

- 在 `condition.py` 中从 `async_get_conditions` 返回它们, 按下键 。
- 以 `conditions.yaml` 描述它们的字段, 格式与 `triggers.yaml` 相同 。
- 在 `strings.json` 中, 在 `conditions` 下输入他们的姓名和描述 。
- 在 `icons.json` 中, 在 `conditions` 下, 用密钥 `condition` 给每个图标 。

```python
CONDITIONS: dict[str, type[Condition]] = {
    "is_phase": IsPhaseCondition,
}

async def async_get_conditions(
    hass: HomeAssistant,
) -> dict[str, type[Condition]]:
    """Return the conditions of the moon integration."""
    return CONDITIONS
```

```yaml
is_phase:
  fields:
    phase:
      required: true
      selector:
        select:
          translation_key: phase
          options:
            - new_moon
            - full_moon
```

对于实体状态的条件,`homeassistant.helpers.condition`有`make_entity_state_condition`和类似`EntityNumericalConditionBase`的基类. 见[`homeassistant/components/light/condition.py`](https://github.com/home-assistant/core/blob/dev/homeassistant/components/light/condition.py).

## 命名 {#naming}

用户看到许多整合蝎子的触发和条件. 统一的名字让他们猜篱笆 一旦他们知道另一个。

为设备类型选择一个名称,如"灯","锁","媒体播放器",或"气候控制设备",并在所有触发器,条件和动作中使用. 不要混合变体如"vacuum"和"vacuum cleaner".

### 触发名称 {#trigger-names}

瑶族  trigger  trigger  names  names

| 事件类型 | 标题 | 密钥 |
| --- | --- | --- |
| 即时变化 | "灯打开" "门打开" "按钮按" | `turned_on`, `opened`, `pressed` |
| 活动的开始或结束 | "割草机开始割草" "巴特里停止充电" | `started_mowing`, `stopped_charging` |
| 计量 | 拜托了,"变身","蝙蝠关卡" | `level_changed`, `level_crossed_threshold` |
| 检测 | "探测到" "烟雾清除" | `detected`, `cleared` |
| 状态 | "巴特里变低了" "巴特里不再低了" | `became_low`, `no_longer_low` |

- 活动使用"启动"或"停止":"Vacuum cleaned"的声音完成,"Vacuum cleaned"开始清洗"没有.
- 不要用裸体的状态作为头衔,如"巴特里低". 他们读作国家,而不是事件。
- 带设备类型的铅,也用于传感器和区:"输入区",而不是"输入区".
- 描述跟随"一个或一个以上[devices][现在的紧张动词]]时的绊脚石",如"一个或几个灯光打开时的绊脚石".

### 条件名称 {#condition-names}

一个条件测试当前状态,所以其标题为"[Device type] is [state]",如"Light is on"或"Lock is lock". 反之使用"不是",如"媒体播放器没有播放". 对于值,使用"[Device类型][财产]]",如"媒体播放器音量".

- 密钥使用 `is_`, 它将条件与触发器和行动区分开来: `is_on`, `is_not_playing`, `is_hvac_mode`, `is_brightness`. 一个子类型在它的前面,像`blind_is_open`.
- 描述跟随"如果一个或多个[devices]是[状态]的测试",比如"如果一个或多个锁锁是锁的测试". 对于数值:“测试一个或多个[装置]的[财产]。”

### 键 {#keys}

- 密钥为小写 `snake_case`, 并匹配标题的含义 。
- 不要重复域:在`update`域中,使用`became_available`,而不是`update_became_available`.
- 不要使用占位符键, 如 `_` 。
- 在前面插入一个子类型: `awning_opened`, `blind_is_open`.
