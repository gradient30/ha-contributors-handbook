---
title: 按键实体
description: 构建按钮实体,在设备或服务上触发单个动作,如重启.
sidebarLabel: 按钮
sidebarGroup: 输入与助手
---

# 按键实体 {#button-entity}

按钮实体在一个设备或服务上触发一个动作:重启一个设备,通过闪烁灯光来识别它,重设过滤器计数器,或者酿造一杯咖啡. 它没有自己的状态。 从`ButtonEntity` 继承到`homeassistant.components.button` 。

按钮是 Home Assistant 内部的虚拟按钮 。 它不适合所有看起来像按钮的东西:

- 在你按住之后, 保持不動的
- gainsit of [事件](/core/entities/event) 是一个实体 。 按钮实体无法报告在 Home Assistant 之外发生的按键 。
- 安装固件属于 [更新](/core/entities/update) 实体 。

## 的临时议程 {#properties}

| 名称 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- |
| `device_class` | `ButtonDeviceClass \| None` | `None` | 按钮做什么? 见[设备类](/core/entities/button#device-classes). |

按钮没有特定平台的状态属性 。 每个实体的通用属性,如`name`,`available`和`unique_id`,都在[实体类别](/core/entities/entity-class)上. 按钮不投票 : `should_poll` 默认为 `False` 。

## 支持的特性 {#supported-features}

该实体没有支持的特性。

## 设备类 {#device-classes}

| 常数 | 说明 |
| --- | --- |
| `ButtonDeviceClass.IDENTIFY` | 识别设备,例如通过闪烁灯光或发出声音. |
| `ButtonDeviceClass.RESTART` | 恢复设备。 |
| `ButtonDeviceClass.UPDATE` | 更新设备的软件。 避免它: 使用 [更新](/core/entities/update) 实体代替 。 |

带有设备类且没有自己名称的按钮会获得其设备类的翻译名称,如"重新启动". 见[命名实体](/core/entities/naming).

识别按钮通常不是设备的主要特征. 给它`EntityCategory.DIAGNOSTIC`[实体类别](/glossary/entity-category)。

## 方法 {#methods}

### 新闻 {#press}

当有人在UI中按下按钮,或者一个自动化或脚本调用`button.press`动作时调用. 实施其中之一。

```python
class MyButton(ButtonEntity):
    

# Implement one of these methods. {#states}

    def press(self) -> None:
        """Handle the button press."""

    async def async_press(self) -> None:
        """Handle the button press."""
```

## 状态 {#example}

按钮的状态是上次从Home Assistant按下的时间戳,作为协调世界时的ISO 8601字符串. 这是`unknown`直到第一次发布。 基础课将它设置在它调用您的按压方法之前, 并在重启后恢复它 。 你不能自己设定:`state`是最终的.

## 示例 {#示例}

```python
from homeassistant.components.button import (
    ButtonDeviceClass,
    ButtonEntity,
)
from homeassistant.const import EntityCategory

class ExampleRestartButton(ButtonEntity):
    """Restart the device."""

    _attr_has_entity_name = True
    _attr_device_class = ButtonDeviceClass.RESTART
    _attr_entity_category = EntityCategory.CONFIG

    def __init__(self, device: ExampleDevice) -> None:
        """Initialize the button."""
        self._device = device
        self._attr_unique_id = f"{device.serial}_restart"

    async def async_press(self) -> None:
        """Restart the device."""
        await self._device.restart()
```

由于设备类,这个按钮被命名为"重新启动",而无需您给出名称或翻译密钥.
