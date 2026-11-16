---
title: 实体登记册
description: 查看您在实体注册簿中的整合实体, 当其独特的身份更改时, 移动它们 。
sidebarGroup: 设备与注册表
order: 2
---

# 实体登记册 {#entity-registry}

此页面涉及从您整合的代码中与实体注册处合作: 查找条目并迁移它们 。 实体如何进入登记册,以及决定实体和平台是启动启用、可见还是分类的[实体登记册](/core/entities/registry)。

实体注册会记住每个拥有 [唯一标识](/glossary/unique-id) 的实体 : 其实体 ID, 用户给它的名称和图标, 其区域, 是否禁用, 以及属于哪个配置条目和设备 。 你的实体最终会自己进去 只要他们有独一无二的身份证

## 获取注册 {#get-the-registry}

```python
from homeassistant.helpers import entity_registry as er

entity_registry = er.async_get(hass)
```

## 查找实体 {#look-up-entities}

```python
# The entity ID for a unique ID of your integration, or None {#the-entity-id-for-a-unique-id-of-your-integration-or-none}
entity_id = entity_registry.async_get_entity_id(
    "sensor", DOMAIN, f"{serial_number}_temperature"
)

# The registry entry for an entity ID {#the-registry-entry-for-an-entity-id}
entry = entity_registry.async_get(entity_id)

# All entities of a config entry {#all-entities-of-a-config-entry}
entries = er.async_entries_for_config_entry(
    entity_registry, config_entry.entry_id
)

# All entities of a device {#all-entities-of-a-device}
entries = er.async_entries_for_device(entity_registry, device_id)
```

。 使用它返回的实体ID:从不自己建立实体ID,用户可以更改它们.

## 移动独有的ID {#migrate-unique-ids}

特殊身份证明不得更改. 当他们不得不这样做时,例如因为旧的不够独特,就迁移登记条目,所以用户保留他们的实体ID,名称和自动化. 在 `async_migrate_entry` 中做到这一点, 并加上 [那个配置条目版本](/core/integrations/config-entries#migrate-a-config-entry) 的凸起 :

```python
from typing import Any

from homeassistant.core import callback
from homeassistant.helpers import entity_registry as er

async def async_migrate_entry(
    hass: HomeAssistant, entry: ExampleConfigEntry
) -> None:
    """Migrate an old config entry."""
    if entry.version == 1:

        @callback
        def _migrate_unique_id(
            entity_entry: er.RegistryEntry,
        ) -> dict[str, Any] | None:
            """Prefix unique IDs with the serial number."""
            if entity_entry.unique_id.startswith(entry.unique_id):
                return None

            return {
                "new_unique_id": f"{entry.unique_id}_{entity_entry.unique_id}"
            }

        await er.async_migrate_entries(
            hass, entry.entry_id, _migrate_unique_id
        )

        hass.config_entries.async_update_entry(
            entry, version=2, minor_version=1
        )
```

这是一个主要版本的凸起, 因此设置 `VERSION = 2` 在您的配置流上 。 旧代码如果不知道新的唯一ID,在降级后将找不到它的实体,并再次创建它们. 这个例子建立在配置条目的独特ID上,所以它假设每个条目都有一个.

`async_migrate_entries` 为配置条目的每个注册条目调用您的功能 。 返回 `async_update_entity` 或 `None` 的更改词典, 以保留条目 。

## 更新或删除条目 {#update-or-remove-entries}

`entity_registry.async_update_entity(entity_id, ...)` 更改一个注册项, `entity_registry.async_remove(entity_id)` 删除它 。 一体化很少需要它们。 使用它们来清理, 就像删除一个功能的实体 您的整合不再提供。 属于妈妈用户的设置,如名称、区域以及实体是否被禁用或隐藏,不是要更改的。
