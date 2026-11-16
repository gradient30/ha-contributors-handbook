---
title: 醒字检测实体
description: 建立醒字实体,当有人说醒字时,听一流的音频和报告.
sidebarLabel: 醒字检测
sidebarGroup: 语音与 AI
---

# 醒字检测实体 {#wake-word-detection-entity}

一个醒字检测实体听一流的音频并告诉Home Assistant当它听到一个醒字(也叫热字),比如"OK Nabu". 这是在Home Assistant中运行醒字检测的[输油管](/glossary/assist-pipeline)的第一步,而不是在设备上运行. 从`WakeWordDetectionEntity` 继承到`homeassistant.components.wake_word` 。 域名为`wake_word`.

许多语音卫星探测到设备本身上的醒号单词. 他们不需要这个实体:它是用于运行在Home Assistant一侧的引擎,比如通过怀俄明集成打开WakeWord.

## 的临时议程 {#properties}

醒字检测实体没有自己的属性. [一般实体属性](/core/entities/entity-class) 应用 。 基础课设置 `entity_category` 到 `EntityCategory.DIAGNOSTIC` 并关闭投票。

## 支持的特性 {#supported-features}

醒字检测实体没有支持的特性.

## 音频 {#audio}

音频流是 `(audio_chunk, timestamp)` tuples 的 async 行程 :

- `audio_chunk`: 16位签名单 PCM 样本在 16 kHz.
- `timestamp`:溪流开始后的毫秒数.

在管道中,醒字检测和语音对文本共享一个音频流. 你的实体消费的一块块 已经用到语音了 除非你还给我 如果您的引擎缓冲音频, 返回结果的 `queued_audio` 中的缓冲块, 因此语音命令的启动不会丢失 。

## 方法 {#methods}

### 获得支持的醒字 {#get-supported-wake-words}

执行 `get_supported_wake_words` 以返回实体能够检测到的提醒字 。 尽管有这个名字,但它是Aync。

```python
async def get_supported_wake_words(self) -> list[WakeWord]:
    """Return a list of supported wake words."""
```

A `WakeWord` 拥有 `id` (实体内的独特性) , 用于 UI 的 `name` , 以及可选的 `phrase` , 人们实际说的单词 。 前端通过 `wake_word/info` 获取此列表 WebSocket命令,10秒后放弃,所以保持速度。

### 处理音频流 {#process-an-audio-stream}

执行`_async_process_audio_stream`。 注意领先的下划线: 公众 `async_process_audio_stream` 将其包装并更新状态 。

```python
async def _async_process_audio_stream(
    self,
    stream: AsyncIterable[tuple[bytes, int]],
    wake_word_id: str | None,
) -> DetectionResult | None:
    """Try to detect a wake word in an audio stream."""
```

`wake_word_id`是用来听的唤醒词,或者`None`用来听其中任何一个。 返回 `None` 当流结束时没有检测到 。 当听到唤醒词时,返回 `DetectionResult` :

| 外地 | 类型 | 说明 |
| ----- | ---- | ----------- |
| `wake_word_id` | `str` | 检测到的醒字的ID. |
| `wake_word_phrase` | `str` | 探测到的唤醒词的短语. |
| `timestamp` | `int \| None` | 您检测到的块的时间戳 。 |
| `queued_audio` | `list[tuple[bytes, int]] \| None` | 你消费了语音对文本 仍然需要。 |

## 状态 {#states}

状态是最后一次检测的时间戳,即`unknown`在第一次检测之前. Home Assistant 设置并恢复它;`state` 属性是最终的 。

## 示例 {#example}

```python
from collections.abc import AsyncIterable

from homeassistant.components import wake_word

class MyWakeWord(wake_word.WakeWordDetectionEntity):
    """Wake word detection with a local engine."""

    _attr_has_entity_name = True
    _attr_name = None

    def __init__(self, entry: MyConfigEntry) -> None:
        """Set up the entity."""
        self.engine = entry.runtime_data
        self._attr_unique_id = f"{entry.entry_id}_wake_word"

    async def get_supported_wake_words(self) -> list[wake_word.WakeWord]:
        """Return the wake words of the engine."""
        return [wake_word.WakeWord(id="okay_nabu", name="Okay Nabu")]

    async def _async_process_audio_stream(
        self,
        stream: AsyncIterable[tuple[bytes, int]],
        wake_word_id: str | None,
    ) -> wake_word.DetectionResult | None:
        """Feed audio to the engine until it hears the wake word."""
        async for chunk, timestamp in stream:
            if self.engine.process(chunk):
                return wake_word.DetectionResult(
                    wake_word_id="okay_nabu",
                    wake_word_phrase="okay nabu",
                    timestamp=timestamp,
                )

        return None
```
