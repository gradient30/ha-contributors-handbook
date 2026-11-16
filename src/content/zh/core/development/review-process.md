---
title: 打开 pull request 之后
description: 打开 pull request 到 Home Assistant Core 之后会发生什么, 以及你能做些什么来帮助它。
sidebarGroup: Pull request
order: 3
---



# 打开 pull request 之后 {#after-you-open-a-pull-request}
您的 pull request 已经打开 。 现在它等待一个[审查](/glossary/review)。 接下来发生的事情在每一个 Home Assistant 寄存器中大多是相同的: bots, wait, Review 注释, and stale pull requests. [pull request和审查](/start/pull-requests#after-you-open-it) 解释这一切 。 本页添加了核心的特定内容.

## 谁审查 {#who-reviews}

维护者合并 pull request s. 在 `manifest.json` 中列出的 [融合所有人](/glossary/integration-owner) 整合的 [融合所有人](/glossary/integration-owner) , 当您更改时会被自动请求审查 。 但任何人都可以检讨:"我用我的设备测试了这个,它起作用了"已经有所帮助.

质量等级的新等级需要核心小组成员的批准。 见[提高融合水平;](/core/quality-scale/raise-tier#the-review).

## 自动审查员 {#automated-reviewers}

两名自动审查员在核心评论 pull request之前,人类看他们。 他们评论,他们不决定。

- QQ质量比标审查器**:当改变集成的pull request打开、重新打开或标记准备审查时运行。 它对照 [质量尺度](/core/quality-scale) 规则 `done` 或 `exempt` 在它的 `quality_scale.yaml` 中将 `done` 或 `exempt` 的整合标记 来检查变化, 并在每条断开一条的行上贴上内线注释 。 当没有任何东西违反规则时,它留下一个简短的评论。 非常大 pull request 被跳过 。
- ** 检查要求**:当 pull request 更改要求文件时运行 。 对于每个新版本或更新的Python软件包,它会检查源寄存器是否公开,您的描述链接到它(对于一个新软件包),或者与两个版本的更改日志或比较(对于更新),软件包是如何发布到PyPI的,等等. 报告将结果作为评论发表。

拱手一看他们的评论 就像你读评论一样拱手相让,

## 何谓封锁合并 {#what-blocks-the-merge}

在CI旁边,一个机器人对您的pull request设置了一些状态检查. 他们必须是绿色的,然后一个维护者可以合并它:

- `required-labels`:红色,而pull request没有类型标签,例如`bugfix`或`new-feature`。 机器人在模板的"变化类型"下从框中添加了这个标签,所以准确检查一个.
- `docs-missing`:红色,而pull request有`docs-missing`标签,或者当一个新的集成或平台在[Home Assistant.io](https://www.home-assistant.io/)上的文档pull request没有链接时。 该模板在"附加信息"下为该链接设置了一个字段.
- `cla-bot`:红色直到你签署Contributor License Agreement。
- `code-owner-approval`:对于白金整合,红色,直到其整合所有者之一批准pull request.
- `blocking-label-awaiting-frontend`:红色而pull request有`awaiting-frontend`标签,因为它等待前端的更改.

## 什么动作更快 {#what-moves-faster}

错误修正、 代码质量改进 和 pull request 测试在新功能之前进行 。 小的 pull request 在大号之前。 需要具备特定知识的改变,如建筑改变或不在身边的融合所有者,需要更长的时间。

测试比其他一切更有用 他们显示你的代码工作, 保持它的工作, 并帮助审查者理解 你解决的问题。

## 要求更改时 {#when-changes-are-requested}

当一个审查者要求更改时,一个机器人会把你的pull request变成草稿. 将您的修正作为新的承诺:不要修改、压碎或重新定位您已经推进的内容。 当您对每篇评论和CI通行证发表过讲话时,请选择** 准备审查**。 然后机器人让要求更改的审核者知道,这又是他们的一次。

## 不断更新 {#keep-it-up-to-date}

在一周左右没有活动后, [带入最近的 `dev`](/core/development/catching-up) 加上合并, 再进行测试 。 然后,你的pull request 准备好去当审查开始。

## 修复补丁释放 {#fixes-for-a-patch-release}

Home Assistant 每月发布一次, 中间有补丁发布 。 如果你的补丁应该进入下一个补丁发布, 在描述中那么清晰地说。 审查者检查它是否合格,并将其添加到下一个补丁发行的里程碑中.

## 使用等待 {#use-the-wait}

等待时检查其它 pull request 。 这是让队列移动,学习核心如何工作的最好方法. 告诉你要找什么
