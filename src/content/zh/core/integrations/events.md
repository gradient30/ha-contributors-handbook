---
title: 整合中的事件
description: 向用户提供您设备的事件, 并与事件帮助者对 Home Assistant 内部发生的事情作出反应 。
sidebarGroup: 数据与更新
order: 2
sidebarLabel: 傀儡
---

# 整合中的事件 {#events-in-integrations}

在 Home Assistant 中发生的一切都会翻过事件总线:状态变化,动作呼叫,以及 Home Assistant 本身的开始和停止. 您的整合可以将自己的 [事件](/glossary/event) 放到公共汽车上, 它可以听到发生的事情。

此页面涉及在您整合时使用事件 。 巴士如何在下面工作, 比如事件对象如何维持, 听者如何运行, 以及事件过滤器, 都在 [核心工作如何:活动](/core/internals/events) 上 。

## 提供设备事件 {#make-device-events-available}

许多设备有非状态的事件:按下按钮,检测到运动,门铃响.

首选方式是 [事件实体](/core/entities/event) 。 用户可以在一个地方找到一个设备的所有事件,并像其他任何实体一样在自动化中使用.

### 公共汽车上的火灾事件 {#fire-events-on-the-bus}

一些整合直接在活动总线上进行火灾事件. 命名事件类型`<domain>_event`, 如`zha_event`, 并在事件属于设备时从 [设备注册](/core/integrations/device-registry) 添加 `device_id` :

```python
hass.bus.async_fire(
    "example_event",
    {
        "device_id": device_entry.id,
        "type": "button_pressed",
    },
)
```

