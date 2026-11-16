---
title: 谁做什么?
description: 参与Home Assistant释放的人 以及他们每个人的行为
order: 2
---

# 谁做什么? {#who-does-what}

解脱是百千众生功德. 多数人从未将自己视为释放的一部分. 这是谁做什么。

## 贡献者 {#contributors}

每个人谁打开一个pull request。 对于发行,你的角色是:

- 如果您想要在本月的发行中合并到 pull request , 请在 β 开始前合并 。
- 当您的更改需要用户采取行动时, 写入清晰 [向后兼容的更改段](/releases/guides/backward-incompatible-changes) 。
- 在 `next` 的分支上打开文件 pull request,连同代码 。

## 维护者和融合所有人 {#maintainers-and-integration-owners}

[维护者](/glossary/maintainer) 审查和合并 pull request 。 [融合所有者](/glossary/integration-owner) 注意特定的整合 。 对于释放便是:

- 在β开始前决定什么被合并.
- 徘徊在β中,在他们最熟悉的代码中发现的问题。
- 标记修正,该修正应进入β或下一个补丁释放。 见[获得补丁释放](/releases/guides/patch-releases).

## Beta 测试器 {#beta-testers}

每个人都在[β 频道](/releases/first-contribution#2-join-the-beta-channel)。 他们提前一周在真正的家里 进行下一次发布 并报告休息情况 没有他们,那些虫子就会袭击所有人。 你可以成为一个:见[你的第一次贡献](/releases/first-contribution)。

## 文件审查员 {#documentation-reviewers}

他们审查并合并了pull request分支上的文档`next`,因此新功能的文档在发布日就已准备好. 见[撰写文档](/writing).

## 笔译员 {#translators}

他们在Lokalise上翻译了新文本。 翻译与每一个建筑一起被拉入,所以他们的工作在β中着陆,释放时没有单独步骤. 见[翻译](/translate).

## 释放小组 {#the-release-team}

发行团队自行运营发行. 仅限步骤:

- 创建β,释放,和补丁释放.
- 樱桃把里程碑的修补结果 放到释放分支
- 发布发行.
- 在他人的帮助下,撰写并发布发行笔记.

The release team uses the [释放帮助脚本](https://github.com/home-assistant/hass-release) to generate the changelog, cherry-pick milestones, and find documentation pull requests that are not merged yet.

## 创建者 {#creators}

[创建者网络](/community/reference/programs#creator-network)成员在β日与团队见面,可以在发布前给出反馈. 他们的视频和文章帮助许多人了解新的事物.
