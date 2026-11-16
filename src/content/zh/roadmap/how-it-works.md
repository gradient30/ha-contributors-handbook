---
title: 从构想到发布
description: How larger work on Home Assistant is planned in the open, from a feature request to a roadmap opportunity, an epic, tasks, and pull requests, and where you can join in along the way.
order: 2
sidebarLabel: 它是如何运作的
sidebarLabel: 工作原理

---

# 从思想到释放 46. {#from-idea-to-release}

关于Home Assistant的大量工作完全不需要计划. 错误修正、 整合的改进或新的整合为 [准备就绪](/core/integrations/create#does-it-belong-in-core) : 您打开 pull request, 就这样 。 覆盖这条路。

更大的工作是不同的。 当某物跨越多个寄存器时,需要设计,或改变Home Assistant的构建方式,则[Open Home Foundation](/glossary/open-home-foundation)按层进行规划,在GitHub上的公有寄存器. 这页走过这些层层, 显示每个层的住址, 以及你可以跟随或加入的地方。 最后,一个真正的作品从第一个特性请求追溯到发货的发行.

## 层层一览 {#the-layers-at-a-glance}

图表. 从上到下:每层被细分为下面的一层. 在 GitHub 上, 机会,史诗和任务作为子问题链接, 这样您就可以上下跟踪链接 。

- 目标:基金会希望去的地方
  - [目标](https://github.com/OpenHomeFoundation/goals): 由棋盘设定
- 机会:值得解决的问题
  - [特性请求](https://github.com/home-assistant/feature-requests/discussions):任何人的想法和投票
  - [路线图](https://github.com/OpenHomeFoundation/roadmap):机会,由产品团队塑造
- Epics: 一套工作,往往是一个机会的阶段
  - ZafatahL0]:交付品和完成标准
- 任务:一个存储库中的一件工作
  - [核心](https://github.com/home-assistant/core): Python和集成
  - [前端](https://github.com/home-assistant/frontend): 接口
  - [文档](https://github.com/home-assistant/home-assistant.io): Home Assistant.io
  - [任务](https://github.com/home-assistant/tasks):无处适合的工作
- 运输
  - [调用请求](/start/pull-requests) : 和其他审查一样
  - [发布](/releases/how-it-works):每个月

在这些层的旁边,而不是其中,坐着[结构](/roadmap/how-it-works#alongside-the-roadmap-architecture). 它守护着Home Assistant的构造, 对于一切进入, 无论它来自路线图与否。

## 目标 {#goals}

在顶部是Open Home Foundation的目标,在[目标存储器](https://github.com/OpenHomeFoundation/goals)中. 基金会的董事会设置了它们,它们定义了基金会想要去的地方. 例如[让提供财政帮助](https://github.com/OpenHomeFoundation/goals/issues/7)和[代理所有的东西](https://github.com/OpenHomeFoundation/goals/issues/4)。 董事会还维护这些目标,每个目标都与实现这些目标的路线图机会挂钩。

只有基金会成员写目标,但讨论是公开的:你可以对一个目标发表评论,分享你的观点.

## 特性请求 {#feature-requests}

大多数想法以 [特性请求](https://github.com/home-assistant/feature-requests/discussions) 开头 。 任何人都可以打开一个,对一个进行投票,或者参加讨论. 描述你想要解决的问题,而不仅仅是你所想的解决方案. 写一个很好的

基金会的产品小组定期审查大众要求和战略要求,并将其中一些要求转化为路线图机会。 投票数和深思熟虑的讨论数不胜数,但并不是每一项要求都使它出现在路线图上。

## 路线图机会 {#roadmap-opportunities}

Open Home Foundation的[路线图](https://github.com/OpenHomeFoundation/roadmap)涵盖Home Assistant,ESPHome,Music Assistant,以及基金会的其他项目. 它不是一个带有日期的特征清单。 这是一组[机会](/glossary/opportunity):值得解决的问题。 每个问题都与其所支持的目标有关。

机会可以作为一个粗略的想法开始,并随着时间的流逝而成型. 其议题有:

- ** 问题说明**:问题是什么,谁有,为什么重要
- **社区信号**:指向它的特性请求,讨论,或Discord线程
- ** 范围和界限**:何在,何在明确
- ** 前方解决方案**:其形状足以理解构建它的意义的解决方案
- ** 风险和未决问题**:尚不确定的是什么
- ** Appetite**:机会值得多少时间,大致是小、中或大。
- ** 执行问题**:与工作的联系,一旦核准
- ** 决定日志**:关键决定和段落,日期

巨大的机会可以少一些。 例如,[塑造一个家庭如何使用其聪明的家](https://github.com/OpenHomeFoundation/roadmap/issues/129) 持有几个更突出重点的。

** 只有基金会工作人员和经授权的捐助者才能创造机会。 任何其他人打开的问题自动关闭。 评论对每个人都开放,它们很重要:它们可以添加信号,质疑范围,或者改变解决方案,如[实例](/roadmap/how-it-works#example-better-sun-triggers)所示.

=============================================================================================================================================================================================================================================================== 公共资料库没有说明如何运作以及谁参与。

** 跟着来:** [路线图项目板](https://ohf.to/roadmap) 显示积极的机会及其进展, 您可以在 GitHub 上观看 [路线图存储器](https://github.com/OpenHomeFoundation/roadmap) 。 Home Assistant博客的[路线图类别](https://www.home-assistant.io/blog/categories/roadmap/)有更大的画面, 当工作船时,释放笔记经常将机会连接起来,就像[2026.6](https://www.home-assistant.io/blog/2026/06/03/release-20266/)关闭了将红外线变成双向平台的机会时那样.

Add.1 需要设计的工作需要通过基础的[UX设计讨论](https://github.com/OpenHomeFoundation/ux-design/discussions).Add 解释这条路

## 图片 {#epics}

刚好是一个 [史诗](/glossary/epic) , 是一个更大的工作体, 由几个任务组成, 往往跨越几个寄存器。 Epics live in the [史诗库](https://github.com/home-assistant/epics) (英语). 每个国家:

- 它提供的路线图机会
- 它解决的问题和它的目标结果
- 其可达到的目标
- 当它算做
- 上下文, 如特性请求、 设计文件, 或 Discord 频道随附

史诗是其机会的子问题. Epics 也可以互相屏蔽, GitHub 在问题的侧边栏显示 。

### 阶段 {#phases}

机会往往分阶段提供,每个阶段都有自己的史诗。 例如, [通过 UI 配置 HTTP 服务器](https://github.com/OpenHomeFoundation/roadmap/issues/47) 已有 [阶段 1, 端口默认驯化和 UI](https://github.com/home-assistant/epics/issues/48) , 已完成 [二级, URI 中的 SSL/ TLS 和双堆栈](https://github.com/home-assistant/epics/issues/118) 正在进行 。 第三阶段列在第二阶段,但还没有史诗。

以后的阶段可以是计划,而不是承诺。 [使 Home Assistant OS 更容易安装的阶段 3](https://github.com/home-assistant/epics/issues/135)的史诗本身如此说:它的范围是一个计划,而不是一个承诺,项目可能在各个阶段之间移动或被丢弃.

### 路线图以外的图片 {#epics-outside-the-roadmap}

不是每个史诗都来自机会 有些是跨越许多整合的清理,比如[用常见的 `OSError` 助手翻译文件系统错误](https://github.com/home-assistant/epics/issues/142). 他们解释正确的模式,列出需要修复的集成,并要求您在pull request中引用史诗. 如果您想要在 Home Assistant Core 中找到一个定义清晰的作品, 这些地方是寻找的好地方 。

** 家庭援助组织成员创作史诗。 任何其他人打开的问题自动关闭。 阅读和跟踪它们是向所有人开放的。

## 任务 {#tasks}

一个任务是一个单个寄存器中比较小的作品. 它属于**任务**类型,在工作发生地的寄存器中:Home Assistant Core,前端,文档,Supervisor,或任何其他. 每项任务都是其史诗的子问题,因此史诗表明工作进展有多远.

不符合任何寄存器的工作到 [任务存储器](https://github.com/home-assistant/tasks) 。 只有家庭援助组织的成员才在那里讨论问题。

** 参加者:** 不是每个人都可以参加一项任务。 在大多数寄存器中,一个工作流程检查了每个新发行的**任务**类型:如果你不是GitHub上的家庭辅助组织的成员,它用`auto-closed`标签和一条评论来结束这个问题,该评论将你指向错误报告表和特征请求. Home Assistant Core还有Home Assistant。 io还接受存储器`CODEOWNERS`文件中列出的任何人的任务,比如集成所有者. 一旦一个任务存在,这是一个普通的问题:你可以评论,提问,或者主动提供帮助. 想做一个吗? 在你开始之前说这个任务, 所以没有人做同样的工作两次。

## 调用请求 {#pull-requests}

作品本身发生在pull requests,就像任何其他贡献一样. 将描述中的任务, 例如 `fixes #12345` 连接起来, 因此任务在 pull request 合并时会关闭 。 新功能的文档转到 `next` Home Assistant. io 的分支, 所以它和发布一起运行。 复检与其它pull request相同:参见[pull request和审查](/start/pull-requests).

** 谁参加:**每个人。 开放 pull request 和审查 pull request 对所有贡献者开放。

## 发布 {#release}

下一期月发行时合并工作船. 前一周,它位于β中,任何人都可以在自己的家中检测. tumour. [如何释放工作](/releases/how-it-works)解释周期,和[您的第一次发布贡献](/releases/first-contribution)显示如何加入β。

## 与路线图:结构 {#alongside-the-roadmap-architecture}

建筑会议守护Home Assistant的技术架构. 这不是路线图流动的一个步骤:它坐在那里,照顾技术。 对Home Assistant的构建方式的任何改变都需要它的认可,无论变化来自何处:机会,史诗,或者自己的pull request. 想想新的实体类型,改变实体模式,或者对实体组成部分提出新的触发和条件.

会议处理提案,即[架构存储器](https://github.com/home-assistant/architecture)中的讨论。

当路线图工作触及到建筑时,两个链接互相连接. 一个机会可以导致一个[结构讨论](https://github.com/home-assistant/architecture/discussions),它与它连接起来,作为推理生活的场所. 一个机会也可以建立在先有的架构讨论的基础上,比如[让 Home Assistant 发送无线电频率命令](https://github.com/OpenHomeFoundation/roadmap/issues/102)的机会.

提案在公开场合讨论,然后在会议上决定。 讨论结果张贴在讨论上,并标为答案:核准或否决,会议日期和任何意见,如会议想要的改变。 为整个项目制定持久规则的决定也被写成建筑决定记录。 [架构决策是如何做出的](/architecture/decisions)解释这个过程。

** 谁参加:** 任何人都可以开始讨论或加入讨论。

## 在那里你可以加入我们 {#where-you-can-join-in}

| 层 | 何处 | 你可以做点什么 |
| --- | --- | --- |
| 目标 | [Open Home Foundation/目标](https://github.com/OpenHomeFoundation/goals) | 阅读和评论 |
| 特性请求 | [特性请求](https://github.com/home-assistant/feature-requests/discussions) | 提议、表决和讨论 |
| 机会 | [Open Home Foundation/道路图](https://github.com/OpenHomeFoundation/roadmap) 和 [项目板](https://ohf.to/roadmap) 。 | 跟踪和评论 |
| 架构 | [结构讨论](https://github.com/home-assistant/architecture/discussions) | 开始讨论, 为什么不加入其中 |
| 设计 | [UX设计讨论](https://github.com/OpenHomeFoundation/ux-design/discussions) | 交流想法和反馈 |
| 图片 | [Home Assistant/医生](https://github.com/home-assistant/epics) | 跟着走,从清理史诗里拿工作 |
| 任务 | 能够在工作资料库中查阅 | 评论和主动提供帮助 |
| 调用请求 | 能够在工作资料库中查阅 | 打开和审查 pull request s |
| 发布 | 那个[贝塔](/releases/first-contribution) | 测试,并报告中断 |

## 实例: 更好的太阳触发器 {#example-better-sun-triggers}

这是一份从头到尾的作品 它使太阳[触发](/glossary/trigger)和[他们是条件](/glossary/condition)配合太阳的实际位置,而不是固定时间抵消日出和日落前后.

1. ** 长期请求。 ** 2026年3月,一个用户要求[我给你点颜色看看](https://github.com/home-assistant/feature-requests/discussions/3043),在日出和日落旁边.
2. ** 机会。 ** 2026年4月,机会[改善太阳触发器和条件](https://github.com/OpenHomeFoundation/roadmap/issues/96)开启,以这个请求作为其社区信号. 它描述了这个问题(一个抵消,即春季的黄昏比赛在冬季是错误的,在北极圈上方是无用的),根据太阳的升降提出了一整套触发器和条件,并设定了小小的食欲. 在评论中,社区成员增加了信号,并质疑将时间抵消排除在外的选择。
3. ** 建筑。 ** 一名维护者指出,实体组成部分的新触发因素和条件需要架构批准。 因此[结构讨论](https://github.com/home-assistant/architecture/discussions/1394)于2026年5月开放,连接回机会. 建筑会议首先要求修改,比如一个带有类型选项的黎明触发器而不是三个独立的触发器. 2026年6月,它批准了修订后的提案.
4. ** 第一次发布。 ** 高优先级触发器和条件在 [核心编号174485](https://github.com/home-assistant/core/pull/174485) 和 [核心编号174537](https://github.com/home-assistant/core/pull/174537) 中构建,并在 [2026.7](https://www.home-assistant.io/blog/2026/07/01/release-20267/) 中发运.
5. ** 任务。 ** 2026年7月,在第一次发布后,史诗[改善太阳触发器和条件](https://github.com/home-assistant/epics/issues/112)在机会下面打开,任务在两个寄存库中:刚刚发运的作品[时间冲抵](https://github.com/home-assistant/core/issues/175828),[剩余触发因素和条件](https://github.com/home-assistant/core/issues/175830)和[文件](https://github.com/home-assistant/home-assistant.io/issues/46939).
6. ** Feedback改变计划。 ** 2026.7后,在Discord上的人和在机会的评论中要求时间抵消. 这需要它自己的[结构讨论](https://github.com/home-assistant/architecture/discussions/1430),在7月底的核心会议上得到批准。 [pull request](https://github.com/home-assistant/core/pull/176967)于次日合并,运至[2026.8](https://www.home-assistant.io/blog/2026/08/05/release-20268/).
7. ** 最后释放。 ** 黄金时段,蓝色时段,午夜太阳和极地夜晚在[核心编号180106](https://github.com/home-assistant/core/pull/180106)中出现,记录在[Home Assistant.io#47624](https://github.com/home-assistant/home-assistant.io/pull/47624)中,并在[2026.9](https://www.home-assistant.io/blog/2026/09/02/release-20269/#golden-hour-blue-hour-and-polar-sun-automations)中发运.
8. ** 已关闭。 ** 该史诗于2026年9月关闭,一周半后的机会. 一个后续任务 [基于太阳方位角的触发器和条件](https://github.com/home-assistant/core/issues/181914) 仍然开放 。

几事突出. 作品以约十几票的特写请求开始. 社区的评论改变了建起来的东西。 架构决定是在代码之前作出的,后来的修改需要自己的决定. 而真实的顺序比地层所显示的更混乱:这里,史诗是在第一部分已经发货之后打开的.

## 谁说话 {#who-to-talk-to}

- 机会还是史诗? 在评论中询问这个问题,因此从事这项工作的人们都看到了.
- 关于改变的结构的问题? 使用[结构讨论](https://github.com/home-assistant/architecture/discussions),或在[Discord](https://www.home-assistant.io/join-chat/)上的[发展中国家**](https://discord.com/channels/330944238910963714/554842238073700352)中询问。
- 不知你的想法属于哪里? 从[特性请求](https://github.com/home-assistant/feature-requests/discussions)开始.