如果一个设备只点火事件而没有实体, [在设备注册中自行注册](/core/integrations/device-registry#register-a-device-yourself), 所以有一个设备可以附加事件 。

少数规则:

- 将您设备的事件转换为 Home Assistant 从集成设置( `async_setup_entry` in `__init__.py`) 中的事件, 而不是实体代码 。
- 别和州里发生假事件 按钮将提供 `on` 后30 秒的二进制传感器不是事件 。
- 用户发现巴士事件很难发现. [设备触发器](/core/integrations/device-automations)曾经是集成使其可见的方式,但新设备自动化已不再被接受. 使用事件实体 。

## 聆听 Home Assistant {#listen-to-home-assistant}

您的整合可能需要在 Home Assistant 内出事时采取行动 。 在 `homeassistant.helpers.event` 中使用帮助器, 当符合时: 它们被优化为只为您所关心的更改调用您的代码, 这在一个有数千个实体的系统中很重要 。 只有在没有帮手时才直接听巴士.

每个帮助者返回一个删除听众的函数. 用 `entry.async_on_unload` (或 `self.async_on_remove`) 在一个实体中注册, 所以当配置条目卸载时, 听众会停止 :

```python
from homeassistant.core import Event, EventStateChangedData, callback
from homeassistant.helpers.event import async_track_state_change_event

@callback
def _async_outside_temperature_changed(
    event: Event[EventStateChangedData],
) -> None:
    """React to a new outside temperature."""
    if (new_state := event.data["new_state"]) is None:
        return
    ...

entry.async_on_unload(
    async_track_state_change_event(
        hass, ["sensor.outside_temperature"], _async_outside_temperature_changed
    )
)
```

大多数帮助者也存在于没有`async_`前缀的情况下,用于不运行在事件循环中的代码.

### 对其他国家的更改 {#state-changes}

| 帮助者 | 用它来 |
| --- | --- |
| `async_track_state_change_event` | 跟踪特定实体的状态变化 |
| `async_track_state_added_domain` | 跟踪添加到一个或多个域的实体 |
| `async_track_state_removed_domain` | 跟踪从就其一个或多个域删除的实体 |
| `async_track_state_change_filtered` | 使用过滤器跟踪状态变化, 您可以稍后更新 |
| `async_track_same_state` | 当实体在一段时间内保持状态时运行某事 |

### 模板 {#templates}

| 帮助者 | 用它来 |
| --- | --- |
| `async_track_template` | 当模板成真时运行某样东西 |
| `async_track_template_result` | 当模板结果改变时运行一些东西 |

### 出版物 {#registries}

| 帮助者 | 用它来 |
| --- | --- |
| `async_track_entity_registry_updated_event` | 跟踪特定实体的登记册变化 |
| `async_track_device_registry_updated_event` | 跟踪特定设备的登记更改 |

### 时间 {#time}

| 帮助者 | 用它来 |
| --- | --- |
| `async_call_later` | 慢一点再跑一次 |
| `async_track_point_in_time` | 一次跑一次,一个时间点 |
| `async_track_point_in_utc_time` | 在协调世界时的某个时间点运行一些东西 |
| `async_track_time_interval` | 每隔一段时间再运行一次 |
| `async_track_time_change` | 当本地时间匹配模式时运行某样东西 |
| `async_track_utc_time_change` | UTC 时间匹配图案时运行一些东西 |
| `async_track_sunrise` | 每天仍在进行 日出时的抵消 |
| `async_track_sunset` | 每天运行一些东西, 在日落的抵消 |

多数时候帮助者会用运行的瞬间调用您的功能, 作为 `datetime` 。 日出和日落的帮手们毫不争辩地称呼它. 注意参数的顺序 :可以为 `async_track_point_in_time(hass, action, point_in_time)` 和 `async_track_time_interval(hass, action, interval)` 先取您的功能, 但 `async_call_later(hass, delay, action)` 先取延迟, 数秒或作为 `timedelta` 。

如果您需要投票, 请使用 [协调员](/core/integrations/fetching-data) 而不是 `async_track_time_interval` 。

### 开始 Home Assistant {#start-of-home-assistant}

一旦 Home Assistant 开始运行, 请使用 `async_at_started` 从 `homeassistant.helpers.start` 运行 。 如果 Home Assistant 已经运行, 它会马上运行, 当用户稍后添加您的集成时就是这种情况 。 `async_at_start` 对较早的启动阶段也这样做 。

```python
from homeassistant.helpers.start import async_at_started

entry.async_on_unload(async_at_started(hass, _async_start_export))
```

## 直接听公交车 {#listen-to-the-bus-directly}

当没有帮助者时,请用 `hass.bus.async_listen` 来听总线, 或者, 对于一个只需要一次的事件, `hass.bus.async_listen_once` 。 两者都返回一个删除听众的函数.

```python
from homeassistant.const import EVENT_HOMEASSISTANT_STOP

entry.async_on_unload(
    hass.bus.async_listen_once(EVENT_HOMEASSISTANT_STOP, _async_disconnect)
)
```

`EVENT_HOMEASSISTANT_START`,`EVENT_HOMEASSISTANT_STARTED`,和`EVENT_HOMEASSISTANT_STOP`每跑一次才放火,所以`async_listen_once`对他们来说是正确的号召.

| 积极地濑子事件 | 当 |
| --- | --- |
| `EVENT_HOMEASSISTANT_START` | 各种不同设置已完成, Home Assistant 进入启动阶段 |
| `EVENT_HOMEASSISTANT_STARTED` | 所有整合都有机会加载。 语音助理和出口国的一体化经常使用。 |
| `EVENT_HOMEASSISTANT_STOP` | 进入停止阶段 |
| `EVENT_HOMEASSISTANT_FINAL_WRITE` | 将数据写入磁盘的最后机会 |
| `EVENT_HOMEASSISTANT_CLOSE` | 减产 |
| `EVENT_STATE_CHANGED` | 一个实体的状况发生了变化。 使用 [状态变化助手](/core/integrations/events#state-changes) 代替 。 |
| `EVENT_ENTITY_REGISTRY_UPDATED` | 实体登记变更。 使用 [登记助手](/core/integrations/events#registries) 代替 。 |
| `EVENT_COMPONENT_LOADED` | 集成完成装入 。 使用 `async_at_start` 代替 。 |
| `EVENT_SERVICE_REGISTERED`, `EVENT_SERVICE_REMOVED` | 已登记或删除的行动 |
| `EVENT_CALL_SERVICE` | 要求采取行动 |
| `EVENT_CORE_CONFIG_UPDATE` | 核心配置已 在这里更改 |
| `EVENT_THEMES_UPDATED` | 主题有所改变 |
