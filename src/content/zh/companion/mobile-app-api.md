---
title: 移动应用 API
description: 一个应用程序如何通过移动 app集成连接到{H0茸}. 注册、网钩、传感器、位置、通知和网页视图。
order: 4
---



# 移动应用 API {#mobile-app-api}
官方的同伴app通过 `mobile_app` 在 Core 中的整合来与 Home Assistant 交谈 。 这是一个公开的API:任何应用程序都可以使用它作为设备在Home Assistant中出现,报告传感器和位置,并收到通知. 本节描述的是,为在官方应用软件上工作的人和任何建造自己的软件的人.

## 如何融为一体 {#how-it-fits-together}

1. ** 查找并登录。 ** 应用找到实例,用户登录与OAuth 2. 该应用程序获得访问权限并刷新令牌.
2. ** 登记员。 ** 使用这些符号,应用程序会用 `mobile_app` 注册自己 。 Home Assistant 为其创建设备, 并返回一个 Webhook ID, 以及 Home Assistant Link 加密和 URL 的可选密件 。
3. ** 发送数据。 ** 从此,该应用程序向webhook发送传感器更新,位置,以及其他请求. Webhook 请求不需要符号:webhook ID是证书.
4. ** 接收通知。 ** Home Assistant 将通知推到 WebSocket 连接上, 或通过应用程序的驱动服务。
5. ** 前端显示。 ** 该应用程序在网页视图中显示前端,并的授权给它一个符号,因此用户不会两次登录.

[辅助应用程序架构](/architecture/platform/companion-apps)有更大的画面。

## 页面 {#pages}

- [连接和注册](/companion/mobile-app-api/setup):发现,登录,和注册电话。
- [发送数据 我有](/companion/mobile-app-api/sending-data):webhook,它的URL,请求格式,以及每个请求类型.
- [加密](/companion/mobile-app-api/encryption):用libsodium加密网络hook流量.
- [传感器](/companion/mobile-app-api/sensors): 登记和更新传感器,并保持其启用状态同步 。
- 的进展情况 [通知](/companion/mobile-app-api/notifications): WebSocket推,云推,和推服务器的合同.
- [网页视图](/companion/mobile-app-api/webview): 显示前端而无需第二个登录.

## 在代码中 {#in-the-code}

整合位于 [`homeassistant/components/mobile_app/`](https://github.com/home-assistant/core/tree/dev/homeassistant/components/mobile_app) 核心 :

| 文件 | 它会做什么 |
| --- | --- |
| `http_api.py` | 登记终点 |
| `webhook.py` | 网络浏览和大多数请求类型 |
| `helpers.py` | 加密和答复 |
| `websocket_api.py` | WebSocket 推动频道 |
| `notify.py` | 发送通知 |
| `live_activity/` | iOS 的 Live 活动符, 以及它们的两个请求类型 |

当代码和此文档存在分歧时,代码获胜. 对集成的修改遵循正常的[核心捐款进程](/core).
