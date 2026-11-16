---
title: 前端的翻译
description: 前端文本存在的地方,如何在代码中使用,以及来自Core和集成的文本如何进入界面.
order: 4
---

# 前端的翻译 {#translations-in-the-frontend}

前端使用数十种语言,因此没有看到文字的人会直接写入代码. 英文来源生活在一个文件中,社区将其翻译成所有其他语言.

## 文本存在的地方 {#where-text-lives}

- ** 前线文本** 在[`src/translations/en.json`](https://github.com/home-assistant/frontend/blob/dev/src/translations/en.json)中。 它是寄存器中唯一的翻译文件. 当它改变 `dev` 上传到 [Lokalise](/glossary/lokalise) 时, 翻译会在那里工作 。 译经如夜筑而归.
- **来自Core和集成**的文字,与实体名称,状态,以及一个配置流的阶梯一样,来自每个集成的`strings.json`. 前端在运行时间从Core装入.

翻译们从不看你的代码, 只有字符串和钥匙。 [让你的弦可变](/translate/guides/developers)解释如何写出他们可以合作的字符串.

## 使用字符串 {#use-a-string}

将英文文本添加到 [`src/translations/en.json`](https://github.com/home-assistant/frontend/blob/dev/src/translations/en.json), 在一个键下, 键上写着它使用的地方 。 这个是修复卡上的修复问题数量, 在 `ui` > `card` > `repairs` 下:

```json
"count_issues": "{count} {count, plural, one {issue} other {issues}}"
```

然后通过 `localize` 使用, 并附上占位符的全部密钥和值 :

```ts
this._localize("ui.card.repairs.count_issues", { count: 3 });
```

键会对照 `en.json` 进行类型检查, 因此密钥中的打字失败类型检查 。

从国际化上下文获取`localize`,与`@consumeLocalize()`,或从`hass.localize`在一个已经拥有`hass`的组件中获取。 见[对象和上下文](/frontend/architecture/hass-and-contexts).

### 占位符和复数 {#placeholders-and-plurals}

字符串使用[ICU 信件格式](https://formatjs.github.io/docs/core-concepts/icu-syntax/) 。 占位符是卷曲的,像`{count}`一样。 以上示例中的{H1 文件为数字选择正确的单词 。 每种语言都有自己的复数规则,笔译员填写其语言需要的形式.

总是翻译整句, 并有占位符用于什么变化 。 永远不要从单独的翻译作品中构建句子:其他语言的词序不同.

### 重新 拜托 。 {#reuse-a-string}

当同一文本已经存在时,请指向它而不是再写一次. 引用使用其他密钥的路径, 在 `::` 部分之间 :

```json
{
  "armed_home": "[%key:state_badge::alarm_control_panel::armed%]"
}
```

忆每一个再利用的字符串都是少一个字符串来翻译,在每种语言中.

## 来自核心的文字 {#text-from-core}

集成后产生的文本按类别按需加载. 在使用密钥前装入所需的类别 :

```ts
const localize = await hass.loadBackendTranslation("title");
localize(`component.${domain}.title`);
```

后 定 的 后 定 的 后 定 的 后 定 的 后 定 的 后 定 的

以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以以 `hass.loadFragmentTranslation()` 装入一个, 例如当一个面板的对话框在另一个面板内打开时 。

## 运行翻译 {#run-with-translations}

开发期间,除非获取翻译,前端只能是英文. 添加`--fetch-translations` 到任何开发服务器, 如`pnpm dev --fetch-translations`。 见[建立环境](/frontend/development/environment#translations) 。

要检查右到左的布局, 请切换到右到左的语言, 如希伯来语或阿拉伯语, 或在 [画廊](/frontend/development/gallery-and-demo) 中使用右到左的切换 。
