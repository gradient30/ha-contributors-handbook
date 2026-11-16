---
title: 诊断
description: 让用户下载一个配置条目或设备的数据,这样他们就可以在报告一个问题时分享,而不会泄露秘密.
sidebarGroup: 融合特征
order: 4
---

# 诊断 {#diagnostics}

{L帮助发展中国家} 让用户下载 JSON 文件与您的整合数据, 并附加到一个问题上 。 对于你作为一个维护者来说,这常常是看到用户家中发生的事情最快的方法.

用户从集成页面条目菜单中下载一个配置条目的诊断,从设备页面下载一个设备的诊断. 如果您的整合没有设备诊断, 设备页面会提供配置条目诊断 。

诊断法是[质量尺度](/core/quality-scale)黄金级的规则。

## 添加诊断 {#add-diagnostics}

创建 `diagnostics.py`,并执行其中一项或两项功能:

```python
from typing import Any

from homeassistant.components.diagnostics import async_redact_data
from homeassistant.const import CONF_API_KEY, CONF_PASSWORD
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntry

TO_REDACT = {CONF_API_KEY, CONF_PASSWORD, "serial_number"}

async def async_get_config_entry_diagnostics(
    hass: HomeAssistant, entry: ExampleConfigEntry
) -> dict[str, Any]:
    """Return diagnostics for a config entry."""
    return {
        "entry_data": async_redact_data(entry.data, TO_REDACT),
        "data": async_redact_data(
            entry.runtime_data.data.to_dict(), TO_REDACT
        ),
    }

async def async_get_device_diagnostics(
    hass: HomeAssistant, entry: ExampleConfigEntry, device: DeviceEntry
) -> dict[str, Any]:
    """Return diagnostics for a device."""
    appliance = entry.runtime_data.get_appliance(device)

    return {"details": async_redact_data(appliance.raw_data, TO_REDACT)}
```

## 省略敏感数据 {#leave-out-sensitive-data}

用户在公众问题上张贴诊断. 确定他们身上没有敏感的东西 比如:

- 密码、 API 密钥和令牌
- 位置数据,如坐标和地址
- 个人信息,如姓名和电子邮件地址

`async_redact_data` 以 `**REDACTED**` 取代您列出的密钥的值, 也出现在嵌入式词典和列表中 。 值为 `None` 或空字符串保持不变, 所以您仍然可以看到一个值没有设置 。 检查您的诊断结果: API 的数据往往比预期的要多 。

要包含一个设备或实体注册项, 请从 `homeassistant.components.diagnostics` 转换为 `device_entry_as_dict` 或 `entity_entry_as_dict` 。 他们把进入的内部领域排除在外。

## 测试诊断 {#test-diagnostics}

用快照测试输出,所以修改后在评论中出现. 在 `tests/components/diagnostics` 中的测试助手 `get_diagnostics_for_config_entry` 和 `get_diagnostics_for_device` 返回哪些用户会下载 。 见[即时测试](/core/development/tests#snapshot-tests).
