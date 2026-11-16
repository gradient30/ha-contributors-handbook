---
title: Android 版本和目标
description: Android 应用的完整和最小版本，以及手机、Android 汽车系统、Wear OS 和电视版本。
sidebarLabel: 口味和目标
sidebarGroup: 架构
order: 4
---

# Android 版本和目标 {#android-flavors-and-targets}

这个安卓应用程序是为多种设备构建的，并且有两种版本。对共享代码的更改可能会影响所有设备，因此了解每种版本的情况是有帮助的。

## 版本 {#flavors}

`:app` 和 `:automotive` 模块有两种版本。`:wear` 模块没有版本。

| | `full` | `minimal` |
| --- | --- | --- |
| Google Play 服务 | 是 | 否 |
| 应用 ID | `io.homeassistant.companion.android` | `io.homeassistant.companion.android.minimal` |
| 用于 [存在检测](https://www.home-assistant.io/getting-started/presence-detection/) 的位置跟踪 | 是 | 否 |
| 推送通知 | 通过 Firebase，并通过 WebSocket | 仅通过 WebSocket，见 [本地推送](https://companion.home-assistant.io/docs/notifications/notification-local) |
| Wear OS 应用 | 是 | 否 |
| 崩溃报告 | 是 | 否 |
| 分发渠道 | Google Play | F-Droid，GitHub 上的 APK，Meta Quest，以及面向汽车厂商的 Android Automotive 构建 |

调试版本会在应用 ID 后添加 `.debug`，因此可以安装在发布版本旁边。

`minimal` 版本适用于那些更喜欢或需要没有 Google Play 服务的应用的人，例如没有 Google Play 服务设备的用户。尽可能将更多代码保留在`main`源集中，以便两种版本的用户都能获得该功能。在有选择的情况下，项目优先选择开源解决方案。只有需要Google Play服务的代码才放入`full`源集中，并且有`minimal`对应部分。如果Play服务功能的开源替代方案可行，它也可以移到`minimal`中。

## 目标 {#targets}

| 目标 | 模块 | 最低 SDK |
| --- | --- | --- |
| 手机和平板 | `:app` | `androidSdk-min` |
| Android 汽车 | `:automotive` | `androidSdk-automotive-min` |
| Wear OS | `:wear` | `androidSdk-wear-min` |

版本信息在 [`gradle/libs.versions.toml`](https://github.com/home-assistant/android/blob/main/gradle/libs.versions.toml)。

### 手机和平板 {#phone-and-tablet}

主要应用，大多数人使用。Android Auto 是其中的一部分：手机将汽车屏幕投射到车载显示器。

### Android 汽车 {#android-automotive}

运行在汽车上的应用。它将 `:app` 的源码与自己的清单文件编译。汽车相关 API 从 API 29 开始存在，因此其最低 SDK 更高。

### Wear OS {#wear-os}

一个独立的应用，但不是独立运行的：它需要手机应用来进行初始化和获取服务器凭证。之后，它直接与 Home Assistant 进行通信。

### 安卓电视 {#android-tv}

手机应用可以安装在安卓电视上，但没有专门的模块，用遥控器导航体验不好。更好的电视体验需要专用的模块和导航支持。
