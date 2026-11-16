---
title: 文本对语音实体
description: 构建文本对语音实体,正处于将文本变成音频状态,其中一次进行或以语言模型的形式流出。
sidebarLabel: 文字对语音
sidebarGroup: 语音与 AI
---

# 文本对语音实体 {#text-to-speech-entity}

文本对语音( TTS) 实体将文本转换为口语音频 。 Assist用它来表达它的响应,而`tts.speak`动作用它来播放一个媒体播放器上的信息. 从`TextToSpeechEntity`在`homeassistant.components.tts`中继承。 用于任何语音合成引擎,本地或云中.

## 的临时议程 {#properties}

文本对语音实体在 [一般实体属性](/core/entities/entity-class) 上方有这些属性 。 每个属性都可以以其`_attr_`属性设定,如`_attr_supported_languages`.

| 名称 | 类型 | 默认 | 说明 |
| ---- | ---- | ------- | ----------- |
| `supported_languages` | `list[str]` | 要求数 | 引擎能讲的语言. |
| `default_language` | `str` | 要求数 | 来电者不选时使用的语言. |
| `supported_options` | `list[str] \| None` | `None` | 呼叫者可能通过的选项, 如 `voice` 。 其他选项的电话被拒绝。 |
| `default_options` | `Mapping[str, Any] \| None` | `None` | 呼叫者不设置时使用的选项 。 |

Home Assistant 检查 `supported_languages` 和 `default_language` 当实体被添加时, 当其中之一缺失时, 则产生错误 。

## 支持的特性 {#supported-features}

文本对语音实体没有支持的特性. 流转输入是从您的代码中检测到的: 当您超过 `async_stream_tts_audio`, Home Assistant 知道引擎接受以块表示的文本 。

## 选项和音频格式 {#options-and-audio-formats}

呼叫者通过选项作为字典,合并在 `default_options` 上. 未放弃 `supported_options` 中的选项: 请求以 `ServiceValidationError` 失败 在它到达你的引擎之前。 `supported_languages`中未使用的语言也是如此。

首选的格式选项是例外. 它们总是被接受,并且Assist设置它们,所以音频符合播放它的设备.

| 选项 | 常数 |
| ------ | -------- |
| `preferred_format` | `ATTR_PREFERRED_FORMAT` |
| `preferred_sample_rate` | `ATTR_PREFERRED_SAMPLE_RATE` |
| `preferred_sample_channels` | `ATTR_PREFERRED_SAMPLE_CHANNELS` |
| `preferred_sample_bytes` | `ATTR_PREFERRED_SAMPLE_BYTES` |
| `preferred_bitrate` | `ATTR_PREFERRED_BITRATE` |

如果您在 `supported_options` 中列出其中之一, 它会到达您的引擎, 而引擎应该以该格式生成音频 。 如果您不这样做, Home Assistant 从选项中删除, 在引擎返回后用FFmpeg转换音频 。 自行制作正确的格式,可以保存转换步骤。 没有首选格式,结果会转换为MP3.

## 方法 {#methods}

### 生成音频 {#generate-audio}

执行 `async_get_tts_audio` 或 `get_tts_audio` 的屏蔽代码 。 它接收到完整的消息,并返回文件扩展名和音频字节的翻转,如{现在已经H2}. 返回 `(None, None)` 当引擎没有产生什么。 Home Assistant 然后给呼叫者带来错误 。

```python
async def async_get_tts_audio(
    self, message: str, language: str, options: dict[str, Any]
) -> TtsAudioType:
    """Load TTS audio from the engine."""
```

### 串流音频 {#stream-audio}

一个语言模型用块块写出答案. 如果您的引擎可以在文本完成前开始发言, 请同样执行 `async_stream_tts_audio` 。 它是美味可选的: 没有它, Home Assistant 收集整个消息并呼叫`async_get_tts_audio` 。

```python
async def async_stream_tts_audio(
    self, request: TTSAudioRequest
) -> TTSAudioResponse:
    """Generate speech from an incoming message."""
```

`TTSAudioRequest` 拥有 `language` 、 `options` 和 `message_gen` 的文本块的同步生成器 。 以文件 `extension` 和 `data_gen` 返回 `TTSAudioResponse`, 一个音频块的同步生成器 。

### 获取支持的声音 {#get-supported-voices}

`async_get_supported_voices(language)`是可选的。 返回一个语言的 `Voice(voice_id, name)` 列表, 前端提供它们作为 `voice` 选项的选择 。 返回 `None` 当引擎没有声音可以选择时 。 这是一个召回,所以它不能做 I/O: 当实体成立时获取声音.

## 状态 {#states}

状态是实体上次生成音频的时间戳, 或 `unknown` 在第一个之前 。 Home Assistant 设置并恢复它;`state` 属性是最终的 。

## 示例 {#example}

```python
from typing import Any

from homeassistant.components import tts
from homeassistant.core import callback

class MyTextToSpeech(tts.TextToSpeechEntity):
    """Text-to-speech with a cloud engine."""

    _attr_has_entity_name = True
    _attr_name = None
    _attr_supported_languages = ["en-US", "nl-NL"]
    _attr_default_language = "en-US"
    _attr_supported_options = [tts.ATTR_VOICE]

    def __init__(self, entry: MyConfigEntry) -> None:
        """Set up the entity."""
        self.client = entry.runtime_data
        self._attr_unique_id = f"{entry.entry_id}_tts"

    @callback
    def async_get_supported_voices(
        self, language: str
    ) -> list[tts.Voice] | None:
        """Return the voices for a language."""
        return [
            tts.Voice(voice.id, voice.name)
            for voice in self.client.voices
            if voice.language == language
        ]

    async def async_get_tts_audio(
        self, message: str, language: str, options: dict[str, Any]
    ) -> tts.TtsAudioType:
        """Turn the message into audio."""
        try:
            data = await self.client.speak(
                message, language, voice=options.get(tts.ATTR_VOICE)
            )
        except MyClientError:
            return None, None

        return "mp3", data
```
