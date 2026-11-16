---
title: 进入目录
description: 将你的仓库添加到 Marketplace 和 HACS 向所有人展示的目录中，说明审核检查内容，以及重命名和删除的工作方式。
sidebarLabel: 进入目录
order: 7
source: https://github.com/hacs/documentation/blob/main/source/docs/publish/include.md
lastVerified: 2026-10-12
---

# 进入目录 {#get-into-the-catalog}

最后验证于 2026-10-12，针对 https://github.com/hacs/documentation/blob/main/source/docs/publish/include.md.

任何用户都可以通过链接添加你的仓库。要让所有人都能看到，而无需链接，它需要在目录中。该目录是 [hacs/default](https://github.com/hacs/default) 仓库，由 HACS 团队管理，Marketplace 读取的也是同一个目录。你可以通过 pull request 进入。

请准备好等待。HACS 的文档对此说明非常诚实：新增加的项目需要几个月时间才能审核。你可以在 [backlog](https://github.com/hacs/default/pulls?q=is%3Apr+is%3Aopen+draft%3Afalse+sort%3Acreated-asc) 中查看你的 pull request 所在的位置。同时，用户仍然可以通过链接添加你的仓库。

## 你的仓库链接 {#the-link-to-your-repository}

用户添加你的仓库的链接是一个 [我的链接](/glossary/my-link)。它会在他们自己的 Home Assistant 市场中打开你的仓库。当市场还不了解你的仓库，并且链接标明了它的类别时，它会先提供将其添加为自定义仓库的选项。类别是 `integration`、`plugin`、`template` 或 `theme`，与目录中对应类型的文件相同。

[我的链接创建者](https://my.home-assistant.io/create-link/?redirect=marketplace_repository) 通过仓库拥有者、名称和类别来生成链接。将徽章放入你的 README 文件中：

```markdown
[![Open your Home Assistant instance and open a repository in the Marketplace.](https://my.home-assistant.io/badges/marketplace_repository.svg)](https://my.home-assistant.io/redirect/marketplace_repository/?owner=me&repository=my-card&category=plugin)
```

`marketplace_repository` 链接在 Home Assistant 2026.11 中是新的。较早的 `hacs_repository` 链接使用相同的 `owner`、`repository` 和 `category`。它在 2026.11 之前打开 HACS，之后在市场打开，因此可以同时到达用户。HACS 在其 [我的 Home Assistant](https://hacs.xyz/docs/use/my/) 页面上有文档说明。

## 谁可以提交 {#who-can-submit}

只有仓库的所有者或主要贡献者可以提交。

仅用于测试核心集成的 alpha 或 beta 版本的集成，或替代核心集成的集成，不被接受。用户仍然可以通过链接添加它们。

## 在你打开 pull request 之前 {#before-you-open-the-pull-request}

1. 确保你的仓库符合其类型的[要求](/marketplace/reference/repository-structure)，并且有描述、主题、启用问题追踪功能，以及一个 README 文件。
2. 向你的仓库添加[HACS action](https://github.com/hacs/action)，并让它在不忽略任何检查的情况下通过。参见[验证检查](/marketplace/reference/validation)。
3. 对于集成，添加[hassfest action](https://github.com/home-assistant/actions#hassfest)，并让它也通过。
4. 在两者都通过后，发布完整的 GitHub 版本。仅有标签是不够的。

## 打开 pull request {#open-the-pull-request}

1. Fork [hacs/default](https://github.com/hacs/default)，并从 `master` 创建一个新分支。不要直接在 `master` 上工作。
2. 将你的仓库作为 `owner/repository` 添加到相应类型的文件中：`integration`、`plugin`、`theme` 或 `template`。每个文件都是一个 JSON 列表。按照字母顺序添加你的，不要加在最后。
3. 从你自己的账户（而非组织账户）打开 pull request，以便 HACS 团队可以编辑。
4. 完整填写 pull request 模板：检查清单、你的最新发布链接、HACS action 不带 `ignore` 的通过运行链接，以及对于一个集成来说，hassfest 的通过运行链接。具有不完整模板或包含不真实陈述的pull request会在不通知的情况下被关闭。向他人请求审核的pull request也是如此。存在小问题的仓库会将其pull request设置为草稿：修复它们，然后再次标记为准备审核。存在重大问题的则会被关闭。

文件还包含`appdaemon`、`python_script`和`netdaemon`列表。HACS仍然会读取这些列表，但市场不会安装这些类型。

## 审查检查的内容 {#what-the-review-checks}

当你的 pull request 需要审查时，会进行自动检查。除非 HACS 团队在你发起之前另有同意，否则所有检查都必须通过：| 检查 | 检查内容 |
| --- | --- |
| 品牌 | 仅限集成。一个 `brand` 文件夹，至少包含一个 `icon.png`，或者 [brands repository](https://github.com/home-assistant/brands) 中的域名图片。 |
| 清单 | 仅限集成。一个有效的 `manifest.json`，包含 `domain`、`documentation`、`issue_tracker`、`codeowners`、`name` 和 `version`。 |
| HACS 验证 | 在仓库上运行相同的 HACS 验证。 |
| HACS 清单 | 一个 `hacs.json`，至少包含一个 `name`。 |
| 已归档 | 仓库未归档。 |
| 发布 | 至少有一次发布。 |
| 所有者 | 您拥有该仓库或是主要贡献者。 |
| 图片 | 仪表板插件和主题专用。在 README 中的图片。 |
| 仓库 | 有描述、开启问题，以及话题标签。 |
| 语法检查 | 您更改的文件是有效的 JSON 并已排序。 |在您的 pull request 合并后，您的存储库将被纳入下一次计划扫描。

## 重命名或移动你的仓库 {#rename-or-move-your-repository}

当你重命名你的仓库，或将其转移到另一个账户时，你无需做任何操作。HACS 团队会更新目录。

## 移除它 {#take-it-out}

当你在GitHub上归档你的仓库时，HACS团队会将其从目录中移除。已安装的用户会保留它，但不会收到更多更新，并且修复操作会告诉他们原因。

如果你有其他原因需要将其移除，请在[hacs/integration](https://github.com/hacs/integration/issues/new?template=removal.yml)中使用 **请求移除仓库** 模板打开一个 issue。在删除仓库之前请先执行此操作：如果你删除了一个在目录中的仓库，将来你将无法将任何仓库添加到该目录中。

当仓库被废弃、破坏Home Assistant、窃取凭证或被删除时，也会被移除。一个有害的仓库会被标记为关键：市场随后会立即从每个拥有它的Home Assistant中卸载它。
