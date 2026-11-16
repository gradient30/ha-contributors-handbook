---
title: 更新状态
description: 不偏不倚地报告可用性。
sidebarLabel: 更新状态
sidebarGroup: 基础
order: 3
---

# 更新状态 {#updating-state}

实体镜像 Home Assistant 之外的东西 : 设备, 云服务, 文件 。 一定有东西能保持两者同步 这样做有两种方法: Home Assistant 在时间表(polling)上向实体询问消息, 或者实体告诉Home Assistant 当某事改变(push)时.

当设备支持时推就更好. 变化马上出现, 没有人发出什么请求。 设备或服务只回答问题时投出.

## 投票 {#polling}

[投票](/glossary/polling) 是默认 :`should_poll` 是`True` 。 Home Assistant在固定间隔时调用实体的更新方法,然后写状态 。 执行其中一项:

```python
class ExampleSensor(SensorEntity):
    async def async_update(self) -> None:
        """Fetch the latest value from the device."""
        self._attr_native_value = await self._device.read_temperature()
```

只有 我可不会用 `update()` 代替徘徊在您的库同步时 。 Home Assistant然后用线条运行它给你。  只有 我可不会这样认为。

### 投票间隔 {#polling-interval}

间隔来自您整合的平台模块 `SCAN_INTERVAL`, 如 `sensor.py` :

```python
from datetime import timedelta

SCAN_INTERVAL = timedelta(minutes=5)
```

没有它,就使用域的默认值,比如传感器和开关的默认值为30秒,或者没有设置域的默认值为15秒. 当更新需要超过10秒时, Home Assistant 记录一个警告 。 选择设备的间隔或API可以舒适地处理.

### 并行更新 {#parallel-updates}

