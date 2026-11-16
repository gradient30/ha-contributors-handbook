---
title: Android 持续集成
description: Android 应用的 GitHub 操作工作流。在您的 pull request 上运行、合并后运行以及按计划运行。
sidebarLabel: 持续集成
sidebarGroup: 发布上线
order: 2
source: https://github.com/home-assistant/android/tree/main/.github/workflows
lastVerified: 2026-10-27
---

# Android 持续集成 {#android-continuous-integration}

最后验证于2026-10-27，针对https://github.com/home-assistant/android/tree/main/.github/workflows.

Android 应用使用 GitHub Actions 来处理所有事情：检查 pull request、构建发布版本，以及通过 [Fastlane](https://fastlane.tools/) 将其发布到商店。共享步骤作为本地操作存放在 `.github/actions` 中。

该应用使用 [日历版本控制](https://calver.org/)，类似于 Home Assistant Core：`YYYY.MM.patch`。

## 工作流程| 工作流 | 运行 | 执行 | {#the-workflows}
| --- | --- | --- |
| `pr.yml` | 每次 pull request 时 | 代码检查、构建、测试，并附加 APK |
| `pr-emulator-wtf.yml` | 在 `pr.yml` 完成后 | 在 Emulator.wtf 上运行 `:app` 仪器测试 |
| `zizmor.yml` | 每次 pull request，以及每周一 05:30 UTC | 使用 [zizmor](https://docs.zizmor.sh/) 扫描工作流和本地操作，并将结果上传到代码扫描 |
| `onPush.yml` | 每次推送到 `main` 时 | 构建发布版本并发布到 Play 商店的内部通道 |
| `weekly.yml` | 每周日 04:00 UTC | 给新版本打标签并使用 `beta` 标志运行 `onPush.yml`，这将创建 GitHub 预发布并将构建升级到测试版通道 || `e2e.yml` | 每天 05:00 UTC | 对真实的 Home Assistant 运行 [端到端测试](/companion/android/e2e-testing)。当测试失败时，会启动 `e2e-triage`，这是一个自主工作流程，会调查失败原因并在 issue 中报告 |
| `monthly.yml` | 每月的第一天 | 创建本月的第一个版本标签 `YYYY.MM.0` |
| `release.yml` | 当预发布版本变为正式发布版本，或手动操作 | 将 beta 版本推广到 Play 商店生产环境 |
| `updateScreenshot.yml` | 由维护人员手动操作 | 重新生成 [截图](/companion/android/screenshot-testing) 引用 |
| `renovate-lockfiles.yml` | 每次推送到 `renovate/` 分支时 | 更新 Renovate pull request 的 [锁定文件](/companion/android/dependencies) 并推送 |

## 关于你的 pull request {#on-your-pull-request}

`pr.yml` 检查你的更改：- KTLint、Detekt、Android Lint 和 Yamllint。请参见 [代码风格与 lint 检查](/companion/android/code-style)。
- lockfiles 是否与版本目录匹配。
- 所有依赖项的许可证是否与项目的 Apache 2.0 许可证兼容，[详细信息](https://github.com/home-assistant/android/blob/main/.github/scripts/check_licenses.py)见 [`.github/scripts/check_licenses.py`]。
- 单元测试和截图测试。
- 每个应用程序能否构建成功，包括调试和发布版本。
- `common/schemas` 中现有的数据库模式没有被更改，并且构建不会生成你忘记提交的模式更改。要更改数据库，请增加其版本号。
- 如果你的 pull request 更改了 `.github/actions/download-translations` 中的 Lokalise 设置，确保翻译仍然可以下载。

- `zizmor.yml` 使用 [zizmor](https://docs.zizmor.sh/) 的严格模式扫描每个工作流和本地操作，无论你的 pull request 是否接触它们。生成的 `e2e-triage.lock.yml` 会被跳过，因为它无法手动编辑。任何发现都会导致检查失败，并且这些发现也会作为代码扫描注释显示在你的 pull request 上。请参见 [更改工作流](/companion/android/ci#changing-a-workflow)。
- 它会将 APK 上传为工件，因此任何人都可以 [测试你的更改](/companion/android/get-started#test-a-pull-request-build)。

CI 上的调试构建使用 [`.github/mock-google-services.json`](https://github.com/home-assistant/android/blob/main/.github/mock-google-services.json) 中的模拟 Firebase 文件。

当检查失败时，修复它并推送一个新的提交：这会再次启动工作流。当你快速推送多个提交时，只有最新的提交会被构建。早期的运行会被取消。如果你是新贡献者，维护者必须先批准你在你的 pull request 上的每次 CI 运行。运行 CI 需要消耗大量资源，因此在你的工作准备好让别人查看之前，不要打开 pull request，即使是草稿也不行。你可以随意向你的 fork 推送更新。

### 仪器测试 {#instrumentation-tests}

`:app` 的仪器测试在 [Emulator.wtf](https://emulator.wtf) 上运行，针对从 `androidSdk-min` 到 `androidSdk-target` 的每个 API 级别，以秒为单位。

这需要两个工作流程。`pr.yml` 构建测试 APK 和设备列表。然后 `pr-emulator-wtf.yml` 在 `pr.yml` 完成后触发，运行它们并在 pull request 上报告结果。这种拆分方式使其适用于分支：由分支启动的工作流程无法访问密钥，因此无法访问 Emulator.wtf。第二个工作流程在主仓库的上下文中运行，并且仅运行第一个工作流程构建的 APK，从不运行分支的代码。`:wear`、`:automotive`、`:common` 和 `:microwakeword` 的仪器测试在 GitHub Actions 上的常规 Android 模拟器上运行。Emulator.wtf 仅提供手机、平板和显示器设备，因此这是 Wear OS 和 Automotive 的唯一选择。一个运行器上只能放一个模拟器，因此每个 API 级别和设备配置文件都是单独的作业，并且每个作业比整个 Emulator.wtf 运行要慢得多。这就是这些目标仅覆盖少数几个 API 级别的原因。

## 合并后 {#after-a-merge}

每次向 `main` 的推送都会经过 `onPush.yml`。它会从 Lokalise 下载最新的翻译，生成合并 pull request 的版本说明，构建所有应用的发布版本，将 APK 附加到工作流运行中，并发布到 Play 商店的内部测试渠道。发布所需的签名密钥和其他文件来自存储库机密，仅在运行期间添加。

所有商店部署都通过 [Fastlane](https://fastlane.tools/) 进行。它的配置，包括工作流调用的 lane，位于 `fastlane` 文件夹中。

使用 `beta` 标志运行，`weekly.yml` 每个星期日执行，它还会创建一个带有 APK 的 GitHub 预发布版本，准备亚马逊列表，并将构建升级到 beta 渠道。因此每个合并的 pull request 都会到达内部测试人员。有关到达生产环境的其余步骤，请参见 [releases](/companion/android/releases)。

## 更改工作流程 {#changing-a-workflow}

- 将多个工作流程都需要的步骤放在 `.github/actions` 的本地操作中，而不是复制它们。
- 仔细选择触发器。每次运行都会消耗资源，因此工作流程应该仅在其结果重要时才运行。
- 永远不要在工作流程文件中放置机密。像现有工作流程一样，在运行时从仓库机密中传入它们。
- 让 [zizmor](https://docs.zizmor.sh/) 高兴：为每个作业命名，只赋予所需权限并注明原因，设置 `concurrency` 组，并将操作固定到 commit SHA。
- 使用 `

# zizmor: ignore[rule-name]` 和理由压制标记行的误报，就像 `pr-emulator-wtf.yml` 做的那样。不要忽略整个文件。 {#f-droid}
- 周一的运行还会检查新的安全通告和过时的固定版本，当失败时，会在 `zizmor-failure` 创建或评论相关问题。

## F-Droid {#f-droid}

[F-Droid](https://f-droid.org/packages/io.homeassistant.companion.android.minimal/) 本身会从每个 GitHub 版本构建 `minimal` 应用程序，遵循其 [元数据](https://gitlab.com/fdroid/fdroiddata/-/blob/master/metadata/io.homeassistant.companion.android.minimal.yml)。每个版本有三个文件用于此目的：

- `version_code.txt`：构建的版本代码。
- `strings.zip`：构建时来自 Lokalise 的翻译。
- `locales_config.xml`：从这些翻译生成的 [本地化配置](https://developer.android.com/guide/topics/resources/app-languages#use-localeconfig)。

某个版本何时在 F-Droid 上出现，由 F-Droid 决定。
