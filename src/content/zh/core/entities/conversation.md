---
title: 对话实体
description: 构建一个从 Assist 中获取文本并进行回答的对话代理, 无论后面是否有语言模型 。
sidebarLabel: 来吧
sidebarGroup: 语音和AI
---

# 对话实体 {#conversation-entity}

对话实体是 [对话代理](/glossary/conversation-agent) : 它接收到有人输入或说的内容, 并返回回复 。 Assist 发送文本作为 [输油管](/glossary/assist-pipeline) 的一部分, 前端的 `conversation.process` 动作和聊天也一样 。 从`ConversationEntity`在`homeassistant.components.conversation`中继承。

今天大多数对话实体都包了一个大语言模型(LLM). Home Assistant在它周围进行举重:它把聊天历史保存在聊天日志中,通过LLM API给模型工具来控制家,并将最后的消息变成口头回应. 您的实体在聊天日志和模型的API之间翻译.

## 的临时议程 {#properties}

对话实体在 [一般实体属性](/core/entities/entity-class) 上方有这些属性 。

| 名称 | 类型 | 默认 | 说明 |
| ---- | ---- | ------- | ----------- |
| `supported_languages` | `list[str] \| Literal["*"]` | 要求数 | 代理人所理解的语言. 返回 `"*"` (`MATCH_ALL`) 当它处理任何语言时, 这是 LLM 的常用语言 。 |
| `supports_streaming` | `bool` | `False` | 代理是否流出其响应 。 设定为 `True` 当您用 `async_add_delta_content_stream` 输入聊天日志时, 因此 Assist 可以开始发言 。 |

`supported_languages`没有`_attr_`快捷键:将其作为属性执行 。

## 支持的特性 {#supported-features}

将 `ConversationEntityFeature` 的值与位符或 (`|`) 运算符合并 。

| 数值 | 说明 |
| ----- | ----------- |
| `CONTROL` | 代理可以在Home Assistant中控制设备,通常因为用户给了它访问LLM API的机会. 当在管道中偏爱本地意图时,Assist 然后将一些句子留给你的代理人,而不是在本地处理它们. |

## 聊天日志 {#the-chat-log}

Home Assistant 将每条消息和`ChatLog` 一起交给你的实体 。 聊天日志目前保存整个对话, 作为`chat_log.content`中的内容对象列表 :

- `SystemContent`:系统迅速。
- `UserContent`:用户所说的,带有可选的`attachments`.
- `AssistantContent`:代理商所说的,带有可选的`tool_calls`和`thinking_content`.
- `ToolResultContent`:工具调用的结果.

聊天日志在聊天会话的存续期间,因此随着已有的更早消息,一个后续问题会随之到来. 你从来没有储存历史自己。

这是你最常使用的电话:

- `await chat_log.async_provide_llm_data(llm_context, user_llm_hass_api, user_llm_prompt, user_extra_system_prompt)` : 构建系统并附加用户在选项中选择的 LLM API 。 传`user_input.as_llm_context(DOMAIN)`为上下文. 当某事出错时,它会提高`ConverseError`,结果会变成`err.as_conversation_result()`。
- `chat_log.llm_api` : 上面呼叫后的 LLM API 实例, 或 `None` 。 它的 `tools` 是您提供给模型的, 而`custom_serializer` 转换他们的计划。
- `chat_log.async_add_delta_content_stream(agent_id, stream)`:添加流化响应的方法. 以 `role`, `content`, `thinking_content` 或 `tool_calls` 输入它的字典 。 它运行工具为您调用并发送它添加的每个消息, 这样您就可以循环到`chat_log.unresponded_tool_results` 是`False` 。
- `chat_log.async_add_assistant_content(content)`:非流体变种. 它还进行工具呼叫并产生结果。
- `chat_log.async_add_assistant_content_without_tools(content)`:增加一个简单的响应。 用它来做没有工具的特工

