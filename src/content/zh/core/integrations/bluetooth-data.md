---
title: 正在获取 Bluetooth 数据
description: 为 Bluetooth 设备选择正确的协调器, 并将其广告变成实体 。
sidebarGroup: 发现
order: 4
---

# 正在获取 Bluetooth 数据 {#fetching-bluetooth-data}

许多 Bluetooth 设备在广告中发送数据 : 它们反复播放的小包, 没有人连接到它们。 Home Assistant有由这些广告而不是投票驱动的协调员。 他们的工作就像[数据更新协调员](/core/integrations/fetching-data), 并照顾你的可用性。

## 选一个协调员 {#pick-a-coordinator}

| 您的设备 | 使用 |
| --- | --- |
| 主要是传感器,二进制传感器,或事件源,广告中所有的数据 | `PassiveBluetoothProcessorCoordinator` |
| 主要是传感器,二进制传感器,或事件源,但有些数据需要连接 | `ActiveBluetoothProcessorCoordinator` |
| 其他东西,所有的数据在广告中 | `PassiveBluetoothDataUpdateCoordinator` |
| 有些数据需要连接 | `ActiveBluetoothDataUpdateCoordinator` |
| 只使用连接, 不使用广告 | 常规 [`DataUpdateCoordinator`](/core/integrations/fetching-data) |

## 处理器协调员 {#processor-coordinators}

处理器协调员将传感器类集成的代码削减到几乎一无所有. 您不久前在库中绘制了广告, 将结果转换为 `PassiveBluetoothDataUpdate` , 框架在实体出现时创建并更新它们 。

A `PassiveBluetoothDataUpdate` 有四幅地图。 密钥为 `PassiveBluetoothEntityKey(key, device_id)`, 如 `PassiveBluetoothEntityKey("temperature", None)` :

| 外地 | 它所持有的 |
| --- | --- |
| `devices` | 每个崛起设备的 `DeviceInfo` ID. `None` 是主设备 。 |
| `entity_descriptions` | 每个实体键 [实体描述](/glossary/entity-description) |
| `entity_names` | 每个实体的密钥名称 |
| `entity_data` | 每个实体的键值 |

### 设置协调员 {#set-up-the-coordinator}

在 `__init__.py` 中,创建包含设备地址和库解析方法的协调员。 在平台建立后开始,这样他们就可以先订阅:

```python
from homeassistant.components.bluetooth import BluetoothScanningMode
from homeassistant.components.bluetooth.passive_update_processor import (
    PassiveBluetoothProcessorCoordinator,
)

type ExampleConfigEntry = ConfigEntry[PassiveBluetoothProcessorCoordinator]

async def async_setup_entry(
    hass: HomeAssistant, entry: ExampleConfigEntry
) -> None:
    """Set up an Example Bluetooth device."""
    assert entry.unique_id is not None
    parser = ExampleParser()

    coordinator = PassiveBluetoothProcessorCoordinator(
        hass,
        _LOGGER,
        address=entry.unique_id,
        mode=BluetoothScanningMode.ACTIVE,
        update_method=parser.update,
    )
    entry.runtime_data = coordinator

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    

# Start after the platforms subscribed {#the-sensor-platform}
    entry.async_on_unload(coordinator.async_start())
```

`connectable`这里默认为`False`,所以每个适配器都提供广告.

### 传感器平台 {#connect-when-needed}

每个平台都注册一个处理器,将解析后的数据转换为 `PassiveBluetoothDataUpdate` , 和一个实体类 :

```python
from homeassistant.components.bluetooth.passive_update_processor import (
    PassiveBluetoothDataProcessor,
    PassiveBluetoothDataUpdate,
    PassiveBluetoothProcessorEntity,
)
from homeassistant.components.sensor import SensorEntity

def sensor_update_to_bluetooth_data_update(
    parsed: ExampleUpdate,
) -> PassiveBluetoothDataUpdate:
    """Turn parsed data into a Bluetooth data update."""
    return PassiveBluetoothDataUpdate(
        devices={None: parsed.device_info},
        entity_descriptions={...},
        entity_data={...},
        entity_names={...},
    )

async def async_setup_entry(
    hass: HomeAssistant,
    entry: ExampleConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up the Example Bluetooth sensors."""
    coordinator = entry.runtime_data
    processor = PassiveBluetoothDataProcessor(
        sensor_update_to_bluetooth_data_update
    )

    entry.async_on_unload(
        processor.async_add_entities_listener(
            ExampleBluetoothSensor, async_add_entities
        )
    )
    entry.async_on_unload(coordinator.async_register_processor(processor))

class ExampleBluetoothSensor(PassiveBluetoothProcessorEntity, SensorEntity):
    """A sensor of an Example Bluetooth device."""

    @property
    def native_value(self) -> float | int | str | None:
        """Return the value of the sensor."""
        return self.processor.entity_data.get(self.entity_key)
```

### 需要时连接 {#ask-for-active-scans}

`ActiveBluetoothProcessorCoordinator`工作方式相同,平台不变. 它增加了两个在广告改变时运行的功能:

- `needs_poll_method(service_info, last_poll)`: 现在返回是否需要连接 。 `last_poll`是上次民调后的秒数, 或`None`.
- `poll_method(service_info)`:连接到设备并返回数据。

