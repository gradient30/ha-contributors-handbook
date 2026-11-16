---
title: 安全伴侣应用程序
description: Android 和 iOS 应用程序的建议教给链接、导出组件、 WebView 和 JavaScript 桥。
sidebarLabel: 伴侣应用
order: 4
---

# 安全伴侣应用程序 {#secure-companion-apps}

A [附带应用程序](/glossary/companion-app) 正在登录到用户的 Home Assistant 服务器, 它会保持该登录的电话 。 这让应用程序成为房子的钥匙 任何可以让应用程序自己做一些事情的,比如同一个手机上的另一个应用程序,一个消息中的链接,或者一个帧中的网页,都可以在永远不知道密码的情况下使用该键.

伙伴应用软件的大部分建议 都是为了这个想法 这个指南通过他们, 那种错误, 与应用程序今天的统计数字。 关于应用程序的构建方式,请参见[伴侣应用](/companion).

## 打开链接前先询问 {#ask-before-acting-on-a-link}

应用程序对链接和标签的反应:NFC标签,QR代码,`homeassistant://`链接,`https://www.home-assistant.io/tag/`的通用链接. 操作系统将那些送到应用程序,它不在乎是谁发送的. 手机上的另一个应用程序可以发送相同的链接,循环中没有用户.

两次出错:

