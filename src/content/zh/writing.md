---
title: 写入文件
description: 帮助数百万人从Home Assistant中获取更多,方法是改进家庭援助者.io的文件。
---

# 写入文件 {#writing-docs}

在 [Home Assistant.io](https://www.home-assistant.io/) 上的文档常常是人们在设置设备,建立自动化,或者被卡住时阅读的第一件事. 那里的每一页都是由社区撰写和改进的. 一个更清晰的句子,一个缺失的台阶,或者一个固定的截图,帮助每一个在你之后读那页的人.

您不需要成为开发者 。 如果你能清楚地解释一些事情,你可以帮助。

要改进这个贡献网站吗? 见[改进这个贡献网站](/writing/this-site).

## 你为谁写的 {#who-you-write-for}

大多数读取文档的人通过它的界面使用Home Assistant,而不是通过YAML文件. 先为他们写:指明通路UI,为需要的人保留技术细节. [样式指南承担起](/writing/reference/style)解释如何。

## 两个帮助的方法 {#two-ways-to-help}

- ** 小修正** 需要几分钟,完全发生在浏览器中。 一个字型,一个过时的截图,这个步骤不再与UI匹配. 每页都有**编辑**链接.
- **未被删除的修改**,与新页面或重组的段落一样,用本地网站副本更容易,因此在分享之前可以预览自己的作品.

## 使用 AI 工具写入 {#writing-with-ai-tools}

[文献储存库](https://github.com/home-assistant/home-assistant.io)为 AI 工具携带技能, 在 `.claude/skills/` 中: 一个用于写作风格, 一个用于 Markdown 和 Liquid , 一个用于 YAML 示例, 以及 `document-integration-docs` 用于集成页面 。 它的指令告诉代理在编辑前要加载它们,除非您询问,否则不要发明新的自动化,脚本或仪表板实例. 页面上的每份索赔都属于你 来核对密码 [用AI 工具做贡献](/start/ai-tools#write-documentation-on-home-assistantio)有工作流程。

## 从这里开始 {#start-here}

- [您的第一个文件修复](/writing/first-contribution) : 从浏览器直接修正一些小东西 。
- [文档如何运作](/writing/how-it-works): 页面住址, 使用哪个分支, 以及如何进行更改 。

## 指南 {#guides}

- 萃取 [结构 a 页](/writing/guides/structure): 概念,任务,参考,以及何时使用哪一个.
- [本地预览网站](/writing/guides/local-preview) : 在自己的机器上运行文档 。
- [综合文件](/writing/guides/integration):用于开发者添加新集成.
- [移动、重命名或删除页面](/writing/guides/move-or-remove):没有断开链接。

## 参考 {#reference}

- [样式指南](/writing/reference/style):语言,语气,和格式化.
- [图像和录像](/writing/reference/images):截图、字幕和嵌入式视频。
- [目录](/writing/reference/liquid):我的链接、词汇提示和文本框。
- [YAML 样式](/writing/reference/yaml): YAML 例应该如何看起来.
- [自动检查](/writing/reference/checks): 您的pull request 的支票在找什么 。
- [一体化问题。](/writing/reference/front-matter):整合页上方的每一个键.
- [整合页面结构](/writing/reference/integration-page):一个集成页面的章节,以及填充它们的块.
- [品牌](/brand):Home Assistant的个性和声音,每页都反映.

## 谁说话 {#who-to-talk-to}

- 读者通过**提供反馈**链接在页面上留下反馈. 他们成为了[问题 GitHub](https://github.com/home-assistant/home-assistant.io/issues), 他们是一个伟大的地方 找到工作。
- 关于你的零钱的问题? 问你的pull request。 评论家们很乐意帮你把事情搞对
- 想谈谈文件吗? 在 [Home Assistant Discord](https://www.home-assistant.io/join-chat/) 上加入 [文件**](https://discord.com/channels/330944238910963714/1475552849835458691) 频道 。
