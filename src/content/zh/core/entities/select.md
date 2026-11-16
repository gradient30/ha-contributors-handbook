---
title: 选择实体
description: 构建一个选择实体,让人们从固定列表中选择一个选项,就像操作模式一样.
sidebarLabel: 选择
sidebarGroup: 投入和帮助
---

# 选择实体 {#select-entity}

一个选定的实体允许人们从您集成提供的有限列表中选择一个选项,比如设备的操作模式或运动传感器的灵敏度. 从`SelectEntity` 继承到`homeassistant.components.select` 。

仅在没有平台适合时才使用选择 。 灯泡的效果可以是选择的,但它属于支持效果的[光线](/core/entities/light)实体上. 粉丝预设,气候模式,媒体播放器的源头也是如此.

## 的临时议程 {#properties}

| 名称 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- |
| `options` | `list[str]` | 要求数 | 人们可以选择选择 |
| `current_option` | `str \| None` | `None` | 现在选择的选项 。 |

您可以在 `SelectEntityDescription` 上设置 `options` 。 当属性或描述都没有aunte给出选项时,属性本身就是 `AttributeError` 。

每个实体的通用属性,如`name`,`available`和`unique_id`,都在[实体类别](/core/entities/entity-class)上.

## 支持的特性 {#supported-features}

该实体没有支持的特性。

## 翻译选项 {#translating-options}

选项是值,而不是供人们阅读的文本. 将它们变成小写 与土著人民 `eco` 或 `high_power` 一样, 在实体上设置 [翻译密钥](/glossary/translation-key), 并将每个选项翻译为 `strings.json` 状态 :

```json
{
  "entity": {
    "select": {
      "operating_mode": {
        "name": "Operating mode",
        "state": {
          "eco": "Eco",
          "high_power": "High power"
        }
      }
    }
  }
}
```

前端显示翻译,而自动化则继续使用稳定键. 见[43. 使您的字符串可转换](/translate/guides/developers) 和[帖式图标](/core/entities/icons) 给每个选项自己的图标 。

## 方法 {#methods}

### ى叶 {#select-option}

当有人在 U 她是 URI 中选择一个选项, 或者一个自动化或脚本调用 `select.select_option` 动作时调用 。 实施其中之一。

```python
class MySelect(SelectEntity):
    

# Implement one of these methods. {#states}

    def select_option(self, option: str) -> None:
        """Change the selected option."""

    async def async_select_option(self, option: str) -> None:
        """Change the selected option."""
```

基础类首先验证选项 : 您只获得 `options` 中的选项 。 在您的方法运行前, 任何其它的都会产生 `ServiceValidationError` 。

动作`select.select_first`,`select.select_last`,`select.select_next`和`select.select_previous`由基类处理. 他们从 `options` 和 `current_option` 制定新的选项, 并用它调用您的选择方法 。 你不执行它们。

## 状态 {#example}

州为`current_option`. 它是`unknown` 当`current_option`是`None`, 或当它不是`options`之一时。

`options`是一个能力属性:它被写到[非常大实体登记处](/core/entities/registry),并被从记录器历史中忽略.

## 示例 {#示例}

```python
from homeassistant.components.select import SelectEntity
from homeassistant.const import EntityCategory

class ExampleOperatingMode(SelectEntity):
    """The operating mode of a heat pump."""

    _attr_has_entity_name = True
    _attr_translation_key = "operating_mode"
    _attr_entity_category = EntityCategory.CONFIG
    _attr_options = ["eco", "comfort", "high_power"]

    def __init__(self, device: ExampleDevice) -> None:
        """Initialize the select."""
        self._device = device
        self._attr_unique_id = f"{device.serial}_operating_mode"
        self._attr_current_option = device.mode

    async def async_select_option(self, option: str) -> None:
        """Change the operating mode."""
        await self._device.set_mode(option)
        self._attr_current_option = option
        self.async_write_ha_state()
```
