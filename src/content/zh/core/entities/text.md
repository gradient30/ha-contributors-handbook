---
title: 文本实体
description: 构建一个文本实体,让人们在设备上设置短文本值,比如显示消息或网络名称.
sidebarLabel: 文本
sidebarGroup: 输入与助手
---

# 文本实体 {#text-entity}

一个文本实体允许人们在一个设备或服务上设定文本值,比如显示中的信息,网络名称,或者PIN代码. 从`TextEntity` 继承到`homeassistant.components.text` 。

文本实体具有保留值。 如果您想要发送一个消息, 它一发送就会消失, 就像一个推动通知, 请使用 [通知](/core/entities/notify) 实体 。

## 的临时议程 {#properties}

| 名称 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- |
| `native_value` | `str \| None` | 要求数 | 现文. |
| `native_min` | `int` | `0` | 最小字符数,包含. |
| `native_max` | `int` | `255` | 最大字符数,包含在内. 超过255的值上限为255,最长的状态Home Assistant可以存储. |
| `pattern` | `str \| None` | `None` | 值必须匹配的正则表达式 。 它被 `re.match` 选中, 因此它只在开始时锁定: 以 `$` 结尾, 以匹配整个值 。 |
| `mode` | `TextMode` | `TextMode.TEXT` | 前端如何显示字段 : `TextMode.TEXT` 用于纯文本, 或 `TextMode.PASSWORD` 用于隐藏您输入的内容 。 |

每个实体的通用属性,如`name`,`available`和`unique_id`,都在[实体类别](/core/entities/entity-class)上.

> [!NOTE]
> `TextMode.PASSWORD`只在前端隐藏输入. 值仍然是实体的状态,任何能看见实体并存储在历史中的人都可以读取. 不要用文字实体来获取真正的秘密.

## 支持的特性 {#supported-features}

该实体没有支持的特性。

## 方法 {#methods}

### 设定值 {#set-value}

当有人更改UI中的文本时调用,或者一个自动化或脚本调用`text.set_value`动作时调用. 实施其中之一。

```python
class MyText(TextEntity):
    

# Implement one of these methods. {#states}

    def set_value(self, value: str) -> None:
        """Set the text value."""

    async def async_set_value(self, value: str) -> None:
        """Set the text value."""
```

动作在调用您的方法之前, 对照 `native_min` 、 `native_max` 和 `pattern` 检查值 。 不符合 `ServiceValidationError` 的值会上升, 您的方法不会被调用 。

## 状态 {#restoring-the-value}

州为`native_value`. 它是`unknown` 当`native_value`是`None`时。

当状态被写入时, 相同的检查会运行在您自己的值上 : `native_value` 太短, 太长, 或者不匹配 `pattern` 升起 `ValueError` 。 确保设备报告符合您设定的限制 。

模式,最小值,最大值,以及模式都是能力属性:它们被写入[非常大实体登记处](/core/entities/registry),并被排除在记录器历史之外.

## 在国际范围内恢复该值 {#example}

如果文本生活在 Home Assistant 而不是设备上, 请继承 `RestoreText` 。 在 `async_added_to_hass` 中调用 `await self.async_get_last_text_data()` 以获得最后一个 `native_value` 、 `native_min` 和 `native_max` 重启后返回 。 它返回`None` 当没有可以恢复的。

## 示例 {#示例}

```python
from homeassistant.components.text import TextEntity
from homeassistant.const import EntityCategory

class ExampleDisplayMessage(TextEntity):
    """The message on the display of the device."""

    _attr_has_entity_name = True
    _attr_translation_key = "display_message"
    _attr_entity_category = EntityCategory.CONFIG
    _attr_native_max = 32

    def __init__(self, device: ExampleDevice) -> None:
        """Initialize the text entity."""
        self._device = device
        self._attr_unique_id = f"{device.serial}_display_message"
        self._attr_native_value = device.message

    async def async_set_value(self, value: str) -> None:
        """Set the message on the display."""
        await self._device.set_message(value)
        self._attr_native_value = value
        self.async_write_ha_state()
```
