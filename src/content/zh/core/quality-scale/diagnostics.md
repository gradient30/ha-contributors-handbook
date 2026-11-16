---
title: 实施诊断
description: 黄金规则诊断:用户可以下载诊断,敏感数据进行编辑.
sidebarLabel: 诊断
sidebarGroup: 黄金
order: 2
---

# 实施诊断 {#implement-diagnostics}

这是黄金规则 在`quality_scale.yaml`中,它被称为`diagnostics`.

集成执行 [诊断](/glossary/diagnostics): a `diagnostics.py` 与 `async_get_config_entry_diagnostics`, `async_get_device_diagnostics` 或两者兼有 。 诊断包含有助于调试一个问题的信息,如配置和收到的集成数据. 它们绝不能包含敏感信息,如密码、信使或坐标。

## 为什么这很重要 {#why-it-matters}

当某事不起作用时,诊断让一个用户用一个选择下载一个集成的快照,并附在一个问题上. 没有它,你最终要求 日志,版本,和有效载荷几轮。 有了它,第一份报告往往包含 你需要的一切。

用户在公共议题中共享这些文件,因此编辑是规则的一部分,而不是额外的.

## 示例 {#example}

在返回数据前用 `async_redact_data` 重写敏感密钥 :

```python
TO_REDACT = {CONF_API_KEY, CONF_LATITUDE, CONF_LONGITUDE}

async def async_get_config_entry_diagnostics(
    hass: HomeAssistant, entry: MyConfigEntry
) -> dict[str, Any]:
    """Return diagnostics for a config entry."""
    coordinator = entry.runtime_data

    return {
        "entry_data": async_redact_data(entry.data, TO_REDACT),
        "data": async_redact_data(coordinator.data.to_dict(), TO_REDACT),
    }
```

`async_redact_data`来自`homeassistant.components.diagnostics`。 它取代匹配密钥的值,同样在嵌入式词典和列表中.

## 如何检查 {#how-it-is-checked}

- Pylint, 当规则是 `done` 时 : `diagnostics.py` 必须执行 `async_get_config_entry_diagnostics` 或 `async_get_device_diagnostics` (`home-assistant-missing-diagnostics`) 。
- Codecov要求每个集成的`diagnostics.py`中更改的线路100%的测试覆盖. 大多数的整合用快照测试他们的诊断.
- 是否输入了正确的数据,敏感数据是否退出,将接受审查。

## 例外 {#exceptions}

如果集成没有有助于调试的数据,例如因为它没有运行时间数据,其配置只包含敏感信息,则该规则不适用.
