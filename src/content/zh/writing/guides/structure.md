---
title: 组织页面结构
description: 围绕读者想要知道或做的事情组织文档,包括概念,任务,参考,教程,以及解决问题.
order: 1
---

# 结构 a 页 {#structure-a-page}

每个读者都会带一个问题来 这是什么? 我该怎么安排? 这个设置有什么用? 为什么它不起作用? 围绕这些问题,而不是如何构建一个特征,组织好文件。

这种做法被称为基于专题的作者。 一个话题回答了一个主要问题。 可以是踌躇整页,也可以是单页的一节. 您不需要踌躇于每个话题的单独页面 。

集成,触发,条件,和动作页都有自己的固定结构,所以它们都以同样的方式阅读. 对于这些,请从 [综合文件](/writing/guides/integration) 和 [整合页面](/writing/reference/integration-page) 引用开始 。 然后,本页的指南适用于每一节。

## 从概览开始 {#start-with-the-overview}

璞以简短的lice导打开每一页:页面的内容,以及它为谁服务. 然后从基础工作到更复杂的工作. 读者最需要的资讯首先出现, 将更长的页面分解成有清晰标题的章节,这样读者就可以跳到他们来找的部分.

## 先把UI放进去 {#put-the-ui-first}

当在 Home Assistant 界面中可以做一些事情时, UI 是标准的方法, 你先描述它. 每一类主题都是如此:任务、参考、辅导和解决问题。

在YAML和命令行选项得到支持和有用的情况下,欢迎它们。 让他们听从UI的指示, 在他们自己的标题下, 并解释什么时候有人需要他们。 不要建议当UI可以完成任务时,编辑文件是设置的正常部分.

## 每节一个目的 {#one-purpose-per-section}

文档中最常见的问题是一节试图同时做一切事情:解释概念,走过步骤,列出每个选项. 然后读者必须挖掘他们需要的部分。

给每个目的自己的方向。 例如,关于各领域的网页可以包含三个专题:

```markdown
## Areas {#areas}
<!-- Concept: what an area is, and why you would use one. -->

## Creating an area {#creating-an-area}
<!-- Task: the steps to create one. -->

## Area settings {#area-settings}
<!-- Reference: every setting, and what it means. -->
```

将每个专题集中在一个专题或目标上:

- 一个概念解释了一个想法。
- 一个任务涉及一个目标。
- 参考文献描述了一组相关事实或选项。
- 一个故障解答话题处理一个问题。
- 一个教程可以结合几个任务,只要它们服务于一个学习目标.

当您注意到您正在描述第二个任务时, 请给出它自己的话题 。 如果创建一个区域首先需要创建一个楼层,则楼层步骤会获得自己的部分,在同一页或另一页上. 从区域步骤链接到它。 直接促进任务成果的步骤要团结一致。

并非每一句上下文都需要自己的一节. 一个简短的导言,一个先决条件,或一行解释为什么一个步骤很重要,就在该步骤旁边。 较长的背景和完整的选项列表是您要搬出的内容 。

父标题可以将多个主题分组到子标题下. 故障排除部分可以将每个问题的详细块分组. 只要保留每个标题下的文本 关于该标题的承诺。

## 选择主题类型 {#choose-a-topic-type}

选择读者需要的类型 :

