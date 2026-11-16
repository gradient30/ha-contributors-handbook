---
title: 在动作失败时提出例外
description: Silver 规则动作例外:动作在失败时提高ServiceValidationError或HomeAssistantError.
sidebarLabel: 动作例外
sidebarGroup: 银
order: 1
---

# 在动作失败时提出例外 {#raise-exceptions-when-actions-fail}

这是Silver的规则 在`quality_scale.yaml`中,它被称为`action-exceptions`.

当 [动作](/glossary/action) 失败时, 集成必须提出例外, 而不是默默失败或只写入日志 。 提升 `ServiceValidationError` 当用户做错事时, 如通过无效输入或指向不存在的东西 。 提高 `HomeAssistantError` 当动作本身失败时, 如网络错误或设备报告的错误 。

这不仅仅是关于您所登记的行动。 实体动作也算数: 当打开 `light` 或按 `button` 失败时, 实体会提出例外 。

## 为什么这很重要 {#why-it-matters}

一个例外是用户唯一得知出错的方法. Home Assistant 在 UI 中显示其消息, 运行动作的自动化或脚本会以错误停止, 而不是像一切顺利一样继续下去 。

两种例外类型都说明是谁造成问题的. A `ServiceValidationError` 说用户可以通过更改输入来修正它. A `HomeAssistantError` 说动作在集成或设备一侧失败 。 UI将其报告为不同的错误,因此用户知道在哪里查看.

## 示例 {#example}

这一行动确定了时间表。 起始日期前的结束日期是用户错误. 连接错误是动作失败 :

```python
from homeassistant.exceptions import (
    HomeAssistantError,
    ServiceValidationError,
)

async def async_set_schedule(call: ServiceCall) -> None:
    """Set the schedule for a day."""
    start_date = call.data[ATTR_START_DATE]
    end_date = call.data[ATTR_END_DATE]
    if end_date < start_date:
        raise ServiceValidationError(
            translation_domain=DOMAIN,
            translation_key="end_before_start",
        )

    entry = service.async_get_config_entry(
        call.hass, DOMAIN, call.data[ATTR_CONFIG_ENTRY_ID]
    )
    try:
        await entry.runtime_data.set_schedule(start_date, end_date)
    except MyConnectionError as err:
        raise HomeAssistantError(
            translation_domain=DOMAIN,
            translation_key="cannot_connect",
        ) from err
```

实体行动也是如此:

```python
async def async_turn_on(self, **kwargs: Any) -> None:
    """Turn the switch on."""
    try:
        await self.client.turn_on()
    except MyConnectionError as err:
        raise HomeAssistantError(
            translation_domain=DOMAIN,
            translation_key="cannot_connect",
        ) from err
```

普通信息,如`HomeAssistantError("Cannot connect")`,足以执行此规则。 翻译信件,如例,是黄金规则[例外翻译](/core/quality-scale/exception-translations)要求的.

升起前不要登录错误。 Home Assistant已经报告过这个例外,所以记录它 以及两次报告。

## 如何检查 {#how-it-is-checked}

- Pylint 旗下动作处理器会抓住一个例外而不再次升起,比如一个空的`except`块,一个只日志的块,或者`contextlib.suppress` (`home-assistant-action-swallowed-exception`).
- 当错误记录在警告级别或更高时, Pylint 会在上升错误的同一块中提前(`home-assistant-log-and-raise`)发出警告.
- 是否提出实质内容的例外类型将接受审查。

## 例外 {#exceptions}

如果集成没有登记自己的动作,并且只有只读平台,如`sensor`和`binary_sensor`,则该规则不适用.

## 相关规则 {#related-rules}

- [例外翻译](/core/quality-scale/exception-translations) : 翻译例外消息 。
- [动作设置](/core/quality-scale/action-setup): 在 async setup 中注册动作 。
