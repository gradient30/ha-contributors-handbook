---
title: 指定实体类别
description: 黄金规则实体类:配置和诊断实体有一个实体类.
sidebarLabel: 实体类别
sidebarGroup: 金
order: 13
---

# 指定实体类别 {#assign-entity-categories}

这是黄金规则 在`quality_scale.yaml`中,它被称为`entity-category`.

非设备主要目的的实体获得 [实体类别](/glossary/entity-category) 。 有两个:

- `EntityCategory.CONFIG`:一个改变设备配置的实体,如关闭状态LED的开关.
- `EntityCategory.DIAGNOSTIC`:显示设备本身信息的实体,比如它的信号强度,上升时间,或固件版本.

实体是某人拥有设备的原因,比如恒温器的温度,保留默认:没有分类.

## 为什么这很重要 {#why-it-matters}

Home Assistant 使用分类来决定一个实体的出现地点 。 自动生成的仪表板离开配置和诊断实体,设备页面在自己的章节中显示它们. 没有分类,一个传感器的信号强度就到每个用户仪表板上的温度旁边.

## 示例 {#example}

```python
class MySignalStrengthSensor(SensorEntity):
    """The signal strength of My device."""

    _attr_entity_category = EntityCategory.DIAGNOSTIC
    _attr_device_class = SensorDeviceClass.SIGNAL_STRENGTH
```

带有实体描述, 在描述上设置 `entity_category` 。

## 如何检查 {#how-it-is-checked}

已检阅.

## 例外 {#exceptions}

如果合并没有实体,或其所有实体都是没有适当类别的主要实体,则不适用这一规则。
