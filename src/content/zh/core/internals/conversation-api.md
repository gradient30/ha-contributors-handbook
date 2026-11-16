---
title: 对话 API
description: 向 REST 或 WebSocket 的对话代理发送文本 API,读读它给回的回复.
sidebarGroup: 语音与 AI
order: 52
---

# 对话 API {#conversation-api}

`conversation` 集成取一个句子, 把它交给 [对话代理](/glossary/conversation-agent), 并返回代理响应 。 内置代理将句子匹配到 [意图](/core/internals/intents) 并处理它 。 其他特工,比如那些有大型语言模型支持的特工,都以自己的方式行事. 无论是哪种反应都是一样的。

的支持者,请参见[实情](/core/entities/conversation)。的支持率是1

## 发送句子 {#send-a-sentence}

在 REST API 上, POST 到 `/api/conversation/process` :

```json
{
  "text": "turn on the lights in the living room",
  "language": "en"
}
```

在 WebSocket API 上, 发送 `conversation/process` 并带有相同的字段 :

```json
{
  "id": 5,
  "type": "conversation/process",
  "text": "turn on the lights in the living room",
  "language": "en"
}
```

| 外地 | 说明 |
| --- | --- |
| `text` | 要求。 论句. |
| `language` | 句子语言. 默认实例的语言 。 |
| `agent_id` | 拟用之剂. 默认内置代理, `conversation.home_assistant` 。 |
| `conversation_id` | 继续前坤对话. 见{L坤}. |
| `device_id` | 呃,句子来自的装置,就像一个语音卫星 |
| `satellite_id` | 卫星的实体标识 句子来自。 |

## 回应 {#the-response}

```json
{
  "response": {
    "response_type": "action_done",
    "language": "en",
    "data": {
      "success": [
        {"name": "Living Room", "type": "area", "id": "living_room"},
        {"name": "Ceiling", "type": "entity", "id": "light.ceiling"}
      ],
      "failed": []
    },
    "speech": {
      "plain": {
        "speech": "Turned on the lights",
        "extra_data": null
      }
    },
    "card": {}
  },
  "conversation_id": "01J9Z7K1M3S8TQ0Y6E4H2B5N7C",
  "continue_conversation": false
}
```

- 发生了什么事? 见下文。
- `data`:取决于响应类型.
- `speech`:对用户说什么. 纯文本在 `plain` 下, 或 `ssml` [SSML 软件](https://www.w3.org/TR/speech-synthesis11/) 下。
- `conversation_id`:通过下句继续对话.
- `continue_conversation` : `true` 如果代理商希望用户给出答案, 如在提问后 。

### 已采取的行动 {#action-done}

意图做了一些事情,比如打开灯。 `data.success` 列出已经行动的目标, `data.failed` 列出失败的目标 。 每个目标有一个`name`,一个`type`,和一个可选的`id`. 该类型为`floor`,`area`,`domain`,`device_class`,`device`,`entity`,或`custom`之一.

目标相辅相成,从一般到具体。 "关闭所有灯"有一个目标,`domain`光. "打开厨房灯"有两个: `area`厨房和`domain`灯光. "打开厨房的百叶窗"有三个:`area`厨房,`domain`封面,和`device_class`瞎子.

### 查询答案 {#query-answer}

答案回答了一个问题,比如"温度是多少?". 答案在 `speech` 中, `data.success` 列出所询问的内容 。

### 错误 {#error}

出了点问题ình'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

- `no_intent_match`:句子与任何意图不符.
- `no_valid_targets`: 区域、 设备或实体不存在, 或未暴露 。
- `failed_to_handle`: 处理意图时出错 。
- `unknown`: 意图处理以外的错误 。

## 谈话 {#conversations}

一个支持它的经纪人会跟踪谈话,所以"在厨房里?"在"打开客厅的灯光"之后就有意义了. 每一份回复都有`conversation_id`。 随下句寄之以续曰:

```json
{
  "text": "and in the kitchen?",
  "conversation_id": "01J9Z7K1M3S8TQ0Y6E4H2B5N7C"
}
```

## 预装句子 {#preload-sentences}

装入语言的句子需要一点时间. 要实情在第一次请求前准备好,请在WebSocket上方发送`conversation/prepare` API,带有可选的`language`和`agent_id`:

```json
{
  "id": 6,
  "type": "conversation/prepare",
  "language": "en"
}
```

## 其他 WebSocket 命令 {#other-websocket-commands}

- `conversation/agent/list`:可用的代理,可选择由`language`和`country`过滤.
- `conversation/sentences/list`(admin):在自动化中由句子触发器注册的句子.
- `conversation/agent/homeassistant/language_scores`:内置代理对每种语言的支持程度如何,以及给定的`language`和`country`的首选语言.
- `conversation/agent/homeassistant/debug` : 显示内置代理如何匹配 `sentences` 列表, 而不对它们采取行动 。 写句子时有用.
