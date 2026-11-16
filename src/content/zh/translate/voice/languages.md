---
title: 支持的语言
description: 语言 Assist 与内置的对话代理, 其领导, 以及如何添加新语言 。
order: 4
---

# 支持的语言 {#supported-languages}

[意图存储器](https://github.com/OHF-Voice/intents)列出了66种语言。 每个人的差别有多大: 有一些涵盖了几乎所有的意图, 另一些则刚刚开始。 [progress overview](https://ohf-voice.github.io/intents/)显示每种语言的分数,每个意图。

## 名单来自何处 {#where-the-list-comes-from}

[`languages.yaml`](https://github.com/OHF-Voice/intents/blob/main/languages.yaml)在意图寄存器中是来源. 对于每种语言,它都有:

- `nativeName`:语言的名称,在那个语言中.
- `isRTL` : `true` 右到左写语言 。
- `leaders`: GitHub [赃物 语言领袖](/translate/voice/language-leaders) 的用户名 。
- `support`:每个区域,哪个语音对文本和文本对语音引擎为语言工作,比如Whisper,Speak对词,Piper,或者Home Assistant Link.

下表为该档案的快照。 当它们有分歧时,`languages.yaml`是正确的。

## 语文 {#languages}

| 的 | 语言 | 语文领导人 |
| --- | --- | --- |
| `af` | 南非荷兰人 | 还没有 |
| `ar` | العربية | [艾哈迈德-法拉格36](https://github.com/Ahmed-farag36), [纳塔吉](https://github.com/Natfaji) |
| `bg` | Български | [圣塔纳芷夫](https://github.com/hristo-atanasov) |
| `bn` | বাংলা | [波尔塔拉什卡语Name](https://github.com/poltalashka), [哈克医生](https://github.com/DrHaque) |
| `ca` | 加泰罗尼亚 | [双层](https://github.com/duhow) |
| `cs` | 克什蒂纳 | [海尔西沃](https://github.com/halecivo), [变形元](https://github.com/schizza) |
| `cy` | 锡姆拉格 | 还没有 |
| `da` | 丹斯克语 | [FadamsenRevolution( 法丹森语)](https://github.com/fadamsen), [红蟹](https://github.com/MTrab) |
| `de` | 德国 | [安德拉斯布莱特](https://github.com/andreasbrett), [东端应用](https://github.com/easterapps), [地狱科技27](https://github.com/hecktech27), [mib1185号](https://github.com/mib1185) |
| `de-CH` | 施维泽尔迪施 | [多做出的承诺,多蒂内利](https://github.com/dontinelli) |
| `el` | Ελληνικά | [阿波玛](https://github.com/apo-mak), [恰齐科](https://github.com/chatziko) |
| `en` | 联合国 | [曼达伦格里夫芬](https://github.com/mrdarrengriffin), [生动板](https://github.com/vividboarder) |
| `es` | 西班牙语Name | [达夫克斯](https://github.com/davefx), [双层](https://github.com/duhow) |
| `et` | 节日 | 还没有 |
| `eu` | 欧斯卡拉 | [尔泽](https://github.com/urtzai) |
| `fa` | فارسی | 还没有 |
| `fi` | 苏美 | [阿基玛吉](https://github.com/Arkkimaagi), [萨莱克语Name](https://github.com/salleq) |
| `fr` | 法国语Name | [jlpouffier (英语).](https://github.com/jlpouffier), [piitaya (英语).](https://github.com/piitaya) |
| `ga` | 盖尔日 | [艾伦·格林](https://github.com/AlanGreene) |
| `gl` | 加利西亚语Name | [齐伯诺克斯语Name](https://github.com/cibernox) |
| `gu` | 古吉拉特语 | 还没有 |
| `he` | עברית | [倾角](https://github.com/leranp), [汉姆 -b](https://github.com/haim-b) |
| `hi` | हिन्दी | [阿曼克鲁克克斯语Name](https://github.com/amankrokx) |
| `hr` | 赫尔瓦茨基 | [斯普尔科](https://github.com/spuljko) |
| `hu` | 马吉亚尔 | [纳吉罗比](https://github.com/nagyrobi), [v1k70rk4](https://github.com/v1k70rk4) |
| `hy` | հայերեն | [ean](https://github.com/eantonya), [沙汉94](https://github.com/shahen94) |
| `id` | 印度尼西亚 | 还没有 |
| `is` | 斯伦斯卡 | [小时](https://github.com/thdg) |
| `it` | 意大利语Name | [阿纳阿斯盖普斯](https://github.com/auanasgheps), [xraver 软件](https://github.com/xraver) |
| `ja` | 日本語 | 还没有 |
| `ka` | ქართული | [赫兹格](https://github.com/hertzg) |
| `kn` | ಕನ್ನಡ | 还没有 |
| `ko` | 한국어 | [无限百网](https://github.com/limitless00net) |
| `kw` | 克尔尼韦克 | 还没有 |
| `lb` | 吕泽布尔格施 | [茂济子秀](https://github.com/mojikosu) |
| `lt` | 利图维ų | 还没有 |
| `lv` | 拉特维苏 | [机械技术](https://github.com/makstech), [克莱杰](https://github.com/klejejs) |
| `ml` | മലയാളം | [阿伦谢克](https://github.com/arunshekher) |
| `mn` | монгол хэл | [{\fn黑体\fs22\bord1\shad0\3aHBE\4aH00\fscx67\fscy66\2cHFFFFFF\3cH808080}你觉得呢?](https://github.com/chuk-a) |
| `mr` | 马拉蒂 | 还没有 |
| `ms` | 巴哈萨·梅莱尤 | [zu2k](https://github.com/zubir2k) |
| `nb` | 诺斯克 Bokmål | [拉斯特拉达](https://github.com/LaStrada) |
| `ne` | नेपाली | [(原始内容存档于2019-09-21). Rrp13](https://github.com/Rrp13) |
| `nl` | 荷兰 | [联邦](https://github.com/TheFes) |
| `pa` | 旁遮普语Name | [平方公里wl](https://github.com/kmlkrwl) |
| `pl` | 波尔斯基 | [乌里齐埃尔01](https://github.com/Uriziel01), [智通格伦](https://github.com/witold-gren) |
| `pt` | 葡萄牙 | [乔奥尔贡卡尔夫](https://github.com/joaorgoncalves), [腹胀](https://github.com/abmantis) |
| `pt-BR` | 葡萄牙语( 布拉西尔语) | [缩写](https://github.com/mhentschke), [卢伊兹费尔南多08](https://github.com/luyzfernando08), [静态dev](https://github.com/staticdev) |
| `ro` | 罗曼 | [泰尔](https://github.com/tetele), [加比马尔奇丹](https://github.com/gabimarchidan) |
| `ru` | Русский | [肝脏3](https://github.com/HepoH3) |
| `sk` | 斯洛文契纳 | [卢博斯·卡达西](https://github.com/LubosKadasi) |
| `sl` | 斯洛文基纳 | [安德列日2号](https://github.com/andrejs2) |
| `sr` | Српски | [克夫拉丹岛](https://github.com/cvladan), [ddxic 数据](https://github.com/ddxic), [暗黑线79](https://github.com/darkobg79), [彭贝格](https://github.com/PengBG) |
| `sr-Latn` | 斯普斯基语Name | 还没有 |
| `sv` | 斯文斯卡语Name | [拉尔斯杜奈马克](https://github.com/larsdunemark), [罗宾圣](https://github.com/Robin-St) |
| `sw` | 斯瓦希里语Name | [喀麦隆](https://github.com/BCorbeek) |
| `ta` | தமிழ் | 还没有 |
| `te` | తెలుగు | 还没有 |
| `th` | ภาษาไทย | 还没有 |
| `tr` | Türkçe | [缩写](https://github.com/alpdmrel) |
| `uk` | Українська | [天际网](https://github.com/skynetua) |
| `ur` | اُردُو | [亚利安汗](https://github.com/AalianKhan) |
| `vi` | Tiếng Việt | [锡金赫82](https://github.com/dinhchinh82) |
| `zh-CN` | 简体中文 | [等一可以根据](https://github.com/al-one) |
| `zh-HK` | 繁體中文（香港） | [摇摆](https://github.com/swonge) |
| `zh-TW` | 繁體中文（台灣） | [蓝狐狸](https://github.com/bluefoxlee) |

马拉蒂(`mr`)被列出,但还没有句子.笃 我们都认为 `sr-Latn` 是由`sr` 生成的 `sr` : 在`sr` 中更改塞尔维亚语, 拉丁文版本如下 。

## 添加新语言 {#add-a-new-language}

你语言不见了吗? 你可以加起来。 这是比改进现有语言更大的第一步,因此计划进行几轮审查。

### 创建文件 1. {#1-create-the-files}

设置 [提供判刑和答复](/translate/voice/contributing#pick-your-setup) 中描述的寄存器, 然后运行 :

```shell
python3 -m script.intentfest add_language <code> <native name>
```

- `<code>`是语言代码。 使用两个字母 [ISO 639-1 国际标准化组织](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) 代码, 如果有一个, 如 `pl` 。一项或多项区域或脚本变体增加了后缀,如`pt-BR`或`sr-Latn`.
- `<native name>`是语言本身中语言的名称,如`Polski`.
- 向左写入语言时添加 `--rtl` 。

脚本将您的语言添加到 `languages.yaml` 中, 并创建其句子, 响应, 并测试来自英语的文件 。 句子是空的,回复以 `TODO` 开头, 这样你就可以看到还需要翻译什么 。

无法自己运行剧本? 在 [语文领导人**](https://discord.com/channels/330944238910963714/1257022942961991781) 频道中询问 Home Assistant [Discord 服务器](https://www.home-assistant.io/join-chat) , 维护者可以为您运行 。

### 2.  保持第一个pull request 小 {#2-keep-the-first-pull-request-small}

将您的第一个 pull request 限制为 :

- `sentences/<code>/_common.yaml`中的错误反应
- `HassTurnOn`和`HassTurnOff`的插槽组合,即`intents.yaml`标记为`required`,以及他们的测试。
- `lists/<code>/`中的列表 和`rules/<code>/`中的规则 这些句子需要。

这足以让人们开始用你的语言 打开和关闭东西。 以后的 pull requests 中会有更多意图, 一次一个。

### 寻找领导者 {#3-find-a-leader}

新语言在没有领导者的情况下开始. 如果您继续贡献, 请考虑 {L邱} 。

> [!NOTE]
> 语音和接口是分开的. 在此添加语言不会将其添加到 Home Assistant 界面 。 关于这一点,见[请求新语言](/translate/guides/new-language)。
