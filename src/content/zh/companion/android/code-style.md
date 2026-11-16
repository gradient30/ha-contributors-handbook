---
title: Android 代码风格和代码检查
description: 在 Android 应用中使用 KTLint、Detekt、Android linter 和 Yamllint。如何运行它们、抑制问题以及使用基线。
sidebarLabel: 代码风格和代码检查
sidebarGroup: 写代码
order: 3
---

# Android 代码风格和代码检查 {#android-code-style-and-linting}

Android 应用程序使用工具强制执行其代码风格，因此审查可以关注逻辑而不是格式。CI 在你的 pull request 上运行每一个工具，并将发现以差异评论的形式报告。

## 工具 {#the-tools}

| 工具 | 检查内容 | 配置于 |
| --- | --- | --- |
| [KTLint](https://pinterest.github.io/ktlint) | Kotlin 格式 | `.editorconfig` |
| [Detekt](https://detekt.dev/) | 可维护性和正确性 | [`.detekt/detekt.yml`](https://github.com/home-assistant/android/blob/main/.detekt/detekt.yml) |
| Android Lint | Android API 使用和项目规则 | [`build-logic/convention/src/main/kotlin/AndroidCommonConventionPlugin.kt`](https://github.com/home-assistant/android/blob/main/build-logic/convention/src/main/kotlin/AndroidCommonConventionPlugin.kt) |
| [Yamllint](https://github.com/adrienverge/yamllint) | YAML 文件 | `.yamllint` |

通过所有这些工具并不意味着代码很好。这意味着审查者可以专注于重要的内容。

## 运行它们 {#run-them}

```bash
# Format Kotlin, run before every commit {#format-kotlin-run-before-every-commit}
./gradlew :build-logic:convention:ktlintFormat ktlintFormat

# Check formatting without changing files {#check-formatting-without-changing-files}
./gradlew ktlintCheck :build-logic:convention:ktlintCheck --continue

# Detekt, with type resolution, as CI runs it {#detekt-with-type-resolution-as-ci-runs-it}
./gradlew detektMain :build-logic:convention:detektMain --continue

# Android Lint {#android-lint}
./gradlew lint --continue

# YAML {#yaml}
yamllint --strict --format github .
```

`--continue` 报告每个模块的问题，而不是在第一个失败处停止。`build-logic` 是一个包含的构建，因此其任务需要显式调用。对于一个模块，使用模块路径，例如 `./gradlew :app:detektMain`。

要在每次提交前运行 KTLint 检查，请安装 git 钩子一次：

```bash
./gradlew addKtlintCheckGitPreCommitHook
```

Yamllint 不会修复任何问题；请自己修复它报告的问题。

## Android Lint 设置 {#android-lint-settings}

Android Lint 很严格：警告即为错误，且构建会在任何不在基线中的问题上失败。有一些规则是有意调整的：

- `LogNotTimber` 是错误，所以所有日志都通过 Timber。
- `MissingTranslation` 已关闭，因为翻译只会从 Lokalise 到达发布版本。
- 依赖版本检查已关闭，因为 Renovate 负责处理更新。

## 抑制问题 {#suppressing-an-issue}

尽可能修复问题，而不是抑制它们。当无法修复时：

- 对于一个地方，尽量在最小的结构上使用 `@Suppress("rule-id")`。
- 对于 Android Lint，一个问题也可以放在模块的 `lint-baseline.xml` 中，如 [baselines](/companion/android/code-style#baselines) 所述。
- 要更改整个项目的规则，请打开一个专门的 pull request 来解释原因。对于 Android Lint，请更改 `AndroidCommonConventionPlugin.kt` 中的 `lint` 块。对于 KTLint，更改 `.editorconfig` 并在规则上方添加备注，说明原因，如果需要更多解释，可附上 GitHub 问题的链接。如果更改涉及代码，请使用两个提交：一个用于规则，一个用于它所更改的代码。

## 基线 {#baselines}

模块有包含在启用工具之前存在的问题的基线文件：

- Android Lint 的 `lint-baseline.xml`。
- Detekt 的 `detekt-baseline-*.xml`。Android 模块每个变体有一个，如 `detekt-baseline-release.xml`；JVM 模块有 `detekt-baseline-main.xml`。

新的问题会导致持续集成失败。基线问题不会。

> [!TIP]
> 修复基线中的问题并从文件中删除它，是一个很好的首次贡献。

当 Android Gradle 插件或 Detekt 的更新更改了规则时，重新生成基线并查看有什么变化：

```bash
./gradlew updateLintBaseline
./gradlew detektBaselineMain :build-logic:convention:detektBaselineMain \
  --continue
```

然后检查新的条目。在同一个 pull request 中修复你能修复的，对于必须等待的问题则创建一个 issue。

## 自定义 lint 规则 {#custom-lint-rules}

`:lint` 模块有项目自己的 lint 规则。它们会检查一些内容，比如 Kotlinx.serialization 缺少 `@Serializable` 注解、Room 实体上的可变属性，以及 `evaluateJavascript` 的使用。如果你在审查中不断看到相同的错误，请提出一条规则。

## CI 中的 SARIF 报告 {#sarif-reports-in-ci}

代码分析器会生成 SARIF 报告，GitHub 会将其显示为你 pull request 上的注释。每个模块都会生成自己的报告，而 GitHub 每次运行只接受一个报告，因此 CI 会使用 [`.github/scripts/merge_sarif.py`](https://github.com/home-assistant/android/blob/main/.github/scripts/merge_sarif.py) 将它们合并。你本地不需要这个，但你可以在代码分析器运行后执行：`python3 .github/scripts/merge_sarif.py` 会在你运行它的文件夹中写入 `merged_results.sarif`。

## 规范 {#conventions}

工具无法捕捉到所有问题。这些规范同样适用。

### 英文 {#english}

所有代码和注释均使用英文。可能会有拼写错误，并且许多贡献者不是母语为英语的人。审查者可能会建议修改；你的 IDE 中的拼写检查器可以提供帮助。

### 禁止魔法数字或字符串 {#no-magic-numbers-or-strings}

用命名常量替换未解释的值，并在定义该值的地方进行说明：

```kotlin
// Explanation, or a link, about why the threshold is 42
const val SUPER_IMPORTANT_THRESHOLD = 42

if (value == SUPER_IMPORTANT_THRESHOLD) {
    // Do something
}
```

常量遵循 [Kotlin 命名规范](https://kotlinlang.org/docs/coding-conventions.html#property-names)。

### 常量的位置 {#where-constants-go}

1. 在文件外使用的常量在被导入时必须容易识别，无论是通过它自身的名字还是父级的名字。
2. 大多数常量放在它所属类的文件中，作为文件顶部的 `private const val`，位于类之外。
3. 仅当常量必须从外部访问，或者一个文件中的多个类需要同名常量时，才使用 `companion object`，例如 `DEFAULT_TIMEOUT`。
4. 当一个文件有太多常量，或者这些常量在多个模块间共享时，将它们移动到 `*Constants.kt` 文件中，并在 `object` 中进行分组。

如果测试需要私有常量，请标记为 `@VisibleForTesting`，而不是将其设为公共。

这些规则相对较新，因此你在代码中可能会发现尚未遵循它们的常量。遇到时可以随意修正它们。

### TODO 需要一个问题（issue） {#todos-need-an-issue}

TODO 很容易被遗忘。尽量避免使用它们。当你和审核者都认为某件事以后必须完成时，请添加一个包含完整链接到 GitHub 问题的 TODO：

```kotlin
// TODO Missing feature https://github.com/home-assistant/android/issues/404
```

始终使用完整链接，绝不使用单独的 `#404`：数字在 GitHub 之外是不明确的。当你链接到代码时，请使用永久链接（在 GitHub 上按 <kbd>y</kbd>），这样链接可以在之后的更改中依然有效。