当模型完成时,`async_get_result_from_chat_log(user_input, chat_log)`从最后的助理消息中构建`ConversationResult`. 它还设置了`continue_conversation` 当最后的信息以问号结尾时(希腊语和中国语的问号也算数),所以一个语音卫星不断监听答案.

全部输入的 API 在 [`chat_log.py`](https://github.com/home-assistant/core/blob/dev/homeassistant/components/conversation/chat_log.py) 中 。

## 方法 {#methods}

### 处理信件 {#handle-a-message}

的人民 执行 `_async_handle_message`. Home Assistant 已经创建了聊天日志, 并在运行时添加用户消息 。

```python
async def _async_handle_message(
    self,
    user_input: ConversationInput,
    chat_log: ChatLog,
) -> ConversationResult:
    """Process a sentence."""
```

持有请求 :

| 名称 | 类型 | 说明 |
| ---- | ---- | ----------- |
| `text` | `str` | 使用者所说. |
| `context` | `Context` | 所采取行动的上下文 。 |
| `conversation_id` | `str \| None` | 对话的ID,用于多回合对话. |
| `device_id` | `str \| None` | 请求的装置,就像一个语音卫星 |
| `satellite_id` | `str \| None` | 请求来自Assist卫星的实体ID。 |
| `language` | `str` | 文字语言. 回落到Home Assistant的语言. |
| `agent_id` | `str` | 处理请求的代理人. |
| `extra_system_prompt` | `str \| None` | 模型的额外指令, 例如 `start_conversation` 动作 。 |

返回以 `intent.IntentResponse` 作为 `response` 的 `ConversationResult` , 可选的 `conversation_id` 和 `continue_conversation` 。

旧集成取代 `async_process` 。 这仍然有效,但是你失去了聊天日志处理,所以新的代码执行`_async_handle_message`.

### 准备 {#prepare}

`async_prepare(language)`是可选的。 Home Assistant一旦它知道一个请求即将到来,就打电话给它,这样你就可以提前装入一个模型或其他资源.

## 状态 {#states}

状态是实体处理的最后一个信件的时间戳, 或者在第一个信件之前 `unknown` 。 Home Assistant 设置并恢复它;`state` 属性是最终的 。

## 示例 {#example}

一个对话实体,可以流出一个模型的响应,让它使用LLM API的工具.

```python
from typing import Literal

from homeassistant.components import conversation
from homeassistant.const import CONF_LLM_HASS_API, MATCH_ALL

from .const import DOMAIN

class MyConversationEntity(conversation.ConversationEntity):
    """A conversation agent backed by a language model."""

    _attr_has_entity_name = True
    _attr_name = None
    _attr_supports_streaming = True

    def __init__(self, entry: MyConfigEntry) -> None:
        """Set up the entity."""
        self.entry = entry
        self._attr_unique_id = entry.entry_id
        if entry.options.get(CONF_LLM_HASS_API):
            self._attr_supported_features = (
                conversation.ConversationEntityFeature.CONTROL
            )

    @property
    def supported_languages(self) -> list[str] | Literal["*"]:
        """Return the supported languages."""
        return MATCH_ALL

    async def _async_handle_message(
        self,
        user_input: conversation.ConversationInput,
        chat_log: conversation.ChatLog,
    ) -> conversation.ConversationResult:
        """Process a sentence."""
        try:
            await chat_log.async_provide_llm_data(
                user_input.as_llm_context(DOMAIN),
                self.entry.options.get(CONF_LLM_HASS_API),
                self.entry.options.get("prompt"),
                user_input.extra_system_prompt,
            )
        except conversation.ConverseError as err:
            return err.as_conversation_result()

        while True:
            stream = self.entry.runtime_data.stream(chat_log)
            async for _ in chat_log.async_add_delta_content_stream(
                self.entity_id, stream
            ):
                pass
            if not chat_log.unresponded_tool_results:
                break

        return conversation.async_get_result_from_chat_log(
            user_input, chat_log
        )
```

`runtime_data.stream` 代表您的客户端库: 它向模型发送聊天日志并生成三角词典 。
