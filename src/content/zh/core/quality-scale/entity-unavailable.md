---
title: 酌情标出不可用的实体
description: 无法获取银元规则实体:当设备或服务无法到达时, 实体无法获取 。
sidebarLabel: 无法获取的实体的人数
sidebarGroup: 银
order: 5
---

# 酌情标出不可用的实体 {#mark-entities-unavailable-when-appropriate}

这是Silver的规则 在`quality_scale.yaml`中,它被称为`entity-unavailable`.

当集成无法从设备或服务获得数据时,其实体必须成为[无](/glossary/unavailable). 当连接工作但单个值暂时缺失时,该实体会报告一个未知状态(`None`),并保持可用.

## 为什么这很重要 {#why-it-matters}

一个持续显示设备下线后最后值的实体在说谎. 客厅在传感器3小时无法到达时已经不是21°C. 不可用告诉用户,以及他们的自动化,这个值现在不能被信任.

## 示例 {#example}

### 有协调员 {#with-a-coordinator}

A `CoordinatorEntity` 为你处理这个 。 当[协调员](/glossary/coordinator) 的更新生成`UpdateFailed`,`last_update_success` 转`False` 时, 协调员的每个实体都变得不可用 :

```python
class MyCoordinator(DataUpdateCoordinator[dict[str, MyDevice]]):
    """Fetch data for all devices."""

    async def _async_update_data(self) -> dict[str, MyDevice]:
        try:
            return await self.client.get_devices()
        except MyConnectionError as err:
            raise UpdateFailed(
                translation_domain=DOMAIN,
                translation_key="update_failed",
            ) from err
```

如果一个实体需要的更多, 就像它的设备从数据中丢失时无法使用一样, 请将您的支票和 `super().available` 合并 :

```python
class MySensor(MyEntity, SensorEntity):
    """A sensor of a device."""

    @property
    def available(self) -> bool:
        """Return if the entity is available."""
        return super().available and self.device_id in self.coordinator.data
```

不要离开 `super().available` 。 当更新失败时, 协调员会保存上次成功更新的数据, 因此仅检查 `coordinator.data` 就可以让实体使用旧数据 。

### 使用同步( U) {#with-asyncupdate}

更新自身设置 `_attr_available` 的实体 :

```python
async def async_update(self) -> None:
    """Fetch the latest value."""
    try:
        data = await self.client.get_data()
    except MyConnectionError:
        self._attr_available = False
        return

    self._attr_available = True
    self._attr_native_value = data.temperature
```

## 如何检查 {#how-it-is-checked}

- Pylint 警告,当 `available` 覆盖一个协调器实体只查看 `coordinator.data` 时, 并忽略上次更新是否成功 (`home-assistant-coordinator-entity-available`) 。
- 其余的经过审查。

## 例外 {#exceptions}

如果合并没有实体,则不适用这一规则。

进入备用状态的装置是特例. 如果集成在备用状态时有办法打开设备,通过用户定义的自动化或Wake-on-LAN或红外爆破器等第二个通道,则该设备报告为`off` 当它处于待命状态时, 而不是因为无法进入。 如果没有这种方法,且设备无法按其当前状态控制,则报告为无法使用.

例如,只能用红外爆破器打开的媒体播放器:

- 首次添加时, 没有连接, 无法使用 。
- 一旦用户设置一个自动化打开它,它在待命状态时是`off`.
- 一旦打开,连接又恢复了 `on`。

当您报告某个设备处于待命状态时, 当向一个协调员报告无法使用时, 请启动 `UpdateFailedUnreachable`, 就像任何无法到达的设备一样 。 它是`UpdateFailed` 的子类, 因此实体变得无法使用, 协调员按照 [不可用时日志](/core/quality-scale/log-when-unavailable) 的要求将其记录在 `info` 级别 。

## 相关规则 {#related-rules}

- [不可用时日志](/core/quality-scale/log-when-unavailable) : 无法记录时日志一次, 返回时日志一次 。
