---
title: 发布与更新
description: 用户如何通过市场获取您的新版本，如何发布预发行版本，以及如何防止某个版本到达对它来说过旧的 Home Assistant
sidebarLabel: 发布与更新
order: 6
---

# 发布与更新 {#releases-and-updates}

市场的用户可以在 **设置** > **更新** 中获取您的更新，位于 Home Assistant 本身的更新旁边。每个已安装的存储库都有一个更新实体，其中包含您的发布说明。本页面解释了这些版本的来源，因此您可以控制用户获取的内容。

这适用于集成、仪表盘插件、主题和模板。Blueprints 没有发布版本：请参阅 [在不破坏 Blueprint 的情况下更改它](/marketplace/guides/blueprints#change-it-without-breaking-it)。

## 发布 GitHub 版本 {#publish-github-releases}

你的版本是你最新 GitHub 发布的标签。仅有标签是不够的：它必须是一个已发布的版本。

如果没有任何发布，用户将获取你默认分支的最新提交，而他们看到的版本将是提交哈希。这样可以使用，但用户无法区分是修复还是重写。HACS 对模板以及希望进入目录的每个仓库都要求发布。

对于集成，请在 `manifest.json` 中使用与标签相同的版本。市场不允许安装清单中没有 `version` 的集成。

## 编写发行说明 {#write-release-notes}

更新实体显示您的发布说明：GitHub 版本的内容。这是用户决定现在更新还是稍后更新的地方。说明发生了哪些变化，并将用户必须先做的操作（例如已更改的选项或已移除的实体）放在顶部。

## 发行版本如何传递给用户 {#how-a-release-reaches-users}

1. 您在 GitHub 上发布一个版本。
2. 目录会获取该版本。目录的 HACS 数据每 4 小时生成一次。
3. 市场每 6 小时读取一次目录，更新实体会显示新版本。

因此，一个发布版本可能需要几小时才能显示。通过链接添加您的存储库的用户，则通过 GitHub API 获取更新，每 48 小时一次，并且仅通过 GitHub 连接。

## 预发布版本 {#pre-releases}

在 GitHub 上将一个版本标记为预发布版本，以便希望测试的用户使用。当用户打开你仓库的 **预发布** 开关时，他们才会获取预发布版本，并且仅当它比你最近的正式版本更新时才可用。

## 需要 Home Assistant 版本 {#require-a-home-assistant-version}

当某个版本需要更新的 Home Assistant 时，在该版本中将 `homeassistant` 设置在 `hacs.json` 中：

```json title="hacs.json"
{
  "name": "My integration",
  "homeassistant": "2026.11.0"
}
```

Marketplace 不会向使用较旧 Home Assistant 的用户提供该版本。当他们安装时，会显示可用的早期版本。要同时允许该版本的测试版，请添加 `b0`，例如 `"2026.11.0b0"`。这仅适用于有发布版本的仓库。

## 发布 ZIP 文件 {#ship-a-zip-file}

一个集成可以作为附加在每个发布版本中的 ZIP 文件进行发布，而不是仓库中的文件。将 `zip_release` 设置为 `true`，并将 `filename` 设置为资产名称：

```json title="hacs.json"
{
  "name": "My integration",
  "zip_release": true,
  "filename": "my_integration.zip"
}
```

Marketplace 会下载该资产并将其解压到集成文件夹中。当您在发布工作流中构建或生成文件时，请使用此方法。HACS 仅支持集成，Marketplace 对模板不允许此操作。

## 较旧版本 {#older-versions}

用户可以从市场中你仓库的菜单安装除了最新版本之外的其他版本。他们可以从你的发布版本中选择，所以请保留旧版本。

## 安全地移除发布版本 {#remove-a-release-safely}

如果你删除一个发布版本或其标签，已经安装的用户仍会保留他们的文件。当市场无法在 GitHub 上找到某个版本时，它会回退到默认安装的版本。
