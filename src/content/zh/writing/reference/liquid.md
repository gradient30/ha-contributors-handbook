---
title: 目录
description: 每个液态标记 home-assistant.io 在Markdown上添加,从我的链接和词汇工具提示到文本框和可重复使用的片段.
order: 3
---

# 目录 {#liquid-helpers}

[Home Assistant.io](https://www.home-assistant.io/) 与 Jekyll 一起建造, 它使用 [液体](https://shopify.github.io/liquid/) 来调温. 在Plain Markdown上,网站为Markdown无法完成的事情添加了一组Liquid标签:链接到读者自己的Home Assistant,词汇工具提示,图标,文本框等等.

用他们帮助读者的地方,而不是因为他们在那里。 包装内容的标记,像文本框一样,有一个匹配的关闭标记,开始于 `end` :

```liquid
{% tip %}
This text is inside the tag.
{% endtip %}
```

## 我的立足点 {#my-links}

一个我的链接打开了读者自己 Home Assistant 安装的页面 。 当您发送读取器到界面中的地方时使用一个, 这样它们可以直接跳到那里而不是通过菜单搜索 :

```liquid
Go to {% my integrations title="**Settings** > **Devices & services**" %} and select your integration.
```

`my`之后的第一个单词是页面的名称. `title` 是链接文本 。 将其写成UI路径, 以粗体表示 `>` 在步骤之间, 与任何 [透视路径](/writing/reference/style#ui-elements-and-steps) 相同 。

这些是我最需要的链接:

```liquid
- {% my areas title="**Settings** > **Areas, labels & zones**" %}
- {% my automations title="**Settings** > **Automations & scenes**" %}
- {% my backup title="**Settings** > **System** > **Backups**" %}
- {% my general title="**Settings** > **System** > **General**" %}
- {% my integrations title="**Settings** > **Devices & services**" %}
- {% my labs title="**Settings** > **System** > **Labs**" %}
- {% my logs title="**Settings** > **System** > **Logs**" %}
- {% my network title="**Settings** > **System** > **Network**" %}
- {% my profile title="**User profile**" %}
```

### 查找页面名称 {#find-the-name-of-a-page}

在键盘上打开Home Assistant中的页面并按`m`。 Home Assistant 显示我的链接 如果有的话 名称是链接的最后一部分:对于`https://my.home-assistant.io/redirect/logs/`,它是`logs`.

[我的链接创造者](https://my.home-assistant.io/create-link/) 列出每个 我的链接, 与它所需要的参数。

### uko. 其他选择 {#other-options}

多数 {\3cHFF8000}我只需要一个... 向着我们这群人

- `badge` 显示链接为 My 徽章图像而不是文本 。 徽章不能有一个 `title` 。
- `domain` 设置需要一个页面的集成, 如 `config_flow_start`, 它开始设置一个特定的集成 。
- `addon`,`blueprint_url`,`brand`,`repository_url`和`service`通过该页面应打开的应用,蓝图,品牌,寄存器,或动作.
- `search` 在有1页的页面中填入搜索字段, 如`logs` 。
- `provider`,`integration`和`raw` 选择 `logs` 页面显示的内容 。 `provider` 是要打开的日志, 如 `supervisor` 或 app swit 。 `integration` 过滤 Home Assistant Core 日志到一个或多个集成, 用逗号分隔 。 `raw` 显示完整的Home Assistant Core 日志, 而不是只显示错误 。

```liquid
{% my config_flow_start badge domain="hue" %}
{% my blueprint_import badge blueprint_url="https://example.com/blueprint.yaml" %}
{% my logs title="**Settings** > **System** > **Logs**"
   provider="supervisor" search="token" %}
```

没有 `title` , 链接会回到默认文本 。 此默认并不总是跟随 [样式指南承担起](/writing/reference/style) , 因此在运行的文本中为链接添加 `title` 。

## 词汇提示 {#glossary-tooltips}

Home Assistant有它自己的词汇:实体,设备,集成,区域,还有更多. [,](https://www.home-assistant.io/docs/glossary/)解释一下 在您的页面上标注一个名词,读者在工具提示中看到它的定义,往往有一个链接来学习更多:

```liquid
{% term <term> [<text>] %}
```

一些例子:

```liquid
{% term integration %}
{% term entity %}
{% term "configuration.yaml" %}
{% term "Home Assistant Operating System" %}
```

- 含有空格或点的引文。 ** 单词可以去而不引.
- ** Aliass 也工作。 ** 每个词汇条目可以列出别名,如复数形式. 所以 `automations` 和 `automation` 一样有效 。 匹配忽略了资本化.
- ** 该词必须存在。 ** 当词汇表中没有术语时, 构建失败了, 所以“ 部署预览” 为您捕获了 types 。

默认情况下,工具提示将术语本身显示为文本. 要将工具提示放在不同的词上,在词后添加文字:

```liquid
I used an {% term automation "automation to turn on the lights" %} at sunset.
```

您不需要标记一个术语的每一个发生 。 在页面中首次出现时标注,或者读者最有可能偶然发现的地方标注.

### 在词汇表中添加一个术语 {#add-a-term-to-the-glossary}

缺少一个术语,还是找到一个更明确的定义? 编辑[`source/_data/glossary.yml`](https://github.com/home-assistant/home-assistant.io/blob/current/source/_data/glossary.yml). 条目按字母顺序排列,每个条目都有这些密钥:

- `term`:这个词本身。 要求。
- `definition`:完整解释,显示在词汇页上. 要求。
- `excerpt`:工具提示的较短版本. 定义较长时添加一个 。
- `link`:一个读者可以多学习的页面.
- `aliases`:其他应该匹配的术语形式,如复数.

```yaml
- term: Scene
  definition: >-
    Scenes capture the states you want certain entities to be. For example, a
    scene can specify that light A should be turned on and light B should be
    bright red.
  link: /integrations/scene/
  aliases:
    - scenes
```

[该网站的词汇表](/glossary)是一个不同的。 它解释了在贡献Home Assistant时所使用的术语.

## 内嵌图标 {#inline-icons}

要指向界面中的图标,请显示其内含. 图标来自 [图标上的材料设计图标](https://icon-sets.iconify.design/mdi/), 同集 Home Assistant 使用 :

```liquid
Select the three dots {% icon "mdi:dots-vertical" %} menu.
```

图标根据其名称获得工具提示. 要设置自己的,请添加 `title` :

```liquid
{% icon "mdi:dots-vertical" title="Three dots menu" %}
```

您将最需要的图标脾气:

```liquid
- Three dots menu: {% icon "mdi:dots-vertical" %}
- Hamburger menu: {% icon "mdi:menu" %}
- Edit: {% icon "mdi:edit" %}
- Revert: {% icon "mdi:restore" %}
- Eye: {% icon "mdi:eye" %}
- Trash: {% icon "mdi:trash" %}
- Cog: {% icon "mdi:cog" %}
- Cog outline: {% icon "mdi:cog-outline" %}
- Drag: {% icon "mdi:drag" %}
- Move cursor: {% icon "mdi:cursor-move" %}
- Arrow left: {% icon "mdi:arrow-left-bold" %}
- Arrow right: {% icon "mdi:arrow-right-bold" %}
- Checkbox list: {% icon "mdi:order-checkbox-ascending" %}
- Upload network: {% icon "mdi:upload-network" %}
- Security network: {% icon "mdi:security-network" %}
- Routes: {% icon "mdi:routes" %}
```

要找到其它图标的名称, 请在 Iconify 上查找, 并在名称前置 `mdi:` 。

## 可折叠的细节媲美 {#collapsible-details}

一个细节块隐藏内容直到读者打开. 用它来表达大多数读者可以跳过的内容,比如如何从一个卖家那里获得证书,或者列出每个读者只需要一个的解决问题的清单:

```liquid
{% details "Generate a client ID and client secret" %}

1. Register your account as a developer account at the vendor's developer portal.
2. Create a new application.
3. Enter an **Application name** of your choice, for example **Home Assistant**.

{% enddetails %}
```

- 单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单 写单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单 对于故障排除,请使用症状或错误消息.
- ** Markdown在标题中工作,** 就像代码的背影。
- ** 在标题前添加一个图标 ** , 加上 `icon` 选项, 如 `icon="mdi:information"` 。
- ** 打开标记之后和关闭标记之前留下空白的行**,所以内部的Markdown是适当的.

使用 Liquid 细节块,而不是 HTML `<details>` 元素 。 Liquid版本与网站的外观相符.

## 文本框 {#text-boxes}

文本框使其周围的文本突出信息。 它们只在罕见的时候才工作:一页满满的盒子里没有任何东西是突出的. 在添加一个之前,问问你自己,如果一个简单的句子会做。

有六类. 选择一个匹配消息:

- ** Tip:** 使事情变得容易或更好的建议。 如果读者跳过它,就不会出问题.
- ** 注:**额外信息有帮助,但不属于主流.
- 耿耿于怀: 读者不能错过成功,
- **Caution:**可以造成数据丢失,出乎意料的行为,或其他难以撤销的结果的动作.
- ** 警告:** 危及系统的安全或完整性,或人身伤害。 最强的盒子 留到真正需要的时候
- **Labs:**标记了一个属于Labs预览功能的功能,并告诉读者如何打开.

```liquid
{% tip %}
Group your lights in an area, so you can turn them all off with one action.
{% endtip %}

{% note %}
The integration updates the data every 5 minutes.
{% endnote %}

{% important %}
Your device needs firmware version 2.0 or later.
{% endimportant %}

{% caution %}
Removing the integration also removes all its entities from your automations.
{% endcaution %}

{% warning %}
Disconnect the power before you open the device.
{% endwarning %}

{% labs %}
Requires the **Feature name** Labs preview feature. Enable it at {% my labs title="**Settings** > **System** > **Labs**" %}.
{% endlabs %}
```

每个框都显示其为标题,如**Tip**。 要添加该标题,请使用`title`. 要替换默认图标, 请使用 `icon` :

```liquid
{% note title="Older devices" icon="mdi:router-wireless" %}
Devices from before 2020 need a firmware update first.
{% endnote %}
```

该框显示**注:旧设备**为标题。

## 示例块 {#example-blocks}

`example` 块显示一个蜕变的自动化,脚本,模板,或上面有标签的其他代码,并带有内置的词汇工具提示和语法加亮. 用它来做例子 阅读器的本意是理解和适应,而不是一个简单的代码块.

内容为YAML. 它的第一个键设置了标签,代码作为块下方有 `|` :

```liquid
{% example %}
automation: |
  alias: "Match fan to ceiling light"
  triggers:
    - trigger: light.brightness_changed
      target:
        entity_id: light.living_room_ceiling
      options:
        threshold: 10
  actions:
    - action: fan.set_percentage
      target:
        entity_id: fan.living_room
      data:
        percentage: >-
          {{ state_attr('light.living_room_ceiling', 'brightness_pct') | int }}
{% endexample %}
```

这些密钥设置了输入类型, 上面显示的标签 。 它们在[`plugins/example.rb`](https://github.com/home-assistant/home-assistant.io/blob/current/plugins/example.rb)中定义:

- `action`
- `automation`
- `condition`
- `script`
- `template`
- `trigger`

每块用一个 3个可选键 添加:

- `output` 显示其下方代码的结果, 中间有箭头 。 这对模板特别有用.
- 拱H0 命名结果类型, 显示在输出标签旁边 。 例如,`string`或`number`。
- `title` 在标签中添加一个简短的描述, 如 **Template:以此作为一个温度格式**.

```liquid
{% example %}
template: |
  {% from 'formatter.jinja' import format_entity %}
  {{ format_entity('sensor.outdoor_temperature') }}
  {{ format_entity('sensor.indoor_temperature') }}
output: |
  Outdoor temperature: 22.5
  Indoor temperature: 21.0
{% endexample %}
```

代码块的80字符限制也在这里适用. 以 `>-` 创建多行的长模板 。

## 可重复使用的文本 {#reusable-text}

一些案文在许多页上出现,例如增加综合的步骤。彬然不复制, 包括来自 [`source/_includes`](https://github.com/home-assistant/home-assistant.io/tree/current/source/_includes) 的共享片段 :

```liquid
{% include integrations/config_flow.md %}
```

路径相对 `source/_includes` 。 当共享文本改变时,包含它的每一页都会随其变化.

一些片段取参数. 检查片段文件以查看它读到的片段 : 文件以和平方式写为 `include.<name>` 的都是参数 。

```liquid
{% include integrations/wwha.md url="https://www.eltako.com" name="Eltako" %}
```

在整合页面中经常看到的片段 :

- `integrations/config_flow.md`:如何通过UI添加整合.
- `integrations/option_flow.md`: 设置后如何改变整合选项 。
- `integrations/remove_device_service.md`:如何去除整合.
- `integrations/supported_brand.md`: 对于通过另一种整合支持的品牌.

## 配置块 {#configuration-blocks}

整合页面描述他们的选项与 `configuration_basic` 块,用于UI中设置的选项,以及 YAML 选项的 `configuration` 块. 两者都涵盖在[整合页面](/writing/reference/integration-page)中.
