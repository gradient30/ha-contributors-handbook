---
title: 用 AI 工具做贡献
sidebarLabel: AI 工具
description: 投稿时如何用好AI编码工具？AI 政策对你的要求，存储库为代理提供的指令和技能，常见任务的工作流程，以及每次自我检查的内容。
order: 7
---



# 用 AI 工具做贡献 {#contribute-with-ai-tools}
当你为Home Assistant做出贡献时，可以使用 AI 工具，而且有几个代码库提供了专门为它们编写的说明和技能。本页是[AI 政策](/start/ai-policy)的实用部分：如何从工具中获得优秀的工作成果，以及如何保持自己对结果的理解和负责能力。

AI 工具可以为你节省大量阅读和输入的时间。但它不能替代你的理解。评审人员能够分辨其中的差异，政策也明确说明了对看起来像未经审查的 AI 输出的 pull request 的处理方式：它们将被关闭。

## 实际上政策对你的要求 {#what-the-policy-asks-of-you-in-practice}
[AI 政策](/start/ai-policy)很简短。在日常工作中，其要求归结为以下几点：- **你理解每一处更改，并能用自己的话解释它。** 如果你无法解释某一行代码的作用，请弄清楚它的功能或在提交pull request之前将其删除。
- **你保持知情。** 不允许使用自主代理。代理可以在你的机器上编写代码，但由你决定提交什么。不要让工具在未经你审核的情况下打开问题或pull request，也不要发布评论。
- **你自己回答审查者。** 使用 AI 来修正语法是可以的。答案的实质内容必须是你自己的。

