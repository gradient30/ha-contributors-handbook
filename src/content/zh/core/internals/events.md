---
title: 活动总线
description: 事件公交如何运作,如何点燃自己的事件,如何在不泄露听众的情况下聆听事件.
sidebarGroup: 核心
order: 2
sidebarLabel: 傀儡
---

# 活动总线 {#the-event-bus}

本页面解释事件总线下方如何运作. 从您的整合点火事件, 或对 Home Assistant 中发生的事件与事件助手的反应, 见[整合中的活动](/core/integrations/events) 。

Home Assistant是由事件驱动的。 状态变化:这是一个事件。 一个动作叫做:事件。 Home Assistant开始或停止:事件。 `hass.bus`上的事件总线载着他们,任何代码都可以听.

实际上,你很少听生车。 可获得普通案件的 Home Assistant 比如跟踪状态变化或者每分钟运行一些东西 。 适时用之. 本页解释了它们所依赖的。

## 什么是一个事件 {#what-an-event-is}

事件是来自 `homeassistant.core` 的 `Event` 对象 :

- `event_type`:一个字符串,最多64个字符. 自定义事件前缀为您的整合域, 如 `my_integration_button_pressed` 。
- `data`:一个词典。 保持JSON的序列, 因为事件由记录器存储 并发送到 WebSocket API. (英语).
- `context`:导致事件的`Context`。 它将事件连接到用户,自动化,或启动它的动作.
- `origin` : `EventOrigin.local` 对于来自此实例的事件, `EventOrigin.remote` 对于来自外部的事件, 如通过 REST API 。
- `time_fired`: 当事件被发射。

Home Assistant本身的火灾事件如`state_changed`,`call_service`,`homeassistant_start`,`homeassistant_started`和`homeassistant_stop`。 常数生活在[`homeassistant/const.py`](https://github.com/home-assistant/core/blob/dev/homeassistant/const.py),如`EVENT_STATE_CHANGED`. [关于Home Assistant.io的参考文献](https://www.home-assistant.io/docs/configuration/events/) 列出用户看到的事件 。

> [!IMPORTANT]
> 事件记录在数据库中。认真地思考一下您事件数据的大小和形状,然后经常点火事件.认真地解释事件是如何存储的 [数据科学门户](https://data.home-assistant.io/docs/events/) 。

## 启动一个事件 {#fire-an-event}

从事件环路各项人权, 使用 `async_fire` :

```python
from homeassistant.core import HomeAssistant

DOMAIN = "my_integration"

async def async_press(hass: HomeAssistant, button_id: str) -> None:
    """Tell the rest of Home Assistant a button was pressed."""
    hass.bus.async_fire(
        f"{DOMAIN}_button_pressed",
        {"button_id": button_id},
    )
```

从另一个线程,使用 `hass.bus.fire` 代替 。 它为您安排了事件循环。 见[线程安全](/core/internals/thread-safety).

当您因为一个用户做了某某事而发射一个事件时,通过他们的`context`,所以日志和权限系统可以归属它. 在动作处理器内,即`call.context`.

代表物理按钮或远程的集成往往想要[事件实体](/core/entities/event)而不是原始事件. 见[提供设备事件](/core/integrations/events#make-device-events-available)。

## 聆听事件 {#listen-for-events}

`async_listen` 注册一个听众并返回一个删除它的函数。 总是保持这个功能,当你完成它,或者你的听者永远活着。

```python
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import EVENT_HOMEASSISTANT_STOP
from homeassistant.core import Event, HomeAssistant, callback

async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry
) -> None:
    """Set up my integration."""

    @callback
    def handle_stop(event: Event) -> None:
        """Close the connection when Home Assistant stops."""
        entry.runtime_data.close()

    entry.async_on_unload(
        hass.bus.async_listen_once(EVENT_HOMEASSISTANT_STOP, handle_stop)
    )
```

`entry.async_on_unload` 配置项卸载时调用删除功能 。 在实体中,同样使用`self.async_on_remove`.

有几个事情要知道:

- 你的听者如何运行取决于它是什么。 以 `@callback` 装饰的函数在事件循环中直接运行 。 Coroutine 函数在事件循环中作为任务运行. 没有 `@callback` 的纯函数运行在执行器的线索中 。 用 `@callback` 装饰小的,非阻塞的听众: 这是最快的选择 。
- ** 听一种活动类型。 ** 你可以通过 `MATCH_ALL` 得到每件事, 但这是昂贵的, 很少你想要的。
- ** Filter 提前。 ** `async_listen` 使用可选的 `event_filter` : 一个 `@callback` 函数, 如果收听器要运行, 则获得事件数据并返回 `True` 。 它运行之前,你的听众 预定,这节省工作 在繁忙的公交车。
- QQH0}**在第一次活动后删除听众.

要输入事件数据,核心使用`homeassistant.util.event_type`的`EventType`. `EVENT_STATE_CHANGED`是一个`EventType[EventStateChangedData]`,所以一个听众得到`Event[EventStateChangedData]`,一个类型检查员知道`event.data`中的内容.

## 常见活动的助手 {#helpers-for-common-events}

`homeassistant.helpers.event` 建立在 `async_listen` 的帮助者之上, 用于您通常想要的东西, 例如跟随少数实体的状态, 或在一天的时间运行一些东西 。 他们为你过滤,并返回一个功能来删除听众,就像`async_listen`一样. 完整列表中包含实例,位于[整合中的活动](/core/integrations/events#listen-to-home-assistant).

## 事件或调度员 {#events-or-the-dispatcher}

事情经过了总线,被记录, 任何人都可以看到, 包括自动化和WebSocket API. (英语). 对于在您集成中仅具有重要性的信号, 如“ 设备 12 的新数据到来 ” , 请使用 `homeassistant.helpers.dispatcher` 中的调度器 。 `async_dispatcher_send` 和 `async_dispatcher_connect` 像事件一样工作, 但保持内存而不记录 。
