---
title: Apple 架构
description: 怎么样Home Assistant 苹果应用组织. 源文件夹,共享代码,当前环境,以及规则的每次更改都随之而来.
sidebarLabel: 架构
order: 2
source: https://github.com/home-assistant/iOS/blob/main/Package.resolved
lastVerified: 2026-10-14
---



# Apple 架构 {#apple-architecture}
最后一次验证是在2026-10-14,对https://github.com/home-assistant/iOS/blob/main/Package.resolved.

Apple App最初是一个网页视图,有一些本地的额外内容,后来成长为一个混合代码库,拥有本地登机,传感器,部件,App Intents,一个Apple Watch App,CarPlay,和Live Actions. 一个寄存器通过MacCatoryst构建了全部,用于iOS,iPadOS,watchOS,和macOS.

## 堆叠 {#the-stack}

- ** Swift**,与SwiftUI换作新的UI. UIKit仍然用于更古老的屏幕以及苹果框架需要的地方.
- QQ码**与`HomeAssistant.xcodeproj`. 依赖是Swift包.
- QQL0}**用于衬里,测试,版本,以及发行.
- 前端 他们在应用程序和前端之间设有 JavaScript 消息总线 。
- 用于部件、控件和快捷键的 QQL0+和QQL1+。

您将遇到的图书馆最多:

