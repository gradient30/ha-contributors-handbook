---
title: 区域登记册
description: 对上述区域有什么了解,以及您如何为设备提供整合建议。
sidebarGroup: 装置和登记册
order: 3
---

# 区域登记册 {#area-registry}

区登记簿记录[区域](/glossary/area):家中的实际位置,如厨房或车库。 用户将设备和实体放置在区域,以及区域上[楼层](/glossary/floor).

区域属于用户. 您的整合不会创造或改变它们。 它能做的是给新设备建议一个区域,在`DeviceInfo`中的`suggested_area`或`async_get_or_create`中的`suggested_area`。 当设备或服务知道它位于哪个房间时使用它,就像它自己的应用程序中设置的一个房间名称.

## 区域属性 {#area-properties}

| 财产 | 这是什么 |
| --- | --- |
| `id` | 为区域生成的 ID 再见 Home Assistant |
| `name` | 区域名称 |
| `aliases` | 我去取这个区域的其他名称,例如语音命令 |
| `floor_id` | 地上那个区域 |
| `icon` | 区域图标 |
| `picture` | 地区图 |
| `labels` | 区域的标签 |
| `temperature_entity_id` | 给出区域温度的实体 |
| `humidity_entity_id` | 给予该地区湿度的实体 |
| `created_at`, `modified_at` | 当区域创建和上次更改时 |

## 阅读区域 {#read-areas}

```python
from homeassistant.helpers import area_registry as ar

area_registry = ar.async_get(hass)
area = area_registry.async_get_area(area_id)
```

一个没有自己的区域的实体在其装置的区域。 要获取申请区域, 请为实体使用 `er.async_get_effective_area_id(hass, entity_entry)` , 或为设备使用 `dr.async_get_effective_area_id(hass, device)` 。
