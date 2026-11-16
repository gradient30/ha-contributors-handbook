---
title: 架构原则
description: Home Assistant 构建背后的理念。一旦你了解了它们，代码审查中的许多规则就不再令人惊讶。
order: 3
sidebarLabel: 原则
---


# 架构原则 {#architecture-principles}
Home Assistant 已经发展了十多年，有成千上万的贡献者。将它维系在一起的是一小套理念，它们无处不在：在代码中、在评审中，以及在 [架构仓库](/architecture/decisions) 中记录的决策中。

你不需要去记住它们。但当审查者要求你修改某些内容，而你又不明白原因时，答案几乎总是这些理念之一。

本页内容关于这些价值观对代码及其构建方式的意义。[我们的原则](/start/principles) 涉及整个项目的价值观及我们的协作方式。[设计原则](/design/principles) 涉及它们对界面的意义。

## 你的家，你的数据 {#your-home-your-data}
Home Assistant 在你家中运行，并且在可能的情况下无需互联网即可工作。关于你家中的数据会留在本地，除非你选择将其发送到其他地方。这也是 [Open Home Foundation](/glossary/open-home-foundation) 所代表的理念：隐私、选择和可持续性。

构建时的含义：

- 优先通过本地网络与设备通信，而不是通过制造商的云服务。[IoT 类](/glossary/iot-class) 的集成告诉用户他们得到的是哪一种。
- 未经用户知晓和选择，不向任何人发送数据。分析为用户选择加入。
- 对于基础功能，不依赖项目自身的服务。Home Assistant Link 是一个可选项，从非必须。

## 一个进程，一个事件循环 {#one-process-one-event-loop}
Home Assistant Core 是一个单一的 Python 进程。几乎所有东西都运行在一个 [事件循环](/core/internals/asyncio) 上：每一个集成、每一个自动化、每一个 API 请求。这让它足够轻量，能在小型计算机上运行，也保持快速，但前提是每个人都遵守规则。

这对于你的开发意味着：

- 永远不要阻塞事件循环。在没有 `await` 的情况下等待网络或磁盘会冻结整个系统，而不仅仅是你的集成。
- 只能阻塞的代码，例如没有异步支持的库，需要在工作线程中运行。

## 设备逻辑存在于库中 {#device-logic-lives-in-libraries}
一个集成在 Home Assistant 与设备或服务之间进行转换。知道如何与该设备、其协议和 API 进行通信的代码，存在于 PyPI 上的单独 Python 库中。集成将该库作为一个 [依赖](/glossary/requirement) 使用。

这可以让 Home Assistant Core 关于 Home Assistant。该库可以单独进行测试、发布和被其他项目使用，而集成保持足够小以便审查。

## 在用户界面中设置 {#set-up-in-the-ui}
用户在用户界面中将[集成](/glossary/integration)添加到他们的首页，而不是通过编辑 YAML。连接到设备或服务的集成通过[配置流程](/glossary/config-flow)进行设置。这在[ADR-0010](https://github.com/home-assistant/architecture/blob/master/adr/0010-integration-configuration.md)中已经确定。

YAML 仍然存在，用于自动化、模板以及一些不连接到任何设备的集成。但是，对于设备来说，用户界面是设置的方式。

## 一切都变成实体和动作 {#everything-becomes-entities-and-actions}
来自 Philips Hue 的灯和来自 IKEA 的灯在 Home Assistant 中看起来和行为方式相同。集成将设备的任何操作转换为具有状态的[实体](/glossary/entity)以及控制它们的动作。

这种共享模型使其他功能成为可能。仪表盘、自动化、语音和历史记录都可以与任何集成一起使用，因为它们只看到实体。当你构建一个集成时，你的任务是将设备融入该模型，而不是创建新的模型。

## 用户的选择优先 {#the-users-choices-win}
用户可以重命名实体，将设备放入不同区域，并隐藏他们不需要的内容。这些更改保存在[注册表](/architecture/core/registries)中，而不是在集成中，并且这些更改在重启和更新后仍然存在。

这就是为什么实体需要一个[唯一 ID](/glossary/unique-id)，以及为什么集成从不决定用户可以更改的内容，例如实体 ID。

## 小心更改 {#change-with-care}
数百万家庭在运行 Home Assistant，人们依赖它来控制灯光、采暖和警报。任何破坏他们设置的更改都会破坏他们的家庭。

- 旧的东西不会立即移除。它首先会被弃用，并附有警告和日期。参见[弃用](/glossary/deprecation)。
- 向后不兼容的更改很少，会有解释，并在发布说明中列出。
- [集成质量标准](/glossary/quality-scale)设定了什么是好的基准。

## 支持越少，支持得越好 {#support-less-support-it-well}
项目限制了其支持的内容，因此可以更好地支持这些内容。一些架构决策的示例：

- **安装方法**：Home Assistant OS 和 Home Assistant Container。不再支持自行安装 Core 或在自己的操作系统上安装 Supervisor。
- **Python**：一次仅支持 Python 的一个小版本，目标是支持最新版本 ([ADR-0020](https://github.com/home-assistant/architecture/blob/master/adr/0020-minimum-supported-python-version.md))。
- **数据库**：SQLite、未达到生命周期终点的 PostgreSQL 版本，以及未达到生命周期终点的 MariaDB 和 MySQL 的 LTS 版本 ([ADR-0018](https://github.com/home-assistant/architecture/blob/master/adr/0018-supported-databases.md))。
- **不再新增集成**，如抓取网站的集成 ([ADR-0004](https://github.com/home-assistant/architecture/blob/master/adr/0004-webscraping.md))，或直接与 GPIO 引脚交互的集成 ([ADR-0019](https://github.com/home-assistant/architecture/blob/master/adr/0019-GPIO.md))。它们太容易出错，或者无法对每个人提供支持。但仍可作为自定义集成存在。

## 处理这个 {#work-on-this}
- 在 [集成质量等级](/core/quality-scale) 中，逐条查看这些原则在集成中的应用。
- 不确定从哪里开始贡献？[你的第一次贡献](/start/first-contribution) 帮助你选择一个领域。
