---
title: 安卓截图测试
description: 使用 Compose 预览截图测试，确保 Android 应用中的 Compose UI 仅在有意时发生变化。
sidebarLabel: 截图测试
sidebarGroup: 测试
order: 2
source: https://github.com/home-assistant/android/blob/main/.github/workflows/pr.yml
lastVerified: 2026-11-06
---

# 安卓截图测试 {#android-screenshot-tests}

最后验证于 2026-11-06，针对 https://github.com/home-assistant/android/blob/main/.github/workflows/pr.yml.

截图测试将用户界面与存储库中的参考图像进行比较。当渲染的用户界面不再与参考图像匹配时，测试失败，因此每一次用户界面更改都是经过深思熟虑的。它们只测试外观，从不测试逻辑。

当用户界面库更新时，这种测试尤其有用。它们已经在诸如 Wear Compose 之类的库的测试版本中证明了其价值，因为库的变化可能会改变应用的外观。

## 它们的工作原理 {#how-they-work}

该应用使用 [Compose 预览截图测试](https://developer.android.com/studio/preview/compose-screenshot-testing-with-testsuites)，作为 Android Gradle 插件的测试套件。它在 JVM 上渲染可组合项，因此无需模拟器。这使得它们比仪器化测试更快、更便宜。

测试位于每个模块的 `src/screenshotTest` 中。套件只会编译这个源集：它没有变体或构建类型的差异。套件针对每个模块的一个变体运行，参考图像存储在其旁边：

| 模块 | 变体 | 参考图像 |
| --- | --- | --- |
| `:app` | `fullDebug` | `src/screenshotTestDefaultFullDebug/reference` |
| `:common` 和 `:wear` | `debug` | `src/screenshotTestDefaultDebug/reference` |

## 编写截图测试 {#write-a-screenshot-test}

- **渲染真实的可组合项**，而不是简化的副本，在每个重要状态下：加载中、为空、出错，以及在有多个服务器时（当这很重要）。
- **重用你的预览**。使用相同的可组合项和预览注解，这样预览和测试不会分离。
- **覆盖尺寸和主题**：从小屏幕如 Wear OS 手表到大屏幕如电视，支持亮色和暗色模式。使用配置注解设置设备尺寸、主题及其他参数。

## 运行和更新 {#run-and-update}

检查是否没有变化：

```bash
./gradlew \
  testDebugScreenshotTestDefaultTestSuite \
  testFullDebugScreenshotTestDefaultTestSuite
```

第一个任务涵盖 `:common` 和 `:wear`，第二个任务涵盖 `:app`，它有不同版本。Android Studio 在 **Screenshot tests verification** 运行配置中有相同的两个任务。当测试失败时，模块的 `build/reports/tests/<task name>/index.html` 中的报告显示参考图、新图像及它们的差异。

CI 在每次 pull request 上运行相同的验证，在 **Screenshot Tests** 作业中，任何差异都会导致检查失败，直到问题解决。

在有意的 UI 更改之后，更新参考图像：

```bash
./gradlew \
  updateDebugScreenshotTestDefaultTestSuite \
  updateFullDebugScreenshotTestDefaultTestSuite
```

更新后不要立即运行测试任务：它会与您刚生成的来自相同代码的图像进行比较。相反，请查看更新后的图像，并检查只有您想改变的部分发生了变化。在您的 pull request 中解释这些更改。

## 当 CI 与你的机器不一致时 {#when-ci-disagrees-with-your-machine}

渲染在不同的操作系统之间会略有差异，例如抗锯齿处理（参见此 [Google issue](https://issuetracker.google.com/issues/348590914)）。阈值保持尽可能低，以确保真实问题不会被掩盖。这意味着你在本地生成的图像可能会在 CI 上失败。

不要在本地追逐像素差异。如果截图测试失败仅是由于这些差异，维护者会在审查过程中解决。他们可以运行 **Update Screenshots** 工作流 (`updateScreenshot.yml`)，该工作流会在 CI 使用的相同类型主机上重新生成图像，并提交到你的分支。运行它需要对仓库的写入权限，并且仅适用于主仓库中的分支，不适用于 fork。该工作流不会再次启动 pull request 检查：之后推送一个新的提交以触发它们。
