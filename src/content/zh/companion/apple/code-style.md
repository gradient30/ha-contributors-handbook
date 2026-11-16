---
title: Apple 代码风格
description: 在苹果项目中SwiftFormat,SwiftLint,RuboCop,和Yamllint,编码公约审查员寻找.
sidebarLabel: 代码样式
order: 4
source: https://github.com/home-assistant/iOS/blob/main/.github/workflows/ci.yml
lastVerified: 2026-10-14
---



# Apple 代码风格 {#apple-code-style}
最后一次验证是在2026-10-14,对https://github.com/home-assistant/iOS/blob/main/.github/workflows/ci.yml.

苹果项目格式并自动涂抹其代码,因此评论可以专注于行为和边缘案例而不是风格.

## 工具 {#the-tools}

| 工具 | 检查 | 配置在 |
| --- | --- | --- |
| [才能实现](https://github.com/nicklockwood/SwiftFormat) | 快速格式化 | `.swiftformat` |
| [闪光灯](https://github.com/realm/SwiftLint) | 斯威夫特规则斯威夫特Format不涵盖,加上定制规则 | `.swiftlint.yml` |
| [鲁博科普](https://rubocop.org) | Fastlane 的 Ruby 代码 | `.rubocop.yml` |
| [雅博·伊利姆·伊利姆](https://yamllint.readthedocs.io/) | 工作流量和其他YAML | `.yamllint.yml` |

## 运行他们 {#run-them}

```bash
# Report problems, change nothing {#report-problems-change-nothing}
bundle exec fastlane lint

# Fix what can be fixed automatically {#fix-what-can-be-fixed-automatically}
bundle exec fastlane autocorrect
```

瑶族在每次犯罪前运行 `autocorrect`瑶族,或者让你做它:

```bash
bundle exec fastlane install_git_hooks
```

Xcode内部,linters只显示警告,而不改变代码. CI还运行着Yamllint,它不属于`lint`车道的一部分.

## 配置执行什么 {#what-the-configuration-enforces}

- **Formatting **:最多120个字符的行,在第一个元素之前包裹的参数和集合,`self`只在初始化器中,`guard`和`else`在同一行上,没有文件头注释.
- ** SwiftLint** 使用规则的允许列表,而不是每个默认规则. 其中:无 `force_cast` 或 `force_try` , 和 低 的 百科复杂 。
- ** Custom SwiftLint 规则**:从未指派给 `Current` 外部测试, 并且使用 `SFSafeSymbols` 而不是原始 SF 符号名称 。

```swift
// Wrong
Image(systemName: "house")

// Right
Image(systemSymbol: .house)
```

### 禁止某项规则 {#suppressing-a-rule}

当心`// swiftlint:disable`。 CI 在每个 pull request 中寻找新的, 当它从寄存器本身的分支中找到一个(在 pull request 上) 时会评论, 所以维护者可以检查它是否真的需要它 。 每一次镇压都需要一个很好的理由。

## 公约 {#conventions}

- ** 每个文件一个类型**,以该类型命名,每个 SwiftUI 视图为 `#Preview` 。 见[每次更改的规则](/companion/apple/architecture#rules-for-every-change).
- ** 带有 `Current.Log` 的日志, 从不 `print` 或 `NSLog` 。
- ** 小型、名副其实的类型和功能**,这些类型和功能本身容易测试。
- ** 共用代码采用共享模块**,而不是在目标之间复制。 不要把关于一个目标的假设放到共享或扩展代码中.
- ** 面对文本的用户** 在`en.lproj/Localizable.strings`中。 SwiftGen 生成代码中使用的 `L10n` 访问器, 翻译来自 [Lokalise](/translate) 。

## 生成的文件 {#generated-files}

一些文件是由工具或工作流程生成的,如`L10n`访问器和图标及颜色集. 生成的文件通常在顶端的注释中这样说. 不要用手编辑它们:改变源头并运行工具. 当你触摸Ruby或工作流程代码时,确保它的linters仍然通过.
