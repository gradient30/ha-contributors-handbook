---
title: 作为贡献者成长
description: 在你的第一个pull request之后会发生什么。回顾、分类、负责一个整合、承担一个角色，以及它可能带来的发展。
sidebarLabel: 作为贡献者成长
order: 4.5
---



# 作为贡献者成长 {#grow-as-a-contributor}
你的第一次贡献已合并。接下来呢？此页面显示人们之后采取的路径，大致按照大多数人走的顺序排列。你不必走完所有路径，也没有终点。很多人通过长期专注于一件事而持续贡献多年。

每一步都会说明它的意义、所需条件以及如何达到那里。如果某些内容未在任何地方记录，本页面会明确说明，而不会随意猜测。

## 1. 成为常规贡献者 {#1-become-a-regular}
成长最简单的方法就是持续出现。在项目的同一部分完成第二次和第三次 pull request 会让你学到比第一次更多的东西，而且审核你贡献的人开始认识你的名字。

然而，维持 Home Assistant 运行的大部分工作并不是编写新内容，而是帮助已有的人和变更。这正是常规贡献者能够产生最大影响的地方。

### 审查 pull request {#review-pull-requests}
现在的 pull request 数量多于审查者。你提供的每条审查都会加快维护者最终审查的速度。你不需要任何权限即可进行审查：任何人都可以对 pull request 评论、测试或批准。

Core 和前端的 pull request 模板会在你打开自己的 pull request 时，要求你审查同一代码库中的另外两个开放 pull request。它们还会链接到一个尚未被审查的 pull request 搜索页面。这是一个不错的起点。

有用审查的特点：

- 使用你自己的设备或设置测试更改，并说明你的发现。例如，“我在我的设备上尝试过，工作正常”非常有帮助。
- 检查基本事项：模板是否已填写完整，检查是否通过，是否只做了一件事情？
- 当某些内容不清楚时提出问题。如果你不理解，下一位也不会理解。有关每个仓库的详细信息，请参见 [在 Core 中审查 pull requests](/core/development/reviewing) 和 [前端的审查和发布](/frontend/development/review-and-release)。总体流程在 [pull requests 和审查](/start/pull-requests) 中。

### 帮助处理问题 {#help-with-issues}
错误报告积累得很快。许多报告缺少日志、版本或复现步骤。你可以在不需要特殊权限的情况下提供帮助：

- 尝试在你自己的安装环境中复现错误，并评论说明发生了什么。
- 礼貌地询问缺失的细节。[报告错误](/start/report-a-bug)列出了每个代码库表单所要求的信息。
- 当发现重复问题时，指出它。
- 确认旧问题在最新版本中仍然存在，以防止它过时。

