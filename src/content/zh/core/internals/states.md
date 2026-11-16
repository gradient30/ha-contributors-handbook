---
title: 状态
description: 状态机器如何保持每个实体的当前状态,状态对象持有什么,以及集成为什么通过实体来写入状态.
sidebarGroup: 核心
order: 3
---

# 国家 {#states}

`hass.states`上的状态机器在Home Assistant中持有每个实体的当前状态. 盘子读它, 自动化触发它, 录音机存储每一个变化。 这是一个简单的商店,几乎没有规则,这是故意的。

## 通过实体写入状态 {#write-states-through-entities}

首先:作为一个集成开发者,你几乎从来没有自己给国产机器打电话. 您创建 [实体](/core/entities), 实体基础类用 `async_write_ha_state()` 来写他们的状态 。 它负责实体ID,名称,单位,图标,设备类,可用性,以及每个实体的属性. 手写状态跳过所有这一切,用户无法重命名、隐藏或配置您所写的内容 。

读下去了解下面的情况

## 78. 状态对象 {#the-state-object}

增进状态是一个 `State` 对象来自 `homeassistant.core` 。 国家是不可改变的:改变会产生一个新的目标。

| 属性 | 说明 |
| --- | --- |
| `entity_id` | 报表一 实体 ID, 如 `light.kitchen_ceiling` : 域, 点, 和对象 ID 。 |
| `domain` | 点前的部分,如`light`. |
| `object_id` | 点自由地 。 |
| `state` | 状态本身,总是最多255个字符的字符串,如`on`或`21.5`. |
| `attributes` | 只读字典，存放额外信息。请保持可 JSON 序列化。|
| `last_changed` | 当`state`最后一次更改时。 |
| `last_updated` | 当 `state` 或任何属性上次更改时 。 |
| `last_reported` | 州上书时,虽无改. |
| `context` | 导致这个状态的`Context`。 |
| `name` | 友好名称, 从 `friendly_name` 属性, 或其他带有下划线空格的对象 ID 。 |

[home-assistant.io上的状态对象页面](https://www.home-assistant.io/docs/configuration/state_object/) 从用户侧描述相同的对象 。

## 读取状态 {#read-states}

```python
state = hass.states.get("sun.sun")
if state is not None:
    elevation = state.attributes.get("elevation")
```

- `hass.states.get(entity_id)` 如果实体不存在, 返回 `State` 或 `None` 。 总是处理`None`: 实体来去.
- `hass.states.async_all(domain)` 返回所有状态, 或一个或多个域的所有状态 。
- `hass.states.async_entity_ids(domain)`只返回实体ID。
- 在这里可以比较。

记住状态也可以是`unavailable`或`unknown`. 常数 `STATE_UNAVAILABLE` 和 `STATE_UNKNOWN` 生活在 [`homeassistant/const.py`](https://github.com/home-assistant/core/blob/dev/homeassistant/const.py) 。

## 写入状态 {#write-states}

`hass.states.async_set(entity_id, state, attributes)` 创建或替换状态 。 接下来会发生什么取决于什么变化:

- **状态或属性改变**:状态机器存储一个新的`State`,并在其数据中以`entity_id`,`old_state`和`new_state`来点燃`state_changed`事件. `last_changed` 只有在 `state` 本身改变时才会移动 。
- ** 无变化**: 状态机器更新 `last_reported` 并发射 `state_reported` 事件代替 。 聆听 `state_reported` 需要 `event_filter` , 因为它发射很多。
- QQH0}**:即使没有改变,一个 `state_changed` 事件也会发射, 而`last_changed` 也会移动 。

在这些头衔中, 在这些头衔上,

`hass.states.async_remove(entity_id)` 删除状态并点火 `state_changed` 事件 `new_state` 设定为`None` 。 聆听者必须预料到这一点,当一个实体是新的时,`old_state`是`None`也是同样的情况。

就像从`async_`开始的一切一样,这些必须运行在事件循环中. 从另一个线程, 使用 `hass.states.set` 和 `hass.states.remove` 。

## 实体 Tulm 的额外属性 {#extra-attributes-on-your-entity}

在实体上,额外信息会在`extra_state_attributes`属性中进行. 它返回一个词典, 最终以 `attributes` 结尾 。

```python
@property
def extra_state_attributes(self) -> dict[str, Any]:
    """Return extra attributes of the entity."""
    return {"filter_life": self._filter_life}
```

不要覆盖 `state_attributes`: 实体基础类, 像光一样, 用它来表示其域的属性 。 在你加入属性之前再想想 每个属性与每个状态变化一起存储,一个变化的值往往属于自己的实体. 详情见[实体](/core/entities)。
