---
title: 您的第一个文件修复
description: 在文档中修补一些小东西, 直接从您的浏览器。 不需要设置
order: 1
sidebarLabel: 你的第一次贡献
---

# 您的第一个文件修复 {#your-first-docs-fix}

最快的开始方式是修复你注意到的东西 你搞错了吗? 还是旧版本的截图? 这是你的首次贡献。

不知道吗? 读者通过每页的反馈链接报告问题. 这些报告是[GitHub 上的公开问题](https://github.com/home-assistant/home-assistant.io/issues),其中许多是小修补,等待有人来取。

您需要免费的 [GitHub](https://github.com/) 账户 。 新建到 GitHub ? [使用 GitHub,](/start/github) 解释您在路上看到的单词, 如叉, 承诺, 和pull request 。

不适合自己编辑吗? 那也没关系。 在 ** 下选择 ** 提供反馈 ** 帮助我们在 [Home Assistant.io](https://www.home-assistant.io/) 页面底部改进文档 ** , 并描述什么是错的 。 这成了别人可以处理的问题。 您也需要一个 GitHub 的账户 。

## 打开页面 {#1-open-the-page}

1. 转到配套的 [Home Assistant.io](https://www.home-assistant.io/) 页面 。
2. 滚动到** 帮助我们改进我们的文档** 在底部,并选择**编辑**。
3. GitHub 显示页面的来源 。 在文件右上方选择铅笔图标, ** 编辑此文件 ** 。
4. 第一次,GitHub主动提出创建您自己的寄存器副本,称为[叉头](/start/github#fork). 接受这个 亦无别用.

## 做你的零钱 {#2-make-your-change}

页面以Markdown书写. 大部分是纯文本,所以可以像其他文本一样编辑. 看看其他页面是如何做事情的,比如链接和列表,并做同样的事情.

保持你的变化焦点:每pull request一个固定比十个更容易审查. 计划更大的事情, 像一个新的部分还是一个新的页面? 先读[样式指南承担起](/writing/reference/style)和[页面的结构](/writing/guides/structure)。

> [!TIP]
> 小事审查员经常指出:写 ** 安排 ** > **Devices & Services ** 在提及界面时用粗体表示,并全写"Home Assistant".

## 3. 提议更改 {#3-propose-the-change}

1. 选择 ** 承诺更改... **。
2. 在打开的窗口中,写一个简短的描述你所改变的东西,比如"给备份菜单的名字".
3. 选择**提议更改黏度**。

GitHub在叉子中保存您的零钱, 并显示您的改变 。 此时在自己的编辑中发现错误? 没问题,反正打开pull request,然后修复它。 第六步解释如何.

## 打开 pull request {#4-open-the-pull-request}

1. Summit 选择 ** 创建 pull request 。
2. 检查顶部的基部分支. 修复现有文件? 它必须说`current`:释放人员的文件正在运行中。 如果上面写了别的东西 改一下菜单
3. 填写模板。 不要删除任何文本:它帮助审查者. 在** 更改类型** 下,请检查符合、通常为** 拼写、语法或其他可读性改进** 或** 当前文件中经过调整的缺失或不正确信息** 的框。 在**检查清单**下,检查适用的框。
4. Summit 选择 ** 创建 pull request 。

就是这样。 您的 pull request 现在已经公开了, 正确的人 由自己通知。 你不需要要求任何人审查

## 5.  检查预览 {#5-check-the-preview}

在您打开 pull request 几分钟后, 一个与 ** Deplocation Preview** 链接的机器人评论 。 那是你改变的完整网站 打开它,检查你的页面 看起来像你想的那样。

## 6.  审查和合并 {#6-review-and-merge}

维护者审查您的更改 。 GitHub 通过电子邮件或github.com发送通知, 取决于您的设置 。

- ** 建议? ** o 直接从pull request接受**承诺建议**。
- 想要改变自己吗? 在您的叉中再次编辑文件, 在您的 pull request 的分支上, 以及 pull request 的更新本身 。 [使用 GitHub](/start/github#7-respond-to-the-review)显示在哪里找到它。
- 你不明白的问题吗? 问. 评论家宁愿解释 也不愿看到你的猜测

一旦你的pull request被合并,Netlife会公布你的固定 Home Assistant.io。

## 接下来是什么 {#what-is-next}

- 硕修几事. 大多数硕名的普通医生从打字开始。
- 最好用每张屏幕的截图走过去? 论坛上的社区指南 [编辑文档并在 GitHub 上创建 pull request](https://community.home-assistant.io/t/editing-the-documentation-and-creating-a-pull-request-on-github/9573) 显示他们。
- 准备做更大的改变吗 [本地预览网站](/writing/guides/local-preview).
