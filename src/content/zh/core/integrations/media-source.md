---
title: 媒体来源
description: 从您在 Home Assistant 的媒体浏览器中集成的可浏览、 可搜索和可播放媒体 。
sidebarGroup: 集成功能
order: 10
---

# 媒体来源 {#media-source}

一个媒体来源在Home Assistant的媒体浏览器中提供您集成的媒体:一个相机,一个音乐库,电台,或生成语音的录音. 用户浏览它喜欢文件夹,并在任何支持它们的媒体播放器上播放项目.

## 添加媒体来源 {#add-a-media-source}

创建`media_source.py` 。 列表中没有任何变化 : Home Assistant 自己找到文件 。 它必须有一个 `async_get_media_source` 函数返回您的媒体源 :

```python
from homeassistant.components.media_player import BrowseError, MediaClass
from homeassistant.components.media_source import (
    BrowseMediaSource,
    MediaSource,
    MediaSourceItem,
    PlayMedia,
    Unresolvable,
)
from homeassistant.core import HomeAssistant

async def async_get_media_source(hass: HomeAssistant) -> ExampleMediaSource:
    """Set up the Example media source."""
    return ExampleMediaSource(hass)

class ExampleMediaSource(MediaSource):
    """Provide the recordings of Example cameras."""

    name = "Example"

    def __init__(self, hass: HomeAssistant) -> None:
        """Initialize the media source."""
        super().__init__(DOMAIN)
        self.hass = hass

    async def async_browse_media(
        self, item: MediaSourceItem
    ) -> BrowseMediaSource:
        """Return the media at a location."""

    async def async_resolve_media(self, item: MediaSourceItem) -> PlayMedia:
        """Return a playable URL for an item."""
```

| 就在那时 | 它会做什么 |
| --- | --- |
| `async_browse_media(item)` | 在一个位置返回`BrowseMediaSource`。 当失败时提高 `BrowseError` 。 |
| `async_resolve_media(item)` | 将项目转换为 `PlayMedia` , 并有一个可以播放的 URL 。 当失败时提高 `Unresolvable` 。 |
| `async_search_media(item, query)` | 可选的 搜索你的媒体。 见[搜索](/core/integrations/media-source#search). |

{H驰}是用户见上文。 没有它,驰名域就见上文.

## 标识符 {#identifiers}

每个项目都有像`media-source://<domain>/<identifier>`一样的URI. 由你来决定标识是什么样子 对于一个等级,一个具有`/`的路径运作良好,比如`albums/1234`. 你的方法是`item.identifier`。 您的媒体来源的根是空的 。

以 `generate_media_source_id(DOMAIN, "albums/1234")` 和 `is_media_source_id(value)` 从 `homeassistant.components.media_source` 构建并检查这些 URI 。

## 浏览 {#browse}

与孩子一起返回该地点的物品:

```python
async def async_browse_media(
    self, item: MediaSourceItem
) -> BrowseMediaSource:
    """Return the media at a location."""
    if item.identifier:
        return await self._async_browse_camera(item.identifier)

    return BrowseMediaSource(
        domain=DOMAIN,
        identifier=None,
        media_class=MediaClass.APP,
        media_content_type="",
        title="Example",
        can_play=False,
        can_expand=True,
        children_media_class=MediaClass.DIRECTORY,
        children=[
            BrowseMediaSource(
                domain=DOMAIN,
                identifier=camera.id,
                media_class=MediaClass.DIRECTORY,
                media_content_type="",
                title=camera.name,
                can_play=False,
                can_expand=True,
            )
            for camera in self._cameras
        ],
    )
```

| 外地 | 这是什么 |
| --- | --- |
| `domain` | 您的域名 |
| `identifier` | 物品的标识符. 为根. |
| `media_class` | 物品是什么,比如`MediaClass.DIRECTORY`,`MediaClass.MUSIC`,`MediaClass.VIDEO`,或`MediaClass.IMAGE` |
| `media_content_type` | 内容的 MIME 类型或介质类型, 如 `"audio/mpeg"` |
| `title` | 用户名见 |
| `can_play` | 是否可以播放项目 |
| `can_expand` | 是否要有孩子浏览 |
| `can_search` | 用户是否可以从此项中搜索 。 默认为 `False` 。 |
| `search_media_classes` | 媒体类用户在此搜索时可以过滤 |
| `children` | 孩子们 只在浏览的项目上 。 |
| `children_media_class` | 儿童传媒班. 如果你不说就算了 |
| `thumbnail` | 缩略图的 URL |
| `not_shown` | 被忽略的儿童数量。 默认为 `0`。 |

## 决定 {#resolve}

当噬者播放一个项目时, 返回 URL 和 MIME 类型 :

```python
async def async_resolve_media(self, item: MediaSourceItem) -> PlayMedia:
    """Return a playable URL for an item."""
    if (recording := self._recordings.get(item.identifier)) is None:
        raise Unresolvable(
            translation_domain=DOMAIN,
            translation_key="recording_not_found",
            translation_placeholders={"item": item.identifier},
        )

    return PlayMedia(recording.url, "video/mp4")
```

URL可以是绝对的,也可以是Home Assistant服务的相对路径. `item.target_media_player` 持有要播放的媒体播放器的实体ID, 如果您需要调整 URL 。 `Unresolvable` 和`BrowseError` 都支持翻译信件 。

## 搜索 {#search}

搜索是可选的。 设定 `can_search=True` 上的项目用户可以搜索, 如 root 或某些文件夹, 并执行 `async_search_media` :

```python
from homeassistant.components.media_player import (
    SearchMedia,
    SearchMediaQuery,
)

async def async_search_media(
    self, item: MediaSourceItem, query: SearchMediaQuery
) -> SearchMedia:
    """Search the media."""
    tracks = await self._client.search(query.search_query)

    return SearchMedia(
        result=[
            BrowseMediaSource(
                domain=DOMAIN,
                identifier=track.id,
                media_class=MediaClass.TRACK,
                media_content_type=track.mime_type,
                title=track.title,
                can_play=True,
                can_expand=False,
            )
            for track in tracks
            if not query.media_filter_classes
            or MediaClass.TRACK in query.media_filter_classes
        ]
    )
```

`item` 告诉你搜索从哪里开始, 这样你就可以将结果限制在媒体的那部分 。 查询有 `search_query` (用户输入的是什么), 以及可选的 `media_content_type`, `media_content_id` 和 `media_filter_classes` 。

要让用户过滤,请在可搜索项目上设定`search_media_classes`, 如`[MediaClass.ALBUM, MediaClass.ARTIST, MediaClass.TRACK]`. 用户选择的类到达 `media_filter_classes` 。 只有这些课程的退货品。

## 使用来自另一集的媒体来源 {#use-media-sources-from-another-integration}

一个媒体玩家集成也可以浏览,搜索和解决媒体来源:

```python
from homeassistant.components.media_source import (
    async_browse_media,
    async_resolve_media,
)

result = await async_browse_media(hass, "media-source://example")
play_media = await async_resolve_media(
    hass,
    "media-source://example/recording_123",
    target_media_player="media_player.living_room",
)
```

搜索一样的方式。
