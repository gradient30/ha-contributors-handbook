---
title: 图像实体
description: 显示一个时而变化的静态图像,如地图、快照或QR代码。
sidebarLabel: 图像
sidebarGroup: 媒体
---

# 图像实体 {#image-entity}

一个图像实体服务于一个单一的静态图像. 想想真空图,门铃的最后一个快照,或宾客网络的QR码. 这是[相机实体](/core/entities/camera)的一个简单得多的兄弟姐妹:没有溪流,没有录音,也没有打开或关闭。 当画面改变时,实体会这么说,前端会获取新的画面.

从`ImageEntity`继承,从`homeassistant.components.image`导入。 当您的设备或服务拥有时常更新的图像时使用它. 如果显示现场视频,或者需要按要求抓帧,则使用相机实体代替.

你以两种方式之一给出图像:

- **A URL**:设置`image_url`,和Home Assistant下载图像,检测其内容类型,并缓存.
- **Bytes**:执行`async_image`(或`image`),并亲自返回图像数据.

## 的临时议程 {#properties}

这些属性是图像实体特有的. 每个实体的通用属性都在 [实体类别](/core/entities/entity-class) 上 。

| 名称 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- |
| `content_type` | `str` | `"image/jpeg"` | 图像的 MIME 类型 。 当图像来自 `image_url` 时自动设定 。 |
| `image_last_updated` | `datetime \| None` | `None` | 当影像最后变化时. 这是实体的状态,当图像改变时,前端会反射图像. |
| `image_url` | `str \| None` | `UNDEFINED` | 要下载图像的 URL 。 如果您返回 `async_image` 的字节, 请保留它 。 |

图像实体默认不进行民意测验(`should_poll`是`False`),因为您通过更改`image_last_updated`来告诉Home Assistant一个新的图像.

> [!IMPORTANT]
> `ImageEntity` 的构造器默认需要 `hass` (和可选的 `verify_ssl` , `False` ) 。 它设置了用于`image_url`的HTTP客户端和访问符. 以自己的 `__init__` 呼叫 `super().__init__(hass)` 。

## 支持的特性 {#supported-features}

图像实体没有支持的特性 。

## 获取和缓存 {#fetching-and-caching}

Home Assistant每当有人问起图像,就打电话给`async_image`。 前端询问有实体加载的页面何时,每次状态变化时都会再次询问. 动作也要求。 当客户端在 `/api/image_proxy_stream/<entity_id>` 观看 MJPEG 流 时, Home Assistant 在每个状态变化上发送一个帧, 包括每5分钟一次的符号旋转, 至少每55秒一次. 你无法控制 `async_image` 运行时, 所以保持便宜。

这意味着命令很重要。 当新图像可用时(从协调器更新,按下消息,或计时器),您会更新`image_last_updated`并写入状态. 前端看到新状态并获取图像. 不要从 `async_image` 内侧突起 `image_last_updated` : 这将触发每次抓取的新抓取 。

当您使用 `image_url` 时, 下载的图像会在 `self._cached_image` 中缓存 。 设定为 `None` 当 URL 或 后面的图像 更改时, 所以下一次获取下载 。

一个图像实体的实体图片用短寿命的访问符指向`/api/image_proxy/<entity_id>`. {\fn黑体\fs22\bord1\shad0\3aHBE\4aH00\fscx67\fscy66\2cHFFFFFF\3cH808080}所以你用不着自己去处理 {\fn黑体\fs22\bord1\shad0\3aHBE\4aH00\fscx67\fscy66\2cHFFFFFF\3cH808080}所以你用不着自己去处理

## 方法 {#methods}

### 返回图像 {#return-the-image}

当返回字节而不是设置 `image_url` 时执行其中之一 。 当没有图像时返回 `None` 。

```python
class MyImage(ImageEntity):
    def image(self) -> bytes | None:
        """Return bytes of the image."""

    async def async_image(self) -> bytes | None:
        """Return bytes of the image."""
```

如果您从远程源获取图像, 请缓存它, 仅在 `image_last_updated` 更改后再次获取 。

## 状态 {#states}

状态为 `image_last_updated` 作为 ISO 8601 倍加码, 如 `2026-10-10T08:15:00+00:00`. 当`image_last_updated`是`None`时,状态是`unknown`. 您不能直接设置状态: 在基础类中是最终的 。

该实体也有一个`access_token`属性,该属性被排除在[录音机](/glossary/recorder)之外,就像`entity_picture`一样.

## 示例 {#example}

相遇的 突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突突切合实际:

```python
from homeassistant.components.image import ImageEntity
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.util import dt as dt_util

from .coordinator import MyCoordinator

class MyMapImage(CoordinatorEntity[MyCoordinator], ImageEntity):
    """The cleaning map of a vacuum."""

    _attr_has_entity_name = True
    _attr_translation_key = "map"
    _attr_content_type = "image/png"

    def __init__(
        self, hass: HomeAssistant, coordinator: MyCoordinator
    ) -> None:
        """Initialize the map image."""
        CoordinatorEntity.__init__(self, coordinator)
        ImageEntity.__init__(self, hass)
        self._attr_unique_id = f"{coordinator.serial}_map"
        self._attr_image_last_updated = dt_util.utcnow()

    @callback
    def _handle_coordinator_update(self) -> None:
        """Mark the image as changed, the frontend fetches it again."""
        self._attr_image_last_updated = dt_util.utcnow()
        super()._handle_coordinator_update()

    async def async_image(self) -> bytes | None:
        """Return the map as PNG bytes."""
        return self.coordinator.data.map_png
```
