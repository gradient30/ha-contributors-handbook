---
title: 重新认证与重新配置
description: 让用户固定已过期的证书,并更改一个已有配置条目的连接细节,而不删除并再次添加.
sidebarLabel: 重新认证与重新配置
sidebarGroup: 设置与配置
order: 6
---

# 重整和重组 {#reauthentication-and-reconfiguration}

事情在设定后会变 一个密码过期,一个令牌被吊销,一个设备移动到一个新的IP地址. 您配置流程的两个特殊步骤 我知道, 两种步骤都更新已有的配置条目, 而不是创建一个新的 :

- ** 重新校正** (`reauth`) 校正全权证书。 Home Assistant 当您的整合报告认证失败时开始 。
- ** 重新配置** (`reconfigure`) 更改其他设置数据, 如主机 。 用户从配置条目的菜单开始.

选择权也一样。 在 [选项流动](/core/integrations/options-flow) 中改变集成行为方式的设置 。

两者都是[质量尺度](/core/quality-scale)的规则: 重新校正是Silver的一部分,重新配置Gold.

## 重新校正 {#reauthentication}

### 开始吧 {#start-it}

当您的证书不再工作抒发时, 从 `async_setup_entry` 或 从您的 [协调员](/core/integrations/fetching-data) 的 `_async_update_data` 升起 `ConfigEntryAuthFailed` 。 Home Assistant 使条目处于错误状态并启动 [重新校正](/glossary/reauthentication) 流量 。 在其他地方长大,它不会开始流动。

```python
async def async_setup_entry(
    hass: HomeAssistant, entry: ExampleConfigEntry
) -> None:
    """Set up Example from a config entry."""
    client = ExampleClient(entry.data[CONF_TOKEN])

    try:
        await client.login()
    except ExampleAuthError as err:
        raise ConfigEntryAuthFailed(
            translation_domain=DOMAIN,
            translation_key="invalid_token",
        ) from err
    ...
```

没有协调员,您也可以用 `entry.async_start_reauth(hass)` 启动流量 。

### 处理 {#handle-it}

流量从 `async_step_reauth` 开始, 并带有配置项的数据 。 显示窗体, 检查新证书, 并更新现有条目 :

```python
from collections.abc import Mapping

from homeassistant.config_entries import ConfigFlowResult

async def async_step_reauth(
    self, entry_data: Mapping[str, Any]
) -> ConfigFlowResult:
    """Start reauthentication."""
    return await self.async_step_reauth_confirm()

async def async_step_reauth_confirm(
    self, user_input: dict[str, Any] | None = None
) -> ConfigFlowResult:
    """Ask for a new token."""
    errors: dict[str, str] = {}

    if user_input is not None:
        try:
            account = await validate_token(user_input[CONF_TOKEN])
        except ExampleAuthError:
            errors["base"] = "invalid_auth"
        else:
            await self.async_set_unique_id(account.id)
            self._abort_if_unique_id_mismatch()

            return self.async_update_reload_and_abort(
                self._get_reauth_entry(),
                data_updates=user_input,
            )

    return self.async_show_form(
        step_id="reauth_confirm",
        data_schema=probatio.Schema({probatio.Required(CONF_TOKEN): str}),
        errors=errors,
    )
```

这里发生一些事情:

- `self._get_reauth_entry()` 返回需要新证书的配置项 。 `self.source == SOURCE_REAUTH`告诉你概览你正在重新校正
- `async_set_unique_id` 之后的`_abort_if_unique_id_mismatch()` 确保用户登录到同一个账户, 而不是另一个账户 。
- `async_update_reload_and_abort` 将 `data_updates` 合并到条目数据中, 重新装入条目, 用 `reauth_successful` 中止流量 。 将 `reload_even_if_entry_is_unchanged=False` 传递到仅在改变时重新装入 。

使用共享标题将步骤添加到 `strings.json` :

```json
{
  "config": {
    "step": {
      "reauth_confirm": {
        "title": "[%key:common::config_flow::title::reauth%]",
        "description": "The token for your Example account no longer works.",
        "data": {
          "token": "[%key:common::config_flow::data::api_token%]"
        }
      }
    }
  }
}
```

`reauth_successful` 和 `reconfigure_successful` 中止消息来自 Home Assistant 本身, 因此它们不会进入您的 `strings.json` 。 只有自定义的中止原因,作为 `reason` 传递, 需要自己的字符串 。 不过, 当用户登录到另一个账户时, 添加 `unique_id_mismatch` 中止原因 。

对于OAuth 2.0,重新校正再次通过服务登录发送用户. 见[奥奥特2.0](/core/integrations/oauth2#reauthentication).

### 试试看 {#test-it}

自动测试必须检查流量是否更新了现有的条目,而不是创建新的条目. 调用 `async_create_entry` 的重校正或重组流程会引发错误 。

要手工尝试, 请停止 Home Assistant, 编辑 `config/.storage/core.config_entries` 中存储的证书( 在您的配置副本上), 并重新开始 。 对 OAuth 2.0, 更改 `access_token`, `refresh_token` 或 `expires_at` 。

## 重新配置 {#reconfiguration}

添加 `async_step_reconfigure` 让用户像主机一样更改一个条目的设置数据 。 用户一旦该步骤存在,即可在配置条目的菜单中找到 ** 重新配置 **.

```python
async def async_step_reconfigure(
    self, user_input: dict[str, Any] | None = None
) -> ConfigFlowResult:
    """Change the host of an existing entry."""
    errors: dict[str, str] = {}
    entry = self._get_reconfigure_entry()

    if user_input is not None:
        try:
            device = await get_device(self.hass, user_input[CONF_HOST])
        except ExampleConnectionError:
            errors["base"] = "cannot_connect"
        else:
            await self.async_set_unique_id(device.serial_number)
            self._abort_if_unique_id_mismatch()

            return self.async_update_reload_and_abort(
                entry, data_updates=user_input
            )

    return self.async_show_form(
        step_id="reconfigure",
        data_schema=self.add_suggested_values_to_schema(
            STEP_USER_SCHEMA, entry.data
        ),
        errors=errors,
    )
```

它的工作原理与重校正相同: `self._get_reconfigure_entry()` 返回条目,`self.source == SOURCE_RECONFIGURE` 告诉你你在哪里, 唯一的ID检查可以确定它仍然是同一个设备, 流结束为`reconfigure_successful`.

许多集成共享`user`步骤和`reconfigure`步骤的代码,并检查`self.source`,以决定是创建还是更新条目.

## 不重新装入更新 {#update-without-reloading}

如果您的整合本身可以接收变化, 请使用 `async_update_and_abort` 代替 。 它需要相同的参数,除了`reload_even_if_entry_is_unchanged`,而不重新装入条目.
