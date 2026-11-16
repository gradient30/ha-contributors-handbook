---
title: 整合页面结构
description: 整合页面的段落顺序,以及您用来填充的块和可重复使用的文本。
order: 6
---

# 整合页面结构 {#integration-page-structure}

每个整合页都遵循相同的结构. 了解一页内容的读者可以在所有这些内容上找到方向,审查人员可以一眼就能发现缺失的内容.

你不必从头开始。 复制 [整合页面模板](https://github.com/home-assistant/home-assistant.io/blob/current/source/_integrations/_integration_docs_template.markdown), 它有每个带示例内容的章节 。 周围的台阶,如使用的分支和品牌pull request,都在[综合文件](/writing/guides/integration)中. 页面顶端的密钥为[一体化问题。](/writing/reference/front-matter).

## 节 {#sections}

我保证你们会用到这些区域 我保证你们不会加入

1. ** 导言**,无标题。 集成会做什么,它连接到哪个品牌或服务,以及一个使用案例:有人能用它做什么. 链接到制造商或服务的网站. 如果集成是其他集成使用的一个构件,请从[可重复使用的文本](/writing/reference/integration-page#reusable-text)中添加构件集成文本.
2. ** 辅助装置**:已知可行装置和型号。 当那里有多个版本时,请提及你测试过的版本,包括固件.
3. **未支持的设备**:已知不起作用的设备,所以没有人需要找到困难的方法.
4. ** 先决条件**:读者在设置前所需的一切,按编号步骤排列。 比如在厂商的应用上安装,创建账户,或者获得API密钥或访问令牌. 一步一步解释如何获得证书.
5. ** 构思**:如何增加整合。 对于从UI设置的集成,请使用标准配置文本,然后使用[块 `configuration_basic`](/writing/reference/integration-page#the-configuration_basic-block)来解释设置窗体的每个字段. 对于只使用YAML的集成,请显示`configuration.yaml`的示例,然后显示[块 `configuration`](/writing/reference/integration-page#the-configuration-block)。
6. ** Configation 选项**:读者设置后可以更改的选项,在一个`configuration_basic`块中.
7. ** 支持的功能**:集成所提供的实体,按照每个平台的标题按平台分组,如**传感器**或**按钮**。 对于每个实体,请简单描述一下,在哪些地方有用,哪些设备有它,以及任何评论。
8. **触发器清单**,**条件清单**,**行动清单**:由单独文件生成. 见[触发因素、条件和行动](/writing/reference/integration-page#triggers-conditions-and-actions).
9. ——"本经" ——"本经","本经","本经","本经". 见[实例](/writing/reference/integration-page#examples).
10. 橙色和红外线,橙色的? 它有民意调查吗? 设备是否推动更新?
11. ** 了解的局限性**:整合无法做到的,以及工作与读者预期不同的事情。
12. ** 所犯的障碍**:常见问题,有症状,是什么原因,以及如何解决。
13. ** 社区说明**:可选。 社区分享的提示和经验,比如特定设备的行为方式.
14. ** 取消合并**:如何取消合并。 从标准删除文本开始,并添加阅读器应该做的任何额外工作,比如从制造商的app中删除Home Assistant.

整页的几条规则:

- 步骤和例子与什么 Home Assistant舰只有关。 不依赖自定义集成或自定义卡.
- 当你提到另一个整合时,请链接到它的页面.
- 先描述一下UI的方法 如果有的话,YAML会来
- 在将您的 pull request 标记为可供审查之前, 删除模板中的评论 。

### 支持的功能 {#supported-functionality}

列出每个实体及其细节为嵌入式子弹:

```markdown
### Sensors {#sensors}

- **Boiler temperature**
  - **Description**: Current temperature of the boiler.
  - **Available for machines**: all
  - **Remarks**: About 3 degrees higher than the target temperature,
    because it is measured in a different place.
```

对于选定的实体,增加一个**备选项**,列出选择。

### 实例 {#examples}

每个例子都以一个短标题和句子开头,说明它解决了什么. 然后描述阅读器在UI中构建的自动化方式,然后将YAML版本放入一个可折叠的部分:

```liquid
### Automation: Turn off the status LEDs at night {#automation-turn-off-the-status-leds-at-night}

The status LEDs are bright. Turn them off when the sun goes down.

- **Trigger**: Sun: after sunset
- **Action**: Turn off light

{% details "YAML example for turning off the LEDs at night" %}

{% example %}
automation: |
  alias: "Turn off the LEDs at night"
  triggers:
    - trigger: sun
      event: sunset
  actions:
    - action: light.turn_off
      target:
        entity_id: light.device_leds
{% endexample %}

{% enddetails %}
```

将粘贴 YAML 的提示添加到视觉编辑器中一次, 在示例部分的顶端 :

```liquid
{% include docs/paste_yaml_tip.md %}
```

`example`块接受一个输入:`automation`,`script`,`trigger`,`condition`,`action`,或`template`。 在 [YAML 样式](/writing/reference/yaml) 之后写入 YAML 。

蓝图在寄存器的 [`source/blueprints/integrations/`](https://github.com/home-assistant/home-assistant.io/tree/current/source/blueprints/integrations) 文件夹中进行, 大多在一个以集成域命名的文件夹中, 或者在社区论坛的 [蓝图交换](https://community.home-assistant.io/c/blueprints-exchange) 上. 用 `blueprint_example` 标签在页面上显示它们 。 对于寄存器中的蓝图,请在该文件夹内给出路径:

```liquid
{% blueprint_example blueprint="example/example_notification.yaml" %}
```

标记会制作一个按钮来导入蓝图 。 对于寄存器中的蓝图,它也使与YAML相同的自动化,脚本,或模板实体,供喜欢手设的读者使用. 因此,蓝图文件是这个例子的唯一副本:不要在页面上重复它的YAML. 蓝图可以是`automation`,`script`或`template`的蓝图.

对于在其他地方宿主的蓝图,请给出其URL. 然后,该标记只使导入按钮:

```liquid
{% blueprint_example blueprint="https://community.home-assistant.io/t/example/123" %}
```

### 故障排除 {#troubleshooting}

每个问题都以症状为主,然后是描述和解决:

```liquid
{% details "Can't set up the device" %}

### Symptom: "This device can't be reached" {#symptom-this-device-cant-be-reached}

When you try to set up the integration, the form shows the message
"This device can't be reached".

#### Description {#description}

The device does not allow local connections yet.

#### Resolution {#resolution}

1. Make sure the device is powered on.
2. In the app of the manufacturer, turn on local access.

{% enddetails %}
```

## 触发因素、条件和行动 {#triggers-conditions-and-actions}

集成的哟,每个触发器,条件,和动作,都会得到自己的文件,以及网站上自己的页面. 集成页列出它们,并附有一个列表,从这些文件中建立列表:

```liquid
{% include integrations/triggers.md %}

{% include integrations/conditions.md %}

{% include integrations/actions.md %}
```

每个都增加了自己的二级标题。 如果一个集成物还没有这类文件记录,则包括这些内容,并与所有这些内容的概述联系起来。 如果整合有所有三种,则可以使用一种包括:

```liquid
{% include integrations/triggers_conditions_actions.md %}
```

### 对任何文件 {#where-the-files-go}

每个文件在集成域名和项目名称后命名, 并 `.markdown` 扩展名 :

- 触发器进入 [`source/_triggers/`](https://github.com/home-assistant/home-assistant.io/tree/current/source/_triggers), 如 `light.brightness_changed.markdown` 。
- 条件进入 [`source/_conditions/`](https://github.com/home-assistant/home-assistant.io/tree/current/source/_conditions), 如 `light.is_on.markdown` 。
- 动作在 [`source/_actions/`](https://github.com/home-assistant/home-assistant.io/tree/current/source/_actions) 中进行, 如 `light.turn_on.markdown` 。

### 前题 {#front-matter}

- `title`:名称,如UI所示,如`Light brightness changed`.
- `trigger`,`condition`,或`action`:项目的全名,如`light.brightness_changed`. 使用匹配文件类型的密钥 。
- `domain`:整合的领域,如`light`. 整合页面使用它来查找属于它的文件.
- `description`:关于物品的用途的一句话.
- `related_triggers`,`related_conditions`,或`related_actions`:可选. 页面链接的同类相关项目列表.
- `since`:只有动作,可选. 引入动作的 Home Assistant 发布, 作为引用字符串 。

### 页面布局 {#page-layout}

一个触发文件看起来像这样。 条件和行动遵循的自由布局相同,自身包括: `conditions/...`和`actions/...`,而不是`triggers/...`.

```liquid
---
title: "Light brightness changed"
trigger: light.brightness_changed
domain: light
description: "Triggers when the brightness of one or more lights changes."
related_triggers:
  - light.brightness_crossed_threshold
---

The **Light brightness changed** trigger fires after... Use it to...

{% include triggers/ui_header.md %}

To use this trigger in an automation:

1. Go to {% my automations title="**Settings** > **Automations & scenes**" %}.
2. Open an existing automation, or select **Create automation** >
   **Create new automation**.
3. In the **When** section, select **Add trigger**.
4. Search for and select **Light brightness changed**.
5. Under **Targets**, select what you want to watch.
6. Select **Save**.

### Options in the UI {#options-in-the-ui}

{% options_ui %}
Threshold type:
  description: How much the brightness has to change before it fires.
{% endoptions_ui %}

{% include triggers/yaml_header.md %}

In YAML, refer to this trigger as `light.brightness_changed`:

{% example %}
trigger: |
  trigger: light.brightness_changed
  target:
    entity_id: light.living_room
  options:
    threshold: 10
{% endexample %}

### Options in YAML {#options-in-yaml}

{% options_yaml %}
threshold:
  description: The minimum change in brightness, in percent.
  required: false
  type: any
{% endoptions_yaml %}

{% include triggers/targets.md %}

{% include triggers/behavior.md %}

## Good to know {#good-to-know}

- Anything else the reader should know.

{% include triggers/try_it.md %}

{% include triggers/more_examples.md %}

### Automation: A real use case {#automation-a-real-use-case}

{% include triggers/stuck.md %}

{% include triggers/related.md %}
```

各类差异:

- ** 附加条件**,如果**节,加上**Add条件**。
- ** 行动** 在** 节中增加,然后执行** Add行动**。 脚本也使用动作,不需要触发.
- 保留 `targets.md` 包括项目是否支持目标 。 如果它支持有行为选项的多个目标,则保留 `behavior.md`. 动作没有 `behavior.md` 。
- 在 ** 更多示例** 下,以 [实例](/writing/reference/integration-page#examples) 格式添加一个或多个示例。

### 以 UI 的方式命名项目 {#name-items-the-way-the-ui-does}

当您在UI步骤或示例中提及触发,条件,或动作时,使用UI显示的名称.

对于不与品牌,产品,或服务捆绑的通用集成,如`fan`,`vacuum`,`media_player`,或`climate`,不要在名称前加上集成:

- 不错: `**Action**: Turn on fan`
- 错误: `**Action**: Fan: Turn on fan`

对于与品牌,产品或服务挂钩的集成,将集成名称放在首位. 除了同名的通用项目之外,

- 不错: `**Action**: Jellyfin: Play media`

### 选项  ui 块 {#the-optionsui-block}

`options_ui` 块列出UI 显示的触发、平等权利或动作选项 。 使用UI的标签作为密钥.

- 每个选项需要 `description` 。 建筑没有一座就失败了.
- `required` 是可选的, 并接受`true` 或`false` 。 设定时,该选项显示**必须**或**可选**标签。
- 没有`type`。 UI为读者处理.

### 选项  yaml 块 {#the-optionsyaml-block}

`options_yaml` 块将选项列表为 YAML 密钥 。 它遵循与[块 `configuration`](/writing/reference/integration-page#the-configuration-block)相同的规则:

- 每个选项需要 `description` 和 `type` 。
- 将 `required` 设定为 `true` 或 `false` 。 不需要默认选项 。
- 如果有, 请记录 `default` 。
- 如果接受的法律地位不止一种,请列出它们,如`type: [string, integer]`。

## 可重复使用的文本 {#reusable-text}

一些文本在许多整合页面上是相同的. 与其再写,请从 [`source/_includes/integrations/`](https://github.com/home-assistant/home-assistant.io/tree/current/source/_includes/integrations) 加入它 。 [目录](/writing/reference/liquid)页解释包含和其他标记。

### 配置 {#configuration}

标准配置文本增加了 ** 配置 ** 标题, 一个启动设置的 My 按钮, 以及当按钮不起作用时的手动步骤 :

```liquid
{% include integrations/config_flow.md %}
```

文本适应页面:

- 如果发现密钥之一设置在 [现在我先说](/writing/reference/front-matter#discovery) 中, 它告诉读者 Home Assistant 可以自己找到设备 。
- 对于帮助者,台阶通过**帮助者**标签.
- 添加 `name="..."` 以使用与页面标题不同的名称, 或 `domain="..."` 启动另一个域的设置 。

对于整合的选项,匹配弄清的文本增加了一个**选项**标题,并解释了如何打开这些选项:

```liquid
{% include integrations/option_flow.md %}
```

### 其他片断 {#other-snippets}

- `integrations/building_block_integration.md`:解释集成的注释是一个构件,其他集成使用和读者不能加入.
- `integrations/remove_device_service.md`:删除整合实例的标准步骤。
- `integrations/serial_connected.md`:解释设备需要串行连接,直接或通过串行代理.
- `integrations/infrared_controlled.md`和`integrations/radio_frequency_controlled.md`: 解释整合需要一个已经设置的红外或无线电频率适配器.
- `integrations/restart_ha_after_config_inclusion.md`:对于YAML集成,请告诉读者在更改`configuration.yaml`后重新启动Home Assistant.

请在 [`source/_includes/integrations/`](https://github.com/home-assistant/home-assistant.io/tree/current/source/_includes/integrations) 中查找每个文本的当前文本 。

## 配置  基本块 {#the-configurationbasic-block}

使用 你想用 `configuration_basic` 块来解释设置窗体的字段, 或者从 UI 设置的集成选项 。 使用 UI 的标签作为密钥 :

```liquid
{% configuration_basic %}
Host:
  description: "The IP address or hostname of your bridge. For example,
    `192.168.1.100`. You can find it in the app, under **Bridge settings**
    > **Local API**."
Local access token:
  description: "The local access token of your bridge. You can find it in
    the app, under **Bridge settings** > **Local API**."
{% endconfiguration_basic %}
```

每个字段只需要 `description`, 这是需要的 。 没有`required`或`type`。 UI已经说清楚了

## 配置块 {#the-configuration-block}

使用 `configuration` 块来记录在 YAML 中设置的集成变量 。 它紧接着`configuration.yaml`的例子:

```liquid
{% configuration %}
api_key:
  description: The API key of your account.
  required: true
  type: string
name:
  description: The name of the sensor in Home Assistant.
  required: false
  type: string
  default: Awesome sensor
monitored_conditions:
  description: The conditions to create sensors for.
  required: true
  type: list
  keys:
    temperature:
      description: The current temperature.
    humidity:
      description: The current humidity.
{% endconfiguration %}
```

栈键 :

- `description`:变量会做什么。 要求。 马克唐在这里工作。
- `required`: 必需。 `true` 将变量显示为 ** required **, `false` 显示为 ** optional **。 不需要默认值的变量,所以设置为`false`. 您也可以使用 `inclusive` 或 `exclusive` 对必须一起使用的变量, 或不能合并的变量 。
- `type`:变量接受的值类型。 需要, 除非变量在 `list` 或 `template` 下嵌入 。 使用以下类型之一。 如果接受一个以上类型,请列出: `type: [string, integer]`.
- `default`:默认值,如果有的话。 `boolean` 类型的可选变量需要。
- `keys`:类型`map`或`list`的变量的嵌入变量。 筑巢变量采用相同的键. 请参看[模板集成](https://www.home-assistant.io/integrations/template/)页的一个大例子。

公认类型:

- `action`
- `any`
- `boolean`
- `date`
- `datetime`
- `device_class`
- `float`
- `icon`
- `integer`
- `list`
- `map`
- `selector`
- `string`
- `template`
- `time`
- `timedelta`

大楼检查这些规则。 缺少我来描述, 未知类型, `required` 值, 或没有默认的可选布尔值 , 使站点停止建设, 错误的变量命名 。

## 图像、图标和标志 {#images-icons-and-logos}

### 图标和标志 {#icon-and-logo}

一个集成的图标和标志来自[品牌存储器](https://github.com/home-assistant/brands). 您不会在文档中添加任何内容 。 页面通过集成域来拾取它们.

- 在品牌仓库中打开一个pull request,将图像添加到`core_integrations/<domain>/`. 在 ** 此 PR 下列出与 pull request 核心 pull request 和 核心 pull request 在同一行的品牌 pull request 一起 。
- 至少添加一个 `icon.png` 。 A `logo.png`,用于暗背景的版本,以及高清的`@2x`版本都是欢迎的. [品牌读取](https://github.com/home-assistant/brands/blob/master/README.md) 列出了确切的大小和要求 。
- 如果集成开始为自定义集成,现在是Home Assistant的一部分,则将其图像从`custom_integrations`移动到`core_integrations`.

### 其他图像 {#other-images}

将截图和其他图像存储在文档存储库中, 保存在您的整合文件夹中 :

- 整合页面的图像在 `source/images/integrations/<domain>/` 中。
- 博客文章的图像在 [`source/images/blog/`](https://github.com/home-assistant/home-assistant.io/tree/current/source/images/blog) 中 。

[图像和录像](/writing/reference/images) 覆盖如何拍摄好的截图并写备选案文 。
