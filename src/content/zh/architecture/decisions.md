---
title: 架构决策是如何做出的
sidebarLabel: 决策是如何做出的
description: 讨论架构的地方，决策如何被记录，以及你如何参与其中。
order: 4
---


# 架构决策是如何做出的 {#how-architecture-decisions-are-made}
架构会议负责Home Assistant的技术架构。对Home Assistant构建方式的每一次更改都需要得到它的批准。

会议负责决策，但这些决策不是在闭门会议中做出的。每个提议都从GitHub上的[架构仓库](https://github.com/home-assistant/architecture)中的讨论开始，结果也会在那里发布。任何人都可以跟踪阅读，任何人都可以发起讨论。

## 什么时候算是架构问题 {#when-something-is-an-architecture-question}
大多数更改不需要先讨论：修复一个 bug、在集成中添加新功能，或者一个新的集成已经 [准备好加入核心](/core/integrations/create#does-it-belong-in-core)。请打开一个 pull request。

当更改影响到每个人如何在 Home Assistant 上开发时，需要发起讨论，例如：

- 一种新的实体类型，或对现有实体的大改动
- 集成的新规则，或对现有规则的例外
- 项目支持内容的变化，如安装方式或 Python 版本
- 其他部分的 Home Assistant 将基于的新概念

如果不确定，请在 [**#developers**](https://discord.com/channels/330944238910963714/554842238073700352) 频道的 [Discord](https://www.home-assistant.io/join-chat) 上询问。这样可以避免你编写的代码后来必须改变方向。

## 从讨论到决策 {#from-discussion-to-decision}
1. **讨论。** 有人提出一个问题和建议，并开启一个[讨论](https://github.com/home-assistant/architecture/discussions)。其他人提出问题，指出漏洞，并建议替代方案。讨论应集中在一个主题上。
2. **决策。** 当讨论结束后，建议将在架构会议上做出决策。结果会发布在讨论中，并标记为其答案：批准或拒绝，同时附上会议日期及备注或理由。
3. **记录。** 对整个项目设定长期规则的决策也需要记录为架构决策记录（Architecture Decision Record，ADR），存放在[`adr` 文件夹](https://github.com/home-assistant/architecture/tree/master/adr)中。

## 决策与路线图 {#decisions-and-the-roadmap}
架构会议不属于路线图流程的一部分。它与路线图并行：对 Home Assistant 构建方式的任何更改都需要其批准，无论该更改来自路线图还是贡献者自己的想法。

较大的工作计划在 Open Home Foundation 的 [路线图](/roadmap) 上，作为机会，并通过 [史诗](https://github.com/home-assistant/epics) 实施。当某个机会改变 Home Assistant 的构建方式时，例如实体组件的新触发器和条件，它需要在工作进行之前做出架构决策。它可以双向进行。对于[阳光触发](https://github.com/home-assistant/architecture/discussions/1394)来说，机会是先出现的：讨论将其链接为推理所在的地方，架构会议批准了修改后的提案，机会又回溯到该批准，工作计划在一个大型任务中。其他机会则是建立在最初就存在的架构讨论之上的。[从想法到发布](/roadmap/how-it-works)遵循了从开始到结束的这一示例。

## 架构决策记录 {#architecture-decision-records}
ADR 是一个简短的文档，具有固定的结构：上下文、决策及其后果。它是编号的，并且永远不会被删除。当决策发生变化时，其状态会显示出来，并链接到取代它的内容。

这使得 ADR 成为项目的历史。一些值得了解的决策：| ADR | 决策 |
| --- | --- |
| [0007](https://github.com/home-assistant/architecture/blob/master/adr/0007-integration-config-yaml-structure.md) | 集成的 YAML 配置存放在其自己的域下。 |
| [0008](https://github.com/home-assistant/architecture/blob/master/adr/0008-code-owners.md) | 成为集成所有者意味着什么。 |
| [0010](https://github.com/home-assistant/architecture/blob/master/adr/0010-integration-configuration.md) | 连接到设备或服务的集成在 UI 中进行设置。 |
| [0011](https://github.com/home-assistant/architecture/blob/master/adr/0011-discovery-requires-unique-id.md) | 可发现的集成设置一个唯一 ID，以便用户可以忽略发现。 |
| [0012](https://github.com/home-assistant/architecture/blob/master/adr/0012-define-supported-installation-method.md) | 什么是支持的安装方法。 |
| [0018](https://github.com/home-assistant/architecture/blob/master/adr/0018-supported-databases.md) | 记录器支持哪些数据库。 |
| [0019](https://github.com/home-assistant/architecture/blob/master/adr/0019-GPIO.md) | 不再创建直接使用 GPIO 引脚的新集成。 |
| [0020](https://github.com/home-assistant/architecture/blob/master/adr/0020-minimum-supported-python-version.md) | 一次只能支持一个 Python 的小版本。 |
| [0021](https://github.com/home-assistant/architecture/blob/master/adr/0021-YAML-integration-configuration-deprecation-policy.md) | YAML 配置会被弃用至少六个月，然后才会移除。 |
| [0022](https://github.com/home-assistant/architecture/blob/master/adr/0022-integration-quality-scale.md) | 集成质量等级，共四个层级。 |一些 ADR 已经被撤销：例如 Home Assistant Core 和监督安装方法的那些。它们的状态在顶部显示了这一点。

## 在讨论中使用 AI {#using-ai-in-discussions}
架构存储库还保存了 Open Home Foundation 的 [AI 政策](https://github.com/home-assistant/architecture/blob/master/AI_POLICY.md)。它适用于所有项目中的讨论、问题和 pull request。简而言之：你可以将 AI 作为工具使用，但你必须理解并能够解释你发布的所有内容，并且不允许自治代理参与。

## 开始工作 {#work-on-this}
- 有提案吗？先阅读 [公开讨论](https://github.com/home-assistant/architecture/discussions)：你的提案可能已经在那里。
- 想了解某个决策如何适应更大的计划？请参阅 [从创意到发布](/roadmap/how-it-works)。
- 不确定从哪里开始贡献？[你的第一次贡献](/start/first-contribution) 可以帮助你选择。
