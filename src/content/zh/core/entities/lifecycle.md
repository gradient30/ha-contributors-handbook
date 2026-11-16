---
title: 实体生命周期
description: 当 Home Assistant 添加并删除一个实体, 以及您用来订阅、 清理和对注册更改作出反应的钩子时会发生什么 。
sidebarLabel: 生命周期
sidebarGroup: 基础
order: 4
source: https://github.com/home-assistant/core/blob/dev/homeassistant/helpers/entity.py
lastVerified: 2026-10-21
---

# 实体生命周期 {#entity-lifecycle}

2026-10-21日最后一次核实,对https://github.com/home-assistant/core/blob/dev/homeassistant/helpers/entity.py.

您在整合的平台设置中创建实体对象, 并将其交给 Home Assistant 和 `async_add_entities` 。 从此,Home Assistant决定实体何时被添加,更新,删除. 生命周期钩子让你运行代码 在每一个时刻。 皆是可选.

## 添加一个实体 {#adding-an-entity}

当你通过一个实体到`async_add_entities`,Home Assistant会经过这些步骤:

1. 它赋予实体`hass`和`platform`属性.
2. 它呼叫`async_prepare_to_add_to_hass()`。
3. 如果您通过了`update_before_add=True`,它就叫更新方法. 如果更新提升, 在此添加停止 。
4. 如果实体有独有的ID,它会在[登记册](/core/entities/registry)中注册设备与实体,并选择实体ID. 如果该实体已禁用, 或者其唯一的ID或实体ID已经使用, 在此添加停止 。
5. 它呼叫`async_added_to_hass()`。
6. It(一作 writes).

