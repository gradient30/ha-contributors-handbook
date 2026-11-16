---
title: 重大变化
description: 告诉集成器导出数据, 如语音助理, 显示您实体类型事项的更改 。
sidebarGroup: 融合特征
order: 8
---

# 重大变化 {#significant-change}

Home Assistant不仅收集数据,它还将数据发送给其他服务,如GoogleAssistant和Alexa. 这些服务并不需要任何微小的变化。 失去0.1%充电的电池,或移动0.1度的温度,不值得发信息. 重要更改支持允许您的实体整合决定哪些更改很重要 。

这是针对定义实体类型的实体集成,如`sensor`或`light`.

## 珂 添加支持 {#add-support}

最快捷的方式是脚手架脚本:

```shell
python3 -m script.scaffold significant_change
```

以 `async_check_significant_change` 创建 `significant_change.py` :

```python
from typing import Any

from homeassistant.core import HomeAssistant, callback

@callback
def async_check_significant_change(
    hass: HomeAssistant,
    old_state: str,
    old_attrs: dict,
    new_state: str,
    new_attrs: dict,
    **kwargs: Any,
) -> bool | None:
    """Return whether the change is significant."""
```

返回 `True` 当变化是显著的, `False` 当它不是, `None` 当您不能告诉。 Home Assistant 对待 `None` 如 `True` : 只过滤 `False` 。

有几个事情要知道:

- `old_state`是最后一个被认为重要的州,而不是以前的州. 在某一时刻,小的变化加起来变得重要。
- 考虑所有你知道的属性, 不只是国家。
- 使用 [设备类](/glossary/device-class) 来区分不同的实体: 对温度很重要的东西对电池不重要 。
- Home Assistant为你处理`unknown`和`unavailable`。