```python
def _needs_poll(
    service_info: BluetoothServiceInfoBleak, last_poll: float | None
) -> bool:
    

# Only poll when Home Assistant is running, the device needs it, {#data-update-coordinators}
    

# and a connectable adapter can reach it {#and-a-connectable-adapter-can-reach-it}
    return (
        hass.state is CoreState.running
        and parser.poll_needed(service_info, last_poll)
        and bool(
            async_ble_device_from_address(
                hass, service_info.device.address, connectable=True
            )
        )
    )

async def _async_poll(service_info: BluetoothServiceInfoBleak):
    

# The advertisement may come from an adapter that cannot connect, {#the-advertisement-may-come-from-an-adapter-that-cannot-connect}
    

# so get a connectable BLEDevice for the same address {#so-get-a-connectable-bledevice-for-the-same-address}
    if service_info.connectable:
        device = service_info.device
    elif not (
        device := async_ble_device_from_address(
            hass, service_info.device.address, True
        )
    ):
        raise RuntimeError(
            f"No connectable device for {service_info.device.address}"
        )

    return await parser.async_poll(device)

coordinator = ActiveBluetoothProcessorCoordinator(
    hass,
    _LOGGER,
    address=address,
    mode=BluetoothScanningMode.PASSIVE,
    update_method=parser.update,
    needs_poll_method=_needs_poll,
    poll_method=_async_poll,
    

# Take advertisements from every adapter, and swap the BLEDevice {#take-advertisements-from-every-adapter-and-swap-the-bledevice}
    

# for a connectable one when polling {#for-a-connectable-one-when-polling}
    connectable=False,
)
```

从 `homeassistant.components.bluetooth.active_update_processor` 导入 。

### 询问活动扫描 {#询问活动扫描}

两个处理器协调员都接受`scan_interval`和`scan_duration`. 他们要求{ 下午2}模式中的扫描器对这个地址进行积极扫描,扫描时间为`scan_duration`秒,每`scan_interval`秒. 一些设备只有在被积极扫描时才会发送其全部数据,在一段时间没有被扫描时才会返回到需要连接的地方. 选择一个短于此的 `scan_interval` 和一个 `scan_duration` 足够长的时间来捕捉下一个广告 :

```python
coordinator = ActiveBluetoothProcessorCoordinator(
    ...,
    scan_interval=165.0,
    scan_duration=10.0,
)
```

两者都默认为 `None`, 这保持了正常的速度 。 扫描已设置为 `PASSIVE` 或 `ACTIVE` 的用户不受影响 。

## 数据更新协调员 {#数据更新协调员}

对于主要不是传感器的设备还会像锁或灯一样使用`PassiveBluetoothDataUpdateCoordinator`(来自`passive_update_coordinator`)或`ActiveBluetoothDataUpdateCoordinator`(来自`active_update_coordinator`). 分类, 处理`_async_handle_bluetooth_event` 中的广告 :

```python
from homeassistant.components import bluetooth
from homeassistant.components.bluetooth.active_update_coordinator import (
    ActiveBluetoothDataUpdateCoordinator,
)
from homeassistant.core import CoreState, callback

class ExampleCoordinator(ActiveBluetoothDataUpdateCoordinator[None]):
    """Handle the data of an Example lock."""

    def __init__(
        self,
        hass: HomeAssistant,
        ble_device: BLEDevice,
        device: ExampleLock,
    ) -> None:
        """Initialize the coordinator."""
        super().__init__(
            hass=hass,
            logger=_LOGGER,
            address=ble_device.address,
            needs_poll_method=self._needs_poll,
            poll_method=self._async_update,
            mode=bluetooth.BluetoothScanningMode.ACTIVE,
            connectable=True,
        )
        self.device = device

    @callback
    def _needs_poll(
        self,
        service_info: bluetooth.BluetoothServiceInfoBleak,
        seconds_since_last_poll: float | None,
    ) -> bool:
        """Return whether to connect and poll the device."""
        return (
            self.hass.state is CoreState.running
            and self.device.poll_needed(seconds_since_last_poll)
            and bool(
                bluetooth.async_ble_device_from_address(
                    self.hass, service_info.device.address, connectable=True
                )
            )
        )

    async def _async_update(
        self, service_info: bluetooth.BluetoothServiceInfoBleak
    ) -> None:
        """Connect to the device and poll it."""

    @callback
    def _async_handle_bluetooth_event(
        self,
        service_info: bluetooth.BluetoothServiceInfoBleak,
        change: bluetooth.BluetoothChange,
    ) -> None:
        """Handle a new advertisement."""
        self.device.update_from_advertisement(service_info.advertisement)
        super()._async_handle_bluetooth_event(service_info, change)
```

从您的名中调用 `_async_handle_bluetooth_event` : 它标记可用的设备, 更新听众, 在活动版本中, 当需要时会安排民调 。

被动版本没有`needs_poll_method`和`poll_method`,而`connectable`默认为`False`. 覆盖 `_async_handle_unavailable` 当设备停止广告时 。

> [!NOTE]
> 不可用取决于 Bluetooth 堆栈是否注意到一个设备停止了广告 。 在 macOS 上, CoreBluetooth 缓存广告, 可能永远不会报告, 所以 `_async_handle_unavailable` 可能不会被调用 。
