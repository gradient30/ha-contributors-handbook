---
title: 伴侣应用程序的作用
description: Home Assistant 在安卓和苹果设备上：应用中的前端，以及来自设备本身的传感器、通知、部件等。
order: 6
sidebarLabel: 伴侣应用
---


# 伴侣应用程序的作用 {#how-the-companion-apps-fit-in}
[伴侣应用程序](/glossary/companion-app) 将 Home Assistant 带到手机、平板电脑、手表、汽车和 Mac 上。它们显示与浏览器相同的 [前端界面](/architecture/frontend)，并添加只有设备上的应用才能实现的功能：传感器、位置、通知、小部件和快速控制。

## 简而言之 {#in-short}
- Android 应用使用 Kotlin 编写，Apple 应用使用 Swift 编写。每个都有自己的代码库。
- 主屏幕是前端，在网页视图中显示。原生部分环绕其周围。
- 应用在 `mobile_app` 集成中注册自己，使手机成为具有实体的设备。
- 应用通过 webhook 发送传感器数据和位置信息。通知通过推送服务返回。

## 两个部分 {#two-parts}
| 部分 | 功能 |
| --- | --- |
| 前端，在网页视图中 | 仪表板、设置，你在浏览器中看到的所有内容 |
| 原生代码 | 登录、传感器、位置、通知、小部件、手表应用、汽车应用以及应用的设置 |

前端知道它何时在应用内运行，并通过桥接与应用通信：扫描二维码、显示原生设置或使用手机的麦克风进行语音。

## 注册 {#registering}
当用户登录应用时，应用会向`mobile_app`集成注册自己。这会创建一个[配置条目](/core/integrations/config-entries)和一个手机设备，并为应用提供一个[Webhook](/architecture/connections)。Webhook可以加密，因此即使在未加密的连接上，其数据也是安全的。

从那时起，应用会通过该Webhook发送传感器数据，如电池电量和位置信息。每个传感器都会成为手机设备的一个实体。使用Home Assistant Link时，Webhook在远程也能工作。

## 通知 {#notifications}
Home Assistant无法直接访问手机。通知通过项目的推送服务发送，该服务将通知交给Google和Apple的服务，由它们送达手机。应用在注册时会告诉`mobile_app`将通知发送到哪里。

## 在代码中 {#in-the-code}
| 什么 | 位置 |
| --- | --- |
| Android，包括 Wear OS 和 Android Auto | [home-assistant/android](https://github.com/home-assistant/android) |
| iOS、iPadOS、macOS、watchOS 和 CarPlay | [home-assistant/iOS](https://github.com/home-assistant/iOS) |
| 核心端 | [`homeassistant/components/mobile_app/`](https://github.com/home-assistant/core/tree/dev/homeassistant/components/mobile_app) |
| 前端的桥接 | [`src/external_app/`](https://github.com/home-assistant/frontend/tree/dev/src/external_app) 在 [home-assistant/frontend](https://github.com/home-assistant/frontend) |

## 处理这个 {#work-on-this}
- 从 [你的第一个伴侣应用贡献](/companion/first-contribution) 开始。
- 每个应用的构建方式：[Android 架构](/companion/android/architecture) 和 [Apple 架构](/companion/apple/architecture)。
- [移动应用 API](/companion/mobile-app-api)：注册、传感器和通知，适用于官方应用和你自己的应用。
