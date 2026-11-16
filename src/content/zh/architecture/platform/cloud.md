---
title: Home Assistant Link
description: Home Assistant Link 如何让家从任何地方都能访问，并将其连接到语音助手，而无需将其开放到互联网。
order: 7
---




# Home Assistant Link {#home-assistant-link}
Home Assistant Link 是来自 [Nabu Casa](/glossary/nabu-casa) 的订阅服务。它增加了在家中难以实现的功能：可以从任何地方联系、与 Amazon Alexa 和 Google Assistant 配合工作，以及语音服务。它在 [2026 年 10 月](https://www.home-assistant.io/blog/2026/10/02/big-tech-ruined-the-cloud-so-were-renaming-ours/) 之前被称为 Home Assistant Cloud。在代码中，它仍然是 `cloud` 集成。

它始终是可选的。它所做的所有事情都可以在没有它的情况下完成，只是需要更多的工作。

## 简而言之 {#in-short}
- Core 中的 `cloud` 集成通过 hass-nabucasa 库连接到 Nabu Casa。
- **远程访问** 通过一个加密隧道进行，该隧道由 Home Assistant 自己打开。家庭中不会开放任何端口。
- **Alexa 和 Google Assistant** 将它们的指令通过云发送到 Home Assistant。
- **Cloudhooks** 为 [webhooks](/architecture/connections) 提供公共 URL，因此伴侣应用可以在家外使用。
- [语音](/architecture/platform/voice) 的语音转文本和文本转语音，以及异地备份。

## 远程访问，无需开门 {#remote-access-without-opening-the-door}
通常，从外部访问 Home Assistant 意味着需要在路由器上打开端口，并管理证书。Home Assistant Link 改变了这一点：Home Assistant 会主动连接到云端，并保持该连接打开。来自外部的请求会通过这条连接返回。

从用户的浏览器到 Home Assistant 的整个连接都是加密的，使用的是属于家庭的证书。云端仅传递流量，但无法读取内容。

## 语音助手 {#voice-assistants}
Amazon Alexa 和 Google Assistant 需要互联网服务才能交互。云端就是这个服务：它接收命令，并通过同一连接将命令传递给 Home Assistant 中的 `alexa` 和 `google_assistant` 集成。用户可以选择哪些实体可以被访问。

## 在代码中 {#in-the-code}
| 什么 | 在哪里 |
| --- | --- |
| 核心部分 | [`homeassistant/components/cloud/`](https://github.com/home-assistant/core/tree/dev/homeassistant/components/cloud) |
| 该库 | [hass-nabucasa](https://pypi.org/project/hass-nabucasa/) |

## 处理这个 {#work-on-this}
- `cloud` 集成是 Core 的一部分：从 [你对 Core 的第一次贡献](/core/first-contribution) 开始。
- 云使 webhook 可以从外部访问，参见 [各部分如何通信](/architecture/connections)。
