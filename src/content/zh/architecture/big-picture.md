---
title: 大局
description: 所有 Home Assistant 的部分都在一页上，每一部分的作用，以及它们如何相互交流。
order: 2
---


# 大局 {#the-big-picture}
Home Assistant 不是一个单一的程序。它是几个协同工作的部分：核心是 Python 应用程序，还有一个网页界面、手机应用程序，以及在大多数安装中运行整个系统的操作系统。本页展示了每个部分及它们的连接方式，以便该区域的其他内容有一个参考。

图示。Home Assistant 的所有部分，从上到下。

- 使用场景  
  - [前端](/architecture/frontend)：在浏览器和应用中  
  - [伴侣应用](/architecture/platform/companion-apps)：安卓和苹果设备  
  - [语音](/architecture/platform/voice)：卫星和 Assist  
  - [其他软件](/architecture/connections)：脚本、Alexa、谷歌  
- 它通过以下方式与核心通信：[WebSocket API、REST API、webhooks](/architecture/connections)  
- [Home Assistant Core](/architecture/core)  
  - [事件循环](/core/internals/asyncio)：运行所有内容  
  - [状态和事件](/core/internals/states)：什么是真实的，发生了什么  
  - [操作](/core/internals/actions)：可以执行的操作  
  - [注册表](/architecture/core/registries)：它记住的内容  
  - 自动化：触发器、条件、操作  
  - [记录器](/architecture/core/history)：历史和统计  
  - [集成](/core/integrations)：与实体的集成，通过 Python 库  
- 核心通过以下方式访问连接的内容：本地网络、互联网、无线电  
- 它连接的对象  
  - 设备：在网络上、Bluetooth、USB- 协议：Zigbee、Z-Wave、Matter、MQTT
  - 服务：天气、能源、人工智能
- 在 Home Assistant OS 上，所有运行于
  - [Home Assistant OS](/os/operating-system)：操作系统
  - [Supervisor](/architecture/platform/supervisor)：运行并更新所有内容
  - [应用程序](/apps/how-apps-work)：核心旁的软件

## 中心：Home Assistant Core {#the-center-home-assistant-core}
[Home Assistant Core](/architecture/core) 是一个 Python 应用程序，每个安装都会运行它。它知道家中每个设备的状态，执行自动化，并保存历史记录。集成将其连接到设备和服务。

最重要的概念：一切都变成 [实体](/glossary/entity)。一个集成会将飞利浦 Hue 灯转换为灯光实体，将恒温器转换为气候实体以及一些传感器。从那时起，其余的 Home Assistant 只处理实体，无论它们来自哪个品牌。

## 使用场景 {#where-people-use-it}
- **[前端](/frontend)** 是网页界面：仪表板、设置、自动化编辑器。它在浏览器中运行，由 Core 提供文件。[其在整体中的位置](/architecture/frontend) 解释了它与 Core 的关系。
- **[伴侣应用](/companion)** 在手机、平板和 Mac 上显示相同的前端，并添加来自设备的传感器、通知和小部件。参见 [它们如何连接](/architecture/platform/companion-apps)。
- **[语音](/architecture/platform/voice)** 将一句口语转化为操作，可以通过厨房里的卫星设备或手机实现。
- **其他软件**，如脚本、Amazon Alexa 和 Google Assistant，通过其 API 或通过 Home Assistant Link 与 Home Assistant 进行通信。

它们都通过相同的 [API](/architecture/connections) 与 Core 通信，并以相同的方式登录。

## 它连接到的内容 {#what-it-connects-to}
集成用于与外部世界通信：本地网络上的设备，像 Zigbee、Z-Wave、Thread 和 Bluetooth 这样的无线电，以及互联网上的服务。知道如何与特定设备通信的代码存在于 Python 库中，集成会使用它。更多内容可以在 [原则](/architecture/principles) 中找到。

一些协议作为独立程序运行，在 Core 旁边：Z-Wave JS 用于 Z-Wave，一个 MQTT 经纪人，以及 Matter 的 Matter 服务器。集成会与该程序通信。

## 它是如何运行的 {#what-runs-it}
在 [Home Assistant OS](/os/operating-system) 上，这是推荐的安装方式，[Supervisor](/architecture/platform/supervisor) 在一个容器中运行 Home Assistant Core，和 [apps](/apps/how-apps-work) 一样，就像一个 MQTT 代理或 Z-Wave JS。它会进行备份，并安装所有内容的更新，包括操作系统。

使用 [Home Assistant Container](/os/installation-types) 时，用户自己在一个容器中运行 Core，而不使用 Supervisor 和 apps。

## 家外 {#outside-the-home}
[Home Assistant Link](/architecture/platform/cloud)，来自 Nabu Casa，是可选的。它使 Home Assistant 可以通过加密隧道从任何地方访问，将其连接到 Alexa 和 Google Assistant，并提供语音服务。

## 一条流程，端到端 {#one-flow-end-to-end}
你从仪表板上打开一盏灯：

1. 你选择灯的卡片。前端通过 [WebSocket API](/core/internals/websocket-api) 发送 `call_service` 给 `light.turn_on`。
2. 核心检查你是否可以执行该操作，并执行 [action](/core/internals/actions)：它在灯实体上调用 `async_turn_on`。
3. 实体（集成的一部分）通过其库告诉灯打开。
4. 灯报告它已打开。实体将其新状态写入 [状态机](/core/internals/states)。
5. 状态机触发 `state_changed`。前端接收并在每个屏幕上显示灯已打开。记录器将其写入历史记录，并且任何等待该事件的自动化任务会运行。

相同的路径也适用于自动化、语音命令或应用程序：唯一不同的是步骤 1。

## 准备好贡献了吗？ {#ready-to-contribute}
本页上的每一部分在本站都有对应区域，并提供首次贡献指导：

- **Home Assistant Core 和集成**：[你的首次 Core 贡献](/core/first-contribution)。
- **前端**：[你的首次前端贡献](/frontend/first-contribution)。
- **伴侣应用**：[你的首次伴侣应用贡献](/companion/first-contribution)。
- **语音**：[语音翻译](/translate/voice)，用于 Assist 能理解的你语言中的句子。
- **Supervisor 和 Home Assistant OS**：[你对 Supervisor 的首次贡献](/os/first-contribution)。
- **应用**：[你在应用区域的首次贡献](/apps/first-contribution)。
- **Home Assistant Link**：`cloud` 集成是 Core 的一部分。

[架构概览](/architecture#ready-to-contribute) 提供完整的地图，包括设计、文档和翻译。
