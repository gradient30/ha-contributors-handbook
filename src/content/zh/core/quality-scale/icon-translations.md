---
title: 使用图标翻译
description: 黄金规则图标-翻译:实体图标在图标.json中定义.
sidebarLabel: 图标翻译
sidebarGroup: 黄金
order: 18
---

# 使用图标翻译 {#use-icon-translations}

这是黄金规则 在`quality_scale.yaml`中,它被称为`icon-translations`.

需要自己图标的实体从 `icons.json` 获得, 由它们的 [翻译密钥](/glossary/translation-key) 获得, 而不是在 Python 中设置 `icon` 。 这个名字听起来很奇怪:没有翻译。 翻译密钥只是将一个实体与它的图标联系起来的引用,和将一个实体与它的名称联系起来的方式一样.

`icons.json` 可以设置默认图标,每个状态的图标,对于数字实体,每个数值范围的图标. 它还可以为状态属性的值设置图标,比如气候实体的预设模式.

> [!NOTE]
> 实体也从其设备类获得图标. 当实体完全是指设备类时,保留该图标. PM2.5传感器不需要自己的图标.

## 为什么这很重要 {#why-it-matters}

图标曾经是实体状态的一部分,每更新一次就写给国家机器,尽管几乎从未改变过. 通过图标翻译,前端从状态中选择图标,因此状态机器的工作较少. 集成的图标都在一个文件中,它们很容易审查并更改。

## 示例 {#example}

实体设置一个翻译密钥 :

```python
class MyPollenSensor(SensorEntity):
    """The tree pollen level."""

    _attr_has_entity_name = True
    _attr_translation_key = "tree_pollen"
```

`icons.json` 给它默认图标, 和 `high` 状态的另一个图标 :

```json
{
  "entity": {
    "sensor": {
      "tree_pollen": {
        "default": "mdi:tree",
        "state": {
          "high": "mdi:tree-outline"
        }
      }
    }
  }
}
```

对于一个数值实体, `range` 选择最大范围值小于或等于状态的图标 :

```json
{
  "entity": {
    "sensor": {
      "water_level": {
        "default": "mdi:water-off",
        "range": {
          "0": "mdi:water-outline",
          "50": "mdi:water-percent",
          "90": "mdi:water"
        }
      }
    }
  }
}
```

60的状态显示 `mdi:water-percent`, 以及90到90的任何东西显示 `mdi:water`. 当状态低于最小范围,无法使用,或者没有数字时,即使用默认. 范围键可以是整数或十进制数,如`"0.5"`,必须依次递增. 当一个实体同时拥有 `state` 和 `range` 图标时, `state` 图标获胜 。

## 如何检查 {#how-it-is-checked}

- Hassfest 验证 `icons.json`: 格式、 范围密钥必须是数字并按上升顺序排列, 状态图标必须与默认图标不同 。
- Pylint 失败于不存在的 {H0natural} 图标, 在 `icons.json` (`home-assistant-mdi-icon-json-not-found`) 和 Python 代码 (`home-assistant-mdi-icon-not-found`) 中.
- 是否在 Python 中设置属于 `icons.json` 的图标会被检查 。

## 例外 {#exceptions}

- 如果合并没有实体,则不适用这一规则。
- 如果实体不使用自己的图标,例如因为其设备类的图标适合,则该规则不适用.

## 相关规则 {#related-rules}

- [实体翻译](/core/quality-scale/entity-translations): 翻译实体名称.
- [实体设备类](/core/quality-scale/entity-device-class): 使用设备类.
