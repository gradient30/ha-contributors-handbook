---
title: Apple 持续集成
description: GitHub苹果项目的动作工作流程. 您的pull request 合并后的运行, 以及时间表 。
sidebarLabel: 持续集成
order: 7
source: https://github.com/home-assistant/iOS/tree/main/.github/workflows
lastVerified: 2026-10-14
---



# Apple 持续集成 {#apple-continuous-integration}
最后一次验证是在2026-10-14,对https://github.com/home-assistant/iOS/tree/main/.github/workflows.

苹果项目使用 GitHub 与Fastlane一起行动,进行衬垫、测试、建造、翻译和分发。 CI检查的不仅仅是代码是否编译:样式,字符串和覆盖也是审查的一部分.

## 在您的 pull request 上 {#on-your-pull-request}

`ci.yml` 工作流程运行在每 pull request 和每推到`main` 。

**Lint**运行在Linux上,因此速度很快:Yamllint,RuboCop,SwiftLint,以及SwiftFormat. 见[代码样式](/companion/apple/code-style).

** Test** 运行于macOS上,带有目前的X码. 它解决了Swift软件包并运行`bundle exec fastlane test`. 它上传:

- 代码覆盖。
- 测试结果和日志.
- 一个模拟器构建的应用程序, `ios-simulator`, 您可以使用到[测试前端更改](/companion/apple/get-started#only-testing-the-frontend) 而无需构建该应用程序 。

**荫影覆盖**检查你所改变的线路至少有90%被测试覆盖. 见[补丁覆盖](/companion/apple/testing#patch-coverage).

再来两张支票 看看你的车 在{在国家资料库本身的分支上,当发现侥幸之处时会留下一个注释:

- 您的 diff 中的新 `swiftlint:disable` 。
- 不再使用的本地化字符串, 由 [`Tools/detect_unused_strings.py`](https://github.com/home-assistant/iOS/blob/main/Tools/detect_unused_strings.py) 找到 。 注释列出密钥, 准备为 QQH0} : 删除密钥** 工作流程, 从 Lokalise 中删除这些密钥, 并打开 pull request 从应用程序中删除这些密钥 。

## 其他工作流程 {#other-workflows}

| 工作流程 | 成为一种运行 | 对 |
| --- | --- | --- |
| `distribute.yml` | 每次推到`main`时,或由维护者手工操作 | 构建并签名iOS和Mac应用程序,并上传至App Store Connect. 见[释放](/companion/apple/releases) |
| `tag_macos_release.yml`, `release_macos.yml` | 手动, 或在 `release/*/*` 标签上 | 以 GitHub 发布 Mac 构建 |
| `e2e.yml` | 每日协调时间05:00,或人工操作 | 运行 [端到端测试](/companion/apple/testing#end-to-end-test) 对一个真实的 Home Assistant |
| `push_ci.yml` | 更改为 `Sources/PushServer` | 驱动服务器运行 `swift test` |
| `push_deploy.yml` | 手动 | 构建驱动服务器图像并将其发布到 GitHub 集装箱登记 |
| `download_localized_strings.yml` | 每天协调世界时06:00,或人工操作 | 上传新字符串到 Lokalise,下载翻译,并打开 pull request |
| `delete_lokalise_keys.yml`, `auto_delete_unused_strings.yml` | 手动 | 从 Lokalise 励志程序中删除未使用的字符串 |
| `update_frontend_colors.yml`, `update_brand_icons.yml`, `update_material_design_icons.yml` | 每周或手动 | 重新生成前端颜色、品牌图标和材料设计图标,并打开 pull request 当它们改变时 |
| `set_version.yml` | 手动 | 更新 [`Configuration/Version.xcconfig`](https://github.com/home-assistant/iOS/blob/main/Configuration/Version.xcconfig) 中的版本并打开 pull request |

macOS跑者没有Docker,所以端到端的测试用pip安装Home Assistant,在跑者身上的虚拟环境中. 默认情况下,它会从它的`dev`分支安装Core. 手动运行可以从PyPI中选择最新的发行版本或特定版本代替.
