---
title: 相机实体
description: 从相机中显示静态图像,并可以选择在HLS或WebRTC上显示一个直播流.
sidebarLabel: 有悖于
sidebarGroup: 媒体
---

# 相机实体 {#camera-entity}

相机实体服务于相机的图像:按请求提供静态图像,如果相机可以,则提供现场视频流. 将摄像柠檬的摄像头植入于仪表板上,

从`Camera`继承,从`homeassistant.components.camera`导入。 用于显示现场或接近现场画面的任何东西. 如果您的设备只有一个静态图像时而变化, 如地图或QR 代码, [图像实体](/core/entities/image) 更简单 。

## 的临时议程 {#properties}

这些属性是相机实体特有的. 每个实体在 [实体类别](/core/entities/entity-class) 广泛宣传属性 。

| 名称 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- |
| `brand` | `str \| None` | `None` | 摄影机的品牌. |
| `camera_entity_capabilities` | `CameraEntityCapabilities` | `CameraEntityCapabilities()` | 摄像头支持什么? 见[双向音频](/core/entities/camera#two-way-audio). |
| `model` | `str \| None` | `None` | 摄影机的模型. |
| `frame_interval` | `float` | `0.5` | Home Assistant 从静态图像中构建的 MJPEG 流的帧之间的秒数 。 |
| `is_on` | `bool` | `True` | 摄像头开不开? 关闭时, 图像请求会以"服务不可用"的响应失败 。 |
| `is_recording` | `bool` | `False` | 相机是否正在录制 。 设州. |
| `is_streaming` | `bool` | `False` | 相机是否在流淌 。 设州. |
| `motion_detection_enabled` | `bool` | `False` | 运动探测是否在进行. |
| `use_stream_for_stills` | `bool` | `False` | 从流中取静态图像, 而不是调用 `async_camera_image` 。 只有财产:没有`_attr_`。 |
| `content_type` | `str` | `"image/jpeg"` | 您返回图像的 MIME 类型 。 `__init__` 中设置的纯实例属性, 不是属性 。 |
| `stream_options` | `dict` | `{}` | 当流集成打开您的流源时, 选项传递到流集成 。 一个简单的例子属性。 |

相机默认不进行民调(`should_poll`是`False`). 当您覆盖 `__init__` 时, 请拨打 `super().__init__()` : 它设置访问符、 流和 WebRTC 簿记 。

## 支持的特性 {#supported-features}

将 `CameraEntityFeature` 的旗帜与位符或 (`|`) 运算符合并 。

| 旗帜 | 说明 |
| --- | --- |
| `ON_OFF` | 相之后才能开关. 执行之后才执行 `turn_on` 和 `turn_off` 。 |
| `STREAM` | 相机有直播流. 嚷嚷 HLS 执行 `stream_source` 或本地的 WebRTC 方法 。 |

## 还是图像 {#still-images}

每个相机通过`async_camera_image`(或`camera_image`)返回静态图像. 前端称它为缩略图和仪表板,而`camera.snapshot`动作将其结果保存为磁盘.

前端可以请求 `width` 和 `height` 。 扩大是最佳努力:

- 如果你的相机可以缩放, 传递大小并返回最小的图像, 至少是那么大。
- 保持宽度比。 当它不匹配时,返回的图像可以比要求的要宽或高.
- 如果您无法缩放并返回 JPEG, Home Assistant 为您缩放 。

如果相机有流且没有单独的快照端点,则设定 `use_stream_for_stills` 到 `True`, Home Assistant 从流中抓取静态 。 另一个常见的方法是将流源传递到FFmpeg集成(`homeassistant.components.ffmpeg`)的`async_get_image`,它从中抓取一个帧.

## 流线 {#streams}

使用 `CameraEntityFeature.STREAM` 的相机以两种方式之一提供实时流 。 前端根据相机提供的内容来选择玩家.

### HLS 通过流集成 {#hls-through-the-stream-integration}

执行`stream_source`并返回一个FFmpeg可以打开的URL,通常是RTSP URL. Home Assistant的溪流集成将它变为前端的HLS,并且也用于`camera.record`和`camera.play_stream`.

当另一个集成已经注册了一个能够处理您的流源的WebRTC供应商,比如go2rtc集成时,前端也会为您的相机获得WebRTC. 你不必为此做任何事情。

### 原生的 WebRTC 网络 {#native-webrtc}

如果您的相机或云本身会讲WebRTC,请执行这些方法:

- `async_handle_async_webrtc_offer(offer_sdp, session_id, send_message)`:为前端的 SDP 提议启动会话 。 以 `send_message` 回调 `WebRTCAnswer` 、 `WebRTCCandidate` 和 `WebRTCError` 发送答案、 候选人和错误。
- `async_on_webrtc_candidate(session_id, candidate)`:处理前端在发价后发送的ICE候选人. 执行报价方法时需要。
- `close_webrtc_session(session_id)`:可选. 前端关闭溪流时进行清理.

一旦您覆盖 `async_handle_async_webrtc_offer`, 前端只使用 WebRTC , 并且永远不会返回到 HLS 。 原生的WebRTC流不会通过流集成,因此无法录制. 要将额外设置传递给 WebRTC 客户端, 就像一个数据通道, 覆盖 `_async_get_webrtc_client_configuration` 并返回 `WebRTCClientConfiguration` 。

### WebRTC 供应商 {#webrtc-providers}

一个集成还可以提供WebRTC,用于基于其流源的其他集成的相机. 执行 `CameraWebRTCProvider` 用 `async_register_webrtc_provider(hass, provider)` 注册它 。 提供商告诉 Home Assistant 它用 `async_is_supported` 支持哪些流源, 并处理这些相机的报价和候选人 。 Go2rtc就是这样工作的,你很少需要它。

### 双向音频 {#two-way-audio}

当摄像头有扬声器时,人们可以在观看直播流时通过它说话. 要提供此选项, 请设置 `camera_entity_capabilities` 到 `CameraEntityCapabilities` , 以 `two_way_audio` 为 `True`, 从 `homeassistant.components.camera` 导入 。

只有在相机能通过流 Home Assistant 使用接收音频时才声明 。

```python
self._attr_camera_entity_capabilities = CameraEntityCapabilities(
    two_way_audio=device.supports_two_way_audio and device.protocol == "rtsp"
)
```

前端只有在这些都持有时才能获得双向音频:

- 您的实体宣布双向音频。
- 或通过WebRTC提供商在WebRTC上的相机流. 双向音频无法通过HLS获取.
- 用户在[实验室](/core/development/labs)中打开了相机集成的**双向音频**预览功能. 浏览器只允许通过HTTPS访问麦克风,因此双向音频需要Home Assistant在HTTPS上打开.

## 方法 {#methods}

每种方法都有同步和Aync变体. 执行其中一项。

| 就在那时 | 同步变体 | 说明 |
| --- | --- | --- |
| `async_camera_image(width=None, height=None)` | `camera_image` | 返回静态图像的字节, 或 `None` 。 |
| `stream_source()` | 无 | 仅限Async. 返回流 URL, 或 `None` 。 需要`STREAM`吗? |
| `async_turn_on()` | `turn_on` | 打开摄像机。 需要 `ON_OFF` 。 |
| `async_turn_off()` | `turn_off` | 关掉摄像机 需要 `ON_OFF` 。 |
| `async_enable_motion_detection()` | `enable_motion_detection` | 开动探测器 |
| `async_disable_motion_detection()` | `disable_motion_detection` | 才可以把探测器关掉 |
| `handle_async_mjpeg_stream(request)` | 无 | 可选的 直接从相机中代理一个MJPEG流. 默认情况下, Home Assistant 每 `frame_interval` 秒从静态图像中构建一个 。 |

本地WebRTC方法列表于[原生的 WebRTC 网络](/core/entities/camera#native-webrtc).

## 状态 {#states}

状态为最终状态,来自`is_recording`和`is_streaming`,依此顺序排列. 值在 `CameraState` enum 中 。

| 状态 | 何时 |
| --- | --- |
| `recording` | `is_recording` is `True`. |
| `streaming` | `is_streaming`是`True`,摄像机没有录音。 |
| `idle` | 也没有 |

相机增加了`access_token`,设定时将`model_name`,`brand`和`motion_detection`作为属性. 访问令牌和实体图片被排除在[录音机](/glossary/recorder)之外,因为令牌每5分钟旋转一次.

## 示例 {#example}

有RTSP流和快照URL的网络相机.

```python
from homeassistant.components.camera import Camera, CameraEntityFeature

class MyCamera(Camera):
    """A network camera."""

    _attr_has_entity_name = True
    _attr_name = None
    _attr_supported_features = CameraEntityFeature.STREAM

    def __init__(self, device: MyDevice) -> None:
        """Initialize the camera."""
        super().__init__()
        self._device = device
        self._attr_unique_id = device.serial
        self._attr_brand = "Example"
        self._attr_model = device.model

    async def async_camera_image(
        self, width: int | None = None, height: int | None = None
    ) -> bytes | None:
        """Return a snapshot."""
        return await self._device.snapshot(width=width, height=height)

    async def stream_source(self) -> str | None:
        """Return the RTSP URL of the main stream."""
        return self._device.rtsp_url
```
