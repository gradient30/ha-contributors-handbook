---
title: 设备跟踪器实体
description: 报告设备的位置或是否与网络或信标相连。
sidebarLabel: 设备跟踪器
sidebarGroup: 传感器与状态
---

# 设备跟踪器实体 {#device-tracker-entity}

设备跟踪器报告存在:无论是手机,标签,还是汽车在家中,离家,还是在[——的图图图图图图图图图图图图图图图图图图图图图图图图,图图图,图图图图,图图图图,图图图图图图图,图图图图图图图,图图图图,图图图,图图,图图图,,图图图图,,图图图,,图图图图的,,,,,的,,,,,,图,,,,,,,的,,的,,,,的,,,的,,,,,,,,的,,,,,,,,的,,,,,,,,,,,,,,,,的,,,,的,,,,,,的,,,,,,,,,的,,,的,,,的,,,,,,,,,,,,,,的,,,,的,,,,,,,,,,,,,,,,,的,,,,,,,,,,的,,,,,,,,,,,的,,,,,,](/glossary/zone). 它只读。 有三个基础类,都是从 `homeassistant.components.device_tracker` 导入的,你选择一个 由你的设备如何知道它在哪里:

- `TrackerEntity`:设备报告其位置,作为GPS坐标或所在区域. 像是电话应用或汽车
- `ScannerEntity`:该设备在本地IP网络上可见,由其MAC地址识别. 就像一个列出连接客户端的路由器.
- `BaseScannerEntity`:设备是否相连,没有`ScannerEntity`的MAC地址假设. 如Bluetooth信标。

三者默认获得`diagnostic`[实体类别](/glossary/entity-category),并设置`tracking_type`能力属性:`position`为`TrackerEntity`,`connection`为扫描仪.

从 Home Assistant 演示中嵌入的仪表板卡的现场演示。 由GPS追踪到的手机 和由路由器追踪到的笔记本电脑 用瓷砖卡

```html
<ha-embed-provider
  style="
    display: grid;
    grid-template-columns: repeat(12, minmax(0, 1fr));
    gap: 8px;
    align-items: start;
    max-width: 500px;
  "
>
  <script type="application/json">
    [
      {
        "entity_id": "device_tracker.phone",
        "state": "home",
        "attributes": {
          "friendly_name": "Phone",
          "source_type": "gps",
          "latitude": 52.3731,
          "longitude": 4.8922,
          "gps_accuracy": 12
        }
      },
      {
        "entity_id": "device_tracker.laptop",
        "state": "not_home",
        "attributes": {
          "friendly_name": "Laptop",
          "source_type": "router"
        }
      }
    ]
  </script>
  <ha-embed-card style="grid-column: span 6">
    <script type="application/json">
      {
        "type": "tile",
        "entity": "device_tracker.phone",
        "grid_options": {
          "columns": 6
        }
      }
    </script>
  </ha-embed-card>
  <ha-embed-card style="grid-column: span 6">
    <script type="application/json">
      {
        "type": "tile",
        "entity": "device_tracker.laptop",
        "grid_options": {
          "columns": 6
        }
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

## 的临时议程 {#properties}

每个实体的通用属性,如`name`或`available`,都在[实体类别](/core/entities/entity-class)上。

### 所有设备跟踪器 {#all-device-trackers}

| 名称 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- |
| `source_type` | `SourceType` | 冉要求 `BaseScannerEntity`. `SourceType.GPS` `TrackerEntity` `SourceType.ROUTER` `ScannerEntity` | 设备的跟踪方式: `GPS`,`ROUTER`,`BLUETOOTH`,或`BLUETOOTH_LE`. |

`battery_level`地产在 Home Assistant2027.7. 以 [传感器](/core/entities/sensor) 和 `battery` 设备类报告电池级别 。

### `TrackerEntity` {#trackerentity}

| 名称 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- |
| `latitude` | `float \| None` | `None` | 器之纬度. |
| `longitude` | `float \| None` | `None` | 器之经度. |
| `location_accuracy` | `float` | `0` | 位置的准确性,以米计. |
| `in_zones` | `list[str] \| None` | `None` | 设备所在区域的实体身份,包括被动区域。 设定时,即使是空列表,它也优先于坐标. 顺序无关紧要:基类按区域半径对列表进行排序,并滴出不存在的区域. |

设置 `in_zones` 或 `latitude` 和 `longitude` 。 没有 `in_zones`, 基座从坐标和精确度 来划分区域。 `location_name`的地产在 Home Assistant2027.7.

A `TrackerEntity` 默认不会进行民意调查, 并且每次更新都会写给州机器, 即使没有改变。

### `BaseScannerEntity` {#basescannerentity}

| 名称 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- |
| `is_connected` | `bool \| None` | 要求数 | 设备是否连接 。 |

### `ScannerEntity` {#scannerentity}

`ScannerEntity`基于`BaseScannerEntity`,所以它也需要`is_connected`.

| 名称 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- |
| `mac_address` | `str \| None` | `None` | 该盎司的MAC地址. 这盎司也是该实体的独特身份证明。 |
| `ip_address` | `str \| None` | `None` | 镶嵌设备的IP地址. |
| `hostname` | `str \| None` | `None` | 设备的主机名. |

一个 `ScannerEntity` 在 MAC 地址上被键入, 并有它自己的几处默认 :

- 它独特的ID是MAC地址. 你没有设置一个自己。
- 直到 Home Assistant Core 2027.11, 基础类设备为有 MAC 地址但没有设备信息 的跟踪器设置设备信息: 以 MAC 地址作为连接的设备, 以主机名命名, 或者在设备是新设备时以 MAC 地址命名. MAC地址从不取代已有设备的名称. 不要依赖它:从2027.11开始,没有设备信息的跟踪器不象其他任何实体一样包含在设备中. 要让一个跟踪器从设备中退出, 请设置 `_attr_device_info = DeviceInfo()` 。 空设备信息表示没有设备,默认仅在设备信息为`None`时适用.
- 默认已禁用 。 路由器看到许多客户端,大多数都不值得跟踪: 设备用户最想跟踪的,像手机一样,通常用Home Assistant Companion应用程序跟踪. 覆盖 `_attr_entity_registry_enabled_default` 当 tracker 不仅仅是在网络上看到的另一个客户端时 。 例如,当跟踪是设备的目的时,就像Zigbee一样. 存在标记是ZHA模型作为设备跟踪器,或者当用户自行设置跟踪设备时.
- 当设置MAC地址和IP地址时,DHCP发现使用它们,在设置一个时使用主机名,以发现设备的集成. 当 Home Assistant 在设备连接时设置实体时会发生这种情况, 即使追踪器被禁用 。 DHCP发现还用`router`源类型为`home`的跟踪器来查看:一次当DHCP发现开始,当这样的跟踪器获得第一个状态. 一个从 `not_home` 到 `home` 的跟踪器不会触发此操作 。

## 支持的特性 {#supported-features}

该实体没有支持的特性。

## 方法 {#methods}

没有执行方法。 通过在 `update` 或 `async_update` 中投票, 或用 `async_write_ha_state` 推动 , 保持属性流畅 。 见[更新状态](/core/entities/state-updates).

## 状态 {#states}

基班设州. 不要设置 `state` 自己 。

| 状态 | `TrackerEntity` | 扫描仪 |
| --- | --- | --- |
| `home` | 首个活动区为家园区. | 连通了 连通区就到了 |
| `not_home` | 无活动区域. | Not connected. |
| 一个区域名称 | 第一个活动区是另一个区. | 连接,而关联区是另一个区. |
| `unknown` | 没有坐标和`in_zones`。 | `is_connected`是`None`,或者关联区不存在. |

扫描仪默认与主区相关联. 用户可以在实体设置中选择另一个区域,比如办公室为那里的信标. 当该区被移除时, Home Assistant 会产生[修理](/glossary/repair) 的问题 。

`in_zones` 状态属性列出设备所在的区域, 首先最小 。 当从坐标区划出来时,大小相同的区按照距离其中心区划,最接近区划. 扫描仪列出它的关联区和包含它的区. 当扫描仪没有连接时, `in_zones` 是一个空列表 。

## 示例 {#example}

报告GPS位置的汽车的追踪器:

```python
from homeassistant.components.device_tracker import TrackerEntity

