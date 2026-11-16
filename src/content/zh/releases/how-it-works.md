---
title: 如何释放工作
description: Home Assistant的月发布周期,从代码第一行到最后补丁发布.
order: 2
sidebarLabel: 它是如何运作的
sidebarLabel: 工作原理

---

# 如何释放工作 {#how-releases-work}

在固定的时间表上发布。 每个月的第一个星期三推出新版本。 前一周,有一个β。 发布后,随即发布带有修正的补丁,通常每周一次. 然后循环又开始了。

[Open Home Foundation](/glossary/open-home-foundation) 设置此调度 。 [释放 FAQ](https://www.home-assistant.io/faq/release/)在Home Assistant。 io为用户描述.

## 循环一览 {#the-cycle-at-a-glance}

| 何时 | 发生什么事 |
| --- | --- |
| 整个月 | 新的特征和修还可以合并到发展分支. 夜造诸天 今晚造诸天. |
| 裘莉,在释放前一个星期 | β开始。 开发分支被冻结成β,第一个结束于`b0`. |
| 在β周期间 | 修复在新β中发现的β土地的问题:`b1`,`b2`等. |
| 每月第一个星期三 | 释放,像`2026.11.0`。 发布笔记开始直播,还有发布会现场直播. |
| 之后的几周 | 带有错误修正的补丁释放, 如 `2026.11.1` 和 `2026.11.2` 。 目标是每周一次,目标是星期五。 |

具体日期见[事件日历](/community/reference/events).

## 开发 {#development}

所有新工作都进入每个寄存器的`dev`分支,通过pull requests. 该分支上的版本总是指向下一个发布,带有开发标记,如`2026.11.0.dev0`.

每天晚上,从`dev`的分支造出一个建筑,其版本类似`2026.11.0.dev202610100230`. 想要生活在边缘的人可以通过dev通道运行这些建筑. 这是新代码第一次与真正的家庭相遇的地方.

用于新功能的文档同时在 `next` 分支的 home-assistant.io 上编写. 它和释放一起生活 见[撰写文档](/writing).

## 贝塔 {#the-beta}

在发布前一周的星期三,发布团队从`dev`分支创造出第一个β. 从那一刻起,发布功能完成:新功能进入下一个月.

β在[β 频道](/releases/first-contribution#2-join-the-beta-channel)上发布. 所有加入频道的人都会得到最新消息 [β发布注释](https://rc.home-assistant.io/latest-release-notes/)和β的文档在rc.home-assistant.io上.

在β周期间,测试者会报告问题,开发者会将其修复. 这些修补被合并为 `dev` 首先,然后发布团队复制 进入β。 这抄袭叫做摘樱桃 每轮修正都变成了新的β. 见[获得补丁释放](/releases/guides/patch-releases) 如何选择一个固定 。

## 释放 {#the-release}

在月的第一个星期三,最后一个β成为释放.窖中装置会得到更新。

同时,发布笔记在[博客 Home Assistant](https://www.home-assistant.io/blog/categories/core/)上发布,新功能的文档在home-assistant.io上直播. 当天晚些时候,有一个发布会:YouTube上的关于新事物的直播流. 见[发行笔记和发行方](/releases/guides/release-notes)。

## 补丁释放 {#patch-releases}

有些bug只在多人运行发布后出现. 补丁释放 修复这些。 它们只包含bug修正,从不新增功能,目标为每周一个补丁发布,瞄准星期五,直到下一次发布出来.

每个补丁发布会得到一个简短的更改日志,在**Patch发布**下加入该月的发布注释.

## 前端和其他部分 {#the-frontend-and-other-parts}

用户界面,即前端,有自己的寄存器和版本号,但遵循相同的节奏. 一个新的前端版本作为发布工作的一部分被撞入了核心,因此每个Home Assistant释放的舰只都有一个属于它的前端.

每次 Lokalise 这将翻译从 Home Assistant 中抽取, 所以翻译不需要自己的释放步骤 。 见[翻译工作方式](/translate/how-it-works).

## 释放小组做了什么 {#what-is-done-by-the-release-team}

有些步骤只由释放小组完成,你不必担心:

- 创建β,释放,和补丁释放.
- 选择和选樱桃 修复进入β或补丁释放。
- 发布构建,并更新安装检查更新的版本信息.
- 在他人的帮助下,撰写并发布发行笔记.

其他人可以做的是让这些步骤变得容易:测试β,明确报告问题,写一个好的后向不兼容的更改部分,并让pull requests及其文档及时准备.
