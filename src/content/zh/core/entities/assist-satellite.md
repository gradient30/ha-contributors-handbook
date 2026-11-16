---
title: Assist 卫星实体
description: 构建 Assist 卫星实体, 用于接收语音指令并表达响应的设备 。
sidebarLabel: 卫星 Assist
sidebarGroup: 语音和AI
---

# Assist 卫星实体 {#assist-satellite-entity}

Assist的卫星实体代表一个带有:“麦克风”的装置,通常是人们交谈的扬声器,如语音助理扬声器。 设备将音频流到 Home Assistant, 它运行着 [输油管](/glossary/assist-pipeline) 并发送回回复 。 实体跟踪设备在对话中的位置,让自动化使其说话或提问。 从`AssistSatelliteEntity` 继承到`homeassistant.components.assist_satellite` 。

实体本身不进行语音识别或合成:这就是[语音对文本](/core/entities/stt),[对话](/core/entities/conversation)和[文本对语音](/core/entities/tts)实体在管道中的工作. 卫星实体在设备与管道之间移动音频和事件.

## 的临时议程 {#properties}

Assist卫星实体在[一般实体属性](/core/entities/entity-class)上面有这些属性。 每个属性都可以以其`_attr_`属性设定,如`_attr_pipeline_entity_id`.

| 名称 | 类型 | 默认 | 说明 |
| ---- | ---- | ------- | ----------- |
| `pipeline_entity_id` | `str \| None` | `None` | 选择此设备的管道的实体 [选择实体](/core/entities/select) ID 。 使用 `None` , 选择的管道 。 |
| `vad_sensitivity_entity_id` | `str \| None` | `None` | 选定实体的实体ID设置了如何敏感语音活动检测,决定沉默结束命令的时间. |
| `tts_options` | `dict[str, Any] \| None` | `None` | 选项传递给文本对语音的响应, 如设备的首选音频格式 。 见[选项和音频格式](/core/entities/tts#options-and-audio-formats). |

通过以下 `assist_pipeline` 集成 已准备好 : 管道的选定实体, 以及您可以添加到同一设备中的敏感度 。

## 支持的特性 {#supported-features}

将 `AssistSatelliteEntityFeature` 的值与位符或 (`|`) 运算符合并 。

| 数值 | 说明 |
| ----- | ----------- |
| `ANNOUNCE` | 该设备可以播放 Home Assistant 开始的宣告 。 执行`async_announce`。 在前端启用 `assist_satellite.announce` 动作和连接测试 。 |
| `START_CONVERSATION` | 设备可以播放一个公告,然后听一个回复. 执行`async_start_conversation`。 启用 `assist_satellite.start_conversation` 动作 。 `assist_satellite.ask_question`动作也使用它。 当管道使用内置的 Home Assistant 对话代理器时, 启动对话失败, 这不会让对话持续进行 。 |

## 运行管道 {#running-a-pipeline}

当设备听到它的唤醒词或有人按下它的按钮时,用 `async_accept_pipeline_from_satellite` 启动一个管道,并通过设备的音频流. 不要以另一种方式运行管道:这种方法会选择管道,使对话ID在转弯之间保持,并处理进行中的公告和问题.

```python
await self.async_accept_pipeline_from_satellite(
    audio_stream,
    start_stage=PipelineStage.STT,
    end_stage=PipelineStage.TTS,
    wake_word_phrase="okay nabu",
)
```

音频必须是16千赫,16位,单PCM. 当设备检测到醒字本身时, 或从 `PipelineStage.WAKE_WORD` 开始, 让 Home Assistant 检测它时, 通过 `wake_word_phrase` 。

要抓取语音设置向导的下一个醒字, Home Assistant 只查看以 `PipelineStage.STT` 开头的管道 `wake_word_phrase` 。 唤醒Home Assistant自己探测到的单词无法被截获.

每个管道事件都转到您的 `on_pipeline_event` 方法上, 即您转发设备需要的东西, 如响应音频的 URL 。 状态本身跟随事件,除了一个例外:在响应后,一旦设备完成演讲,就呼叫`tts_response_finished()`,返回`idle`.

## 方法 {#methods}

| 就在那时 | 要求数 | 说明 |
| ------ | -------- | ----------- |
| `on_pipeline_event(event)` | 对 | 处理一个运行中的管道事件。 召回,所以它不能等待。 |
| `async_get_configuration()` | 对 | 返回当前 `AssistSatelliteConfiguration` 。 回调,所以返回一个缓存副本,并在设置时从设备中获取. |
| `async_set_configuration(config)` | 对 | 对设备应用新配置 。 一旦设备和 Home Assistant 同意就返回 。 |
| `async_announce(announcement)` | 使用 `ANNOUNCE` | 播放公告. 只有玩完后才能返回。 |
| `async_start_conversation(start_announcement)` | 使用 `START_CONVERSATION` | 播放公告,然后听一个答复,并运行一个管道在上面。 公告播放完毕后返回 。 |

### 配置 {#configuration}

`AssistSatelliteConfiguration` 描述设备的唤醒词 :

| 外地 | 类型 | 说明 |
| ----- | ---- | ----------- |
| `available_wake_words` | `list[AssistSatelliteWakeWord]` | 设备可以收听的醒字,每个 16. H0}, `wake_word` 短语, 及其 `trained_languages` 。 |
| `active_wake_words` | `list[str]` | 装置的醒悟词的ID现在听. |
| `max_active_wake_words` | `int` | 脫                                                                                                         的                              的         的       的     的     的            的              的      的     的 的 的   的 的 的    的 的 的 的 的 的的 的 的 的 |

