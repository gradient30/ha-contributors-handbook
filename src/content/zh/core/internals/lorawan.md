---
title: LoRAWAN 设备
description: 一个连接集成是如何注册一个LoRAWAN网络服务器的,一个设备集成是如何找到并曝光其上的设备的.
sidebarLabel: 洛拉万语
sidebarGroup: 你说的
order: 35
---

# LoRAWAN 设备 {#lorawan-devices}

LoRAWAN是一种远程低功率的无线电协议,由电池动力传感器使用,偶尔发送读数. 设备不直接对 Home Assistant 说话 。 他们与网络服务器交谈,比如ChirpStack或The Things Stack,以及Home Assistant与服务器交谈.

LoRAWAN支持包含两种整合, 由共享 `lorawan` 整合连接:

- 一个**连接集成** 设置一个网络服务器并注册它与Home Assistant的连接.
- 一个**设备集成**支持一个供应商的设备。 它在每个注册的连接上找到它们,然后把它们变成实体.

在它们的 [显示](/core/integrations/manifest#dependencies) 的 `dependencies` 中都列出 `lorawan` 。 两者都基于[`lorawan-connection`](https://github.com/home-assistant-libs/lorawan-connection),一个由Home Assistant项目维护的Python软件包. 与每一个集成一样,对服务器说话的代码,以及解码设备的有效载荷的代码,都生活在[图书馆](/core/integrations/api-library)中. 该集成处理配置、发现和实体。

## 连接集成 {#connection-integrations}

### 执行后端 {#implement-the-backend}

连接集成库执行 `Connection` `lorawan-connection` 的协议 :

- `stack_type`:服务器的命名空间, 如 `"chirpstack"` 或 `"tts"` 。 在连接之前就知道了
- { 我必须先将所有匹配设备发送给听者,然后返回一个功能来取消订阅,然后继续发送直播设备事件。 `brands`是`frozenset`的一对。 `None` 选择所有设备 。
- `on_disconnect(listener)`: 连接丢失时报告, 并返回一个函数来取消订阅 。
- `async_send_downlink(downlink)`:为设备排队命令,并返回其ID。

每个设备后端报告都有 `DeviceDescriptor` 。 将其 `network_id` 设置为您连接集成的配置条目的ID 。 将其 `stack` 设置为连接的 `stack_type`, 并填写 `brand_id` 和 `model_id` 服务器知道设备 。 发现和模型选择匹配

库的[所审议的纲和后端指南](https://home-assistant-libs.github.io/lorawan-connection/connection/adding-a-backend/)覆盖事件顺序,来了过滤,下行链接.

### 我以为你从根本上竭力的公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公公几句公缜骏伎恪ử鸳鸯竿蝎徘呜鸳鸯嬷冉寐 Spider焕艳公玲公公公公公公公公公公公公公公公公公 {#register-the-connection}

连接到 `async_setup_entry` 中的服务器, 然后注册与 `async_register_connection` 的连接 :

```python
from lorawan_connection import Connection

from homeassistant.components import lorawan

async def async_register_server(
    hass: HomeAssistant, entry: MyConfigEntry, connection: Connection
) -> None:
    """Register a connected backend during setup of the entry."""
    unregister = await lorawan.async_register_connection(
        hass, entry, connection=connection
    )
    entry.async_on_unload(unregister)
```

一旦连接发送了设备,登记返回,并开始为这些设备发现设备集成匹配。 一个配置条目可以一次注册一个连接: 第二个会提高`ValueError`. 它返回的函数会撤回连接 。 它没有关闭它。

其余的留在你的整合:

- 如果设置失败或取消, 请关闭后端 。 当认证失败时加高 `ConfigEntryAuthFailed` , 当服务器目前无法到达时加高 `ConfigEntryNotReady` 。 见[处理设置失败](/core/integrations/setup-failures).
- 当连接丢失时, `lorawan` 撤销它 。 您的集成重新连接, 对它的配置条目重新加载, 并注册新连接 。 保持相同的`network_id`,所以上面的装置保持相同的装置.
- 卸货时,当Home Assistant停止时,撤销注册,关闭后端. 在您故意关闭后端之前, 移除您自己的重联听器, 或者关闭后端, 重新排程 。

## 设备整合 {#device-integrations}

### 被发现 {#get-discovered}

在您的 [显示](/core/integrations/manifest#lorawan) 中添加 `lorawan`ء子殆 。 您的整合需要 [配置流量](/core/integrations/config-flow) , 和 `lorawan` 在 `dependencies` 中 。 {\fn黑体\fs20\shad2\2aH82\3aH20\4aH33\fscx95\3cH592001\be1}哈斯福特检查过两个

,                                          ,                                                                                                                                                                                    发现信息没有字段: 流量只需要知道您的供应商的设备出现. 只有添加的设备开始发现. 设备的更新和活动没有。

您的集成需要一个配置条目, 对于供应商, 不是每个设备或服务器一个 。khan. 设备管理器在每个连接上找到设备,所以用户不会选择服务器. 12月12日-12月31日-12月31日-12月31日-12月31日-12月31日-12月31日-12月31日-12月31日-12月31日-12月12日-12月31日-12月12日-12月12日-12月12日-12月12日-12月12日-12月12日-12月12日-12月12日-12月12日-12月12日-12月12日-12月12日-12日-12日-12日-12月12日-12月12日-12月12日-12日-12月-12日-12日-12月-12日-12月-12日-12月-12日-12月-12日-12日-12月-12日-12日-12日-12月-12月-12日-12日-12天-12天-12天-12天-12天-12天-12天-12天-12天-12天-12天-------12天-12天-12天-

标注在品牌上匹配,并选择您的整合. 您的图书馆决定它支持的模型 。 它拥有每个型号的`Device`子类,在它的`identifiers`中列出每个堆栈的`(brand_id, model_id)`,和一个在`DEVICES`中列出这些型号的`DeviceCollection`子类. 见[葱花 :](https://home-assistant-libs.github.io/lorawan-connection/patterns/library/).

### 设备管理器设置 {#set-up-the-device-manager}

记账的 它为每个连接创建了您的库, 包括以后注册的连接, 并为每个匹配模型的设备创建一个协调器 。 您赋予它 女士们 `Connection` 和 `hass` 和 设备 的 协调器 。

在示例中, `ExampleDevice` 和`ExampleDevices` 代表设备库的类 。 在您的列表 `requirements` 中列出该库 。

```python title="__init__.py"
from example_lorawan import ExampleDevice, ExampleDevices

from homeassistant.components.lorawan import DeviceManager
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant

from .coordinator import ExampleCoordinator

type ExampleConfigEntry = ConfigEntry[
    DeviceManager[ExampleDevice, ExampleCoordinator]
]

PLATFORMS = [Platform.SENSOR]

async def async_setup_entry(
    hass: HomeAssistant, entry: ExampleConfigEntry
) -> None:
    """Set up the vendor integration."""
    manager = entry.runtime_data = DeviceManager(
        hass,
        entry,
        create_collection=ExampleDevices,
        create_coordinator=ExampleCoordinator,
    )
    entry.async_on_unload(manager.close)
    await manager.async_setup()

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

async def async_unload_entry(
    hass: HomeAssistant, entry: ExampleConfigEntry
) -> None:
    """Unload the vendor integration."""
    await hass.config_entries.async_unload_platforms_or_raise(entry, PLATFORMS)
```

### 共享更新设备 {#share-device-updates}

一个设备的所有实体都共享它的协调员. 协调员不民意调查:从设备开始作为数据,并听设备更新. 没有更新间隔, 也没有第一次刷新 。

```python title="coordinator.py"
import logging
from typing import override

from example_lorawan import ExampleDevice

from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

_LOGGER = logging.getLogger(__name__)

class ExampleCoordinator(DataUpdateCoordinator[ExampleDevice]):
    """Share the updates of one device with its entities."""

    def __init__(self, hass: HomeAssistant, device: ExampleDevice) -> None:
        """Initialize the coordinator."""
        

# The device manager shuts the coordinator down. {#entities-and-devices}
        super().__init__(
            hass, _LOGGER, config_entry=None, name=device.descriptor.name
        )
        self.async_set_updated_data(device)
        self._unsubscribe = device.add_update_listener(self._updated)

    @callback
    def _updated(self) -> None:
        self.async_set_updated_data(self.data)

    @override
    async def async_shutdown(self) -> None:
        self._unsubscribe()
        await super().async_shutdown()
```

每个平台向管理员询问 `subscribe_coordinator_added` 的协调员 。 听者立刻得到存在的协调员,然后得到每一个新的协调员。 卸载时取消订阅 :

```python title="sensor.py"
async def async_setup_entry(
    hass: HomeAssistant,
    entry: ExampleConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up the sensors."""

    @callback
    def coordinator_added(coordinator: ExampleCoordinator) -> None:
        async_add_entities([ExampleSensor(coordinator)])

    entry.async_on_unload(
        entry.runtime_data.subscribe_coordinator_added(coordinator_added)
    )
```

### 实体和装置 {#what-the-device-manager-handles}

以 `LoRaWANEntity` 为基础, 连同平台的实体类 。 `LoRaWANEntity` 是一个 [`CoordinatorEntity`](/core/integrations/fetching-data) , 它将设备作为 `self.device` 给予您, 并且当设备关闭时使实体无法使用 。 它设置 `_attr_has_entity_name` , 而它的 `async_update` 却无所作为, 因为更新通过设备输入 。

描述您实体的 `device_info` 中的设备, 用 `device_identifier` 表示 :

```python title="entity.py"
from typing import override

from example_lorawan import ExampleDevice

from homeassistant.components.lorawan import (
    LoRaWANEntity,
    device_identifier,
)
from homeassistant.helpers.device_registry import DeviceInfo

from .const import DOMAIN

class ExampleEntity(LoRaWANEntity[ExampleDevice]):
    """Base entity for a device of this vendor."""

    @property
    @override
    def device_info(self) -> DeviceInfo:
        return DeviceInfo(
            identifiers={device_identifier(DOMAIN, self.device)},
            name=self.device.descriptor.name,
        )
```

标识符是您的域名,带有设备的网络ID和DevEUI. 两个服务器每个可以有一个设备与相同的DevEUI,所以将网络ID和DevEUI也放到你实体的独有ID中,然后是测量或通道的密钥.

解码有效载荷和编码命令留在您的库中. 实体属性读取设备状态,实体动作调用设备的方法. 将失败的命令转换为 [Home Assistant 例外](/core/development/style#error-handling) 。

### 设备管理器处理什么 {#testing}

- 当连接丢失时, 管理者会保存设备及其注册项, 并标记其协调员为失败, 因此这些实体无法使用 。 当一个新的连接注册同一配置条目时,它会比较设备. 仍然在那里的装置保留着他们的模型和协奏器. 丢失的装置被移除 。
- 经理没有超时。 发送的设备很少保持可用 。
- 当一个设备从服务器中移除,或者其连接的配置条目被删除时,管理器会从设备注册中移除设备并关闭其协调器. 它的实体也随之而来。
- 当您的配置条目卸下时, 管理者会关闭收藏和协调员 。 它保存着登记册条目,并且不接触连接。

## 测试 {#测试}

`lorawan_connection.mock.MockConnection`在测试中支持服务器 。所面对的问题包括: 与您库中的真实收藏一起使用, 测试它报告的设备, 实时更新, 发现, 实体, 移除, 卸载。 值得测试的案件:

- 在您装入后注册的连接 。
- 与一个设备有两条连接 同一DevEUI.
- 断开和重联,包括连接中断时删除的设备.
- 安装失败时清理 Home Assistant 订阅和收藏, 取消, 或者 Home Assistant 停止 。
- 清理设备注册缇, 包括您集成时删除的连接项 。

在您的库中测试解码, 不在整合中 。 自行测试连接集成的后端,针对真实的服务器: 认证,设备列表,事件发送,下行链路,在设置失败时关闭传输,将被取消,或者Home Assistant停止.
