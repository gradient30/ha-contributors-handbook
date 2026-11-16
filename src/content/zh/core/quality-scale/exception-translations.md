---
title: 翻译例外消息
description: 黄金规则例外-翻译:向用户显示的错误来自字符串.json,所以可以翻译.
sidebarLabel: 例外翻译
sidebarGroup: 黄金
order: 17
---

# 翻译例外消息 {#translate-exception-messages}

这是黄金规则 在`quality_scale.yaml`中,它被称为`exception-translations`.

到达用户的例外是可转换的。 提升`HomeAssistantError`,或像`ServiceValidationError`一样的子类,带有`translation_domain`和`translation_key`,而不是硬编码的英文消息,并将消息放入`strings.json`的`exceptions`部分.

## 为什么这很重要 {#why-it-matters}

当动作失败时,用户会在界面中看到错误消息. 对于使用自己语言运行Home Assistant的用户来说,翻译界面中间的英语错误更难理解,确切地说,在他们需要理解出什么错误的时刻.

从 `HomeAssistantError` 继承到支持从框中翻译的例外, 因此它只需要一个键和一个字符串 。

## 示例 {#example}

```python
async def async_set_schedule(call: ServiceCall) -> None:
    """Set the schedule for a day."""
    start = call.data[ATTR_START_DATE]
    end = call.data[ATTR_END_DATE]
    if end < start:
        raise ServiceValidationError(
            translation_domain=DOMAIN,
            translation_key="end_before_start",
        )

    try:
        await client.set_schedule(start, end)
    except MyConnectionError as err:
        raise HomeAssistantError(
            translation_domain=DOMAIN,
            translation_key="cannot_connect",
            translation_placeholders={"error": str(err)},
        ) from err
```

`strings.json`:

```json
{
  "exceptions": {
    "end_before_start": {
      "message": "The end date can't be before the start date."
    },
    "cannot_connect": {
      "message": "Could not connect to the device: {error}"
    }
  }
}
```

不要也传递消息:用翻译密钥,消息来自`strings.json`.

## 如何检查 {#how-it-is-checked}

- Pylint, 当规则是 `done` 时: 提出 `HomeAssistantError` 或带有硬码消息的子类被标记 (`home-assistant-exception-not-translated`) 。
- Pylint,对于每个集成:翻译密钥必须存在于`strings.json`(`home-assistant-exception-translation-key-missing`),`translation_domain`和`translation_key`的 `translation_key` 的 `home-assistant-exception-translation-key-domain-mismatch` 的 `exceptions` 一节中,占位符必须匹配信件(`home-assistant-exception-placeholder-mismatch`),并且一个翻译密钥(`home-assistant-exception-message-with-translation`)的旁边不得有消息.
- 当某个动作引起一个缺失翻译的例外时,测试失败.

## 例外 {#exceptions}

如果合并 我没事例外,则该规则不适用。

## 相关规则 {#related-rules}

- [实体翻译](/core/quality-scale/entity-translations): 翻译实体名称.
- [动作例外](/core/quality-scale/action-exceptions) : 在动作失败时提出例外 。
