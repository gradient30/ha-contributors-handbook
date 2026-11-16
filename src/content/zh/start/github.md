---
title: 使用GitHub，无需成为开发者
description: 什么是仓库、问题、分叉、分支、提交和pull request，以及如何完全在浏览器中对Home Assistant进行小的修改。
sidebarLabel: 使用 GitHub
order: 2
---



# 使用GitHub，无需成为开发者 {#use-github-without-being-a-developer}
Home Assistant的大部分时间都花在了 [GitHub](https://github.com/home-assistant) 上：代码、文档、错误报告，以及关于更改的讨论。GitHub 是开发者为开发者创建的，这一点很明显。文字显得有些奇怪，界面很繁忙，第一次使用时可能会感觉像走进了别人的厨房。

不过，你不需要成为开发者也能使用它。修改文档中的一句话、报告一个错误，或对翻译文件提出更改建议，都可以在浏览器中完成，无需安装任何软件。本页面解释了你可能遇到的一些词汇，并带你从头到尾完成一个小修改。

## 创建一个账户 {#create-an-account}
你需要一个免费的 GitHub 账户来报告错误、发表评论或提出更改。阅读则无需账户。

1. 访问 [github.com/signup](https://github.com/signup)。
2. 按照步骤操作。GitHub 会要求你验证你的电子邮件地址：请完成验证，因为在验证前有些功能无法使用。
3. 启用 [两步验证](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication)。GitHub 强烈建议这样做，因为它可以保护你的账户安全。

你的用户名是公开的，你在 GitHub 上写的所有内容也是公开的。选择一个你愿意让人看到与你的贡献一起出现的名字。

## 用简单的语言讲述的词汇 {#the-words-in-plain-language}
GitHub 反复使用少量词汇。一旦你了解了这些词，屏幕内容就会更容易理解。

#

## 仓库 {#repository}
一个 [仓库](/glossary/repository)（或“repo”）是一个项目：一个文件夹加上对这些文件所做的每一次更改的完整历史。Home Assistant 有很多仓库。文档存放在 [home-assistant/home-assistant.io](https://github.com/home-assistant/home-assistant.io)，界面在 [home-assistant/frontend](https://github.com/home-assistant/frontend)，而 Home Assistant Core 在 [home-assistant/core](https://github.com/home-assistant/core)。每个仓库都有自己的问题、pull request 和维护者。

#

## 问题 {#issue}
一个 [问题](/glossary/issue) 是关于某个问题的报告，比如错误或页面内容不正确。任何人都可以在公共仓库中创建问题，任何人都可以评论。问题不是用于支持问题或功能建议的地方：请查看 [我们讨论的地方](/start/where-we-talk) 了解这些内容应该去哪里。

### 派生仓库（Fork {#fork}
[派生仓库](/glossary/fork) 是你在自己账户下的仓库副本。你不能直接更改 Home Assistant 仓库，但你可以更改你的副本，然后向原始仓库提议你的更改。你不必自己创建派生仓库：GitHub 会在你第一次编辑文件时为你提供创建的选项。

### 分支 {#branch}
一个 [分支](/glossary/branch) 是仓库中独立的更改线路。它让你可以在不影响主版本的情况下进行工作。每个仓库都有一个主分支，pull request 会进入该分支：`dev` 用于 Home Assistant Core 和前端，`current` 用于文档的修复。每个区域的首次贡献页面会告诉你使用哪一个。

#

## 提交 {#commit}
一个 [提交](/glossary/commit) 是一次保存的更改：包括你修改的文件、修改者、时间，以及简短的信息说明你做了什么。当你在 GitHub 上保存编辑时，你就完成了一次提交。

### pull request {#pull-request}
一个 [pull request](/glossary/pull-request) 是一个提议：“这里有一个更改，请接受它”。它会准确显示你所做的更改，对其运行自动检查，并有自己的讨论区，人们可以在其中讨论它。尽管名字叫拉取，你实际上并不会拉取任何东西。可以把它看作是请求维护者将你的更改合并进来的请求。

### 审查 {#review}
[审查](/glossary/review) 是指在你的 pull request 提交之前有人阅读它。审查者可以批准、评论或要求修改。有时他们会建议一个具体的编辑，你可以通过一次选择来接受。

#

## 合并 {#merge}
[合并](/glossary/merge) 一个 pull request 意味着将它的更改纳入仓库。只有维护者可以合并。当你的 pull request 显示 **已合并** 时，你的更改已成功纳入：干得好。

### 你还会看到的一些术语 {#a-few-more-youll-see}
- **Push（推送）**：将提交从其他地方发送到 GitHub。如果你只在浏览器中编辑，GitHub 会为你执行此操作，你可以忽略这个词。
- **Merge conflict（合并冲突）**：你的更改和其他人的更改修改了同一文件的同一行，Git 无法决定保留哪一个。参见 [当 GitHub 说存在冲突时](/start/github#when-github-says-there-is-a-conflict)。
- **Draft（草稿）**：尚未准备好进行审查的 pull request。
- **Checks（检查）**：在每个 pull request 上运行的自动化测试。绿色勾表示通过，红色叉表示某些测试失败。参见 [CI](/glossary/ci)。

## 在浏览器中做一个小更改 {#make-a-small-change-in-your-browser}
这是完整的流程，从你发现错误到合并修复。示例是对 [home-assistant.io](https://www.home-assistant.io/) 文档的修复，因为大多数人都是从这里开始的。其他仓库的操作方式相同，只是分支和模板不同。

#

## 1. 打开文件 {#1-open-the-file}
每一页文档底部都有一个 **帮助我们改进文档** 部分，其中有一个 **编辑** 链接。选择它，GitHub 会打开该页面的源文件。

在任何其他仓库中，浏览文件列表并选择文件名即可。

#

## 2. 开始编辑 {#2-start-editing}
选择文件上方的铅笔图标。第一次操作时，GitHub 会提示你需要自己的仓库副本才能进行更改。选择 **Fork this repository（分叉此仓库）**。GitHub 会在你的账户中创建分叉，并打开编辑器。

### 3. 进行修改 {#3-make-your-change}
在编辑器中修改文本。保持只改一件事：一个拼写错误、一条过时的步骤或一句不清楚的句子。小的修改比大的修改更快被审查。

选择 **预览** 来查看你的修改效果。

### 4. 提议更改 {#4-propose-the-change}
1. 选择 **提交更改...**。
2. 在 **提交信息** 字段中，写下你所更改内容的简短描述，例如“修正设置菜单的名称”。
3. 选择 **提议更改**。

GitHub 会将你的更改保存为你分支中的一次提交，并显示你所更改的内容。

### 5. 打开 pull request {#5-open-the-pull-request}
1. 选择 **创建 pull request**。
2. 检查顶部的基础分支：你的 pull request 将要合并到的分支。对于文档修复，这是 `current`。如果显示的是其他分支，请在该菜单中更改。
3. 写一个清晰的标题，例如“修复备份页面上过时的菜单名称”。
4. 在描述中填写模板。保留其标题和复选框，并勾选适用的复选框。模板是为了帮助审核者，而不是为了测试你。
5. 选择 **创建 pull request**。

就是这样。你的提案现在是公开的，相关人员会自动收到通知。你无需向任何人请求审查。

### 6. 让机器人自行处理 {#6-let-the-bots-do-their-thing}
几分钟内，会发生几件事：

- 机器人会添加标签，并开始自动检查。
- 对于文档，机器人会发布一个[部署预览](/glossary/deploy-preview)的链接：整站已经包含了你的更改。打开它并检查你的页面。
- 在代码仓库中，比如Home Assistant Core或前端，机器人会第一次请求你签署[Contributor License Agreement](/start/licensing)。点击它的链接操作。你只需做一次，在你完成之前，你的pull request无法合并。

如果检查失败且你不明白原因，可以在你的pull request上留言问。这是一个正常的问题，没有人指望你第一次就能看懂检查日志。

### 7. 回复审查 {#7-respond-to-the-review}
迟早会有审查员查看你的更改。根据仓库的繁忙程度，这可能需要几个小时或几周。[pull request和审查](/start/pull-requests#waiting-for-a-review) 解释了原因，以及你在等待时可以做什么。

审查的评论会显示在你的 pull request 的 **对话** 标签页中，并在 **已更改的文件** 标签页中显示在相关行旁边。

- **回复评论**，请在评论下方撰写你的回复。  
- **接受建议更改**，选择 **接受建议**。有多个建议吗？在每个建议上选择 **添加建议到批处理**，然后选择 **提交建议** 一次性应用它们。  
- **自行更改内容**，前往你的 fork，使用文件列表上方的分支菜单切换到你的 pull request 分支，然后像以前一样编辑文件。提交时，选择直接提交到该分支，你的 pull request 会自动更新。  
- **处理完评论后**，选择 **解决对话**，让大家清楚剩余的问题。  

审查评论针对的是更改内容，而不是你本人。如果你认为审查者有误，请礼貌地说明原因。如果你不理解评论，请提问。审查者更愿意解释，而不是看到你自行猜测。在许多 Home Assistant 仓库中，当审阅者要求修改时，机器人会将你的 pull request 转为草稿。处理完所有内容后，选择 **准备审阅** 来通知他们。

### 8. 已合并 {#8-merged}
当维护者合并你的 pull request 时，它会显示 **已合并**。你的更改现在是 Home Assistant 的一部分。在 `current` 上的文档修复会自行上线：该分支就是 [home-assistant.io](https://www.home-assistant.io) 发布的内容。代码更改会在下一个版本中到达每个人。

有时 pull request 会在未合并的情况下被关闭。审查者通常会说明原因：问题以其他方式修复，或不适合合并。这种情况也会发生在有经验的贡献者身上，并不是对你的评判。

## 当 GitHub 表示存在冲突时 {#when-github-says-there-is-a-conflict}
如果在你的 pull request 等待时有人更改了相同的行，GitHub 会显示该分支存在冲突。对于简单的冲突，你可以在浏览器中解决：

1. 在你的 pull request 上，选择 **解决冲突**。
2. GitHub 会显示两个版本，在 `<<<<<<<`、`=======` 和 `>>>>>>>` 等标记之间。编辑文本，使只保留你想要的版本，并删除标记。
3. 选择 **标记为已解决**，然后 **提交合并**。

并非所有冲突都能在浏览器中解决。如果 **解决冲突** 不可用，或者你不确定保留哪个版本，请在你的 pull request 上通过评论寻求帮助。

你的分支只是落后，没有冲突吗？那么 GitHub 会在 pull request 底部附近显示 **更新分支** 按钮。选择它可拉取最新更改。

## 老实说，什么令人困惑 {#what-is-confusing-honestly}
有几件事几乎会让每个人在第一次遇到时感到困惑：- **你的更改似乎消失了。** 当你提出更改时，它存在于你的分支中，而不是在Home Assistant仓库中。这是正常的。当pull request合并后，它才会被移动过去。
- **什么都有两份。** 你的分支和原始仓库看起来几乎一样。检查左上角的名字：你的用户名，或者`home-assistant`。
- **错误的基础分支。** 针对错误分支的pull request是新手常犯的错误。你可以之后更改它：在pull request的标题旁选择**编辑标题**，在基础分支菜单中选择另一个分支，然后点击**更改基础**。
- **通知的数量。** 一旦你打开pull request，GitHub会给你发送所有发生在它上的事情的邮件。你可以在[通知设置](https://docs.github.com/en/subscriptions-and-notifications/get-started/configuring-notifications)中进行调整。

- **沉默。** 一段时间没有回应并不意味着无人关心。pull request 比评论者还多。

## 接下来去哪里 {#where-to-go-from-here}
- [你的第一次贡献](/start/first-contribution)：选择你想要处理的内容。
- [你的第一次文档修正](/writing/first-contribution)：这个循环，用于文档。
- [pull request和审查](/start/pull-requests)：当你打开一个 pull request 后会发生什么，更详细说明。
- GitHub 自己的 [Hello World](https://docs.github.com/en/get-started/start-your-journey/hello-world) 教程，如果你想先在自己的仓库中练习。