{开放供使用>在平台模块中限制该平台有多少实体同时更新或运行一个动作:

```python
# One request at a time: the device can't handle more {#one-request-at-a-time-the-device-cant-handle-more}
PARALLEL_UPDATES = 1
```

没有它,添加的平台的第一个实体决定整个平台的限值:1当它有同步的`update()`方法,没有其他限制. `0`也意味着没有限制。

### 通过协调员投票 {#polling-through-a-coordinator}

当一个请求返回许多实体的数据时,每个实体单独投票是浪费。 使用 [协调员](/glossary/coordinator) 代替 : 它每间隔获取一次数据, 而其实体( 基于 `CoordinatorEntity` ) 是当协调员有新数据时写入状态的推动实体 。 多数与少数受调查实体合并的做法都是这样。

## 推开 {#push}

对于推,将 `should_poll` 设置为 `False` , 在实体被添加时订阅您设备或库的更新, 并在信件到达时写入状态 。

```python
class ExampleSensor(SensorEntity):
    _attr_should_poll = False

    async def async_added_to_hass(self) -> None:
        """Subscribe to updates once the entity is added."""
        self.async_on_remove(
            self._device.subscribe(self._handle_update)
        )

    @callback
    def _handle_update(self, value: float) -> None:
        """Store the new value and write it."""
        self._attr_native_value = value
        self.async_write_ha_state()
```

`async_on_remove`当实体消失时,确保订阅被清理。 见[实体生命周期](/core/entities/lifecycle).

## 写入状态 {#writing-the-state}

这些方法将实体状态写入了国家机器. 挑一个适合你穿的线条

| 就在那时 | 用这个 |
| --- | --- |
| `async_write_ha_state()` | 从事件循环, 在您更改 `_attr_` 值后 。 这是你最常用的 它什么也没有拿. |
| `schedule_update_ha_state()` | 从另一个线程,像一个同步库的回调. 它在事件循环上安排写入. |
| `async_schedule_update_ha_state(force_refresh=True)` | 从事件循环, 当 Home Assistant 应先调用您的更新方法 。 |
| `schedule_update_ha_state(force_refresh=True)` | 同样,从另一个线。 |

从事件循环外部调用 `async_write_ha_state()` 不安全, 而 Home Assistant 报告 。 使用 `force_refresh=False` , `async_schedule_update_ha_state` 方法只是调用 `async_write_ha_state` 。

动作后写什么,像打开灯光一样,有它自己的部分:[在命令之后](/core/entities/state-updates#after-a-command).

### 已为您添加前更新 {#update-before-add}

将 `update_before_add=True` 传到 `async_add_entities` 在实体添加前一次调用更新方法, 因此它从真实数据开始, 而不是 `unknown` 。 然后,第一个状态被延迟到更新完成,这减缓了您的整合设置. 在设置时使用协调员获取第一个数据 。

## 在命令之后 {#after-a-command}

当用户打开灯光时,你的实体会向设备发送命令. 然后你有选择:立即显示新状态,或者等待设备确认. 立即写入预期状态称为 乐观更新 .

没有普遍正确的答案。 这取决于设备的表现:

- ** 设备将新状态推回。 ** 等着 本地设备的推更新确认瞬间内有变化,然后您所写的状态是真实的状态. 令后别写.
- 你调查一个报告其状态的装置。 不要等待下一个间隔: 在命令后请求刷新 。 与协调员,呼叫`await self.coordinator.async_request_refresh()`。 第一个请求立即刷新,10秒内更多的请求被分批为一个刷新. AirGradient集成(`airgradient/switch.py`)的开关是这样工作的.
- ** 该装置缓慢确认。 ** 云服务需要一段时间来反映变化,或者API你只能每隔几分钟投票,让用户看旧状态太久. 乐观的更新在这里是有道理的。 下一轮民意调查如果指挥部不坚持,则会纠正州.
- ** 设备完全不能报告状态。 ** 想想用红外或无线电频率控制的设备,或者没有状态主题的MQTT切换. 乐观是唯一的选择,实体也设置 `assumed_state`,见下文。

乐观的更新是这样的。 只莺在命令成功后才写状态:当发送失败时,会提出错误并离开状态. 不要显示一个州 设备从来没有接受。

```python
async def async_turn_on(self, **kwargs: Any) -> None:
    """Turn the fan on."""
    await self._device.send(Command.ON)
    self._attr_is_on = True
    self.async_write_ha_state()
```

### 假设状态 {#assumed-state}

设定 `_attr_assumed_state = True` 当状态是猜测时, 因为设备无法报告 。 前端然后显示隔开和断开的按钮,而不是切换,并保持打开和贴近的封面,这样用户可以总是发送他们所需要的命令,即使猜错.

像这样的实体在以 `RestoreEntity` 重启后可以恢复最后状态, 因为没有问题 。 Core中的两个例子:

- 晋级Dyson红外融合(`dyson_infrared/fan.py`)的风扇总是假定其状态. 它在发送每个红外线命令后写下新的状态
- MQTT开关(`mqtt/switch.py`)没有状态主题,或用户设置的`optimistic`,是乐观的. 它设置 `assumed_state`, 在发布命令后写入状态, 并在启动时恢复其最后一个状态 。

## 可用性 {#availability}

`available` 属性告诉 Home Assistant 如果它能到达设备 。 当返回 `False` 时, 状态变为 [`unavailable`](/glossary/unavailable) , 状态属性和额外的状态属性被忽略( 能力属性, 单位, 设备类 stay), 前端显示实体为不可用 。

```python
async def async_update(self) -> None:
    try:
        value = await self._device.read_temperature()
    except ExampleConnectionError:
        self._attr_available = False
        return

    self._attr_available = True
    self._attr_native_value = value
```

无法获取数据时标记一个无法获取的实体, 而不是数据只是缺失时: 现在没有值的传感器应该报告 `None`, 这将成为 `unknown` 。 记录第一次失败, 并在设备返回时记录一次, 而不是每次更新 。

## 部队更新 {#force-update}

默认情况下, Home Assistant 只在状态或属性发生变化时写新状态 。 再次写入相同的值只是更新 `last_reported` 时间戳 。 非常简单 将 `force_update` 设定为瓮 `True` 每次读数应该算作更新, 就像直接从硬件读取的传感器一样 。 节制使用:每次强制更新都是自动化和记录器处理的状态变化事件.

## Keep the database small {#keep-the-database-small}

每一个状态变化都最终会出现在数据库中. 一个经常变化的实体,带有经常变化的属性,迅速填补它. 保持额外的属性数量和稳定性,并将快速变化的值移动到自己的传感器实体中. 见[状态和属性](/core/entities/state-attributes).
