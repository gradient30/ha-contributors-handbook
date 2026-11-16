---
title: 场景实体
description: 为生活在设备或枢机上的场景构建一个场景实体,这样人们就可以从Home Assistant激活它.
sidebarLabel: 场景
sidebarGroup: 输入与助手
---

# 场景实体 {#scene-entity}

一个 [场景](/glossary/scene) 实体为一组设备激活一组状态, 如在照明枢纽上的"电影之夜" 。 当场景在设备或服务上运行时, 您的集成执行一个场景实体, 而 Home Assistant 只需告诉它即可激活 。 从`Scene` 继承到`homeassistant.components.scene` 。

在场景编辑器或YAML中,人们自制的场景由Home Assistant自己处理. 你不需要一个场景实体

一个场景没有在州外。 如果有东西在关闭前一直打开,请使用 [切换](/core/entities/switch) 。

前端如何显示一个场景,请参见[显示更多信息视图](/design/more-info/scene).

## 的临时议程 {#properties}

一个场景没有平台特定属性. 每个实体的通用属性,如`name`,`available`和`unique_id`,都在[实体类别](/core/entities/entity-class)上. 一个场景不投票:`should_poll`默认是`False`.

## 支持的特性 {#supported-features}

该实体没有支持的特性。

## 方法 {#methods}

### 启动 {#activate}

当有人激活UI中的场景时调用,或者一个自动化或脚本调用`scene.turn_on`动作. 实施其中之一。

```python
class MyScene(Scene):
    

# Implement one of these methods. {#states}

    def activate(self, **kwargs: Any) -> None:
        """Activate the scene."""

    async def async_activate(self, **kwargs: Any) -> None:
        """Activate the scene."""
```

当动作有 `transition` 时, 您可以将其作为关键词参数: 设备达到新状态所需的秒数 。 如果设备支持它,就传下去.

## 状态 {#scenes-activated-outside-home-assistant}

场景状态是最后一次启用的时间戳,作为UTC的ISO 8601字符串. 这是`unknown`直到第一次激活。 基础课在它调用您的激活方法之前记录它,并在重启后恢复它. 你不能自己设定:`state`是最终的.

## 启动于 Home Assistant 外景 {#example}

一些设备也自行激活场景,如带物理场景按钮的枢机. 你怎么在 Home Assistant 中显示激活, 继承 `BaseScene` 而不是 `Scene` :

- 执行 `_async_activate(self, **kwargs)` 从 Home Assistant 激活该场景 。 注意主下划线 与 `Scene` 不同的是, `BaseScene` 没有为您记录激活 。
- 呼叫`self._async_record_activation()`,然后是`self.async_write_ha_state()` 当设备告诉你现场活动时,谁激活它。 从事件环外的线程,使用`self._record_activation()`而不是`_async_record_activation()`.

这样,时间戳就跟随设备,同样当来自Home Assistant的激活需要一点时间才能降落.

```python
from typing import Any

from homeassistant.components.scene import BaseScene

class ExampleHubScene(BaseScene):
    """A scene stored on the hub."""

    async def _async_activate(self, **kwargs: Any) -> None:
        """Ask the hub to activate the scene."""
        await self._hub.activate_scene(self._scene_id)

    def _handle_scene_activated(self) -> None:
        """Handle the hub reporting that the scene is active."""
        self._async_record_activation()
        self.async_write_ha_state()
```

## 示例 {#示例}

```python
from typing import Any

from homeassistant.components.scene import Scene

class ExampleScene(Scene):
    """A scene stored on the lighting hub."""

    _attr_has_entity_name = True

    def __init__(self, hub: ExampleHub, scene: HubScene) -> None:
        """Initialize the scene."""
        self._hub = hub
        self._scene_id = scene.id
        self._attr_name = scene.name
        self._attr_unique_id = f"{hub.serial}_scene_{scene.id}"

    async def async_activate(self, **kwargs: Any) -> None:
        """Activate the scene."""
        await self._hub.activate_scene(self._scene_id)
```

场景的名字来自中枢,所以这个例子使用它们作为它们而不是翻译密钥. 见[命名实体](/core/entities/naming).
