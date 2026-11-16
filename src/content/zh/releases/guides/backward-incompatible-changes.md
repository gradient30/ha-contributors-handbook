---
title: 记录一个向后兼容的更改
description: 当您的更改意味着用户必须做一些事情时,告诉他们什么是破碎的,如何修复,以及为什么. 这段文字最终出现在发行笔记中.
order: 2
---

# 记录一个向后兼容的更改 {#document-a-backward-incompatible-change}

向后不兼容的改变,是指要求人们在更新后在自己身边做一些事情,比如改变自己的配置,自动化,或者仪表板. 努力避开他们 当一个是不可避免的时,它必须加以很好的解释,因为成千上万的人在更新之前就读了它。

## 如果你能避免的话 {#avoid-it-if-you-can}

在写出向后兼容的更改之前, 请检查是否可以避免 :

- 旧方式能否在新方式旁边工作一段时间? 那么,它是一个[折旧](/releases/guides/deprecations), 不是一个落后的不兼容的变化。
- Home Assistant 可以自动迁移旧配置吗 ? 那就没人可以做任何事了

## 当它向后不兼容时 {#when-it-is-backward-incompatible}

要问的问题是:这种变化能否在更新后立即影响到某人? 将您的 pull request 标为向后不兼容的更改, 并标为 ** breaking 更改 ** 段和 `breaking-change` 标签, 当 :

- 它立刻打破了东西,没有第一个 [折旧](/releases/guides/deprecations)。 用户没有事先被告知,在更新之前没有机会采取行动。
- 它在腐烂期过后会从整合中移除一些东西. 用户被以 [修理](/glossary/repair) 警告, 但其中一些人可能没有对此采取行动, 移除仍然影响着他们.

当:

- Nothing breaks.
- 它删除了已贬值的[核心 API](/core/development/deprecating#developer-facing-deprecations),像帮助者或常数一样,在其贬值期之后,在Home Assistant Core中没有集成或其他代码使用. 只有自定义集成仍然可以受到影响,其开发者在 [开发能使博客](https://contributors.home-assistant.io/blog/) 开始贬值时被告知.

最低折旧期,即用户所见的6个月和核心API的12个月,在[贬值的东西](/releases/guides/deprecations#how-long)中。

## 是吗 pull request {#mark-the-pull-request}

pull request [核心存储器](https://github.com/home-assistant/core) 的模板有一类更改清单 。 请检查access-date=中的日期值 (帮助) ** 当当前功能中断时,如上所述,请检查access-date=中的日期值 (帮助) ** 当中断时,请检查access-date=中的日期值 pull request 然后得到`breaking-change` 标签, 即将您的文本放入发布注释中 。

## 写入向后兼容的更改部分 {#write-the-backward-incompatible-change-section}

pull request 模板以 ** 中断更改** 部分开始 。 模板直截了当地说:告诉用户什么中断,如何让它再次工作,以及为什么. 文本随发行笔记一起发布,所以为用户而不是开发者写.

一个好的后向不兼容的修改部分回答了三个问题:

1. *什么改变了* 描述用户看到的,而不是代码. "`uptime`传感器被移除"的作品. "重塑感应平台"没有.
2. 我该怎么办? 给这些具体步骤。 如果用户需要更改YAML,请显示新的YAML.
3. 为什么? 一两句已足. 人们在理解原因后更容易接受变化.

例如:

```markdown
The **Subscribed to Xbox Game Pass** binary sensor has been removed,
because it never worked. The Xbox API always reported `false`, whether
you were subscribed to Game Pass or not.

If you use this binary sensor in an automation or a dashboard, remove it.
```

## 提示 {#tips}

- 写下来让不知道融合的人理解 许多人读到每一个落后的不相容的变化,只是为了检查它是否影响他们.
- 使用用户在UI中看到的名称命名集和更改的实体,动作或选项.
- 别藏着淳洁 如果有东西淳朴地停止了工作,在第一句中就这么说.
- 将一节保留在 pull request 中, 更新审查时的变化变化 。
- 跟着[用户文档的写样式](/writing/reference/style)。 释文亦用.

## 你的短信会怎样 {#what-happens-with-your-text}

发行准备时,发行团队会收集所有合并的pull requests与`breaking-change`标签的后向不兼容的更改部分. 它们最终出现在**Backward-uncompatiable changes**的发行注释中,按集成分类,链接到您的pull request和文档. 发布注释作者可以编辑您的文本,以便清晰和一致.

反向不兼容但仅影响开发者的更改, 如更改为 Python API,改用开发者博客. 发布说明与这些员额有关。
