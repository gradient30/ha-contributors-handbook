---
title: 请求新语言
description: 您的语言还没有可用吗? 这是如何得到它添加。
order: 2
---

# 请求新语言 {#request-a-new-language}

如果您的语言不在列表中,您可以请求. 一旦加入,它就会出现在Lokalise中,任何人都可以开始翻译.

## 请求 {#make-the-request}

在前端寄存器的[本地化类别](https://github.com/home-assistant/frontend/discussions/categories/localization) 中开始讨论 。 包含您的语言的英文名称和本地名称:

```text
English name: German
Native name: Deutsch
```

## 齐心协力,实现《公约》的目标。 {#regional-variants}

区域变体,如加拿大法语或巴西葡萄牙语,也是可能的. 它们只有在文本与基础语言真正不同时才有意义. 一个变体只有在它有不同于基语言的翻译时才被列入.

当您翻译一个区域变体时, 请复制您所在区域相同字符串的基数翻译, 而不是留空 。 这样,就清楚哪些关系已经过审查。

## 接下来会发生什么? {#what-happens-next}

一个维护者将语言添加到Home Assistant和Lokalise. 语言以 [BCP 47 《巴塞尔公约》缔约方会议](https://www.rfc-editor.org/info/bcp47) 标记表示, 如 `fr`, `fr-CA` 或 `zh-Hans` 。 标记只包含一个区域需要自己的翻译时,而基础语言已经翻译. 完成后,你可以加入项目并开始翻译.

对于维护者,添加一种语言需要两个步骤:

1. 在前端寄存器中添加语言标记及其本土名称,如"Français"或"Français (CA)",以 [`src/translations/translationMetadata.json`](https://github.com/home-assistant/frontend/blob/dev/src/translations/translationMetadata.json).
2. 在Lokalise中添加语言. 有时Lokalise中的标记需要更改以匹配,在语言设置下,作为自定义的ISO代码.
