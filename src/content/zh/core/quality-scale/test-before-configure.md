---
title: 在配置流中测试连接
description: 青铜规则测试-配置前:配置流在创建条目前测试连接.
sidebarLabel: 提交的文件 你还好吗?
sidebarGroup: 铜
order: 18
---

# 在配置流中测试连接 {#test-the-connection-in-the-config-flow}

此是铜法. 在`quality_scale.yaml`中,它被称为`test-before-configure`.

在 [配置流量](/glossary/config-flow) 创建配置项之前通话, 它必须测试整合可以连接到用户输入的内容 。 当测试失败时,流会再次以错误显示表单,从而告诉用户出了什么错误.

## 为什么这很重要 {#why-it-matters}

一个接受任何东西的配置流给用户留下了一个不起作用的集成,并且不知道为什么. 许多问题在此时很容易被抓住:IP地址中的typo,错误的端口,路上的防火墙,DNS问题,错误的证书,或者不支持的设备. 在这里捕捉它们,虽然用户仍在查看表格,但比以后日志中的一个错误要友好得多.

## 示例 {#example}

通 知

```python
async def async_step_user(
    self, user_input: dict[str, Any] | None = None
) -> ConfigFlowResult:
    """Handle a flow started by the user."""
    errors: dict[str, str] = {}
    if user_input is not None:
        client = MyClient(
            user_input[CONF_HOST], async_get_clientsession(self.hass)
        )
        try:
            await client.get_device_info()
        except MyConnectionError:
            errors["base"] = "cannot_connect"
        except MyAuthenticationError:
            errors["base"] = "invalid_auth"
        except Exception:
            LOGGER.exception("Unexpected exception")
            errors["base"] = "unknown"
        else:
            return self.async_create_entry(
                title="My integration", data=user_input
            )

    return self.async_show_form(
        step_id="user",
        data_schema=probatio.Schema({probatio.Required(CONF_HOST): str}),
        errors=errors,
    )
```

错误键在 `strings.json` 中, 在 `config.error` 下 。 像`cannot_connect`,`invalid_auth`和`unknown`这样的常见错误,都与`[%key:common::config_flow::error::cannot_connect%]`共享了翻译。

## 如何检查 {#how-it-is-checked}

- Pylint, 当规则是 `done` 时 : `home-assistant-missing-test-before-configure` 当一个配置流创建条目但未显示报告失败的迹象时警告 : 没有 `errors=` 传递到一个表单, 没有在 `except` 内中止 。 OAuth2 流量被跳过,因为符号交换是连接测试.
- 对设备的测试是否合理进行复核。

## 例外 {#exceptions}

- 与设备或服务不连接的集成, 如 [帮助者](/glossary/helper) , 没有任何测试和豁免 。
- 在运行时发现其设备的集成,没有用户的连接细节(如Google Cast),则免责.

## 相关规则 {#related-rules}

- [配置流量](/core/quality-scale/config-flow):从UI设置有配置流.
- [唯一配置输入](/core/quality-scale/unique-config-entry) : 防止重复配置条目 。
- {L刚好} : 完全测试配置流 。
- [发现](/core/quality-scale/discovery):支持发现.
- [重新校正流量](/core/quality-scale/reauthentication-flow):从UI中重新认证.
- [重组流程](/core/quality-scale/reconfiguration-flow):从UI重新配置.
