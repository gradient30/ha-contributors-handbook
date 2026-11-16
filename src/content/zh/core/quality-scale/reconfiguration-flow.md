---
title: 焕然一新
description: Gold 规则重组-流量:用户可以更改一个条目的设置而不删除它.
sidebarLabel: 重组流程
sidebarGroup: 黄金
order: 19
---

# 焕然一新 {#reconfigure-from-the-ui}

这是黄金规则 在`quality_scale.yaml`中,它被称为`reconfiguration-flow`.

配置流有 [重新配置步骤](/glossary/reconfigure-flow) : `async_step_reconfigure` 。 它允许用户从集成项的菜单中,像设备的主机一样,在设置过程中更改所输入的内容,而无需移除并再次设置.

## 为什么这很重要 {#why-it-matters}

事情变了 一个设备获得一个新的IP地址,一个用户将一个服务移动到另一个服务器. 最理想的是,Home Assistant通知和要求用户采取行动,通过发现或重新校正. 这并非总是可能的。 重新配置的流量让用户可以自行修复,并保持自己的实体,历史和自动化.

取消和添加一个集成再次失去其实体的所有定制。 没有人应该这样做 对于一个新的IP地址。

## 示例 {#example}

重新配置步骤测试新输入,确定它仍然是同一个设备或账户,并更新条目:

```python
async def async_step_reconfigure(
    self, user_input: dict[str, Any] | None = None
) -> ConfigFlowResult:
    """Handle reconfiguration of the integration."""
    errors: dict[str, str] = {}
    if user_input is not None:
        client = MyClient(user_input[CONF_HOST])
        try:
            serial = await client.get_serial()
        except MyConnectionError:
            errors["base"] = "cannot_connect"
        else:
            await self.async_set_unique_id(serial)
            self._abort_if_unique_id_mismatch(reason="wrong_device")
            return self.async_update_reload_and_abort(
                self._get_reconfigure_entry(),
                data_updates=user_input,
            )

    return self.async_show_form(
        step_id="reconfigure",
        data_schema=probatio.Schema({probatio.Required(CONF_HOST): str}),
        errors=errors,
    )
```

`_abort_if_unique_id_mismatch` 阻止用户将条目指向不同的设备 。 `async_update_reload_and_abort`更新数据,重新装入条目,并以`reconfigure_successful`理由结束流量。

使用当前值预先填充表单,使用 `self.add_suggested_values_to_schema`,所以用户只更改自己需要的.

## 如何检查 {#how-it-is-checked}

- Hassfest, 当规则是 `done` 时: 配置流必须有一个 `async_step_reconfigure` 。
- Codecov要求对`config_flow.py`中更改的行进行100%的测试覆盖,因此重构步骤需要测试,包括从错误中恢复. 见[配置- 流量- 测试- 覆盖](/core/quality-scale/config-flow-test-coverage).

## 例外 {#exceptions}

- 在其配置流中没有设置的集成可免于此规则.
- 唯一设置为资质的集成,再校正流柄的集成,不受此规则约束.
- 如果每次更改都需要新的配置条目,则该规则不在此列。

## 相关规则 {#related-rules}

- [配置流量](/core/quality-scale/config-flow):从UI设置有配置流.
- [提交的文件 你还好吗?](/core/quality-scale/test-before-configure):测试配置流中的连接.
- [唯一配置输入](/core/quality-scale/unique-config-entry) : 防止重复配置条目 。
- {L刚好} : 完全测试配置流 。
- [重新校正流量](/core/quality-scale/reauthentication-flow):从UI中重新认证.