- **在模板要求的地方如实披露。** [Home Assistant Core](https://github.com/home-assistant/core/blob/dev/.github/PULL_REQUEST_TEMPLATE.md) 和 [前端](https://github.com/home-assistant/frontend/blob/dev/.github/PULL_REQUEST_TEMPLATE.md) 的 pull request 模板有两个复选框：“我理解我提交的代码并且可以解释其工作原理”，以及“任何生成的代码都已被仔细审查以确保正确性并符合项目标准”。[Android](https://github.com/home-assistant/android/blob/main/.github/pull_request_template.md) 和 [iOS](https://github.com/home-assistant/iOS/blob/main/.github/pull_request_template.md) 模板要求你确认已阅读政策，并从三种选项中准确选择一个：没有 AI、AI 协助，或者由 AI 完全生成且你已审查并理解的代码。在这些模板部分保持原样，并仅在内容真实时勾选。  
- **你对 AI 审查评论的处理方式应如同对待任何其他审查评论。** 一些项目使用 AI 工具进行审查和分流。它们可能出错。如果你认为某条评论是错误的，请简要指出。代理指令对工具说的是同样的事情。在核心、前端、两个应用程序、[home-assistant.io](https://github.com/home-assistant/home-assistant.io) 和 Supervisor 中，它们都以“AI 政策”部分结尾，告诉代理不要自主打开问题或 pull request，也不要在未经你审查的情况下为你发布评论。##存储库如何准备你的代理

你不用从头开始给你的AI工具解释Home Assistant。大多数存储库为代理提供两种文件:

-**说明* *:一个Markdown文件，包含存储库的基础知识，如如何设置环境、运行测试、格式化代码，以及代理经常出错的规则。大多数工具会在每次会话开始时读取它。
-**技能* *:每个文件夹都有一个`SKILL.md`文件。前面的事有一个`name`和一个`description`。当你的任务符合它的描述时，或者当你通过名字要求它时，这个工具装载一个技能。在克劳德代码中，技能也变成了命令:`ha-review`技能与`/ha-review`一起运行。

这两本书都很便宜，值得你亲自阅读。例如，core的集成技巧在几十行中总结了复习指南。

### 哪个工具读取哪个文件 {#how-the-repositories-prepare-your-agent}
每个工具都会查看自己的位置。以下是每个工具官方文档的说明：

| 文件或文件夹 | 由以下工具读取 |
| --- | --- |
| `AGENTS.md` | [Codex](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [GitHub Copilot](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions) 和 [Claude Code](https://code.claude.com/docs/en/memory) （当没有 `CLAUDE.md` 时） |
| `CLAUDE.md` | Claude Code。GitHub Copilot 也接受在根目录下的 `CLAUDE.md` 或 `GEMINI.md` |
| `.github/copilot-instructions.md` | GitHub Copilot |
| `.github/instructions/*.instructions.md` | GitHub Copilot，针对每个文件匹配 `applyTo` 模式的文件 |
| `.claude/skills/` | [Claude Code](https://code.claude.com/docs/en/skills) 和 [GitHub Copilot](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) |
| `.agents/skills/` | [Codex](https://learn.chatgpt.com/docs/build-skills) 和 GitHub Copilot |
| `.github/skills/` | GitHub Copilot |为了从一个源提供每个工具，存储库使用符号链接。例如，在前端，`CLAUDE.md` 和 `.github/copilot-instructions.md` 链接到 `AGENTS.md`，而 `.claude/skills` 链接到 `.agents/skills`。这样，大多数工具获得相同的指令。不过，并不是每个工具都能找到每个技能文件夹。例如，Codex 读取 `.agents/skills/` 而不是 `.claude/skills/`，所以在 core 和 home-assistant.io 中，你需要自己将其指向一个技能。

- **[核心](https://github.com/home-assistant/core)**：`AGENTS.md`，与 `CLAUDE.md` 相连。`.github/copilot-instructions.md` 通过 `script/gen_copilot_instructions.py` 生成，带有 Copilot 代码审查的额外规则。具备 `.claude/skills/` 技能，以及在 `.claude/agents/` 的 `raise-pull-request` 子代理。
- **[前端](https://github.com/home-assistant/frontend)**：`AGENTS.md`，与 `CLAUDE.md` 和 `.github/copilot-instructions.md` 相连。具备 `.agents/skills/` 技能。
- **[安卓](https://github.com/home-assistant/android)**：`AGENTS.md`，与 `CLAUDE.md`、`GEMINI.md`、`.github/copilot-instructions.md` 和 `.junie/guidelines.md` 相连。具备 `.agents/skills/` 技能，以及一项 `.github/skills/` 技能。
- **[iOS](https://github.com/home-assistant/iOS)**：`AGENTS.md`，与 `CLAUDE.md` 和 `.github/copilot-instructions.md` 相连。具备 `.agents/skills/` 技能。
- **[home-assistant.io](https://github.com/home-assistant/home-assistant.io)**：`.github/copilot-instructions.md`，与 `AGENTS.md`、`CLAUDE.md` 和 `GEMINI.md` 相连。具备 `.claude/skills/` 技能。
- **[Supervisor](https://github.com/home-assistant/supervisor)**：`.github/copilot-instructions.md`，与 `AGENTS.md` 和 `CLAUDE.md` 相连。无技能。

- **[本网站](https://github.com/home-assistant/contributors.home-assistant.io)**：`.github/copilot-instructions.md`，并且与`AGENTS.md`和`CLAUDE.md`相关联，同时在`.github/instructions/`中有审查清单。`.github/skills/`的技能，并且与`.claude/skills`相关联。

[操作系统](https://github.com/home-assistant/operating-system) 仓库包含 AI 政策，但没有代理说明或技能。

## 每个仓库的技能 {#which-tool-reads-which-file}
每行一个技能。选择一个名称以阅读该技能本身。
#

## Home Assistant Core {#the-skills-per-repository}
| 技能 | 使用场景 |
| --- | --- |
| [`ha-integration-knowledge`](https://github.com/home-assistant/core/blob/dev/.claude/skills/ha-integration-knowledge/SKILL.md) | 构建、测试和审核集成。该技能建议在查看集成时将其作为主要参考 |
| [`ha-quality-scale-verify`](https://github.com/home-assistant/core/blob/dev/.claude/skills/ha-quality-scale-verify/SKILL.md) | 检查集成是否遵循质量等级规则，或达到某个等级 |
| [`ha-review`](https://github.com/home-assistant/core/blob/dev/.claude/skills/ha-review/SKILL.md) | 针对目标分支审核代码更改，每个发现都进行二次检查 |
| [`ha-pr-reviewer`](https://github.com/home-assistant/core/blob/dev/.claude/skills/ha-pr-reviewer/SKILL.md) | 审核 GitHub 上的 pull request。它只在终端中报告，不会对 GitHub 进行操作 |
| [`ha-pr-comment-audit`](https://github.com/home-assistant/core/blob/dev/.claude/skills/ha-pr-comment-audit/SKILL.md) | 查找尚未处理的 pull request 审核评论 |
| [`ha-merge-queue`](https://github.com/home-assistant/core/blob/dev/.claude/skills/ha-merge-queue/SKILL.md) | 查找准备合并的未完成 pull request。主要用于维护者 |
| [`bump-dependency`](https://github.com/home-assistant/core/blob/dev/.claude/skills/bump-dependency/SKILL.md) | 升级 Python 依赖项，重新生成需求文件，并准备 pull request |

### 前端| 技能 | 使用场景 | {#home-assistant-core}
| --- | --- |
| [`ha-frontend-components`](https://github.com/home-assistant/frontend/blob/dev/.agents/skills/ha-frontend-components/SKILL.md) | 对话框、表单、警报、键盘快捷键、工具提示、面板、卡片和按钮 |
| [`ha-frontend-contexts`](https://github.com/home-assistant/frontend/blob/dev/.agents/skills/ha-frontend-contexts/SKILL.md) | Lit 上下文，以及将组件从广泛的 `hass` 对象中移开 |
| [`ha-frontend-demo`](https://github.com/home-assistant/frontend/blob/dev/.agents/skills/ha-frontend-demo/SKILL.md) | 独立演示、其配置及其模拟 API |
| [`ha-frontend-events`](https://github.com/home-assistant/frontend/blob/dev/.agents/skills/ha-frontend-events/SKILL.md) | 输入、分派和声明事件 |
| [`ha-frontend-gallery`](https://github.com/home-assistant/frontend/blob/dev/.agents/skills/ha-frontend-gallery/SKILL.md) | 页面、演示和画廊内容 |
| [`ha-frontend-lit`](https://github.com/home-assistant/frontend/blob/dev/.agents/skills/ha-frontend-lit/SKILL.md) | Lit 规范：响应式属性、状态、生命周期和 DOM 查询 |
| [`ha-frontend-review`](https://github.com/home-assistant/frontend/blob/dev/.agents/skills/ha-frontend-review/SKILL.md) | 审查前端更改、准备 pull request 并填写模板 |
| [`ha-frontend-styling`](https://github.com/home-assistant/frontend/blob/dev/.agents/skills/ha-frontend-styling/SKILL.md) | CSS、主题、间距、响应式布局、RTL 及视图过渡 |
| [`ha-frontend-testing`](https://github.com/home-assistant/frontend/blob/dev/.agents/skills/ha-frontend-testing/SKILL.md) | Lint、类型检查、Vitest、Playwright 及开发服务器 |
| [`ha-frontend-types`](https://github.com/home-assistant/frontend/blob/dev/.agents/skills/ha-frontend-types/SKILL.md) | 与后端的TypeScript约定和数据协议 |
| [`ha-frontend-user-facing-text`](https://github.com/home-assistant/frontend/blob/dev/.agents/skills/ha-frontend-user-facing-text/SKILL.md) | 需要翻译的标签、错误、术语和字符串 |
| [`ha-frontend-ux-readiness`](https://github.com/home-assistant/frontend/blob/dev/.agents/skills/ha-frontend-ux-readiness/SKILL.md) | 决定新的卡片、徽章、屏幕或交互模式是否需要设计团队的输入 |

### 安卓应用| 技能 | 使用场景 | {#frontend}
| --- | --- |
| [`ha-android-architecture`](https://github.com/home-assistant/android/blob/main/.agents/skills/ha-android-architecture/SKILL.md) | 模块、层、Hilt、安全存储，以及调用 Home Assistant API |
| [`ha-android-committing`](https://github.com/home-assistant/android/blob/main/.agents/skills/ha-android-committing/SKILL.md) | 完成变更：格式化、测试、更新日志、分支名称，以及 pull request |
| [`ha-android-concurrency`](https://github.com/home-assistant/android/blob/main/.agents/skills/ha-android-concurrency/SKILL.md) | 协程、调度器、Flow 和线程安全 |
| [`ha-android-e2e-debugging`](https://github.com/home-assistant/android/blob/main/.agents/skills/ha-android-e2e-debugging/SKILL.md) | 找出端到端测试失败的原因 |
| [`ha-android-kotlin-style`](https://github.com/home-assistant/android/blob/main/.agents/skills/ha-android-kotlin-style/SKILL.md) | Kotlin 风格：常量、类型、时间、命名和注释 |
| [`ha-android-logging-errors`](https://github.com/home-assistant/android/blob/main/.agents/skills/ha-android-logging-errors/SKILL.md) | 日志记录、错误处理，以及避免用户数据出现在日志中 |
| [`ha-android-review`](https://github.com/home-assistant/android/blob/main/.agents/skills/ha-android-review/SKILL.md) | 审查变更的正确性、风格和安全性 |
| [`ha-android-skill-maintenance`](https://github.com/home-assistant/android/blob/main/.agents/skills/ha-android-skill-maintenance/SKILL.md) | 保持 `AGENTS.md` 和技能的更新 |
| [`ha-android-testing`](https://github.com/home-assistant/android/blob/main/.agents/skills/ha-android-testing/SKILL.md) | 单元测试、Robolectric、Flow 和截图测试 |
| [`ha-android-ui`](https://github.com/home-assistant/android/blob/main/.agents/skills/ha-android-ui/SKILL.md) | 组成屏幕、ViewModel、导航、控件和设计系统 |
| [`agentic-workflows`](https://github.com/home-assistant/android/blob/main/.github/skills/agentic-workflows/SKILL.md) | 在仓库中设计和调试 GitHub 代理工作流程 |

Android 仓库中还有一个 Claude Code 钩子在 `.claude/settings.json`，它会提醒代理在编辑测试时加载 `ha-android-testing`。

### iOS 应用| 技能 | 用途 | {#android-app}
| --- | --- |
| [`ha-ios-architecture`](https://github.com/home-assistant/iOS/blob/main/.agents/skills/ha-ios-architecture/SKILL.md) | 项目布局、目标、`Current` 依赖模式以及代码签名 |
| [`ha-ios-code-style`](https://github.com/home-assistant/iOS/blob/main/.agents/skills/ha-ios-code-style/SKILL.md) | Swift 风格、SwiftFormat、SwiftLint、图标和日志记录 |
| [`ha-ios-concurrency`](https://github.com/home-assistant/iOS/blob/main/.agents/skills/ha-ios-concurrency/SKILL.md) | async/await、actors、Combine，以及使用 HAKit 与服务器通信 |
| [`ha-ios-localization`](https://github.com/home-assistant/iOS/blob/main/.agents/skills/ha-ios-localization/SKILL.md) | 添加或更改面向用户的字符串 |
| [`ha-ios-magicitem`](https://github.com/home-assistant/iOS/blob/main/.agents/skills/ha-ios-magicitem/SKILL.md) | 由小组件、Apple Watch、CarPlay 和 App 快捷方式共享的项目模型 |
| [`ha-ios-persistence`](https://github.com/home-assistant/iOS/blob/main/.agents/skills/ha-ios-persistence/SKILL.md) | 使用 GRDB、Realm 或 UserDefaults 存储数据 |
| [`ha-ios-push-live-activities`](https://github.com/home-assistant/iOS/blob/main/.agents/skills/ha-ios-push-live-activities/SKILL.md) | 推送通知和实时活动 |
| [`ha-ios-skill-maintenance`](https://github.com/home-assistant/iOS/blob/main/.agents/skills/ha-ios-skill-maintenance/SKILL.md) | 保持技能和 `AGENTS.md` 更新 |
| [`ha-ios-testing`](https://github.com/home-assistant/iOS/blob/main/.agents/skills/ha-ios-testing/SKILL.md) | 单元测试、快照测试以及模拟依赖项 |
| [`ha-ios-ui`](https://github.com/home-assistant/iOS/blob/main/.agents/skills/ha-ios-ui/SKILL.md) | SwiftUI 和 UIKit 约定，以及设计系统包 |
| [`ha-ios-webview`](https://github.com/home-assistant/iOS/blob/main/.agents/skills/ha-ios-webview/SKILL.md) | 显示前端的 Web 视图、它的消息总线以及深度链接 |
| [`ha-ios-workflow-ci`](https://github.com/home-assistant/iOS/blob/main/.agents/skills/ha-ios-workflow-ci/SKILL.md) | 提交前的步骤顺序、TestFlight 门控以及 CI 检查 |

### home-assistant.io 文档 {#ios-app}
| 技能 | 使用场景 |
| --- | --- |
| [`home-assistant-docs-writing-style`](https://github.com/home-assistant/home-assistant.io/blob/current/.claude/skills/home-assistant-docs-writing-style/SKILL.md) | 任何文档、页面或面向用户的文章 |
| [`home-assistant-markdown-liquid-style`](https://github.com/home-assistant/home-assistant.io/blob/current/.claude/skills/home-assistant-markdown-liquid-style/SKILL.md) | Markdown、Liquid、链接、图片、词汇表条目、我的链接和文本框 |
| [`home-assistant-yaml-style`](https://github.com/home-assistant/home-assistant.io/blob/current/.claude/skills/home-assistant-yaml-style/SKILL.md) | YAML 示例、自动化、脚本和模板 |
| [`document-integration-docs`](https://github.com/home-assistant/home-assistant.io/blob/current/.claude/skills/document-integration-docs/SKILL.md) | 以分页格式撰写或更新集成文档 |
| [`create-blog-post`](https://github.com/home-assistant/home-assistant.io/blob/current/.claude/skills/create-blog-post/SKILL.md) | 将 Google 文档草稿转换为博客文章 |
| [`create-astro-component`](https://github.com/home-assistant/home-assistant.io/blob/current/.claude/skills/create-astro-component/SKILL.md) | 将网站的一部分重建为 Astro 组件 |
| [`update-agent-instructions`](https://github.com/home-assistant/home-assistant.io/blob/current/.claude/skills/update-agent-instructions/SKILL.md) | 更新仓库的代理说明 |

### 这个贡献者网站| 技能 | 用途 | {#documentation-on-home-assistantio}
| --- | --- |
| [`write-page`](https://github.com/home-assistant/contributors.home-assistant.io/blob/main/.github/skills/write-page/SKILL.md) | 添加或更改页面，从选择区域到运行检查 |
| [`review`](https://github.com/home-assistant/contributors.home-assistant.io/blob/main/.github/skills/review/SKILL.md) | 审查 pull request、页面或网站代码，每个声明都与来源核对 |
| [`fact-check`](https://github.com/home-assistant/contributors.home-assistant.io/blob/main/.github/skills/fact-check/SKILL.md) | 检查现有页面与源代码库的匹配情况，并修复不一致的部分 |
| [`add-glossary-term`](https://github.com/home-assistant/contributors.home-assistant.io/blob/main/.github/skills/add-glossary-term/SKILL.md) | 添加或更改词汇表条目 |
| [`design-component-page`](https://github.com/home-assistant/contributors.home-assistant.io/blob/main/.github/skills/design-component-page/SKILL.md) | 设计区域中的组件页面，带有实时演示 |

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](/start/ai-tools)。
| [`update-demos`](https://github.com/home-assistant/contributors.home-assistant.io/blob/main/.github/skills/update-demos/SKILL.md) | 使用更新的前端重建实时组件演示 |
| [`port-developers-change`](https://github.com/home-assistant/contributors.home-assistant.io/blob/main/.github/skills/port-developers-change/SKILL.md) | 将旧开发者文档中的更改迁移到本网站 |
| [`create-blog-post`](https://github.com/home-assistant/contributors.home-assistant.io/blob/main/.github/skills/create-blog-post/SKILL.md) | 将草稿变成本网站上的博客文章 |
| [`update-agent-instructions`](https://github.com/home-assistant/contributors.home-assistant.io/blob/main/.github/skills/update-agent-instructions/SKILL.md) | 更新代理指令，并同步与 home-assistant.io 共享的写作规则 |

## 常见任务的工作流 {#this-contributor-site}
这些工作流将上述技能与本网站的指南结合起来。它们适用于任何能够读取技能文件夹的工具。如果你的工具不支持，请自己将其指向 `SKILL.md` 文件。

### 修复集成中的一个错误1. 首先自己重现该错误，并在GitHub上找到问题。如果你从未看到它失败，代理无法告诉你其修复是否解决了*你的*错误。 {#workflows-for-common-tasks}
2. 使用`ha-integration-knowledge`技能请代理找出原因。在修改代码之前，让它编写一个因该错误而失败的测试。一个在未修复情况下通过的测试不能证明任何问题。
3. 让它修复代码，然后像在[运行测试](/core/development/testing)中一样自己运行集成测试：`pytest tests/components/<domain>`。如果修复更改了`strings.json`，核心`AGENTS.md`会告诉代理先重新生成英文翻译，因为测试会读取这些翻译。

4. 阅读差异。代理通常会添加比修复更多的东西：额外的“防御性”检查、叙述代码的注释、附带的重构。核心的指示告诉代理避免添加重述代码的注释和验证已涵盖的检查，但仍要检查，并删除修复不需要的内容。
5. 亲自打开 pull request，并填写 [模板](/core/development/submitting)。核心有一个 `raise-pull-request` 子代理，它会为你运行检查并填写模板。要知道，它会推送你的分支并将 pull request 以草稿形式打开。它会将“我理解代码...”和“任何生成的代码都已仔细审核...”保持未勾选，等你确认后再勾选。

### 构建一个新的集成并达到青铜级 {#fix-a-bug-in-an-integration}
一个新的集成必须达到[质量等级](/core/quality-scale)的青铜级，其第一个pull request应保持较小。请先阅读[创建集成](/core/integrations/create)：它解释了一个新的集成何时属于核心，并设定了审核者要求的限制。

1. **从库开始。** `ha-integration-knowledge` 技能指出，集成应该是薄包装器，而协议和设备逻辑应放在 PyPI 上的独立库中。代理可以轻松地在你的集成中编写 HTTP 客户端。不要让它这么做。请参见 [构建 Python 库](/core/integrations/api-library)。
2. **自己生成骨架**，使用 `python3 -m script.scaffold integration`。这个脚手架会在你的代码位置留下 `TODO` 注释，并且有一个 `quality_scale.yaml`，每条规则都设置为 `todo`。
3. **用代理逐个平台填写**，加载 `ha-integration-knowledge`。在继续之前，请让它解释配置流程和协调器。你随后需要向审核者解释它们。
4. **在 `quality_scale.yaml` 中如实标记铜级规则**：`done`，或 `exempt` 并给出理由。[规则](/core/quality-scale/rules) 解释了每条规则。

5. **使用 `ha-quality-scale-verify` 进行验证。** 该技能一次检查一个规则，并检查每个层级的每条铜规则。它会运行现有的工具，例如 hassfest，而不是从代码中猜测，并在无法检查规则时将其标记为未验证。一些铜规则位于核心仓库之外：`brands` 资源，以及 `docs-*` 规则，这些需要你在 home-assistant.io 上的文档 pull request。阅读报告，并修复或豁免报告中发现的问题。
6. **自行运行检查**：检查你的集成和 `prek run --all-files`。请参阅 [Linters, hassfest, and CI](/core/development/checks)。
7. **逐行阅读**，然后打开上述 pull request。审查者会问为什么某段代码存在。“AI写的”不是政策认可的答案。

### 审查 pull request {#build-a-new-integration-and-take-it-to-bronze}
审查有助于整个项目，核心模板会邀请你审查另外两个 pull request。AI 工具可以帮助你在不熟悉的变更中找到方向。你发布的审查仍然必须是你自己的。

- **核心**: `ha-pr-reviewer` 使用 GitHub CLI 阅读 pull request，使用 `ha-review` 进行审查，并使用 `ha-pr-comment-audit` 检查未关闭的评论线程。它仅在你的终端中报告。
- **前端**: `ha-frontend-review`，配备与变更匹配的相关技能。它首先阅读现有评论，并优先考虑人类的反馈，而不是代理的反馈。
- **安卓**: `ha-android-review`.然后在写下每个发现之前，将其与代码进行核对。删除那些你无法确认或不理解的内容。用你自己的话发布你的审查，不要粘贴工具的输出，也不要让工具代替你发布。[审查 pull requests](/core/development/reviewing) 解释了优秀核心审查应关注的内容。

### 在前端添加卡片 {#review-a-pull-request}
对于新卡片，项目首先推荐使用 Marketplace，详见 [分享它](/frontend/custom-ui#share-it)。这些步骤适用于前端本身的卡片。

1. 加载 `ha-frontend-components` 和 `ha-frontend-styling`。组件技能列出了卡片必须执行的操作：验证其配置、处理加载、错误、不可用和缺失的实体，并在需要时提供编辑器。
2. 在编写大量代码之前，请阅读 `ha-frontend-ux-readiness`。新卡片既是设计决策，也是代码。当方向尚未确定时，评审者会向设计团队征求意见。请参见 [审查和发布](/frontend/development/review-and-release) 和 [我们的设计方法](/design/how-we-design)。
3. 将每一个可见字符串通过翻译系统处理，如 `ha-frontend-user-facing-text` 所解释。
4. 运行 `pnpm lint` 和 `pnpm test`，并在浅色模式、深色模式以及手机上亲自尝试卡片。将截图或短视频添加到 pull request：前端模板需要它们。

你自己仓库中的自定义卡片没有要加载的技能。参考 [自定义卡片指南](/frontend/custom-ui/card)。

### 在 home-assistant.io 上撰写文档 {#add-a-card-to-the-frontend}
home-assistant.io 的说明告诉代理在编辑之前加载匹配的技能，并加载所有适用的技能：

- `home-assistant-docs-writing-style` 用于任何散文。
- `home-assistant-markdown-liquid-style` 用于链接、图片、Liquid 及其他站点语法。
- `home-assistant-yaml-style` 用于 YAML 示例。
- `document-integration-docs` 用于集成页面。它需要域名，比如 Claude Code 中的 `/document-integration-docs <domain>`，并在你将 core 和前端克隆到文档旁时读取集成在 core 中的触发器、条件和操作。在那些说明中，有两条规则对 AI 工作最重要。除非你要求，否则代理不得发明新的仪表板、卡片、自动化或脚本示例。并且 `document-integration-docs` 不得信任问题文本或现有文档，除非核心确认它们。你的自我审查也要遵循同样的标准：检查每个选项、默认值和步骤与代码是否一致，并在部署预览中查看你的页面。[撰写文档](/writing)有其余内容。

### 翻译不是人工智能的任务 {#write-documentation-on-home-assistantio}
界面的翻译是在 [Lokalise](/glossary/lokalise) 由人工完成的。[翻译规则](/translate/reference/rules) 要求你只翻译成你的母语，因为机器翻译会显示出来。应用程序的代理指令从另一方面也同意：代理仅添加或更改英文字符串。Android 技能说明翻译文件来自 Lokalise，绝不能添加或编辑，而 iOS 技能说明只修改英文`.strings`文件。

有一个已记录的例外。对于 [语音意图](/translate/voice/style-guide#drafts-from-an-ai-model)，[意图仓库](https://github.com/OHF-Voice/intents) 可以生成一个提示，你将其粘贴到 AI 模型中以起草意图的句子。这是一个草稿，由母语者重写。

## 每次都要自查的内容 {#translations-are-not-an-ai-task}
工具的输出只是一个草稿。这些检查可以发现本站审核中一次又一次发现的错误。

- **在正确的分支上对照代码进行验证。** 事实应该以仓库的默认分支为准，例如核心和前端的 `dev`。不是你的记忆，不是工具的记忆，也不是几周前的本地克隆。函数名称、参数和命令会发生变化。
- **关于人员、流程和数字的说法需要有来源。** 谁来决定，谁来审核，需要多长时间，有多少个。这些都无法通过代码证明，工具会用听起来合理的内容来填补空白。请找到官方页面，或者干脆不提。
- **注意绝对词。**“总是”、“从不”、“每一个”、“唯一”。寻找例外：第二条代码路径、备用方案、功能标志。条件在工具总结时常常会被遗漏。

- **在生命周期边界上进行测试。** 在理想情况下能正常工作的代码，在第一次更新、卸载后重新加载、迁移之后、设备消失又重新出现时，或者在列表为空时，可能会出问题。问问自己每种情况会发生什么。
- **从头开始按顺序执行步骤。** 工具编写的说明常常会漏掉`cd`、一次安装或后续步骤需要的设置。
- **不要让摘要代替原文。** 获取页面或文件的工具会给你摘要，而摘要会搞乱名称和数字。在依赖细节之前请自己阅读原文。
- **在提交前查看差异。** 注意那些你没有要求的更改、代码中承诺过但实现不足的注释，以及你无法解释的代码。

## 为你的代理提供有关此网站的上下文 {#what-to-check-yourself-every-time}
该网站发布了 [`/llms.txt`](/llms.txt)，这是其 AI 工具相关区域和页面的索引，采用 [llms.txt 格式](https://llmstxt.org/)。在任务开始时将其提供给你的代理，这样它可以找到适用的指南，而不是猜测，或去阅读其他地方过时的页面。同样的规则也适用于它在那里找到的内容：这是一个起点，代码才是来源。

## 联系对象 {#give-your-agent-context-about-this-site}
- 不确定你的 AI 使用是否符合政策？请向维护人员咨询，在你的 pull request 或 [Home Assistant Discord](https://www.home-assistant.io/join-chat/) 上。
- 技能给出了错误的建议？请在承载该技能的存储库中打开问题或 pull request。技能像任何其他文件一样进行维护。
