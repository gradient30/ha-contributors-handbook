---
title: 你的第一个伴侣应用贡献
description: 选择Android或Apple,在您的机器上构建应用程序,并打开您的第一个pull request.
sidebarLabel: 你的第一次贡献
order: 1
---



# 你的第一个伴侣应用贡献 {#your-first-companion-app-contribution}
您对一个辅助应用的首次贡献并不一定是一个特征. 一个小的bug修补, 一个提示,没有人修补, 或缺失测试是一个伟大的开始。 它让你通过整个循环一次: 构建,改变,测试,pull request,审查。

## 选择您的平台 {#1-choose-your-platform}

这两个应用程序除了与API交谈之外,什么也没有分享. 挑一个和你每天使用的技能和设备相匹配的:

| | 安卓 | 苹果公司 |
| --- | --- | --- |
| 语言 | 科特林语Name | 挥动 |
| IDE 密码 | Android 工作是吗 | Xcode( 在 Mac 上) |
| 构建系统 | 牵引 | 带有 Swift 软件包管理器的 Xcode, 用于工具的 Fastlane |
| UI | Jetpack 编译( XML 正在迁移) | 快速UI 和 UIKit |
| 仓库 | [Home Assistant/机器人](https://github.com/home-assistant/android) | [Home Assistant/iOS](https://github.com/home-assistant/iOS) |

你需要一个Mac来操作苹果的应用程序 对于Android来说,任何运行Android Studio的机器都会起作用.

## 要求对你好 {#2-say-hi}

加入 [Home Assistant Discord](https://www.home-assistant.io/join-chat) , 在 **Channels & Locations ** 下选择开发者角色, 并前往 [Android 项目线索](https://discord.com/channels/330944238910963714/1346948551892009101) 或 [苹果应用**](https://discord.com/channels/330944238910963714/1481713628553019392) 频道 。 告诉大家你想做什么 它能拯救你 建造别人已经建造的东西。

## 创建了应用程序 3. {#3-build-the-app}

遵循您的平台设置指南 :

- [开始使用 Android](/companion/android/get-started)
- [从苹果开始](/companion/apple/get-started)

在模拟器、模拟器或你自己的设备上运行应用程序,并将其连接到Home Assistant实例。 测试实例最好: 应用程序在您所连接的每个服务器上注册为新设备 。

## 寻找工作 {#4-find-something-to-work-on}

第一个好目标:

- ** 未决问题**:浏览[机器人问题](https://github.com/home-assistant/android/issues)或[iOS问题](https://github.com/home-assistant/iOS/issues)。 你能够繁殖的小东西是理想的。
- ** Lint 基线** (Android):应用,磨损,汽车,常见,微醒字模块各有一个`lint-baseline.xml`,已知的问题从未固定. 修好一个,把它从基线上移除,完成 见[代码样式和折叠](/companion/android/code-style#baselines).
- ** 缺失测试**:添加一个没有代码的测试。 两种寄存器值测试都很高,苹果寄存器甚至要求您更改的大部分行被覆盖.
- ** 让你烦恼的东西**:你撞到自己的虫子是最好的第一话题,因为你已经知道它为什么重要。

## 5.  打开 pull request {#5-open-a-pull-request}

叉出寄存器,创建分支,使您的更改,并打开 pull request 对 `main` 。 完全填写 pull request 模板; 它有一个核对表并询问您如何使用 AI 工具 。 在开始前读 [AI 政策](/start/ai-policy) 。

提交的指南详细介绍如下:

- [提交 Android pull request](/companion/android/submitting)
- [提交 Apple pull request](/companion/apple/submitting)

如果用户可以看见您的更改, 还需要在 [用户文档](https://github.com/home-assistant/companion.home-assistant) 中显示 pull request 。

> [!NOTE]
> 检讨需要一段时间 耐心点 确保CI是绿色的

## 接下来是什么 {#what-is-next}

- 读取您的平台的架构 : [安卓](/companion/android/architecture) 或 [苹果公司](/companion/apple/architecture) 。
- 好奇应用程序怎么和Home Assistant说话? 读[移动应用程序 API](/companion/mobile-app-api).
