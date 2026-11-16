---
title: 认证 API
description: 往往是使用 OAuth 2 的 Home Assistant 例, 应用程序是如何登录到 Home Assistant 的 。
sidebarGroup: 4.a(a)的合格后得到过合格后后得到过合格后后得到过过合格后后后得到过过过过过过等等等等等等等等等等等的合格后后才能得到过合格的合格后后后后才能得到过。等等等等等等等等合格后后才能得到合格后后后才能得到合格后后后才能得到过。等等等等等等等等等等等等等等等等等等等等等等等等等等等等等等等等、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、等等、、、、、、、、、、、、、、、、、、、、、、、、、、、、
order: 22
---

# 认证 API {#authentication-api}

每个 Home Assistant 实例属于某人, 因此没有中心注册应用程序 。 相反,Home Assistant使用 {L耿} 与 [独立](https://indieauth.spec.indieweb.org/) 处理客户端的方法 : 您的应用程序由自己的网站识别 。 此页面会通过您的应用程序的流程来获取用户实例的标志 。

如果您写入 JavaScript, [Home Assistant-js-websocket](https://github.com/home-assistant/home-assistant-js-websocket) 库为您执行此流程 。 前端也使用过.

## 您的客户身份 {#your-client-id}

您的客户端ID 是您的应用程序网站的 URL, 如 `https://www.my-application.io/` 。 您发送用户返回的重定向 URI 必须拥有相同的主机和端口, 如 `https://www.my-application.io/auth_callback` 。

需要在另一个主机上重定向 URI, 例如本地应用程序的自定义方案 ? 在您的网站上声明, 而Home Assistant 在您的客户端 ID 中获取页面以找到它 。 它读了前10 KB, 并接受其中之一:

- HTML 中的链接标记 :

```html
  <link rel="redirect_uri" href="hass://auth" />
  ```

- JSON劳力 [OAuth 客户端识别元数据文档](https://datatracker.ietf.org/doc/draft-ietf-oauth-client-id-metadata-document/) 在客户端 ID URL 服务, 包含 `redirect_uris` 列表 :

```json
  {
    "client_id": "https://www.my-application.io/oauth/metadata.json",
    "redirect_uris": ["https://oauth.my-application.io/hass/auth_callback"]
  }
  ```

Home Assistant 只在页面没有链接标记时读取元数据文档 。 它只在客户端ID是 `https` 时才接受此文档 带路径的 URL, 响应是否会举例为年世界 你这个 如果是 真的吗 该死 `200 OK` (没有重定向) , 文档中的 `client_id` 完全就是它从中获取的 URL, 而 `redirect_uris` 中的每个条目都是绝对的 URI 。

Home Assistant 描述它支持的 `/.well-known/oauth-authorization-server`, 如 [RFC 8414 (韩语).](https://datatracker.ietf.org/doc/html/rfc8414) 中定义的 。 发现端点的客户可以从那里开始。

## 步骤1:发送用户授权 {#step-1-send-the-user-to-authorize}

的会员国 :

```text
https://homeassistant.local:8123/auth/authorize
  ?client_id=https%3A%2F%2Fwww.my-application.io%2F
  &redirect_uri=https%3A%2F%2Fwww.my-application.io%2Fauth_callback
  &state=abc123
```

该行间断仅供阅读. 可选参数 :

- `state` : 返回方向不变 。 用户正在登录的实例的 URL 的好位置 。
- `code_challenge`和`code_challenge_method`:为PKCE ([RFC 7636 (英语).](https://datatracker.ietf.org/doc/html/rfc7636)). 唯一支持的方法是 `S256` 。 随时使用 PKCE, 并总是在本地应用程序中使用 。

用户登录并批准。 Home Assistant 然后用 `code` 和 `state` 重定向到您的重定向 URI :

```text
https://www.my-application.io/auth_callback?code=12345&state=abc123
```

## 步骤2: 将代码交换为令牌 {#step-2-exchange-the-code-for-tokens}

POST to `/auth/token`,车身编码为`application/x-www-form-urlencoded`. 使用与步骤1完全相同的 `client_id` :

```text
grant_type=authorization_code
&code=12345
&client_id=https%3A%2F%2Fwww.my-application.io%2F
```

加上 PKCE, 加上`code_verifier` 。 答复:

```json
{
  "access_token": "ABCDEFGH",
  "expires_in": 1800,
  "refresh_token": "IJKLMNOPQRST",
  "token_type": "Bearer",
  "ha_auth_provider": "homeassistant"
}
```

访问令牌为 `expires_in` 秒有效 。 安全存储刷新令牌:这是保持用户登录的原因 。

在错误的请求下,您会得到像 `{"error": "invalid_request", "error_description": "Invalid code"}` 这样的状态 400 。 如果用户不能登录,例如由于用户不活动,则您会得到错误`access_denied`的状态403。

## 实情如下: {#step-3-refresh-the-access-token}

当访问令牌崽子闺蜜过期时, POST 重回 `/auth/token` :

```text
grant_type=refresh_token
&refresh_token=IJKLMNOPQRST
&client_id=https%3A%2F%2Fwww.my-application.io%2F
```

您得到了一个新的 `access_token` 和它的 `expires_in` 。 如果刷新令牌不再有效, 用户会被登录: 清除您存储的内容并重新开始流量 。

刷新令牌在90天未使用时过期 。

## 撤销一个符号 {#revoke-a-token}

要登录, POST 更新到 `/auth/revoke` 的令牌, 日举行 旷代 { 我是 `application/x-www-form-urlencoded` :

```text
token=IJKLMNOPQRST
```

这撤销了刷新符和它创造的每一个访问符. 反应总是以空体状态200,无论是否符号存在. 旧的表单,张贴`token`和`action=revoke`到`/auth/token`,仍然有效,但已贬值。

## 提出经认证的请求 {#make-authenticated-requests}

对于 HTTP,请在 `Authorization` 标题中发送访问符 :

```shell
curl \
  -H "Authorization: Bearer ABCDEFGH" \
  https://homeassistant.local:8123/api/
```

对于WebSocketAPI,请在[认证消息](/core/internals/websocket-api#authentication)中发送. 超过 HTTP,过期或无效的令牌获得状态 401. 在 {抨击} API 上, 您可以得到 `auth_invalid` 而服务器会关闭连接 。 无论哪种方式:刷新符号,再试一次.

## 长寿命访问符 {#long-lived-access-tokens}

对于无法通过登录流的脚本和服务,用户可以在**Security**下在其配置中创建长寿的访问符. 有效期为10年,使用方式与进入标志完全相同。

使用 WebSocket 连接的应用程序也可以为当前使用 `auth/long_lived_access_token` 的用户创建 。 `lifespan`的天数为:

```json
{
  "id": 11,
  "type": "auth/long_lived_access_token",
  "client_name": "GPS Logger",
  "lifespan": 365
}
```

结果就是象征 Home Assistant 不存储它, 所以无法再次显示 。

## 已签名路径 {#signed-paths}

有时用户需要打开一个没有`Authorization`头的URL,就像一个下载链接. 签名路径是普通路径, 并添加了签名, 如 `/api/states?authSig=ABCDEFGH` 。 打开它的人 被授权作为创造它的新标志

在 WebSocket API 上, 用 `auth/sign_path` 创建 。 `expires` 以秒计, 默认为 30 :

```json
{
  "id": 12,
  "type": "auth/sign_path",
  "path": "/api/states",
  "expires": 20
}
```

结果是 `path` 要使用 。 在集成中,使用`async_sign_path`从`homeassistant.components.http.auth`开始. 它使用当前HTTP请求的刷新令牌或WebSocket连接,当没有时会回到一个特殊的内容用户身上,比如在自动化中.

铭记:

- 当其刷新令牌被删除,当用户被删除,当Home Assistant重新启动时,一个已签名的路径停止工作.
- 请求到达时会检查签名 。 下载时间比到期时间还要长 。
