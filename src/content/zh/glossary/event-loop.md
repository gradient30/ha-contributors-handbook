---
title: 事件循环
description: 运行 Home Assistant Core 的 asyncio 循环。若代码在没有 await 的情况下等待网络，就会卡住其他所有任务。
sidebarGroup: 核心与集成
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

- 代码：`async_`、`hass.async_add_executor_job`
- 另见：asyncio、executor

以 `async_` 开头的函数在事件循环中运行，并且绝不能阻塞。只能阻塞的代码（例如没有异步支持的库）应通过 `hass.async_add_executor_job` 放到 executor 线程里运行。

## 相关术语 {#related-terms}

- [Home Assistant Core](/glossary/core)：位于 Home Assistant 核心的 Python 应用程序及其所有集成，代码在 `home-assistant/core` 仓库中。
- [hass 对象](/glossary/hass)：集成获得的 `HomeAssistant` 实例，用于访问状态机、事件总线、动作和配置。

