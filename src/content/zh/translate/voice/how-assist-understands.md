---
title: Assist 如何理解语言
description: 意向,句子,槽,列表,以及回复. Assist背后的想法, 一个口头命令如何变成一个行动。
order: 1
sidebarLabel: Assist 如何理解
---

# Assist 如何理解语言 {#how-assist-understands-language}

在你写第一句之前,它有助于知道它的后果。 本页遵循的命令从有人说到Assist回答。

## 从声音到行动 {#from-voice-to-action}

当你与 Assist 交谈时, 您的命令会经过几个步骤 。 他们一起被称为[输油管](/glossary/assist-pipeline):

1. 将音频变成句子,如"打开厨房灯"。
2. ** 计算** 说明该句的含义。 内置的 [对话代理](/glossary/conversation-agent) 通过将句子匹配到 [意图存储器](https://github.com/OHF-Voice/intents) 中的模板来做到这一点 。 结果是一种意图。
3. ** 有意处理** 执行意图,例如打开厨房的灯。
4. ** 答复** 由语言模板提供,如“打开灯”。
5. ** 发言** 说明这一答复。

第二步和第四步是你们的工作所在 句子和回应在[意图存储器](https://github.com/OHF-Voice/intents)中. 它们作为`home-assistant-intents`软件包发布,其中Home Assistant包括.

集成可以为其中一些步骤插入自己的引擎:一个[对话代理](/core/entities/conversation),[对文本的语音](/core/entities/stt),或[猿人咆哮的声响](/core/entities/tts). 你的句子被内置的对话代理使用.

您也可以输入到 Assist 。 然后,语音步骤被跳过, 但匹配效果相同。

## 意图 {#intents}

[意图](/glossary/intent)是句子的意思,以Home Assistant的形式可以采取行动. "翻开 只有厨房的灯

意向名称以 `Hass` 开头, 如 `HassTurnOn`, `HassGetState` 或 `HassStartTimer` 。 意旨列表对每种语言都是一样的. 它在 [`intents.yaml`](https://github.com/OHF-Voice/intents/blob/main/intents.yaml) 和 [内设意图](/translate/voice/intents) 中定义, 并描述其中每一个 。

## 槽数 {#slots}

一个槽乃是意图ẩn的关键要素. 在"乃是厨房ẩn的关键要素"中,有两个:

- `area`是"厨房"。
- `domain`是"光",因为"光"这个词告诉Assist你指的是哪种设备.

有些槽上填充的是用户在 Home Assistant : `name` (实体名称), `area` 和 `floor` 中设置的东西. Home Assistant 在匹配句子时提供这些 。 其他槽来自寄存器中的列表,如颜色,或者数字,如50%的亮度.

## 槽组合 {#slot-combinations}

众生以异法求同. "打开高架灯"指一个实体. "打开厨房的灯"命名了一个区域和一种装置. 每一组句子填充的插槽是一个插槽组合,并有自己的名称:

- `name_only`:"打开上面的灯"
- "打开厨房的灯"
- `domain_only`:"打开这里的灯",这里的区域是您正在说话的语音卫星之一。

判决和测试按意向和组合进行。 每个槽组合有一个重要关卡,说明语言需要多少,从`required`到`optional`. [progress overview](https://ohf-voice.github.io/intents/)使用这些级别来评分每种语言.

## 句子模板 {#sentence-templates}

你不能写每一句 您会同时写出许多句子的模板:

```text
(turn | switch) on [the] {name}
```

这符合"打开上面的灯","打开上面的灯",以及所有这些词的其他组合. {H0将能够列出其他选项,`[ ]`标记可选的单词,`{name}`是一个槽. 匹配模板的引擎是 [杂乱](https://github.com/OHF-Voice/hassil) 。 [模板句子语法](/translate/voice/template-syntax)有完整的参考文献。

## 清单和扩展规则 {#lists-and-expansion-rules}

两个工具使模板简短且可读:

- ** Lists ** 持有一个插槽的可能值,就像光线可以拥有的颜色一样. 列表也可以是数字范围,也可以是匹配任何文本的通配符,如歌曲的名称.
- ** 扩展规则**是可重复使用的模板。 一条名为 `turn` 的规则, 它持有 `(turn | switch)` 允许您在每个文件中写 `<turn> on [the] {name}` 。

这两种语言巷口都是按语言定义的,因为每个语言的单词不同.

## 答复 {#responses}

在 Home Assistant 处理意图后, Assist 回答 。 答案来自您语言的响应模板,以[锦佳2](https://jinja.palletsprojects.com/en/latest/templates/)写成. 一个响应可以使用槽的值,一些意图让它与更多工作,比如你所询问的实体状态:

```yaml
one: "{{ slots.name | capitalize }} is {{ state.state_with_unit }}"
```

每一组句子都指出适合它的反应. 这样,"打开车库门"就可以回答"打开",而"打开灯"可以回答"打开灯".

## 所面对的问题 {#tests}

每个句子模板都需要至少一个测试句. 一个测试描述了一个小的家(有些区域,有些实体),几个句子,它们应该填充的插槽,以及应该给出的确切响应Assist. 每个pull request都会进行测试,所以当别人改变什么时,你的句子会继续工作. 解释如何写

## 下一步 {#next-step}

准备好了吗? 让你度过你的第一个变化。
