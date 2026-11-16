---
title: 使用同步依赖
description: 白金法则 async-dependency:集成的图书馆使用asyncio.
sidebarLabel: 关联依赖性
sidebarGroup: 铂
order: 1
---

# 使用同步依赖 {#use-an-async-dependency}

这是白金规则 在`quality_scale.yaml`中,它被称为{叩头}}.

集成用于与设备或服务交谈的库必须写成Ayncio. 它的I/O和网络请求一样,在Home Assistant的[事件循环](/glossary/event-loop)上运行为coroutines,而不是屏蔽需要线程的呼叫.

## 为什么这很重要 {#why-it-matters}

运行在Ayncio。 屏蔽库无法在事件循环上运行,所以每个呼叫都必须到执行器中的线程,结果必须返回循环. 每一个开关都花费时间和记忆力,随着许多集成投票,它增加了许多设备。 一个Async库避免了这一切,集成代码也变得更加简单.

## 示例 {#example}

使用一个屏蔽库,每个呼叫都会通过执行器:

```python
data = await hass.async_add_executor_job(client.get_data)
```

有了Aync库,你直接等待电话:

```python
data = await client.get_data()
```

如果您自己维护库, 这通常意味着在 HTTP 的 `aiohttp` 或 `httpx` 上建库, 或者在 Ayncio 流上建原始套接字 。 这也使得[泻入网会话](/core/quality-scale/inject-websession)成为可能.

## 如何检查 {#how-it-is-checked}

本规则经审核. 代码中一个很好的提示是使用 `async_add_executor_job` 呼叫库 。

## 例外 {#exceptions}

如果集成没有外部依赖性,或者其依赖性没有I/O,这一规则不适用.

## 相关规则 {#related-rules}

- [泻入网会话](/core/quality-scale/inject-websession)}:通过网页会话.
- [依赖透明度](/core/quality-scale/dependency-transparency) : 使用透明依赖 。
