---
title: Android 版本
description: Android 应用的更改如何从合并的 pull request 传递到内部测试人员、测试版和正式版，以及如何自己构建签名版本。
sidebarLabel: 发布
sidebarGroup: 船
order: 3
source: https://github.com/home-assistant/android/tree/main/.github/workflows
lastVerified: 2026-10-14
---

# Android 版本 {#android-releases}

最后验证于 2026-10-14，对照 https://github.com/home-assistant/android/tree/main/.github/workflows.

每个合并的 pull request 都会立即发送给内部测试人员。每周，最新的构建版本会发送到公开测试版。当测试版稳定时，维护者会将其提升到生产环境。本页介绍了该流程，以及如何在自己的机器上构建已签名的发布版本。

## 从合并到生产 {#from-merge-to-production}

### 内部测试 {#internal-testing}

当一个 pull request 被合并到 `main` 时，CI 会构建发布版本并发布到 Play 商店的内部测试渠道。内部测试人员会立即收到每个更改。应用功能繁多，所以他们无法在每次构建中测试每个功能。

`main` 上每次提交的 APK 也会附加到 [Push 工作流运行](https://github.com/home-assistant/android/actions/workflows/onPush.yml)

### 每周测试版 {#weekly-beta}

每周日 04:00 UTC（美洲为周六晚），CI 会标记一个新版本，创建带有 APK 的 GitHub 预发布版本，并将最新的 `main` 构建版本提升到公开测试版。在截止时间之前，`ChangelogContent.kt` 内的应用内更新日志应列出本周的新功能和不兼容更改。

任何人都可以 [在 Google Play 上加入测试版](https://play.google.com/apps/testing/io.homeassistant.companion.android)。测试版用户会发现测试和内部测试人员无法发现的问题。

Google 会审核所有进入公开测试版的构建。审核所需时间各不相同，可能超过一周。当下一次每周测试版到来时，如果上一版仍在审核中，上一版将被放弃。这不会阻碍任何事情，但当你想知道测试版为什么延迟时，这一点值得了解。

### 推向生产环境 {#promoting-to-production}

维护者在测试版稳定后，将其推向生产环境，并使所有从 [Google Play](https://play.google.com/store/apps/details?id=io.homeassistant.companion.android) 安装应用的用户都能使用。

在推向生产环境之前：

- 在测试版发布后等待几天，让测试用户能够发现回归问题。
- 检查 [`app/src/main/kotlin/io/homeassistant/companion/android/changelog/ChangelogContent.kt`](https://github.com/home-assistant/android/blob/main/app/src/main/kotlin/io/homeassistant/companion/android/changelog/ChangelogContent.kt) 中的应用内更新日志是否涵盖了本次发布的内容。
- 在 Sentry 中检查测试版是否出现异常数量的问题。
- 检查 [Google Play Console](https://play.google.com/console) 中的崩溃、ANR（应用无响应）和其他异常情况。
- 在 [配套文档](https://github.com/home-assistant/companion.home-assistant) 中准备 pull request，移除此版本中功能的测试版标签。

推向生产环境步骤：1. 编辑 [GitHub](https://github.com/home-assistant/android/releases) 上的最新测试版发布。保留生成的提交列表，并在顶部添加一个 **本次发布亮点** 部分，与 `ChangelogContent.kt` 匹配。示例请参见 [2026.6.1](https://github.com/home-assistant/android/releases/tag/2026.6.1)。
2. 清除 **预发布** 复选框，并将其设置为 **最新** 发布。

这会启动 `release.yml`，它使用 Fastlane 将测试版渠道推广到手机、Wear OS 和汽车应用的生产版。Google 会先审核发布，通常需要几天时间。在审核期间无需进行任何操作。

### 其他商店 {#other-stores}

Play 商店只涵盖 `full` 版本。发布之后：

- 将 `minimal` 汽车应用发送到 Harman Ignite 商店。
- 在 [Amazon 开发者控制台](https://developer.amazon.com/apps-and-games/console/apps/list.html) 提交发布审核。APK 和更新日志已经在 beta 构建时通过 `prep_amazon` Fastlane lane 在 `onPush.yml` 上传。
- 在 Meta Quest 商店发布 `minimal` 应用。
- F-Droid 会在几天后自行构建发布。参见 [F-Droid](/companion/android/ci#f-droid)。

### 一旦上线 {#once-it-is-live}

- 合并删除 beta 标签的 pull request 文档。
- 如果本次发布修复了自上一次正式发布以来的安全问题，请在 GitHub 发布说明中增加一个 **已披露的安全公告** 部分，位于亮点之后，并附上每个公告的链接。
- 对于重大变更或重要新功能的发布，请请社区经理帮助推广，例如通过博客文章或社交媒体。

## 自行构建签名版本 {#build-a-signed-release-yourself}

只有在发布自己的构建版本时才需要此操作。发布版本必须签名。

> [!WARNING]
> 请妥善保管您的密钥库及其密码，切勿将其提交到版本控制系统。

1. 在 Android Studio 中通过 **Build** > **Generate Signed App Bundle or APK** 创建一个密钥库，或者使用现有的密钥库。记住密码和密钥别名。
2. 将其命名为 `release_keystore.keystore` 并放在你构建的每个应用模块中：[`app/`](https://github.com/home-assistant/android/tree/main/app)、[`wear/`](https://github.com/home-assistant/android/tree/main/wear) 或 [`automotive/`](https://github.com/home-assistant/android/tree/main/automotive)。或者将 `KEYSTORE_PATH` 设置为其位置。
3. 设置签名变量：
   - `KEYSTORE_PASSWORD`
   - `KEYSTORE_ALIAS`
   - `KEYSTORE_ALIAS_PASSWORD`
   - `KEYSTORE_PATH` ，如果密钥库在其他位置

   读取这些变量的签名配置位于 [`build-logic/convention/src/main/kotlin/AndroidApplicationConventionPlugin.kt`](https://github.com/home-assistant/android/blob/main/build-logic/convention/src/main/kotlin/AndroidApplicationConventionPlugin.kt)。
4. 构建 APK 或应用包，可针对所有应用或单个模块：

```bash
# APKs {#apks}
./gradlew assembleRelease
./gradlew :app:assembleRelease

# App bundles {#app-bundles}
./gradlew bundleRelease
./gradlew :wear:bundleRelease
```你也可以通过 Android Studio 构建，选择 **构建** > **生成已签名的应用包或 APK**。