- [概念](/writing/guides/structure#concept):了解什么是东西,为什么它很重要,或者它是如何工作的.
- [任务](/writing/guides/structure#task):完成一个特定目标。
- [参考](/writing/guides/structure#reference) : 查找一个事实、 设置、 值或行为 。
- [教学](/writing/guides/structure#tutorial):学习通过遵循一个导引练习,以一些能起作用的东西结束.
- [解决问题](/writing/guides/structure#troubleshooting): 认清一个问题并修好它。

主体不决定类型. 领域可以是概念、任务和参考的主题,如上文的例子。 UI和YAML既不是类型:它们是完成任务的两种方式,也不是描述配置的两种方式.

## 概念 {#concept}

一个概念解释什么是事物,帮助读者理解它. 用于定义,事物如何相互关联,设计选择,以及使用一个特征的理由.

### 概念标题 {#headings-for-concepts}

- 使用名词或描述词:"区域","自动化的部分",或"Wake word processing".
- 一个问题,当它说 读者想要更清楚地知道什么: "什么是数据投票?"
- 当您可以指定主题时, 避免“ 导言” 或“ 概览 ” 。

### 概念的内容 {#content-for-concepts}

始明释义. 增加一个具体的例子,并解释关系或权衡。 定义不熟悉的术语,或与其定义的链接,例如使用 [单词](/writing/reference/liquid#glossary-tooltips) 。

```markdown
## Areas {#areas-1}

An area groups devices and entities that belong to a room or another part of your home. For example, a living room area lets you target all the lights in that room with one action.
```

保持设置指令脱离概念, 并链接到任务中 。 一个将选项列表或一长串的UI步骤变成一个概念已不再是一个概念:将选项放到一个参考话题中,并与它链接.

## 任务 {#task}

一项任务帮助读者达到特定的目标. 读者希望有所成就,而不是通过课来工作.

### 任务标题 {#headings-for-tasks}

- 命名动作及其对象:"创建一个区域",而不是"任务".
- `-ing` 短语, 如“ 创建区域” 或“ 更新 Home Assistant ”, 匹配大多数现有页面使用的内容 。
- 一个必修课对于一个较长的程序的阶段来说是很好的:"将图像写到您的SD卡上". 命令重要时,请注明阶段。
- 保持兄弟标题平行 。 如果一个动词以 `-ing` 开头, 他们都一样.
- 避免诸如"Usage","Configation"等模糊标题,或当任务有更具体的结果时,避免"与区域合作".

### 任务内容 {#content-for-tasks}

1. 如果标题没有明确,请在几句话中说明你何时或为什么这样做,并链接到相关信息。
2. 在 `Prerequisites:` 引导下, 直接列出步骤前的前提条件, 如硬件、 权限或必须先完成的设置 。 仅在要求适用于整页时使用单独的 `

## Prerequisites` 一节 。 没有值得提及的先决条件? 把名单放出去 {#creating-an-area-1}
3. 将台阶写成编号列表。 每一步从指示开始. 将解释或预期结果放在下面。
4. 以结果结束,并在有用时,用一个方法检查它是否奏效。

```markdown
## Creating an area {#reference}

1. Go to {% my areas title="**Settings** > **Areas, labels & zones**" %} and select **Create area**.
2. Enter a **Name** for the area.
3. Select **Create**.
   - Result: The new area appears in the list.
```

将步骤集中在目标上。 长篇解释和对每个字段的描述,以及其它程序属于别处. 与概念或参考链接。

## 参考 {#headings-for-references}

参考文献中包含读者查阅的事实,没有遵循程序。 用于设置,支持的值,语法,响应数据,以及其他定义的行为.

### 参考文献标题 {#content-for-references}

- 命名信息:"地区设置","蓝印输入",或"响应数据".
- 当内容有更具体的主题时,可避免"重要信息"或"好知"等囊括所有标题.

### 参考内容 {#area-settings-1}

- ** 每个条目使用相同的结构。 ** 对于设置,给出名称,它做什么,被接受的值,以及那些应用的默认值.
- ** 明确要求和可选择性。 **
- ** 使用阅读器所看到的名称。 ** UI 设置的 UI 标签, YAML 选项的精确密钥 。
- ** 在适用的设置旁边保留限制,** 不再列在单独的清单中。
- ** 方便扫描。 ** 使用列表,或[整合页面](/writing/reference/integration-page)中描述的配置块. 避免表格,见[样式指南承担起](/writing/reference/style#tables)。

```markdown
## Area settings {#tutorial}

- **Name**: The name of the area. Required.
- **Alias**: Another name a voice assistant can use for the area.
```

一个简短的例子可以显示一个有效的值或正确的语法. 不要让它长成一个教程, 不要在字段描述中隐藏设置步骤 。

## 教学 {#headings-for-tutorials}

教程通过指导性例子传授技能. 最后,读者有作品,可以保留或适应.

与任务的差异在于目的,而非难度. 一项任务帮助读者完成自己的作品. 教育课程让他们可以学习。 简单的程序不是自动的教程,教程可以教一些复杂的东西.

### 教学指导 {#content-for-tutorials}

- 开始标题为"Tutorial:",之后是动作和结果:"Tutorial:创建你的第一个自动化".
- 以读者在其中所做的事命名每个阶段,使用一致的措辞.
- 命令重要时,请注明阶段。

### 自由地进行教学好几年。 {#what-you-will-build}

说明读者将建立和学习什么,以及他们在开始前需要什么. 然后引导他们走一条道路,各行各业, 沿途显示预期结果,最后进行最后检查。

```markdown
## What you will build {#prerequisites}
<!-- An automation that turns on a light before sunset. -->

## Prerequisites {#step-1-create-the-automation}

## Step 1: Create the automation {#step-2-add-the-sunset-trigger}

## Step 2: Add the sunset trigger {#step-3-add-the-light-action}

## Step 3: Add the light action {#step-4-save-and-test-the-automation}

## Step 4: Save and test the automation {#next-steps}

## Next steps {#troubleshooting}
```

- 让解释贴近他们帮助的步骤。
- 与概念和参考资料相联系,而不是打断与这些概念和参考资料的工作。
- 沿途不要显示任何可选或可选的特性 。 在主演练后加上扩展,例如放在"下一步"下.
- 代码示例集不是一个教程. 通过学习经验指导读者。

## 故障排除 {#where-troubleshooting-goes}

一个排除麻烦的话题帮助读者识别出一个问题并从中恢复过来.

### 解决问题的地方 {#headings-for-troubleshooting}

将一个页面的故障排除在一个地方,所以读者知道当事情出错时该往哪里看:

- 参与了页面的一节:将问题放在`

## Troubleshooting`的一节中,放在页面的末尾. 在集成页面上,该部分在[区域顺序](/writing/reference/integration-page#sections)中被取代. {#content-for-troubleshooting}
- 在自己的页面上:当一个特性有许多问题时,将其移动到单独的故障排除页面. 从功能的页面链接到它.

不要将故障排除放在它相关页面的部分旁边, 就像一个故障排除小节在一个特性或设置下。
将问题放在页面的故障排除部分。
当它有所帮助时,链接到它相关页面部分的故障排除部分.

### 清除故障的方向 {#troubleshooting-1}

- 将每个问题放入自己的[可折叠的细节块](/writing/reference/liquid#collapsible-details).
- 使用症状或准确错误消息作为块的标题,如`Can't access Home Assistant in my browser`或`Stuck at "Preparing Home Assistant"`.
- 对于单独的故障解析页面,使用"故障解析"之后的题材:"故障解析Assist".
- 避免标题只有知道原因才有意义。 读者寻找所见所见,而非所错.

### 排除故障的内容 {#symptom}

每个区块内使用相同的三部分:

1. ** 音节:** 读者所见,以其语. 如果有, 包含准确的错误消息 。
2. ** 描述:** 正在发生什么,如果有帮助。 不要以肯定的方式提出 可能的原因。
3. ** 决议:** 怎么办。 把简单的检查放在更多参与的检查之前,解释一个动作在读者采取之前会做什么,并告诉他们如何确认问题已经消失.

在不增加任何内容时,如对一个非常简短的专题的描述,略去一部分。 页面上是这样看的:

```liquid
## Troubleshooting {#description}

{% details "The device shows as unavailable" %}

### Symptom {#resolution}

All entities of the device show as unavailable.

#### Description {#description}

Home Assistant can't reach the device on your network. This often happens when the device gets a new IP address from your router.

#### Resolution {#resolution}

1. Check that the device is powered on and connected to your network.
2. Give the device a fixed IP address in your router.
3. Go to {% my integrations title="**Settings** > **Devices & services**" %}, select the integration, and reload it.

The entities become available again within a minute.

{% enddetails %}
```

如果检查不能解决问题,链接到合适的帮助地点,并说要包含什么信息,如日志或诊断. 与社区论坛本身的联系并不是解决问题。

在任务主题中保持正常设置步骤. 如果一个设置步骤错过,就可以解释这个问题,就把这项工作联系起来,而不是重复。
