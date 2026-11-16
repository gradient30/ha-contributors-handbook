---
title: 获取数据
description: 使用投票或推力从设备或服务中获取数据,并与数据更新协调员在实体之间共享数据。
sidebarGroup: 数据与更新
order: 1
---

# 获取数据 {#fetching-data}

您的集成需要来自某个地方的数据: 本地网络上的 API, 云服务, 插座, 或 USB 棒上的序列端口 。 如何得到它取决于API提供什么。 此页面帮助您选择正确的方法 。

## 推动或投票 {#push-or-poll}

API分为两种:

- ** Push** : 您订阅, API 告诉你时有什么变化。 这使用最少的资源,更新立即出现.
- ** Poll**:您每隔一段时间向API询问最新数据。 下次民意调查时会出现变化。

API支持时使用推力. 设置列表中的 [IOT 类](/core/integrations/manifest#iot_class) 以匹配 。

## 对所有实体进行一次投票:协调员 {#poll-once-for-all-entities-the-coordinator}

多数APIs在一个请求中返回许多实体的数据. 然后,你想要一个民意调查 整个整合, 和所有实体 从它的结果更新。 `DataUpdateCoordinator`中的 `homeassistant.helpers.update_coordinator` 就是这样。 它还处理错误、重试和退后, 当更新失败时, 您的实体无法访问 。

将协调员插入 `coordinator.py` :

```python
from datetime import timedelta
import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import (
    DataUpdateCoordinator,
    UpdateFailed,
)

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

type ExampleConfigEntry = ConfigEntry[ExampleCoordinator]

class ExampleCoordinator(DataUpdateCoordinator[ExampleData]):
    """Fetch data for all Example entities."""

    config_entry: ExampleConfigEntry

    def __init__(
        self,
        hass: HomeAssistant,
        config_entry: ExampleConfigEntry,
        client: ExampleClient,
    ) -> None:
        """Initialize the coordinator."""
        super().__init__(
            hass,
            _LOGGER,
            config_entry=config_entry,
            name=DOMAIN,
            update_interval=timedelta(minutes=1),
        )
        self.client = client

    async def _async_setup(self) -> None:
        """Load data that only needs to be fetched once."""
        self.device = await self.client.get_device()

    async def _async_update_data(self) -> ExampleData:
        """Fetch the latest data."""
        try:
            return await self.client.get_data()
        except ExampleAuthError as err:
            raise ConfigEntryAuthFailed from err
        except ExampleRateLimitError as err:
            raise UpdateFailed(retry_after=err.retry_after) from err
        except ExampleError as err:
            raise UpdateFailed(
                translation_domain=DOMAIN,
                translation_key="update_error",
                translation_placeholders={"error": str(err)},
            ) from err
```

这些部件是做什么的:

- `config_entry`:永远通过它。 必须融入核心。
- `update_interval`: 如何频繁的投票。 协调员只听民意调查,而至少一个实体听。
- `_async_setup`:可选. 在第一次刷新时运行一次, 数据只需要加载一次即可 。
- `_async_update_data`:获取数据。 无论它返回到什么, 都最终在 `coordinator.data` 中 。

和例外做什么:

- `UpdateFailed`: 更新失败 。 协调员记录一次(不是每一次失败的民意测验),标记无法进入的实体,并在下一次间隔时再次尝试. 使用 `retry_after` , 它会等待这么多秒 。 在第一次刷新时, `retry_after` 传递给失败设置的 `ConfigEntryNotReady`, 所以 [设置重试](/core/integrations/setup-failures) 尊重它 。
- `UpdateFailedUnreachable`:当设备或服务无法到达时,像关闭的设备一样,一个`UpdateFailed`的子类. 它的行为与`UpdateFailed`相同,但协调员将其记录在`info`级别,而不是`error`(`<name> is unavailable: <message>`),正如[不可用时日志](/core/quality-scale/log-when-unavailable)规则要求的那样。
- `ConfigEntryAuthFailed`: 证书不再有效。 协调员停止投票并开始[重新校正](/core/integrations/reauth-reconfigure#reauthentication)。
- 超时和`aiohttp`客户端错误由协调员自己处理,[OAuth 2.0 符号错误](/core/integrations/oauth2#errors)也是如此.

### 设置时进行第一次刷新 {#do-the-first-refresh-during-setup}

在 `async_setup_entry` 中创建协调员, 在设置平台前进行第一次刷新 :

```python
coordinator = ExampleCoordinator(hass, entry, client)
await coordinator.async_config_entry_first_refresh()

entry.runtime_data = coordinator
```

如果第一次刷新失败, `async_config_entry_first_refresh` 将提高 `ConfigEntryNotReady` 和 Home Assistant [重试设置](/core/integrations/setup-failures) 。 您的实体总是从数据开始 。 只从 `async_setup_entry` 调用 : 在其它配置条目状态下, 它会引起错误 。 如果第一次更新失败, 不应停止设置, 请拨打 `await coordinator.async_refresh()` 。

### 使用协调员的实体 {#entities-that-use-the-coordinator}

扩展`CoordinatorEntity`。 它负责投票、可用和倾听协调员的意见。 在属性中从 `self.coordinator.data` 读取值, 如 `native_value` :

```python
from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity

class ExampleSensor(CoordinatorEntity[ExampleCoordinator], SensorEntity):
    """A sensor of an Example device."""

    @property
    def native_value(self) -> float:
        """Return the temperature."""
        return self.coordinator.data.temperature
```

当新数据到达时,协调员会拨打`_handle_coordinator_update`,它会写状态,属性读取新值. 您也可以覆盖 `_handle_coordinator_update` 并设置 `_attr_native_value` 。 如果有,请从 `coordinator.data` 设置在 `__init__` 中。 实体只在其被添加后才开始监听,要进行第一次刷新,在设置时已经发生,从未达到`_handle_coordinator_update`. 没有这个,传感器会一直保持`unknown`直到下一次更新. 与 `always_update=False` 和不改变的数据, 这需要很长时间 。

在命令后, 请求使用 `await self.coordinator.async_request_refresh()` 提供新数据 。 请求被解禁,如此一连串的呼叫导致一个更新.

### 跳过更新该更改无 {#skip-updates-that-change-nothing}

默认情况下,协调员在每次更新后都会给其听众打电话,即使数据没有变化. 如果您的数据可以和`==` 相比较, 就像一个数据类, 通过`always_update=False` 。 然后,协调员只在数据变化时给听众打电话,这样可以保存状态写作.

### 只获取所使用的 {#only-fetch-what-is-used}

一些API允许您要求更少的数据. 将 `context` 传递到 `CoordinatorEntity` , 如设备 ID, 并在协调器中使用 `self.async_contexts()` 来查看哪个上下文有听众 。 已禁用的实体不听,所以您不会获取数据 。

## 向协调员推 {#push-with-a-coordinator}

一名协调员还致力于推动API. 省去`update_interval`,所以它从不投票,在新数据到达时拨打`async_set_updated_data`:

```python
@callback
def _handle_push(self, data: ExampleData) -> None:
    """Handle new data pushed by the device."""
    self.async_set_updated_data(data)
```

如果协调员也进行投票,这将重新确定下一次投票之前的时间。

## 没有协调员就推 {#push-without-a-coordinator}

当每个实体有自己的订阅时,在`async_added_to_hass`中订阅,在删除实体时不订阅. 实体可以禁用,所以在添加前不要订阅. 设定 `_attr_should_poll = False`,并在数据到达时亲自写状态 :

```python
class ExampleSwitch(SwitchEntity):
    """A switch that gets pushed updates."""

    _attr_should_poll = False

    async def async_added_to_hass(self) -> None:
        """Subscribe to updates."""
        self.async_on_remove(
            self._device.subscribe(self._handle_update)
        )

    @callback
    def _handle_update(self) -> None:
        """Write the new state."""
        self.async_write_ha_state()
```

`async_write_ha_state()` 立即写入当前状态 。 先嘱咐你的`async_update`然后写下状态

## 每个实体的票价 {#poll-per-entity}

如果每个实体都有自己的终点,并且有一个请求将地图映射到一个实体,那么您就可以以实体的`async_update`方法获取数据。 Home Assistant 在一个间隔中调用它, 只要 `should_poll` 是 `True` (默认) 。

- 如果实体在添加前需要数据, 请将 `update_before_add=True` 传递到 `async_add_entities` 。
- 在平台上以 `SCAN_INTERVAL` 常数设置间隔, 如 `SCAN_INTERVAL = timedelta(seconds=30)` 。 不要设置太低:它在{H2 对不起 Home Assistant 中花费资源,可以超载设备,还可以让用户被云API屏蔽.

如果几个实体有一个终点,则使用协调员。

## 平行请求 {#parallel-requests}

Home Assistant限制每个平台同时运行多少个更新和动作呼叫,因此集成不会超载一个设备或API. 多数一体化不需要在这里改变任何事情。

限量是每个平台的semaphore,既适用于实体更新,也适用于动作呼叫. 默认是 `1` 当您的实体有同步的 `update` 方法时, 和 `0` (无限制) 否则, 就像对有 `async_update` 方法或根本没有更新方法的实体一样 。 Home Assistant在平台添加的第一个实体上决定。 用平台文件中的 `PARALLEL_UPDATES` 常数覆盖它 :

```python
# Only one update or action call at a time on this device {#only-one-update-or-action-call-at-a-time-on-this-device}
PARALLEL_UPDATES = 1
```

在每一个平台上明确设定:这是[质量尺度](/core/quality-scale)银级规则。 一个协调员已经集中了更新,所以使用一个的集成可以设置`PARALLEL_UPDATES = 0`像`sensor`和`binary_sensor`这样的只读平台. 那么只有动作才有限度
