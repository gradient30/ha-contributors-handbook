---
title: 在通用模块中设置常见模式
description: 青铜规则通用模块:协调员生活在coord.py中,基实体位于实体.py中.
sidebarLabel: 常用模块
sidebarGroup: 铜
order: 4
---

# 在通用模块中设置常见模式 {#put-common-patterns-in-common-modules}

此是铜法. 在`quality_scale.yaml`中,它被称为`common-modules`.

许多整合共享的模式存在于每一个整合中的同一个模块中. [协调员](/glossary/coordinator)进入`coordinator.py`。 一个基础实体类,由所有平台的实体共享,在`entity.py`中进行.

## 为什么这很重要 {#why-it-matters}

一致性使核心工作更容易进行。 当每一个集成都保持它的协调员在 `coordinator.py` 时,你知道在哪里查看一个集成,你从来没有见过。 这帮助审查者,帮助下一个贡献者, 当你一年后回到自己的代码时,帮助你.

一个碱性实体也删除了重复的代码:设备信息,命名,以及协调器链接被写入一次,而不是每个平台一次.

## 示例 {#example}

`coordinator.py`担任协调员:

```python
class MyCoordinator(DataUpdateCoordinator[MyData]):
    """Fetch data for My integration."""

    config_entry: MyConfigEntry

    def __init__(
        self, hass: HomeAssistant, entry: MyConfigEntry, client: MyClient
    ) -> None:
        """Initialize the coordinator."""
        super().__init__(
            hass,
            LOGGER,
            config_entry=entry,
            name=DOMAIN,
            update_interval=timedelta(minutes=1),
        )
        self.client = client

    async def _async_update_data(self) -> MyData:
        """Fetch the latest data."""
        return await self.client.get_data()
```

`entity.py`拥有每个平台所基于的基础实体:

```python
class MyEntity(CoordinatorEntity[MyCoordinator]):
    """Base entity for My integration."""

    _attr_has_entity_name = True

    def __init__(self, coordinator: MyCoordinator) -> None:
        """Initialize the entity."""
        super().__init__(coordinator)
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, coordinator.data.serial)},
            name=coordinator.data.name,
        )
```

## 如何检查 {#how-it-is-checked}

- Pylint建议将一个类移动到它所属的模块(`home-assistant-enforce-class-module`). 它在`coordinator.py`以外的一个子类上标注了`DataUpdateCoordinator`,在`entity.py`以外一个类似`Entity`或`CoordinatorEntity`的类上直接产生的基础实体. 第二次检查跳过定义实体平台的集成, 如 `light` 。
- 其余的经过审查。

## 例外 {#exceptions}

这一规则没有只是为了例外。 没有协调员或领先实体的一体化完全没有动静。
