---
title: WebSocket API
description: Home Assistant Core的API,前端和同伴的应用程序在一个开通的连接上,用来读取状态,执行动作,并在发生时获得更新.
sidebarGroup: 核心与集成
term:
  code:
  - websocket_api
  - /api/websocket
  - home-assistant-js-websocket
  related:
  - frontend
  - companion-app
  - core
  autolink:
  - WebSocket API
---

# API (韩语) {#websocket-api}

- 在代码中:`websocket_api`,`/api/websocket`,`home-assistant-js-websocket`

一个客户端连接到`/api/websocket`,用访问符登录,然后作为JSON消息发送命令. 整合可以使用 `websocket_api` 整合来添加自己的命令. 前端通过Home Assistant-js-websocket图书馆与之交谈.

信件和如何添加命令参见[该 WebSocket API](/core/internals/websocket-api) 。

## 相关条件 {#related-terms}

- [前端](/glossary/frontend):用 Lit 和 TypeScript 建造的 Home Assistant 的网页界面, 位于家用辅助/ 前端寄存器中 。
- [辅助应用程序](/glossary/companion-app):Android,iOS和macOS的应用程序 Home Assistant. 它显示前端,并添加来自设备的传感器,通知和部件.
- [Home Assistant Core](/glossary/core): {的答复} Python 应用程序位于Home Assistant 的核心, 及其所有集成, 在Home Assistant/核心寄存器中 。
