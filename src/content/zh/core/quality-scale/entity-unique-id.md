---
title: 给实体一个独特的ID
description: 青铜规则实体-唯一-id:每个实体都有独特的ID,因此用户可以自定义.
sidebarLabel: 实体- 唯一
sidebarGroup: 青铜
order: 15
---

# 给实体一个独特的ID {#give-entities-a-unique-id}

此是铜法. 在`quality_scale.yaml`中,它被称为`entity-unique-id`.

整合的每个实体必须有一个[唯一标识](/glossary/unique-id). ID必须是稳定的:同一实体在重启,重新加载,或硬软件更新后获得相同的ID. 使用设备或服务提供的东西,如序列号或MAC地址,以及实体计量的密钥.

## 为什么这很重要 {#why-it-matters}

实体 [登记](/glossary/registry) 用其独特的 ID 来记住整个重新启动的实体 。 这就是允许用户重命名一个实体,更改其实体ID,区域,图标,或单位,并保留这些更改. 没有独有的ID,这些都不可能,实体也不过是一个屏幕上的值.

独特的ID只须每个集成和每个平台独有. 不要将集成领域或平台放入其中:登记处已经包括两者。

## 示例 {#example}

设定 `_attr_unique_id` 当创建实体时 :

```python
class MySensor(SensorEntity):
    """Temperature sensor of a device."""

    def __init__(self, device: MyDevice) -> None:
        """Initialize the sensor."""
        self._attr_unique_id = f"{device.serial_number}_temperature"
```

使用 [实体描述](/glossary/entity-description) , 通常的图案是设备的序号 `key` 描述 。

避免IP地址,主机名,用户可以更改的名称. 他们改变,一旦改变,用户就会失去他们的定制. 改变释放后如何构建独有的ID需要迁移,所以从一开始就立刻得到.

## 如何检查 {#how-it-is-checked}

- Pylint, 当规则是 `done` 时 : `home-assistant-missing-entity-unique-id` 当一个实体类并不总是设置一个唯一的ID时发出警告, `home-assistant-entity-unique-id-static` 当它是一个集成中的固定字符串, 允许一个以上的配置条目时发出警告 。
- Pylint, 对于每个集成: `home-assistant-entity-unique-id-redundant-domain`和`home-assistant-entity-unique-id-redundant-platform` 当唯一ID重复域或平台时警告.
- 身份是否稳定会被检查 。

## 例外 {#exceptions}

如果合并没有任何实体,则不适用这一规则。

## 相关规则 {#related-rules}

- [唯一配置输入](/core/quality-scale/unique-config-entry) : 防止重复配置条目 。
