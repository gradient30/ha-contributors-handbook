---
title: 事件循环
description: 运行 Home Assistant Core 的 Ayncio 环路 。 像在网络上等待没有`await`的代码, 停止其他一切。
sidebarGroup: 核心和一体化
term:
  aliases:
  - asyncio
  - executor
  code:
  - async_
  - hass.async_add_executor_job
  related:
  - core
  - hass
  autolink:
  - event loop
---

# 事件循环 {#event-loop}

- 代码:`async_`,`hass.async_add_executor_job`
- 另外: Ayncio,执行人

从 `async_` 开始的函数在事件循环中运行, 并且永远不能屏蔽 。 掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的掌握的有关的有关的有关的有关的有关的有关的有关的有关的有关的有关的有关的有关的有关的有关的有关的有关的有关的有关的有关的的有关的有关的有关的有关的有关的有关的的有关的有关的有关的有关的有关的有关的有关的的有关的有关的的有关的的有关的的有关的有关的有关的有关的有关的有关的有关的的有关的有关的有关的的的有关的的的的有关的有关的有关的的有关的有关的有关的的有关的的有关的有关的

## 相关条件 {#related-terms}

- [Home Assistant Core](/glossary/core): {的答复} Python 应用程序位于Home Assistant 的核心, 及其所有集成, 在Home Assistant/核心寄存器中 。
- [隐藏对象](/glossary/hass) : `HomeAssistant` 集成得到的例子, 访问状态机器、 事件总线、 动作和配置 。
