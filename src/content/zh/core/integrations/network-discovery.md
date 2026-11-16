---
title: 网络发现
description: 大使, 请使用零conf, SSDP, DHCP, USB, MQTT 和 Home Assistant 的网络 API, 在您的集成运行时找到设备
  。
sidebarGroup: 发现
order: 2
---

# 网络发现 {#network-discovery}

[通过清单发现](/core/integrations/discovery) 启动新设备的配置流程 。 一些集成需要更多:一个在出现设备时添加设备的中枢,或者一个检查已知设备现在位置的集成. Home Assistant通过本页面上的API共享其发现集成,所以您的集成不需要运行自己的扫描器.

将您使用的整合, 如 我真 `zeroconf` 或 `ssdp` 添加到您的 [显示](/core/integrations/manifest#dependencies) 中的 `dependencies` 。

## Zerocon坚定地致力于我们 {#zeroconf}

Home Assistant运行一个 mDNS 执行,[python- 零conf 键](https://github.com/python-zeroconf/python-zeroconf),并共享它。 在一个主机上运行多个 mDNS 执行是不推荐的,所以从不开始自己的程序. 获取共享实例,并将其传递到您的库:

```python
from homeassistant.components import zeroconf

aiozc = await zeroconf.async_get_async_instance(hass)
```

对同步 `Zeroconf` 对象使用 `zeroconf.async_get_instance(hass)` 。 Python-zeroconf的例子显示了你对两者所能做的.

## 南苏丹 {#ssdp}

SSDP集成保存了它发现的设备的缓存. 查一下他们:

| 函数 | 回返情况 |
| --- | --- |
| `ssdp.async_get_discovery_info_by_udn_st(hass, udn, st)` | 一个 UDN 和 ST 的发现信息, 或 `None` |
| `ssdp.async_get_discovery_info_by_st(hass, st)` | 这个ST找到的每样东西列表 |
| `ssdp.async_get_discovery_info_by_udn(hass, udn)` | 一个设备的所有服务列表 |

```python
from homeassistant.components import ssdp

discovery_infos = await ssdp.async_get_discovery_info_by_st(
    hass, "urn:schemas-upnp-org:device:ZonePlayer:1"
)
```

要立即听到新设备, 请用 `ssdp.async_register_callback` 注册回调 。 它与表单中的`ssdp`格式相同,而`homeassistant.const`中的`MATCH_ALL`格式与任何信头的值相同:

```python
from homeassistant.components import ssdp

entry.async_on_unload(
    await ssdp.async_register_callback(
        hass,
        _async_player_discovered,
        {"st": "urn:schemas-upnp-org:device:ZonePlayer:1"},
    )
)
```

## DHCP 人权方案 {#dhcp}

`dhcp.async_discovered_service_info` 返回仍然在 DHCP 缓存中的设备, 作为 `DhcpServiceInfo` 对象 `ip`, `hostname` 和 `macaddress` 。 主机名是小写,MAC地址是小写,没有冒号:`AA:BB:CC:12:34:56`变成`aabbcc123456`.

```python
from homeassistant.components import dhcp

for service_info in dhcp.async_discovered_service_info(hass):
    ...
```

## USB 美国 {#usb}

USB集成在 Home Assistant 启动时, 当用户打开集成页时, 以及设备被插入时, 如果系统支持, 寻找新设备 。 要在同一时间检查新的兼容设备, 请注册回调 :

```python
from homeassistant.components import usb
from homeassistant.core import callback

@callback
def _async_check_for_usb() -> None:
    """Check for new compatible USB devices."""

entry.async_on_unload(
    usb.async_register_scan_request_callback(hass, _async_check_for_usb)
)
```

## MQTT {#mqtt}

使用 MQTT 的整合必须等到 MQTT 客户端在订阅前可用 。 `async_wait_for_mqtt_client` 正在设置时等待 MQTT 。 它返回 `True` 当客户端可用时, 和 `False` 当 MQTT 未设置时, 或者在超时无法使用 。 客户端目前无需连接.

```python
from homeassistant.components import mqtt

if not await mqtt.async_wait_for_mqtt_client(hass):
    raise ConfigEntryNotReady("MQTT is not available")
```

## 网络适配器 {#network-adapters}

如果你的集成使用自己的发现方法,它需要知道要使用哪个网络接口. [网络整合](https://www.home-assistant.io/integrations/network/) 持有用户的偏好 。 问它,而不是自己看界面:

```python
from homeassistant.components import network

adapters = await network.async_get_adapters(hass)
```

每个适配器都是这样的词典:

```python
{
    "name": "eth1",
    "enabled": True,
    "auto": True,
    "default": False,
    "ipv4": [{"address": "192.168.1.5", "network_prefix": 23}],
    "ipv6": [],
}
```

只使用 `enabled` 的适配器 。 要获得地址的网络:

```python
from ipaddress import ip_network

for adapter in adapters:
    if not adapter["enabled"]:
        continue

    for ip_info in adapter["ipv4"]:
        network_range = ip_network(
            f"{ip_info['address']}/{ip_info['network_prefix']}", False
        )
```
