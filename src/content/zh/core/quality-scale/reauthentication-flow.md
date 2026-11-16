---
title: 来自UI的再认证
description: Silver规则重校正-流量:用户可以输入新的证书而不移除整合.
sidebarLabel: 重新校正流量
sidebarGroup: 银
order: 9
---

# 来自UI的再认证 {#reauthenticate-from-the-ui}

这是Silver的规则 在`quality_scale.yaml`中,它被称为`reauthentication-flow`.

当集成证书停止工作时,集成必须启动[重新校正](/glossary/reauthentication)流. 在该流中,用户输入新的证书,集成测试,并更新和重新加载现有的[配置条目](/glossary/config-entry).

## 为什么这很重要 {#why-it-matters}

人们更改密码,API令牌失效. 没有再校正流,整合只是停止了工作,唯一的修补就是去掉它,重新设置. 这样就失去了实体的定制,在路上打破了仪表板和自动化.

随着重新校正的流,整合出现在**Settings** >下. ** 需要注意的设备和服务。 用户输入新密码,一切照旧运行.

## 示例 {#example}

重新校正流在集成产生`ConfigEntryAuthFailed`时开始,在设置时或在一个协调器更新中开始. 见[设置前测试](/core/quality-scale/test-before-setup). 然后在配置流中运行 `async_step_reauth` :

```python
class MyConfigFlow(ConfigFlow, domain=DOMAIN):
    """Config flow for My integration."""

    async def async_step_reauth(
        self, entry_data: Mapping[str, Any]
    ) -> ConfigFlowResult:
        """Start reauthentication after an authentication error."""
        return await self.async_step_reauth_confirm()

    async def async_step_reauth_confirm(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Ask for a new API token."""
        errors: dict[str, str] = {}
        if user_input is not None:
            entry = self._get_reauth_entry()
            client = MyClient(
                entry.data[CONF_HOST], user_input[CONF_API_TOKEN]
            )
            try:
                account_id = await client.get_account_id()
            except MyAuthError:
                errors["base"] = "invalid_auth"
            except MyConnectionError:
                errors["base"] = "cannot_connect"
            else:
                await self.async_set_unique_id(account_id)
                self._abort_if_unique_id_mismatch(reason="wrong_account")
                return self.async_update_reload_and_abort(
                    entry, data_updates=user_input
                )

        return self.async_show_form(
            step_id="reauth_confirm",
            data_schema=probatio.Schema(
                {probatio.Required(CONF_API_TOKEN): str}
            ),
            errors=errors,
        )
```

这里的一些细节很重要:

- 流量在保存它们之前就测试新的证书,就像配置流量一样.
- `_abort_if_unique_id_mismatch` 无意中阻止用户使用不同的账户登录, 这将将数据转换到所有实体的后面。
- 的男人 `async_update_reload_and_abort` 更新条目, 重新装入, 并结束 `reauth_successful` 原因 。

## 如何检查 {#how-it-is-checked}

- Pylint, 当规则是 `done` 时 : `config_flow.py` 必须执行 `async_step_reauth` (`home-assistant-missing-reauthentication-flow`) 。
- 重校正流向[配置- 流量- 测试- 覆盖](/core/quality-scale/config-flow-test-coverage)的测试, 和Codecov 要求每个更改的 `config_flow.py` 的行都被覆盖 。
- 其余的经过审查。

## 例外 {#exceptions}

如果整合 爸爸不需要任何形式的认证,则该规则不适用.

## 相关规则 {#related-rules}

- [配置流量](/core/quality-scale/config-flow):从UI设置有配置流.
- [提交的文件 你还好吗?](/core/quality-scale/test-before-configure):测试配置流中的连接.
- {L刚好} : 完全测试配置流 。
- [设置前测试](/core/quality-scale/test-before-setup):在设置时检查连接.
- [重组流程](/core/quality-scale/reconfiguration-flow):从UI重新配置.
