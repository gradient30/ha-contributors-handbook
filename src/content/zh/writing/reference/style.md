---
title: 文档样式指南
description: home-assistant.io上的每页语言、语气和Markdown格式化规则。
order: 1
sidebarLabel: 样式指南
---

# 文档样式指南 {#documentation-style-guide}

文件遵循[微软写样式指南](https://learn.microsoft.com/en-us/style-guide/welcome/)。 对于拼写和单词使用,它使用[梅里亚姆-韦伯斯特](https://www.merriam-webster.com/),同样的词典微软依赖. 本页列出我们在上面添加的规则,以及你遇到最多的规则.

页面用 [GitHub 模糊的标记](https://github.github.com/gfm/) 写成, 包含一些 [目录](/writing/reference/liquid) 用于 Markdown 无法焰头 。 图像和视频有 [它们的页面](/writing/reference/images), [YAML 实例](/writing/reference/yaml) 也是如此 。 如何组织页面,请见[结构 a 页](/writing/guides/structure)。

## 语言和语气 {#language-and-tone}

- ** 用美国英语写作。 ** Home Assistant在世界各地使用,许多读者不是母语英语。 短句和直白的言语帮助了所有人。
- ** 与读者交谈。 ** 使用"你"和"你的",而不是"用户"或"用户".
- ** 友好和直接。 ** 写得像你在向一个喜欢科技的朋友解释 资料性和个人性,不正式或技术性。
- ** 为使用UI的人写作。 ** 大多数读者从不打开YAML文件. 首先显示UI路径,并将YAML或其他手动配置作为需要时的选项.
- 感觉可以接近 避免措辞使其听起来脆弱、困难或容易打破。 不要将YAML或更复杂的特性称为"先进",除非产品本身使用这个词.
- 老实说 不要隐藏营销语言背后的限制或复杂性. 说一些能做和不能做的
- ** 具有包容性。 ** 保持写作客观如意,不带性别偏见,两极化的言论,以及任何基于种族或宗教而排斥人们的东西. 写入不遵循此选项可能违反 [行为守则](https://github.com/home-assistant/home-assistant.io/blob/current/CODE_OF_CONDUCT.md) 。

## 词语和术语 {#words-and-terminology}

- ** 全文写"Home Assistant"。 ** 不是"HA"或"HASS".
- ** 使用"选择",而不是"点击". ** "点击"只为鼠标工作. "选择"为触摸屏,键盘,屏幕阅读器也工作. 仅在描述鼠标特定动作时使用"单击",如右击或双击.
- ** Skip 拉丁语缩写。 ** 不要写"例如","即","etc",或"etcetera". 使用"类似","例如",或者"例如"代替.
- ** 不要使用"主人/奴隶"。 ** 使用符合上下文的[备选案文](https://learn.microsoft.com/en-us/style-guide/a-z-word-list-term-collections/m/master-slave),例如"客户/服务器","领导/跟随者","main/replica",或"controller/device".
- ** 匹配名称的正式拼写。 ** 品牌,服务,协议,集成,以及平台都是用其所有者写作的方式书写. 例如,"Z-Wave",而不是"Z波","Z波","Z波",或者"ZWave". 同样的情况还有"GitHub","WebSocket","Wi-Fi".
- ** 统一使用术语表。 ** 当一个页面像实体,设备,或集成一样使用 Home Assistant 术语时, 用它来定义它. 您可以在 [Home Assistant.io](https://www.home-assistant.io/) 上显示定义为工具提示, 见 [词汇提示](/writing/reference/liquid#glossary-tooltips) 。

自动检查执行长清单的品牌和产品拼写. 名单在[`.textlintrc.json`](https://github.com/home-assistant/home-assistant.io/blob/current/.textlintrc.json)里 如果检查标记为正确拼写的名称,请在同一pull request中添加。 请参看[自动检查](/writing/reference/checks) 检查如何工作 。

## 标点语法和语法 {#punctuation-and-grammar}

- ** 使用牛津逗号。 ** 在)、三个或三个以上项目的列表中,在“和”或“或”之前加上逗号:“Zigbee、Z-Wave和Matter”。
- ** 刑期届满。 ** 遵循正常的语法规则,同样在列表项目中为满句.
- ** 一段时间后使用一个空间。 ** 从来没有两个。
- * 轻点* 太多的人产生长的,缠绕的句子,它们是机器写作文字的常见标志. 修改句子结构:
  - 将长句分为两短句.
  - 我还以为是名单还是解释呢? 我还以为是结肠呢
  - 加入一个进行检查? 用括号或进行检查。

  如果一个破折号真的是最好的选择, 请遵循 [梅里亚姆-韦伯斯特风格](https://www.merriam-webster.com/grammar/em-dash-en-dash-how-to-use) : 一个没有周围空格的 em破折号 。 复合词中的连字符,如"内 你自己建"或"Z-Wave",都很好.

## 还会如何格式化基础 {#formatting-basics}

- ** 以流动文本写。 ** 没有线长度限制。 每段保持单行,不以固定宽度包裹线条. 这使得页面更容易编辑,特别是在GitHub的在线编辑器中.
- ** 在HTML上优先标注。 ** 只当Markdown无法完成任务时使用 HTML, 就像一个带有标题的图像一样.
- ** 带空白线的轮廓区块。 ** 标题、列表、代码块和文本框在它们前后都需要一条空行。

## 标题 {#headings}

一页的标题是它的一级标题. 它来自文件顶端的前题`title`,所以你从不写`#`自己:

```markdown
---
title: "Create an automation"
---
```

页面内容从标题2开始. 使用带有 `#` 字符的 Markdown 标题, 从 2 级到 6 级 :

```markdown
## Heading level 2 {#heading-level-2}
### Heading level 3 {#heading-level-3}
#### Heading level 4 {#heading-level-4}
##### Heading level 5 {#heading-level-5}
###### Heading level 6 {#heading-level-6}
```

- ** 使用判刑案件。 ** 将第一个单词和正名只资本化:"创建自动化",而不是"创建自动化". 微软有[更多关于资本化](https://learn.microsoft.com/en-us/style-guide/capitalization).
- ** 不要跳过级别。 ** 4级头部始终位于3级头部之下.
- ** 知道目录中显示的内容。 ** 在home-assistant.io上,只有第2和第3级标题出现在页面旁边的目录中。旷课后,
- ** 主题名称。 ** "地区设置"这样的标题告诉读者接下来的内容. "总览"或"好知"则不然. [结构 a 页](/writing/guides/structure)每个科都有建议。

## 强调 {#emphasis}

- ** 强调的意大利语。 ** 使用下划线: `_emphasized words_`. 不要使用单一星号。
- ** 没有重点首都。 ** 在所有 CAPS 中写作为喊叫。
- ** 无黑体强调。 ** 粗体保留给UI元素. 也不要用粗体文字代替标题。

少加强调 当万物显露,无所不至.

## UI 元素和步骤 {#ui-elements-and-steps}

用粗体写出UI元素的名称或显示的UI文本,例如传感器状态,使用双星号:`**Settings**`. 把它们写在界面里

要描述通过接口的路径,请在步骤之间使用一个大于符号(`>`)的符号. `>`本身不是大胆的 :

```markdown
1. Go to **Settings** > **Devices & services**.
2. Select **Restart Home Assistant** > **Quick reload**.
```

要写入您在UI中看到的错误信息, 请不要使用粗体 。 以引号输入信件。

当路径开始于{H0 很显然的带来的好处是,使用[我的连结](/writing/reference/liquid#my-links),这样读者就可以在自己的安装中直接跳到该页面. 要指向界面中的图标,请使用[内嵌图标](/writing/reference/liquid#inline-icons).

## 文件路径、名称和输入 {#file-paths-names-and-input}

对文件路径、文件名称、可变名称和阅读器输入字段的任何文字使用回击:

- 文件 `/boot/config.txt`
- 文件 `configuration.yaml`
- `this` 变量
- 输入 `/newbot`

当一个实例中的值需要替换为读者自己的值时,用下划线在首都写,如{H0ý}或`REPLACE_ME`.

## 列表 {#lists}

- ** 选择正确的类型。 ** 使用一个编号列表来显示按顺序发生的步骤。 命令无关紧要时使用子弹.
- ** 对子弹使用`-`。 ** 不是`*` 或`+`。
- ** 适当订购的清单数目。 ** 每行写`1.`,`2.`,`3.`,而不是`1.`.
- ** 每个项目以大写字母开始,** 除非有理由不使用,比如命令或代码值。
- ** 保持标点一致。 ** 如果至少有一项是完整的句子,则以一个期限结束每一项。 如果不是,则完全不用时间。
- ** 不结束带有分号、逗号或“和”或“或”的项目。 **
- ** 名单前后留一行空白。 **

```markdown
1. Select **Create area**.
2. Enter a **Name** for the area.
3. Select **Create**.
```

## 代码块 {#code-blocks}

使用带有三个反键的有栅栏的代码块,并且总是在打开反键后指定语言:

````markdown
```

雅姆尔
自动化 :
  - 化名:日落时在门廊灯光上转

```
```

`

home-assistant.io上的语法突出显示使用[棱镜](https://prismjs.com/). 通用语言名称为:

- `yaml`用于配置和自动化(使人们看到YAML内部的模板也被强调)
- 用于独立模板的 `template` 或 `jinja2`
- 命令的 `bash` 或 `shell`
- `json`
- `python`
- `markdown`
- `html`
- `text` 纯输出, 如日志行

1999年12月31日,纽约

- ** 每行保持低于80个字符。 ** 较长的线路迫使读者滚动侧面,特别是在电话上.
- ** 不 `$` 在命令前提示。 ** 读者从页面直接复制命令,并迅速解开。 只当块也显示输出时使用一个,需要提示符来告诉命令与其打印的内容不同.
- *最有背力的栅栏* 为了在代码块内显示一个代码块,给外侧的栅栏比内侧的要多回击. 四个背影环绕一个街区,使用三个,五个环绕一个街区,使用四个.

`````markdown
```

减记

```yaml
key: value
```

````
```

``

YAML的例子有它们自己的缩进规则,引用,等等. 见[YAML 样式](/writing/reference/yaml).

## 表格 {#tables}

避开桌子匙子,许多人在手机上阅读文档,在小屏幕上宽的桌子很难使用. 列表几乎总是效果更好:

- 一张两栏的表格是一个伪装的列表. 写为一体.
- 如果无法避免表格,请将列数和每个单元格中的文字保持低调。
- 对于配置选项,使用[整合页面](/writing/reference/integration-page)中描述的块代替.

## 链接 {#links}

与Home Assistant的其他网页链接。 io 跟随已公布的 URL, 而不是寄存器中的文件 :

- ** 使用绝对路径,** 从`/`开始。
- ** 退出 `source` 目录。 **
- ** 出第一个目录的主要下划线**。
- ** 结尾为斜线而不是文件扩展名** 如`.markdown`、`.md` 或`.mdx` 。
- ** 不写入完整域名。 ** 使用 `/integrations/date/` 而不是 `https://www.home-assistant.io/integrations/date/` 。

例如,链接到[`source/_integrations/date.markdown`](https://github.com/home-assistant/home-assistant.io/blob/current/source/_integrations/date.markdown) :

```markdown
[Date](/integrations/date)
```

当一个页面غ 或 平台 时, 将其名称链接到其文档页面, 如 `[飞利浦](/integrations/hue)` 。 然后读者可以直接跳到细节.

一般链接:

- ** 无裸体 URL。 ** 不要阐释 `https://example.org` 或 `<https://example.org>` 。 给每个链接一个描述文本。
- ** 没有关联或跟踪链接。 **
- ** 链接文本描述目的地。 ** 避免"这里"或"这个链接".

## 简称和缩略语 {#abbreviations-and-acronyms}

在可以的地方避免缩写和缩写. 当您确实需要时, 请用 `<abbr>` 标记 包裹它对上述标签 。 读者将整个术语视为工具提示:

```html
<abbr title="Audio & video">A/V</abbr>
<abbr title="current transformers">CT</abbr>
<abbr title="Dutch smart meter requirement">DSMR</abbr>
<abbr title="embedded MultiMediaCard">eMMC</abbr>
<abbr title="flash video">FLV</abbr>
<abbr title="Large Language Models">LLMs</abbr>
<abbr title="Model Context Protocol">MCP</abbr>
<abbr title="pan, tilt, and zoom">PTZ</abbr>
<abbr title="real-time messaging protocol">RTMP</abbr>
<abbr title="real-time streaming protocol">RTSP</abbr>
<abbr title="USB-On-The-Go">USB-OTG</abbr>
```

对于Home Assistant自己的条件,一个[单词](/writing/reference/liquid#glossary-tooltips)是更好的选择.
