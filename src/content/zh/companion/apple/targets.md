---
title: Apple 目标
description: 苹果项目的应用,扩展,Apple Watch,CarPlay,和Mac目标,以及当您的更改触及到共享代码时需要检查什么.
sidebarLabel: 目标
order: 3
---



# Apple 目标 {#apple-targets}
Xcode项目从一个代码库中构建了许多产品. 共享代码的改变会最终出现在所有代码中, 所以检查一下您更改的触摸到哪些代码.

## 计划 {#the-schemes}

| 计划 | 构建 |
| --- | --- |
| `App-Debug` | 应用,为地方发展. 从这里开始 |
| `App-Release` | 应用程序,随着它的船 |
| `Tests-Unit` | CI运行的单元测试 |
| `Tests-UI` | UI测试和端到端登机测试 |
| `WatchApp` | 苹果观察应用 |
| `Extensions-*` | 每个应用程序扩展一个, 如 `Extensions-Widgets` |

## iPhone 和 iPad 软件 {#iphone-and-ipad}

主应用,在`Sources/App`中. 大部分特征都从这里开始.

## 你想怎样? {#widgets-controls-and-app-intents}

`Sources/Extensions/Widgets` 和`Sources/Extensions/AppIntents` 功率主屏幕和锁屏幕部件, 控制中心控件和快捷键 。 它们作为扩展运行,在应用程序之外。

部件、 手表、 CarPlay 和快捷键中出现的项目共享一个模型 `MagicItem` 。 如果你添加了一种新的项目或行动,它可能需要在所有这些方面发挥作用。

## 通知 {#notifications}

若干目标处理通知:

- 通知服务扩展,在显示前更改通知,例如下载附件。
- 通知内容扩展,用于扩大的通知视图,如相机流.
- 推推供应商延伸,为本地推推家庭网.

直播活动是应用程序和部件的一部分。 在做通知时,请检查所有通知。 查看 [用户文档](https://companion.home-assistant.io/docs/notifications/notifications-basic) 用户可以做什么 。

## 苹果观察 {#apple-watch}

手表应用在 `Sources/Watch` 和 `Sources/WatchApp` 中, 以及它的并发症和部件在 `Sources/WatchWidgets` 中 。 改变动作、通知、并发症或共享设置往往也需要在表上进行测试。 手表有它自己的测试,它运行在手表模拟器上.

## 车牌 {#carplay}

`Sources/CarPlay` 拥有模板、 列表项、 过滤器以及支持的实体的行动 。

## 共享和 { 看来 Matter {#share-and-matter}

共享扩展处理从其他应用程序共享到Home Assistant的内容. Matter 扩展是添加Matter 设备的一部分 。 如果您的更改触及到来的内容或设备设置, 请检查这些 。

## 没什么 {#mac}

Mac App是用同一代码的Mac Catoryst构建的. `Sources/MacBridge`有Mac的特定部件。 即使你只研究一个iOS特性,共享代码也被编译为Mac,所以它必须在那里构建.

## 推进服务器 {#the-push-server}

`Sources/PushServer`是用于推力继电器的独立Swift包. 它不属于Xcode项目,并有自己的测试. 它自带 `Sources/SharedPush` 的通知解析器副本 : 当您更改一个时, 决定另一个是否需要相同的更改 。 见[测试](/companion/apple/testing#the-push-server).
