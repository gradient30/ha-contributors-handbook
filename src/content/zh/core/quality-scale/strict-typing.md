---
title: 使用严格的打字
description: 白金规则严格打字:整合后完全打字,并使用严格的神秘设置进行检查.
sidebarLabel: 严格打字
sidebarGroup: 铂金
order: 3
---

# 使用严格的打字 {#use-strict-typing}

这是白金规则 在`quality_scale.yaml`中,它被称为{叩头}}.

集成必须完全输入,并列出在核心的`.strict-typing`文件中,所以 mypy用严格的设置来检查. 它的库也必须打字,并按 [PEP 561号协议](https://peps.python.org/pep-0561/) 所述发送 `py.typed` 文件 。

## 为什么这很重要 {#why-it-matters}

Python在运行时不检查类型,所以错误的类型在用户面前作为错误出现. 类型提示让 mypy在代码合并前找到这些错误. 严格的模式使得 mypy在缺失提示上失败,所以没有东西会滑过未打字.

图书馆也很重要 没有 `py.typed` 文件, mypy 将库中的所有内容都当作 `Any` , 以及集成中所有触摸库的提示检查无任何内容 。

## 示例 {#example}

在 [核心存储器](https://github.com/home-assistant/core) 根部添加 `.strict-typing` 整合, 按字母顺序 :

```text
homeassistant.components.my_integration.*
```

并运行整合的迷信:

```shell
python3 -m script.hassfest -p mypy_config
mypy homeassistant/components/my_integration
```

通过严格的打字,在每一个地方都使用一个打入的配置条目:在`async_setup_entry`,`async_unload_entry`中,平台,诊断,和选项流. 如何定义它, 见[运行时间数据](/core/quality-scale/runtime-data) :

```python
type MyConfigEntry = ConfigEntry[MyClient]

async def async_setup_entry(
    hass: HomeAssistant, entry: MyConfigEntry
) -> None:
    """Set up My integration from a config entry."""
```

见 [输入](/core/development/typing) 核心如何使用类型提示和 mypy 。

## 如何检查 {#how-it-is-checked}

- Hasfest, 当规则是 `done` 时: 集成必须在 `.strict-typing` 中, 其表单中的每一项要求都必须发送 `py.typed` 文件, 或者有一个单独的 `types-` 根包 。 Hassfest 只能检查您环境中安装的要求, 即需要的版本 。
- hassfest,当规则为 `done` 时与 [运行时间数据](/core/quality-scale/runtime-data) : `async_setup_entry`, `async_unload_entry` 以及 `__init__.py` 中的其他切入点时, 平台, `diagnostics.py` 和选项流必须使用一个打入的配置条目, 命名为 `MyConfigEntry` 。
- Pylint 警告当一个协调员不使用集成(`home-assistant-coordinator-untyped-config-entry`)的输入配置条目时.
- Mypy在CI和Git钩中运行,在类型错误上失败.

## 例外 {#exceptions}

这一规则没有例外。

## 相关规则 {#related-rules}

- [运行时间数据](/core/quality-scale/runtime-data):在运行时间数据中存储运行时间数据。
