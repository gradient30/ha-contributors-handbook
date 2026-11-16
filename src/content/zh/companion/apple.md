---
title: Apple
description: Home Assistant iPhone, iPad, Mac, Apple Watch, 和 CarPlay 的应用程序 。 仓库里有什么,从哪里开始
order: 3
source: https://github.com/home-assistant/iOS/blob/main/CONTRIBUTING.md
lastVerified: 2026-10-14
---



# Apple {#apple}
最后一次验证是在2026-10-14,对https://github.com/home-assistant/iOS/blob/main/CONTRIBUTING.md.

苹果应用为iPhone,iPad,Mac,Apple Watch和CarPlay带来了Home Assistant. 与Android应用程序一样,其中心是使用Home Assistant前端的网页视图. 围绕它,很多是本土的:登机,设置,传感器,位置,通知和现场活动,部件和控制,App intents和快捷键,手表应用及其并发症,以及CarPlay.

所有它都生活在一个寄存器[Home Assistant/iOS](https://github.com/home-assistant/iOS),用斯威夫特写成. Mac App是用同一代码的Mac Catoryst构建的.

## 存储器 {#the-repository}

一切众生住[Home Assistant/iOS](https://github.com/home-assistant/iOS). 这是一个 Xcode 工程, `HomeAssistant.xcodeproj`, 其源代码为几个主要文件夹 :

| 文件夹 | 这是什么 |
| --- | --- |
| `Sources/App` | iPhone 和 iPad 应用程序 |
| `Sources/Shared` | 编码每个目标份额:API、数据库、传感器、通知 |
| `Sources/Extensions` | 部件、 App 插件、 通知、 共享和 Matter 扩展 |
| `Sources/Watch`, `Sources/WatchApp` | 苹果观察应用 |
| `Sources/CarPlay` | 车牌 |
| `Sources/MacBridge` | 催化剂建筑的Mac 特定代码 |
| `Sources/PushServer` | 驱动中继服务器, 一个单独的 Swift 包 |
| `Tests` | 单位、用户界面、快照和部件测试 |

完整列表在[结构](/companion/apple/architecture#the-source-folders)中.

## 设置 {#set-up}

- ؟ [开始](/companion/apple/get-started): 安装 Xcode 和工具, 设置签名, 运行应用程序 。

## 架构 {#architecture}

- [架构](/companion/apple/architecture) : 代码是如何排列的 `Current` 支撑它的环境, 以及应用程序如何与 Home Assistant 交谈 。
- [目标](/companion/apple/targets): 应用, 扩展, 手表, CarPlay, 和 Mac, 以及变化会影响什么 。

## 写代码 {#write-code}

- [代码样式](/companion/apple/code-style): SwiftFormat, SwiftLint, 以及项目的常规.

## 测试 {#test}

- [测试](/companion/apple/testing):单位,快照,UI,以及端到端的测试,以及补丁覆盖门.

## 船 {#ship}

- [提交 pull request](/companion/apple/submitting):核对表、模板和审查。
- [持续集成](/companion/apple/ci) : 您的 pull request 运行情况, 合并后会发生什么 。
- [发布](/companion/apple/releases):从一个合并的pull request到App Store Connect,和Mac在GitHub上发布.

## 翻译 {#translate}

app的文本在 Lokalise 上翻译, 在自己的 iOS 项目中. 你不需要Mac或X码 见[您的第一个翻译](/translate/first-contribution).

## 谁说话 {#who-to-talk-to}

- [苹果应用**](https://discord.com/channels/330944238910963714/1481713628553019392) [Home Assistant Discord](https://www.home-assistant.io/join-chat) 上的频道 。 先在 **Channels & Locations ** 下选择开发者角色.
- [问题](https://github.com/home-assistant/iOS/issues)在iOS寄存器中,用于错误和特性请求.
- 想早点测试新特性吗? 加入 [测试 Flight β](https://www.home-assistant.io/ios/beta/) 。
- 关于应用程序如何为用户服务,请参见[辅助应用程序文档](https://companion.home-assistant.io/).
