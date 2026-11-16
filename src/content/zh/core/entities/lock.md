---
title: 锁定实体
description: 为锁,解锁的智能锁建立锁实体,并可选择打开一个门.
sidebarLabel: 锁定
sidebarGroup: 开合与安防
---

# 锁定实体 {#lock-entity}

一个锁实体控制一个锁:它会锁,解锁,在一些锁上,通过拉回锁来打开门. 它可以要求一个代码。 从`LockEntity` 继承到`homeassistant.components.lock` 。

前端显示锁的方式,请参见[锁定更多信息视图](/design/more-info/lock).

从 Home Assistant 演示中嵌入的仪表板卡的现场演示。 锁 嗯 锁上 锁上 锁上 锁上 锁上 卡片为直播:解锁,或开门.

```html
<ha-embed-provider
  style="
    display: grid;
    grid-template-columns: repeat(12, minmax(0, 1fr));
    gap: 8px;
    align-items: start;
    max-width: 500px;
  "
>
  <script type="application/json">
    [
      {
        "entity_id": "lock.front_door",
        "state": "locked",
        "attributes": {
          "friendly_name": "Front door",
          "supported_features": 1
        }
      }
    ]
  </script>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "tile",
        "entity": "lock.front_door",
        "features": [
          {
            "type": "lock-commands"
          },
          {
            "type": "lock-open-door"
          }
        ]
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

## 的临时议程 {#properties}

锁定实体在 [一般实体属性](/core/entities/entity-class) 上方有这些属性 。 每个属性都可以以其`_attr_`属性设定,如`_attr_is_locked`.

| 名称 | 类型 | 默认 | 说明 |
| ---- | ---- | ------- | ----------- |
| `is_locked` | `bool \| None` | `None` | 锁定是否锁定 。 |
| `is_locking` | `bool \| None` | `None` | 锁定是否在被锁定的过程中 。 |
| `is_unlocking` | `bool \| None` | `None` | 锁是否在解锁过程中 。 |
| `is_open` | `bool \| None` | `None` | 锁是否解锁并释放了锁链 。 |
| `is_opening` | `bool \| None` | `None` | 锁是否正在解锁过程中 。 |
| `is_jammed` | `bool \| None` | `None` | 无论是锁试图移动,还是锁定,解锁,还是打开,但在完成前被卡住了. |
| `code_format` | `str \| None` | `None` | 代码必须匹配的正则表达式, 如 `^\d{4}$` 。 `None`表示锁不需要代码. |
| `changed_by` | `str \| None` | `None` | 到底是谁或是什么把锁最后换了,比如用户名或键盘. |

## 代码 {#codes}

当 `code_format` 被设定时, Home Assistant 在它调用您的方法之前, 在锁定、 解锁或打开对它的行动时检查代码, 当它不匹配时, 并产生验证错误 。 此检查也会运行一个没有代码的动作: 一个空代码也必须匹配 `code_format`, 所以像 `^\d{4}$` 这样的模式会让每个动作都需要一个代码 。 您的方法在 `kwargs` 中以 `ATTR_CODE` 得到代码, 并且只有在有代码时, 所以在可选时用 `kwargs.get(ATTR_CODE)` 读它 。

用户可以在实体设置中存储默认代码. 当一个动作没有代码时, Home Assistant 使用默认代码 。 不匹配 `code_format` 的默认代码被忽略 。 您不必为此做任何事情: 它从 [实体登记选项](/core/entities/registry) 读取设置, 并为您添加代码 。

## 支持的特性 {#supported-features}

将 `LockEntityFeature` 旗帜设置为 `supported_features`。 见 [支持的特性](/glossary/supported-features) 。

| 数值 | 说明 |
| ----- | ----------- |
| `OPEN` | 锁可以打开门锁 执行`open`。 |

## 方法 {#methods}

执行岔或每种方法的同步变体,而不是两者。

| 就在那时 | Async 变体 | 说明 |
| ------ | ------------- | ----------- |
| `lock(**kwargs: Any)` | `async_lock` | 锁上锁 |
| `unlock(**kwargs: Any)` | `async_unlock` | 解锁. |
| `open(**kwargs: Any)` | `async_open` | 打开门锁 需要 `OPEN` 。 |

## 状态 {#states}

州为`LockState`,取自首个属性为`True`,按此顺序:

| 数值 | 从 | 说明 |
| ----- | ---- | ----------- |
| `LockState.JAMMED` | `is_jammed` | 锁试图移动,但在完成前卡住了. |
| `LockState.OPENING` | `is_opening` | 锁打开锁 |
| `LockState.LOCKING` | `is_locking` | 锁被锁了 |
| `LockState.OPEN` | `is_open` | 锁没有被锁住,并释放了锁。 |
| `LockState.UNLOCKING` | `is_unlocking` | 锁被解锁了 |
| `LockState.LOCKED` | `is_locked` is `True` | 锁锁了 |
| `LockState.UNLOCKED` | `is_locked` is `False` | 锁没锁 |

实例没有应用,且`is_locked`为`None`时,状态为`unknown`.

`OPEN` 既需要:锁没有安全, * 也释放了它的锁。 锁仍安全时放出的锁不是打开状态.

## 示例 {#example}

```python
from typing import Any

from homeassistant.components.lock import LockEntity

class MyLock(LockEntity):
    """A smart lock with a four digit code."""

    _attr_has_entity_name = True
    _attr_name = None
    _attr_code_format = r"^\d{4}$"

    def __init__(self, device: MyDevice) -> None:
        """Set up the lock."""
        self._device = device
        self._attr_unique_id = device.serial

    @property
    def is_locked(self) -> bool:
        """Return if the lock is locked."""
        return self._device.locked

    @property
    def is_jammed(self) -> bool:
        """Return if the lock is jammed."""
        return self._device.jammed

    async def async_lock(self, **kwargs: Any) -> None:
        """Lock the lock."""
        await self._device.lock()

    async def async_unlock(self, **kwargs: Any) -> None:
        """Unlock the lock."""
        await self._device.unlock(kwargs["code"])
```
