---
title: 进取号
description: nitity name, 翻译密钥, 设备类如何给您的实体一个名称, 以及Home Assistant 如何将它变成友好名称和实体ID 。
sidebarLabel: 命名
sidebarGroup: 基础
order: 2
---

# 进取号 {#naming-entities}

一个好的实体名称很短,只说实体是什么:"巴特里","权力使用","儿童锁". Home Assistant 自己在前面添加设备名称 。 你作为一个融合作者的工作是给实体一个简短的名字,以能够翻译的方式.

## 使用 `has_entity_name` {#use-hasentityname}

在每个实体上设定 `has_entity_name` 到`True` 。 新的一体化需要这种能力。 它告诉Home Assistant实体的名称只描述实体,而不是它所属的设备.

```python
class ExampleSensor(SensorEntity):
    _attr_has_entity_name = True
```

有了 `has_entity_name` 设定, 实体的名称是三件事之一 :

- ** 是的,它本身的名称**,如“Battery”,指在设备上属于几个实体之一的实体。 通过一个[翻译密钥](/core/entities/naming#translated-names)。
- QQH0}**,为作为其设备主要特征的实体,如智能灯泡的光. 实体然后取设备的名称.
- ** 未设置**, 对于一些平台: 实体随后以 [设备类](/core/entities/naming#names-from-the-device-class) 命名 。

实体名称以大写字母开头,其余为小写,除非一个词是适当的名词或缩写,总是用首都书写.

不设置 `has_entity_name` 的集成使用遗留行为, 其中 `name` 拥有包括设备在内的全名 。 别用它做任何新的

## 翻译名称 {#translated-names}

别用英文名字硬化 设置一个 `translation_key` 代替, 并将此名称放在您的整合 `strings.json` 的 `entity` 区域 。 翻译名称只适用于设置 `has_entity_name` 到`True` 的实体 :

```json
{
  "entity": {
    "sensor": {
      "water_temperature": {
        "name": "Water temperature"
      }
    }
  }
}
```

`entity`下面的密钥是实体的域,下面的密钥是翻译密钥. 同一个翻译密钥用于翻译实体的状态和状态属性,其度量单位,并查看其[帖式图标](/core/entities/icons). 关于`strings.json`文件的全部图片,见[翻译](/core/integrations/translations).

```python
class ExampleSensor(SensorEntity):
    _attr_has_entity_name = True
    _attr_translation_key = "water_temperature"
```

只跳过每种语言中相同名称的翻译:适当的名词,模型名称,或来自设备或其库的名称. 在这种情况下,直接设置`name`。

> [!NOTE]
> 译名在实体初创建时用Home Assistant服务器的语言解决,而不是用用户界面的语言解决. 稍后更改服务器语言不会重命名现有的实体.的一个基本性

### 占位符 {#placeholders}

当名称中每个实体有不同部分时, 如频道编号, 在翻译中使用占位符并填充 `translation_placeholders` :

```json
{
  "entity": {
    "switch": {
      "outlet": {
        "name": "Outlet {number}"
      }
    }
  }
}
```

```python
class ExampleOutlet(SwitchEntity):
    _attr_has_entity_name = True
    _attr_translation_key = "outlet"

    def __init__(self, number: int) -> None:
        self._attr_translation_placeholders = {"number": str(number)}
```

如果占位符与名称不符,Home Assistant会在开发与β版本上引起错误,并在稳定释放上登录警告.

## 设备类的名称 {#names-from-the-device-class}

一些平台在不设置名称时会在其设备类之后命名一个实体:`binary_sensor`,`button`,`event`,`number`,`sensor`和`update`,以及`infrared`的发射和接收实体. 一个具有`temperature`设备类且无名称的传感器被称为"Temperature",被翻译为服务器语言. 在许多情况下,这是你所需要的。 与 `enum` 设备类的传感器是例外的:它们没有得到它的名称.

只有在名称完全没有设定时才会发生这种情况. `_attr_name = None`仍然表示"使用设备名称".

## 友好名称和实体ID {#friendly-name-and-entity-id}

从实体名称和设备名称, Home Assistant 构建 `friendly_name` 属性 :

| 情况 | 友好名称 |
| --- | --- |
| 实体没有设备 | 实体名称塞族人 |
| 实体有设备并对其名称 | 设备名称, 然后是实体名称 : “ 夜光电池 ” |
| 该实体有一个设备, 它的名字是 `None` | 设备名称:"夜光" |

当实体首次注册时,实体标识也从名称部分中构建。 默认这些是区域,母设备的名称(对于一个子设备),设备名称,以及实体名称,因此一个没有区域叫做"夜光"的设备的电池传感器变为`sensor.nightlight_battery`,它的光变为`light.nightlight`. 名称来源于英文译文,除非服务器语言是获得实体ID的本语言之一. 用户可以选择哪些部分Home Assistant用于新实体ID. 因此,在您的整合中永远不要依赖特定实体ID:在[非常大实体登记处](/core/entities/registry)中用它们独特的ID来查找实体.

当用户重命名一个实体或其设备时,Home Assistant使用新名称. 你的密码从不需要知道。
