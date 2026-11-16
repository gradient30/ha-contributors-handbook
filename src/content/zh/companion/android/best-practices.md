---
title: Android最佳实践
description: 每次 Android 审查中都会出现的编码规则。强类型、时间、并发、依赖注入、日志记录，以及快速失败。
sidebarLabel: 最佳实践
sidebarGroup: 编写代码
order: 2
---

# Android最佳实践 {#android-best-practices}

这些是审核人员在 Android 应用中寻找的做法。大多数归结为一个观点：让编译器和工具捕捉错误，这样人们就不必自己去做。

## 一般原则- **SOLID、KISS 和 DRY。** 常用原则。 {#general-principles}
- **遵循社区准则。** 对于本页面未涵盖的任何内容，[Now in Android](https://github.com/android/nowinandroid) 应用展示了该项目遵循的实践。
- **保持直接。** 不要为单一实现或可能永远不会来的未来添加抽象。直接使用库或 API，只有当出现第二个实际用途或为了在模块外隐藏实现（在`:common`中的公共接口，通过Hilt绑定`internal`实现）时才进行抽象。
- **不要存储可以从现有状态派生的信息。**
- **在修复前找出根本原因。** 一个错误修复应说明实际原因以及如何重现。不要进行修复症状的推测性解决方法。
- **小类，小函数。** 一个难以命名的函数做的事情太多了。

- **组合优于继承。** 从小型、可重用的部分构建行为，而不是深层的类层次结构。
- **持久的注释。** 记录公共函数，在有帮助的地方添加注释，并保持注释与代码同步。问问自己六个月后是否还能理解它。

## 在逻辑中使用强类型 {#use-strong-types-for-logic}

字符串用于显示和来自外部的原始值。不要用它们来控制行为：一个拼写错误会编译通过但在运行时出错。应使用密封类或接口，或者如果必须，可以使用 `enum`。

```kotlin
private const val DESTINATION_KEY = "destination"

@Parcelize
sealed interface Destination : Parcelable {
    data object General : Destination
    data class Notifications(val title: String) : Destination
    data object Privacy : Destination
}

fun newInstance(destination: Destination): Intent =
    Intent().apply { putExtra(DESTINATION_KEY, destination) }
```

密封类型优于枚举：每个情况都可以携带自己的数据，就像上面的 `title`。当你用 `when` 处理它们时，可以省略 `else` 分支：

```kotlin
fun onIntent(intent: Intent) {
    val destination = IntentCompat.getParcelableExtra(
        intent,
        DESTINATION_KEY,
        Destination::class.java,
    )
    when (destination) {
        Destination.General -> showGeneral()
        is Destination.Notifications -> showNotifications(destination.title)
        Destination.Privacy -> showPrivacy()
        null -> showDefault()
    }
}
```

这样在添加新情况时，会使未处理的地方编译失败，这正是你想要的。你的 IDE 也可以找到使用特定目标的每一个地方，而字符串永远做不到这一点。[Kotlin 文档关于密封类](https://kotlinlang.org/docs/sealed-classes.html) 有详细说明。

如果必须使用字符串，请将其做为 `const val`（参见 [不要使用魔法数字或字符串](/companion/android/code-style#no-magic-numbers-or-strings)），或者将其封装在 [内联值类](https://kotlinlang.org/docs/inline-classes.html) 中。

## 对时间使用真实类型 {#use-real-types-for-time}

永远不要对时间或持续时间使用简单数字。单位会混淆。使用 `Instant`、`Duration` 及其相关类型，并尽早将从 API 返回的毫秒值进行转换：

```kotlin
// Bad: seconds or milliseconds?
const val THRESHOLD = 600000

// Good
val THRESHOLD = 10.minutes
```

永远不要调用 `System.currentTimeMillis()`。通过 Hilt 注入 `kotlin.time.Clock`，这样测试就可以控制时间。如果你真的需要使用原始类型，请在名称中注明单位：`THRESHOLD_MS`。

## 不可变性 {#immutability}

优先使用不可变的数据类，并通过 `copy()` 或返回新实例的函数来产生更改。默认使用 `private` 或 `internal` 可见性。

## 并发 {#concurrency}

- 将协程绑定到生命周期，例如 `viewModelScope` 或 `lifecycleScope`，以防止泄漏。
- 任何被多个协程访问的内容必须是线程安全的。如果不是，要么使其安全，要么不要共享它。
- 竞态条件非常难以调试。提前为其设计方案。

## 依赖注入 {#dependency-injection}

所有可以注入的内容都通过 [Hilt](https://developer.android.com/training/dependency-injection/hilt-android) 提供。永远不要手动创建注入类。

当你需要相同类型的两个绑定时，使用自定义限定符注解，而不是 `@Named("...")`。自定义注解可以进行类型检查，容易找到，并且安全重命名。`NoNamedAnnotation` Lint 规则会在 `@Named` 时使构建失败：

```kotlin
@Qualifier
@Retention(AnnotationRetention.RUNTIME)
annotation class NamedKeyChain

@Inject
@NamedKeyChain
lateinit var keyChainRepository: KeyChainRepository
```

[pull request #5667](https://github.com/home-assistant/android/pull/5667) 展示了从 `@Named("keyChainRepository")` 到 `@NamedKeyChain` 的实际迁移。

## 日志记录 {#logging}

使用 [Timber](https://github.com/JakeWharton/timber)，不要使用 `android.util.Log`。在 `Log` 调用上 linter 会使构建失败。记录有助于调试问题的信息，而不是所有信息，并且使用说明发生了什么错误以及原因的消息。绝不要记录令牌、密码或其他敏感数据。对于在调试构建中有助于调试的用户数据，将其包装在 `sensitive()` 中，这将在调试构建中显示，而在发布构建中隐藏。

## 快速失败 {#fail-fast}

你越晚发现一个漏洞，修复就越困难。尽可能在构建时捕获错误：使用具有详尽`when`的密封类型，以及在编译器无法强制执行时的[lint 规则](/companion/android/code-style#custom-lint-rules)。当同样的意见在代码审查中反复出现时，把它变成工具，而不是依赖记忆：自定义 lint 规则、KTLint 覆盖、`FailFast` 检查或测试监听器。

不要吞掉异常。至少要记录它们。更好的是：使用 `FailFast`。它会记录错误，在调试构建中崩溃以便你注意到，并在发布构建中退回到安全值：

```kotlin
import io.homeassistant.companion.android.common.util.FailFast

val value = FailFast.failOnCatch(
    message = { "Couldn't read value, state: ${api.state()}" },
    fallback = "fallback",
) {
    api.value()
}
```

当 `FailFast` 触发时，Logcat 会显示来自 `CrashFailFastHandler` 的大型 `CRITICAL FAILURE: FAIL-FAST` 横幅，然后是你的消息和堆栈跟踪，很难错过。

## 通过小步骤推送重大变更 {#ship-big-changes-in-small-steps}

小的pull request可以更快地被审查。将一个大变更拆分成每一步都能保持应用正常工作的步骤。如果一次小的pull request无法完成重做，可以在`WIPFeature`对象中通过标志放置新路径，通常通过`BuildConfig.DEBUG`仅在调试版本中启用。在用户仍在使用旧路径时合并这些步骤，功能完成后移除该标志。有关其他内容，请参见[提交pull request](/companion/android/submitting)。
