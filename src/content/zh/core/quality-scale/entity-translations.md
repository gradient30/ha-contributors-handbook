---
title: 翻译实体名称
description: 黄金规则实体翻译:实体名称来自字符串. json,因此可以翻译.
sidebarLabel: 实体翻译
sidebarGroup: 金
order: 16
---

# 翻译实体名称 {#translate-entity-names}

这是黄金规则 在`quality_scale.yaml`中,它被称为`entity-translations`.

实体从 `strings.json` 获得它们的名字, 通过 [翻译密钥](/glossary/translation-key), 而不是 Python 的硬码英文名称 。 Home Assistant的翻译者然后将这些名字翻译成它支持的每一种语言.

## 为什么这很重要 {#why-it-matters}

Home Assistant在世界各地使用,许多人使用英语以外的语言. 在荷兰语,日语或巴西语界面中称为"阶段电压"的实体是一件小事,但其中几百个使Home Assistant感觉它不是为你制造的.

翻译名称只适用于设置为 `has_entity_name` `True` 的实体, 这是 [有实体名称](/core/quality-scale/has-entity-name) 规则 。

## 示例 {#example}

设置实体上的翻译密钥 :

```python
class MyVoltageSensor(SensorEntity):
    """The phase voltage of My device."""

    _attr_has_entity_name = True
    _attr_translation_key = "phase_voltage"
```

按平台和翻译键在`entity`中添加名称:

```json
{
  "entity": {
    "sensor": {
      "phase_voltage": {
        "name": "Phase voltage"
      }
    }
  }
}
```

使用名为"我的设备"的设备,实体显示为"我的设备相位电压".

在 `binary_sensor`, `button`, `event`, `infrared`, `number`, `sensor` 或 `update` 平台上带有设备类的实体, 当设备类的名称适合时, 不需要翻译密钥 。 它以设备类命名,如"Temperature",该名称已经翻译. 这不适用于 `enum` 设备类的传感器 。

谧 见[让你的弦可变](/translate/guides/developers) 如何写出翻译可以使用的字符串 。

## 如何检查 {#how-it-is-checked}

- Hassfest 验证 `strings.json` 的格式 。
- Pylint警告当一个翻译密钥只重复设备类的名称(`home-assistant-redundant-translation-key`)时.
- 检查每个实体是否有译名 。

## 例外 {#exceptions}

- 如果合并没有实体,则不适用这一规则。
- 如果这些实体只有用户定义自己的名字,无法翻译,则该规则不适用.
- 如果所有实体都使用它们设备的名称,带有`_attr_name = None`,则此规则不适用.

## 相关规则 {#related-rules}

- [有实体名称](/core/quality-scale/has-entity-name):使用有 实体 名称。
- [实体设备类](/core/quality-scale/entity-device-class): 使用设备类.
- [图标翻译](/core/quality-scale/icon-translations): 使用图标翻译 。
- [例外翻译](/core/quality-scale/exception-translations) : 翻译例外消息 。
