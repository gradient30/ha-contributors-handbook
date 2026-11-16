---
title: 项目的组织方式
description: 谁拥有Home Assistant，谁支付费用，工作的归属地，以及谁决定合并什么内容。
sidebarLabel: 项目的组织方式
order: 5
---



# 项目的组织方式 {#how-the-project-is-organized}
Home Assistant 是一个开源项目，由一个非盈利基金会拥有，并与社区贡献者共同建设。本页面解释了这些部分如何配合运作，让你知道自己在与谁合作。

## Open Home Foundation {#the-open-home-foundation}
Home Assistant 属于 [Open Home Foundation](https://www.openhomefoundation.org/)，这是一个非营利组织。Home Assistant 和其他项目在 2024 年转移到了该基金会。如今，基金会还拥有类似 ESPHome 和 Music Assistant 的项目。

基金会聘请了超过 50 名全职员工。他们在相同的代码库工作，遵循相同的审查流程，并使用相同的频道交流。你会在审查中遇到他们，但他们远不是唯一进行审查和合并的人。

基金会在智能家居领域坚持三个价值观：隐私、选择和可持续性。这些价值观在 [我们的原则](/start/principles) 中有所体现。其 [架构页面](https://www.openhomefoundation.org/structure/) 解释了基金会如何管理和资助。

## 商业合作伙伴 {#commercial-partners}
该基金会的资金来自商业合作伙伴费用和捐款。目前的商业合作伙伴是 [Nabu Casa](https://www.nabucasa.com/) 和 Apollo Automation。每个合作伙伴在合同上都被要求将其销售许可产品的利润的大部分贡献给基金会。

Nabu Casa 是 Home Assistant 产品和服务的官方提供商，例如 Home Assistant Link：一种可选订阅，可增加远程访问、Amazon Alexa 和 Google Assistant，以及 Assist 的云端语音服务。

## 仓库 {#the-repositories}
所有的工作都在公开环境下进行，在 GitHub 上，归 [home-assistant](https://github.com/home-assistant) 组织管理。你早期可能会遇到的几个仓库：

- [core](https://github.com/home-assistant/core)：Home Assistant Core 以及所有内置集成，位于 Python。
- [frontend](https://github.com/home-assistant/frontend)：网页界面，位于 TypeScript。
- [home-assistant.io](https://github.com/home-assistant/home-assistant.io)：用户文档。
- [android](https://github.com/home-assistant/android) 和 [iOS](https://github.com/home-assistant/iOS)：伴侣应用。
- [supervisor](https://github.com/home-assistant/supervisor) 和 [operating-system](https://github.com/home-assistant/operating-system)：负责安装、更新和运行所有内容。
- [architecture](https://github.com/home-assistant/architecture)：关于 Home Assistant 构建方式的讨论和决策。

一些项目存在于基金会的其他组织中，例如 [OHF-Voice](https://github.com/OHF-Voice/intents) 中的语音意图。[Repositories](/architecture/repositories) 列出了它们的全部，并告诉你每个仓库适合做什么。

## 维护者、团队和集成所有者 {#maintainers-teams-and-integration-owners}
任何人都可以打开问题、提交pull request或进行审查。谁决定合并取决于仓库：

- **维护者** 可以批准并合并pull request。每个仓库都有自己的维护者，通常组织在GitHub团队中，例如`@home-assistant/core`的Home Assistant Core。
- **集成所有者** 负责某个集成。在Home Assistant Core中，每个集成都在其清单的`codeowners`字段中列出其所有者。他们会收到关于该集成的问题通知，并且GitHub会要求他们审查涉及该集成的pull request。
- **审查者** 可以是任何人。贡献者的仔细审查可以帮助维护者更快地做出决定。更大的问题，比如一种新类型的实体或适用于所有集成的规则，会在架构仓库中公开讨论。[架构决策是如何做出的](/architecture/decisions)解释了其工作原理。

### CODEOWNERS中的团队 {#teams-in-codeowners}
`CODEOWNERS` 文件告诉 GitHub 应该向谁请求审查。在 Home Assistant Core 以及 [home-assistant.io](https://github.com/home-assistant/home-assistant.io) 上，它列出了人员和 `home-assistant` 组织中的一些 GitHub 团队：

- `@home-assistant/core`：核心文件，以及核心团队负责的集成
- `@home-assistant/frontend`：`frontend`、`lovelace` 和 `panel_custom` 集成
- `@home-assistant/supervisor`：`hassio` 集成，以及构建容器镜像的文件
- `@home-assistant/cloud`：`cloud`、`alexa` 和 `google_assistant` 集成，在 Home Assistant Link 背后
- `@home-assistant/matter`：`matter` 集成
- `@home-assistant/z-wave`：`zwave_js` 集成

一些集成由组织之外的团队拥有，例如制造商的团队。在 Core 中，`CODEOWNERS` 文件是根据集成的清单生成的，因此当清单更改时，它也会变化。

### 成为集成所有者 {#become-an-integration-owner}
集成的所有者列在其 `manifest.json` 的 `codeowners` 字段中。要成为所有者，请打开一个 pull request，将你的 GitHub 用户名添加到那里。先参与集成的工作会有很大帮助。[集成所有者](/core/quality-scale/integration-owner) 解释了该角色对你的要求，以及如何更新文件。

## 志愿者和员工 {#volunteers-and-staff}
有两类人参与 Home Assistant 的工作：

- **员工** 由 Open Home Foundation 雇用。基金会通过其商业合作伙伴的费用和捐赠支付他们的薪水。其 [结构页面](https://www.openhomefoundation.org/structure/) 上有详细信息。
- **志愿者** 不领取报酬。他们在空闲时间贡献，因为他们关心 Home Assistant 。

两者都在相同的代码库工作，遵守相同的规则。大多数贡献者是志愿者。这塑造了项目的运作方式：审查可能需要一段时间，没有人欠任何人合并，同时耐心是双向的。它也意味着项目的形态由参与的人决定。如果你关心某件事，你可以帮助它实现。

## 项目的发展方向 {#where-the-project-is-heading}
基金会计划在公开场合进行更大的工作。其董事会设定了[目标](https://github.com/OpenHomeFoundation/goals)。产品团队将一些功能请求转换为[路线图](https://github.com/OpenHomeFoundation/roadmap)上的机会：值得解决的问题，而不是带日期的功能列表。通过史诗任务和在工作发生的仓库中的任务来交付这些机会。

你可以通过[功能请求](https://github.com/home-assistant/feature-requests/discussions)来影响它：分享你的想法、投票和讨论。[从想法到发布](/roadmap/how-it-works)会讲解每一个步骤，并展示你可以参与的地方。
