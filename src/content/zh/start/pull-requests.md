---
title: Pull request 与审查
description: 如何打开一个易于审查的pull request，打开后会发生什么，以及如何帮助它被合并。适用于每个仓库。
sidebarLabel: Pull request 与审查
order: 4
---



# Pull request 与审查 {#pull-requests-and-reviews}
[pull request](/glossary/pull-request) 是更改进入 Home Assistant 的方式，无论是代码、文档还是设计令牌。此页面解释了每个仓库中相同的部分。每个区域都会添加自己的细节，例如 [核心开发指南](/core/development) 或 [前端审查](/frontend/development/review-and-release)。

刚接触 GitHub？像 fork、branch、commit 和 push 这样的词在 [使用 GitHub，无需成为开发者](/start/github) 中都有解释。它还会带你完全在浏览器中完成第一次 pull request，无需安装任何软件。

## 在你打开它之前 {#before-you-open-it}
### 检查是否合适 {#check-that-it-fits}
大多数更改不需要事先获得许可。修复错误、改进文档或增加小功能可以直接提交到 pull request。较大的更改则不同：一种新的实体类型、对所有集成方式的修改，或对所有人增加新的依赖。这些需要先讨论，这样你就不会开发出必须改方向的东西。请参阅 [决策是如何做出的](/architecture/decisions)。

