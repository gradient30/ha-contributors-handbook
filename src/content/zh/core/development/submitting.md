---
title: 提交 pull request
description: pull request对于Home Assistant Core,从分支到将消息输入模板,新集成,以及依赖性更新,具体是什么?
sidebarGroup: 调用请求
order: 2
---



# 提交 pull request {#submitting-a-pull-request}
更改通过GitHub上的Home Assistant Core通过[pull requests](/glossary/pull-request),对准`dev`分支。 pull request 如何在每个 Home Assistant 寄存器中工作, 从保持小到等待审查, 都在 [pull request和审查](/start/pull-requests) 上 。 先念这个. 本页添加了核心的特定内容.

## 在你打开它之前 {#before-you-open-it}

- 将您的obs基于最新的 `dev` 。 见{Lo}.
- 通过[发展清单](/core/development/checklist)。
- 运行测试和[线条](/core/development/checks)。
- 实际上运行Home Assistant与您的零钱,并尝试它。 根本没用的密码 是浪费每个人的时间 包括你的
- 更改核心工作方式请检查[结构决定](https://github.com/home-assistant/architecture/tree/master/adr). 如果需要新的决定, 请在写代码前启动 [讨论情况](https://github.com/home-assistant/architecture/discussions) 。

## 提交并按 {#commit-and-push}

为每个 pull request 工作自己的分支, 永远不要在 `dev` 上 :

```shell
git fetch upstream
git checkout -b add-battery-sensor upstream/dev
```

等你的零钱准备好 承诺并推到你的叉子上

```shell
git add .
git commit -m "Add battery sensor to Example"
git push -u origin HEAD
```

`-u` 使您叉上的分支成为此分支的默认值 。 没有它,你的分支会一直跟随`upstream/dev`,一个后来的平原`git push`或`git pull`去错地方了.

一个良好的承诺信息:

- 说变化是做什么的,不是"更新"或"Fix"
- 使用强制值:“添加电池传感器”,而不是“添加电池传感器”。
- 以大写字母开头,而不以周期结尾
- 没有像`[example]`或`sensor:`这样的前缀

Git 钩子在您承诺时运行, 可以在您的整合文件夹外更改文件 。 这些变化也属于您的 pull request 。

## 打开 pull request {#open-the-pull-request}

在 GitHub 上, 从您的分支打开 pull request 对 `dev` 的分支 [Home Assistant/核心人员](https://github.com/home-assistant/core) 。 然后填写模板。 请勿删除任何内容, 包括您不检查的框 。

- **Breaking change**:如果您的更改打破了对现有用户的某样东西,请解释哪些中断,如何修复,以及原因. 此文本会进入发行笔记,所以为用户而不是开发者写. 无中断时删除该部分。 [当它向后不兼容时](/releases/guides/backward-incompatible-changes#when-it-is-backward-incompatible) 帮助您决定, 也是在 贬值 结束时删除 。
- ** 建议的改动**:解释为什么*,而不仅仅是什么。 审查者需要判断解决方案的理由.
- ** 更改类型**:检查一个方框。 如果一个以上适合, 您的 pull request 做太多: 拆分 。 机器人使用此框标记您的 pull request 。
- ** 补充信息**:将您处理的问题与`fixes #12345` 和用于文档或前端的pull request 链接起来。
- ** 核对清单:诚实地通过。

在您的第一个 pull request 上, 一个机器人要求您在 Contributor License Agreement 上签名 。 在此之前无法合并您的 pull request 。 如果您的 GitHub 账户是新建的, CI 也会等待维护者批准运行 。

## 页:1 {#once-the-pull-request-is-open}

在 pull request 打开后, 不要修改、 壁球或重置您已按下 。 评论家们需要关注历史,看看他们上次看之后有什么变化. 添加新的承诺, 并用合并方式带来 `dev` 的更改 。 见[不断更新你的分支](/core/development/catching-up).

CI 必须在您 pull request 被审查并合并之前通过 。 有些测试是片面的:当您确定失败与您的更改无关时, 请等待维护者, 而不是再次推动运行 CI 。

[打开 pull request 后](/core/development/review-process)解释下个核心会发生什么.

## 新整合 {#new-integrations}

在新建集成前,请读 [我发誓它属于核心](/core/integrations/create#does-it-belong-in-core). 项目建议您先在 [市场](/marketplace) 中公布 。 一旦它成熟并具有用户至少在 [发展中国家**](https://discord.com/channels/330944238910963714/554842238073700352) 频道中询问 [Discord](https://www.home-assistant.io/join-chat/) 是否应该飞船建造。

当它出现时, [保留第一个 pull request 小](/core/integrations/create#keep-the-first-pull-request-small) : 青铜层,一个平台,没有额外的。

在pull request的描述中:

- 解释产品或服务是什么.
- 链接到您使用的库的源寄存器 。
- 链接 pull request 上的文档和品牌图像 。

[教程](/core/integrations/tutorial) 走过一个全新的整合, 到这个pull request。

## 依赖性更新 {#dependency-updates}

在 pull request 中更新依赖关系 。 只包含代码更改新版本需要. 使用新版本的新功能在后续中出现.

在描述中,链接到上游的变化:发布注释或更改日志,或旧版本和新版本之间的diff. 审查者在合并前阅读上游变化,既看更新是否安全进行补丁释放,又发现任何可疑情况. 运行 `python3 -m script.gen_requirements_all` 以更新要求文件, 并包含它们 。

## """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" {#using-ai}

你可以使用AI工具帮助你写代码,只要你把人留在循环中. 核心遵循[AI 政策](/start/ai-policy):你检讨和理解你提交的所有文件,你可以解释每个变化,并且你自己回答审查者的问题. 自主代理不得出资. pull request 模板要求您确认您理解您提交的代码 。

Core在存储器中拥有 `AGENTS.md` AI 工具的文件和技能. 见[存储器中的AI工具](/core/development/environment#ai-tools-in-the-repository).
