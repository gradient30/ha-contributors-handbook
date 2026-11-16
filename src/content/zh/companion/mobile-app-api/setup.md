---
title: 连接与注册
description: 查找 Home Assistant 实例, 用 OAuth 2 登录用户, 用 mobile app 集成 注册 。
order: 1
---



# 连接与注册 {#connect-and-register}
在应用程序可以发送任何东西之前,它需要找到实例,登录用户,并自己注册. 你每个服务器都做一次

## 寻找实例 {#find-the-instance}

Home Assistant以0conf在本地网络上宣布自己为`_home-assistant._tcp.local.`. 浏览此服务以向用户提供实例列表 。 如果找不到任何信息, 请查询 URL 。 关于服务宣布的内容,请参见[实例发现](/core/internals/instance-discovery)。

## 登录用户 {#log-the-user-in}

Home Assistant 客户端使用 [独立](https://indieauth.spec.indieweb.org/) 扩展的 OAuth 2 。 不存在客户端注册:客户端ID是您的应用程序网站的URL,重新定向的URI必须具有相同的方案,主机和端口.

本地应用程序需要像 `myapp://auth-callback` 这样的重定向 URI, 它位于不同的主机上 。 要允许,请在您的客户端ID的页面中添加链接标记 。 Home Assistant读该页的前10 kB:

```html
<link rel="redirect_uri" href="myapp://auth-callback">
```

该页面不是链接标记,也可以是OAuth客户端ID元数据文档:带有您的`client_id`和`redirect_uris`列表的JSON对象.

The flow:

1. 在浏览器中打开`/auth/authorize`,以`client_id`,`redirect_uri`为查询参数,可选用`state`作为查询参数.
2. 用户日志录入. Home Assistant 以 `code` 重定向到您的重定向 URI 。
3. 用 POST 到 `/auth/token` 交换令牌的代码, 格式编码为 `grant_type=authorization_code`, `code` 和相同的 `client_id` 。

你得到一个访问令牌,有效期为30分钟,还有一个刷新令牌来获得新的访问令牌. 请参看[认证](/core/internals/auth-api) 。

> [!NOTE]
> 官方应用程序使用固定的客户端ID,`https://home-assistant.io/iOS`和`https://home-assistant.io/android`,并带有`homeassistant://auth-callback`的重定向,以及两个Wear OS调用Android. Core允许那些不获取网站的人,因此登录也无法使用互联网. 使用自己的客户身份作为自己的应用程序.

## 确保装入移动 app {#make-sure-mobileapp-is-loaded}

`mobile_app`是`default_config`的一部分,所以它被装在大多数装置上. 如果用户删除 `default_config`, 他们需要在其 `configuration.yaml` 中添加 `mobile_app:` 并重新启动 。

要检查, 请用访问令牌拨打 `GET /api/config` , 在 `components` 中查找 `mobile_app` 。 如果注册返回一个404,则集成没有加载.

## 注册应用程序 {#register-the-app}

向 `/api/mobile_app/registrations` 发送认证的 POST :

```json
{
  "device_id": "ABCDEFGH",
  "app_id": "awesome_home",
  "app_name": "Awesome Home",
  "app_version": "1.2.0",
  "device_name": "Robbie's iPhone",
  "manufacturer": "Apple",
  "model": "iPhone X",
  "os_name": "iOS",
  "os_version": "17.4",
  "supports_encryption": true,
  "app_data": {
    "push_websocket_channel": true
  }
}
```

| 密钥 | 要求数 | 类型 | 说明 |
| --- | --- | --- | --- |
| `app_id` | 对 | 字符串 | 您的应用程序独有的标识符 |
| `app_name` | 对 | 字符串 | 您的应用程序名称 |
| `app_version` | 对 | 字符串 | 您的应用程序版本 |
| `device_name` | 对 | 字符串 | 装置名. 用于命名设备及其实体 |
| `manufacturer` | 对 | 字符串 | 设备制造商 |
| `model` | 对 | 字符串 | 设备的模型 |
| `os_name` | 对 | 字符串 | 操作系统的名称 |
| `os_version` | 不在确定,但发送 | 字符串 | 操作系统的版本. Home Assistant中的设备使用它作为其软件版本. 注册电话接受一个没有它的请求, 但设置注册失败, |
| `device_id` | 不在确定,但发送 | 字符串 | 一个稳定,独特的设备标识符. 没有它, Home Assistant 会产生随机的 |
| `supports_encryption` | No | 布尔 | app [加密](/companion/mobile-app-api/encryption) 是否其网页浏览流量 。 默认为 `false` |
| `app_data` | No | 对象 | 应用特定数据。 用于启用 [通知](/companion/mobile-app-api/notifications) |

合并 `app_id` 和 `device_id` 确定注册 。 重新 对同一对进行注册取代了旧的注册:你得到一个新的webhook ID和秘密,旧的则停止工作. 没有`device_id`,每个注册都是新的。

以 `201 Created` 回答 。 永久存储响应, 这是你唯一得到它的时间:

```json
{
  "cloudhook_url": "https://hooks.nabu.casa/randomlongstring123",
  "remote_ui_url": "https://randomlongstring123.ui.nabu.casa",
  "secret": "qwerty",
  "webhook_id": "abcdefgh"
}
```

| 密钥 | 说明 |
| --- | --- |
| `webhook_id` | 网路标记为[发送数据](/companion/mobile-app-api/sending-data) 到 |
| `secret` | 加密的密钥 。 只在您发送 `supports_encryption` 时设置 。 |
| `cloudhook_url` | 通过 Home Assistant Link 的 Webhook URL 。 仅在实例有活动订阅并连接到云中时设定,且用户不只本地 |
| `remote_ui_url` | 通过 Home Assistant Link 实现实例的远程 URL 。 同样的条件,除了云连接 |

不适用的值为 `null` 。

注册后, Home Assistant 拥有用于您的应用程序的新设备, 并设有设备跟踪器 。  追踪器被添加到注册的用户身上  传感器以您 [登记他们](/companion/mobile-app-api/sensors) 出现 。
