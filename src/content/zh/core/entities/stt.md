---
title: 语音对文本实体
description: 为 Assist 建立语音对文本实体,将音频流转换成文本 。
sidebarLabel: 语音对文本
sidebarGroup: 语音与 AI
---

# 语音对文本实体 {#speech-to-text-entity}

语音对文本( STT) 实体会接收音频流并返回所讲的文本 。 这是[输油管](/glossary/assist-pipeline)听到声音命令和理解它之间的一步。 从`SpeechToTextEntity` 继承到`homeassistant.components.stt` 。 用于任何语音识别引擎,本地或云中.

## 的临时议程 {#properties}

语音对文本实体在 [一般实体属性](/core/entities/entity-class) 上方有这些属性 。 六 `supported_*` 属性是抽象的: 每个属性作为属性执行, 没有 `_attr_` 快捷键 。

| 名称 | 类型 | 默认 | 说明 |
| ---- | ---- | ------- | ----------- |
| `supported_languages` | `list[str]` | 要求数 | 引擎理解的语言, 如 `en-US` 。 |
| `supported_formats` | `list[AudioFormats]` | 要求数 | 引擎接受的容器格式 。 |
| `supported_codecs` | `list[AudioCodecs]` | 要求数 | 引擎接受的解码器. |
| `supported_bit_rates` | `list[AudioBitRates]` | 要求数 | 调研结果为: |
| `supported_sample_rates` | `list[AudioSampleRates]` | 要求数 | 样本对引擎的接受率进行评分. |
| `supported_channels` | `list[AudioChannels]` | 要求数 | 频道布局引擎接受. |
| `audio_processing` | `SpeechAudioProcessing` | 见下文 | 音频应如何在到达引擎前′准备. |

## 支持的特性 {#supported-features}

语音对文本实体没有支持的特性。

## 音频格式 {#audio-formats}

每条溪流都伴着`SpeechMetadata`,上面写着音频是什么样子的. 在您实体获得流之前, Home Assistant 用 `check_metadata` 检查您的 `supported_*` 属性的元数据, 所以您只能收到您说可以处理的音频 。

| 栏 | 类型 | 数值 |
| ---------------------- | ---- | ------ |
| `language` | `str` | 是呀,一个是`supported_languages` |
| `format` | `AudioFormats` | `WAV`, `OGG` |
| `codec` | `AudioCodecs` | `PCM`, `OPUS` |
| `bit_rate` | `AudioBitRates` | `BITRATE_8`, `BITRATE_16`, `BITRATE_24`, `BITRATE_32` |
| `sample_rate` | `AudioSampleRates` | `SAMPLERATE_8000`, `SAMPLERATE_11000`, `SAMPLERATE_16000`, `SAMPLERATE_18900`, `SAMPLERATE_22000`, `SAMPLERATE_32000`, `SAMPLERATE_37800`, `SAMPLERATE_44100`, `SAMPLERATE_48000` |
| `channel` | `AudioChannels` | `CHANNEL_MONO`, `CHANNEL_STEREO` |

以便为 16 kHz, 16 位, 单 PCM 音频发送 WAV 格式的语音卫星, 所以如果想要与 Assist 硬件合作, 请至少支持该组合 。

### 音频处理 {#audio-processing}

`audio_processing` 从`homeassistant.components.stt.models` 返回 `SpeechAudioProcessing` 。 管道只在 `requires_external_vad` 是 `True` 时运行自己的语音活动检测, 并且它会在其事件中通过所有三个设置, 所以记录音频的设备可以准备它 。

| 外地 | 默认 | 说明 |
| ----- | ------- | ----------- |
| `requires_external_vad` | `True` | Home Assistant用自己的语音活动检测来检测语音的结束. 设定为 `False` 当引擎检测到它本身时 。 |
| `prefers_auto_gain_enabled` | `True` | 该音频应获得自动增益控制。 |
| `prefers_noise_reduction_enabled` | `True` | 音频应减少噪音。 |

## 方法 {#methods}

### 处理音频流 {#process-an-audio-stream}

执行`async_process_audio_stream`。 它接收元数据以及原始音频块的合成可移动性, 一旦流结束, 返回 `SpeechResult` 。

```python
async def async_process_audio_stream(
    self, metadata: SpeechMetadata, stream: AsyncIterable[bytes]
) -> SpeechResult:
    """Process an audio stream to STT service."""
```

`SpeechResult` 拥有公认的 `text` (或 `None`) 和 `SpeechResultState.SUCCESS` 或 `SpeechResultState.ERROR` 的 `result` 。

读读溪流,当它进来 并发送到你的引擎马上。 等待整个流首先将命令的长度添加到每个响应中.

### 部分结果 {#partial-results}

当您的引擎在用户仍在发言时返回记录稿时, 请执行 `async_process_audio_stream_with_progress` 代替 。 它是具有相同论据的同步生成器。 表示 0 个或更多 `PartialSpeechResult` 对象, 结尾处精确的 `SpeechResult` 。

```python
async def async_process_audio_stream_with_progress(
    self, metadata: SpeechMetadata, stream: AsyncIterable[bytes]
) -> AsyncGenerator[PartialSpeechResult | SpeechResult]:
    """Yield partial transcripts, then the final result."""
```

A `PartialSpeechResult` 拥有 `text` 的 完整 `text` 到目前为止, 不仅有 新 字 , 还有 可选 `speaker_id` 。 每个部分用相同的 `speaker_id` 替换上一个部分 。 没有这种方法,基类会调用`async_process_audio_stream`,只产生其最终结果.

部分结果是新的: Assist管道还没有使用它们,它只是等待最后的结果.

## 状态 {#states}

状态是实体上次处理音频的时间戳, 即`unknown` 第一次处理之前的时间戳 。 Home Assistant 设置并恢复它;`state` 属性是最终的 。

## 示例 {#example}

```python
from collections.abc import AsyncIterable

from homeassistant.components import stt

class MySpeechToText(stt.SpeechToTextEntity):
    """Speech-to-text with a cloud engine."""

    _attr_has_entity_name = True
    _attr_name = None

    def __init__(self, entry: MyConfigEntry) -> None:
        """Set up the entity."""
        self.client = entry.runtime_data
        self._attr_unique_id = f"{entry.entry_id}_stt"

    @property
    def supported_languages(self) -> list[str]:
        return ["en-US", "nl-NL"]

    @property
    def supported_formats(self) -> list[stt.AudioFormats]:
        return [stt.AudioFormats.WAV]

    @property
    def supported_codecs(self) -> list[stt.AudioCodecs]:
        return [stt.AudioCodecs.PCM]

    @property
    def supported_bit_rates(self) -> list[stt.AudioBitRates]:
        return [stt.AudioBitRates.BITRATE_16]

    @property
    def supported_sample_rates(self) -> list[stt.AudioSampleRates]:
        return [stt.AudioSampleRates.SAMPLERATE_16000]

    @property
    def supported_channels(self) -> list[stt.AudioChannels]:
        return [stt.AudioChannels.CHANNEL_MONO]

    async def async_process_audio_stream(
        self, metadata: stt.SpeechMetadata, stream: AsyncIterable[bytes]
    ) -> stt.SpeechResult:
        """Send the audio to the engine as it arrives."""
        try:
            text = await self.client.transcribe(stream, metadata.language)
        except MyClientError:
            return stt.SpeechResult(None, stt.SpeechResultState.ERROR)

        return stt.SpeechResult(text, stt.SpeechResultState.SUCCESS)
```
