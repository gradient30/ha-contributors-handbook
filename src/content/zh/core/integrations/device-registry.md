---
title: 设备注册
description: 注册您的整合设备,将其连接到枢纽,将产品分割到儿童设备中,让用户删除设备.
sidebarGroup: 装置和登记册
order: 1
---

# 设备注册 {#device-registry}

设备注册是 Home Assistant 记录 [设备](/glossary/device) 的地方 。 一个设备将属于同一个实体分组:一个带电池的温度和湿度传感器是一个有三个实体的设备。 用户在自己的页面上看到设备,放入区域,在自动化中瞄准.

## 什么是设备 {#what-is-a-device}

装置特别是最不发达国家的装置是具有自身控制单元的物理装置,或服务装置。 控制单位不必聪明,但必须控制发生的事情.

- 带有4个房间传感器的自动调温器是5个装置:一个是带有内置传感器的自动调温器,另一个是每个房间传感器。
- 一个连接到另一个设备上的传感器来读取它的数据,是一个独立于那个其他设备的装置. 传感器可以移动去读另一个设备.
- 一个具有多个独立部件的产品,像一个有单独切换插座的电源条,可以被拆分为一个带有[儿童装置](/core/integrations/device-registry#child-devices)的母设备.

设备属于注册它们的配置条目. 一个由两个集成设置积极合作这一观点的ủ体设备制定出两个设备,每个配置条目一个.

## 设备属性 {#device-properties}

| 财产 | 这是什么 |
| --- | --- |
| `id` | 为设备生成的 ID Home Assistant |
| `identifiers` | 一套`(DOMAIN, identifier)`Tuples, 就像一个序列号。 每个在配置条目中都是独特的. |
| `connections` | 一套`(connection_type, value)`Tuples,像一个MAC地址。 每个在配置条目中都是独特的. 类型为`CONNECTION_NETWORK_MAC`,`CONNECTION_BLUETOOTH`,`CONNECTION_UPNP`和`CONNECTION_ZIGBEE`. |
| `config_entry_id` | 设备所属的配置条目 |
| `config_subentry_id` | 囤积器属于 [子审查报告](/core/integrations/subentries), 或`None` |
| `name` | 嗯 设备的名称 |
| `name_by_user` | 用户给它的名称 |
| `manufacturer` | 制造商 |
| `model` | 模型名称 |
| `model_id` | 模型标识符 |
| `serial_number` | 序号. 与`identifiers`中的序列号不同,它不一定是独一无二的. |
| `sw_version` | 固件版本 |
| `hw_version` | 硬件版本 |
| `configuration_url` | 可以配置设备或服务的地方 。 使用 `homeassistant://<path>` 链接到 Home Assistant 内的页面 。 |
| `entry_type` | `None` 或 `DeviceEntryType.SERVICE` 服务 |
| `via_device_id` | 设备 Home Assistant 像中枢一样通过此设备 |
| `parent_device_id` | 对于一个儿童设备:其父母。 只有子设备(`ChildDeviceEntry`)有这个属性. WebSocket API 将其报告为 `null` 用于其他设备 。 |
| `area_id` | 设备所在区域 |
| `labels` | 设备的标签 |
| `disabled_by` | 谁将设备示例, 作为 `DeviceEntryDisabler` 或 `None` |
| `created_at`, `modified_at` | 当设备创建和上次更改时 。 由登记机构管理。 |

## 通过一个实体,通过一个实体, , , , , , , , , , , , , , , , , , ,  , , , ,  的 的 , , ,   ,   的 , , , 的 ,  的 的 , ,      的 的 的 , , 而 的 的的 , 而 的 的 的 而 的 而而而 的的 的 的 的 而 而的 的 的 而 的 的  而 的  的 而 的 的 的 的 的 而 的 的 的 而  的 的 的 的 的 而 而 而 而 的 的 ( 而 而 的 的 而 的 的 的 的 而而 而 而 而 而    而 而 的 的 而 而 而 {#register-a-device-through-an-entity}

通常方式: 给您的实体 `device_info` 。 Home Assistant 添加实体时创建或更新设备 。 只对从配置条目添加的实体有效, 包含 [唯一标识](/glossary/unique-id) 。

```python
from homeassistant.helpers.device_registry import DeviceInfo

class ExampleEntity(CoordinatorEntity[ExampleCoordinator]):
    """Base entity of the Example integration."""

    _attr_has_entity_name = True

    def __init__(self, coordinator: ExampleCoordinator) -> None:
        """Initialize the entity."""
        super().__init__(coordinator)
        device = coordinator.data.device
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, device.serial_number)},
            manufacturer="Example",
            model=device.model_name,
            model_id=device.model_id,
            name=device.name,
            sw_version=device.firmware_version,
        )
```

`DeviceInfo`取 `identifiers`,`connections`,`name`,`manufacturer`,`model`,`model_id`,`serial_number`,`sw_version`,`hw_version`,`configuration_url`,`entry_type`,`suggested_area`,`via_device_id`,和`translation_key`为译名.

登记册首先通过标识符,然后通过连接,寻找同一配置条目的现有设备。 一个匹配就够了:您通过的其他标识符和连接被添加到该设备中. 如果它们已经属于同一配置条目的另一个设备,即碰撞,则登记簿产生错误。

## 自己注册设备 {#register-a-device-yourself}

一个没有实体的设备,像中枢一样,直接注册. 在 `async_setup_entry` 中这样做 :

```python
from homeassistant.helpers import device_registry as dr

device_registry = dr.async_get(hass)

hub = device_registry.async_get_or_create(
    config_entry_id=entry.entry_id,
    connections={(dr.CONNECTION_NETWORK_MAC, dr.format_mac(info.mac))},
    identifiers={(DOMAIN, info.bridge_id)},
    manufacturer="Signify",
    model=info.model_name,
    model_id=info.model_id,
    name=info.name,
    sw_version=info.sw_version,
)
```

它以 `id` 返回 `DeviceEntry` 。

当您笃信 `DeviceInfo` 时, 例如 帮助者 所建 的 或 与您的实体 共享的 , 请通过 `async_get_or_create_from_info` :

```python
hub = device_registry.async_get_or_create_from_info(
    config_entry_id=entry.entry_id, device_info=hub_device_info
)
```

## 连接设备到中心 {#link-devices-to-a-hub}

`via_device_id`告诉 Home Assistant 它通过哪个设备到达另一个设备, 就像桥后面的灯泡。 它显示了网络的地形. 这需要Home Assistant 中枢设备的ID,所以中枢必须先注册.

如果您自己注册了中心站, 您已经拥有了中心站的ID: pass `hub.id` 到您的实体 。 否则,从中枢的识别符中查找:

```python
via_device_id = dr.async_get_device_id_by_identifier(
    hass, (DOMAIN, bridge_id), config_entry_id=entry.entry_id
)
```

当中心尚未存在时,它会提高`ValueError`。

## 儿童装置 {#child-devices}

儿童装置是一个物理产品的一个逻辑部分的轻量级装置,如电源条的一个出口或一帮墙开关. 母设备持有属于整个产品的东西,如网络连接和固件更新. 每个儿童拥有自己的实体,如每个出口的开关和能量传感器。 用户可以将每个部分放入不同的区域.

不要和 `via_device_id` 混为一谈: 这是关于不同产品之间的连接。 儿童器械大约是一个产品的部件。

儿童设备 :

- 属于父母一方,以父母一方的设备ID(`parent_device_id`)作为参考.
- 属于 我们得拥有与母子相同的配置条目和子条目。
- 没有自己的身份:没有`connections`,`via_device_id`,`manufacturer`,`model`,固件版本,或序列号. 这些是父母的
- 获取其父的面积,除非它有自己的区域.
- 无法拥有自己的儿童设备 。

### 登记儿童设备 {#register-a-child-device}

通过一个实体,返回带有 `identifiers` 和 `parent_device_id` 的 `ChildDeviceInfo` 。 父母必须已经注册:

```python
from homeassistant.helpers.device_registry import ChildDeviceInfo

self._attr_device_info = ChildDeviceInfo(
    identifiers={(DOMAIN, f"{strip_id}_outlet_{number}")},
    name=f"Outlet {number}",
    parent_device_id=parent_device_id,
)
```

或直接:

```python
outlet = device_registry.async_get_or_create_child(
    config_entry_id=entry.entry_id,
    parent_device_id=parent.id,
    identifiers={(DOMAIN, f"{strip_id}_outlet_1")},
    name="Outlet 1",
)
```

除了需要的`config_entry_id`,`parent_device_id`,和`identifiers`,`async_get_or_create_child`取`config_subentry_id`,`name`,`suggested_area`,`disabled_by`,`translation_key`,和`translation_placeholders`. 故意没有`via_device_id`,`connections`,`manufacturer`,`model`,或固件论证:一个儿童设备没有这些. 当您已经持有 `ChildDeviceInfo` 时, 请通过 `async_get_or_create_child_from_info` 。

如果父属于子条目, 也通过 `config_subentry_id` 。 这是没有继承的。 注册机构从未为您 太创建父程序 : 当父程序不存在时, 它会生成 `DeviceInfoError` , 它是一个子设备本身, 或者属于另一个配置条目或子条目 。

### 将已有设备移动到子设备 {#move-existing-devices-to-child-devices}

如果一个儿童设备的标识符与同一配置条目的现有设备相匹配,则该设备成为儿童设备,并保留其ID. 使用该设备的自动化继续工作. 这使得一个已经将产品分割成单独的设备的集成体易于移动.

只有在配置条目自条目设置以来没有将该设备注册为普通设备时才有效:注册者会提出 `DeviceInfoError` 。 它忘了那些注册 当配置入口卸下。 所以只将该部分登记为儿童设备,不要为它留下一个`DeviceInfo`在它的一个实体上.

反之则不直接支持. `async_update_child_device` 无法改变父机, 且 `async_get_or_create` 与已有的孩子设备的标识符一起, 会产生一个错误, 而不是把它变成一个普通的设备 。 要将一个孩子设备重新变成一个普通设备,用 `async_remove_device` 移除它, 然后用 `async_get_or_create` 重新注册它, 用相同的标识符 。 命令事项:识别器仅在儿童设备被移除后才免费使用. 删除一个设备也会删除其实体的注册条目,因此这适合一个没有实体的儿童设备. 实体只有在您重新加入它们时才会回来, 它们的设置, 如实体 ID 和名称, 恢复 。

### 跟随父母的是什么 {#what-follows-the-parent}

- 移除父母会删除孩子。
- 使父母残疾使子女残疾,使父母能够使子女再次残疾。 残疾父母的子女不能单独启用。
- 没有自己区域的儿童属于其父母。 `dr.async_get_effective_area_id(hass, device)` 返回适用的区域 。
- 标签没有继承。
- 有子女的父母不能移动到另一个配置条目或子条目。
- 一项针对家长机构的行动也针对其子女的实体。 一项只针对儿童实体的行动。 这样一来, 没错,当一个集成器将设备的实体移动到儿童设备上时, 瞄准设备的自动化会继续工作。

## 查找设备 {#look-up-devices}

在实体内,使用`self.device_entry`. 在其他地方,对配置条目的瞄准镜:标识符和连接仅在一个配置条目内独有.

```python
device_registry = dr.async_get(hass)

# By the ID Home Assistant gave it {#by-the-id-home-assistant-gave-it}
device = device_registry.async_get(device_id)

# By one of its identifiers or connections {#by-one-of-its-identifiers-or-connections}
device = device_registry.async_get_device_by_identifier(
    (DOMAIN, serial_number), entry.entry_id
)
device = device_registry.async_get_device_by_connection(
    (dr.CONNECTION_NETWORK_MAC, mac), entry.entry_id
)

# All devices of a config entry {#all-devices-of-a-config-entry}
devices = dr.async_entries_for_config_entry(device_registry, entry.entry_id)
```

`async_get` 返回正常的设备和子设备 。 传 `include_child_devices=False` 只获得普通设备 。 要只获得一个孩子设备, 请同时通过 `include_main_devices=False` 和 `include_composite_devices=False` : 默认情况下, `async_get` 也返回一个只读的 [每个冉装项拆分为一个设备的设备](https://contributors.home-assistant.io/blog/2026/07/21/device-registry-single-config-entry/#backwards-compatibility) ID 的站点, 这不是一个孩子设备 。 其他的检查返回正常设备,而不是儿童设备. 对于儿童设备,使用`async_get_child_device_by_identifier(identifier, config_entry_id)`,或`dr.async_entries_for_parent_device(device_registry, parent_device_id)`,用于设备的所有儿童。 要在配置条目中获取每个带有标识符或连接的设备,请使用`device_registry.async_get_devices()`.

要将设备与您拥有的集成的配置条目合并, 例如在动作中, 使用 `dr.async_get_device_and_config_entry_for_domain(hass, device_id, domain=DOMAIN)` 。 它返回 `(None, None)` 当设备未知, 而`(device, None)` 当您的域没有配置条目拥有它时 。 它需要与 `include_child_devices` 和 `include_main_devices` 参数相同的参数 。

## 更新设备 {#update-devices}

当某事发生变化时,如更新后的固件版本,更新设备:

```python
device_registry.async_update_device(device.id, sw_version=new_version)
```

## 让用户删除设备 {#let-users-remove-devices}

用户只能在您的整合允许的情况下从UI中删除一个设备. 在`__init__.py`中执行`async_remove_config_entry_device`。 返回 `True` 如果设备可以去, 在任何清理后它需要:

```python
from homeassistant.helpers.device_registry import DeviceEntry

async def async_remove_config_entry_device(
    hass: HomeAssistant, entry: ExampleConfigEntry, device_entry: DeviceEntry
) -> bool:
    """Allow removing a device that is no longer connected."""
    return not any(
        identifier
        for identifier in device_entry.identifiers
        if identifier[0] == DOMAIN
        and identifier[1] in entry.runtime_data.data.devices
    )
```

此示例只允许删除中心不再报告的设备 。 整合也可以在`EVENT_DEVICE_REGISTRY_UPDATED`上行动,如果这样更方便的话.

看到设备消失的集成器还应自行去除 Stale 设备:这是[质量尺度](/core/quality-scale)的黄金级规则.
