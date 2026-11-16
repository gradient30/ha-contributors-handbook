---
title: 占位符和参考文献
description: 您不应该翻译字符串的部分, 以及如何处理它们 。
order: 1
---

# 占位符和参考文献 {#placeholders-and-references}

有些字符串不是纯文本 。 它们包含在运行时 Home Assistant 填充的部分, 或者指向另一个字符串 。 这些部分必须保持原样。

## 圆括号:运行时填入的数值 {#curly-brackets-values-filled-in-at-runtime}

卷曲括号中的一部分,如`{name}`,被活值所取代. 在此字符串中 :

```text
{count} devices found
```

将实际数字替换为 `{count}` 。 保持占位符原样,移动到适合您语言的地方:

```text
{count} Geräte gefunden
```

广泛散发文件

- 英语字符串中的每个占位符也必须出现在您的翻译中 。
- 从不翻译括号间的名称. 继续 继续 继续
- 你可以移动占位符周围, 你的句子命令获胜。

### 多元性和选择 {#plurals-and-choices}

一些占位符在变体中选择,例如一个或许多项目:

```text
{count, plural,
  one {

# device} {#square-brackets-references-to-other-strings}
  other {

# devices} {#devices}
}
```

翻译内括号内的文字,而不是周围的关键词. Hun. 具有较复数形式的语言可以添加它们,如`few`或`many`. 语法是ICU消息格式. [格式.js 指南](https://formatjs.github.io/docs/core-concepts/icu-syntax/)解释这一切。

## 方括号:提及其他字符串 {#方括号提及其他字符串}

方括号之间的文字,在Lokalise中以绿色显示,是一种参考。 它指向另一个字符串,因此同一文本只翻译一次. 当翻译一个包含一个引用的字符串时,通常可以把它作为:在编辑器中使用**Insert source**.

您的语言可能有英语没有的重复 。 欢迎各位也把这些内容与参考资料联系起来。 Lokalise 如何在 [密钥引用](https://docs.lokalise.com/en/articles/1400528-key-referencing) 的文件中解释 。
