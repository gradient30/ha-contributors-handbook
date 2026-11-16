---
title: Android
description: The Home Assistant app for Android, Wear OS, Android Auto, and Android Automotive. What is in the repository, and where to start.
order: 2
sidebarGroups:
- 设置
- 架构
- 写代码
- 测试
- 船
---


# Android {#android}
这款 Android 应用于 2019 年启动，现在已有数百万人使用。它的核心是一个显示 Home Assistant 前端的网页视图。围绕它的都是原生功能：从手机报告的传感器、通知、部件、磁贴、NFC 标签、Assist、Wear OS 应用，以及用于 Android Auto 和 Android Automotive 的车载屏幕。

该项目完全用 Kotlin 编写。新界面使用 Jetpack Compose。你仍然会发现一些较旧的代码，如 XML 布局和视图绑定，这些都是在现行指南之前的代码。这些代码会随时间迁移，这里页面描述了新代码应该如何编写。

## 仓库 {#the-repository}

所有内容都位于 [home-assistant/android](https://github.com/home-assistant/android)。这是一个包含多个模块的 Gradle 项目：

| 模块 | 说明 |
| --- | --- |
| `:app` | 手机和平板应用 |
| `:automotive` | Android 汽车应用。重用 `:app` 的源码 |
| `:wear` | Wear OS 应用 |
| `:common` | 所有应用共享的代码：数据层、传感器、WebSocket 和 REST 客户端、设计系统以及所有字符串 |
| `:testing-unit` | 所有模块单元测试共享的辅助工具 |
| `:lint` | 项目的自定义 lint 规则 |
| `:microwakeword` | 设备端唤醒词检测 |
| `:provides-sensor-processor` | 传感器注册的代码生成器 |
| `build-logic` | 配置所有模块方式相同的约定插件 |

最低和目标 SDK 版本位于 [`gradle/libs.versions.toml`](https://github.com/home-assistant/android/blob/main/gradle/libs.versions.toml)，在 `androidSdk-*` 键下。

## 设置 {#set-up}

- [入门](/companion/android/get-started)：安装 Android Studio，构建应用并运行。
- [推送通知](/companion/android/push-notifications)：如果你处理通知，请设置你自己的 Firebase 项目。

## 架构 {#architecture}

- [架构](/companion/android/architecture)：原则、技术栈以及各模块如何结合在一起。
- [UI 架构](/companion/android/ui-architecture)：屏幕如何构建，从视图到仓库。
- [前端屏幕](/companion/android/frontend-screen)：承载 Web 视图的屏幕，以及 UI 架构的参考实现。
- [版本和目标](/companion/android/flavors-and-targets)：`full` 和 `minimal`，以及手机、汽车、手表和电视的构建。

## 编写代码 {#write-code}

- [Compose 与设计系统](/companion/android/compose)：使用 `HATheme` 和 `HA*` 组件构建 UI。
- [最佳实践](/companion/android/best-practices)：强类型、并发、依赖注入，以及快速失败。
- [代码风格与检查](/companion/android/code-style)：KTLint、Detekt 和 Android linter。
- [依赖管理](/companion/android/dependencies)：版本目录、锁文件，以及 Renovate。
- [调试工具](/companion/android/debugging)：开发者游乐场、StrictMode 和 LeakCanary。

## 测试 {#test}

- [测试](/companion/android/testing)：如何使用 JUnit、MockK、Robolectric 和 Turbine 编写测试和单元测试。
- [截图测试](/companion/android/screenshot-testing)
- [仪器测试](/companion/android/instrumentation-testing)
- [端到端测试](/companion/android/e2e-testing)

## 发布 {#ship}

- [提交一个 pull request](/companion/android/submitting)：清单、模板和审查。
- [持续集成](/companion/android/ci)：在你的 pull request 上运行的内容，以及合并后运行的内容。
- [发布](/companion/android/releases)：从合并的 pull request 到 Play 商店，并自己构建签名发布版本。

## 联系对象 {#who-to-talk-to}

- 在 [Home Assistant Discord](https://www.home-assistant.io/join-chat) 上的 [Android 项目线程](https://discord.com/channels/330944238910963714/1346948551892009101)。首先在 **渠道与角色** 下选择开发者角色。
- Android 仓库中的 [问题](https://github.com/home-assistant/android/issues)，用于报告错误和功能请求。
- 关于应用如何为用户工作，请参阅 [伴侣应用文档](https://companion.home-assistant.io/)。