您的 至少 {H0将有助于运行 `self.hass` 和 `self.entity_id` 尚未设置 。 保留 `__init__` 关于存储实体需要的东西, 并做剩下的在钩。

### `async_added_to_hass()` {#asyncaddedtohass}

主钩子. 它作为最后的添加步骤运行,就在第一个状态写成之前. 该实体届时有其实体识别和登记条目。 使用它来订阅更新,注册听众,或者恢复先前的状态.

在更早的一步加点时,钩子不会运行. 但加法在钩子开始后仍然可以失败:当钩子加法,当加法被取消,或者在写入第一个状态加法时. `async_will_remove_from_hass`在那样的情况下不会运行,所以登记您在这里设置的 `async_on_remove` 的清理,就像下面的例子一样.

```python
async def async_added_to_hass(self) -> None:
    """Subscribe to the device once the entity is added."""
    await super().async_added_to_hass()
    self.async_on_remove(
        self._device.subscribe(self._handle_update)
    )
```

当您继承了同样可能执行钩子的类时, 如 `CoordinatorEntity` 或 `RestoreEntity` 拨打 `super()` 。

因为残疾实体从未被添加过,所以如果您的整合需要,这个钩子也是保留一个实体的引用的正确地点. 您在此注册的任何东西只登记在实际运行的实体 。

当用户更改实体ID时,钩子不会再次运行,除了一些自定义集成的实体. 见[`async_entity_id_changed`](/core/entities/lifecycle#async_entity_id_changedold_entity_id).

### `async_prepare_to_add_to_hass()` {#asyncpreparetoaddtohass}

在 Home Assistant 查看登记册之前, 每次尝试添加实体都会运行 。 它也运行在最终不会被添加的实体上,例如因为它们被禁用. 用于在 Home Assistant 处理注册项之前必须进行的工作, 甚至当实体被禁用时 。 例如,在创建或浏览注册条目时读取的种子实体注册选项,或用您的整合帮助者注册该实体,所以一个被创建的已禁用的实体可以稍后启用.

你很少需要它。 铭记:

- 不要依赖 `entity_id` 或 `registry_entry` 。 视实体的添加方式而定,它们可能是未设置的,由您的整合设置的,也可能是先前尝试留下的.
- 提出例外中止 。
- `async_added_to_hass` 可能永远不会运行, 而`async_will_remove_from_hass` 当添加中止时不会运行 。 `async_on_remove` 调用已运行, 取消添加时正确, 也禁用实体时正确 。 使用 `async_on_remove` 来清理此添加实体的尝试中唯一要紧的事项 。 不要用它来做一个必须从一个残疾实体中生存下来的注册, 比如下面的例子: 这个注册属于你的整合, 所以把它保存在那里, 在像独一无二的ID一样的稳定的东西上。
- 不要写国家, 不要订阅更新 写它。 该实体可能还没有实体ID,所以写入状态失败 。 改用 `async_added_to_hass` 订阅 。

```python
async def async_prepare_to_add_to_hass(self) -> None:
    """Run before the entity is added."""
    await super().async_prepare_to_add_to_hass()
    

# Let the hub know about the entity, even when it turns out to be {#removing-an-entity}
    

# disabled, so it can be enabled later. Not undone when adding is aborted. {#asynconremovefunc}
    self._hub.register_known_entity(self.unique_id, self._channel)
```

> [!WARNING]
> `add_to_platform_start()`,`add_to_platform_finish()`,和`add_to_platform_abort()`的`Entity`是实体平台的执行细节. 在你的整合中不要压倒他们。 用本页的钩子代替 。

## 删除一个实体 {#asyncwillremovefromhass}

当一个实体的配置条目卸载、用户禁用或从实体登记册中删除时,该实体将被删除。 停止 Home Assistant 不删除实体, 因此这些钩子不会在关闭时运行 。 如果关闭时一定出事, 请听 `EVENT_HOMEASSISTANT_STOP` 。 当一个实体被移除时, Home Assistant :

1. 用 `async_on_remove` 调用每个已注册的回调 。
2. 拨打`async_will_remove_from_hass()`。
3. 撤销 the州. 或者,当实体仍在注册并启用时,比如当配置项刚刚卸下时,它会设置状态为`unavailable`,带有`restored`属性.

### `async_on_remove(func)` {#asyncremovedfromregistry}

注册一个函数,以便在实体被移除时调用,或者在添加时中止。 大多数订阅帮助者返回一个未订阅的函数,这样您就可以直接通过这个功能. 这是最干净的方法 确保你不会泄露一个听众。 一个例外是您稍后替换的订阅, 例如当实体 ID 更改时 。 见[`async_entity_id_changed`](/core/entities/lifecycle#async_entity_id_changedold_entity_id).

### `async_will_remove_from_hass()` {#registry-changes}

`async_added_to_hass`的对应方. 用它来撤销`async_on_remove`不能完成的工作,比如关闭只属于这个实体的连接.

它只运行一个被添加的实体. 当添加被中止或失败时, 即使在 `async_added_to_hass` 已经运行后, 只有 `async_on_remove` 调用运行 。 单单人和单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人和单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人,单人 见[`async_entity_id_changed`](/core/entities/lifecycle#async_entity_id_changedold_entity_id).

### `async_removed_from_registry()` {#asyncregistryentryupdated}

当实体从实体注册处删除时运行, 而非仅仅删除到现在 。 使用它来清理存储在实体外的数据,比如只对该实体有意义的设备上的文件或设置.

## 书记官处变动 {#asyncentityidchangedoldentityid}

用户可以在运行时更改注册中的一个实体:重命名,给它另一个实体ID,更改其选项.

### `async_registry_entry_updated()` {#restoring-state}

实体登记条目变更后运行。 `self.registry_entry`持有新条目。 当您的实体依赖注册选项时使用它, 就像一个单位或用户所选择的精度。

### `async_entity_id_changed(old_entity_id)` {#async_entity_id_changedold_entity_id}

当用户更改实体ID时运行 。 该实体在原位被更改:它没有被移除并再次添加,因此`async_will_remove_from_hass`和`async_added_to_hass`不要运行. 和那些钩子不同,这个是 `@callback` 在事件循环中运行,所以它不能等待。

> [!IMPORTANT]
> 直到Home Assistant2027.11,自定义集成必须选择在位更改. 如果一个自定义集成的类执行`async_prepare_to_add_to_hass`,`async_added_to_hass`,或`async_will_remove_from_hass`,但该类或它的子类都没有执行`async_entity_id_changed`,则其实体仍然被删除,并在实体ID更改时再次添加. 然后添加和移除的钩子再次运行,这个钩子不会运行. 见[关于新生命周期钩子的博客文章](https://contributors.home-assistant.io/blog/2026/10/12/new-entity-lifecycle-hooks/).

到那时,`self.entity_id`就是新的ID,旧的ID作为`old_entity_id`通过. 旧ID下的状态已经删除, `async_registry_entry_updated` 已经运行, Home Assistant 已经将自己的簿记器移动到新的ID上, 就像注册跟踪和恢复状态 。 新身份证下的州还没有写出来

如果您通过自己的实体ID追踪到某样东西,比如在`self.entity_id`上键入的状态更改收听器或调度器信号,或者从实体ID到实体的查询表,请将其移动到这里的新ID. 总是调用`super()`,所以基班也可以同样调用. 如果你的单位没有在自己的实体ID上设置任何密钥,你不需要这个钩子. 一个执行添加或移除钩子的自定义集成仍然需要它选择在位更改,然后一个只调用`super()`的钩子就足够了.

Home Assistant 钩子返回时在新ID下写状态, 除非你已经这样做了 。 如果您需要自己在新ID下的状态,例如要制作一个引用 `this` 的模板, 请用 `self.async_write_ha_state()` 自己写, 但只能在拨打 `super()` 之后, 所以基础类已经更新了状态所依赖的 。

需要等待的工作可以在一项任务中进行。 注册更新不会等待这个任务,因此在每个 `await` 之后,检查实体是否仍然被添加, `self.entity_id` 没有再次更改 。

如果钩灼升起, Home Assistant 记录例外, 更改无论如何会完成: 状态在新ID下写 。

注意,任何你再次订阅的东西 仍然被清理 当实体被移除。 `self.async_on_remove(self._unsub_signal)` 登记 * first * 订阅的未订阅功能 。 在实体ID更改后,移除实体再次调用 stale 函数,新订阅漏洞. 相反, 在调用当前未订阅函数时, 注册回调 :

```python
async def async_added_to_hass(self) -> None:
    """Subscribe once the entity is added."""
    await super().async_added_to_hass()
    self._subscribe_signal()
    self.async_on_remove(lambda: self._unsub_signal())

@callback
def _subscribe_signal(self) -> None:
    """Subscribe to the signal for the current entity ID."""
    self._unsub_signal = async_dispatcher_connect(
        self.hass, f"{DOMAIN}_{self.entity_id}", self._handle_signal
    )

@callback
def async_entity_id_changed(self, old_entity_id: str) -> None:
    """Move the subscription to the new entity ID."""
    super().async_entity_id_changed(old_entity_id)
    self._unsub_signal()
    self._subscribe_signal()
```

在 `async_will_remove_from_hass` 中不订阅也避免了 stale 函数, 但是在 `async_added_to_hass` 运行后添加失败时, 钩子不会运行 。

## 恢复状态 {#恢复状态}

一些实体必须记住它们在整个重启时的状态,因为设备不能告诉他们. 在 `homeassistant.helpers.restore_state` 中继承 `RestoreEntity` , 并在 `async_added_to_hass` 中读取最后一个状态 :

```python
from homeassistant.helpers.restore_state import RestoreEntity

class ExampleSwitch(SwitchEntity, RestoreEntity):
    async def async_added_to_hass(self) -> None:
        await super().async_added_to_hass()
        if (last_state := await self.async_get_last_state()) is not None:
            self._attr_is_on = last_state.state == "on"
```

sensors 使用 `RestoreSensor` 代替 `RestoreSensor` , 并用 `RestoreSensor.async_get_last_sensor_data()` 读取最后的状态 。 见[传感器实体](/core/entities/sensor).
