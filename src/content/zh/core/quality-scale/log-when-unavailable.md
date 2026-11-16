---
title: 不可用时记录一次, 返回一次
description: 'Silver 规则日志 - 当 - 不可用时: 集成日志一次丢失连接,一次返回时。'
sidebarLabel: 不可用时日志
sidebarGroup: 银
order: 7
---

# 不可用时记录一次, 返回一次 {#log-once-when-unavailable-and-once-when-back}

这是Silver的规则 在`quality_scale.yaml`中,它被称为`log-when-unavailable`.

当设备或服务无法到达时,集成日志会记录一次. 当它能够再次到达时,整合记录也一样。 没有在间隔期间的每次失败更新中 。 当您自己写这些信件时, 请在 `info` 级别上登录 。

## 为什么这很重要 {#why-it-matters}

当实体去[无](/glossary/unavailable)时,用户会在日志中查看以找出原因. 一个信息,当连接丢失, 一个当它回来,告诉他们发生了什么,什么时候。 每一个失败的民意调查都有一个信息,这些信息在噪音中,填充日志文件,并隐藏其他问题.

## 示例 {#example}

### 有协调员 {#with-a-coordinator}

协调员为你做这个。 当更新失败时加高 `UpdateFailedUnreachable` 。 协调员记录 `info` 级别的第一个失败, 在失败持续期间保持安静, 在获取数据时记录 `info` 级别 :

```python
async def _async_update_data(self) -> MyData:
    """Fetch the latest data."""
    try:
        return await self.client.get_data()
    except MyConnectionError as err:
        raise UpdateFailedUnreachable(
            translation_domain=DOMAIN,
            translation_key="update_unreachable",
        ) from err
```

### 使用同步( U) {#with-asyncupdate}

一个自我更新的实体会跟踪它是否已经登录 :

```python
class MySensor(SensorEntity):
    """A sensor that updates itself."""

    _unavailable_logged = False

    async def async_update(self) -> None:
        """Fetch the latest value."""
        try:
            data = await self.client.get_data()
        except MyConnectionError as err:
            self._attr_available = False
            if not self._unavailable_logged:
                _LOGGER.info("The device is unavailable: %s", err)
                self._unavailable_logged = True
            return

        self._attr_available = True
        self._attr_native_value = data.temperature
        if self._unavailable_logged:
            _LOGGER.info("The device is available again")
            self._unavailable_logged = False
```

## 如何检查 {#how-it-is-checked}

- 当一个错误在警告级别或更高时, Pylint 警告它, 就像在上升 `UpdateFailed` (`home-assistant-log-and-raise` 之前的日志) 。 Home Assistant已经报告了这些例外。
- 其余的经过审查。

## 例外 {#exceptions}

如果合并没有实体,则不适用这一规则。

## 相关规则 {#related-rules}

- [无法获取的实体的人数](/core/quality-scale/entity-unavailable): 酌情标记不可用的实体。