设置标签或关闭问题需要在 GitHub 上的权限，大多数贡献者没有。你会看到用于此目的的标签包括 Core 中和 [home-assistant.io](https://github.com/home-assistant/home-assistant.io) 上的 `needs-more-information`、前端的 `needs more information` 以及 Core 中的 `waiting-for-reply`。在寻找可以自己修复的东西吗？有些仓库会用 `good first issue` 或 `help-wanted` 标记问题，其中包括 Core、前端和 home-assistant.io。并不是每个仓库都使用这些标签，并且任意时刻带有这些标签的问题数量差异很大。

### 帮助他人 {#help-people}
回答问题是一种贡献，并且用户会立即感受到。

- 在 [社区论坛](https://community.home-assistant.io/) 和 [Discord](https://www.home-assistant.io/join-chat/) 上，帮助他人进行设置。[回答你的第一个问题](/community/first-contribution) 说明了如何操作，[欢迎新手](/community/guides/welcome-newcomers) 可以帮助你做好这件事。
- 在 [功能请求](https://github.com/home-assistant/feature-requests/discussions) 中，帮助塑造想法。解释请求背后的问题，指向现有请求而不是重复，并进行投票。产品团队使用功能请求来制定 [路线图](/roadmap/how-it-works) 。

## 2. 成为集成负责人 {#2-become-an-integration-owner}
[集成负责人](/glossary/integration-owner) 负责管理一个集成。你对设备或服务最了解，因此当它发生变化时，审查人员会倾听你的意见。

### 所需条件 {#what-it-takes}
集成的所有者列在 Home Assistant Core 中其 `manifest.json` 的 `codeowners` 字段内。要成为所有者，先打开一个 pull request，将你的 GitHub 用户名添加进去，然后运行 hassfest 来更新仓库的 `CODEOWNERS` 文件：

```shell
python3 -m script.hassfest
```

提交两个文件。pull request 的审核方式与其他的相同。先参与集成开发会非常有帮助。[拥有集成所有者](/core/quality-scale/integration-owner) 解释了该角色及其要求：所有者需要长期维护该集成。没有活跃所有者的集成可能会在质量等级上失去位置。

### 你将获得- **审核请求。** GitHub 会请你审核涉及你集成部分的 pull request，因为 `CODEOWNERS` 文件是从清单生成的。 {#what-you-get}
- **文档也是如此。** home-assistant.io 的 `CODEOWNERS` 文件与核心同步。如果你拥有该集成，你也拥有其文档页面，并会被要求审核其更改。
- **问题提及。** 当核心或 home-assistant.io 上的某个问题或 pull request 被打上与你的集成相关的标签 (`integration: <domain>`) 时，机器人会将你分配并在评论中提及你。

- **机器人命令。** 那条评论列出了只有该集成的集成所有者可以使用的命令，通过评论 `@home-assistant <command>`：关闭、重新打开或重命名问题，移除你的集成标签，以及添加或移除一些分诊标签，如 `needs-more-information`。在 pull request 上，你还可以将其标记为草稿，标记为可供审核，或更新其分支。未指明集成的命令仅在该问题或 pull request 拥有单一集成标签时才可使用。
- **任务问题。** 在 Core 和 home-assistant.io 中，只有 GitHub 组织的成员以及 `CODEOWNERS` 中列出的人可以打开任务类型的问题。其他人的任务问题会被自动关闭。

机器人的源代码位于 [OpenHomeFoundation/bots](https://github.com/OpenHomeFoundation/bots)。它准确显示了每个命令的功能。

## 3. 在你的领域中担任一个角色 {#3-take-on-a-role-in-your-area}
有些领域的角色拥有更多的责任。每个角色都有其自己的授予方式。

- **语言负责人。** 每种 Assist 理解的语言都有负责审查该语言在 [意图仓库](https://github.com/OHF-Voice/intents) 中更改的负责人。申请时，你需要是母语使用者，至少在意图仓库中做过两次 pull request，并帮助审查你语言的 pull request。查看 [语言负责人](/translate/voice/language-leaders)。
- **版主。** 版主负责保持论坛、Discord 和子版块的友好与安全。版主由其他版主提名，Open Home Foundation 的社区经理接受提名。查看 [版主管理流程](/community/guides/moderation#becoming-a-moderator)。
- **创作者网络。** 如果你制作关于 Home Assistant 的视频、帖子或其他内容，可以申请加入 [创作者网络](/community/reference/programs#creator-network)。
- **与 Home Assistant 合作。** 如果你在设备制造商工作，[与 Home Assistant 合作](/community/reference/programs#works-with-home-assistant) 项目适合你的公司。

## 4. 维护者和团队 {#4-maintainers-and-teams}
[维护者](/glossary/maintainer) 可以批准并合并仓库中的 pull request。每个仓库都有自己的维护者，通常组织在 GitHub 团队中，比如 `@home-assistant/core` 或 `@home-assistant/frontend`。[项目的组织方式](/start/organization#teams-in-codeowners) 列出了你将在 `CODEOWNERS` 文件中遇到的团队，以及每个团队负责的内容。

关于某人如何成为维护者，目前该网站上还没有记录。无论之后发生什么，进行审查、分类和管理一个集成都本身是有价值的。

## 5. 获得认可 {#5-get-recognized}
你的工作会出现在用户阅读的地方：

- **发行说明。** 在 [Home Assistant 博客](https://www.home-assistant.io/blog/) 上的发行说明中，通过他们的 GitHub 用户名感谢贡献者，这些用户名会显示在他们工作的功能旁边。帮助撰写发行说明的人也会得到感谢。
- **完整更新日志。** 每次发布都有完整的 Home Assistant Core 更新日志，从发行说明中的 **所有更改** 链接可查看。每个合并的 pull request 都会在日志中列出及其作者。

## 6. 与基金会进一步接触 {#6-go-further-with-the-foundation}
Home Assistant 是 [Open Home Foundation](https://www.openhomefoundation.org/) 的一个项目。还有更多可以参与的内容：

- **路线图。** 查看基金会正在进行的工作，以及你可以贡献的地方，请访问 [路线图](/roadmap)。
- **线下聚会和社区日。** 亲自见其他贡献者，或者自己主持一次聚会。基金会会报销主持者的一些费用。请参阅 [主持聚会](/community/guides/meetups)。
- **其他项目。** 基金会还拥有 ESPHome 和 Music Assistant 等项目，并与其他项目合作。其 [项目页面](https://www.openhomefoundation.org/projects/) 列出了所有项目，并附有各自的链接。
- **工作机会。** 基金会在其 [招聘页面](https://jobs.ashbyhq.com/openhomefoundation) 发布空缺职位。

## 与谁交流 {#who-to-talk-to}
- 不确定接下来该做什么？可以在 [**#developers**](https://discord.com/channels/330944238910963714/554842238073700352) 或 [Home Assistant Discord](https://www.home-assistant.io/join-chat/) 上的频道，或者你所在领域的频道里提问。[我们讨论的地方](/start/where-we-talk#by-area) 列出了这些频道。[项目论坛](https://discord.com/channels/330944238910963714/1346914401508392980) 则包含持续时间更长的项目和团队正在冲刺的更大主题。
- 想成为一个集成负责人吗？可以在该集成的 pull request 或问题中提问，让当前所有者看到。
- 想成为语言负责人吗？可以在 [意图讨论](https://github.com/OHF-Voice/intents/discussions) 中开启一个话题。
- 关于社区角色、聚会或社区日的问题？请发邮件给社区团队 [community@openhomefoundation.org](mailto:community@openhomefoundation.org)。
