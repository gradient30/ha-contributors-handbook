---
title: Android 推送通知
description: 建立你自己的 Firebase 项目和推送服务，以便在处理通过 Firebase 云消息传递发送的通知时使用。
sidebarLabel: 推送通知
sidebarGroup: 开始设置
order: 2
---

# Android 推送通知 {#push-notifications-on-android}

The `full` 版本通过 Firebase Cloud Messaging (FCM) 接收通知。Home Assistant 向项目的推送服务发送通知，由推送服务交给 FCM，再由 FCM 发送到手机。[移动应用 API](/companion/mobile-app-api/notifications) 描述了该契约。

只有在你处理那条路径时才需要自己的设置。对于其他所有情况，来自 [入门](/companion/android/get-started#3-add-a-firebase-configuration) 的模拟 Firebase 文件就足够了，通知仍然会通过 WebSocket 连接到达应用。这也是 `minimal` 版本接收通知的方式。

> [!提示]
> 设置 FCM 需要一些努力。如果你可以用 WebSocket 通知测试你的更改，请这样做。

## 设置您自己的 FCM 项目 {#set-up-your-own-fcm-project}

1. 在 [Firebase 控制台](https://console.firebase.google.com) 创建一个项目。
2. 为以下每个应用程序 ID 将 Android 应用添加到项目中：
   - `io.homeassistant.companion.android`
   - `io.homeassistant.companion.android.debug`
   - `io.homeassistant.companion.android.minimal`
   - `io.homeassistant.companion.android.minimal.debug`
3. 在您的 Firebase 项目中创建默认的 Cloud Firestore 数据库。推送服务会在那里保持其速率限制，除非您配置它使用 Valkey。
4. 将推送服务从 [home-assistant/mobile-apps-fcm-push](https://github.com/home-assistant/mobile-apps-fcm-push) 部署到您的 Firebase 项目。
5. 将应用指向您的服务。在 Gradle 用户主目录 (`~/.gradle/gradle.properties`) 中的 `gradle.properties` 中添加已部署 `androidV1` 函数的 URL，而不是仓库中的 URL：

   ```properties
   homeAssistantAndroidPushUrl=https://push.example.com/androidV1
   ```

   可选地，也可以将速率限制检查指向您的服务：

   ```properties
   homeAssistantAndroidRateLimitUrl=https://push.example.com/checkRateLimits
   ```

   如果没有这些覆盖，应用将使用项目自己的推送服务，该服务在仓库的 `gradle.properties` 中设置。

6. 从你的 Firebase 项目下载 `google-services.json` 并将其放入 [`app/`](https://github.com/home-assistant/android/tree/main/app)、[`automotive/`](https://github.com/home-assistant/android/tree/main/automotive) 和 [`wear/`](https://github.com/home-assistant/android/tree/main/wear) 中。

`google-services.json` 文件必须包含所有四个应用程序 ID 的客户端。如果缺少其中一个，FCM 将无法在该构建中工作，并且只有 WebSocket 通知会到达。