所有架构决策都记录在 [架构仓库](https://github.com/home-assistant/architecture) 中。你的更改必须遵循这些决策。

### 保持简洁 {#keep-it-small}
一个pull request 应该只做一件事：修复一个漏洞、添加一个功能，或更新一个页面。途中发现了其他问题？放到另一个pull request 中。

小的pull request 会更快获得审核。更多的人可以进行审核，它们冲突的几率更小，而且对小改动的认真审核比快速浏览大改动更容易发现问题。许多小pull request 并不低效，它们更高效。

依赖更新也应该放在独立的pull request 中，并附上发布说明或者两个版本之间的变更链接，这样审阅者就可以检查发生了什么变化。

#

## 测试它 {#test-it}
运行你的修改并检查它是否工作正常，或者对于文档来说，是否看起来正确。这听起来很明显，但当操作正确时，它能节省整个审核轮次。

### 从最新版本开始 {#start-from-the-latest-version}
一个 [分支](/glossary/branch) 是一条独立的变更线路，因此你的工作不会与其他内容混在一起。每做一次 pull request 都要创建一个新的分支，基于代码库主分支的最新版本。例如，对于 Home Assistant Core 和前端，使用 `dev`，对于文档，则使用 `current` 或 `next`。各个领域的指南会告诉你应该使用哪个分支。

你的 [分叉](/glossary/fork)，也就是你自己的代码库副本，不会自动更新。如果你之前创建过，它可能会落后：在开始之前，请拉取最新的更改。

### 填写模板 {#fill-out-the-template}
每个代码库都有一个 pull request 模板。请使用它，并且不要删除其部分。写一个清晰的标题，以及一个解释你 *为什么* 做此更改的描述，而不仅仅是它做了什么。链接到它修复的问题。如果你使用了 AI 工具，请遵循 [AI 政策](/start/ai-policy)：你必须能够用自己的话解释每一个更改。有几个模板会通过复选框询问这个问题。[pull request 模板询问的内容](/start/ai-policy#what-the-pull-request-templates-ask) 列出了这些问题。

## 打开它之后 {#after-you-open-it}
### 机器人先行 {#the-bots-go-first}
在几分钟内，会有几件事情自动发生：- **CLA 检查。** 在代码仓库中，机器人会在你第一次贡献时要求你签署 [Contributor License Agreement](/start/licensing)。在你签署之前，你的 pull request 无法被合并。
- **标签。** 机器人会给你的 pull request 打标签，例如根据更改类型或涉及的集成。标签帮助维护者找到他们可以审查的 pull request。
- **集成负责人。** 如果你修改了一个集成，GitHub 会请求其 [集成负责人](/glossary/integration-owner) 进行审查。其他文件也可以有负责人，这些负责人会列在仓库的 `CODEOWNERS` 文件中。

- **CI。** 自动化检查会构建你的更改、运行测试并检查代码风格。红色叉号表示某些检查失败。打开详细信息，修复与你的更改相关的问题，然后再次推送：将你的新提交发送到你的 pull request 分支，检查会再次运行。参见 [CI](/glossary/ci)。无法理解某个失败？在 pull request 上的评论里询问。

如果检查因你的更改而失败，在修复期间将你的 pull request 标记为草稿。这会告诉审阅者它尚未准备好。如果你确定失败与你的更改无关，则保持打开状态并注明。

### 等待审核 {#waiting-for-a-review}
这是困难的部分。审核需要时间，从几个小时到几周不等，而且没有任何保证。总是提交的 pull request 比审核员多。

有些事情通常会更快被发现：错误修复、小的更改，以及带有测试的 pull request。大的 pull request，或需要具有特定知识的人来审核的 pull request，需要更长时间。

等待的同时：- **保持更新。** 合并冲突意味着其他人修改了与你相同的行，Git 无法自动合并。GitHub 会在你的 pull request 上显示冲突。修复它，如果已经有一段时间了，就用最新的更改更新你的分支。[当 GitHub 显示有冲突时](/start/github#when-github-says-there-is-a-conflict) 在浏览器中可以看到具体操作方法。
- **再次查看。** 一天后，你通常会自己发现一些问题。
- **审查别人的工作。** 这是让队列顺利进行的最佳方式，对每个人都有帮助。测试一个 pull request 并评论“我用我的设备试过了，可以正常工作”，已经是一种有用的审查。

不要在 pull request 中或者通过私人消息去提醒维护者或集成负责人请求审查。机器人会通知相关人员。在描述中请求审查也是多余的：打开 pull request 已经会自动完成通知。

### 审查意见 {#review-comments}
在某个阶段，审查者会对你的工作发表评论，或者要求做出修改。这不是针对你个人的。审查者和你希望的一样：一个更好的 Home Assistant。如果你不理解某条评论，就问清楚。如果你认为审查者错了，可以礼貌地提出反对。解释你的理由。

在许多仓库中，当审查者请求修改时，机器人会将你的 pull request 变为草稿。一旦你处理完所有评论并且检查通过，选择 **准备审查**。然后机器人会通知审查者你已完成。

一些项目使用 AI 工具来帮助审查。对待它们的评论就像对待任何其他审查评论一样：如果你认为某条评论错了，可以简要说明。维护者拥有最终决定权。

### 过时与锁定 {#stale-and-locked}
一个pull request或一段时间没有活动的问题，会被机器人加上`stale`标签，并附带评论。如果之后没有任何操作，机器人会关闭它。任何活动都会重置计时：如果你仍在等待审核，一条评论就足够。有些标签，比如`no-stale`，可以让机器人保持距离。

一旦某个问题被关闭，另一台机器人会在一段时间后锁定对话。之后，只有对仓库有写权限的人才能评论。再次遇到同样的问题？请打开一个新问题，并链接旧问题。

各个仓库的时间设置不同：| 仓库 | 问题在多久后过期 | pull request在多久后过期 | 标签标记后多久关闭 | 关闭后多久锁定 |
| --- | --- | --- | --- | --- |
| [core](https://github.com/home-assistant/core/blob/dev/.github/workflows/stale.yml) | 90天 | 60天 | 7天 | 问题30天, pull requests 1天 |
| [frontend](https://github.com/home-assistant/frontend/blob/dev/.github/workflows/stale.yaml) | 90天 | 90天 | 7天 | 问题30天, pull requests 1天 |
| [home-assistant.io](https://github.com/home-assistant/home-assistant.io/blob/current/.github/workflows/stale.yml) | 60天 | 60天 | 7天 | 问题30天, pull requests 1天 |
| [supervisor](https://github.com/home-assistant/supervisor/blob/main/.github/workflows/stale.yml) | 30天（仅限错误） | 30天 | 7天 | 问题30天, pull requests 1天 |
| [operating-system](https://github.com/home-assistant/operating-system/blob/dev/.github/workflows/stale.yml) | 90天 | 90天 | 7天 | 问题30天, pull requests 7天 |
| [addons](https://github.com/home-assistant/addons/blob/master/.github/workflows/stale.yml) | 30天 | 未设置 | 7天 | 未设置 |
| android | 不活跃 | 不活跃 | 不活跃 | 未设置 |
| iOS | 未设置 | 未设置 | 未设置 | 未设置 |这些链接指向每个仓库在其 `.github` 文件夹中的配置。锁定时间在 `lock.yml`（前端为 `lock.yaml`），就在旁边。Android 仓库仍然有一个旧机器人的 [`stale.yml`](https://github.com/home-assistant/android/blob/main/.github/stale.yml)（问题为 90 天，pull request 为 30 天），但自 2021 年以来该机器人没有在那里标记任何内容。

## 做一个好邻居 {#being-a-good-neighbor}
- 一次不要打开超过五个pull request。等待一些合并后再打开更多。
- 不要打开依赖尚未合并的其他pull request的pull request。
- 只打开你打算完成的pull request。如果你不能继续，说明情况并关闭它。这没有什么可羞愧的。如果你卡住了，可以在[Discord](/start/where-we-talk)上寻求帮助。

## 已合并 {#its-merged}
恭喜你，并感谢你。你让Home Assistant对所有使用它的人都更好。

大多数更改会在下一个版本中提供给用户。需要包含在补丁版本中的修复？请在描述中清楚说明。审核者决定，并将其添加到下一个补丁发布的里程碑。

然后继续：打开另一个pull request，或帮助审核。每次都会变得更容易。
