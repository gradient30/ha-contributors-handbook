---
title: 发行笔记和发行方
description: 月度发行笔记如何汇合,如何帮助他们更好,发行派对是什么.
order: 1
---

# 发行笔记和发行方 {#release-notes-and-the-release-party}

每次发布都会有发布笔记:在[Home Assistant.io](https://www.home-assistant.io/)上的博客文章, 对许多人来说,这是他们唯一读到的关于释放的内容。 得到它的权利。

## 释放说明里有什么 {#what-is-in-the-release-notes}

发行笔记每月采用相同的结构:

- ** 介绍** 带有要点,并记录了最上面的发行方。
- **大特辑**,每部都有自己的部分,截图,经常是短视频.
- **整合**:新的整合,值得注意的改进,整合达到[质量尺度](/glossary/quality-scale)的新水平,整合现在可以从UI建立,整合被移除.
- ** 其他值得注意的变化**:值得了解的较小特征。
- ** 批量释放**:在月内添加,每批补丁释放的修补.
- 需要帮忙吗? 加入社区**:在哪里获得帮助,在哪里报告问题。
- ** Backward-incompatiable changes **:每个[向后仍处于不兼容状态的更改](/releases/guides/backward-incompatible-changes),每个集成组,以及一个开发者博客帖单,对于自定义集成开发者很重要.
- ** 所有更改**:与完整更改日志的链接。

完整更改日志列出发行时的每个合并pull request,与它的作者. 它由发布团队与[释放帮助脚本](https://github.com/home-assistant/hass-release)生成.

## 谁写的? {#who-writes-them}

发行笔记由发行团队在他人帮助下撰写. 帮助的人们在每一个发布帖子的顶端都得到了名声的感谢. 写出发行笔记并不是一个公开免费的,但你可以在几个方面提供帮助.

## 栈道如何帮助 {#how-you-can-help}

- ** 写一个好的 pull request 描述。 ** 发行注释作者读作pull requests以理解一个特性. 清晰的描述,带有变化的截图,可以节省他们很多时间.
- ** 写一个好向后兼容的更改部分。 ** 几乎照原样抄入发行笔记. 见[记录一个向后兼容的更改](/releases/guides/backward-incompatible-changes).
- ** 及时获得文件。 ** 没有文件的特性很难写,也很难链接到。 打开文件 pull request 与 `next` 分支的 home-assistant.io 并用代码 。 见[撰写文档](/writing).
- ** 审查β释放说明。 ** 在β周期间,发行笔记已经在[rc.home-assistant.io 互联网档案馆的存檔,存档日期2013-09-02.](https://rc.home-assistant.io/latest-release-notes/)发布. 发现一个错误,一个断掉的链接, 或某事不明? 在[Discord](https://www.home-assistant.io/join-chat/)上的[贝塔**](https://discord.com/channels/330944238910963714/427516175237382144)频道中报告,或在[Home Assistant.io](https://github.com/home-assistant/home-assistant.io)上打开一个问题或pull request。

## 释放方 {#the-release-party}

在发布日,有一个发布会:在[Home AssistantYouTube频道](https://youtube.com/@home_assistant)上的直播流. Home Assistant和 社区团队的 [Open Home Foundation](/glossary/open-home-foundation)将其组合起来。 他们走过新的事物,展示行动的特点。 有时客人会来谈他们的工作

录音嵌入在发行笔记的顶之一就是后期,以便以后可以观看.

## 补丁发布注释 {#patch-release-notes}

补丁发布没有获得自己的博客文章. 他们的修改被添加到该月的发行注释中,在**Patch发行**下,加上日期和修正清单.
