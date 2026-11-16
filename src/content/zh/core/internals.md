---
title: 核心如何工作
description: Home Assistant Core的内在。 拥有对象,事件,状态,Ayncio,认证,API,以及语音和AI的构件.
order: 40
sidebarGroups:
- 核心内容
- 自动同步
- 认证
- 你说的
- 语音和AI
---

# 核心如何运作 {#how-core-works}

每个集成都与同一组小块块交谈:事件总线,状态机器,动作注册,以及配置. 他们都挂在一个物体,`hass`, 他们都运行在一个Ayncio事件循环。 一旦你知道这些碎片的行为, 大部分核心停止是魔法。

这部分是针对想要了解集成下发生的情况,在核心本身上工作,或者从外部构建一个对Home Assistant说话的客户端的开发者. 关于核心,前端,Supervisor和操作系统如何组合的大图,参见[架构](/architecture)区域.

## 从哪里开始 {#where-to-start}

如果你是新到核心,先读这三本. 他们解释你在每一个融合中遇到的事情:

1. [隐藏对象](/core/internals/hass):什么是`hass`,什么挂着它。
2. [在 Home Assistant 中同步](/core/internals/asyncio): 为什么几乎一切都是`async`, 以及您可以从哪里调用哪些功能 。
3. [傀儡](/core/internals/events)和[状态](/core/internals/states):事情是如何发生的,以及Home Assistant如何记住它们。

## 核心内容 {#the-core}

- [隐藏对象](/core/internals/hass):中心对象,和`hass.config`上的核心配置.
- [傀儡](/core/internals/events):在活动总线上开火和监听.
- [国家](/core/internals/states):状态机器和状态对象.
- 10. [动作](/core/internals/actions):动作注册、呼叫动作和响应数据。

## 自动同步 {#async}

- [在 Home Assistant 中同步](/core/internals/asyncio):事件循环,衣冠,召回,以及执行者.
- [Thread安全](/core/internals/thread-safety): 当您的代码运行在事件循环之外时, 要使用哪个 API 。
- [封锁行动](/core/internals/blocking-operations): 不让 I/O 进入事件循环, 包括导入 。

## 认证

- [认证工作方式](/core/internals/auth):用户,证书,令牌,认证提供者,以及多要素模块.
- [权限](/core/internals/permissions): 政策, 检查你的代码 。
- [认证 API](/core/internals/auth-api) : 让一个应用登录到 Home Assistant 与 OAuth 2 的实例 。

## 你说的 {#apis}

- 1929 [(原始内容存档于2018-09-21) (英语). Rest API](/core/internals/rest-api)的制度: `/api/` 下的 HTTP 终点 。
- [API (韩语)](/core/internals/websocket-api): 前端使用的API, 以及如何添加自己的命令 。
- [案例发现](/core/internals/instance-discovery):应用程序如何在网络上找到Home Assistant.
- [运动會](/core/internals/modbus): Modbus 设备的库,并共享一个连接.
- taitified [LoRAWAN 设备](/core/internals/lorawan): 注册一个网络服务器, 并曝光其中的设备 。

## 语音和AI {#voice-and-ai}

- [意图](/core/internals/intents):处理和发射意图。
- [内设意图](/core/internals/built-in-intents): 意图 Home Assistant 处理出框 。
- [对话 API](/core/internals/conversation-api): 向对话代理发送文本并读取回复.
- 将提供语句到文本, 意向识别, 以及文本到语句 WebSocket API. (英语).
- [LLM API 语言](/core/internals/llm-api): 向大型语言模型曝光工具,并构建自己的API.

打造谈话代理,语音对文本提供商,还是文字对语音提供商?. 这些实体,见[对话](/core/entities/conversation)、[语音对文本](/core/entities/stt)和[文本对语音](/core/entities/tts)。 写句如此 Assist 理解您的语言是翻译工作 : 见 [翻译语音命令](/translate/voice) 。

## 谁说话 {#who-to-talk-to}

- 有关于核心内部的技术问题吗? 在 [编码支持**](https://discord.com/channels/330944238910963714/1257019582112334014) 上启动一条线程 。
- 许多语音工作,如句子和醒字引擎,发生在[超高频声音](https://github.com/OHF-Voice)组织在GitHub上. 融合本身,如`conversation`和`assist_pipeline`,生活在核心中.
- 关于改变核心工程如何作为[架构存储器](https://github.com/home-assistant/architecture/discussions)讨论开始的建议。
