---
title: 支持发现
description: 黄金规则发现:设备被发现,因此用户不必进行查询.
sidebarLabel: 发现
sidebarGroup: 金
order: 3
---

# 支持发现 {#support-discovery}

这是黄金规则 在`quality_scale.yaml`中,它被称为`discovery`.

如果集成设备可以在网络或总线上找到,集成支持[发现](/glossary/discovery). Home Assistant可以通过 Bluetooth, DHCP, HomeKit, mDNS (zeroconf), MQTT, SSDP, 和 USB 来发现设备, apps可以通过 Supervisor 来宣布一项服务. 您在 `manifest.json` 中声明要听什么, 并在配置流的一步中处理发现 。

## 为什么这很重要 {#why-it-matters}

没有发现,用户首先必须找出哪个集成支持他们的设备,然后查看它的IP地址. 随着发现,Home Assistant告诉他们它发现了一个装置, 他们确认。 这是需要一分钟的设置和需要路由器管理页面的设置的区别.

Discovery在设置后也继续工作:当设备获得一个新的IP地址时,集成可以更新其配置. 见[发现- 更新- info](/core/quality-scale/discovery-update-info).

## 示例 {#example}

设备在 mDNS 上宣布 `_mydevice._tcp.local.` 服务 。 在 `manifest.json` 中声明 :

```json
{
  "zeroconf": ["_mydevice._tcp.local."]
}
```

然后在 `config_flow.py` 中处理, 在用户步骤旁边 。 发现步骤设置了唯一的ID,在设备已经配置时中止,并要求用户确认:

```python
class MyConfigFlow(ConfigFlow, domain=DOMAIN):
    """Config flow for My integration."""

    host: str

    async def async_step_zeroconf(
        self, discovery_info: ZeroconfServiceInfo
    ) -> ConfigFlowResult:
        """Handle zeroconf discovery."""
        self.host = discovery_info.host
        serial = discovery_info.properties["serialno"]

        await self.async_set_unique_id(serial)
        self._abort_if_unique_id_configured(updates={CONF_HOST: self.host})

        try:
            await MyClient(self.host).get_data()
        except MyClientError:
            return self.async_abort(reason="cannot_connect")

        return await self.async_step_discovery_confirm()

    async def async_step_discovery_confirm(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Ask the user to confirm the discovered device."""
        if user_input is not None:
            return self.async_create_entry(
                title="My device",
                data={CONF_HOST: self.host},
            )

        self._set_confirm_only()
        return self.async_show_form(step_id="discovery_confirm")
```

`ZeroconfServiceInfo`来自`homeassistant.helpers.service_info.zeroconf`。 其他发现方法在`homeassistant.helpers.service_info`中都有自己的服务信息类,也有自己的步骤,比如`async_step_dhcp`或`async_step_bluetooth`.

如果用户步骤设置相同的唯一ID,则通过`raise_on_progress=False`到`async_set_unique_id`。 否则,一个用户在为它打开的发现流时用手设置设备,则会流产.

## 如何检查 {#how-it-is-checked}

- hassfest,当规则是 `done` 时: 集成需要 `config_flow.py` , 或者是在 `manifest.json` (`bluetooth`,`dhcp`,`homekit`,`lorawan`,`mqtt`,`ssdp`,`usb`或`zeroconf` ) 中发现密钥, 或者在配置流中发现步骤, 如 `async_step_zeroconf` 或 `async_step_hassio` 。
- Codecov要求对`config_flow.py`中变更的线路进行100%的测试覆盖,因此发现步骤需要测试.
- 是否对设备的每一种发现方式都进行了审查。

## 例外 {#exceptions}

并不是每个设备都能被发现.  If  If  If

## 相关规则 {#related-rules}

- [配置流量](/core/quality-scale/config-flow):从UI设置有配置流.
- [提交的文件 你还好吗?](/core/quality-scale/test-before-configure):测试配置流中的连接.
- [唯一配置输入](/core/quality-scale/unique-config-entry) : 防止重复配置条目 。
- {L刚好} : 完全测试配置流 。
