---
title: 打开 pull request
description: 如何打开前端 pull request 供维护者审查 。
order: 7
---

# 打开 pull request {#open-a-pull-request}

您的更改和 [检查](/frontend/development/testing) 通过 。 在晋级前,您需要的就是这些 。 每个寄存器的一般步骤在[pull request和审查](/start/pull-requests)中。

## 准备好检讨后再打开 {#open-it-when-its-ready-for-review}

当您的更改完成后打开 pull request 您想要重审, 不要尝试什么 。

每个{ 22} 需要时间的人 分门别类,标签,审查, 当它是一个草稿。 要进行实验,请在您的 [叉头](/glossary/fork) 中按到分支 。 你可以看到结果 没有打开任何东西。

如果CI在打开后失败,请修复. [一般指南](/start/pull-requests#the-bots-go-first)解释何时把它标为草案 同时。

## 写一个短标题 {#write-a-short-title}

标题告诉维护者什么变化,用几句话来说。 也终於发行笔记. 使其简短和有意义:

- 好:“不可用实体的 Fix 牌卡图标颜色”
- 好:"添加搜索到标签拾取器"
- 无帮助:"Fix bug","Update hui-tile-card.ts",或"Changes"

## 填入模板 {#fill-in-the-template}

使用 [pull request 模板](https://github.com/home-assistant/frontend/blob/dev/.github/PULL_REQUEST_TEMPLATE.md) 。 遍历每一节,只删除模板指示您在不应用时删除的部分. 如 [审查和发布](/frontend/development/review-and-release#before-review) 解释, 当模板缺失或不完整时, 检查失败 pull request 。

- 以Breaker为代言人,以Fre 在这一轮中,以Free为代言人。 为用户而不是维护者写. 无中断时删除该部分。 帮助你决定。
- ** 拟议变动**:说明哪些变动和为何变动,因此,审查员得到概览。 数句已足. 不要描述每一行代码: diff已经显示了这一点. 如果你使用AI工具,不要让他们为你写长篇描述. 以己语写之.
- **Screenshots**:在截图前后添加,或短视频,用于任何可见的东西. 如无可见更改,则删除该区域。
- ** 更改类型**:检查一个方框。 如果您需要两个, 请将 pull request 拆分 。
- ** 补充资料**:将它处理的问题与任何相关的后端或文档pull request联系起来。
- ** 核对清单**:核对正确的框。 只有你能说,你理解代码,测试它。

## 处理副驾驶审查 {#handle-the-copilot-review}

打开 pull request 后, GitHub Copilot 进行第一次审查, 并留下评论 。 评论从一个摘要开始, 像这样一个pull request 在那里,它发现没有 弥补:

![pull request的副驾驶评论,标题是"批准" 建议,这句话概括了变化, 和无争议的行](/_astro/copilot-review.BBnvbTIO_XiVAU.webp)

- 若一评有理,修之而推之.
- 如果它不这样做,就回答评论并解释原因. 那样,维护者就会看到你看它, 以及你为什么离开它。

不要让副驾驶的评论没有答案. 维护者审查时会读到这些答案。
