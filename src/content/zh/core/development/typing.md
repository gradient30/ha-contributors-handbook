---
title: 类型提示
description: '{ 他会如何使用类型提示和 mypy, 以及如何选择一个模块来严格检查 。'
sidebarGroup: 写代码
order: 3
---



# 类型提示 {#type-hints}
类型提示让下一个人更容易理解代码,它们让[神秘点](https://mypy.readthedocs.io/)在用户之前找到错误. 核心检查每个模块与神秘, 在Git钩和CI。

## 所需内容 {#what-is-required}

类型提示尚未在每次整合中都要求,但受到大力鼓励,目标是全覆盖. 在测试中,审查人员确实期望它们:给一个测试函数的每个参数一个类型,更喜欢像`HomeAssistant`或`MockConfigEntry`这样的混凝土类型,而不是`Any`.

```python
async def test_setup(
    hass: HomeAssistant,
    mock_config_entry: MockConfigEntry,
) -> None:
    """Test setting up the integration."""
```

Python 3.14 评估注解懒散,因此可以指在文件下方被进一步定义的类,不用引用.

## 向未键入代码添加提示 {#adding-hints-to-untyped-code}

打入一个完全没有提示的模块是一大堆工作. {L砂 } 可以做第一个通过: 它在测试运行时监视呼叫, 并推荐来自它所看到的类型的提示. Core有这个剧本 MonkeyType不是默认安装的,所以首先用`uv pip install monkeytype`安装.

1. 在 MonkeyType 下运行您的模块测试 :

```shell
   script/monkeytype tests/components/example/test_sensor.py
   ```

2. 看它暗示的提示,与 `monkeytype stub homeassistant.components.example.sensor` 。
3. 如果看起来合理,请使用 `monkeytype apply homeassistant.components.example.sensor` 。
4. 检查diff 并修复它有什么问题。 它只知道测试使用的类型

这在没有任何提示的模块上效果最好. 应用到一个已经有一些的模块中可能会失败.

## 严格检查 {#strict-checking}

默认情况下, mypy 接受只有部分输入的代码. 一个完全输入的模块可以选择严格检查,在缺少提示和 `Any` 爬入时也会失败.

要选择加入,请将模块."到寄存器根部的`.strict-typing`文件中,按字母顺序排列。 对于一个集成,就是类似`homeassistant.components.example.*`的线条. 然后运行繁忙更新 `mypy.ini` :

```shell
python3 -m script.hassfest -p mypy_config
```

提交两个文件 。 [整合质量尺度](/core/quality-scale) 的白金级上的整合必须严格输入 。

## 帮助类型检查器 {#helping-the-type-checker}

有时你比类型检查器更了解. 例如,在一般情况下,一个值可以是`None`,但是在代码的这个时刻从来没有. 在 `TYPE_CHECKING` 块内用 `assert` 缩小类型, 因此它只为类型检查器存在, 并且从未运行 :

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    assert self.coordinator.data is not None
```

只有在修改说明本身不可能或非常繁琐时才这样做。
