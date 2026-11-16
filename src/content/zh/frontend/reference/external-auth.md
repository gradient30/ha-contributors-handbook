---
title: 外部认证
description: 嵌入前端的应用程序如何像同伴的应用程序一样,保持登录本身,并将访问符交给前端.
order: 3
---

# 外部认证 {#external-authentication}

通常前端处理自己的登录:它显示登录页,存储符,并刷新. 在网页视图中嵌入前端的应用程序,如[辅助应用程序](/companion),想要保留登录本身,当前端需要时只给它一个访问符. 这就是外部认证的目的。

## 打开它 {#turn-it-on}

在 URL 中以 `?external_auth=1` 装入前端 。 前端预计其中一座桥将在`window`上定义:

- `window.externalAppV2`:Android,推荐桥. 它需要一个支持[`WebViewFeature.WEB_MESSAGE_LISTENER`](https://developer.android.com/reference/androidx/webkit/WebViewCompat.WebMessageListener)的网页视图.
- `window.externalApp`:Android,没有这个功能的网页视图的倒置.
- `window.webkit.messageHandlers`: iOS和macOS.

当存在多个时,前端按此顺序使用. 没有它们,前端就无法启动.

## 获取访问符 {#get-an-access-token}

前端在加载时会要求一个符号,每当其符号过期时也会再次要求. 它发送一个带有召回名称的有效载荷,当它需要一个新的代号时,即使旧的代号还没有过期:

```js
// Android, V2
window.externalAppV2.postMessage(
  JSON.stringify({
    type: "getExternalAuth",
    payload: { callback: "externalAuthSetToken", force: true },
  })
);

// Android, V1
window.externalApp.getExternalAuth(
  JSON.stringify({ callback: "externalAuthSetToken", force: true })
);

// iOS and macOS
window.webkit.messageHandlers.getExternalAuth.postMessage({
  callback: "externalAuthSetToken",
  force: true,
});
```

在Android上,有效载荷是JSON弦,在iOS和macOS上是物体.

应用程序以是否成功回调来回答, 以保留有效的秒数回调:

```js
window.externalAuthSetToken(true, {
  access_token: "ABCDEFGH",
  expires_in: 1800,
});

// When the app can't get a token
window.externalAuthSetToken(false);
```

## 撤销标志 {#revoke-the-token}

当用户在配置文件中登录出时,前端会要求应用程序登录出. 应用程序必须用 Core 的 [认证 API](/core/internals/auth-api) 撤销其刷新令牌, 并登录用户 :

```js
// Android, V2
window.externalAppV2.postMessage(
  JSON.stringify({
    type: "revokeExternalAuth",
    payload: { callback: "externalAuthRevokeToken" },
  })
);

// Android, V1
window.externalApp.revokeExternalAuth(
  JSON.stringify({ callback: "externalAuthRevokeToken" })
);

// iOS and macOS
window.webkit.messageHandlers.revokeExternalAuth.postMessage({
  callback: "externalAuthRevokeToken",
});
```

完成后,该应用程序将召回:

```js
window.externalAuthRevokeToken(true);

// When the app could not log out
window.externalAuthRevokeToken(false);
```

## 回调名 {#the-callback-names}

召回名称 `externalAuthSetToken` 和 `externalAuthRevokeToken` 永远不变 。 应用软件应该检查一个请求中的回调是它所期望的,所以一个伪造的请求不能让它叫别的东西.

所有其它的应用程序和前端互相告诉对方的都经过[外部总线](/frontend/reference/external-bus).
