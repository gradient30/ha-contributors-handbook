---
title: 声音的工作原理
description: 一句口语如何变成动作：唤醒词、语音转文字、会话代理和文字转语音，以及每个环节运行的位置。
order: 8
sidebarLabel: 语音
---


# 声音的工作原理 {#how-voice-works}
[Assist](/glossary/assist) 是 Home Assistant 的语音助手。你说“打开厨房的灯”，灯就会亮起来。在这句话的背后有一系列步骤，每个步骤都可以在不同地方运行：你说话的设备上、你的 Home Assistant 上，或者在云端。

## 简而言之 {#in-short}
- 一个 [Assist 流水线](/glossary/assist-pipeline) 包含四个步骤：唤醒词、语音转文本、对话代理和文本转语音。
- 每个步骤都是一个独立的引擎，用户为每个步骤选择一个：本地的、集成的，或者来自 Home Assistant Link 的。
- 对话代理将文本转换为动作。内置的对话代理会将句子匹配到 [意图](/glossary/intent)，AI 代理则使用大型语言模型。
- 语音卫星，如 Home Assistant Voice 预览版，是分布在房子周围的麦克风和扬声器。

## 流程管道 {#the-pipeline}
| 步骤 | 输入 | 输出 | 引擎 |
| --- | --- | --- | --- |
| 唤醒词 | 声音 | “有人说出唤醒词” | 在卫星上，或在Home Assistant |
| 语音转文本 | 声音 | 文本 | 本地，如 Whisper 或 Speech-to-Phrase，或在云端 |
| 会话代理 | 文本 | 一个动作和一个回答 | 内置代理，或 AI 代理 |
| 文本转语音 | 回答 | 声音 | 本地，如 Piper，或在云端 |

用户在 **设置** > **语音助手** 中设置流程管道，每个卫星使用一个。在 Assist 对话中输入文本会运行相同的流程管道，从会话代理开始。

## 会话代理 {#conversation-agents}
**内置代理** 完全在本地运行。它通过 hassil 库将句子与模板进行匹配，使用来自 [intents repository](https://github.com/OHF-Voice/intents) 的每种语言的句子，由 [Open Home Foundation](/glossary/open-home-foundation) 提供。匹配会产生一个意图，比如 `HassTurnOn`，对应的区域是厨房，领域是灯光，而 Home Assistant 来处理它。

**AI 代理** 来自连接到大型语言模型的集成。Home Assistant 通过其 LLM API 为模型提供工具，以查看和控制用户在 Assist 中暴露的实体。用户可以先让内置代理尝试，只有当它无法理解时才使用 AI 代理。

## 卫星 {#satellites}
卫星是一种带有麦克风和扬声器的设备。它会监听唤醒词，将音频流传输到 Home Assistant，并播放答案。ESPHome 设备，例如 Home Assistant Voice 预览版，以及支持怀俄明协议的设备都可以是卫星。每个卫星都是一个 `assist_satellite` 实体。

## 更深入了解 {#go-deeper}
- [Assist 管道](/core/internals/assist-pipelines)：运行管道、其事件以及音频如何传送
- [意图](/core/internals/intents) 和 [内置意图](/core/internals/built-in-intents)：一句话如何变成一个动作
- [对话 API](/core/internals/conversation-api) 和 [大语言模型 API](/core/internals/llm-api)：用于代理和 AI 集成
- 每个步骤背后的实体：[唤醒词](/core/entities/wake-word)、[语音转文字](/core/entities/stt)、[对话](/core/entities/conversation)、[文字转语音](/core/entities/tts) 以及 [Assist 卫星](/core/entities/assist-satellite)
- [语音翻译](/translate/voice)：Assist 能理解的句子，按语言分类

## 进行实践 {#work-on-this}
- 想说 Assist 还不太理解的语言？[语音翻译](/translate/voice) 是起点，不需要编程。
- 构建语音引擎、AI 代理或卫星？从 [你对核心的首次贡献](/core/first-contribution) 开始，然后查看“更深入了解”下的页面。
