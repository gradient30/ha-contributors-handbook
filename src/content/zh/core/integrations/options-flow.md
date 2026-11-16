---
title: 选项流
description: 让用户在设置后改变您的集成行为,并在完成后重新加载.
sidebarGroup: 设置和配置
order: 4
---

# 选项流 {#options-flow}

[选项流动](/glossary/options-flow) 让用户在设置后更改配置项的设置, 例如哪些设备包含或是否显示来宾 。 用户用条目的**配置**按钮打开. 选项最终在 `entry.options` 中 。

选择是整合如何进行。 更改其连接方式, 如新主机一样, 是 [重组](/core/integrations/reauth-reconfigure), 更改证书为 [重新校正](/core/integrations/reauth-reconfigure#reauthentication) 。 投票间隔也不是一个选项: 您为用户选择, 请参见 [适当投票](/core/quality-scale/appropriate-polling) 。

## ẩ然大波 {#add-an-options-flow}

返回配置流上的 `async_get_options_flow` 选项 。 选项流始于 `async_step_init`,并通过 `self.config_entry` 到达配置项 。

```python
from homeassistant.config_entries import (
    ConfigEntry,
    ConfigFlow,
    ConfigFlowResult,
    OptionsFlowWithReload,
)
from homeassistant.core import callback

OPTIONS_SCHEMA = probatio.Schema(
    {probatio.Required(CONF_SHOW_GUESTS, default=False): bool}
)

class ExampleConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Example."""

    @staticmethod
    @callback
    def async_get_options_flow(
        config_entry: ConfigEntry,
    ) -> ExampleOptionsFlow:
        """Create the options flow."""
        return ExampleOptionsFlow()

class ExampleOptionsFlow(OptionsFlowWithReload):
    """Handle the options of Example."""

    async def async_step_init(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Manage the options."""
        if user_input is not None:
            return self.async_create_entry(data=user_input)

        return self.async_show_form(
            step_id="init",
            data_schema=self.add_suggested_values_to_schema(
                OPTIONS_SCHEMA, self.config_entry.options
            ),
        )
```

`async_create_entry` 在选项流中不会创建新条目: 它存储 `data` 作为现有选项的新选项 。 `add_suggested_values_to_schema` 以当前选项填表。 文本在 `strings.json` 键下, 与 [配置流程文本](/core/integrations/flow-steps#labels-and-descriptions) 相同 。

选项流的 `__init__` 中没有配置项 。 在台阶中使用 `self.config_entry` 。

## 关于新选项的行动 {#act-on-new-options}

大多数集成需要重新加载才能使用新的选项. 扩展 `OptionsFlowWithReload` 而不是 `OptionsFlow`, 如上面的例子, 当选项改变时 Home Assistant 重新装入配置项 。

如果您的集成可以在不重新加载的情况下应用新选项,请扩展 `OptionsFlow`,并在设置条目时注册更新的收听器. 条目更新后运行,条目卸载时停止:

```python
async def async_setup_entry(
    hass: HomeAssistant, entry: ExampleConfigEntry
) -> None:
    """Set up Example from a config entry."""
    ...
    entry.async_on_unload(entry.add_update_listener(async_update_options))

async def async_update_options(
    hass: HomeAssistant, entry: ExampleConfigEntry
) -> None:
    """Apply the new options."""
    entry.runtime_data.show_guests = entry.options[CONF_SHOW_GUESTS]
```

不合并两者: 当条目有更新的倾听器时, `OptionsFlowWithReload` 产生错误 。 更新的收听器也被调用到条目的每一个其它更新上,所以如果有更新,它负责重装. Home Assistant 当重新配置或重新校正的流, 或发现更新条目时, 登录一个警告, 重新装入有更新倾听器的条目 。 该警告计划成为Home Assistant2026.12中的一个错误. 使用更新的听器重新装入条目的子条目重构流程已引起错误 。
