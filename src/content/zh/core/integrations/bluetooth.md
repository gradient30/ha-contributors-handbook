---
title: Bluetooth 整合
description: 使用 Bluetooth 和 Bluetooth 整合的 API 的最佳做法 。
sidebarLabel: Bluetooth
sidebarGroup: 发现
order: 3
---


# Bluetooth 整合 {#bluetooth-integrations}

Home Assistant艳丽管理所有Bluetooth适配器和扫描器本身,包括远程的,如ESPHomeBluetooth代理. 您的集成从未开始自己的扫描器: 它使用 Bluetooth 集成, 它与每一个需要的集成共享一流的广告 。

本页有最佳做法和API. 要将广告变成实体,请参见[正在获取 Bluetooth 数据](/core/integrations/bluetooth-data). 要被发现, 请在您的 [显示](/core/integrations/manifest#bluetooth) 中添加 `bluetooth` 匹配器 。

## 最佳实践 {#best-practices}

- 在您的列表中添加 `bluetooth_adapters` 到 `dependencies` 。自由地将所有支持的远程适配器连接起来 在您试图使用它们之前
- 您的图书馆需要 `BleakScanner` 吗 ? 用`bluetooth.async_get_scanner(hass)`拿一个 运行几台扫描仪成本很高,当用户更改适配器设置时,这一台继续工作.
- 连接之间不要重复使用 `BleakClient` 。 这使得连接的可靠性降低.
- 使用至少10秒的连接超时. BlueZ在第一次连接到一个新的或更新的设备时,必须解决服务.
- 期待连接偶尔失败, 并重试 。 诠释 [`bleak-retry-connector`](https://pypi.org/project/bleak-retry-connector/) 软件包快速可靠地将猜想解开 。

## 可连接和不可连接 {#connectable-and-non-connectable}

一些Bluetooth适配器,像许多远程的适配器一样,只能收听广告:它们不能连接到设备. 许多设备不需要连接,因为所有设备都在广告中。

这就是`connectable`的目的。 它默认为 `True` : 您只能从可连接的适配器获取数据 。 设定为 `False` 前提是您的设备只需要广告, 而您可以从所有适配器获取数据, 无论是否可连接 。

如果您的一些设备需要连接, 而其他设备不需要, 请在列表中设置 `connectable` 每个匹配者 。 如果您无法用匹配器将它们区分开, 请检查配置流中的 `connectable` `BluetoothServiceInfoBleak` , 并中止需要您无法连接的设备 。

## 订阅广告 {#subscribe-to-advertisements}

`bluetooth.async_register_callback` 当看到匹配的设备时, 或者当它的广告改变时, 打电话给你 。 它使用与清单相同的匹配器,加上`address`. 它返回一个取消订阅的函数。

```python
from homeassistant.components import bluetooth
from homeassistant.core import callback

@callback
def _async_discovered_device(
    service_info: bluetooth.BluetoothServiceInfoBleak,
    change: bluetooth.BluetoothChange,
) -> None:
    """Handle a new advertisement."""

entry.async_on_unload(
    bluetooth.async_register_callback(
        hass,
        _async_discovered_device,
        {"address": "44:33:11:22:33:22", "connectable": False},
        bluetooth.BluetoothScanningMode.ACTIVE,
    )
)
```

其他匹配者的工作方式相同,如家用Kit设备的`{"manufacturer_id": 76, "manufacturer_data_start": [6]}`,或`{"local_name": "Prodigio_*"}`.

### 重播已知设备 {#replay-of-known-devices}

当您订阅时, Bluetooth 集成重播它已经拥有的广告, 所以您立即看到所有已知的设备 。 通过 `replay` 来更改 :

| 数值 | 行为 |
| --- | --- |
| `BluetoothCallbackReplay.OLDEST_FIRST` | 重放顺序 设备被首次看到。 默认. |
| `BluetoothCallbackReplay.NEWEST_FIRST` | 首先重播最新广告, 因为当您想要立即对当前状态采取行动时 |
| `BluetoothCallbackReplay.DISABLED` | 没有重播, 只有新广告 |

### 一个设备的主动扫描 {#active-scans-for-one-device}

`AUTO`模式中的扫描器被动扫描,并在短窗口中切换为主动扫描. 如果您的匹配器有 `address`, 而模式不是 `PASSIVE`, 您可以请求该地址的主动扫描窗口, 速度适合您的设备 : 通过 `scan_interval` (窗口之间的秒) 和 `scan_duration` (每窗口秒) 。 没有它们,蓝牙的默认适用:每5分钟有一个10秒的窗口. 数值被夹在允许的蓝牙范围内。 用户设置为 `PASSIVE` 或 `ACTIVE` 的扫描器不受影响 。

### 每个广告 {#every-advertisement}

`async_register_callback`跳过没有改变的广告。 要查看每个地址的广告, 请使用 `async_register_advertisement_callback`, 例如检查一个设备是否还在广告中, 配置流量是否打开 :

```python
entry.async_on_unload(
    bluetooth.async_register_advertisement_callback(
        hass, _async_advertisement, "44:44:33:11:23:42"
    )
)
```

只有`raw`字节是每包的,它们都是`None`在不提供原始广告的后端。 其他数据则通过包合并。 回调一次每个扫描仪听到一个包, 也用于广告, 然后投放一个更强大的来源, 所以它运行很多。 噪音的苹果广告 Home Assistant 过滤出早期 从来没有达到它。 不再需要时立即取消订阅.

### 等一等广告 {#wait-for-one-advertisement}

`async_process_advertisements` 等待您返回 `True` 发布广告, 或等待超时 :

```python
def _has_temperature(
    service_info: bluetooth.BluetoothServiceInfoBleak,
) -> bool:
    """Wait for an advertisement with manufacturer ID 323."""
    return 323 in service_info.manufacturer_data

service_info = await bluetooth.async_process_advertisements(
    hass,
    _has_temperature,
    {"address": discovery_info.address, "connectable": False},
    bluetooth.BluetoothScanningMode.ACTIVE,
    ADDITIONAL_DISCOVERY_TIMEOUT,
)
```

用匹配器中的 `address` 和一个非 `PASSIVE` 模式, 超时也被用作该地址的主动扫描窗口 。

## 查找设备 {#look-up-devices}

| 函数 | 回返情况 |
| --- | --- |
| `async_ble_device_from_address(hass, address, connectable=True)` | 从最近的适配器可以到达设备的暗 `BLEDevice`, 或`None` 。 使用它而不是启动扫描仪来解决地址. |
| `async_last_service_info(hass, address, connectable=True)` | 最近蕙H0],从扫描仪带出最佳信号 |
| `async_address_present(hass, address, connectable=True)` | 设备是否仍然被看到 |
| `async_discovered_service_info(hass, connectable=True)` | 仍然存在的每个设备 |
| `async_scanner_devices_by_address(hass, address, connectable=True)` | 遐每看到设备的适配器一个`BluetoothScannerDevice`,带有它的`ble_device`,`advertisement`和`scanner` |
| `async_scanner_count(hass, connectable=True)` | 扫描仪的数量。 当没有扫描仪可以到达设备时,用它来给出一个明显的错误. |

如果您从无法连接的适配器接收到数据,但需要连接,则将`BLEDevice`交换一个与`async_ble_device_from_address(hass, address, connectable=True)`连接的`BLEDevice`. 只要一个可连接的适配器在射程内,那就可行。

### 解释设备为何无法到达 {#explain-why-a-device-is-unreachable}

当 `async_ble_device_from_address` 返回 `None` 或连接失败时, `async_address_reachability_diagnostics` 在给人类的文本中解释原因 。 从设备中传递您需要的东西:想要连接的人关心连接槽,只读广告的人不关心.

```python
from homeassistant.components.bluetooth import BluetoothReachabilityIntent

reason = bluetooth.async_address_reachability_diagnostics(
    hass, address, BluetoothReachabilityIntent.CONNECTION
)
```

文中说,是否看到地址,用哪个扫描仪和什么信号,所有扫描仪是否都忙于连接. 把它放在错误或日志消息中, 但不要分析它: 它的措辞可以改变 。

## 可用性 {#availability}

`async_track_unavailable`当设备不再被看到时给你打电话。 最多需要5分钟。 有了`connectable=True`,只要一个可连接的适配器能够到达,设备就算得上可用. 使用`connectable=False`,任何适配器都会做.

```python
@callback
def _async_unavailable(
    service_info: bluetooth.BluetoothServiceInfoBleak,
) -> None:
    """Handle the device going away."""

entry.async_on_unload(
    bluetooth.async_track_unavailable(
        hass, _async_unavailable, address, connectable=True
    )
)
```

当一个设备算作已消失,取决于它广告的频率. Bluetooth 集成学该间隔 : 用 `async_get_learned_advertising_interval(hass, address)` 获得它 。 它返回`None`直到知道为止。 在此之前,使用倒置间隔,您可以设置为 `async_set_fallback_availability_interval(hass, address, seconds)` , 并读为 `async_get_fallback_availability_interval` 。 没有两者,则适用`bluetooth.FALLBACK_MAXIMUM_STALE_ADVERTISEMENT_SECONDS`。

## 重新发现 {#rediscovery}

Bluetooth 集成会记住它已经开始发现的哪些设备, 所以它不会两次询问用户 。 有时你希望它忘记:

| 函数 | 用它的时候 |
| --- | --- |
| `async_rediscover_address(hass, address)` | 一个配置条目或设备被移除 。 清除历史, 你必须从缓存数据开始再次发现, 这样设备就可以在不重启的情况下再次设置 。 |
| `async_clear_address_from_match_history(hass, address)` | 一个设备改变了状态,但仍发布同样的UUID广告,就像工厂重置之后一样. 清除历史,所以接下来的广告可以开始新的发现. |
| `async_clear_advertisement_history(hass, address)` | 下一则广告应该到达您的召回, 即使它与前一则相同。 在关贸总协定会议之后,听到下一个“我醒了”广告很有用。 它不影响发现。 |
| `async_request_active_scan(hass, duration=None)` | 您现在需要主动扫描, 例如在配置流程中 。 等待 `duration` 秒( 或 Habluetooth 的默认值) , 这样您就可以阅读之后的新广告 。 同时通话共享一个扫描窗口. 只影响`AUTO`模式扫描仪. |

> [!WARNING]
> 不要使用`async_clear_address_from_match_history`对广告经常变的装置,比如将读数放入其中的传感器. 每一个变化都会开始一个新的发现流。

## 扫描仪 {#scanners}

这些用于提供Bluetooth鼎适配器或需要查看扫描仪的集成.

### 扫描仪 {#inspect-scanners}

`async_scanner_by_source(hass, source)` 按其MAC地址返回一个扫描器, `async_current_scanners(hass)` 返回全部扫描器 。 仅用于诊断和调试. 扫描仪的物体来自蓝牙,它们的界面可以在发布之间变化. 读取`source`和`current_mode`这样的简单属性,期望它们为`None`,绝不改变任何东西,也不保留对扫描仪的引用.

### 提供扫描仪 {#provide-a-scanner}

提供 Bluetooth 适配器 `bluetooth` 在它的 `dependencies` 中添加 `bluetooth` , 并在 `bluetooth_adapters` 的 `after_dependencies` 中列出 。 注册扩展 `BaseHaScanner` 的扫描仪 。 如果适配器需要限制连接,则通过连接槽的数目:

```python
cancel = bluetooth.async_register_scanner(
    hass, scanner, connection_slots=slots
)
```

扫描仪通过`bluetooth.async_get_advertisement_callback(hass)`的回调将广告输入到Home Assistant作为`BluetoothServiceInfoBleak`对象。 要移除扫描仪,包括它的广告历史,请拨打`bluetooth.async_remove_scanner(hass, source)`。
