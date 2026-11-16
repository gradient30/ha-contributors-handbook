---
title: 教益
description: 通过将存储状态重新变成行动呼叫, 让场景与您实体整合的实体一起工作 。
sidebarGroup: 集成功能
order: 7
---

# 教益 {#reproduce-state}

A [场景](/glossary/scene)存储了一组实体的状态,比如"客厅灯光的30%和温暖的白色". 当一个场景被激活时,Home Assistant必须让那些状态回归现实,通过称正确行动. 它要求整合每个实体领域以做到这一点。

这是针对实体集成的,比如`light`或`climate`:定义实体类型及其行动的集成. 只提供现有类型实体的集成,如光线平台,并不需要.

## 珂 添加支持 {#add-support}

最快捷的方式是脚手架脚本:

```shell
python3 -m script.scaffold reproduce_state
```

以 `async_reproduce_states` 创建 `reproduce_state.py` :

```python
from collections.abc import Iterable
from typing import Any

from homeassistant.core import Context, HomeAssistant, State

async def async_reproduce_states(
    hass: HomeAssistant,
    states: Iterable[State],
    *,
    context: Context | None = None,
    reproduce_options: dict[str, Any] | None = None,
) -> None:
    """Reproduce the given states."""
```

对于每个状态,将其与实体的当前状态比较,如果它们已经匹配就跳过,并调用使实体到达存储状态和属性的动作. 传`context`到动作呼叫,所以变化与场景相连. 记录无法复制的状态的警告, 如无效的状态值, 然后跳过它们 。 运行状态平行, 例如与 `asyncio.gather` 并行运行, 因此快速应用了多个实体的场景 。

`reproduce_state.py` [切换集成](https://github.com/home-assistant/core/blob/dev/homeassistant/components/switch/reproduce_state.py) 的 `reproduce_state.py` 是一个简短的完整的例子 。
