---
title: 向后兼容的更改
description: 一个需要用户或开发者改变自己一方的东西的更改,比如他们的配置或他们的自定义集成.
sidebarGroup: 贡献
term:
  aliases:
  - backward-incompatible changes
  code:
  - breaking-change (label)
  formerly:
  - breaking change
  related:
  - deprecation
  - release
  - pull-request
  autolink:
  - backward-incompatible change
  - backward-incompatible changes
---

# 向后兼容的更改 {#backward-incompatible-change}

- 代码 : `breaking-change (label)`
- 又:向后兼容的变化
- 原名:打破更改(旧名:别在新文字中使用)

使用可影响用户获得 `breaking-change` 标签的向后兼容的更改来pull request,并在描述中解释其变化和应做什么. 该文本最终被收录在**Backward-uncompatible changes**部分发行注释中. 移除一个已贬值的核心API在其贬值期过后, 当只有自定义集成仍然可以使用时, 无法获得标签 : 这些开发者在开发者博客上听到它。 有细节

pull request Home Assistant Core 的模板和标签称之为"破碎的改变". 两者同义. 发行笔记称其为逆向变化,你所写的一切都应该如此.

如果可能的话, 更改不是向后兼容的 : 它首先从 [折旧](/glossary/deprecation) 开始 。

## 相关条件 {#related-terms}

- [折旧](/glossary/deprecation):宣布某物会在稍后的发行中被移除,同时它一直工作到那时,所以人们可以继续前进.
- [发布](/glossary/release): Home Assistant的新版本 。 每个月的第一个星期三都出场 中间放出补丁
- [调用请求](/glossary/pull-request):在GitHub上请求将一个更改合并到一个寄存器中,在它进入之前要经过审查.
