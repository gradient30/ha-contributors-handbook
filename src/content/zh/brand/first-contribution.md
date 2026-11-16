---
title: 你第一次的品牌贡献
description: 选择一页或一段界面文本，根据Home Assistant的个性进行阅读，并加以改进。
order: 1
sidebarLabel: 你的第一次贡献
---


# 你第一次的品牌贡献 {#your-first-brand-contribution}
品牌并不是你单独就能贡献的东西。它体现在其他一切中：一页文档、一段对话、一条错误信息。所以最好的首次贡献是小而具体的：选取一段文字，带着品牌个性去阅读，并将其改进。

不需要设计技能或编码技能，只需要一个GitHub账户。对于文档，你可以在浏览器中自己修改。对于界面文本，你可以指出哪里有问题，让开发者去修改，或者如果你熟悉代码仓库，也可以自己修改。

## 1. 阅读个性 {#1-read-the-personality}
阅读[个性](/brand/personality)一次。注意每个特质不是的列表。这能帮助你发现某个特质被过度表现的情况：坦率变得直率、支持变得居高临下、热情变得阿谀奉承。

## 2. 选择一些内容来阅读 {#2-pick-something-to-read}
从你熟悉的内容开始，这样你才能判断是否正确：

- **一页文档**，在 [home-assistant.io](https://www.home-assistant.io/) 上，关于你自己设置的内容。
- **一段界面文本**，比如你遇到的对话框或错误信息。

保持在一页或一个对话框。小的修改更容易审阅。

## 3. 根据特质来阅读 {#3-read-it-against-the-traits}
阅读时问自己几个问题：

- **热情欢迎**：它是否以读者的水平来交流，还是居高临下？它是否假设读者具备他们可能没有的知识？
- **坦率**：它是否直截了当地表达意思？是否隐藏了某些限制，或假装某事比实际更简单？
- **支持性**：当出现问题时，它是否说明下一步该做什么？
- **慷慨**：它是否提供读者所需，而不是掩盖起来？
- **独立**：它听起来像Home Assistant，还是像一个企业科技品牌？

也请检查基础部分：Home Assistant 的全称、使用“select”而不是“click”，以及术语是否按照[词汇表](/glossary)定义来使用。[语音和语气](/brand/voice-and-tone)展示了在不同类型文本中这些特质的表现。

## 4. 进行更改 {#4-make-the-change}
你进行更改的位置取决于你选择的内容：- **文档**：home-assistant.io 上的每个页面都有一个 **编辑** 链接。[你的第一个文档修复](/writing/first-contribution) 将带你直接在浏览器中操作。
- **界面文本，无需代码**：在前端仓库中[提交一个 issue](https://github.com/home-assistant/frontend/issues)，说明界面名称，引用当前文本，并提出你的版本。或者，如果你不确定正确的用词，可以先到 [Home Assistant Discord](https://www.home-assistant.io/join-chat-design) 的 [**#designers**](https://discord.com/channels/330944238910963714/1463606665311158284) 频道。提出新用词前，请阅读 [UI 文本](/design/ui-text)。

- **界面文本，作为 pull request**：界面英文文本位于 [`src/translations/en.json`](https://github.com/home-assistant/frontend/blob/dev/src/translations/en.json) 的 [前端代码库](https://github.com/home-assistant/frontend)，集成的文本位于其 `strings.json` 在 [核心代码库](https://github.com/home-assistant/core)。这些都是代码仓库：那里的 pull request 会运行自动检查，并且需要一个签署的 [Contributor License Agreement](/start/licensing)，首次会由机器人请求。

不要在翻译工具中更改英文文本。翻译人员是以英文原文为基础的，所以应先修正原文，翻译会跟随。

在你的问题或 pull request 中，解释哪里感觉不对以及为什么你的版本更好。指出特性会帮助审阅：“旧文本隐藏了这只能在本地使用，所以我把它改得更明确”易于评审。

GitHub 新手？请参阅 [使用 GitHub，无需成为开发者](/start/github)。

## 接下来做什么 {#what-is-next}
- 阅读 [语音和语调](/brand/voice-and-tone) 了解该人格在其他地方的表现。
- 想改善用词？[写作文档](/writing) 区域和 [UI 文本](/design/ui-text) 还有很多内容可改进。
- 会说其他语言？在 [翻译](/translate) 中用相同的语音呈现。
