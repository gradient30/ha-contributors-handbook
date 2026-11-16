---
title: 提交 Apple pull request
description: 核对表,pull request模板,以及Apple仓库审查期间的预期.
sidebarLabel: 提交 pull request
order: 6
---



# 提交 Apple pull request {#submit-an-apple-pull-request}
一旦您的更改准备好, 请在 [Home Assistant/iOS](https://github.com/home-assistant/iOS) 中打开 pull request 对应 `main` 。

## 在你打开它之前 {#before-you-open-it}

- ** 运行自动校正和链接**:`bundle exec fastlane autocorrect`,然后是 你不该这样做的。
- ** 运行测试**:`bundle exec fastlane test`。 添加或更新您改变的行为测试 。 记住 [补丁覆盖](/companion/apple/testing#patch-coverage)大门。
- ** 建造你碰过的东西。 ** 检查您的更改是否影响部件、 手表、 CarPlay、 扩展或 Mac 。 见 [开放供衡量的目标](/companion/apple/targets) 。
- 保持小点声 一个想法 pull request。 如果生长,则将其分为后续.
- ** 将未完成 见[每次更改的规则](/companion/apple/architecture#rules-for-every-change).
- ** 读 [AI 政策](/start/ai-policy) 。 ** 你可以使用AI工具,但你必须明白并能够解释你提交的一切. 调用自主代理的请求被关闭.

## 那个pull request {#the-pull-request}

不要删除模板中的任何内容. 填写 :

- **AI政策**:确认你读过,并选择一个确切的选项来描述你如何使用AI.
- **摘要**:你改变了什么,为什么。
- **Screenshots**:用于UI在前端外的变换,光线和暗模式.
- **Document**:在[用户文档](https://github.com/home-assistant/companion.home-assistant)中添加,更改或删除功能的更改需要pull request. 链接它。

草稿 pull request 是一个在一切被抛光之前, 及早获得方向或架构反馈的好方法 。

## 审查 {#review}

评论家们看:

- 是否属实。
- 重击 目录
- 试验范围。
- 是否可以维护 。
- 共享代码是否在正确的模块中 。

CI是审查的一部分,而不是替代它。 在重点后续行动中发表评论,再次进行插座和测试,并在CI为绿色时要求再次审查。 用你自己的话回答维护者的问题.

## 让你的分支更新 {#keep-your-branch-up-to-date}

每次 `main` 移动时不需要更新分支 。 当有原因时更新 : 冲突, 最近更改导致的 CI 失败, 或者对 `main` 您需要的固定 。 在审查之前,重新定位是好的。 一旦审查开始,请选择最不干扰现有讨论的更新。

## 字符串 {#strings}

翻译在[Lokalise](/translate)上管理. 如果添加或删除字符串,则使生成的文件保持一致。 不再使用的字符串从 Lokalise 和 Lokalise 的应用程序中删除 : 删除密钥** 工作流程, 见 [持续融合](/companion/apple/ci#on-your-pull-request) 。
