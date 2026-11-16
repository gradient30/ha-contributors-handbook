---
title: 你集成中的分析
description: 对于开发者来说，了解你的集成如何在分析中显示，以及如何将设备或实体排除在设备数据库之外。
order: 4
---


# 你集成中的分析 {#analytics-in-your-integration}
大多数集成不需要为分析做任何操作。Home Assistant 报告哪些集成被使用，并且对于设备数据库，从设备和实体注册表中收集设备信息。本页面适用于你希望对此进行控制的情况。

## 关于你的集成报告的内容 {#what-is-reported-about-your-integration}
- **使用分析** 会报告你的集成在使用时的域。自定义集成会通过其清单中的域和版本进行报告。
- **设备数据库** 仅包括其清单中具有 `device` 或 `hub` 的内置集成。具有条目类型 `service` 的设备始终被排除在外。

对于每个设备，快照包含制造商、型号、型号 ID、硬件和软件版本、是否有配置 URL 以及设备连接的方式。对于每个实体，它包含域、原始设备类别、实体类别、计量单位、是否有实体名称，以及其状态是否为假定状态。请参见 [分析是如何工作的](/data/how-it-works#the-device-database)。

## 排除设备或实体 {#leave-devices-or-entities-out}
有时，一个集成的设备信息并不能反映真实硬件，或者在设备数据库中会产生误导。这时，集成可以添加一个 `analytics.py` 平台，并提供一个 `async_modify_analytics` 函数。Home Assistant 使用集成的设备 ID 和实体 ID 调用它，并用返回结果来过滤快照。

排除整个集成：

```python
"""Analytics platform."""

from homeassistant.components.analytics import (
    AnalyticsInput,
    AnalyticsModifications,
)
from homeassistant.core import HomeAssistant

async def async_modify_analytics(
    hass: HomeAssistant, analytics_input: AnalyticsInput
) -> AnalyticsModifications:
    """Modify the analytics."""
    return AnalyticsModifications(remove=True)
```

或者只排除某些设备或实体，使用 `DeviceAnalyticsModifications` 和 `EntityAnalyticsModifications`：

```python
"""Analytics platform."""

from homeassistant.components.analytics import (
    AnalyticsInput,
    AnalyticsModifications,
    EntityAnalyticsModifications,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers import entity_registry as er

async def async_modify_analytics(
    hass: HomeAssistant, analytics_input: AnalyticsInput
) -> AnalyticsModifications:
    """Leave out entities that only exist for diagnostics."""
    entity_registry = er.async_get(hass)
    entities = {}

    for entity_id in analytics_input.entity_ids:
        entry = entity_registry.async_get(entity_id)
        if entry and entry.translation_key == "debug_info":
            entities[entity_id] = EntityAnalyticsModifications(remove=True)

    return AnalyticsModifications(entities=entities)
```

移除设备也会移除其实体。

如果该函数引发异常或返回的不是 `AnalyticsModifications`，Home Assistant 将排除整个集成，并记录错误。

## 核心中的示例 {#examples-in-core}
ESPHome、移动应用和 WLED 都有分析平台。查看它们在 [核心仓库](https://github.com/home-assistant/core/tree/dev/homeassistant/components) 中的 `analytics.py`，获取真实示例。

关于构建集成的其他所有内容，请参阅 [核心和集成](/core)。
