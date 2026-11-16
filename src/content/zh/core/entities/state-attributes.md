---
title: 状态和属性
description: 最终在您实体的状态对象, 何时添加额外的属性, 以及如何将属性排除在历史之外 。
sidebarLabel: 状态和属性
sidebarGroup: 基础
order: 5
---

# 状态和属性 {#state-and-attributes}

每次实体写入状态时,Home Assistant在[状态机器](/glossary/state-machine)中将其变为状态对象. 这个物体就是自动化,前端和历史所看到的. 它有两个部分: [状态](/glossary/state)本身, 和一组 [属性](/glossary/attribute).

## 国家 {#the-state}

状态是一个短字符串,如`on`,`21.5`,或`cleaning`. 您自己不构建它:您平台的基类从自己的属性中计算出来,比如 `is_on` 用于切换或 `native_value` 用于传感器 。 平台页面列出每个域的可能状态.

有几个规则适用于每个实体:

- 当`available`是`False`时,状态是`unavailable`.
- 当状态是`None`时,它就变成了`unknown`.
- 数字转换为字符串。 浮点是四舍五入到可读精度.
- 一个状态最多可以达到255个字符. 更长的状态会被作为错误 65. 被 `unknown` 替换 。 长文本属于属性,或者属于不同种类的实体.

使用您的平台定义的状态 。 如果一个域使用`on`和`off`,不要发明`running`. 如果您需要域没有的词, 请 长官检查另一个平台是否更合适, 如 enum [传感器](/core/entities/sensor) 或 [选择](/core/entities/select) 。

## 属性 {#attributes}

Home Assistant 填充来自多个来源的属性, 按此顺序 :

1. 域的能力属性,如光线支持的颜色模式列表. 它们描述了该实体能够做什么,并储存在实体登记处。
2. 域的状态属性, 9. 如光的当前亮度 。 当实体不存在时,  9.
3. 你的`extra_state_attributes`。 在实体不可用时,也被排除在外。
4. 通用属性: `unit_of_measurement`,`assumed_state`,`attribution`,`device_class`,`entity_picture`,`icon`,`friendly_name`,和`supported_features`,当它们被设定时.

前两个来自平台基础课. 在整合中不要覆盖 `state_attributes` 或 `capability_attributes` 。

### 额外的状态属性 {#extra-state-attributes}

`extra_state_attributes`是用来解释状态的整合特定信息。 一个好的属性可以帮助某人理解或使用当前状态,比如读取的来源或下一次预定运行.

```python
class ExampleSensor(SensorEntity):
    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return the station that measured the value."""
        return {"station": self._station.name}
```

或者uangn `_attr_extra_state_attributes` 当你准备好值时。

在添加属性之前,询问它是否应该是一个自己的实体. 属性举例说明不能用于能量仪表板,没有长期统计,翻译也不容易. 自动变化的值,如电池电位或信号强度,几乎总是作为自己的传感器效果更好. 关于该设备的静态信息,如同它的固件版本或序列号一样,属于[设备信息](/core/entities/registry#linking-to-a-device),而不是属性.

属性名称为小写 `snake_case` 。 价值必须是JSON可序列的。

### 属性不来不走 {#attributes-dont-come-and-go}

在自动化或模板中使用属性的人需要告诉"这个实体没有它",除了"它现在没有价值". 这些规则适用于每一个状态属性,而不仅仅是额外的属性:

- 预期的属性总是在词典中.本国境内没有值时,其值为`None`.
- 词典中根本不包含一个无法预期的属性 。

不可用的实体是例外:如上所述,它不包含其域的状态属性及其额外的状态属性.

当实体支持它时,例如当它属于该实体支持的`supported_features`中的特性时,一个属性是预期的. 该设备现在是否有值并不重要:这就是`None`的用途. 轻基级以这种方式工作. 支持效果的光总是有`effect`属性,在光线关闭时它是`None`. 无效果的光支持没有`effect`属性.

这是在[关于实体属性的架构讨论](https://github.com/home-assistant/architecture/discussions/680)中决定的。

## 将属性向秘书处提交历史 {#keep-attributes-out-of-the-history}

记录器存储每个状态变化,包括其属性. 它只留下了几个, 永远不变的属性,或以后不再有用的属性,只填充数据库。 以类属性排除它们:

```python
from homeassistant.const import MATCH_ALL

class ExampleCamera(Camera):
    _unrecorded_attributes = frozenset({"access_token", "snapshot_url"})
```

- `_unrecorded_attributes` 是为您整合的实体类。
- `_entity_component_unrecorded_attributes`是用于域的基类,如扇子的`preset_modes`.

两者必须是阶级属性. 把它们放在一个实例上是没用的。 使用 `MATCH_ALL` 一次排除一切 。 即便如此,Home Assistant继续录制`device_class`,`unit_of_measurement`,`friendly_name`和`state_class`,因为其他特性都取决于它们.

## 要避免的事情 {#things-to-avoid}

- 每次更新时不要更改属性, 如“ 上次检查的” 时间戳 。 每一次更改都是数据库中的新一行和自动化看到的状态更改事件.
- 不要在属性和状态中把相同值放在一起.
- 不要使用属性围绕一个域中缺失的特征工作. 取而代之的就是这个
