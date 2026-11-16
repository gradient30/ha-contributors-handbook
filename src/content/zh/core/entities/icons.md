---
title: 图标
description: 在图标.json中给跟随其状态的实体图标翻译,以及何时使用图标属性。
sidebarLabel: 图标
sidebarGroup: 基础
order: 6
---



# 图标 {#icons}
每个实体都有图标. Home Assistant 使用 [材料设计图标](https://pictogrammers.com/library/mdi/), 写成 `mdi:` 之后是图标的名称, 如 `mdi:water-pump` 。

在大多数情况下,你不需要做任何事情。 Home Assistant从域,设备类,实体状态中选择一个图标:一个门传感器显示一个开着的或闭着的门,一个温度传感器显示一个温度计. 符合要求时要遵守规定 他们让你的实体看起来像其他同类实体, 帮助人们找到他们的方式。

当您的实体需要自己的图标时,请使用图标翻译. 无论你选择什么,用户总是可以在实体设置中设置自己的图标,他们的胜利.

## 图标翻译 {#icon-translations}

在您整合的 `strings.json` 旁边的 `icons.json` 文件中, 图标将 [翻译密钥](/glossary/translation-key) 映射到图标 。 他们的工作就像被翻译的状态,但给一个图标而不是一个词.

```json
{
  "entity": {
    "sensor": {
      "moon_phase": {
        "default": "mdi:moon-full",
        "state": {
          "new_moon": "mdi:moon-new",
          "first_quarter": "mdi:moon-first-quarter",
          "last_quarter": "mdi:moon-last-quarter"
        }
      }
    }
  }
}
```

实体通过翻译密钥把它捡起来 :

```python
class MoonPhaseSensor(SensorEntity):
    _attr_has_entity_name = True
    _attr_translation_key = "moon_phase"
```

- `default` 当没有状态匹配时使用 。 没有它,实体就回到其域和设备类的图标.
- `state` 地图为图标。 状态密钥是`snake_case`,就像所有翻译密钥一样. 在此不要重复默认图标: 状态图标与默认相同 。

### 数字状态图标 {#icons-for-numeric-states}

对于数态,像电池级别或填充百分比一样,使用`range`而不是列出每个值. 键是按上升顺序排列的数字。 前端选择高于当前值的最高键的图标,并对低于最低键的值使用`default`.

```json
{
  "entity": {
    "sensor": {
      "tank_level": {
        "default": "mdi:gauge-empty",
        "range": {
          "25": "mdi:gauge-low",
          "50": "mdi:gauge",
          "90": "mdi:gauge-full"
        }
      }
    }
  }
}
```

在 `state` 中精确的比对仍然胜过 `range` 。

### 状态属性图标 {#icons-for-state-attributes}

一些属性在前端获得一个图标,比如一个气候实体的预设模式或扇子模式. 在 `state_attributes` 和 `range` 键下添加, 键为相同的 `default` 、 `state` 和 `range` :

```json
{
  "entity": {
    "climate": {
      "heat_pump": {
        "state_attributes": {
          "preset_mode": {
            "default": "mdi:thermostat",
            "state": {
              "vacation": "mdi:beach",
              "night": "mdi:weather-night"
            }
          }
        }
      }
    }
  }
}
```

这只对带有图标的前端显示属性有效 。 它不给任意属性一个图标.

## 图标属性 {#the-icon-property}

您也可以设置 `icon` 属性, 或 `_attr_icon` 。 它覆盖图标翻译,设备类,以及实体状态. 因为它是代码, 它可以依赖于任何:

```python
from homeassistant.util import dt as dt_util

class ExampleSensor(SensorEntity):
    @property
    def icon(self) -> str:
        """Show a moon at night."""
        if dt_util.now().hour < 7:
            return "mdi:weather-night"
        return "mdi:weather-sunny"
```

偏爱图标翻译. 它们将图标保留在状态对象之外,因此它们不会最终在数据库中记录每个状态变化,前端可以在状态发生前显示正确的图标,比如在历史或状态选择器中. `icon` 属性不能给状态属性图标 。

## 实体平台 {#for-entity-platforms}

一个实体平台,如`sensor`或`light`,在自己的`icons.json`中,在`entity_component`下定义了其域的默认图标. `_`键是域的默认值,其他键是设备类. 你只有在研究域本身时才会碰它。

关于图标在界面中的外观和行为,请参见设计区的[状态图标](/design/components/state-icon).
