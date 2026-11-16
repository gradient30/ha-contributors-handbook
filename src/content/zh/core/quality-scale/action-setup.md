---
title: 在 async setup 中注册动作
description: '青铜法则动作设置: 动作在集成负载时进行注册, 而不是按照配置条目进行。'
sidebarLabel: 动作设置
sidebarGroup: 青铜
order: 1
---

# 在 async setup 中注册动作 {#register-actions-in-async_setup}

此是铜法. 在`quality_scale.yaml`中,它被称为`action-setup`.

如果集成添加了自己的 [动作](/glossary/action) , 它会在 `async_setup` 中注册,而不是 `async_setup_entry` 。 动作在集成负载时立即存在, 无论一个 [配置条目](/glossary/config-entry) 是否装入 。 校验发生在动作内: 检查它的目标配置条目是否存在并装入, 并提升 `ServiceValidationError` 当它不是,或者输入在其他情况下无效时。

## 为什么这很重要 {#why-it-matters}

许多集成在 `async_setup_entry` 中注册其动作, 在 `async_unload_entry` 中再次删除它们 。 这意味着动作只有在一个条目被装入时才存在. 当设备在启动时下线时,动作缺失,并且Home Assistant无法验证使用它的自动化和脚本. 用户得到一个模糊的"行动找不到",而不是一个明确的理由.

在 `async_setup` 中注册的动作总是有的 。 当条目未加载时,动作本身会告诉用户它为什么无法运行.

## 示例 {#example}

注册 `services.py` 中的动作, 在一个名为 `async_setup_services` 的函数中 。 它是一个同步函数,由{H2 没事的,它只需要`hass` :

```python title="services.py"
@callback
def async_setup_services(hass: HomeAssistant) -> None:
    """Register the actions of My integration."""

    async def async_get_schedule(call: ServiceCall) -> ServiceResponse:
        """Get the schedule of a device."""
        entry: MyConfigEntry = service.async_get_config_entry(
            hass, DOMAIN, call.data[ATTR_CONFIG_ENTRY_ID]
        )
        schedule = await entry.runtime_data.client.get_schedule()
        return {"schedule": schedule}

    hass.services.async_register(
        DOMAIN,
        SERVICE_GET_SCHEDULE,
        async_get_schedule,
        schema=SERVICE_GET_SCHEDULE_SCHEMA,
        supports_response=SupportsResponse.ONLY,
    )
```

`service.async_get_config_entry`从`homeassistant.helpers.service`做检查。 当条目不存在,属于另一个集成,或者没有加载时,它会提出一个翻译的`ServiceValidationError`.

在 `__init__.py` 中调用函数 `async_setup` 。 仅由UI设置的集成还需要一个`CONFIG_SCHEMA`,上面写着:

```python title="__init__.py"
CONFIG_SCHEMA = cv.config_entry_only_config_schema(DOMAIN)

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up My integration."""
    async_setup_services(hass)
    return True
```

## 如何检查 {#how-it-is-checked}

- Pylint 在 `async_setup_entry` (`home-assistant-service-registered-in-setup-entry`) 中注册动作时会发出警告.
- Pylint 警告 页 次 `services.py` (`home-assistant-action-registered-outside-services-module`) 以外的动作注册时.
- 当 `async_setup_services` 没有在示例除其他事项外的形状 (`home-assistant-invalid-setup-services`) 时, Pylint 警告 。
- 对行动中的检查进行核查。

## 例外 {#exceptions}

如果合并没有登记任何自己的行动,则不适用这一规则。

## 相关规则 {#related-rules}

- [动作例外](/core/quality-scale/action-exceptions) : 在动作失败时提出例外 。
