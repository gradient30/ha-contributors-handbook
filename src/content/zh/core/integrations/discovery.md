---
title: 发现
description: Home Assistant 如何在网络、 USB 或 Bluetooth 上找到您的设备, 并把它们交给您的配置 。
sidebarGroup: 发现
order: 1
---

# 发现 {#discovery}

[发现](/glossary/discovery) 是 Home Assistant 如何自己找到设备, 并提出设置它们 。 用户在整合页面上看到"发现"卡片,确认,完成. 这是你融入经验中最能做的一件事,也是[质量尺度](/core/quality-scale)黄金级的规则。

您的整合不搜索网络本身 。 Home Assistant 运行发现集成, 如`zeroconf` 和`dhcp` , 并检查他们发现什么 匹配者在所有集成的列表中 。

## 工作原理 {#how-it-works}

1. 您在您的 [显示](/core/integrations/manifest#discovery) 中添加匹配器, 就像您的设备的 0conf 服务类型 。
2. 一个发现集成找到一个匹配的设备.
3. Home Assistant 开始您的配置流程, 在以源命名的阶梯上, 如 `async_step_zeroconf`, 开始一个描述所找到的内容的服务信息对象 。
4. 您的步骤设置了唯一的ID, 检查设备是否已经设置, 并要求用户确认 。 见[发现步骤](/core/integrations/config-flow#discovery-steps).

同样的设备经常反复被发现. Home Assistant 当发现数据相同者仍在运行时, 不启动新流, 而当设备已经设置时, 您唯一的ID 使流中止 。 当已知设备出现新的IP地址时,从发现步骤更新条目. 见[更新苍蝇上的连接细节](/core/integrations/config-flow#update-connection-details-on-the-fly).

当用户忽略一个发现的设备时,Home Assistant会用它独特的ID创建一个被忽略的配置条目,并且不会再次提供.

## 发现源." {#discovery-sources}

| 来源 | 突出键 | 步骤 | 服务信息 |
| --- | --- | --- | --- |
| mDNS 和 0conf 数据 | `zeroconf` | `async_step_zeroconf` | `ZeroconfServiceInfo` |
| HomeKit, 超过 0conf | `homekit` | `async_step_homekit` | `ZeroconfServiceInfo` |
| SSDP 和 UPnP | `ssdp` | `async_step_ssdp` | `SsdpServiceInfo` |
| DHCP 人权方案 | `dhcp` | `async_step_dhcp` | `DhcpServiceInfo` |
| USB 美国 | `usb` | `async_step_usb` | `UsbServiceInfo` |
| MQTT | `mqtt` | `async_step_mqtt` | `MqttServiceInfo` |
| Bluetooth | `bluetooth` | `async_step_bluetooth` | `BluetoothServiceInfoBleak` |
| 洛拉万语 | `lorawan` | `async_step_integration_discovery` | `LoRaWANDiscoveryInfo` |
| A Supervisor 应用程序 | 无 | `async_step_hassio` | `HassioServiceInfo` |
| 另一种一体化 | 无 | `async_step_integration_discovery` | 由这种一体化定义 |

服务信息类居住在`homeassistant.helpers.service_info`,但Bluetooth一个除外,它来自`homeassistant.components.bluetooth`. 例如:

```python
from homeassistant.helpers.service_info.zeroconf import ZeroconfServiceInfo

async def async_step_zeroconf(
    self, discovery_info: ZeroconfServiceInfo
) -> ConfigFlowResult:
    """Handle a device found with zeroconf."""
    host = discovery_info.host
    serial_number = discovery_info.properties["serialno"]
    ...
```

一些有用的领域:

- `ZeroconfServiceInfo`:`host`,`port`,`hostname`,`name`,`type`,以及`properties`中的TXT记录.
- `SsdpServiceInfo`:像 谁的SSDP 头像 `ssdp_location` 和 `ssdp_st` , 以及 `upnp` 中的 UPnP 设备描述 。
- `DhcpServiceInfo`:`ip`,`hostname`(小写),和`macaddress`(小写,没有结肠).
- `UsbServiceInfo`: `device`(串口的路径),`vid`,{H3 我们走吧女友,`serial_number`,{H咨商并不构成,循序渐进全盘几分钟  我感觉所拥有的一声的最新资料的某些方面促进实现.
- 女士们加大力度几句隧  工作

如果您对源代码不执行该步骤, Home Assistant 将调用您的 `user` 步骤 。 它只在您的集成还没有配置条目时才这样做,并且一次一个流:一旦设备设置,发现就不再开始流. 从来没有独有身份的整合就是这样被发现的.

## 另一种融合的发现 {#discovery-by-another-integration}

一个集成可以找到另一个集成的设备. 例如,八月集成知道耶鲁访问Bluetooth集成需要的Bluetooth锁键. 以 `discovery_flow.async_create_flow` 启动另一集成的流, 以 `integration_discovery` 源 :

```python
from homeassistant.config_entries import SOURCE_INTEGRATION_DISCOVERY
from homeassistant.helpers import discovery_flow

discovery_flow.async_create_flow(
    hass,
    "other_domain",
    context={"source": SOURCE_INTEGRATION_DISCOVERY},
    data={"address": address, "key": key},
)
```

其他集成在`async_step_integration_discovery`中处理. 对您从代码开始的每个发现流使用此帮助器: 当一个数据相同的时候, 它会避免启动流, 并等待 Home Assistant 开始 。

## 设置后查找设备 {#find-devices-after-setup}

通过清单的发现涉及新的配置条目。 集成枢纽往往也需要了解后来出现的设备,或者它已经设置的设备。 发现集成有API用于此. 见[网络发现](/core/integrations/network-discovery)和[Bluetooth 整合](/core/integrations/bluetooth)。

## 试试看 {#test-it}

测试每一个发现步骤:一个新设备,一个已经设置的设备,一个移动到新地址的设备,以及一个被忽略的设备. 在测试中用手构建服务信息对象,其中的值是一个真实的设备发送的.
