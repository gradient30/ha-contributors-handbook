---
title: 模板句子语法
description: 句子文件的完整引用,模板语法,列表,扩展规则,回复,以及一种语言的常见文件.
order: 7
sidebarLabel: 模板语法
---

# 模板句子语法 {#template-sentence-syntax}

此页面莹指您为[意图存储器](https://github.com/OHF-Voice/intents) 语言撰写的每个文件, 除了测试, 测试有[它们的页面](/translate/voice/test-syntax) 。 这一切都是新的? 先读[Assist 如何理解语言](/translate/voice/how-assist-understands).

模板由 [杂乱](https://github.com/OHF-Voice/hassil) 匹配 。 该寄存器使用hassil 3.

## 语言文件 {#files-of-a-language}

| 路径 | 目录 |
| --- | --- |
| `sentences/<language>/<intent>/<slot_combination>.yaml` | [句子文件](/translate/voice/template-syntax#sentence-files)一个意图和插槽组合 |
| `sentences/<language>/_common.yaml` | 驯服 [常见文件](/translate/voice/template-syntax#the-common-file): 错误响应, 跳过单词和设置 |
| `lists/<language>/<group>.yaml` | 此语言的 [列表](/translate/voice/template-syntax#lists) |
| `lists/<group>.yaml` | [共享名单](/translate/voice/template-syntax#shared-lists):每种语言的数字范围和通配符 |
| `rules/<language>/<group>.yaml` | 此语言的 [扩展规则](/translate/voice/template-syntax#expansion-rules) |
| `responses/<language>/<intent>.yaml` | 一个意图的 [答复](/translate/voice/template-syntax#responses) |
| `tests/<language>/<intent>/<slot_combination>.yaml` | [所面对的问题](/translate/voice/test-syntax)一个意图和插槽组合 |

您自己选择列表的组名并规范文件 。重新审查事物的方式对语言有意义,如颜色和亮度水平的`lights.yaml`,或动词的`verbs.yaml`。

除了[`lists/`](https://github.com/OHF-Voice/intents/tree/main/lists)中的列表之外,每个模板都可以使用列表`name`,`area`和`floor`. Home Assistant 当与句子匹配时, 填入用户已曝光的实体、 区域和地板的名称 。

## 槽组合 {#slot-combinations}

意图及其槽组合以 [`intents.yaml`](https://github.com/OHF-Voice/intents/blob/main/intents.yaml) 声明, 并同时适用于所有语言 。 您不更改此文件, 但需要读取 。 插槽组合是这样的:

```yaml
HassTurnOn:
  slot_combinations:
    name_only:
      description: "Turns on a device or opens a cover by name"
      slots:
        - "name"
      name_domains:
        required:
          - "light"
          - "cover"
        optional:
          - "valve"
      name_domain_groups:
        default:
          - "light"
          - "switch"
      example:
        - "turn on the overhead light"
        - "open sliding door"
```

| 密钥 | 含义 |
| --- | --- |
| `slots` | 这种组合的每一个句子都必须填满,不能多,也不能少 |
| `importance` | 语言需要这个组合多少 : `required`, `usable`, `complete` 或 `optional` |
| `name_domains` | 对于与 `name` 槽的组合: 实体域`{name}` 可能匹配, 按重要性分组 |
| `name_domain_groups` | 哗! 命名了句子文件可以引用的一组域, 而不是重复列表 |
| `inferred_domains` | 对于与 `domain` 插槽的组合: 句子词可以隐含的域, 按重要性分类 |
| `context_area` | 当这个区域来自语音卫星,而不是句子, 就像"打开这里的灯" |
| `wildcard_slots` | 必须用 [通配符列表](/translate/voice/template-syntax#wildcards) 填充的槽, 如定时器的名称 |
| `example` | 一个或多个英文实例 |

重要性水平意味着:

- `required`: 最低限度。 缺少句子时验证失败 。
- `usable`: 人们期望的。 当判决缺失时验证警告.
- `complete`:需要完全覆盖语言。
- `optional`:额外,不计入全覆盖.

当组合使用 `name` 或 `domain` 时, 每个域在 `name_domains` 或 `inferred_domains` 下设定级别, 而不是使用 `importance` 。

## 句子文件 {#sentence-files}

句子文件包含一个意图和一个插槽组合的模板, 在 `data` 下的一个或多个组中 :

```yaml
# sentences/en/HassTurnOn/name_only.yaml, shortened {#sentencesenhassturnonnameonlyyaml-shortened}
language: "en"
data:
  

# lights, switches, and other things you turn on {#speech-to-phrase}
  - sentences:
      - "<turn> on [<the>] {name}"
      - "activate [<the>] {name}"
    example: "turn on the overhead light"
    name_domains: "default"
    response: "default"

  

# covers {#template-syntax}
  - sentences:
      - "<open> [<the>] {name}"
    example: "open the sliding door"
    name_domains:
      - "cover"
    response: "cover"
```

每个组支持这些密钥 :

| 密钥 | 要求数 | 含义 |
| --- | --- | --- |
| `sentences` | 对 | 那个[句子模板](/translate/voice/template-syntax#template-syntax) |
| `response` | 对 | [回应](/translate/voice/template-syntax#responses) 当其中一句匹配时给定的密钥 |
| `name_domains` | 当组合有 {H0瓷} | 实体域内这些句子的目标, 作为列表, 或 `name_domain_groups` 组的名称 |
| `inferred_domain` | 当组合有 {H0瓷} | 这些句子的词意指的一个域,比如`light`的"灯光" |
| `example` | No | 此组匹配的句子, 用您的语言 |
| `speech_to_phrase` | No | `true` 使用该组进行语句对词, 见下文 |

适用一些规则:

- 每个模板必须填写 `intents.yaml` 宣布的组合的精确空格 。 模板直接用 `{slot}` 填充一个槽, 或者通过包含它的扩展规则 。 `domain`槽是例外:你从来不用模板写,它来自`inferred_domain`.
- 在 `name_domains` 或 `inferred_domains` 中标有 `required` 的每个域都必须由某些组覆盖 。 不一定是同一组: 以任何适合你语言的方式将句子分开 。 这就是为什么英语用一个组来做你"打开"的东西,另一个用盖子来做你的"打开".
- 用您的语言驴写`example` 。 一个和英国驴一样的例子给出了警告.

您不写入句子可能针对哪一个实体, 或固定的槽值 。 这部分由`intents.yaml`生成,它使每种语言都保持不变.

### 语音对词组 {#alternatives}

Speech-to-Phrase是一个语音对文本的引擎,它只识别一组固定的短语,这使得它在小硬件上的速度很快. 使用 `speech_to_phrase: true` 组来构建这组词组 。

当一个槽组合有带有和没有标记的组时,被标记的组只是用于Speak-to-Phase的较小的集,而Home Assistant本身忽略了它们. 其中的每一个句子也必须与未加标记的团体相匹配. 当每个组被标记时,它们都用于两者.

## 模板语法 {#optional-parts}

一个句子模板同时描述了许多句子.

### 替代品 {#lists}

在括号之间插入选项, 并用 `|` 分隔 :

```text
set color to (red | green | blue)
```

替代品也存在于一个词内。 `turn(s | ed | ing)`匹配"转","转","转".

### 可选部分 {#expansion-rules}

将可选的词、短语或部分词放在方括号内:

```text
turn on [the] light[s]
```

35),这与"开灯","开灯","开灯","开灯"相匹配. `[this | that]`可以选择其他选择。

### 列表 {#permutations}

`{list_name}` 匹配 [列表](/translate/voice/template-syntax#lists) 的任何值, 并将该值放在同名的槽中 。 当槽名与列表不同时, 请写入 `{list_name:slot_name}` :

```text
set [the] {name} brightness to {brightness_level:brightness}
```

清单可能不在备选部分或任择部分之内。 `(text | {list_name})`和`[{list_name}]`是不允许的,因为模板必须总是填补相同的空档.

### 扩展规则 {#escaping}

`<rule_name>` 被 [扩展规则](/translate/voice/template-syntax#expansion-rules) 的正文所取代 :

```text
<turn> on [<the>] {name}
```

### 周期 {#sizes}

括号中的项目, 由 `;` 分隔, 任意顺序匹配 :

```text
<turn> on ({name}; <area>)
```

这既符合"在厨房的灯上转动",也符合"在厨房的灯上转动",这是一些语言需要的. 在项目之间添加空格,所以它们从不合并为新词. 保持2至4项:4项已经下达24项命令,5项给出120项.

### 逃脱 {#lists-1}

为了匹配其中的某个角色`( ) [ ] { } < >`字面意思,在前面放一个反弹,像`\(`.

### 大小 {#listsenlightsyaml}

每个可选部分将一个模板匹配的句数翻倍,替代部分则将其倍增. 在小型设备上,数量庞大使得匹配速度缓慢. 使用`count_sentences`检查,参见[提供判刑和答复](/translate/voice/contributing#try-things-out).

## 列表 {#values-in-your-language-values-for-home-assistant}

列表包含一个槽的可能值. 有三种类型:固定值,数字范围,以及通配符. 语言列表在 `lists/<language>/` 中存在, 并且每个文件名称其语言 :

```yaml
# lists/en/lights.yaml {#ranges}
language: "en"
lists:
  color:
    values:
      - "white"
      - "red"
      - "orange"
```

### 您语言中的值, Home Assistant 的值 {#wildcards}

意向处理器期望一些英语的值,如颜色. 使用 `in` 和 `out` 在您的语言中匹配一个单词并将英文值传递到 :

```yaml
language: "nl"
lists:
  color:
    values:
      - in: "rood"
        out: "red"
      - in: "oranje"
        out: "orange"
```

`in`可以是一个带有替代品的模板,而`out`可以是数字. 这使得单词变为固定数字:

```yaml
language: "en"
lists:
  brightness_level:
    values:
      - in: "(max | maximum | highest)"
        out: 100
      - in: "(minimum | lowest)"
        out: 1
```

价值可能不包含列表或扩展规则,也可能不是完全可选的.

### 范围 {#shared-lists}

范围匹配数字,写成数字或单词 。 "50%"和"50%"都匹配:

```yaml
lists:
  brightness:
    range:
      type: "percentage"
      from: 0
      to: 100
      step: 1
```

| 密钥 | 要求数 | 含义 |
| --- | --- | --- |
| `from` | 对 | 人数最少 |
| `to` | 对 | 最高数字 |
| `step` | No | 数字之间的步骤, `1` 默认 |
| `type` | No | `number`, `percentage`, or `temperature` |
| `fractions` | No | 同时匹配 `halves` 或 `tenths` |
| `multiplier` | No | 将匹配的数字乘以此值 |

### 通关卡 {#listslightsyaml}

匹配任意文本的通配符 :

```yaml
lists:
  album:
    wildcard: true
  artist:
    wildcard: true
```

使用模板 `play {album} by {artist}`,句子"用节拍打白专辑"填充 `album`的"白专辑"和`artist`的"节拍". 怀德牌贪婪,所以要保证周围的字句足够具体,不要抓住其他意图的句子.

### 共享名单 {#expansion-rules-1}

范围与通配符不需要翻译 。 在 `lists/<group>.yaml` 中, 在 [`lists/`](https://github.com/OHF-Voice/intents/tree/main/lists) 的根部, 每个语言都可以使用 。 共享文件没有 `language` 密钥 :

```yaml
# lists/lights.yaml {#rulesenverbsyaml}
lists:
  brightness:
    range:
      type: "percentage"
      from: 0
      to: 100
  color_temperature:
    range:
      from: 1000
      to: 10000
      step: 100
```

有值的列表无法共享,因为它们的值是语言中的单词.

## 扩展规则 {#rulesencommonyaml}

扩展规则是您经常使用的模板的一部分. 语言规则在 `rules/<language>/` 中:

```yaml
# rules/en/verbs.yaml {#responses}
language: "en"
expansion_rules:
  turn: "(turn | switch)"
  open: "(open | raise | lift) [up]"
```

```yaml
# rules/en/common.yaml {#responsesenhasslightsetyaml}
language: "en"
expansion_rules:
  the: "(the | my | our)"
  here: "([in] here | [in] (this | the | my | our) (room | area | space))"
```

规则必须包含一些非可选文本。

规则使模板更短,但也可能使其难以阅读. 有两项建议对此加以控制:

- ** 规则不应载有清单。 ** 用 `{name}` 隐藏在 `<name>` 规则中, 您无法看到模板填充的哪个位置 。 这也导致了双倍的单词,比如`[the] <name>`变成`[the] [the] {name}`.
- ** 规则不应使用其他规则。 ** 读者随后必须遵循一个链条来查看模板匹配的是什么,巢规则中的替代品可以快速地乘以句数.

pull request 当您的语言有规则或列表没有使用时失败 。 删除它们, 或者运行 `python3 -m script.intentfest prune --language <language> --write` 来为你做它 。

## 答复 {#sentencesenhasslightsetnamebrightnessyaml-shortened}

每组句子都命名为`response`. 意图的响应模板存在于 `responses/<language>/<intent>.yaml` :

```yaml
# responses/en/HassLightSet.yaml {#the-common-file}
language: "en"
responses:
  intents:
    HassLightSet:
      brightness: "Brightness set"
```

```yaml
# sentences/en/HassLightSet/name_brightness.yaml, shortened {#error-responses}
language: "en"
data:
  - sentences:
      - "[<the>] {name} brightness [to] {brightness} percent"
    example: "set the bedroom lamp brightness to 50%"
    name_domains:
      - "light"
    response: "brightness"
```

答复为[锦佳2](https://jinja.palletsprojects.com/en/latest/templates/)模板。 它们与句子模板的格式不同: 这里 `{{ }}` 打印一个值 。

每个响应都可以使用`slots`,每个匹配槽的值,如`{{ slots.name }}`. 一些意图给出了与 `state` (第一个匹配的实体) 或 `query` 合作的响应 。 (各实体关于国家的问题相符)。 [内设意图](/translate/voice/intents) 列出每个意图的响应变量, `response_variables` 在`intents.yaml` 中描述它们 。

当没有其他响应被命名时,则使用`default`响应. 查看 [英文答复](https://github.com/OHF-Voice/intents/tree/main/responses/en) 作为示例, 以及 [样式指南承担起](/translate/voice/style-guide#responses) 如何写它们 。

## 常见文件 {#skip-words}

`sentences/<language>/_common.yaml` 持有没有绑定在一个意图上的东西: 错误响应、 跳过单词和设置 。

### 错误为支持 {#settings}

Assist 当它不能处理一个命令时, 给出一个错误响应, 例如因为没有一个实体有你说的名称 :

```yaml
language: "en"
responses:
  errors:
    no_intent: "Sorry, I couldn't understand that"
    no_area: "Sorry, I am not aware of any area called {{ area }}"
    no_entity: "Sorry, I am not aware of any device called {{ entity }}"
```

全套密钥在 [英语常见文件](https://github.com/OHF-Voice/intents/blob/main/sentences/en/_common.yaml) 中 。 译一切法.

### 跳过单词 {#跳过单词}

匹配时忽略了跳过单词 。 这些是人们添加到命令中的文字,而不改变它的含义:

```yaml
skip_words:
  - "please"
  - "can you"
```

### 设置 {#设置}

何者为最上方,

```yaml
language: "zh-CN"
settings:
  ignore_whitespace: true
```

- `ignore_whitespace`:在匹配时忽略空格,用于汉语和日语等语言.
- `filter_with_regex`:不再有任何效果. 它仍然被接受, 所以旧文件继续工作。