- 2023年,一个链接或QR代码可以在服务器上制作iOS和macOS app [呼叫动作](https://github.com/home-assistant/core/security/advisories/GHSA-h2jp-7grc-9xpp),无需询问.
- 2026年,其他应用程序可以在[Android 应用程序](https://github.com/home-assistant/core/security/advisories/GHSA-2xqv-hwrf-983f)和[iOS 应用程序](https://github.com/home-assistant/core/security/advisories/GHSA-j23v-9672-677j)中打开标记链接,扫描直接到服务器. 标记往往与解锁门或解除警报的自动化绑定.

教训:链接是请求,而不是命令. 当它会在服务器上改变一些东西时,用户首先批准,在应用内部.

应用程序今天做什么:

- 两个应用程序在从一个链接发送标记扫描到服务器之前都会询问,其中**Allow一次**和**Allow总是**. 设置允许用户收回总是允许的标记 。
- iOS应用程序在要求动作,点火事件,或因URL而发送位置之前,要求确认.

如果您在服务器上添加了新的链接,新的意图,或者新的快捷键来进行操作,则给出相同的确认.

## 显示您连接到的服务器 {#show-which-server-you-connect-to}

Android应用程序的一个邀请链接载有服务器的地址,该应用程序开始针对它登机[不显示地址](https://github.com/home-assistant/core/security/advisories/GHSA-68f4-97mf-f68w). 登录页面然后在WebView中加载,而不设地址栏. 假服务器可以显示登录页的完美副本并收集密码.

教训:当链接决定应用程序的连接地点时,在事发前向用户显示所在位置. Andro 这是我们的Android应用软件,现在显示一个邀请屏幕,上面有服务器的地址,警告只接受你信任的人的邀请,以及**接受**和**拒绝**.

## 将内部 URL 保存应享有 {#keep-the-internal-url-at-home}

服务器内部的URL经常是普通的`http:`,这在主网络上是好的,而不是其他地方. iOS app [掉回内部 URL](https://github.com/home-assistant/core/security/advisories/GHSA-cm5v-547m-qh5h) 在用户家用Wi-Fi网络列表中没有的网络上. 在公共网络上 信物可以用简洁的文字 发给那些在那个地址上回答的人

教训:一个旨在限制事物发生地的列表,必须限制它出现在每一个路径上,包括倒退. iOS应用程序现在每个服务器都有连接安全级别. 当内部的URL是服务器唯一的URL,而不是`https:`时,这个选择很重要. 使用 ** 最安全**, 应用程序只使用用户所列出的家庭网络上的 URL 。 使用**Less security**,在任何地方使用,用户接受这种风险. Android应用每个服务器都保持一个相似的选择,作为`allowInsecureConnection`.

## 保持组件私有 {#keep-components-private}

在Android上,一个活动,一个服务,或者一个拥有 `android:exported="true"` 的接收器,可以通过电话上的任何应用程序启动,并有任何数据. Android app的定位接收器被导出, 以及 [已接受位置更新](https://github.com/home-assistant/core/security/advisories/GHSA-77r5-pw5w-mgj3) 从任何应用程序中导出 。 一个恶意的应用程序可以发送一个假的位置,并触发自动化,对回家的人作出反应.

固定显示模式 :

- 处理位置数据的接收器不再驴出。
- 一个小的,单独的接收器保留出口,用于像Tasker这样的工具所使用的公共行动. 它只接受一个动作, 放下任何调用者发送的数据,

```xml
<receiver
    android:name=".sensors.LocationSensorReceiver"
    android:exported="false" />
```

在导出一个组件之前, 询问还需要找到谁 。 如果答案无人, 请设置 `android:exported="false"` 。 如果其他的应用必须到达它,接受最小的可行事物,永远不要相信随之而来的数据.

Android寄存器的[建筑技能](https://github.com/home-assistant/android/blob/main/.agents/skills/ha-android-architecture/SKILL.md)增加了一条相关的规则:总是设置一个`PendingIntent`的变异性,默认为`FLAG_IMMUTABLE`,因为不必要的变异性会拓宽攻击表面.

## 只装入 WebVi及其它服务器 {#load-only-the-server-in-the-webview}

apps的WebView运行前端,可以访问符号. 在2023年,一个链接可以使Android应用[装入任意 URL](https://github.com/home-assistant/core/security/advisories/GHSA-jvpm-q3hq-86rg)在那个WebView中. 攻击者的一页会以与前端相同的权力运行.

教训:从链接、意图或通知中获取的URL是不可信的。 检查它在WebView加载前的指针位置.

## 守护JavaScript桥 {#guard-the-javascript-bridge}

前端通过 JavaScript 桥向应用程序说话 : `window.externalApp` 在Android上, 以及像 `getExternalAuth` 在 iOS 上的信息处理器 。 前端通过它要求访问符.

在2026年, [两个错误在一起](https://github.com/home-assistant/core/security/advisories/GHSA-7jp2-p2fw-mgvf) 允许一个网页在一个架构中, 就像一个在仪表板上的网页卡一样, 得到一个符号:

1. 该桥 你在回答每个帧, 也从另一个来源的帧。
2. 应用程序将消息中的召回名称放入 JavaScript 它运行在主框, 不检查它。

应用程序今天做什么:

- 在Android上,一个更新的桥型,`externalAppV2`使用`addWebMessageListener`,并忽略了来自帧,以及来自不匹配加载服务器的源头的信息. 该应用程序在服务器和WebView支持时使用.
- 在Android上,`getExternalAuth`和`revokeExternalAuth`只接受前端使用的两个召回名称,`externalAuthSetToken`和`externalAuthRevokeToken`,两个桥都使用.
- 在iOS上,`SafeScriptMessageHandler`只传递来自主帧的信息,有一个方案,主机,端口匹配服务器的URL.

Android检查的核心是这样的:

```kotlin
if (!isMainFrame) {
    Timber.w("Ignored message from iframe")
    return@addWebMessageListener
}
val currentUri = stateProvider().url?.toUri()
if (!sourceOrigin.hasSameOrigin(currentUri)) {
    return@addWebMessageListener
}
```

教训:决定谁可以和桥说话,按框和来源. 永远不要将一个值从一个消息变成代码:把它比作一个固定的列表.

## 保存日志中的秘密 {#keep-secrets-out-of-logs}

用户在报告问题时共享日志. Android 仓库的 [伐木技能](https://github.com/home-assistant/android/blob/main/.agents/skills/ha-android-logging-errors/SKILL.md) 要求您将用户数据包入 `sensitive()` , 因此它不会在发布日志中显示 。 实体ID是罚款。 URL,以及任何识别服务器或用户的东西,都不是. 对于存储在电话上的数据,[建筑技能](https://github.com/home-assistant/android/blob/main/.agents/skills/ha-android-architecture/SKILL.md)指向`EncryptedSharedPreferences`.

## 相关 {#related}

- [过去的建议](/security/reference/advisories#companion-apps):每一份伴侣应用的咨询在一个表格中.
- :前端端,应用程序程序显示数显示数.数)数.数.数.数.数.数.数.数数.数数数数数数数数数数数数数数数数数数数数数数数数数数数数数数数数数值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值值
- [伴侣应用](/companion):应用程序是如何构建的.
