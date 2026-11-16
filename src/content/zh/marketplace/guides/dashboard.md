---
title: 发布仪表板卡片或插件
description: 打包自定义卡片、卡片功能、徽章或其他 JavaScript 模块，以便市场可以安装并在每个仪表板上加载它。
sidebarLabel: 仪表板卡片和插件
order: 2
---

# 发布仪表板卡片或插件 {#publish-a-dashboard-card-or-plugin}

卡片、卡片功能、徽章、视图布局和仪表板策略是 JavaScript 模块，由 Home Assistant 加载到前端。如何构建它们，请参阅前端区域的 [自定义卡片及更多](/frontend/custom-ui)。本页面介绍如何打包一个模块，以便市场可以安装它。

目录、`hacs.json` 和 HACS 操作称这种类型为 `plugin`。市场将其显示为 **仪表板**。它们是同一事物。

## 市场如何处理它 {#what-the-marketplace-does-with-it}

当用户安装你的仓库时，市场会：

1. 下载你的 JavaScript 文件，以及与其相邻的其他文件，到配置文件夹的 `www/community/<repository name>/`。
2. 将该文件作为类型为 `module` 的 [仪表板资源](/frontend/custom-ui/resources) 添加，在 `/local/community/<repository name>/<file name>`，使用 URL 中的版本号，例如 `?v=<id>-1.2.0`。版本在每次更新时都会变化，因此浏览器会加载新文件而不是缓存文件。
3. 剩下的交给用户，用户需要重新加载浏览器以加载你的模块。

当用户在 YAML 中管理资源时，市场无法添加该资源。安装对话框会显示用户需要添加的内容。当你的模块已经在 `frontend` 配置中通过 `extra_module_url` 加载时，市场不会再添加资源，因此不会被加载两次。

在卸载时，市场会删除这些文件和资源。

## 将你的文件命名为你的代码库名称 {#name-your-file-after-your-repository}

Marketplace 会寻找一个文件，并通过其名称找到它。如果 `hacs.json` 中没有 `filename`，它将尝试以下名称，其中 `<name>` 是你的代码库名称：

1. `<name>.js`，去掉 `lovelace-` 前缀。代码库 `lovelace-awesome-card` 提供 `awesome-card.js`。
2. `<name>.js`
3. `<name>.umd.js`
4. `<name>-bundle.js`

它首先在你最新的 GitHub 发布版本的资源中查找它们。如果没有包含这些文件的发布版本，它会先在代码库的根目录查找，然后在 `dist` 文件夹中查找。如果 `hacs.json` 中将 `content_in_root` 设置为 `true`，则只会在根目录中查找。

如果你的卡片需要其他文件，例如图片或翻译，请将它们与卡片一起放在 `dist` 中，或者将它们全部附加到发布版本。

任何其他名称的文件都需要 `hacs.json` 中的 `filename`：

```json
{
  "name": "Awesome card",
  "filename": "awesome-card-bundle.js"
}
```

[代码库结构](/marketplace/reference/repository-structure#dashboard) 中有示例。

## 在发布前先构建它 {#build-it-before-you-release}

用户获得的正是你发布的文件：Marketplace 并不会构建任何东西。将构建好的文件提交到 `dist`，或者更好的是，在你发布版本时在 GitHub Action 中构建它，并将其作为资源附加到发布版本中。这样你的仓库只保存源代码，每个发布版本都有自己的构建文件。

单个打包文件是最容易安装的。将你的依赖项（如 Lit）打包到其中：前端不会共享自己的副本，如 [使用哪些工具](/frontend/custom-ui#which-tools-to-use) 所解释的那样。

## 两个卡片不能共享一个文件夹 {#two-cards-can-not-share-a-folder}

文件夹以仓库命名，不包含其所有者。当用户已安装来自 `someone/awesome-card` 的卡片时，Marketplace 会拒绝在其旁边安装 `someone-else/awesome-card`。

## 显示外观 {#show-what-it-looks-like}

用户根据卡片的外观来选择。请在你的 README 中放置截图，Marketplace 会在你的仓库页面显示这些截图。目录会检查仪表板仓库的 README 是否包含图片。

为了让用户在安装前试用你的卡片，请在自己的网站上放置一个 [在线演示](/frontend/custom-ui/demo)，并在 README 中链接到它。

## 在你的仓库中检查 {#check-it-in-your-repository}

在每次 push 和 pull request 时使用 `category: "plugin"` 运行 [HACS 动作](https://github.com/hacs/action)。参见 [验证检查](/marketplace/reference/validation) 。

## 推向前端 {#bring-it-to-the-frontend}

一旦你的卡片成熟并拥有了用户群体，可以联系维护者，例如在 [**#frontend**](https://discord.com/channels/330944238910963714/1475552784278360176) 频道的 [Discord](https://www.home-assistant.io/join-chat/)，看看是否应该内置发布。前端的新卡片既是设计决策，也是代码问题：请参阅 [需要设计输入的更改](/frontend/development/review-and-release#changes-that-need-design-input)。
