---
title: 在适当的间隔内投票
description: 青铜规则 适当计票:投票一体化使用与其数据相符的间隔.
sidebarLabel: 适当定价
sidebarGroup: 青铜
order: 2
---

# 在适当的间隔内投票 {#poll-at-an-appropriate-interval}

此是铜法. 在`quality_scale.yaml`中,它被称为`appropriate-polling`.

如果集成 [民意调查](/glossary/polling) 一个设备或服务, 它设置一个适合数据的投票间隔 。 间隔是您作为开发者对大多数用户的选择. 这不是一个字段 在配置流。

## 为什么这很重要 {#why-it-matters}

在理想的世界中,每个设备都会推动其更新. 许多设备和服务不能,所以Home Assistant必须问. 绞尽脑尽头地要求浪费资源,可能会得到云服务限制的用户费率。

适当的措施取决于数据。 空气质量感应器不会每5秒改变一次:每分钟投票一次对几乎每个人都是罚款的. 一旦每小时一次更新太阳能生产,

真正需要不同间隔的用户可以使用自动化程序 [定义自己的投票间隔](https://www.home-assistant.io/common-tasks/general/#defining-a-custom-polling-interval).

## 示例 {#example}

使用 [协调员](/glossary/coordinator),在创建时通过 `update_interval` :

```python
class MyCoordinator(DataUpdateCoordinator[MyData]):
    """Fetch data for My integration."""

    config_entry: MyConfigEntry

    def __init__(self, hass: HomeAssistant, entry: MyConfigEntry) -> None:
        """Initialize the coordinator."""
        super().__init__(
            hass,
            LOGGER,
            config_entry=entry,
            name=DOMAIN,
            update_interval=timedelta(minutes=1),
        )
```

自行投票的实体,使用 `should_poll` 设定为 `True`,使用 `SCAN_INTERVAL` 平台模块的常数 :

```python
SCAN_INTERVAL = timedelta(minutes=1)

class MySensor(SensorEntity):
    """A sensor that polls by itself."""

    _attr_should_poll = True
```

## 如何检查 {#how-it-is-checked}

- Pylint警告当一个配置流要求一个投票间隔时,比如`CONF_SCAN_INTERVAL`或`update_interval`(`home-assistant-config-flow-polling-field`).
- 检查间隔秃牙是否合适。 准备好解释秃头的选择

## 例外 {#exceptions}

如果集成不萃民弄清,例如因为设备推动其更新,则此规则不适用.

## 相关规则 {#related-rules}

- [并行更新](/core/quality-scale/parallel-updates) : 设置并行更新的数目 。
