---
title: 伴侣应用
description: 官方 Home Assistant 为Android,iOS,iPadOS,macOS,watchOS,Wear OS,以及车的应用程序.
  如何建造,如何帮助建造.
---



# 伴侣应用 {#companion-apps}
伴侣应用将Home Assistant放入你的口袋,手腕和车内. 它们显示的是浏览器上所知道的相同的前端,并添加了设备上只有应用程序能做的:传感器,位置,通知,部件,监视应用程序,以及汽车屏幕.

有两款应用程序,每款由自己的贡献者组建在自己的库中:

| 应用 | 运行在 | 语言 | 仓库 |
| --- | --- | --- | --- |
| 安卓 | Android手机和平板电脑,Wear OS,Android Automotive,Android Automotive,Meta Quest | 科特林语Name | [Home Assistant/机器人](https://github.com/home-assistant/android) |
| 苹果公司 | iPhone, iPad, Mac, 苹果观察, CarPlay | 挥动 | [Home Assistant/iOS](https://github.com/home-assistant/iOS) |

两者通过Core中相同的集成来和Home Assistant交谈:`mobile_app`. 这种整合是公共API,所以其他的应用程序也可以使用.

这个区域是给想要在任一应用程序上工作的开发者,以及给任何建立自己的应用程序来向Home Assistant说话的人的. 你需要与科特林和Android Studio, 或与斯威夫特和Xcode舒适. 如果您想要帮助而不写入代码, 也有很多工作要做 : 见 [帮助的方式](/companion#ways-to-help) 。

## 帮助的方法 {#ways-to-help}

- **Fix a bug或构建一个特性**:在Android或iOS寄存器中选择一个问题.
- ** 测试β**: 加入 [谷歌游戏中的Android beta](https://play.google.com/apps/testing/io.homeassistant.companion.android) 或 [测试 Flight 上的 iOS β 怎么了?](https://www.home-assistant.io/ios/beta/), 并报告中断的内容 。
- ** Test pull requests**:从 pull request 安装一个构件,并告知作者是否有效 。 见[测试 pull request 构建](/companion/android/get-started#test-a-pull-request-build).
- ** 审查**:每个人都可以对pull request发表意见。 即使是简短的检讨也会有所帮助。
- ** 翻译**:两个应用程序都在Lokalise上翻译. 见[翻译](/translate).
- ** 文件**:用户文档位于{L遵照},位于[伴侣,Home Assistant](https://github.com/home-assistant/companion.home-assistant)仓库。

## 从这里开始 {#start-here}

- [你的第一次贡献](/companion/first-contribution): 选择您的平台, 构建应用程序, 并打开您的第一个 pull request 。
- [应用程序是如何适应的](/architecture/platform/companion-apps):大局,从网页视图到推车服务.

## 安卓 {#android}

- [55. 机器人概况](/companion/android):寄存器,模块,以及在哪里找到什么.
- ổ人:设置Android Studio并构建应用.
- [架构](/companion/android/architecture)和[UI 架构](/companion/android/ui-architecture):应用程序及其屏幕的结构如何排列.
- [测试](/companion/android/testing):单位,截图,仪表,以及端到端的测试.
- [提交 pull request](/companion/android/submitting):核对表和审查过程。

## 苹果公司 {#apple}

- [苹果概览](/companion/apple):寄存器,目标,以及在哪里找到什么.
- [开始](/companion/apple/get-started):设置 Xcode,签名,并构建应用程序.
- [架构](/companion/apple/architecture)和[开放供衡量的目标](/companion/apple/targets) : 代码如何在 iPhone, Watch, CarPlay, 部件和 Mac 之间共享 。
- [提交 pull request](/companion/apple/submitting):核对表和审查过程。

## 移动应用程序 API {#the-mobile-app-api}

- [移动应用程序 API](/companion/mobile-app-api):一个应用程序如何连接到Home Assistant,自行登记,发送传感器数据和位置,并收到通知. 无论是正式的应用程序还是你自己的

## 谁说话 {#who-to-talk-to}

- 加入 [Home Assistant Discord](https://www.home-assistant.io/join-chat) 并选择 **Channels & Locations ** 下的开发者角色 。 然后前往 [Android 项目线索](https://discord.com/channels/330944238910963714/1346948551892009101) 或 [苹果应用**](https://discord.com/channels/330944238910963714/1481713628553019392) 频道 。 超越一个app的问题,如`mobile_app`集成,适合[发展中国家**](https://discord.com/channels/330944238910963714/554842238073700352)频道.
- 错误和特性请求到 [安卓](https://github.com/home-assistant/android/issues) 或[iOS系统](https://github.com/home-assistant/iOS/issues) 寄存器的问题 。
- 关于 `mobile_app` 在 Core 中的整合 的问题 转到 [核心存储器](https://github.com/home-assistant/core) 。