class ExampleCarTracker(TrackerEntity):
    """Location of an example car."""

    _attr_has_entity_name = True
    _attr_translation_key = "location"

    def __init__(self, car: ExampleCar) -> None:
        """Initialize the tracker."""
        self._car = car
        self._attr_unique_id = f"{car.vin}_location"

    async def async_added_to_hass(self) -> None:
        """Subscribe to position updates."""
        self.async_on_remove(self._car.subscribe(self._update))

    def _update(self) -> None:
        """Handle a new position from the car."""
        self._attr_latitude = self._car.latitude
        self._attr_longitude = self._car.longitude
        self._attr_location_accuracy = self._car.accuracy
        self.async_write_ha_state()
```

路由器客户端的跟踪器,包含在客户端的设备中. 客户端名称在设备上进行,当路由器上名称改变时,设备会重新命名. 重命名只发生在 tracker 启用时 : Home Assistant 不添加已禁用的实体, 因此它不会得到协调器更新 。 被禁用的跟踪器的设备信息在每次集成设置时仍然被使用,因此其设备获得现在的名称.

```python
from homeassistant.components.device_tracker import ScannerEntity
from homeassistant.core import callback
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC, DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

class ExampleClientTracker(CoordinatorEntity[ExampleCoordinator], ScannerEntity):
    """A client connected to an example router."""

    _attr_has_entity_name = True
    _attr_name = None

    def __init__(self, coordinator: ExampleCoordinator, client: ExampleClient) -> None:
        """Initialize the tracker."""
        super().__init__(coordinator)
        self._attr_mac_address = client.mac
        self._attr_hostname = client.hostname
        self._attr_device_info = DeviceInfo(
            connections={(CONNECTION_NETWORK_MAC, client.mac)},
            name=client.name,
            via_device_id=coordinator.router_device_id,
        )

    @property
    def is_connected(self) -> bool:
        """Return if the client is connected to the router."""
        return self.mac_address in self.coordinator.data.connected

    @callback
    def _handle_coordinator_update(self) -> None:
        """Rename the device when the client is renamed on the router."""
        name = self.coordinator.data.clients[self.mac_address].name
        if name and (device := self.device_entry) and device.name != name:
            dr.async_get(self.hass).async_update_device(device.id, name=name)
        super()._handle_coordinator_update()
```
