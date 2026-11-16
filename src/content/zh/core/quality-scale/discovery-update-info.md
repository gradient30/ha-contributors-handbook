---
title: 更新来自发现的网络信息
description: 黄金规则发现-更新-info:发现在已知设备改变时更新其地址.
sidebarLabel: 发现- 更新- info
sidebarGroup: 金
order: 4
---

# 更新来自发现的网络信息 {#update-network-information-from-discovery}

这是黄金规则 在`quality_scale.yaml`中,它被称为`discovery-update-info`.

当已经设置的设备再次被发现时,集成使用发现信息更新其配置条目的网络信息,如主机或IP地址. 它只有在确定它是同一个设备时才这样做,因此它匹配在稳定的独特ID上,从不匹配地址本身.

## 为什么这很重要 {#why-it-matters}

大多数家用网络都动态发布IP地址. 一个重启的设备,或者一个重新boots的路由器,可以给一个设备一个新地址,一个只知道旧地址停止工作的集成. 要求用户设置静态IP地址并不是一个固定:不是每个人都可以,任何人都不应该这样做.

发现者已经在新地址看到此设备. 利用这一信息可以修复整合本身。

## 示例 {#example}

在发现步骤中,设置流中唯一的ID,并将新地址传递到`_abort_if_unique_id_configured`. 如果存在该唯一ID的条目, Home Assistant 将更新其数据, 当有变化时重新加载, 并中止流量 :

```python
async def async_step_zeroconf(
    self, discovery_info: ZeroconfServiceInfo
) -> ConfigFlowResult:
    """Handle zeroconf discovery."""
    host = discovery_info.host
    serial = discovery_info.properties["serialno"]

    await self.async_set_unique_id(serial)
    self._abort_if_unique_id_configured(updates={CONF_HOST: host})

    

# Only a new device gets this far. {#how-it-is-checked}
    self.host = host
    return await self.async_step_discovery_confirm()
```

DHCP 发现仅在 `manifest.json` 中为匹配者启动流量 。 也可以在您已经知道的设备出现新地址时获得一个流量,在 DHCP 匹配器中设置 `registered_devices` 到 `true` , 用 `connections={(CONNECTION_NETWORK_MAC, mac)}` 在设备信息中注册设备的 MAC 地址 。

```json
{
  "dhcp": [{ "registered_devices": true }]
}
```

## 如何检查 {#exceptions}

已检阅. 配置流的测试应涵盖在新地址发现已知设备。

## 例外 {#例外}

如果无法发现集成装置,则不适用本规则.
