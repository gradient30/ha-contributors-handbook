---
title: 开始使用 Android
description: 安装 Android Studio，分叉并克隆仓库，构建应用，并在模拟器或你的手机上运行它。
sidebarLabel: 开始贡献
sidebarGroup: 开始设置
order: 1
source: https://github.com/home-assistant/android/blob/main/.github/workflows/pr.yml
lastVerified: 2026-11-06
---

# 开始使用 Android {#get-started-with-android}

最后验证于 2026-11-06，依据 https://github.com/home-assistant/android/blob/main/.github/workflows/pr.yml.

Android Studio 是你唯一需要的工具。它包含 Android SDK、模拟器和 JDK。本页面将带你从零到在模拟器上运行应用。

## 1. 安装 Android Studio {#1-install-android-studio}

安装最新稳定版的 [Android Studio](https://developer.android.com/studio)。

该项目还需要 NDK 和 CMake，用于本地唤醒词代码。Android Studio 通常会在第一次 Gradle 同步时安装它们。如果失败，请自行安装：

1. 打开 **设置** > **语言与框架** > **Android SDK** > **SDK 工具**。
2. 选择 **NDK（并行版本）** 和 **CMake**。
3. 安装 [https://github.com/home-assistant/android/blob/main/gradle/libs.versions.toml](`gradle/libs.versions.toml`) 列出的 `androidNdk` 和 `cmake` 版本。

## 2. 分叉、克隆和分支 {#2-fork-clone-and-branch}

1. 在 GitHub 上分叉 [home-assistant/android](https://github.com/home-assistant/android)。不熟悉分叉？GitHub 解释了 [如何分叉一个仓库](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)。
2. 克隆你的分叉，并进入它创建的文件夹：

   ```bash
   git clone https://github.com/<your-github-username>/android.git
   cd android
   ```

   或者在 Android Studio 中，使用 **文件** > **新建** > **从版本控制创建项目**。在项目的文件夹中运行下面的命令。

3. 为你的修改创建一个分支，分支名称应说明你修改的内容：

   ```bash
   git checkout -b fix-sensor-crash
   ```

## 3. 添加 Firebase 配置 {#3-add-a-firebase-configuration}

`full` 版本使用 Firebase 进行推送通知，构建时每个应用模块都需要一个 `google-services.json` 文件。除非你正在处理推送通知，否则请使用仓库中的模拟文件。在 `android` 文件夹中运行以下命令：

```bash
cp .github/mock-google-services.json app/google-services.json
cp .github/mock-google-services.json automotive/google-services.json
cp .github/mock-google-services.json wear/google-services.json
```

使用模拟文件时，通知仍然可以通过 WebSocket 连接工作，只是无法通过 Firebase。如果你需要真实的推送通知，请参阅 [推送通知](/companion/android/push-notifications)。

## 4. 构建并运行 {#4-build-and-run}

在 Android Studio 中：

1. 打开项目并让 Gradle 同步。
2. 选择 `app` 运行配置以及一个模拟器或已连接的设备。
3. 选择 **运行**。

从终端，将 `JAVA_HOME` 设置为 JDK 21（CI 使用的版本）并运行：

```bash
./gradlew assembleDebug
```

在 Windows 上，使用 `gradlew.bat assembleDebug`。这会构建两个 [flavors](/companion/android/flavors-and-targets) 的调试版本。要在运行中的模拟器或设备上安装 `full` 调试应用：

```bash
./gradlew :app:installFullDebug
```

调试版本有自己的应用 ID，即 `io.homeassistant.companion.android.debug`，因此它会与 Play 商店的应用并存安装。它的图标有红色背景，因此你可以区分两者。

需要签名的发布版本吗？请参见 [自己构建签名发布版本](/companion/android/releases#build-a-signed-release-yourself)。

一旦应用运行，将其连接到 Home Assistant 实例。如果可以，使用测试实例：每次入驻时，应用都会在该服务器上注册一个新设备。

## 方便的命令 {#handy-commands}

这些是你最常用的命令。它们与 CI 执行的命令相同：

```bash
# Format the code, run before every commit {#format-the-code-run-before-every-commit}
./gradlew :build-logic:convention:ktlintFormat ktlintFormat

# Unit tests, or :common:test for one module {#unit-tests-or-commontest-for-one-module}
./gradlew test

# Static analysis {#static-analysis}
./gradlew detektMain :build-logic:convention:detektMain --continue
./gradlew lint --continue

# Screenshot tests, per module {#screenshot-tests-per-module}
./gradlew :app:testFullDebugScreenshotTestDefaultTestSuite
./gradlew :wear:testDebugScreenshotTestDefaultTestSuite
./gradlew :common:testDebugScreenshotTestDefaultTestSuite

# After changing a dependency {#after-changing-a-dependency}
./gradlew alldependencies --write-locks
```

## 测试 pull request 构建 {#test-a-pull-request-build}

你不需要自己构建任何东西就可以尝试别人的修改。CI 为每个 pull request 构建 APK：

1. 在 GitHub 上打开 pull request 并转到 **Checks** 标签。
2. 选择 **Pull Request** 工作流并向下滚动到 **Artifacts**。
3. 下载 **APKs** 工件。你必须登录 GitHub 才能操作。
4. 解压它。里面包含手机、Wear OS 和 Android Automotive 应用的调试 APK。对于手机，请选择 `full` 或 `minimal` APK。
5. 从手机上的文件管理器安装，或者使用 `adb install path/to/app.apk` 安装。

工件只会在构建作业完成后出现。该作业需要等待锁文件和 KTLint 检查，所以如果其中之一失败，就不会有 APK。

调试 APK 会安装在你常规应用旁边，图标为红色，因此你可以在不破坏现有设置的情况下进行测试。

## AI 工具 {#ai-tools}

该仓库有关于 `AGENTS.md` AI 编码工具的说明，以及 [`.agents/skills/`](https://github.com/home-assistant/android/tree/main/.agents/skills) 的技能，如 `ha-android-architecture`、`ha-android-testing` 和 `ha-android-review`。pull request 模板会询问你是否使用了 AI，以及如何使用的。[使用 AI 工具做出贡献](/start/ai-tools) 列出了每项技能，并解释了 [AI 政策](/start/ai-policy) 对你的要求。

## 下一步 {#what-is-next}

- 阅读 [架构](/companion/android/architecture) 以了解代码结构。
- 查看 [开发者游乐场](/companion/android/debugging#the-developer-playground)，这是一个仅用于调试的快速尝试界面。
- 遇到问题？在 Discord 的 [Android 项目讨论串](https://discord.com/channels/330944238910963714/1346948551892009101) 中提问。
