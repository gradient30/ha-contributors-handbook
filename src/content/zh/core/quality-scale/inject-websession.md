---
title: 通过网络会话
description: 白金规则注入- 106.websession:库接受Home Assistant的网络会话.
sidebarLabel: 泻入网会话
sidebarGroup: 铂
order: 2
---

# 通过网络会话 {#pass-in-the-web-session}

这是白金规则 在`quality_scale.yaml`中,它被称为{叩头}}.

集成的库必须接受外部的HTTP会话,集成必须在Home Assistant提供的会话中通过. Home Assistant 为 [亚欧http](https://docs.aiohttp.org/) 和 [HTTPX 密码](https://www.python-httpx.org/) 共享会话, 因此库使用其中之一 。

## 为什么这很重要 {#why-it-matters}

许多集成论讲HTTP. 如果每个库打开自己的会话,Home Assistant最终会有许多连接池,每个库都有自己的连接和SSL设置. 共享会话会重新利用集成之间的连接,并使用更少的内存和更少的套接字.

## 示例 {#example}

将共享的 aiohttp 会话传递给 `async_setup_entry` 中的客户端 :

```python
from homeassistant.helpers.aiohttp_client import async_get_clientsession

async def async_setup_entry(
    hass: HomeAssistant, entry: MyConfigEntry
) -> None:
    """Set up My integration from a config entry."""
    session = async_get_clientsession(hass)
    client = MyClient(entry.data[CONF_HOST], session=session)
    ...
```

对于HTTPX,使用`get_async_client`从`homeassistant.helpers.httpx_client`开始.

有时一个共享的会话不是你想要的,例如当库使用不应泄露给其他集成的饼干时. 然后创建您自己的会话 Home Assistant 仍然管理 : `async_create_clientsession` for aiohttp, 或 `create_async_httpx_client` for HTTPX 。

## 如何检查 {#how-it-is-checked}

本规则经审核.

## 例外 {#exceptions}

如果集成没有提出HTTP请求,例如因为它讨论Modbus,Bluetooth,或者一个原始的TCP套接字,则这个规则不适用.

## 相关规则 {#related-rules}

- [关联依赖性](/core/quality-scale/async-dependency) : 使用同步依赖 。
