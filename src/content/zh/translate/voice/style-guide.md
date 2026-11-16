---
title: 语音样式指南
description: 如何写出与人们说话方式相符的句子,以及短而清晰的反应.
order: 3
sidebarLabel: 样式指南
---

# 语音样式指南 {#voice-style-guide}

善句与众生所说无别. 良好的反应告诉人们发生了什么,没有更多的。 这页收集了每种语言的实用性。 您的语言领袖可能会有协议 除此之外, 您的语言。

## 判决 {#sentences}

### 写人说话的方式 {#write-how-people-talk}

不逐字翻译英语模板词 。 想想用你语言的人 如何大声地说出命令, 在家里,对角落的扬声器。 包含短表("厨房灯亮")以及全表("打开厨房的灯亮"),单词命令您的语言允许.

如果您的语言有自由的单词顺序, 请使用 [常规](/translate/voice/template-syntax#permutations), 如 `({name}; <area>)` , 而不是写入所有命令 。

### 使用您的语言作为示例 {#use-your-language-for-examples}

每句有`example`. 用汝语写. 它显示审查者和进展情况概览,说明小组打算如何匹配。

### 对重复的部分使用规则 {#use-rules-for-repeated-parts}

当同一个词不断回来时,像动词来打开某个东西时,把它们放进[扩展规则](/translate/voice/template-syntax#expansion-rules). 然后在一个地方改进它们。 保持规则简单:规则内部没有列表,规则内部没有规则. 否则就没人知道什么是模板匹配的

### 保留礼貌以跳过单词 {#leave-politeness-to-skip-words}

人们会在命令中加上"请"或"能". 不要在每一个模板中添加这些单词。 把它们放进你语言的[跳过单词](/translate/voice/template-syntax#skip-words), 配对者忽略了它们 到处都是。

### 继续检查数字 {#keep-the-numbers-in-check}

每个可选部分将一个模板匹配的句数增加一倍. 几个太多,而你的语言有上百万句,这使得Assist在小设备上慢了下来. 使用 `count_sentences` (参见 [试试看](/translate/voice/contributing#try-things-out)) 检查, 并选择几个清晰的模板, 而不是一个匹配一切的模板 。

### 别太吻合 {#do-not-match-too-much}

一个过于松散的模板 捕获属于另一个意图的句子。 这与 [通配符](/translate/voice/template-syntax#wildcards) 发生次数最多,可用来匹配任意文本 : 一个松散的“ 玩 `{search_query}` ” 可以吞下“ 将灯设为最大 ” 。 在通配符上加上具体的单词. 检查每个 pull request 抓住它, 但是在您写的时候更容易避免它 。

### 翻译值, 保留  在我 Home Assistant 需要时 {#translate-values-keep-what-home-assistant-needs}

颜色,状态,以及 Home Assistant 在英语中期望的 `in` 和 `out` 的 [列表](/translate/voice/template-syntax#values-in-your-language-values-for-home-assistant) 形式的 `in` : 您的单词进入, 英文值 出来了 。

### AI模型的草稿 {#drafts-from-an-ai-model}

该 也许该寄存器可以为AI模型写一个提示,以获得意图的句子初稿:

```shell
python3 -m script.intentfest llm_template nl HassListAddItem
```

将输出视为草稿. 你是讲母语的人:读每一句,放下没有人会说的话,加上缺少的内容。

### 与接口保持一致 {#stay-consistent-with-the-interface}

使用与语言中的Home Assistant接口相同的单词和相同的地址形式. 如果您的语言已就正式或非正式的地址或如何翻译某些词语达成一致,请遵循这一措辞。 见[语言准则](/translate/reference/languages).

## 答复 {#responses}

### 简洁 {#be-concise}

回答是公开的,所以每个尤其在词里都是重要的。

- 当一个命令命令目标为单个设备时,不要重复其名称。 "翻灯照灯""阳县志·卷三·水产·水产·水产·水产·水产·水产·水产·水产·水产·水产·水产·水产·水产·水产·水产·水产·水产·对现有水产·水产·水产·水产·水产·水产·水产·水产·水产·水产·水产·水产·水产·水产·水产·水 86. 水产·水产·水产·水产·水产·水产·水产·水产·水产·水产·水产·水产·水产·水产·水产·水产·水产·水产·水产·水产·水产·水产·水产·水产·水产·水产·水产·水产·水产·水产·水产·水产·水产·水产·水产·水·水产·水产·水产·水产·水产·水产·水产·水产·水产·水产·水产·水产
- 当一个指令瞄准一个区域时,不要重复这个区域或命名其实体.
- 当答复列出实体时,如果有四个或四个以下,请全部点名。 若有余者,举前慧三,并说余数,如"克钦,堂道,办公室及二处".

对于列表,使用与英文回复相同的模板,因此每个回复读法相同. 不要写自己的变体:

```jinja
{% if query.matched %}
  {% set match = query.matched | map(attribute="name") | sort | list %}
  {% if match | length > 4 %}
    Yes, {{ match[:3] | join(", ") }} and {{ (match | length - 3) }} more
  {%- else -%}
    Yes,
    {% for name in match -%}
      {% if not loop.first and not loop.last %}, {% elif loop.last and not loop.first %} and {% endif -%}
      {{ name }}
    {%- endfor -%}
  {% endif %}
{% else %}
  No
{% endif %}
```

翻译其中的文字,如"是","否","和","更",保持逻辑原样.

### 使用当前时态 {#use-the-present-tense}

"灯亮了" 不是"灯亮了"

### 使用活动声音 {#use-the-active-voice}

"开灯了",不是"开灯了".

盖与阀为例外. 他们需要一段时间才能打开或关闭,所以他们的回应描述了正在发生的事情:"打开","关闭".
