---
title: 架构
description: 一切是如何组合在一起的，以及背后的决策。
---


# 架构 {#architecture}
Home Assistant 运行着数百万个家庭，从小型的树莓派到壁橱里的服务器都能运行。在其背后，它是一套由成千上万的人在十多年中共同构建的协作组件。本区域解释了其工作原理。

你不需要全部理解才能贡献。从大局入手，当你的工作需要时再深入。每个页面先提供简短版本，然后提供详细内容，供有兴趣的人阅读。

## 从这里开始 {#start-here}
- [大局](/architecture/big-picture)：在一页上展示所有组件，以及它们如何连接。
- [原则](/architecture/principles)：Home Assistant 构建背后的理念。
- [架构决策的制定方式](/architecture/decisions)：讨论架构的地方，以及如何参与。
- [代码仓库](/architecture/repositories)：代码存放的位置。

## 深入探索 {#go-deeper}
- [深入 Home Assistant Core](/architecture/core)：从初创到实体，位于核心的 Python 应用程序。
- [各部分如何交流](/architecture/connections)：API 和登录方式。
- [前端](/architecture/frontend)：网页界面，以及仪表板的工作方式。
- [围绕核心](/architecture/platform)：Supervisor、Home Assistant OS、应用程序、伴侣应用、云和语音。
- [Home Assistant 如何处理信任](/security/how-it-works)，在安全领域：Home Assistant 信任谁，以及可能受到攻击的地方。

## 准备好贡献了吗？ {#ready-to-contribute}
本区域解释了事情如何运作。实际的工作发生在本站的其他区域。每个区域都从一个小的初次贡献开始：| 你想要工作的领域 | 前往 | 第一步 |
| --- | --- | --- |
| Home Assistant Core 和集成 | [核心和集成](/core) | [你对核心的第一次贡献](/core/first-contribution) |
| 网络界面和仪表板 | [前端](/frontend) | [你第一次前端贡献](/frontend/first-contribution) |
| 界面的外观、功能和可读性 | [设计](/design) | [你第一次设计贡献](/design/first-contribution) |
| 安卓和苹果应用 | [伴侣应用](/companion) | [你第一次伴侣应用贡献](/companion/first-contribution) |
| Supervisor 和 Home Assistant OS | [OS 与 Supervisor](/os) | [你对 Supervisor 的第一次贡献](/os/first-contribution) |
| 与 Home Assistant 一起运行的软件 | [应用](/apps) | [你的第一个应用](/apps/first-app) |
| Assist 理解的句子 | [语音翻译](/translate/voice) | [贡献句子和回应](/translate/voice/contributing) |
| Home Assistant 用你的语言 | [翻译](/translate) | [你的第一次翻译](/translate/first-contribution) |
| 用户文档 | [撰写文档](/writing) | [你的第一次文档修正](/writing/first-contribution) |
| 保持家庭安全 | [安全](/security) | [你的第一次安全贡献](/security/first-contribution) |
| 测试和发布版本 | [发布](/releases) | [你的第一次测试版](/releases/first-contribution) |

还不确定？在“入门”中，[你的第一次贡献](/start/first-contribution) 可以帮助你选择。

## 适用人群 {#who-this-is-for}
所有想了解 Home Assistant 内部工作原理的人。页面假设你已经作为用户了解 Home Assistant。涉及代码的部分，对核心部分是 Python，对前端是 TypeScript，但相关解释不需要你去阅读代码。

代码是真理的来源。页面会指向它们所描述代码的位置，这样你可以检查并进一步阅读。每个页面最后都有 _Work on this_ ：当你想修改它所描述的内容时，可以去的地方。

## 与谁交流 {#who-to-talk-to}
- **架构讨论** 在 [architecture repository](https://github.com/home-assistant/architecture/discussions) 进行。
- **工作中有问题** 可以去 [https://www.home-assistant.io/join-chat](https://www.home-assistant.io/join-chat) 上的 [**#developers**](https://discord.com/channels/330944238910963714/554842238073700352) 频道。看不到它？在 **Channels & Roles** 下，选择 **I want to contribute dev skills to Home Assistant**。
- 在这些页面上发现有错误或过时的内容？请使用页面底部的编辑链接。
