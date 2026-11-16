---
title: 市场
description: 与所有使用 Home Assistant 的人分享你所构建的内容。发布自定义集成、仪表板卡片、主题、模板宏和蓝图，并保持它们的更新。
---

# 市场 {#marketplace}

并不是人们为Home Assistant制作的所有内容都应该放在Home Assistant本身里。为某个特定设备制作的一张卡片、你最喜欢颜色的主题、只有少数人使用的服务集成、解决你家问题的自动化：这些都值得分享，而且成千上万的人都在分享。

分享是使Home Assistant成为Home Assistant的重要部分。有人为自己的墙面平板制作卡片并分享。另一个人将其用于家庭中，发现了一个错误并发送了修复。第三个人看到它，并获得了新的创意。你分享的内容会激发别人并帮助他们，而他们分享的内容同样也会帮助你。这就是社区：热爱Home Assistant的人，并乐于分享他们用它制作的内容。[市场](/glossary/marketplace) 是用户查找和安装该功能的地方。从 2026.11 版本开始，它内置在 Home Assistant 中，路径为 **设置** > **市场**。它起源于 [HACS](/glossary/hacs)，这是一个社区商店，多年来人们将其作为自定义集成进行安装，它使用相同的目录和相同的 `hacs.json` 文件。如今与 HACS 兼容的集成、卡片、主题或模板大多也能在市场中使用，尽管市场在安装前会检查一些事项更严格。AppDaemon 应用程序和 Python 脚本是例外：市场不处理它们。

市场也是新的集成或仪表板卡片的起点。在这里发布它，一旦它成熟并拥有用户基础，可以联系维护者，看看是否应该作为内置功能发布。请参阅 [它是否属于核心](/core/integrations/create#does-it-belong-in-core)。

## 你可以分享的内容 {#what-you-can-share}

| 内容 | 功能 | 分享途径 |
| --- | --- | --- |
| [自定义集成](/marketplace/guides/integrations) | 为设备或服务添加支持，如内置集成 | 市场 |
| [仪表板卡片或插件](/marketplace/guides/dashboard) | 向仪表板添加卡片、卡片功能、徽章或其他构建模块 | 市场 |
| [主题](/marketplace/guides/themes) | 改变界面的颜色和部分尺寸 | 市场 |
| [模板宏](/marketplace/guides/templates) | 可重用的 Jinja 宏，其他人可以导入到他们的模板中 | 市场 |
| [蓝图](/marketplace/guides/blueprints) | 自动化、脚本或模板实体，带有供他人填写的空白 | 导入链接，以及论坛上的 [蓝图交流](https://community.home-assistant.io/c/blueprints-exchange/53) |蓝图不在市场中。用户是从链接导入它们的，Home Assistant 会记住该链接以获取更新。它们在这里是因为共享它们的方式精神上是相同的：你发布，别人安装，你保持它的运行。

## 目标对象 {#who-this-is-for}

如果你为自己的 Home Assistant 创建了某些东西，并希望其他人也能使用它，这个区域适合你。你所需的内容取决于你分享的内容类型：

- 蓝图需要 YAML 文件和在你自己家中可运行的自动化。不需要编程。
- 主题需要 YAML 文件和对颜色的敏感。
- 卡片或其他仪表板插件需要 JavaScript。
- 集成需要 Python。

除蓝图外，每种类型的内容都存放在公共 GitHub 仓库中。你不需要成为 Git 专家，但需要有一个账户，并能够发布版本。

以这种方式分享的所有内容都是由你制作和维护的，而不是 Home Assistant 项目负责。在用户从 Marketplace 安装任何内容之前，会看到一条警告说明这一点。请准备好回答问题，并在 Home Assistant 发生变化时更新你的作品。

## 从这里开始 {#start-here}

1. [你的第一次贡献](/marketplace/first-contribution)：把你已经使用的自动化转化为蓝图，并分享它。
2. [它是如何工作的](/marketplace/how-it-works)：市场如何查找、检查、安装和更新你发布的内容，以及蓝图是如何共享和更新的。
3. 在下面选择适合你构建的指南。

## 指南 {#guides}

- [自定义集成](/marketplace/guides/integrations)：当你的集成存在于核心之外时，有哪些不同。
- [仪表板卡片和插件](/marketplace/guides/dashboard)：打包卡片、卡片功能或其他 JavaScript 模块。
- [主题](/marketplace/guides/themes)：结构、可设置的变量、明暗模式以及测试。
- [模板宏](/marketplace/guides/templates)：以模板文件分享 Jinja 宏。
- [蓝图](/marketplace/guides/blueprints)：编写、测试、版本控制并分享蓝图。
- [版本和更新](/marketplace/guides/releases)：用户如何获取你的新版本，以及如何保持其正常运行。
- [进入目录](/marketplace/guides/catalog)：将你的仓库添加到目录中，让所有人都能找到它。

## 参考资料 {#reference}

- [hacs.json](/marketplace/reference/hacs-json)：文件的每个键，以及市场如何处理它。
- [仓库结构](/marketplace/reference/repository-structure)：每种类型的文件放置位置。
- [验证检查](/marketplace/reference/validation)：HACS 操作检查的内容，以及市场拒绝安装的情况。

## 相关领域 {#related-areas}

- [核心与集成](/core/integrations)：如何构建集成，无论是自定义还是非自定义。
- [自定义卡片及更多](/frontend/custom-ui)：如何构建卡片、卡片功能、徽章、视图、策略和面板。
- [主题与设计令牌](/frontend/architecture/theming)：从前端角度来看，CSS 变量主题的更改。
- [安全](/security)：在运行于他人环境的代码中需要注意的事项。

## 与谁联系 {#who-to-talk-to}

- 在 [Home Assistant Discord](https://www.home-assistant.io/join-chat/) 上的 [**#developers**](https://discord.com/channels/330944238910963714/554842238073700352) 频道，是构建集成和卡片的人互相帮助的地方。看不到该频道？在 **Channels & Roles** 下，选择 **I want to contribute dev skills to Home Assistant**。
- 关于目录、`hacs.json` 或 HACS 操作的问题：请访问 [HACS Discord 服务器](https://discord.gg/apgchf8) 和 [hacs/integration](https://github.com/hacs/integration/issues) 的问题页面。
- 蓝图在社区论坛的 [Blueprint Exchange](https://community.home-assistant.io/c/blueprints-exchange/53) 上进行共享和讨论。
- 在市场本身发现了错误？请在 [核心仓库](https://github.com/home-assistant/core/issues) 中提交问题。
