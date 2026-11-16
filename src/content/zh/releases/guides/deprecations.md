---
title: 贬值的东西
description: Home Assistant的堕落政策,对使用它的人意味着什么,堕落如何出现在发行笔记中.
order: 3
---

# 贬值的东西 {#deprecate-something}

A [折旧](/glossary/deprecation) 是计划未来的一个落后- 不兼容的更改 。 旧的方式持续工作一段时间,每一个使用它的人都会受到警告,只有在那个时期之后才会被移除. 它使人们有时间以自己的速度前进。

此页面是政策,以及它对于用户和发行注释的意义. 如何在代码中贬低某物,包括修补问题,翻译字符串,以及正确的严重程度,属于核心和集成领域:[折旧](/core/development/deprecating).

## 规则 {#the-rule}

任何被移除的东西必须先贬值。 即便你认为只有少数人使用它, 也依然如此, 因为一个实体,动作,或者选项 可以用在自动化,脚本和仪表板上, 其他人看不到。

## 多长时间 {#how-long}

| 谁受影响 | 最低期限 |
| --- | --- |
| 用户:YAML配置,动作,实体,属性,集成 | 6个月 |
| 开发者:自定义集成所使用的常数、 帮助者、 实体属性和平台 API | 12个月 |

拆解旧方式的解脱名称. 当人们需要更多时间时,这一期限可以延长,但从未缩短。

## 用户看到的 {#what-users-see}

向用户询问某事的贬值在 **Settings ** > 中以 [修理](/glossary/repair) 显示 。 ** 系统** > ** Repairs**,仅涉及其影响的设施。 修理说明什么是去,什么时候,做什么。 受影响者被告知,没有受影响者不会被打扰。

## 在发行笔记中 {#in-the-release-notes}

一次贬值两次到达释放说明:

1. ** 当开始时。 ** 将某物贬值的版本的发布注释可以将其列在**Backward-uncompatiable changes**下,比如"升时传感器已贬值,在未来发布时会被移除. 使用新的最后一个重启传感器。”
2. ** 当它结束时。 ** pull request去除旧方式的,在贬值期之后,当它仍然可以影响没有对贬值采取行动的用户时,就是一种落后的不兼容的变化. 它来自pull request的文本最终出现在该版的同一节. 见[当它向后不兼容时](/releases/guides/backward-incompatible-changes#when-it-is-backward-incompatible).

影响自定义集成开发者的PythonAPI的折价在[开发能使博客](https://contributors.home-assistant.io/blog/)上公布. 发布笔记链接了该发布中最显著的帖子,旧代码在仍然有效的同时记录了警告.

## 在 pull request 中 {#in-the-pull-request}

pull request [核心存储器](https://github.com/home-assistant/core) 的模板有这样的变化类型 : 检查 ** 折旧 ** 当断裂发生于将来, ** 断裂 ** 当它发生于现在。 开始贬值的pull request是第一个。 结束它的那个是第二个,除非它只删除一个在Home Assistant Core中已无用的核心API.