前端通过 `assist_satellite/get_configuration` 和 `assist_satellite/set_wake_words` WebSocket 命令读取并修改此内容 。 `get_configuration` 还返回卫星的 `pipeline_entity_id` 和 VAD 敏感实体( 作为 `vad_entity_id`) 。 `set_wake_words` 取一个 `wake_word_ids` 的列表 : Home Assistant 拒绝不在 `available_wake_words` 的ID, 以及比 `max_active_wake_words` 允许的更多的 ID 。 语音设置向导也使用 `assist_satellite/intercept_wake_word` 来捕捉下一个醒字并显示给用户.

### 通知 {#announcements}

`async_announce` 和 `async_start_conversation` 收到了 `AssistSatelliteAnnouncement` 。 Home Assistant 已经将信件变成音频, 所以您只播放媒体 :

| 外地 | 说明 |
| ----- | ----------- |
| `message` | 公告的文本,如果设备有,则在屏幕上显示. |
| `media_id` | 要播放的音频的 URL 。 |
| `preannounce_media_id` | 在 `media_id` 之前要播放的声音, 如鸣笛, 或者 `None` 跳过它 。 |
| `original_media_id` | 传呼者通过时的媒体ID,在Home Assistant解决之前. |
| `media_id_source` | 音频来自何处 : `url`, `media_id`, 或`tts` 。 |
| `tts_token` | 生成的文本对语音音频的符号, 如果有的话 。 |

用`ask_question`,Home Assistant؟ 妍娜打电话`async_start_conversation`,然后在演讲到文字之后停止下一个管道,并将记录稿与呼叫者给出的答案相匹配. 为此,在语音对文本时启动回复的管道,这是`async_accept_pipeline_from_satellite`的默认`start_stage`. 一个从钟声开始的管道 运行在过去的语音到文字。

Home Assistant 将状态设置为 `responding` 当一个宣告播放时, 当您的方法返回时, 返回到 `idle` 。 如果第一次有第二次通知出现,它会引起`SatelliteBusyError`。

## 状态 {#states}

国家沿着输油管, 从`AssistSatelliteState`enum。 Home Assistant 设置它; `state` 属性是最终的 。

| 数值 | 说明 |
| ----- | ----------- |
| `idle` | 等待唤醒词或按钮按下. |
| `listening` | 将语音命令流到 Home Assistant 。 |
| `processing` | Home Assistant正在研究命令的含义。 |
| `responding` | :: 发言或宣布。 |

## 示例 {#example}

```python
from homeassistant.components import assist_satellite
from homeassistant.components.assist_pipeline import (
    PipelineEvent,
    PipelineEventType,
)
from homeassistant.core import callback

Feature = assist_satellite.AssistSatelliteEntityFeature

class MySatellite(assist_satellite.AssistSatelliteEntity):
    """A voice satellite speaker."""

    _attr_has_entity_name = True
    _attr_name = None
    _attr_supported_features = Feature.ANNOUNCE

    def __init__(self, device: MyDevice) -> None:
        """Set up the entity."""
        self.device = device
        self._attr_unique_id = f"{device.serial}_satellite"

    @callback
    def async_get_configuration(
        self,
    ) -> assist_satellite.AssistSatelliteConfiguration:
        """Return the cached configuration."""
        return self.device.configuration

    async def async_set_configuration(
        self, config: assist_satellite.AssistSatelliteConfiguration
    ) -> None:
        """Send the new wake words to the device."""
        await self.device.set_wake_words(config.active_wake_words)

    @callback
    def on_pipeline_event(self, event: PipelineEvent) -> None:
        """Forward the response audio to the device."""
        if event.type is not PipelineEventType.TTS_END or not event.data:
            return

        if tts_output := event.data["tts_output"]:
            self.device.play(
                tts_output["url"], on_done=self.tts_response_finished
            )

    async def async_announce(
        self, announcement: assist_satellite.AssistSatelliteAnnouncement
    ) -> None:
        """Play an announcement and wait until it is done."""
        await self.device.play_and_wait(announcement.media_id)
```
