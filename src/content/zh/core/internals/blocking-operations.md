---
title: 封锁行动
description: 如何继续屏蔽 I应享有的I/O 并慢化事件循环的导入,以及如何修复屏蔽调用 Home Assistant 报告 。
sidebarGroup: 自动同步
order: 12
---

# 封锁行动 {#blocking-operations}

在 [事件循环](/glossary/event-loop) 中一个屏蔽呼叫会拖住 Home Assistant 的全部, 直到它返回 。 网络I/O,磁盘I/O,睡眠,重计算全部块. 在执行器中执行它们,或者使用同步替代.

Home Assistant在事件循环中检测到许多阻断呼叫,并在日志中报告,其中包含集成和发出该呼叫的行. 其中两个, `sleep` 和`putrequest` 也停止了 : 调用产生 `RuntimeError` 而不是运行 。 如果你从这样的报告来到这里, 在下面的列表中找到你的电话。

## 在执行器中运行屏蔽代码 {#run-blocking-code-in-the-executor}

内皮内皮 提 人

```python
import asyncio
from functools import partial

# In Home Assistant {#in-home-assistant}
result = await hass.async_add_executor_job(blocking_code, "something")
result = await hass.async_add_executor_job(
    partial(blocking_code_with_kwargs, kwarg=True)
)

# In library code {#in-library-code}
loop = asyncio.get_running_loop()
result = await loop.run_in_executor(None, blocking_code, "something")
```

读 Python 在 [运行屏蔽代码](https://docs.python.org/3/library/asyncio-dev.html#running-blocking-code) 上的笔记, 用于陷阱 。

## 调用 Home Assistant 检测 {#calls-home-assistant-detects}

### 文件系统: 打开、 g Northeastb、 行走、 列表dir、 扫描dir 和 pathlib 读写 {#file-system-open-glob-walk-listdir-scandir-and-pathlib-reads-and-writes}

`open`,`glob.glob`,`glob.iglob`,`os.walk`,`os.listdir`,`os.scandir`,以及`pathlib.Path`方法,如`read_text`,`read_bytes`,`write_text`,和`write_bytes`都做磁盘 I/O。在执行器中运行。 调用 Home Assistant 也不检测, 如 `os.stat` 或 `os.path.exists` 。

> [!WARNING]
> Home Assistant 只检测到 `open` 的呼叫, 而不是它之后的文件上的读写 。 将 `open` 移动到执行器中时, 将读数移动并随其写入其中 。 一个只移动 `open` 的固定装置, 留下阻挡 I/O 的位置, 长时间内没有人会注意到 。

### 睡觉 {#sleep}

将`time.sleep`替换为`await asyncio.sleep`。 一个共同的阻塞睡眠来源是`pyserial-asyncio`. 使用 [`serialx`](https://github.com/puddly/serialx) 代替 : 它有本地的 Ayncio 支持, 并且与 `serial`, `serial_asyncio` 和 `serial_asyncio_fast` 兼容 。 见 [从 pyserial 迁移到序列x](https://contributors.home-assistant.io/blog/2026/04/27/pyserial-to-serialx/) 。

### 请求 {#putrequest}

`http.client` 和它上建的任何东西, 如 `urllib` 和 `requests` , 都会屏蔽网络 I/O。 在执行器中运行它, 或者更好, 切换到像 `aiohttp` 一样的 Aync HTTP 客户端 。

### SSL: 负载 默认 证书, 负载 验证 地点, 负载  cert 链条, 设置  默认  验证  路径 {#ssl-loaddefaultcerts-loadverifylocations-loadcertchain-and-setdefaultverifypaths}

创建 SSL 上下文从磁盘读取证书 。 不要创建自己的: 使用共享客户端和上下文 Home Assistant 在事件循环之外已经准备的 。

- 对`aiohttp`:`async_get_clientsession(hass)`从`homeassistant.helpers.aiohttp_client`。
- 对`httpx2`:`get_async_client(hass)`从`homeassistant.helpers.httpx_client`。
- 其它的: `homeassistant.util.ssl` 中的助手, 如`get_default_context()` 。

### 导入模块 {#importmodule}

钳子从磁盘中导入模块读取 。钳子:

## 进口 {#imports}

导入需要注意有两个原因:一个导入从磁盘的可持续读取文件,磁盘会块化,而CPython的导入是[无线条安全](https://github.com/python/cpython/issues/83065).

### 在模块一级导入 {#import-at-module-level}

如果您的集成导入了它最顶端的模块, 而 `__init__.py` 导入它所需要的模块, 您就没有什么可担心的 。 Home Assistant 在事件循环开始前加载您的集成, 或在导入执行器中: 一个仅用于导入的单独线程 。

这对几乎所有的一体化都是正确的选择。

### 稍后再导入,小心 {#import-later-carefully}

有时只在罕见的情况下需要模块,或者顶层导入会oncle time导入. 然后说:

- 如果模块已经装入, 则一个 plain 仍旧 `import` 语句是好的 : Python 不再装入它 。
- 如果模块只导入到一个地方, 请将导入放入函数中, 用 `hass.async_add_executor_job` 运行 。
- 如果模块可能同时从不同地点导入,请使用`async_import_module`从`homeassistant.helpers.importlib`导入. 它缓存结果,使同时进口的商品互相等待。

```python
from homeassistant.helpers.importlib import async_import_module

module = await async_import_module(
    hass, f"homeassistant.components.my_integration.{name}"
)
```

要检查模块是否装入, 请查看 `sys.modules` 。 装入 * starts * 后立即出现一个模块, 因此从几个路径导入, 请记住比赛条件 。

### 仅导入类型检查 {#imports-only-for-type-checking}

如果您只需要导入类型提示, 请守护它, 因此它不会在运行时导入 :

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from some_library import SomeClass

def some_function() -> SomeClass:
    ...
```

### 很少使用的代码 {#rarely-used-code}

导入成本为CPU时间和磁盘 I/O,一旦装入内存. 对于偶尔才需要的代码,只要遵循上述规则,晚进口就可能更好。

## 提前查找阻断呼叫 {#find-blocking-calls-early}

开发时打开调试模式,在`configuration.yaml`的`debug: true`下打开`homeassistant:`,用Python的[ayncio 调试模式](https://docs.python.org/3/library/asyncio-dev.html#debug-mode)运行。 这两种阻塞电话,否则只会作为一个缓慢的系统出现。
