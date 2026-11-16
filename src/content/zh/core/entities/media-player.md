---
title: 媒体播放器实体
description: 控制任何播放音频或视频,从智能扬声器到电视或AV接收器.
sidebarLabel: 媒体播放器
sidebarGroup: 媒体
---

# 媒体播放器实体 {#media-player-entity}

媒体播放器实体控制着播放媒体的东西:智能扬声器,电视机,流线棒,AV接收器,或放映机. 它报告正在播放的作品,有艺术作品和位置,并使用播放,暂停,音量,源,播放此URL等命令. 它是Home Assistant 中最丰富的实体类型之一, 但您只执行您设备所能做的 : [支持的特性](/glossary/supported-features) 决定存在哪些动作和控件 。

充分履行 `MediaPlayerEntity` 继承, 导入 `homeassistant.components.media_player` 。 前端如何显示媒体播放器,请参见[媒体播放器更多信息视图](/design/more-info/media-player).

从 Home Assistant 演示中嵌入的仪表板卡的现场演示。 演讲者演奏,暂停,跳过音轨, 是吗?

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
        "entity_id": "media_player.living_room_speaker",
        "state": "playing",
        "attributes": {
          "friendly_name": "Living room speaker",
          "media_content_type": "music",
          "media_title": "Clair de lune",
          "media_artist": "Claude Debussy",
          "volume_level": 0.4,
          "supported_features": 16437
        }
      }
    ]
  </script>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "tile",
        "entity": "media_player.living_room_speaker",
        "features": [
          {
            "type": "media-player-playback"
          },
          {
            "type": "media-player-volume-slider"
          }
        ]
      }
    </script>
  </ha-embed-card>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "media-control",
        "entity": "media_player.living_room_speaker"
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

## 的临时议程 {#properties}

这些属性是媒体播放器实体特有的. 每个实体的通用属性都在 [实体类别](/core/entities/entity-class) 上 。 全部默认为`None`, 除非表格另有说明。

### 玩家 {#player}

