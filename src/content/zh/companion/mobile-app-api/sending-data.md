---
title: 发送数据
description: 移动 app网络hook. 要使用的URL, 请求的格式, 回复, 以及每个被webhook接受的请求类型 。
order: 2
---



# 发送数据 {#send-data}
在 [登记](/companion/mobile-app-api/setup) 之后, 所有应用程序发送到一个 Webhook 。 它不需要一个访问符: webhook ID是证书. 把它当成密码

## 要使用的 URL {#which-url-to-use}

从 Webhook ID 中构建 Webhook URL: `<instance_url>/api/webhook/<webhook_id>`. 然后按此顺序尝试您拥有的 URL, 当请求失败时移动到下一个 :

1. `cloudhook_url`,如果注册给你一个。
2. 拱门,如果注册给了你一个`remote_ui_url`。
3. `<instance_url>/api/webhook/<webhook_id>`,用户设置了URL.

双 Home Assistant Link URL 都可以随着用户订阅的变化而来去. [`get_config`](/companion/mobile-app-api/sending-data#get_config) 响应有当前的响应 。

### 家园与远离 {#home-and-away}

一些路由器无法通过其外部地址(没有NAT回转,或发夹)在本地网络上到达一个设备. 如果用户通过动态 DNS 名称到达 Home Assistant, 家庭内部的请求失败 。 让用户告诉Wi-Fi网络是何家的应用程序,并使用该软件的内部URL.

## 发送到 WebSocket API 密码 {#sending-over-the-websocket-api}

当应用程序已经有一个 [WebSocket](/core/internals/websocket-api) 连接时, 它可以发送webhook 请求, 上面有 `webhook/handle` 命令 :

```json
{
  "id": 5,
  "type": "webhook/handle",
  "webhook_id": "abcdefgh",
  "method": "POST",
  "body": "{\"type\": \"get_zones\"}",
  "headers": {
    "Content-Type": "application/json"
  }
}
```

`method`是`GET`、`HEAD`、`POST`或`PUT`之一。 `body`和`query`是可选字符串,而鱿鱼是带有字符串值的可选对象。 结果包含响应的`body`,`status`和`headers`:

```json
{
  "id": 5,
  "type": "result",
  "success": true,
  "result": {
    "body": "[]",
    "status": 200,
    "headers": {
      "Content-Type": "application/json"
    }
  }
}
```

## 社区的 {#the-request}

每个请求都是HTTP POST(PUT也与JSON机构合作):

```json
{
  "type": "<type of request>",
  "data": {}
}
```

有些类型没有 `data` 。 如果注册已启用加密, 每个请求都必须加密, 见 [加密](/companion/mobile-app-api/encryption) 。

## 回应 {#the-response}

| 状态 | 含义 |
| --- | --- |
| `200` | 处理。 同样返回,带有空的`{}`,当有效载荷与该类型的计划不匹配时,加密的有效载荷无法解密,或者该类型不明. Home Assistant记录细节 |
| `201` | 登记了一个传感器 |
| `400` | 主体无效 JSON, 加密启用时请求没有加密, `enable_encryption` 是在加密已经启动时发送的, 或者`stream_camera` 得到了未知的相机 。 |
| `404` | Webhook 端点不在那里, 因为 `webhook` 集成没有加载 |
| `405` | 请求使用了 `GET` 。 网络标记只接受 `POST` 和 `PUT` |
| `410` | 登记被删除。 告诉用户,再登记一次 在Home Assistant删除后重新启动之前, webhook 回答像一个未知的答案,使用空的`200` |

请求使用一个 Home Assistant 并不知道得到空的 `200` 的 Webhook ID, 也是当 `mobile_app` 本身没有被装入时 。 这样,API就不会透露究竟存在哪些网友.

身体的错误是这样的:

```json
{
  "success": false,
  "error": {
    "code": "encryption_required",
    "message": "Encryption required"
  }
}
```

如果注册使用加密,内容的回复也被加密. 这些不是:空 người`{}`的响应,对`enable_encryption`的响应,以及上面格式的两个错误,`encryption_required`和`encryption_already_enabled`. 请求类型因其结果而返回的加密与其它响应一样出错 。 例如,`stream_camera`用加密的`{"success": false}`和`400`来回答一个未知的相机. 所以不要按状态代码进行:检查机身是否设置了`encrypted`.

## 请求类型 {#request-types}

### `update_location` {#updatelocation}

更新应用程序的设备跟踪器。

```json
{
  "type": "update_location",
  "data": {
    "gps": [12.34, 56.78],
    "gps_accuracy": 120,
    "battery": 45
  }
}
```

| 密钥 | 类型 | 说明 |
| --- | --- | --- |
| `gps` | 列表 | 谁知经纬.  谁要求 `gps_accuracy` |
| `gps_accuracy` | 编号 | 位置精确度以米计. 零或以上 |
| `location_name` | 字符串 | 设备所在区域的名称 |
| `in_zones` | 列表 | 设备所在区域的实体ID |
| `battery` | 整数 | 电池电位百分比 零或以上 |
| `speed` | 整数 | 速度以米每秒计. 零或以上 |
| `altitude` | 编号 | 高度以米计 |
| `course` | 整数 | 旅行方向为学位,相对于应北。 零或以上 |
| `vertical_accuracy` | 整数 | 高度精确度以米计. 零或以上 |

所有密钥都是可选的 。 当发送`in_zones`,Home Assistant忽略`location_name`。

### `register_sensor` 和 `update_sensor_states` (韩语) {#registersensor-and-updatesensorstates}

建议将传感器注册,并更新一个或多个传感器。建议将 [传感器](/companion/mobile-app-api/sensors) 。

### `call_service` {#callservice}

在 Home Assistant 中执行享有同等的 [动作](/glossary/action) 。 类型和密钥仍然使用旧名享有同等服务.

```json
{
  "type": "call_service",
  "data": {
    "domain": "light",
    "service": "turn_on",
    "service_data": {
      "entity_id": "light.kitchen"
    }
  }
}
```

| 密钥 | 类型 | 说明 |
| --- | --- | --- |
| `domain` | 字符串 | 我们会发现, |
| `service` | 字符串 | 动作名称 |
| `service_data` | 对象 | 动作的数据。 可选 |

动作作为注册该应用程序的用户运行. 如果它失败, Home Assistant 记录错误, 而反应是 `200` 没有身体 。

### `fire_event` {#fireevent}

开一活动.

```json
{
  "type": "fire_event",
  "data": {
    "event_type": "my_custom_event",
    "event_data": {
      "something": 50
    }
  }
}
```

| 密钥 | 类型 | 说明 |
| --- | --- | --- |
| `event_type` | 字符串 | 事件的类型 |
| `event_data` | 对象 | 事发地的數據 B. 任 务 |

### `render_template` {#rendertemplate}

在一个请求中创建一个或多个模板。 `data` 中的每个密钥都是您自己命名的模板 :

```json
{
  "type": "render_template",
  "data": {
    "greeting": {
      "template": "Hello {{ name }}, you are {{ states('person.paulus') }}.",
      "variables": {
        "name": "Paulus"
      }
    }
  }
}
```

| 密钥 | 类型 | 说明 |
| --- | --- | --- |
| `template` | 字符串 | 要渲染的模板 |
| `variables` | 对象 | 模板的额外变量 。 可选 |

响应使用相同的密钥: `{"greeting": "Hello Paulus, you are home."}`. 无法返回 `{"error": "<message>"}` 的模板在其密钥下, 其他模板仍然渲染 。

### `update_registration` {#updateregistration}

更新注册, 例如在应用程序更新后, 或在按键更改时 。

```json
{
  "type": "update_registration",
  "data": {
    "app_data": {
      "push_token": "abcd",
      "push_url": "https://push.example.com/push"
    },
    "app_version": "2.0.0",
    "device_name": "Robbie's iPhone",
    "manufacturer": "Apple",
    "model": "iPhone XR",
    "os_version": "17.4"
  }
}
```

| 密钥 | 要求数 | 类型 | 说明 |
| --- | --- | --- | --- |
| `app_version` | 对 | 字符串 | 应用程序的版本 |
| `device_name` | 对 | 字符串 | 嗯 设备的名称 |
| `manufacturer` | 对 | 字符串 | 设备制造商 |
| `model` | 对 | 字符串 | 设备的模型 |
| `os_version` | No | 字符串 | 操作系统的版本 |
| `app_data` | No | 对象 | 替换应用程序数据, 例如启用 [通知](/companion/mobile-app-api/notifications) |

回应是更新注册,没有秘密值.

### `get_config` {#getconfig}

返回用于配置应用程序的信息 。

```json
{
  "type": "get_config"
}
```

该响应有实例的`latitude`,`longitude`,`elevation`,`unit_system`,`location_name`,`time_zone`,`components`,`version`和`theme_color`,加上:

| 密钥 | 说明 |
| --- | --- |
| `hass_device_id` | 设备注册中应用的设备的ID |
| `instance_id` | 案件独有的ID |
| `cloudhook_url`, `remote_ui_url` | 当前 Home Assistant Link URL, 当实例有活动订阅, 而用户不只为本地 |
| `entities` | 以您注册的唯一 ID 键入的注册实体的启用状态, 请参见 [保持传感器同步](/companion/mobile-app-api/sensors#keep-the-enabled-state-in-sync) |

### `get_zones` {#getzones}

返回所有区域的状况,按实体ID排序。

```json
{
  "type": "get_zones"
}
```

### `enable_encryption` {#enableencryption}

打开已有注册的加密 。 见[加密](/companion/mobile-app-api/encryption#enable-it-later).

### `stream_camera` {#streamcamera}

没事的 返回相机流的路径 。

```json
{
  "type": "stream_camera",
  "data": {
    "camera_entity_id": "camera.front_door"
  }
}
```

```json
{
  "mjpeg_path": "/api/camera_proxy_stream/camera.front_door",
  "hls_path": "/api/hls/<token>/master_playlist.m3u8"
}
```

没关系 `hls_path` 是 `null` 当相机不能流时 。 将路径与您用于实例的 URL 合并 。 一个未知的相机以 `400` 返回 `{"success": false}` 。 如果注册使用加密,那尸体也是加密的.

### `conversation_process` {#conversationprocess}

发送到 [Assist](/glossary/assist) 的句子, 并返回对话代理的回应 。

```json
{
  "type": "conversation_process",
  "data": {
    "text": "Turn on the lights",
    "language": "en",
    "conversation_id": "ABCD"
  }
}
```

只要求 `text` 。 响应的格式与[对话框 API](/core/internals/conversation-api)相同.

### `scan_tag` {#scantag}

报告该设备扫描了NFC标记或QR代码. Home Assistant 启动标记扫描事件, 以应用程序的设备作为扫描仪 。

```json
{
  "type": "scan_tag",
  "data": {
    "tag_id": "5f0ba733-172f-430d-a7f8-e4ad940c88d7"
  }
}
```

### `live_activity_token` 和 `live_activity_dismissed` (韩语) {#liveactivitytoken-and-liveactivitydismissed}

由iOS应用程序用于现场直播活动. 见[通知](/companion/mobile-app-api/notifications#live-activities).
