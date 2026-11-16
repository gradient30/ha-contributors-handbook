---
title: 安卓调试工具
description: Android 应用调试版本中的开发者游乐场、Compose 目录、StrictMode 和 LeakCanary。
sidebarLabel: 调试工具
sidebarGroup: 编写代码
order: 5
---

# 安卓调试工具 {#android-debug-tools}

Android 应用的调试版本附带一些工具，可以加快开发速度并及早发现问题。这些工具在发布版本中都没有。

## 开发者操场 {#the-developer-playground}

该应用依赖于服务器和网页视图，因此尝试某些功能通常意味着需要先完成引导和几个界面。开发者操场可以跳过这些步骤。它是在调试版本中的一个[应用快捷方式](https://developer.android.com/develop/ui/views/launch/shortcuts/creating-shortcuts#static)：长按应用图标并选择 **DevPlayground**。在 Android Studio 中，`dev playground` 运行配置可以直接打开它。它的代码位于 `app/src/debug` 源集里，因此永远不会出现在发布版本中。

通过操场，你可以执行诸如故意让应用崩溃或触发快速失败、启动 NFC 标签模拟器，以及打开所有 `HA*` 组件的 [Compose 目录](/companion/android/compose#the-compose-catalog) 等操作。随意使用游乐场。只提交对其他开发者也有帮助的更改，例如用于测试崩溃报告的崩溃按钮，或显示所有组件和主题的目录。提交的游乐场代码遵循[代码风格](/companion/android/code-style)和[最佳实践](/companion/android/best-practices)，就像其他代码一样。那里不需要翻译。

## 严格模式 {#strictmode}

[StrictMode](https://developer.android.com/reference/android/os/StrictMode) 在调试构建中开启，在运行 Android 12 或更新版本的设备上也会开启。它会捕获主线程上的磁盘和网络访问，以及新版本 Android 弃用的行为，这使得升级到新的 Android API 级别更加容易。

任何违反 [VM 策略](https://developer.android.com/reference/android/os/StrictMode.VmPolicy.Builder) 或 [线程策略](https://developer.android.com/reference/android/os/StrictMode.ThreadPolicy.Builder) 的行为都会被记录到 `FailFast`，因此调试构建会因为它而崩溃。来自项目无法控制的代码（如 WebView 或供应商框架）的已知违规行为，会通过 [`app/src/main/kotlin/io/homeassistant/companion/android/util/IgnoreViolationRules.kt`](https://github.com/home-assistant/android/blob/main/app/src/main/kotlin/io/homeassistant/companion/android/util/IgnoreViolationRules.kt) 中的规则被忽略。

如果严格模式阻止了你，可以在构建中将其关闭：

```bash
./gradlew :app:assembleFullDebug -PnoStrictMode
```

或者在 `gradle.properties` 中取消注释 `noStrictMode=true`。如果你不得不关闭它，请开一个 issue 或在 [Discord](https://www.home-assistant.io/join-chat/) 上提及，这样底层问题才能得到修复。

## LeakCanary {#leakcanary}

[LeakCanary](https://square.github.io/leakcanary/) 包含在调试版本中，会在你工作时报告内存泄漏，这样你可以尽早修复它们。如果它报告了一个问题，请提出问题。如果泄漏来自库且暂时无法修复，请进行记录。

例如，要在不使用它的情况下构建以进行性能测试：

```bash
./gradlew :app:assembleFullDebug -PnoLeakCanary
```

或者在 `gradle.properties` 中设置 `noLeakCanary=true`，在项目中或在你的 Gradle 用户主目录中。

> [!WARNING]
> 如果没有 LeakCanary，解析的依赖项会改变，Gradle 会对锁文件提出警告。按 [dependencies](/companion/android/dependencies#lockfiles) 中的说明在本地更新锁文件，但不要提交这些更改。pull request 上的锁文件检查会使用包含 LeakCanary 的配置重新生成锁文件，并在它们与你提交的内容不同的时候失败。

## FailFast {#failfast}

`FailFast` 会在捕获到发布版本可以静默处理的错误时使调试版本崩溃。日志显示带有堆栈跟踪的大型 `CRITICAL FAILURE: FAIL-FAST` 横幅。参见 [快速失败](/companion/android/best-practices#fail-fast)。
