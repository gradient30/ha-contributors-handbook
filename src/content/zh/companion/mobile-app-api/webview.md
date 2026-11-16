---
title: WebView
description: 在应用程序内显示 Home Assistant 前端, 不要求用户第二次登录 。
order: 6
---



# WebView {#web-view}
用户在设置您的应用程序时已经登录了 。 他们不该再登录看仪表板了 前端支持:当它运行在应用程序内部时,它可以向应用程序询问访问符而不是显示登录页.

## 外部认证 {#external-authentication}

该应用程序向网页视图注入一个小的JavaScript桥. 当前端需要一个符号时,它会通过那座桥调用该应用程序,该应用程序会用一个访问符号回答. 当用户在前端登录时,它要求应用程序撤销该令牌.

该应用程序刷新访问符本身, 并刷新符号为 [登录](/companion/mobile-app-api/setup#log-the-user-in) 。 前端从未看到刷新符号.

## 外部总线 {#the-external-bus}

同桥搭载外部总线:前端和app之间双向消息. 通过它,前端可以打开应用程序的本土设置,启动条码扫描仪,启动Assist,或者将一个实体交给应用程序自己的**Add来进行**动作,该应用程序可以告诉前端它支持什么.

两个协议都导则在前端:[外部认证](/frontend/reference/external-auth)和[外部总线](/frontend/reference/external-bus). 关于Android应用程序如何执行它们,请参见[前端屏幕](/companion/android/frontend-screen#talking-to-the-frontend).

## 需要直接连接 {#needs-a-direct-connection}

网页视图从实例本身加载前端:内部URL,外部URL,或Home Assistant Link的远程URL. 网友的云泡URL在这里没有用.
