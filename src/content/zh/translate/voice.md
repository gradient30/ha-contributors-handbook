---
title: 声音
description: 教Assist你的语言。株式会社蓉子,
order: 30
---

# 声音 {#voice}

Assist,Home Assistant的语音助理,理解命令如"打开厨房的灯",而不发送任何东西给云. 它可以做到这一点,因为人们为自己的语言写下, 人们可能会说的许多方式。 这项工作发生在 [意图存储器](https://github.com/OHF-Voice/intents) 在 GitHub 上的 [意图存储器](https://github.com/OHF-Voice/intents) 中, 它与 Lokalise 中的界面文本不同 。

你不能逐句翻译 您描述语言短语中的人如何使用一个命令, 带有一个紧凑的模板语法, 您添加了测试来证明它有效。 如果你在本地说自己的语言,而且你很舒服地编辑YAML文件,你可以提供帮助.

## 这是给谁的 {#who-this-is-for}

- ** 母语** 希望Assist理解自己的语言,或更好理解自己的语言。
- ** 语言领导人** 为自己的语言审查工作。
- **掺 对了,他们想知道存在何种意图和判决如何转化为行动。

## 如何开始 {#how-to-start}

1. 读[Assist 如何理解语言](/translate/voice/how-assist-understands). 它解释了意图,插槽, 和插槽组合, 你会看到任何地方的词。
2. 在 [progress overview](https://ohf-voice.github.io/intents/) 上查看您的语言 。 它显示,根据意图, 你的语言已经覆盖。
3. 选择一个缺失或弱的意向, 并遵循 [提供判刑和答复](/translate/voice/contributing) 。

开始小。 一个 pull request 一个语言的意向 被审查的速度比一个大。

## 指南 {#guides}

- [Assist 如何理解语言](/translate/voice/how-assist-understands):意图,句子,插槽,列表,和响应,以及它们是如何结合的.
- [提供判刑和答复](/translate/voice/contributing):意图库中的工作流程,从第一次编辑到合并的pull request.
- [样式指南](/translate/voice/style-guide):如何写出效果好的句子和回应.
- [支持的语言](/translate/voice/languages):语言Assist知道,如何添加一个新的语言。
- ử丝:他们做什么,如何成为一体。
- [贡献你的声音](/translate/voice/contributing-your-voice) : 帮助训练语音识别和语音。

## 参考 {#reference}

- 指导方针 [模板句子语法](/translate/voice/template-syntax): 句子文件的完整语法,列表,扩展规则,以及回应.
- [测试语法](/translate/voice/test-syntax):如何为您的句子写测试.
- [内设意图](/translate/voice/intents):每一个意图,都有它的插槽和插槽组合.

## 谁说话 {#who-to-talk-to}

- 关于你语言的问题? 询问语言领袖, 在[`languages.yaml`](https://github.com/OHF-Voice/intents/blob/main/languages.yaml) 中列出 。 他们审查每一个变化。
- 关于寄存器、工具或不符合你语言的意图的问题? 使用[意图讨论](https://github.com/OHF-Voice/intents/discussions),或打开[问题](https://github.com/OHF-Voice/intents/issues)。
- 想聊聊吗? 在 Home Assistant [Discord 服务器](https://www.home-assistant.io/join-chat) 上加入 [语文领导人**](https://discord.com/channels/330944238910963714/1257022942961991781) 频道 。 看不见吗? 在 **Channels & 角色** 下选择合适的角色.
- 写一个处理或放火的代码? 这在[核心内部](/core/internals)中覆盖。
