---
title: 通知
description: Mobile app如何向一个app发送通知,通过WebSocket连接或通过一个推力服务器,而合同中一个推力服务器必须遵循.
order: 5
source: https://github.com/home-assistant/mobile-apps-fcm-push/blob/main/functions/handlers.js
lastVerified: 2026-10-14
---



# 通知 {#notifications}
最后一次验证是在2026-10-14,对https://github.com/home-assistant/mobile-apps-fcm-push/blob/main/functions/handlers.js.

`mobile_app` 通知已建入 。 一旦一个应用程序允许它们, Home Assistant 得到一个通知实体和一个`notify.mobile_app_<device_name>` 动作, 用户可以从自动化发送通知 。

发出通知有两种方式:

- **通过WebSocket连接**(局部推),而应用是连接的. 不需要服务器,但应用程序必须保持连接畅通.
- **通过推推服务器**(云推). Home Assistant 将通知发布到您运行的 URL, 您的服务器把它交给 Apple, Google, 或者另一个按键服务 。

应用程序可以支持两者。 当它打开时, Home Assistant 在打开时使用 WebSocket 频道, 当没有打开时, 或当应用程序没有及时确认通知时, 则使用 WebSocket 服务器 。

用户向官方应用程序发送通知的方式在[通知文件](https://companion.home-assistant.io/docs/notifications/notifications-basic)中.

## 过WebSocket {#over-the-websocket}

要启用它, 请在 `app_data` 、 [登记](/companion/mobile-app-api/setup#register-the-app) 或 [`update_registration`](/companion/mobile-app-api/sending-data#update_registration) 中设置 `push_websocket_channel` 到 `true` 。

然后在认证的 [WebSocket](/core/internals/websocket-api) 连接上打开一个频道 :

```json
{
  "id": 2,
  "type": "mobile_app/push_notification_channel",
  "webhook_id": "abcdefgh",
  "support_confirm": true
}
```

Webhook ID必须属于连接用户. 为同一 Webhook 打开新频道 关闭旧频道 。

通知是作为订阅活动发出的:

```json
{
  "id": 2,
  "type": "event",
  "event": {
    "message": "Hello world",
    "title": "Hi",
    "hass_confirm_id": "6d8c3e2a1f4b4f0b9c0d5e7a8b9c0d1e"
  }
}
```

用 `support_confirm` 好,每份通知都有 `hass_confirm_id`,你有10 秒来确认它:

```json
{
  "id": 3,
  "type": "mobile_app/push_notification_confirm",
  "webhook_id": "abcdefgh",
  "confirm_id": "6d8c3e2a1f4b4f0b9c0d5e7a8b9c0d1e"
}
```

如果确认没有及时到来,Home Assistant关闭频道并发送通知,以及任何其他未经证实的通知,代之以通过推器服务器. 没有push服务器,一个没有连接的应用程序就得不到通知,动作失败时会出现设备没有连接的错误.

## 通过一个推器服务器 {#through-a-push-server}

要启用它, 请在 `app_data` 中设置两个密钥 :

| 密钥 | 说明 |
| --- | --- |
| `push_token` | 设备的推码, 如 APNs 或 FCM 注册码 |
| `push_url` | URL Home Assistant 发布通知到 |

`mobile_app`不关心通知是如何到达设备的. 寄到你的服务器上 剩下的就交给你了 这让你完全控制了你的俯卧撑 官方应用程序使用[项目的推力服务](https://github.com/home-assistant/mobile-apps-fcm-push),通过Firebase Cloud Messaging向Android和iOS两个设备发送通知. 它的代码是你们自己的良好起点.

### 社区的 {#the-request}

Home Assistant送一个带JSON身体的POST,10秒后放弃:

```json
{
  "message": "Hello World",
  "title": "Test message",
  "push_token": "my-secure-token",
  "registration_info": {
    "app_id": "io.robbie.HomeAssistant",
    "app_version": "2026.10.0",
    "os_version": "26.0",
    "webhook_id": "abcdefgh"
  },
  "data": {
    "key": "value"
  }
}
```

`title` 和`data` 只有在用户设置时才存在 。 `data` 持有用户通过的其他所有文件, 并且是应用特定选项的位置 。

### 回应 {#the-response}

在通知被接受时以 `200`, `201` 或 `202` 回复 。 总是发送带有 `application/json` 内容类型的 JSON 机构, 即使没有报告, 如 `{}` 。 Home Assistant将每个响应读作JSON,无法读取的响应失败像一个错误一样,无论状态如何.

在其它状态上, 通知失败为错误 `Error sending notification to <device>` 。 A `429` 给 `Rate limit exceeded sending notification to <device>` 相反, 一个需要10秒以上的请求给 `Timeout sending notification to <device>` 。 通知实体提出这些错误,所以其行动失败. `notify.mobile_app_<device_name>` 动作只记录它们, 作为速度限制的警告和错误, 动作本身成功 。 你的JSON反应可以解释出了什么问题 Home Assistant 在调试级别记录解释 :

| 密钥 | 说明 |
| --- | --- |
| `message` | 已登录, 并注明消息来自 {H在内} |
| `errorMessage` | 添加到标准消息中 : “ 内部服务器错误, 请稍后再试 :... ” |

尽可能具体,告诉用户知道后如何解决问题.

### 费率限制 {#rate-limits}

推动服务费钱,一个破碎的自动化可以发送上千个通知. 使用率限. 官方app的推推服务默认允许每个设备每天有500个通知,在协调世界时午夜重新计数.

Home Assistant不限制任何东西本身。 您的服务器有, 并且告诉 Home Assistant 。 在您的回复中添加 `rateLimits` :

```json
{
  "rateLimits": {
    "successful": 1,
    "errors": 5,
    "maximum": 500,
    "resetsAt": "2026-10-11T00:00:00.000Z"
  }
}
```

| 密钥 | 类型 | 说明 |
| --- | --- | --- |
| `successful` | 整数 | 这一期间发出的通知 |
| `errors` | 整数 | 在此期间失败的通知 |
| `maximum` | 整数 | 每个期间的上限 |
| `resetsAt` | 时间戳 | 当周期结束时,在协调世界时ISO 8601中 |

Home Assistant 在调试级别上记录这些数字, 保留到重置的时间 。 当用户点击极限时,用 `429` 回复直到结束, 并尽早拒绝 。 Home Assistant 记录到一个警告, 已经达到极限 。

## 现场活动 {#live-activities}

iOS应用显示Live Activity,如定时器或锁定屏幕上的交付,通知可以启动,更新,结束. 每个活动都有自己的推力符, 和`mobile_app`跟踪它们。 这仅适用于通过推器服务器的通知,用于以`Apple`作为`manufacturer`的注册:

- 在注册时,或后来与 `update_registration` 一起,该应用程序将 `start_live_activity_token` 置入 `app_data` , 用于启动新的 Live 活动 。
- 当一个 Live 活动在设备上启动时,应用程序会以 `live_activity_token` webhook 请求发送其更新令牌: 活动的 `tag`, `push_token` 和 `expires_at` 作为 Unix 时间戳 。
- 当用户在设备上将其解析老头时,应用程序会随`tag`发送`live_activity_dismissed`.

当一个通知在它的`data`中有`tag`和`live_update: true`时,Home Assistant在对推器服务器的请求中增加了`live_activity_token`,以及`start`,`update`或`end`到`data`的`event`。 使用同一标记的 `clear_notification` 消息结束活动 。 过期的令牌会被自动删除.

对于用户,此描述见[一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一,一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一](https://companion.home-assistant.io/docs/notifications/live-activities).
