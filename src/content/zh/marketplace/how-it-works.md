---
title: 市场是如何运作的
description: 市场如何找到你的仓库、检查它、安装它并保持其更新，以及蓝图如何在没有它的情况下被共享和更新。
sidebarLabel: 它是如何运作的
order: 2
---

# 市场是如何运作的 {#how-the-marketplace-works}

[/glossary/marketplace/] 市场是 Home Assistant Core、`marketplace` 的一项集成，在 **设置** > **市场** 下有一个面板。它随 Home Assistant 2026.11 版本发布，并已默认设置。此页面将你在 GitHub 仓库的工作与用户的 Home Assistant 对应，因此你可以知道它在这个过程中会发生什么。

市场是 [HACS](/glossary/hacs)，尽可能少修改地引入到 Home Assistant 中。[pull request 添加它的人](https://github.com/home-assistant/core/pull/183502) 也是这么说的，并表示进一步发展的想法将会在之后提出。以下内容描述了市场在核心中的现状。如果与 HACS 不同，本页面会说明。

## 目录 {#the-catalog}

市场显示目录中的内容。目录是按类型列出的GitHub 仓库列表，保存在 [hacs/default](https://github.com/hacs/default) 仓库中：集成文件一个，`plugin`（仪表板卡片和插件）一个，主题一个，模板一个。你可以通过在那里打开一个 pull request 将你的仓库加入其中：请参见 [加入目录](/marketplace/guides/catalog)。

目录作为 `data-v2.hacs.xyz` 的数据提供，这些数据也被 HACS 使用。它不仅包含列表：还包括每个仓库的最新版本、描述、星标，以及两个被移除仓库的列表：- **已移除**：该存储库不再提供，例如因为它已被弃用或归档。已安装的副本仍可使用，但不会收到更新，用户会收到说明原因的修复信息。
- **关键**：该存储库是有害的。市场会立即卸载它，并重启 Home Assistant。

市场在启动时读取目录，并且每隔 6 小时再次读取。

用户还可以添加目录中没有的存储库，通过 [链接](/marketplace/guides/catalog#the-link-to-your-repository)：自定义存储库。该操作需要 GitHub 连接，并且存储库必须满足与目录中的存储库相同的要求。市场会拒绝核心存储库以及包含应用程序的存储库。

## 类型 {#the-types}

Marketplace 知道四种类型。每种类型在用户配置文件夹中都有自己的文件夹：

| 类型 | 在目录中 | 安装到 | 安装后 |
| --- | --- | --- | --- |
| 集成 | `integration` | `custom_components/<domain>/` | 当有配置流程且之前未加载时，会立即加载。否则，修复会要求重启。 |
| 仪表板 | `plugin` | `www/community/<repository name>/` | 作为仪表板资源添加。用户需要重新加载浏览器。 |
| 主题 | `theme` | `themes/<theme file name>/` | 主题会被重新加载。 |
| 模板 | `template` | `custom_templates/` | 自定义模板会被重新加载。 |

HACS 还处理 AppDaemon 应用和 Python 脚本。Marketplace 不处理这些。已经安装的用户保留文件，但不会收到更新，修复会提示用户。

## 它检查的内容 {#what-it-checks}

Marketplace 会从仓库的根目录读取 `hacs.json`，用于安装的每一个版本。没有该文件，就无法安装或更新你的仓库。[hacs.json 参考](/marketplace/reference/hacs-json) 列出了所有键。

然后，它会在 [仓库结构](/marketplace/reference/repository-structure) 描述的位置查找你的类型的文件。如果文件不在那儿，则说明仓库不符合规范，无法安装。

在写入文件之后，但在调用安装完成之前，它会检查 Home Assistant 是否可以使用这些文件。当检查失败时，安装会失败，并且文件会恢复到原来的状态：- 一个集成需要一个具有相同 `domain` 的 `manifest.json`，以及加载器可以接受的 `version`。
- 主题文件必须是有效的 YAML，不能包含 `!include` 之类的标签，并通过与 `configuration.yaml` 中主题相同的验证。
- 模板文件必须为 UTF-8 编码，并且不大于 Home Assistant 读取量。
- 仪表板插件需要其 JavaScript 文件存在。

完整列表以及 HACS 操作的检查，可参考 [验证检查](/marketplace/reference/validation)。

## 版本 {#versions}

当你的仓库有 GitHub 发布时，用户获取的版本是最新发布的标签。预发布版本只提供给开启了仓库预发布开关的用户，并且仅在其比最新发布版本更新时有效。如果没有发布，用户将获取默认分支的最新提交。[发布指南](/marketplace/guides/releases) 有详细信息。

从目录安装的版本会直接从该版本的发布资源或存档中安装，而不通过 GitHub API，因此即使没有 GitHub 连接也能工作。其他版本和自定义仓库则通过 GitHub API 进行。

每个已安装的仓库都会获得一个 [更新实体](https://www.home-assistant.io/integrations/update/)，这样新版本就会显示在 **设置** > **更新** 下，与 Home Assistant 本身的更新一起。用户可以在此处阅读你的发布说明。

## 在 Home Assistant 2026.11 之前 {#before-home-assistant-202611}

在 Marketplace 推出之前，HACS 是用户自行安装的自定义集成。在更新后的首次启动时，Marketplace 会接管 HACS 安装：已安装的仓库、自定义仓库和更新实体会被保留，同时 HACS 会被移除。指向 `/hacs` 的链接会打开 Marketplace，仪表板文件仍可通过旧的 `/hacsfiles/` 路径访问。

对于你作为发布者来说，变化不大。目录、`hacs.json`、文件夹结构以及 [HACS 操作](https://github.com/hacs/action) 都保持不变。[我的 Home Assistant](/glossary/my-link) 类型为 `hacs_repository` 的链接仍然有效，并且会在 Marketplace 中打开你的仓库。新的类型是 `marketplace_repository`。

## 蓝图 {#blueprints}

[蓝图](/glossary/blueprint) 不在市场上。Home Assistant 可以从 URL 导入它们：

- [社区论坛](https://community.home-assistant.io/) 上的一个主题。Home Assistant 会从第一篇帖子的第一个 YAML 代码块中获取一个蓝图。
- GitHub 上的一个文件，或者 GitHub gist。
- home-assistant.io 上的 YAML 文件。
- 任何其他返回蓝图 YAML 的 URL。当 URL 不在 GitHub 或 Home Assistant 网站上时，导入对话框会警告用户。Home Assistant 将 URL 保存在蓝图中，就像 `source_url` 一样。该 URL 决定了更新的工作方式：用户选择 **重新导入蓝图**，Home Assistant 会再次从同一位置下载蓝图，并覆盖现有的副本。从此，基于该蓝图构建的自动化和脚本将使用新版本。没有更新实体，也不会有新版本存在的通知：用户是在听说有更新后才重新导入。 [蓝图指南](/marketplace/guides/blueprints) 解释了如何在不破坏已有构建的情况下更改蓝图。