| 名称 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- |
| `state` | `MediaPlayerState \| None` | `None` | 玩家状态. 见[国家](/core/entities/media-player#states). |
| `device_class` | `MediaPlayerDeviceClass \| None` | `None` | 这是什么样的装置? 见[设备类](/core/entities/media-player#device-classes). |
| `volume_level` | `float \| None` | `None` | 卷,从`0`到`1` |
| `volume_step` | `float` | `0.1` | 注意了, 注意了, 实体说明上也设置了表格。 |
| `is_volume_muted` | `bool \| None` | `None` | 音量是否为哑声 。 |
| `source` | `str \| None` | `None` | 选定输入源 。 |
| `source_list` | `list[str] \| None` | `None` | 用户可以 该死的从输入源中选择,作为人可读名. 仅在玩 该死的 `SELECT_SOURCE` 时显示 。 |
| `sound_mode` | `str \| None` | `None` | 选定的声音模式 。 |
| `sound_mode_list` | `list[str] \| None` | `None` | 用户可以选择的声音模式 。 仅在玩家有 `SELECT_SOUND_MODE` 时显示 。 |
| `shuffle` | `bool \| None` | `None` | 喽啰是否开着. |
| `repeat` | `RepeatMode \| str \| None` | `None` | 重复模式: {cyclo},`RepeatMode.ALL`,或`RepeatMode.ONE`在这一方面. |
| `group_members` | `list[str] \| None` | `None` | 用于同步播放的玩家实体ID 。 如果你的平台有集团领导,请先放. |
| `app_id` | `str \| None` | `None` | 正在运行的应用程序的ID 。 |
| `app_name` | `str \| None` | `None` | 正在运行的应用程序的名称 。 |
| `supported_features` | `MediaPlayerEntityFeature` | `MediaPlayerEntityFeature(0)` | 玩家能做什麽? 见[支持的特性](/core/entities/media-player#supported-features). |

### 当前媒体 {#current-media}

| 名称 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- |
| `media_content_id` | `str \| None` | `None` | 正在播放的媒体的ID。 |
| `media_content_type` | `MediaType \| str \| None` | `None` | 播放的媒体类型, 如 `MediaType.MUSIC` 或 `MediaType.TVSHOW` 。 |
| `media_duration` | `int \| None` | `None` | 媒体持续时间以秒计. |
| `media_position` | `int \| None` | `None` | 媒体中的位置 秒。 |
| `media_position_updated_at` | `datetime \| None` | `None` | 当 `media_position` 最后一次有效时 。 使用 `homeassistant.util.dt.utcnow()` 。 |
| `media_title` | `str \| None` | `None` | 传媒名号. |
| `media_artist` | `str \| None` | `None` | 艺术家,为音乐。 |
| `media_album_name` | `str \| None` | `None` | 专辑,用于音乐. |
| `media_album_artist` | `str \| None` | `None` | 专辑艺术家,用于音乐. |
| `media_track` | `int \| None` | `None` | 音轨号,用于音乐. |
| `media_series_title` | `str \| None` | `None` | 系列剧名, 你也是为了电视剧. |
| `media_season` | `str \| None` | `None` | 该季,用于电视节目. |
| `media_episode` | `str \| None` | `None` | 剧集,用于电视节目. |
| `media_channel` | `str \| None` | `None` | o 播放的频道。 |
| `media_playlist` | `str \| None` | `None` | 播放列表的标题 。 |
| `media_image_url` | `str \| None` | `None` | 艺术品的URL。 |
| `media_image_remotely_accessible` | `bool` | `False` | 前端能否直接装入 `media_image_url` 。 当`False`,Home Assistant代理图像时. |
| `media_image_hash` | `str \| None` | URL 的宽度 | 艺术聆讯时更改, 因此浏览器不会显示缓存图像 。 当 URL 保持不变但图像不不变时设定它 。 |

前端根据 `media_position` 和 `media_position_updated_at` 自行移动位置栏 。 因此只有在位置真的跳跃时,比如在寻找或新赛道之后,而不是每秒更新两者. 每秒更新一次,只填充数据库。

当状态是 `off` 时, Home Assistant 将媒体属性, 音量, 源, 声音模式, 洗牌, 和重复属性, 以及实体图片 。 `group_members` 属性保留, 用于支持分组的玩家 。

## 支持的特性 {#supported-features}

将 `MediaPlayerEntityFeature` 的旗帜与位符或 (`|`) 运算符合并 。 Home Assistant 只有在实体有它的旗帜时才会提供动作 。

| 旗帜 | 说明 | 执行 |
| --- | --- | --- |
| `TURN_ON` | 打开玩家。 | `turn_on` |
| `TURN_OFF` | 关掉玩家 | `turn_off` |
| `PLAY` | 开始或恢复播放 。 | `media_play` |
| `PAUSE` | 暂停播放。 | `media_pause` |
| `STOP` | 停止播放回放。 | `media_stop` |
| `PREVIOUS_TRACK` | 转到上一个音轨。 | `media_previous_track` |
| `NEXT_TRACK` | 入下一轨. | `media_next_track` |
| `SEEK` | 跳到一个位置。 | `media_seek` |
| `VOLUME_SET` | 将音量设定为关卡 。 | `set_volume_level` |
| `VOLUME_STEP` | 上下翻转音量. | `volume_up` 和 `volume_down` , 或依赖 `set_volume_level` |
| `VOLUME_MUTE` | 哑而无哑. | `mute_volume` |
| `SELECT_SOURCE` | 选择输入源 。 | `select_source` 和 `source_list` (韩语) |
| `SELECT_SOUND_MODE` | 选择一个声音模式 。 | `select_sound_mode` 和 `sound_mode_list` (韩语) |
| `PLAY_MEDIA` | 播放特定的媒体片段. | `play_media` |
| `MEDIA_ENQUEUE` | 玩家处理`enqueue` `play_media` 的选项 。 | `play_media` |
| `MEDIA_ANNOUNCE` | 玩家处理`announce` `play_media` 的选项 。 | `play_media` |
| `BROWSE_MEDIA` | 浏览玩家可以玩的媒体. | `async_browse_media` |
| `SEARCH_MEDIA` | 搜索玩家可以玩的媒体. | `async_search_media` |
| `CLEAR_PLAYLIST` | 清除游戏队列 。 | `clear_playlist` |
| `SHUFFLE_SET` | 打开或关闭洗牌机。 | `set_shuffle` |
| `REPEAT_SET` | 设置重复模式 。 | `set_repeat` |
| `GROUPING` | 用于同步播放的分组玩家 。 | `join_players` 和 `unjoin_player` , 和 `group_members` |

## 设备类 {#device-classes}

设备类告诉 Home Assistant 和同步的语音助手, 这是什么样的设备 。 使用 `MediaPlayerDeviceClass` enum 。

| 设备类 | 说明 |
| --- | --- |
| `tv` | 电视 |
| `speaker` | 扬声器或立体声系统. |
| `receiver` | 嚼音向秘书处提交音频视频接收器,将音频发送给扬时光机,将视频发送给显示器. |
| `projector` | 投影仪 |

## 播放媒体 {#playing-media}

`media_player.play_media` 动作调用 `play_media` 有媒体类型、 媒体ID 和 `kwargs` 中的一些选项 :

- `enqueue`:一个`MediaPlayerEnqueue`,上面写着该怎么排队。 `add` 将媒体添加到队列的结尾, `next` 在当前项目之后播放, `play` 现在播放并保留队列, `replace` 现在播放并清除队列。 动作编辑器只提供给玩家使用`MEDIA_ENQUEUE`,但Home Assistant没有过滤出来,所以如果不支持它就忽略它.
- `announce` : `True` 用于宣布, 如门铃声或文字对语音消息 。 暂停播放,播放公告,并恢复播放。 动作编辑器只提供给 `MEDIA_ANNOUNCE` 的玩家.
- `extra`:一个字典,其中包含动作呼吁中的额外选项. 总是出现, 默认为空 。

一个动作呼叫可以有 `enqueue` 或 `announce` , 从来没有两者。

`media_type` 通常是 `MediaType` 值 。 如果您的集成处理的介质不符合其中任何一种,那么使用您的集成域作为类型是好的.

## 浏览媒体 {#browsing-media}

用 `BROWSE_MEDIA` 执行 `async_browse_media` 。 它为根获得 `media_content_type` 和 `media_content_id`, 两者均为 `None`, 并返回 `BrowseMedia` 对象 : 项树, 每个项都有标题, 介质类 (`MediaClass`), ID, 是否可以播放或扩展, 以及缩略图 。 提高`BrowseError`的ID你不知道。

### 媒体来源 {#media-sources}

媒体源集成允许任何集成提供媒体:本地文件,文本对语音,电台,摄像头. 如果您的玩家可以播放一个 URL, 请在浏览器中免费添加这些源 。 将浏览呼叫传递到 `media_source.async_browse_media` , 或将其根添加到您自己的树上 。 当您播放媒体源代码时, 请先用 `media_source.async_resolve_media` 解析为 URL, 然后通过 `async_process_play_media_url` 运行该 URL, 将相对的 URL 变成您设备可以到达的 。

### 浏览器中的艺术工作 {#artwork-in-the-browser}

如果您的缩略图只能从将这些缩略图从本地网络中获取, 请通过 Home Assistant 代理它们, 因此它们也会在离家的 company app 中工作 。 将 `BrowseMedia` 项目的 `thumbnail` 设置为 `self.get_browse_image_url(media_content_type, media_content_id, media_image_id)` 。 当浏览器加载时,Home Assistant会拨打您的`async_get_browse_image`. 用 `self._async_fetch_image(url)` 获取图像, 并返回内容和内容类型的翻转 。

> [!WARNING]
> 从不使用 `media_image_id` 的 URL 。 任何能联系到代理的,都可以使用它从本地网络中获取任何信息.

只有请求来自网络外时的代理:`is_local_request(hass)`来自`homeassistant.helpers.network`告诉你. 现在播放的作品要经过 `async_get_media_image`, 它有自己的缓存: 您只需要设置 `media_image_url` 。

## 搜索媒体 {#searching-media}

用 `SEARCH_MEDIA` 执行 `async_search_media` 。 它得到一个 `SearchMediaQuery` 带有 `search_query` 的 `media_content_type` 和可选的 `media_content_id` 的 `media_content_id` 搜索, 和 `media_filter_classes` 的 `MediaClass` 值列表来限制结果 。 返回 `SearchMedia` 与 `BrowseMedia` 中的匹配项 `result` 。

## 方法 {#methods}

每种方法都有同步和Aync变体. 执行其中一项。 亚音变体起始 Sungs `async_`, 如 `async_media_play`.

| 就在那时 | 说明 |
| --- | --- |
| `turn_on()` | 打开玩家。 |
| `turn_off()` | 关掉玩家 |
| `media_play()` | 开始或恢复播放 。 |
| `media_pause()` | 暂停播放。 |
| `media_stop()` | 停止播放回放。 |
| `media_previous_track()` | 转到上一个音轨。 |
| `media_next_track()` | 入下一轨. |
| `media_seek(position: float)` | 跳到位置,数秒。 |
| `set_volume_level(volume: float)` | 设定音量, 从 `0` 到 `1` 。 |
| `mute_volume(mute: bool)` | 哑或哑. |
| `select_source(source: str)` | 选择输入源 。 |
| `select_sound_mode(sound_mode: str)` | 选择一个声音模式 。 |
| `play_media(media_type, media_id, **kwargs)` | 播放媒体片段. 见[播放媒体](/core/entities/media-player#playing-media). |
| `clear_playlist()` | 清除游戏队列 。 |
| `set_shuffle(shuffle: bool)` | 打开或关闭洗牌机。 |
| `set_repeat(repeat: RepeatMode)` | 设置重复模式 。 |
| `join_players(group_members: list[str])` | 用这个把这些玩家集合起来 |
| `unjoin_player()` | 从它的组中删除此玩家 。 |
| `async_browse_media(media_content_type, media_content_id)` | 仅限Async. 返回树 `BrowseMedia` 。 |
| `async_search_media(query)` | 仅限Async. 返回 `SearchMedia` 结果 。 |
| `async_get_browse_image(media_content_type, media_content_id, media_image_id)` | 仅限Async. 返回浏览器缩略图的字节和内容类型 。 |

有些方法有默认,您可以覆盖:

- `toggle` : 当玩家是`off`时打开, 否则关闭 。
- `media_play_pause`:当状态是`playing`时暂停,否则播放.
- `volume_up`和`volume_down`:由`volume_step`通过`set_volume_level`更改`volume_level`,当玩家有`VOLUME_SET`时. 如果您的设备有自己的音量按钮, 请自己执行 。

## 状态 {#states}

从 `state` 返回 `MediaPlayerState` 。

| 状态 | 说明 |
| --- | --- |
| `off` | 玩家关闭,在打开前不接受命令. |
| `on` | 玩家开始,但你不知道更多。 |
| `idle` | 玩家开机并接受命令,但无所事事,就像家用屏幕上一样. |
| `playing` | 发展 发展 发展 发展 发展 发展 |
| `paused` | 媒体被装入并暂停。 |
| `buffering` | 玩家已经准备好玩了 |

> [!NOTE]
> `MediaPlayerState.STANDBY`已经贬值了。 使用 `off` 或 `idle` 代替 。

许多玩家在待命时无法被控制. 如果Home Assistant仍然可以在另一条路上打开设备,比如Wake-on-LAN或者对不同连接的电源命令,显示为`off`. 如果无法从 Home Assistant 打开, 请标记实体 [无](/glossary/unavailable) 。 质量尺度的[实体无规则](/core/quality-scale/entity-unavailable)有细节。

## 示例 {#example}

播放,暂停,设定音量,播放URL的网络扬声器,包括媒体来源.

```python
from typing import Any

from homeassistant.components import media_source
from homeassistant.components.media_player import (
    BrowseMedia,
    MediaPlayerDeviceClass,
    MediaPlayerEntity,
    MediaPlayerEntityFeature,
    MediaPlayerState,
    MediaType,
    async_process_play_media_url,
)

class MySpeaker(MediaPlayerEntity):
    """A network speaker."""

    _attr_has_entity_name = True
    _attr_name = None
    _attr_device_class = MediaPlayerDeviceClass.SPEAKER
    _attr_supported_features = (
        MediaPlayerEntityFeature.PLAY
        | MediaPlayerEntityFeature.PAUSE
        | MediaPlayerEntityFeature.VOLUME_SET
        | MediaPlayerEntityFeature.PLAY_MEDIA
        | MediaPlayerEntityFeature.BROWSE_MEDIA
    )

    def __init__(self, speaker: MySpeakerClient) -> None:
        """Initialize the speaker."""
        self._speaker = speaker
        self._attr_unique_id = speaker.serial

    @property
    def state(self) -> MediaPlayerState:
        """Return the state of the speaker."""
        if self._speaker.is_playing:
            return MediaPlayerState.PLAYING
        return MediaPlayerState.IDLE

    @property
    def volume_level(self) -> float:
        """Return the volume, from 0 to 1."""
        return self._speaker.volume / 100

    async def async_media_play(self) -> None:
        """Resume playback."""
        await self._speaker.play()

    async def async_media_pause(self) -> None:
        """Pause playback."""
        await self._speaker.pause()

    async def async_set_volume_level(self, volume: float) -> None:
        """Set the volume."""
        await self._speaker.set_volume(round(volume * 100))

    async def async_browse_media(
        self,
        media_content_type: MediaType | str | None = None,
        media_content_id: str | None = None,
    ) -> BrowseMedia:
        """Browse the audio of media sources."""
        return await media_source.async_browse_media(
            self.hass,
            media_content_id,
            content_filter=lambda item: item.media_content_type.startswith(
                "audio/"
            ),
        )

    async def async_play_media(
        self, media_type: MediaType | str, media_id: str, **kwargs: Any
    ) -> None:
        """Play a URL or a media source."""
        if media_source.is_media_source_id(media_id):
            play_item = await media_source.async_resolve_media(
                self.hass, media_id, self.entity_id
            )
            media_id = play_item.url

        url = async_process_play_media_url(self.hass, media_id)
        await self._speaker.play_url(url)
```
