---
title: 代码风格
description: Python在Home Assistant Core中的样式规则。 格式、文件串、记录、错误处理和公约审查人员寻找。
sidebarGroup: 写代码
order: 2
---



# 代码风格 {#code-style}
核心是一个庞大的密码库,有上千名贡献者. 一种一致的风格使得它可以被所有的人读取. 大部分规则都是用工具执行的,所以你不必记住. 其余是审查人员将指出的公约。

## 格式化和折叠 {#formatting-and-linting}

您不手工格式化代码,也没有样式指南可以记住:工具决定.

- [鲁夫](https://docs.astral.sh/ruff/) 格式化所有代码, 以及它的linter 抓住大多数问题, 包括您的导入顺序 。 Docstrings跟随Google会议,Ruff也检查过.
- [Py](https://pylint.readthedocs.io/) 用为Home Assistant 写的一组检查, 捕获图案 Ruff 无法看到 。

两人在犯罪时都会逃跑 再在CI里▪ 不通过它们的pull request是不合并的。▪ 如何自己运行。

核心需要Python3.14或更新,所以使用它所提供的. 您不需要 `from __future__ import annotations` (Ruff even block it), 注释中的前置引用不需要引用 。

## 文件串和评论 {#docstrings-and-comments}

每个模块,类,和功能都有一个docstring. 文件顶端的docstring 表示文件的内容:

```python
"""Support for Example sensors."""
```

键入提示文档函数的参数。 当一个函数需要更多的解释时,请使用 [谷歌风格](https://google.github.io/styleguide/pyguide.html#383-functions-and-methods) , 并且不列出类型: 类型已经在签名中 。

```python
def calculate_dew_point(temperature: float, humidity: float) -> float:
    """Calculate the dew point.

    Args:
        temperature: The temperature in degrees Celsius.
        humidity: The relative humidity, in percent.

    Raises:
        ValueError: If the humidity is not between 0 and 100.
    """
```

评论是满句,以一段时间结束。 保持简短,用它们来解释 "为什么,从来没有" "什么":代码已经说了它做了什么。 不要把代码留下 Git记得它。

## 顺序和常数 {#order-and-constants}

- 保持常数,以及列表和词典的内容,在顺序无关紧要时按字母顺序排列.
- 经常在 `const.py` 中使用一个以上的模块,并从中导入。 一个恒定模块只使用一个留在该模块中.
- 用常数替换魔法字符串 。

## 日志 {#logging}

伐木机已经添加整合名称,不要在电务. 和syslog消息一样,日志消息不会以周期结束.

```python
_LOGGER.error("No route to device: %s", self._resource)
```

```text
ERROR [homeassistant.components.example] No route to device: 10.0.0.8
```

- 使用 `_LOGGER.debug` 用于任何不是针对用户的 。 当心`_LOGGER.info`。
- 使用 `_LOGGER.error` 只用于用户应该操作的东西, 和`_LOGGER.warning` 当某事起作用时, 但不完全使用 。 需要离线的设备,而不是错误。
- 永远不要登录 API 密钥、 令牌、 用户名或密码 。 甚至没有错的

## 字符串格式化 {#string-formatting}

使用 f 字符串, 而不是 `%` 或 `str.format` :

```python
name = f"{device_name} {sensor_name}"
```

伐木是例外。 传递这些值为参数, 因此信件只有在实际登录时才会格式化 :

```python
_LOGGER.info("Can't connect to %s at %s", service, host)
```

## 章 {#error-handling}

- 只检查您期望的例外, 如您的库的连接和 API 错误 。 不要使用 `except Exception:` 。 一个被接受的地方是配置流程步骤的最后一个 `except`,它用 `_LOGGER.exception` 记录出乎意料的错误,并显示 `unknown` 错误, 就像脚手架生成的 。
- 保持`try`小块。 只要把线 能够提高你的例外。
- 更喜欢早归于深筑巢:`if not condition: return`.
- 当验证保证键存在时,使用`data["key"]`,而不是`data.get("key")`. 缺失的密钥是错误, 它应该显示 。
- 不添加已验证的动作计划输入检查 。

当动作失败时, 当输入错误时, 将 `HomeAssistantError` 或 `ServiceValidationError` 升起, 因此用户会在界面中看到错误 。 不要同时登录, 信件已经登录 。

```python
async def async_turn_on(self, **kwargs: Any) -> None:
    """Turn on the switch."""
    try:
        await self.device.turn_on()
    except DeviceConnectionError as err:
        raise HomeAssistantError(f"Failed to turn on: {err}") from err
```

## 使用断言 {#using-assert}

Python 与 `-O` 一起运行时盎然删除 `assert` 语句, 因此它们不是用于运行时的检查 。 在测试中使用它们,并帮助类型检查器缩小一个类型. 这样的话, turbine  put } }

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    assert self.client is not None
```

## 架构 {#structure}

- 使用数据类来传递周围的相关值,而不是Tuple或字典.
- 不在两个地方存储相同的值 。
- 实体使用`_attr_`属性, 如`_attr_native_value`, 而不是属性, 除非读取时必须计算值 。
- 改变配置或具有安全影响的行动需要一名管理员。 以 `async_register_admin_service` 注册 。
- 集成不包含`.gitignore`文件 。

不知该怎么看? 查看 [整合质量尺度](/core/quality-scale) 的白金或黄金级上的整合 。 等级为`manifest.json`。
