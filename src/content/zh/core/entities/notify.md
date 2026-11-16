---
title: 通知实体
description: 构建一个向设备或服务发送消息的通知实体,比如聊天,电子邮件地址,或者显示.
sidebarLabel: 通知
sidebarGroup: 输入与助手
---

# 通知实体 {#notify-entity}

通知实体向设备或服务发送消息:短信,电子邮件,聊天信息,或设备显示时的文本. 消息一传,就不见了. 从`NotifyEntity` 继承到`homeassistant.components.notify` 。

如果设备有留下的文本值, 并且人们可以改变, 请使用 [文本](/core/entities/text) 实体 。

## 的临时议程 {#properties}

一个通知实体没有平台特定属性. 每个实体的通用属性,如`name`,`available`和`unique_id`,都在[实体类别](/core/entities/entity-class)上. 一个通知实体不投票:`should_poll`是`False`默认的。

## 支持的特性 {#supported-features}

| 常数 | 说明 |
| --- | --- |
| `NotifyEntityFeature.TITLE` | 该实体支持消息旁边的标题 。 |

设置特性为 `_attr_supported_features` 。 默认不是特性 。 当您执行同步 `send_message` 时, 基准类仅在设置 `TITLE` 时通过 `title` 。 见[支持的特性](/glossary/supported-features).

## 方法 {#methods}

### 发送消息 {#send-message}

他是个自动程序 。 他是个坏人

```python
class MyNotifier(NotifyEntity):
    

# Implement one of these methods. {#record-a-notification}

    def send_message(self, message: str, title: str | None = None) -> None:
        """Send a message."""

    async def async_send_message(
        self, message: str, title: str | None = None
    ) -> None:
        """Send a message."""
```

### 记录通知 {#states}

基础类记录了通过`notify.send_message`发送的每一封信. 当您的整合也以其他方式发送消息时, 例如通过它自己带有额外选项的动作, 自己记录: 从事件循环以外的线索中调用 `self._async_record_notification()` 或 `self._record_notification()` 。 其更新州并撰.

只记录Home Assistant发送的信件 。 从外部传来的信息,或者另一个系统发送的信息,不属于通知实体:为这些消息使用[事件](/core/entities/event)实体.

## 状态 {#example}

通知实体的状态是最后一个从Home Assistant发送的信件的时间戳,作为协调世界时的ISO 8601字符串. 这是`unknown`直到第一个消息。 基础类记录在您的发送方法返回后, 并在重启后恢复它 。 你不能自己设定:`state`是最终的.

## 示例 {#示例}

```python
from homeassistant.components.notify import (
    NotifyEntity,
    NotifyEntityFeature,
)

class ExampleChatNotifier(NotifyEntity):
    """Send messages to a chat channel."""

    _attr_has_entity_name = True
    _attr_supported_features = NotifyEntityFeature.TITLE

    def __init__(self, client: ExampleClient, channel: str) -> None:
        """Initialize the notifier."""
        self._client = client
        self._channel = channel
        self._attr_name = channel
        self._attr_unique_id = f"{client.account_id}_{channel}"

    async def async_send_message(
        self, message: str, title: str | None = None
    ) -> None:
        """Send a message to the channel."""
        await self._client.post(self._channel, message, title=title)
```

频道名称来自聊天服务,所以示例 Musevenis使用它作为实体的名称而不是翻译密钥. 见[命名实体](/core/entities/naming).
