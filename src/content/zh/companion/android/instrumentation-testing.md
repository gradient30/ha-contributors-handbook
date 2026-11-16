---
title: Android 仪器测试
description: 在真实的 Android 运行环境中测试 Android 应用程序，并在每个支持的 API 级别的模拟器上进行测试。
sidebarLabel: 仪器测试
sidebarGroup: 测试
order: 3
---

# Android 仪器测试 {#android-instrumentation-tests}

单元测试在你的 JVM 上运行。用户在 Android 上运行应用，而 Android 有[自己的运行时](https://source.android.com/docs/core/runtime)，并且在较老的版本上只支持部分[Java 语言特性和 API](https://developer.android.com/studio/write/java8-support)。仪器测试可以弥补这一差距：它们在模拟器上运行，使用与用户相同的运行时环境。

先编写单元测试。当行为依赖于真实的 Android 系统时，再考虑使用仪器测试。

## 为什么它们很重要 {#why-they-matter}

有些错误只有在特定 Android 版本的运行时才会出现。[Jackson](https://github.com/FasterXML/jackson) 库就是一个真实例子：从 2.14 版本开始，它需要 API 26，而且直到应用在较老设备上运行之前不会出现任何问题。只有仪器测试或者用户的崩溃报告才能发现这一问题。请参见[这个 pull request](https://github.com/home-assistant/android/pull/5108)了解事情的经过。

## 它们涵盖的内容 {#what-they-cover}

- **屏幕**，使用 [Espresso](https://developer.android.com/training/testing/espresso) 和 Compose UI 测试，检查当用户与屏幕交互时屏幕的表现。
- **无 UI 的代码**，例如 [前台服务](https://developer.android.com/develop/background-work/services/fgs)，检查数据和与系统的交互。

大多数这些测试不应依赖 Home Assistant 服务器。用伪造的对象或 [MockK](https://mockk.io/) 的模拟替代服务器。伪造对象是更好的选择：它们让你对行为有更多控制。针对真实服务器的测试则属于 [端到端测试](/companion/android/e2e-testing) 的范围。

## 他们运行的位置 {#where-they-run}

在每个 pull request 上，`:app` 的仪器测试在 [Emulator.wtf](https://emulator.wtf) 上运行，针对从 `androidSdk-min` 到 `androidSdk-target` 的每个 API 级别。整个运行只需几秒钟。有关如何在分支中使用的详情，请参见 [持续集成](/companion/android/ci#instrumentation-tests)。

`:wear`、`:automotive`、`:common` 和 `:microwakeword` 的测试在常规 Android 模拟器上运行，在 GitHub Actions 上执行，因为 Emulator.wtf 不提供这些目标。这会更慢，因此覆盖的 API 级别较少。

## 使用过时 WebView 的模拟器 {#emulators-with-an-outdated-webview}

该应用在 WebView 中显示 Home Assistant 前端。模拟器系统镜像附带的 WebView 是镜像发布时的最新版本。API 级别越低，WebView 越旧。

当 WebView 对于你运行的前端来说过旧时，前端无法渲染，或者 WebView 崩溃。你最有可能在应用支持的最老 API 级别上遇到此问题。

如何更新 WebView 取决于系统镜像：- 含有 Google Play 的镜像包括 [Play 商店应用](https://developer.android.com/studio/run/managing-avds)。在那里登录并更新 WebView，就像在真实设备上一样。Android 9 及更早版本仅能获得针对这些版本的 [最后的 WebView 发行版](https://chromium.googlesource.com/chromium/src/+/HEAD/android_webview/docs/prerelease.md)，因此在这些 API 级别上，更新可能不够。
- 不含 Play 商店的镜像，如 Google APIs 和 AOSP 镜像，需要手动安装更新的 WebView APK。[这个 Stack Overflow 答案](https://stackoverflow.com/a/79514205/3289338) 展示了如何操作，其中的脚本是为 API 21 模拟器编写的。它需要模拟器处于可写模式，并且你需要调整脚本中的变量以匹配你的模拟器。

如果你运行自己的 [前端开发服务器](/frontend/development/run)，你也可以使用 `ES5=1` 启动它。此时它还会构建前端的传统版本，较旧的 WebView 可以运行它：

```shell
ES5=1 pnpm dev
```

## 不稳定的模拟器 {#flaky-emulators}

Android 模拟器有时会无缘无故地失败。解决方法是再次运行该任务。只有维护者可以重新运行任务，所以如果你认为这是偶发情况，请在 pull request 中询问。
