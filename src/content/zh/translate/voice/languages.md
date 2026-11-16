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
| `af` | Afrikaans | None yet |
| `ar` | العربية | [Ahmed-farag36](https://github.com/Ahmed-farag36), [Natfaji](https://github.com/Natfaji) |
| `bg` | Български | [hristo-atanasov](https://github.com/hristo-atanasov) |
| `bn` | বাংলা | [poltalashka](https://github.com/poltalashka), [DrHaque](https://github.com/DrHaque) |
| `ca` | Català | [duhow](https://github.com/duhow) |
| `cs` | Čeština | [halecivo](https://github.com/halecivo), [schizza](https://github.com/schizza) |
| `cy` | Cymraeg | None yet |
| `da` | Dansk | [fadamsen](https://github.com/fadamsen), [MTrab](https://github.com/MTrab) |
| `de` | Deutsch | [andreasbrett](https://github.com/andreasbrett), [easterapps](https://github.com/easterapps), [hecktech27](https://github.com/hecktech27), [mib1185](https://github.com/mib1185) |
| `de-CH` | Schwyzerdütsch | [dontinelli](https://github.com/dontinelli) |
| `el` | Ελληνικά | [apo-mak](https://github.com/apo-mak), [chatziko](https://github.com/chatziko) |
| `en` | English | [mrdarrengriffin](https://github.com/mrdarrengriffin), [vividboarder](https://github.com/vividboarder) |
| `es` | Español | [davefx](https://github.com/davefx), [duhow](https://github.com/duhow) |
| `et` | Eesti | None yet |
| `eu` | Euskara | [urtzai](https://github.com/urtzai) |
| `fa` | فارسی | None yet |
| `fi` | Suomi | [Arkkimaagi](https://github.com/Arkkimaagi), [salleq](https://github.com/salleq) |
| `fr` | Français | [jlpouffier](https://github.com/jlpouffier), [piitaya](https://github.com/piitaya) |
| `ga` | Gaeilge | [AlanGreene](https://github.com/AlanGreene) |
| `gl` | Galician | [cibernox](https://github.com/cibernox) |
| `gu` | Gujarati | None yet |
| `he` | עברית | [leranp](https://github.com/leranp), [haim-b](https://github.com/haim-b) |
| `hi` | हिन्दी | [amankrokx](https://github.com/amankrokx) |
| `hr` | Hrvatski | [spuljko](https://github.com/spuljko) |
| `hu` | Magyar | [nagyrobi](https://github.com/nagyrobi), [v1k70rk4](https://github.com/v1k70rk4) |
| `hy` | հայերեն | [eantonya](https://github.com/eantonya), [shahen94](https://github.com/shahen94) |
| `id` | Bahasa Indonesia | None yet |
| `is` | íslenska | [thdg](https://github.com/thdg) |
| `it` | Italiano | [auanasgheps](https://github.com/auanasgheps), [xraver](https://github.com/xraver) |
| `ja` | 日本語 | None yet |
| `ka` | ქართული | [hertzg](https://github.com/hertzg) |
| `kn` | ಕನ್ನಡ | None yet |
| `ko` | 한국어 | [limitless00net](https://github.com/limitless00net) |
| `kw` | kernewek | None yet |
| `lb` | Lëtzebuergesch | [mojikosu](https://github.com/mojikosu) |
| `lt` | Lietuvių | None yet |
| `lv` | Latviešu | [makstech](https://github.com/makstech), [klejejs](https://github.com/klejejs) |
| `ml` | മലയാളം | [arunshekher](https://github.com/arunshekher) |
| `mn` | монгол хэл | [chuk-a](https://github.com/chuk-a) |
| `mr` | Marathi | None yet |
| `ms` | Bahasa Melayu | [zubir2k](https://github.com/zubir2k) |
| `nb` | Norsk Bokmål | [LaStrada](https://github.com/LaStrada) |
| `ne` | नेपाली | [Rrp13](https://github.com/Rrp13) |
| `nl` | Nederlands | [TheFes](https://github.com/TheFes) |
| `pa` | Punjabi | [kmlkrwl](https://github.com/kmlkrwl) |
| `pl` | Polski | [Uriziel01](https://github.com/Uriziel01), [witold-gren](https://github.com/witold-gren) |
| `pt` | Português | [joaorgoncalves](https://github.com/joaorgoncalves), [abmantis](https://github.com/abmantis) |
| `pt-BR` | Português (Brasil) | [mhentschke](https://github.com/mhentschke), [luyzfernando08](https://github.com/luyzfernando08), [staticdev](https://github.com/staticdev) |
| `ro` | Română | [tetele](https://github.com/tetele), [gabimarchidan](https://github.com/gabimarchidan) |
| `ru` | Русский | [HepoH3](https://github.com/HepoH3) |
| `sk` | Slovenčina | [LubosKadasi](https://github.com/LubosKadasi) |
| `sl` | Slovenščina | [andrejs2](https://github.com/andrejs2) |
| `sr` | Српски | [cvladan](https://github.com/cvladan), [ddxic](https://github.com/ddxic), [darkobg79](https://github.com/darkobg79), [PengBG](https://github.com/PengBG) |
| `sr-Latn` | Srpski | None yet |
| `sv` | Svenska | [larsdunemark](https://github.com/larsdunemark), [Robin-St](https://github.com/Robin-St) |
| `sw` | Kiswahili | [BCorbeek](https://github.com/BCorbeek) |
| `ta` | தமிழ் | None yet |
| `te` | తెలుగు | None yet |
| `th` | ภาษาไทย | None yet |
| `tr` | Türkçe | [alpdmrel](https://github.com/alpdmrel) |
| `uk` | Українська | [skynetua](https://github.com/skynetua) |
| `ur` | اُردُو | [AalianKhan](https://github.com/AalianKhan) |
| `vi` | Tiếng Việt | [dinhchinh82](https://github.com/dinhchinh82) |
| `zh-CN` | 简体中文 | [al-one](https://github.com/al-one) |
| `zh-HK` | 繁體中文（香港） | [swonge](https://github.com/swonge) |
| `zh-TW` | 繁體中文（台灣） | [bluefoxlee](https://github.com/bluefoxlee) |

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
