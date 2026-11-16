---
title: 仓库结构
description: 每种类型的文件在你的仓库中放在哪里，市场从中安装什么，以及这些内容在用户配置中最终会放在哪里。
order: 2
---

# 仓库结构 {#repository-structure}

每种类型都需要一个公共 GitHub 仓库，在根目录下有一个 `hacs.json` 和一个 README。除此之外，每种类型都有自己的布局。一个仓库包含一个类型的一个项目。

## 每个仓库 {#every-repository}

| 内容 | 原因 |
| --- | --- |
| GitHub 上的公共仓库 | Marketplace 和 HACS 只读取公共 GitHub 仓库。 |
| 根目录中的 `hacs.json` | 没有它，Marketplace 无法安装或更新仓库。参见 [hacs.json](/marketplace/reference/hacs-json)。 |
| `README.md` | 用户在安装前阅读的内容。Marketplace 会在你的仓库页面上显示它，但不包括你 [省略的部分](/marketplace/reference/repository-structure#leave-part-of-your-readme-out-of-the-marketplace)。 |
| GitHub 上的描述 | 在 Marketplace 列表中显示。目录所必需。 |
| GitHub 上的话题 | 帮助用户找到你的仓库。目录所必需。 |
| 启用问题追踪 | 用户报告问题的位置。目录所必需。 |
| GitHub 的发布版本 | 推荐每种类型使用，对于模板和目录是必需的。参见 [发布和更新](/marketplace/guides/releases)。 |

## 集成 {#integrations}

```text
custom_components/awesome/__init__.py
custom_components/awesome/manifest.json
custom_components/awesome/sensor.py
custom_components/awesome/brand/icon.png
hacs.json
README.md
```

- 每个仓库仅允许一个集成，位于 `custom_components/<domain>/`。Marketplace 会使用 `custom_components/` 中的第一个文件夹。
- 集成所需的所有内容都在该文件夹中。
- `manifest.json` 有一个 `domain`，只包含小写字母、数字、下划线和连字符，以及一个 `version`。HACS 还需要 `documentation`、`issue_tracker`、`codeowners` 和 `name`。
- 对于 `content_in_root`，集成的文件位于仓库的根目录。
- 安装到 `custom_components/<domain>/`。

请参阅 [自定义集成](/marketplace/guides/integrations)。

## 仪表板 {#dashboard}

```text
dist/awesome-card.js
hacs.json
README.md
```

- 一个以仓库命名的 JavaScript 文件：`<name>.js`、`<name>.umd.js` 或 `<name>-bundle.js`。对于 `<name>.js`，也会尝试不包含 `lovelace-` 的名称。任何其他名称放在 `filename` 的 `hacs.json` 中。
- 文件附加到你最新的版本，或者在根目录，或者在 `dist` 中。
- 模块需要的文件，例如图片，放在 `dist` 中，或者附加到版本中。
- 安装到 `www/community/<repository name>/`，并作为仪表板资源添加。

请参阅 [仪表板卡片和插件](/marketplace/guides/dashboard)。

## 主题 {#themes}

```text
themes/awesome.yaml
hacs.json
README.md
```

- 一个 YAML 文件位于 `themes/`。HACS 为每个仓库管理一个主题文件。
- 使用 `content_in_root` 时，文件位于仓库根目录。
- 有效的 YAML，不包含像 `!include` 或 `!secret` 的标签。
- 安装到 `themes/<name of the theme file>/`。

参见 [themes](/marketplace/guides/themes)。

## 模板 {#templates}

```text
awesome.jinja
hacs.json
README.md
```

- 根目录中有一个 `.jinja` 文件，在 `hacs.json` 中以 `filename` 命名。不放在子文件夹中。
- UTF-8 编码，大小小于 5 MiB。
- 不包含 `zip_release`。
- 安装到 `custom_templates/`。

参见 [template macros](/marketplace/guides/templates)。

## 市场不安装的类型 {#types-the-marketplace-does-not-install}

HACS 也处理 AppDaemon 应用程序 (`apps/`) 和 Python 脚本 (`python_scripts/`)，目录中也有它们的列表。市场不会安装任何一个。从 2026.11 开始，Home Assistant 还会阻止 HACS 自定义集成，因为市场会替换它。因此在 2026.11 及以后版本，它们都无法被安装。

市场还拒绝包含 Home Assistant OS 的 [apps](/glossary/app) 的仓库。这些可以作为应用程序仓库在 **设置** > **应用程序** 下添加：请参见 [创建和共享仓库](/apps/guides/repository)。

## 在市场中省略部分 README 内容 {#leave-part-of-your-readme-out-of-the-marketplace}

你的 README 会在两个地方被阅读：在 GitHub，人们可以找到你的仓库，以及在市场中，在你的仓库页面。安装说明、一个 [我的链接](/glossary/my-link) 徽章或安装徽章在 GitHub 上有帮助，但市场页面已经有一个安装按钮，所以在那里它们会显得多余。将那些只用于 GitHub 的部分放在两个 HTML 注释之间，市场会将它们省略：

```markdown title="README.md"
# Awesome card {#awesome-card}

<!-- ha-marketplace:exclude-start -->
## Installation {#installation}

Add this repository in the Marketplace, or install it through HACS.
<!-- ha-marketplace:exclude-end -->

## Configuration {#configuration}
```

GitHub 不显示 HTML 注释，因此 README 在那里仍然如前所述。

- 一个部分从开始标记到下一个结束标记。如果没有结束标记，它将一直持续到 README 末尾。
- 标记内的空格是可选的。
- 代码块或内联代码内的标记是文本，而非标记，因此 README 可以将它们作为示例显示。
