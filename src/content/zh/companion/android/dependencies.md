---
title: Android 依赖项
description: Android 应用中的版本目录、依赖锁文件和 Renovate。
sidebarLabel: 依赖
sidebarGroup: 编写代码
order: 4
source: https://github.com/home-assistant/android/blob/main/.github/workflows/renovate-lockfiles.yml
lastVerified: 2026-10-14
---

# Android 依赖项 {#android-dependencies}

最后验证时间为 2026-10-14，依据 https://github.com/home-assistant/android/blob/main/.github/workflows/renovate-lockfiles.yml.

Android 应用程序对其依赖项进行严格控制。每个库都在一个地方声明，每个解析的版本都被锁定，并且有一个机器人保持它们的最新状态。

## 版本目录 {#the-version-catalog}

所有依赖项都在 [版本目录](https://docs.gradle.org/current/userguide/version_catalogs.html) 中声明，[`gradle/libs.versions.toml`](https://github.com/home-assistant/android/blob/main/gradle/libs.versions.toml)。这是添加依赖项的唯一方式：在目录之外声明的依赖项不会被接受。通过在一个地方集中管理所有版本，每个模块使用相同版本的共享库，更新会在整个项目中统一进行。模块通过 `libs` 访问器引用它：

```kotlin
dependencies {
    implementation(libs.kotlinx.coroutines.android)
}
```

## 锁文件 {#lockfiles}

该项目使用 Gradle [依赖锁定](https://docs.gradle.org/current/userguide/dependency_locking.html)。每个模块都有一个 `gradle.lockfile`，记录了每个直接和传递依赖的准确版本，因此每台机器上的构建都是相同的，而且传递依赖不会在无人注意的情况下发生变化。

在你添加或更改目录中的任何内容后，需要更新锁文件并提交它们：

```bash
./gradlew alldependencies --write-locks
```

当目录发生变化但锁文件没有更新时，CI 会失败。

## Renovate {#renovate}

[Renovate](https://docs.renovatebot.com/) 会打开 pull request 来更新在 `renovate.json5` 中配置的依赖项。它会在发布后三天才提出更新，以便其他人先发现早期问题。相关的库，例如 AndroidX 或 Kotlin 库，会被分组到同一个 pull request 中。

Renovate 本身不会修改锁文件。`Auto-update Renovate lockfiles` 工作流 ([`.github/workflows/renovate-lockfiles.yml`](https://github.com/home-assistant/android/blob/main/.github/workflows/renovate-lockfiles.yml)) 会在每个 Renovate 分支上运行，更新锁文件，并将其推送到同一个分支。

## 仅稳定版本 {#stable-versions-only}

项目避免使用库的 alpha、beta 和候选发布版本。例外情况会在 pull request 中达成一致，当某个特性仅在预发布版本中可用时使用。它们有一个代价：每次更新都可能改变 API，必须有人来处理这些改变。
