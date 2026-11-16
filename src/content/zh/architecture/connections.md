---
title: 这些碎片如何交流
description: Home Assistant Core 与其周围一切之间的 API，以及每个连接的人如何证明他们的身份。
order: 20
---


# 这些碎片如何交流 {#how-the-pieces-talk}
Home Assistant Core 从不孤单。前端、伴侣应用、语音卫星、Supervisor 和 Home Assistant Link 都会与它通信。它们通过少量 API 与 Core 的自有 Web 服务器进行通信，默认端口为 8123。

## 连接一览 {#the-connections-at-a-glance}
| 谁 | 通过什么与 Core 通信 | 做什么 |
| --- | --- | --- |
| 浏览器或应用中的前端 | [WebSocket API](/core/internals/websocket-api) | 所有操作：状态、动作、设置、实时更新 |
| 伴侣应用 | WebSocket API 和 Webhook | 显示前端，并发送传感器数据和位置 |
| 脚本及其他软件 | [REST API](/core/internals/rest-api) 或 WebSocket API | 读取状态，执行动作 |
| 互联网设备和服务 | Webhook | 向集成推送数据 |
| Supervisor | 自有 API 和 Core 的 API | 管理 Core、应用和备份，查看 [Supervisor](/architecture/platform/supervisor) |

## WebSocket API {#the-websocket-api}
WebSocket API 是主要的入口方式。与 REST API 不同，连接保持打开状态，因此 Home Assistant 可以在变化发生的那一刻就推送每一个变化：一盏灯亮起时，会立即在每个屏幕上显示为开启状态。前端几乎在所有操作中都会使用它，通过 [home-assistant-js-websocket](https://github.com/home-assistant/home-assistant-js-websocket) 库。集成可以添加自己的命令。

REST API 覆盖基础功能，比如读取状态和执行操作，适用于需要简单功能的软件。

## 登录 {#logging-in}
每个连接，除了 webhooks，都从验证你的身份开始。用户通过 OAuth 2 流程登录，并获得令牌：一个长期有效的刷新令牌和一个持续 30 分钟的访问令牌。脚本使用长期有效的访问令牌，用户可以在个人资料中创建。请参见[认证如何工作](/core/internals/auth)和[权限](/core/internals/permissions)。

最重要的界限是管理员和其他用户之间的界限：更改设置、添加集成以及任何揭示敏感信息的操作仅限管理员。请参见[Home Assistant如何处理信任](/security/how-it-works)。

## Webhooks（网络钩子） {#webhooks}
Webhook 是一种无需登录即可访问的方式：一个 URL，`/api/webhook/<webhook_id>`，任何人都可以向其发送数据。这是安全的，因为 ID 是一个随机的 64 位字符值：知道它就有权限。未知的 ID 会得到与已知 ID 相同的答复，因此没有人能得知某个 ID 是否存在，并且集成可以让 webhook 仅接受来自家庭网络的请求。

Webhook 适用于无法登录的场景，例如发送更新的服务，或在后台发送其位置的手机。通过 Home Assistant Link，webhook 还可以通过云获得一个公共 URL，因此即使不在家，也可以工作，而无需将 Home Assistant 暴露到互联网上。

## 在代理后面 {#behind-a-proxy}
Core 可以自己提供 HTTPS 服务，但很多人会在前面放一个反向代理，或者使用 Home Assistant Link。在代理后面，Core 只信任用户配置的代理转发的地址，因此没有人可以冒充在家庭网络中。

## 开始操作 {#work-on-this}
- 对 Core 新手？从 [你在 Core 的第一个贡献](/core/first-contribution) 开始。API 是 Core 的一部分。
- [WebSocket API](/core/internals/websocket-api) 和 [REST API](/core/internals/rest-api)：每条消息和端点。
- [添加 WebSocket 命令](/frontend/extending/websocket-api)：当前端需要 Core 提供新功能时使用。
- [认证工作原理](/core/internals/auth)：令牌、用户和权限。
