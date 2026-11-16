---
title: 意图
description: 什么是意图,一个集成是如何处理意图的,以及如何从代码或HTTP上发射一个.
sidebarGroup: 语音和AI
order: 50
---

# 意图 {#intents}

An [意图](/glossary/intent) 描述某人想要的东西, 和他们怎么说的分开. "打开厨房的灯","厨房的灯",以及一个语音助理的按钮都变成了相同的意图: `HassTurnOn`,其中的插槽 `area`设定到厨房,`domain`设定到灯光.

分裂才是重点。 理解用户(Assist,大型语言模型,或外部语音助理)的事物产生意向. 做它的东西, 一个意图处理者, 不在乎它来自哪里。 写一个处理器一次,它从每个来源都起作用。

In Home Assistant:

- `conversation` 整合将文本变成意图, 并用 [意图存储器](https://github.com/OHF-Voice/intents) 的句子 。 见[对话框 API](/core/internals/conversation-api)。
- [LLM API 语言](/core/internals/llm-api)为大语言模型提供了作为工具的意向. 并非每一种意图:一体化选择其意图提供哪一种。
- `intent` 集成注册 [内置意图](/core/internals/built-in-intents) 并提供一个 HTTP 端点来发射它们 。 它被装入`conversation`,这是默认配置的一部分.
- 任何整合都可以为自己的意向登记处理者.

## 意图对象 {#the-intent-object}

`Intent`从`homeassistant.helpers.intent`持有 :

| 属性 | 说明 |
| --- | --- |
| `hass` | Home Assistant实例。 |
| `platform` | 释放意图的融合 |
| `intent_type` | 意图的名称,如`HassTurnOn`. |
| `slots` | 槽值,按槽名排列. 每个槽是一个字典,有一个`value`. |
| `text_input` | 导致这一意图的文本,如果有的话。 |
| `context` | `Context`,与用户。 |
| `language` | 默认为实例语言的语言。 |
| `assistant` | 处理请求的助手, 如`conversation` 。 曾经只行动于接触它的实体. |
| `device_id` | 请求的装置,就像一个语音卫星 |
| `satellite_id` | 请求来自卫星的实体身份。 |
| `conversation_agent_id` | 处理请求的谈话代理人 |

## 处理一个意图 {#handle-an-intent}

子类 `IntentHandler` 用 `intent.async_register` 注册一个实例 。 有意的集成通常在一个`intent.py`平台中进行,其中的函数为`async_setup_intents`,而`intent`集成称为:

```python
import probatio

from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_validation as cv, intent

INTENT_ADD_COFFEE = "MyIntegrationAddCoffee"

async def async_setup_intents(hass: HomeAssistant) -> None:
    """Set up the intents of my integration."""
    intent.async_register(hass, AddCoffeeHandler())

class AddCoffeeHandler(intent.IntentHandler):
    """Count how much coffee was had."""

    intent_type = INTENT_ADD_COFFEE
    description = "Adds cups to today's coffee count"
    slot_schema = {probatio.Optional("cups"): cv.positive_int}

    async def async_handle(
        self, intent_obj: intent.Intent
    ) -> intent.IntentResponse:
        """Handle the intent."""
        slots = self.async_validate_slots(intent_obj.slots)
        cups = slots.get("cups", {}).get("value", 1)
        total = await async_add_coffee(intent_obj.hass, cups)

        response = intent_obj.create_response()
        response.async_set_speech(f"That is {total} cups today.")
        return response
```

- `intent_type`是这个名字。 预先设定自己避免冲突的意图. 从`Hass`开始的名字属于Home Assistant.
- 解释意图 当意图被作为工具提供给语言模型时,他们会阅读它,所以为他们写作.
- `slot_schema`描述槽。 验证它们,并在它们不适合时加价。
- `platforms`可选择的限制 整合可能释放意图。

您在操作器中设置的语句是像现在这样,很快就会被翻译。 内置的意向从意向寄存器中,从每种语言中,得到他们的响应句.

对于需要针对匹配实体采取行动的普通意图,`ServiceIntentHandler`从`homeassistant.helpers.intent`开始为您进行匹配,调用和响应.

### 回应 {#the-response}

`intent_obj.create_response()` 返回 `IntentResponse` :

- `async_set_speech(text)`:该说什么回来。 默认的纯文本, 或 SSML 为 `speech_type="ssml"` 。
- `async_set_reprompt(text)`:如果用户没有及时回答,对于一个提问的答复,该怎么说.
- `async_set_card(title, content)`:一个可以显示一个的助手的卡片.
- `async_set_results(success_results, failed_results)`: 被作为`IntentResponseTarget`对象采取行动的目标 。
- `async_set_error(code, message)`: 将响应变成错误 。
- `response_type`: `IntentResponseType.ACTION_DONE`默认。 设定为 `QUERY_ANSWER` 以回答一个问题 。

当意图无法处理时, 将 `intent.IntentHandleError` 提升, 并为用户发送消息 。

## 开枪是故意的 {#fire-an-intent}

如果您的代码能理解用户本身, 就像外部语音助理的集成, 请 Home Assistant 处理结果 :

```python
from homeassistant.helpers import intent

try:
    response = await intent.async_handle(
        hass,
        DOMAIN,
        intent.INTENT_TURN_ON,
        {"name": {"value": "Kitchen light"}},
        context=context,
        language="en",
    )
except intent.UnknownIntent:
    _LOGGER.warning("Unknown intent")
except intent.InvalidSlotInfo as err:
    _LOGGER.error("Invalid slot data: %s", err)
except intent.IntentError:
    _LOGGER.exception("Error handling the intent")
```

由你把回复带回给用户。 `response.speech`按类型举行演讲,如`response.speech["plain"]["speech"]`. `response.as_dict()`给出整个响应,形状与[对话框 API](/core/internals/conversation-api#the-response)相同.

### 超过 H才可以 {#over-http}

`intent` 集成提供 `POST /api/intent/handle`, 意为 `name` 及其在 `data` 中的位值 :

```json
{
  "name": "HassTurnOn",
  "data": {
    "name": "Kitchen light"
  }
}
```

可选字段为`language`,`assistant`,`device_id`和`satellite_id`。 反应是作为JSON的意向反应.

要一切顺利, 请 Home Assistant 确定意图, 请使用 [对话框 API](/core/internals/conversation-api) 。