- [HAKIT (韩语)](https://github.com/home-assistant/HAKit): Home Assistant AP樊客户端, 用于 WebSocket 和 REST APIS 。
- [GRDB.swift 服务器](https://github.com/groue/GRDB.swift): SQLite存储器.
- [你就是阿拉摩火 阿拉摩火](https://github.com/Alamofire/Alamofire): HTTP (韩语).
- [承诺Kit](https://github.com/mxcl/PromiseKit): 旧代码中的许诺. 新代码使用Aync并等待.
- [SFSafe 符号](https://github.com/SFSafeSymbols/SFSafeSymbols):类型安全 SF符号.
- [键链访问](https://github.com/kishikawakatsumi/KeychainAccess): 键链存储 。
- [XCG 标记器](https://github.com/DaveWoodCom/XCGLogger): 记录,通过`Current.Log`.
- [对象Mapper](https://github.com/tristanhimmelman/ObjectMapper):JSON在旧模型中的映射.

## 源文件夹 {#the-source-folders}

| 文件夹 | 里面有什么东西? |
| --- | --- |
| `Sources/App` | iPhone和iPad应用:登机,设置,网页视图,相机,通知,亭模式 |
| `Sources/Shared` | 代码每个目标股份: API 和网络, 数据库, 模型, 传感器, 位置, Assist, 通知, 部件支持 |
| `Sources/Extensions` | 应用程序扩展名:部件、 App Intents、 意图、 共享、 通知服务和内容、 push 提供者和 Matter |
| `Sources/Watch`, `Sources/WatchApp` | 苹果卫视的应用程序及其与手机的通信 |
| `Sources/CarPlay` | CarPlay 模板和行动 |
| `Sources/MacBridge` | 催化剂建筑的Mac 特定代码 |
| `Sources/Thread` | Thread 证书管理和分享 |
| `Sources/Improv` | 在 Bluetooth 上与国际模拟 43. 设置设备 |
| `Sources/PushServer` | 驱动中继服务器, 一个独立的 Swift 包 |
| `Sources/SharedPush` | 分析推进通知有效载荷。 Push 服务器保存自己的副本 |
| `Sources/SharedTesting` | 测试的助手 |
| `Tests` | 单位、用户界面、快照和部件测试 |
| `Configuration` | Xcode 构建设置 |
| `fastlane` | 快车道 |

该寄存器在[`Sources/`](https://github.com/home-assistant/iOS/tree/main/Sources)中也有较小的模块,比如`HADesignSystem`和`HAModels`.

## 密码去哪里 {#where-code-goes}

一个特征经常出现在比应用程序更多的地方. 实体动作可以在应用程序,部件,手表,快捷键和CarPlay中出现. 在开始前,请决定代码属于何处:

1. `Sources/Shared`中超过一个目标需要的逻辑。
2. 一个表面的代码会进入目标,比如`Sources/Extensions/Widgets`或`Sources/CarPlay`.
3. 大多数特性始于`Sources/App`. 看那里,先看看情况如何
4. 在写入新代码前请查看 `Tests/App` 和 `Tests/Shared` 。

扩展运行有严格的限制,不能使用应用程序所能使用的每个API. 共享代码必须保持安全,以便在扩展中使用.

## 当前环境 {#the-current-environment}

代码库中最重要的模式是Global `Current`,一个 `AppEnvironment`,它持有每个依赖:日期,服务器,日志,数据库等等. 它遵循了来自 Point-Free [怎样控制世界](https://www.pointfree.co/blog/posts/21-how-to-control-the-world) 的"世界"模式.

生产代码从中读出:

```swift
let now = Current.date()
let server = Current.servers.all.first
Current.Log.info("Something happened")
```

测试取代它们所需要的:

```swift
Current.date = { Date(timeIntervalSince1970: 1_000_000) }
Current.servers = FakeServerManager()
```

从不分配到 `Current` 外部测试 。 自定义 SwiftLint 规则失败 CI 。

## 每次修改的规则 {#rules-for-every-change}

这些准则来自项目本身的准则,审查人员将其应用于每个pull request:

- ** 每个文件一个类型**,以该类型命名. 在类型内筑巢的小型私人帮手是唯一的例外.
- ** 每个SwiftUI的视图都有 `#Preview`。 **
- ** 每个屏幕一个标题。 ** 一个以 `AppleLikeListTopRowHeader` 开头的屏幕已经在那页眉中显示其标题, 因此它没有设置 `.navigationTitle` 。 否则两个标题会堆叠成用户卷轴 。
- ** 确认在触发处。 ** 将 `.confirmationDialog` 放在打开它的 `Button` 上, 而不是在 `List` 、 `Section` 或其他容器上 。 对话被束缚在自己的控制之下 所以它不能从一个无关的人身上开火
- ** Beta 仅使用 `Current.isTestFlight`**} 特性, 其它没有: 无构建设置 , `#if` 分支, 或隐藏设置 。 每个 pull request 在门后面放置一个特性的, 都会有第二个, pull request 草稿, 移除门, 将第一个门分支, 并与它相连。 取出Beta的特征是合并
- ** 传感器选择加入。 ** 在用户打开传感器之前,没有报告,应用程序更新从不开始报告新的信息。 现在无法读取的感应器仍然被列出,与状态 `unavailable`. 如果需要许可, 打开它就是要求它。 启用是每个服务器: 一个您添加的服务器, 以没有启用开始 。

## 与 Home Assistant 说话 {#talking-to-home-assistant}

Android App一样,App以两种方式向Home Assistant说话:

- ** 移动应用程序 API.** 在登机时,`HomeAssistantAPI`(在[`Sources/Shared/API/HAAPI.swift`](https://github.com/home-assistant/iOS/blob/main/Sources/Shared/API/HAAPI.swift)中)用`mobile_app`集成登记该应用. 之后,传感器,位置更新和其他设备数据通过webhook返回服务器,通过`WebhookManager`. 应用程序以加密支持进行注册, 而`WebhookPayloadCrypto` 加密有效载荷 。 传感器位于`Sources/Shared/API/Webhook/Sensors`。 所有这一切的服务器侧参见[移动应用程序 API](/companion/mobile-app-api) 。
- ** WebSocket 和 REST APIS **, 通过[HAKIT (韩语)](https://github.com/home-assistant/HAKit), 用于实体状态和行动等。 用于新服务器调用, 有 `async` 和 `await` 。

## 和前端说话 {#talking-to-the-frontend}

网页视图加载Home Assistant前端,并通过外部认证传递访问令牌,因此用户不会两次登录. app和前端在外部总线上交换消息,例如打开本地设置或扫描一个QR代码. 前端部分在[外部认证](/frontend/reference/external-auth)和[外部总线](/frontend/reference/external-bus)中被记录.
