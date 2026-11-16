---
title: 测试 Apple 应用
description: 单位,快照,UI,以及苹果项目中的端到端测试,用Currency,补丁覆盖门进行嘲笑.
sidebarLabel: 测试
order: 5
---



# 测试 Apple 应用 {#testing-the-apple-app}
Apple的应用运行在许多目标上,很多代码被他们共享. 测试保持了共享代码的稳定 同时人们改变上船,部件,通知,手表等等。

## 运行测试 {#run-the-tests}

```bash
bundle exec fastlane test
```

这在 iPhone 模拟器上运行了 `Tests-Unit` 方案, 在 Apple Watch 模拟器上运行了表测试 。 在 Xcode 中,选择 `Tests-Unit` 方案并按 <kbd> 命令</kbd>} <kbd>} U</kbd> 。

## 检测所在 {#where-tests-live}

| 文件夹 | 测试什么 |
| --- | --- |
| `Tests/App` | 应用行为 |
| `Tests/Shared` | 共同逻辑:模型、数据库、传感器、通知和公用事业 |
| `Tests/Widgets` | 部件灼伤 |
| `Tests/WatchAppTests`, `Tests/WatchComplications` | 手表应用及其并发症 |
| `Tests/UI` | 用户界面测试和端到端测试 |
| `Tests/Mocks` | 测试共用的口袋 |

测试镜像`Sources`的结构. 共享的帮助者生活在 `Sources/SharedTesting` 。

## 使用当前 {#mock-with-current}

每个依赖都生活在 [`Current`](/companion/apple/architecture#the-current-environment) 中, 所以一个测试可以取代它设置中所需要的 :

```swift
override func setUp() {
    super.setUp()
    Current.date = { Date(timeIntervalSince1970: 1_000_000) }
    Current.servers = FakeServerManager()
}
```

## 快照测试 {#snapshot-tests}

新的 SwiftUI 视图会获得光和暗模式的快照测试, 来自 `SharedTesting` 的帮助 :

```swift
import SharedTesting

func testMyView() {
    assertLightDarkSnapshots(of: MyView())
}
```

参考图像存在于测试旁边的 `__Snapshots__` 文件夹中 。 如果您有意更改视图, 请在操作前查看更新的图像 。

## 端到端测试 {#end-to-end-test}

{L0推动了对真实的Home Assistant的登机:从欢迎屏幕到前端在外部总线上打开的本地设置屏幕. 它每天晚上在`E2E`工作流程中运行,而不是在pull requests上运行.

它驱动的元素有`AccessibilityIdentifier`在[`Sources/App/Accessibility/`](https://github.com/home-assistant/iOS/tree/main/Sources/App/Accessibility)中的标识符. 在此添加一个大小写, 而不是匹配可见文本, 翻译会中断 。

要自己运行, 请从 `.github/e2e/homeassistant` 开始 Home Assistant 实例( 由 README 解释如何) , 然后 :

```bash
bundle exec fastlane e2e
```

## 推进服务器 {#the-push-server}

`Sources/PushServer` 是一个单独的Swift包,有自己的测试:

```bash
cd Sources/PushServer
swift test
```

## 补丁覆盖 {#patch-coverage}

CI 需要您 pull request 的 pull request 修改 中至少90% 的线由单位测试覆盖 。 下面,**Patch覆盖**检查失败,工作摘要列出没有测试运行的行. 在 pull request 从寄存器本身的分支上,一个bot 也请求更改,一旦有推力清除了栏,则驳回该复核.

只有可执行行数 。 没有建立 `Tests-Unit` 目标的文件, 如只监视或只配置部件的代码, 被跳过, 而 pull request 更改任何无法覆盖的文件 。 当代码真的不能被单位测试时,如UIKit管道,维护者可以解除审查. 解释为什么在pull request描述。

你可以在当地得到同样的号码。 从寄存器的根而不是从 `Sources/PushServer` 运行 :

```bash
bundle exec fastlane test
python3 Tools/xccov_to_lcov.py \
  fastlane/test_output/Tests-Unit.xcresult \
  --lcov fastlane/test_output/coverage.lcov
python3 Tools/diff_coverage.py fastlane/test_output/coverage.lcov \
  --base origin/main
```

## 好习惯 {#good-habits}

- 每个测试一个行为。
- 相对于对时间敏感的测试,决定性测试.
- 当一个变化影响到几个目标时,测试接近共享逻辑.
