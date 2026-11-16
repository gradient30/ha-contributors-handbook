---
title: 在 Home Assistant 中同步
description: 为什么 Home Assistant 运行在一个 Ayncio 事件循环上, 您所写的功能类型, 以及如何移动工作 进出循环 。
sidebarLabel: 在 Home Assistant 中同步
sidebarGroup: 异步
order: 10
---

# 在 Home Assistant 中同步 {#async-in-home-assistant}

Home Assistant Core运行于Python的`asyncio`。 所有核心对象,如状态机器,事件总线,以及注册,都生活在一个线程中:[事件循环](/glossary/event-loop). 只有一个代码运行在那里一次。 在两个 `await` 之间, 您的代码运行时没有其它代码在中间运行, 所以当其它代码查看时, 状态变化永远不会完成 。

这有两个方面。 当一个coroutine等待的东西, 像一个网络响应, 其他代码运行在此期间。 因此,跨 `await` 的工作仍需要 `asyncio.Lock` 才能将它分开 。 例如,协调员这样做是为了刷新。 但是,当事件循环中的代码 blocks 时,像来自同步库的网络呼叫或者从磁盘读取文件, Everything waits. 单打一个阻断电话会让整个系统变得缓慢. 这页的大部分内容是避免它。

新来的Ayncio? Python关于[与Ayncio一起开发](https://docs.python.org/3/library/asyncio-dev.html)的文档是一个好的开始,关于Ayncio如何和为什么工作的方式, [Robert Smallshire的演讲](https://www.youtube.com/watch?v=M-UcUs7IMIM)也是如此。

## 职能的种类 {#the-kinds-of-functions}

Home Assistant有命名惯例:其名称以`async_`开头的函数必须在事件循环中运行. 你处理的功能有四种.

### 套装功能 {#coroutine-functions}

与 `async def` 一起宣布 。 呼唤一个人返回一个曲棍球,这在等待或作为一项任务安排之前一无所获。 在等待期间,其他工作在事件循环中进行。

```python
async def async_update_data(self) -> None:
    """Fetch the latest data from the device."""
    self._data = await self._client.async_get_status()
```

使用这些在 I/O 上等待的任何东西,只要您拨打的库是 Aync.

### 回拨 {#callbacks}

从 `homeassistant.core` 中以 `@callback` 装饰的纯函数 。 它承诺在事件循环中运行是安全的:它不做I/O,也永远不会挡住. 它不能等待任何东西,但它可以安排一项任务。

```python
from homeassistant.core import Event, callback

@callback
def _async_handle_event(self, event: Event) -> None:
    """Handle an event from the bus."""
    self._last_event = event.data
    self.async_write_ha_state()
```

何不把一切都做成胸针? 速度和一致性。 Home Assistant马上回电。 皮管必须包裹在任务和排程中,每个 `await` 是其它代码在中间运行的点 。 事件收听器,状态更改处理器,以及小帮助器都是核心中的召回.

忘记 `@callback` 是常见的错误 。 Home Assistant 然后将该函数当作屏蔽并用线程运行, 其中调用 `async_` APIs不是线性安全。 见[线程安全](/core/internals/thread-safety).

### 基本函数 Thread {#thread-safe-functions}

只计算如`sum()`或合并两个词典的函数在任何地方都是安全的. 没有标记 当怀疑时,阅读其执行情况。

### 其他的都一样 {#everything-else}

作用于I/O,睡眠,或不已知是安全的. 他们不能跑在事件循环。 在执行器中运行它们。

## 将屏蔽工作移至执行器 {#move-blocking-work-to-the-executor}

执行器是用于屏蔽代码的线程集合. 从事件循环中, 用 `hass.async_add_executor_job` 将一个函数交给它并等待结果 :

```python
data = await hass.async_add_executor_job(client.get_status)
```

参数在函数之后。 对于关键词参数,请在 `functools.partial` 中包裹调用:

```python
from functools import partial

data = await hass.async_add_executor_job(
    partial(client.get_status, include_history=True)
)
```

存在时优先使用ASync库. 执行者线程比皮层要贵得多,游泳池也不是无限的. 见[阻断操作](/core/internals/blocking-operations) 调用 Home Assistant 检测, 和怎么办 。

## 要求对背景开始工作 {#start-work-in-the-background}

在不等待的情况下启动胸围,创建一个任务. 在集成中,使用配置条目上的方法,因此任务与条目的寿命挂钩:

```python
entry.async_create_background_task(
    hass, self._async_listen(), "my_integration listener"
)
```

- the profile. `entry.async_create_task(hass, coro)`和 `hass.async_create_task(coro)` 创建任务 Home Assistant 在启动时等待 。
- `entry.async_create_background_task(hass, coro, name)` 和 `hass.async_create_background_task(coro, name)` 创建一个任务, 用于一个长期运行的东西, 就像一个插座上的听众 。 它不能维持启动,在关闭时取消。 配置条目版本在卸载该条目时也被取消.

## 从线索调用 ASync 代码 {#call-async-code-from-a-thread}

有时你处于一个线条中, 就像一个同步库的回调, 并且需要调用一些 ASync。 使用同步版本的 API 如果有一个, 如 `hass.bus.fire` 而不是 `hass.bus.async_fire` 。 否则,在圈子上安排一个胸围,等待结果:

```python
import asyncio

def say_hello(hass: HomeAssistant, target: str) -> str:
    """Call async code from a thread and wait for it."""
    return asyncio.run_coroutine_threadsafe(
        async_say_hello(hass, target), hass.loop
    ).result()
```

> [!WARNING]
> 永远不要从事件循环中做到这一点:它陷入僵局。 当薛素本身使用执行器时要小心,因为这也会陷入僵局.

## 使您的代码同步 {#make-your-code-async}

如果您在进行一个仍然使用同步代码的集成, 这些是同步对应器 :

| 同步 | 自动同步 |
| --- | --- |
| `def setup(hass, config)` | `async def async_setup(hass, config)` |
| 关于一个实体的`def update(self)` | `async def async_update(self)` |
| `def turn_on(self, **kwargs)` | `async def async_turn_on(self, **kwargs)` |

实体属性从事件环读取. 在属性中绝不使用 I/O : 获取更新方法或 [协调员](/glossary/coordinator) 中的数据, 并返回您存储的内容 。

## 早发现错误 {#find-mistakes-early}

开发时打开调试模式 。 它让 Home Assistant 检查许多线程安全和阻塞错误, 用堆栈跟踪报告它们 。 将此添加到 `configuration.yaml` :

```yaml
homeassistant:
  debug: true
```

您也可以以 Python 的 [ayncio 调试模式](https://docs.python.org/3/library/asyncio-dev.html#debug-mode) 开始 Home Assistant , 它报告从未等待过的皮层, 以及需要太长时间的召回 。
