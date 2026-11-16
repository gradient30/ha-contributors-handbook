---
title: 分析是如何运作的
description: 你的分析数据从安装到公共分析网站的路径，以及设备数据库如何融入其中。
order: 2
sidebarLabel: 它是如何运作的
---


# 分析是如何运作的 {#how-analytics-works}
Home Assistant 有两种方式与项目共享数据，都是选择加入的：分析，它会告诉项目有关安装的信息；设备数据库，它会告诉项目有关设备的信息。本页面跟踪数据从你的家到最终去向的全过程。

## 为什么项目需要数据 {#why-the-project-wants-numbers}
Home Assistant 无法看到它是如何使用的。这是故意为之，但这让一些决策变得困难。分析有助于三件事：

- **决定花时间的方向。** 了解哪些集成受欢迎可以帮助团队决定改进、重写或扩展哪些功能。
- **与制造商沟通。** “成千上万的 Home Assistant 用户拥有你的设备”比功能请求更能说服公司添加本地 API。这促使制造商增加了本地控制和隐私功能。
- **帮助用户选择。** 公共分析网站显示哪些集成和设备受欢迎。[home-assistant.io](https://www.home-assistant.io/) 上的集成页面显示每个集成的活跃安装数量，使用的都是相同的数据。

## 分析 {#analytics}
### 收集 {#collecting}
[分析集成](https://github.com/home-assistant/core/tree/dev/homeassistant/components/analytics) 是 Home Assistant 本身的一部分。启用分析后，它会在 Home Assistant 启动后等待 15 分钟，发送一份报告，然后在 Home Assistant 运行期间每 24 小时发送一次。

报告中的内容取决于你启用的选项。[分析分享的内容](/data/reference/analytics-data) 列出了每个字段。运行开发版本的安装会将其数据发送到单独的测试环境，因此不会与真实数据混合。

### 接收 {#receiving}
报告会发送到分析接收器，这是一个在 Cloudflare Workers 上运行的小程序。它会检查报告，根据 IP 地址添加报告来源的国家（以及美国的州），并将其存储在键值存储中，以安装的随机标识符为键。

每个安装只有一个条目。当报告与存储的内容不同或至少每 30 天（即使没有变化）会重写该条目。如果一个条目 60 天内没有被重写，它将被移除。

### 处理 {#processing}
计划任务会遍历存储的条目并计算总数：

| 任务 | 运行频率 | 功能 |
| --- | --- | --- |
| 处理队列 | 每分钟，直到完成 | 遍历所有条目并计数。完成后，网站会使用新数据重新构建。 |
| 更新历史 | 每小时 | 更新安装类型、版本和总数的历史记录。 |
| 重建网站 | 每小时，在xx:15 | 使用最新数据重建网站。 |
| 重置队列 | 每天一次，在午夜之后 | 开始新一轮处理。 |

### 发布 {#publishing}
[分析网站](https://analytics.home-assistant.io/) 已根据新的总数重新构建。它显示了随时间变化的安装情况、版本、安装类型、板子、集成、应用程序和统计数据。相同的数据也可以作为文件供任何人使用。请参阅 [使用公共数据](/data/guides/public-data)。

所有内容，包括接收、处理和网站，在 [analytics.home-assistant.io 仓库](https://github.com/home-assistant/analytics.home-assistant.io) 中都是开源的。

## 诊断 {#diagnostics}
诊断与其他功能不同。启用时，意外错误的崩溃报告会发送到 [Sentry](https://sentry.io/)，开发人员会使用这些报告来修复错误。这些报告只有开发人员可以看到。此选项目前覆盖 Supervisor 和操作系统代理。

## 设备数据库 {#the-device-database}
Open Home Foundation 正在构建一个设备数据库：一个开放的、由社区驱动的资源，展示智能家居设备在真实家庭中的表现。这个传感器能在没有云的情况下工作吗？这个插座提供哪些实体？答案来自那些选择共享其设备匿名数据的 Home Assistant 安装。

### 打开它 {#turning-it-on}
设备数据库是一个预览功能。要进行分享，请在 **设置** > **系统** > **实验室** 中打开 **设备数据库** 功能。这也会在 **设置** > **系统** > **分析** 中打开 **设备**，在那里你可以再次关闭分享。在同一位置，**预览设备分析** 会下载将要分享的内容。

### 共享的内容 {#what-is-shared}
每天一次，在每次安装时随机选定的时间，Home Assistant 会发送其设备的快照：

- 仅限随 Home Assistant 提供的集成设备，并且仅限用于设备和集线器的集成。自定义集成以及诸如天气服务提供商之类的服务不会被包括在内。
- 每个设备：制造商、型号、型号 ID、硬件和软件版本、是否有配置 URL，以及它通过哪个设备连接。
- 每个实体：其域、设备类别、实体类别、计量单位、是否使用实体名称，以及其状态是否为假定状态。

你的设备 ID 不会被发送。设备之间仅通过列表中的位置相互引用。你为设备、区域和实体命名的名称从不包括在内。一个集成可以省略其部分或所有设备和实体。请参阅 [你的集成中的分析](/data/guides/integration-analytics)。

### 它的位置 {#where-it-goes}
快照会存储到 Open Home Foundation 的设备数据库中，而不是分析接收器。数据如何处理在 [数据使用声明](https://www.openhomefoundation.org/device-database-data-use-statement) 中进行了描述。设备数据库的计划和进展会在博客中分享，首先是 [我们将如何共同构建设备数据库](https://www.home-assistant.io/blog/2026/02/02/about-device-database/)。
