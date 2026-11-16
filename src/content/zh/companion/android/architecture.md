---
title: 安卓架构
description: Android 应用背后的原理、各个模块、技术栈，以及手机、汽车和手表应用如何协同工作。
sidebarLabel: 架构
sidebarGroup: 架构
order: 1
---

# 安卓架构 {#android-architecture}

该应用遵循谷歌的[推荐应用架构](https://developer.android.com/topic/architecture)，并从[Android 中的 Now](https://github.com/android/nowinandroid)中汲取灵感。该项目历史悠久，因此你会发现一些代码尚未遵循这些规则。本页描述了项目的发展方向。如有疑问，请遵循本页内容，而非你旁边的代码。

## 带本地功能的网页视图 {#a-web-view-with-native-features}

Home Assistant 一直是一个强大的渐进式网页应用，Android 应用在此基础上构建。它的主屏幕是一个显示 Home Assistant 前端的 [WebView](https://developer.android.com/reference/android/webkit/WebView)。应用和前端通过 JavaScript 桥进行通信：前端通过 [外部认证](/frontend/reference/external-auth) 向应用请求访问令牌，并通过 [外部总线](/frontend/reference/external-bus) 交换消息。有关详细工作机制，请参见 [前端屏幕](/companion/android/frontend-screen)。

其他所有功能都是本地的：入门引导、设置、传感器、通知、组件、磁贴、Assist，以及汽车和手表应用。

## 原则- **仅限 Kotlin。** 整个代码库都是 Kotlin，并且将保持这种状态。 {#principles}
- **所有新 UI 使用 Compose。** 不再使用新的 XML 布局、数据绑定或视图绑定。新的组件使用 Jetpack Glance。新的屏幕使用 `HATheme` 主题。旧的 `HomeAssistantAppTheme` 是 Material 2，已被弃用。参见 [Compose 和设计系统](/companion/android/compose)。
- **所有并发操作使用协程（Coroutines）和 Flow。**
- **依赖注入使用 Hilt。** 永远不要手动创建注入的类。
- **保持代码与风味无关。** 将代码放在 `main` 源代码集，以便两个 [flavors](/companion/android/flavors-and-targets) 均可使用。只有需要 Google Play 服务的代码才放在 `full`。
- **跟上 Android 步伐。** 目标 SDK 遵循最新的 Android 版本，并在新 Android 版本推出时进行测试。

- **服务器版本的 Gate 功能** 当它们需要 Home Assistant 中旧版本没有的某些东西时，例如 `server.version?.isAtLeast(2025, 6, 0)`。

## 模块 {#modules}

模块列在 [Android 概览](/companion/android#the-repository) 中。有几件事值得注意：

- 公共的 Gradle 配置位于 `build-logic` 的约定插件中，这是一个包含的构建。如果你在多个模块中需要相同的设置，它应该放在那里。
- `:common` 包含手机、汽车和手表应用共享的所有内容，包括 [`common/src/main/res/values/strings.xml`](https://github.com/home-assistant/android/blob/main/common/src/main/res/values/strings.xml) 中面向用户的所有字符串。只编辑英文文件：翻译来自 Lokalise。请参见 [翻译](/translate)。
- `:automotive` 本身没有源代码。它使用不同的清单文件和更高的最低 SDK 来编译 `:app` 的源代码。

在模块内部，代码按功能打包：`sensors/`、`notifications/`、`settings/`、`onboarding/`、`widgets/`、`frontend/`，等等。

## 技术栈 {#the-tech-stack}

| 关注点 | 应用使用 |
| --- | --- |
| UI | [Jetpack Compose](https://developer.android.com/compose), [Glance](https://developer.android.com/develop/ui/compose/glance) 用于小部件 |
| 导航 | 使用类型安全路由的 Navigation Compose |
| 依赖注入 | [Hilt](https://developer.android.com/training/dependency-injection/hilt-android) |
| 并发 | [Kotlin 协程](https://kotlinlang.org/docs/coroutines-overview.html) 和 Flow |
| WebSocket API | [OkHttp](https://square.github.io/okhttp/) |
| REST API | [Retrofit](https://square.github.io/retrofit/) |
| 序列化 | Kotlinx.serialization |
| 数据库 | [Room](https://developer.android.com/training/data-storage/room)，用于用户数据 |
| 应用设置 | SharedPreferences，通过 `LocalStorage` 抽象 |
| 日志记录 | [Timber](https://github.com/JakeWharton/timber) |

## 选择流类型 {#picking-a-flow-type}

当你公开一个流时，根据在没有人收集它的情况下值必须发生的处理方式来选择其类型：

| 它承载的内容 | 用途 |
| --- | --- |
| 状态：只有最新的值重要，重新渲染它也没关系，比如屏幕状态或模式 | `StateFlow` |
| 每个收集器都必须接收到的事件，或者一旦其上下文消失就无意义且在无人监听时必须丢弃的事件，比如绑定到已加载页面的 WebView 操作 | `SharedFlow` |
| 一个消费者必须恰好处理一次、永不丢失也永不重复的事件，比如导航、Snackbar 或打开链接 | `Channel(Channel.BUFFERED)` 通过 `receiveAsFlow()` 暴露 |`Channel` 会保留一个值，直到有消费者存在，并将每个值交给单个收集器。在屏幕开始收集之前发送的事件仍然会到达。没有重放的 `SharedFlow` 会丢弃它。从协程中使用 `send`，只在不能挂起的回调中使用 `trySend`。

## 与 Home Assistant 通信 {#talking-to-home-assistant}

该应用使用三种渠道：

- [`mobile_app` 集成](/companion/mobile-app-api)的 **Webhook**，用于传感器更新、位置和注册更新。
- **WebSocket API**，保持开放以支持实时功能，如 Assist、小部件中的实体状态，以及无需 Firebase 的通知。
- **REST API**，用于其他功能。

传感器数据在后台收集，并由前台服务和工作器发送到 Home Assistant。

## Wear OS {#wear-os}

Wear OS 应用是 `:wear` 中的独立应用。它无法自行注册：它通过 [Wearable 数据层](https://developer.android.com/training/wearables/data/data-layer) 从手机应用获取服务器 URL 和凭据。这需要 Google Play 服务，因此只适用于手机应用的 `full` 版本。设置完成后，手表通过 WebSocket API 及其自身的 webhook 直接与 Home Assistant 通信。

## Android 汽车系统与 Android Auto {#android-automotive-and-android-auto}

Android Auto 从手机应用运行：它将 `:app` 从手机投射到汽车显示屏。Android 汽车系统是一个独立的构建，`:automotive`，运行在汽车本身上。两者使用相同的源代码。

## 深度链接 {#deep-links}

应用程序处理 `homeassistant://` 链接，以打开应用程序的特定部分。这些链接在 [URL 处理文档](https://companion.home-assistant.io/docs/integrations/url-handler/) 中为用户记录。

## 接下来 {#next}

- [UI 架构](/companion/android/ui-architecture)：单个界面的结构方式。
- [最佳实践](/companion/android/best-practices)：每次审核中都会出现的编码规则。
