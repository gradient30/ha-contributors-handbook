---
title: 我们如何设计
description: 在设计工作发生的地方,一个想法如何成为Home Assistant的一部分,谁决定,以及研究如何塑造它.
order: 2
---

# 我们如何设计 {#how-we-design}

设计 Home Assistant 发生在开放。 提案、反馈、研究和决定都是公开的,任何人都可以加入:设计者、研究人员、作家、无障碍专家和开发者。 这页显示了这种情况的发生地, 以及一个想法是如何从最初的想法 传到人们每天使用的东西。

## 在设计时 {#where-design-happens}

### UX设计讨论 {#ux-design-discussions}

[Open Home Foundation](/glossary/open-home-foundation)的[UX 设计仓库](https://github.com/OpenHomeFoundation/ux-design)是设计工作的家园,为Home Assistant和基金会的其他项目. 其[讨论情况](https://github.com/OpenHomeFoundation/ux-design/discussions)是分享、审查和决定提案的地方。 选择适合您拥有的类别:

- ** 构想**:在具体设计之前,先有早期想法、问题和可能的改进。
- ** 设计审查**:需要反馈的设计或进行中的工作。
- **设计系统**:共享组件、模式、符号和准则。
- ** 无障碍**:包容性设计、无障碍问题和改进。
- ** UX 研究和见解**:用户研究、可用性发现、分析和其他用于设计决定的证据。
- ** UX战略和远景**:整个基金会的长期经验方向。

[项目板](https://github.com/orgs/OpenHomeFoundation/projects/7) 列出正在运行和计划中的设计任务 。

### Discord {#discord}

[设计人员**](https://discord.com/channels/330944238910963714/1463606665311158284) [Home Assistant Discord](https://www.home-assistant.io/join-chat-design) 上的频道用于快速提问和早期反馈 。 产品和UX讨论发生在[产品和工具**](https://discord.com/channels/330944238910963714/1475553148847526123). 看不到频道吗? 在 **Channels & 角色** 下选择合适的角色.

### 图片 {#figma}

是否会在 Figma Community 上的 [设计套件](https://www.figma.com/community/file/1697311104929761103/home-assistant-design-kit) 是 Home Assistant 界面的官方 Figma 库, 由 Open Home Foundation 维护 。 它的变量,文本样式,以及组件都是由[前端](https://github.com/home-assistant/frontend)源生成的,所以你设计什么与哪些船相匹配. 它包括轻黑模式,此领域记录的[组件](/design/components),以及每个文件与文档和源链接的用法指南。 从它开始的口袋 靠近可以建造的东西

### 前端仓库 {#the-frontend-repository}

[前端仓库](https://github.com/home-assistant/frontend)是设计变成代码的地方。 界面中的具体问题是那里的问题,有[`UX`](https://github.com/home-assistant/frontend/labels/UX)或[`Accessibility`](https://github.com/home-assistant/frontend/labels/Accessibility)标签. 拉动需要设计团队输入的请求获得[`Needs UX`](https://github.com/home-assistant/frontend/labels/Needs%20UX)标签.

## 从想法到执行 {#from-idea-to-implementation}

设计工作遵循这些步骤:

1. 页:1 有人注意到一个问题或有一个想法。 在 ** 定义 ** 类别中开始,或检查项目板,以确定已经规划的任务。
2. ** 讨论。 ** 这个想法在公开场合讨论,得到他人的反馈和研究.
3. ** 建议。 ** 混凝土设计,带有模型或原型. 在**设计审查**中分享,提前,并征求反馈意见。 你不需要一个完整的设计开始。
4. ** 审查。 ** 设计者,开发者,以及用户对提议的反应,它根据他们说的话而改变.
5. ** 决定。 ** 方向已定. 主要决定摘要与属于理事会的项目相联系。
6. ** 执行。 ** 设计是构建的,通常位于前端,并更新了这个区域的匹配页面. 讨论链接到执行它的pull requests。

在设计新项目之前, 请检查 [组件](/design/components) 和 [模式](/design/patterns) 。 一致性是良好设计的一部分.

## 写建议 {#write-a-proposal}

** 设计审查** 类别中的建议通常遵循同样的提纲。 从这里开始 :

```markdown
## Problem {#problem}

Who runs into it, when, and why it matters.

## Proposal {#proposal}

What you propose. Add mockups, a prototype, or a short video.
Explain the choices you made.

## Open questions {#open-questions}

What you are unsure about, and want feedback on.

## Related {#related}

The board item, related discussions, and issues.
```

领头解决问题. 一个明显的问题使讨论重点突出,往往使解决办法变得明显。 如果有的话, 将您的讨论与它所属的董事会项目联系起来 。

## 谁决定 {#who-decides}

在UX设计讨论中审查提案,这是确定设计方向的地方。 报告概述了主要决定,并将其与属于理事会的项目联系起来。

对于代码,由前端审查员决定. 一种能保持既定经验的固定装置通常会留在他们身上。 新牌,徽章,屏幕,或交互模式,是设计决定,与代码更改一样多. 当其方向尚未确定时,一个审查者会添加{H不错}标签,并要求设计团队投入. 在写代码之前讨论一个更大的想法可以保存重写. 请参看[审查和发布](/frontend/development/review-and-release) 前端审查如何工作 。

### 在指定某个组件时 {#where-a-component-is-specified}

这个站点上的设计区域是设计指导的参考:[组件](/design/components)的外观和行为,何时使用,它们的规格,以及它们的可访问性. [基础](/design/foundations)、[模式](/design/patterns)和[品牌](/brand)也一样。 这个区域取代了设计. home-assistant.io.

更改一个组件:

1. 从** 设计系统** 类别开始讨论,确定方向。
2. 在 [前端仓库](https://github.com/home-assistant/frontend) 中打开 pull request 以更改组件 。
3. 打开 pull request 到 [这个网站](https://github.com/home-assistant/contributors.home-assistant.io) 更新组件页面 。

找到一个不再匹配组件的页面吗 ? 其中一个需要解决。 在此网站上打开一个问题或 pull request , 或者在您不确定哪个问题正确时开始讨论 。

## 研究 {#research}

研究将设计决策建立在人们实际做的基础之上,而不是基于人们建筑Home Assistant的假设. Open Home Foundation的[用户研究库](https://github.com/OpenHomeFoundation/user-research)是该作品的家,也向社区研究者开放。

### 方法 {#methods}

- ** 用户测试。 ** 在配置菜单重组为**Settings**之前,一个用Figma制作的原型机在网上测试了十天,有六个问题和三个任务. 任何人都可以加入, 915人参加,留下407条评论. 结论包括增加一个搜索栏,并将**图**改为**安排**。
- ** 调查。 ** 2024年的社区调查有超过8600份答复. 匿名数据集和问题发布为[打开数据](https://github.com/OpenHomeFoundation/user-research/tree/main/community-survey24),在CC BY 4.0下,供任何人使用.
- ** 研究报告。 ** 该存放处还进行隐私研究,并附有纸张和海报。

研究出现在产品中. 例如,研究不断显示,人们打开仪表板编辑器时会想到一个设备或实体,而不是一种卡片. 这就是为什么添加卡片的对话框现在从您的设备和实体开始 。

### 参加 {#taking-part}

基金会要求社区参与研究,比如在提示[博客](https://www.home-assistant.io/blog/2024/12/16/community-survey-2024/)上宣布的社区调查,以及论坛和社交媒体共享的用户测试. 与参与者的研究遵循了Open Home Foundation的[用户研究协议](https://www.openhomefoundation.org/user-research-agreement/).

想自己去研究还是分析? 分享你的计划或结论, 要与从事用户研究的人交谈,请加入[用户-研究人员**](https://discord.com/channels/330944238910963714/1518940566576959618)在[Home Assistant Discord](https://www.home-assistant.io/join-chat/)上.

## 我们为谁设计 {#who-we-design-for}

每个设计决定都考虑[三类用户](/design/users):超越其他智能家庭平台的人提出建议,
