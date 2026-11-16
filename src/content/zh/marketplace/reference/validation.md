---
title: 验证检查
description: 在每次推送时检查你的仓库的 HACS 操作，以及市场在调用安装完成之前运行的检查。
order: 3
---

# 验证检查 {#validation-checks}

有两种检查会查看你的工作。HACS 操作在你自己的仓库中运行，也是目录审核运行的操作。Marketplace 在用户安装时会运行它自己的检查，并会拒绝安装失败的项目。两者如下。

## HACS 操作 {#the-hacs-action}

[hacs/action](https://github.com/hacs/action) 以 GitHub Action 的方式运行与 HACS 相同的验证。将它添加到你的仓库中，在 `.github/workflows/validate.yaml`：

```yaml title=".github/workflows/validate.yaml"
name: Validate

on:
  push:
  pull_request:
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch:

permissions: {}

jobs:
  validate-hacs:
    runs-on: "ubuntu-latest"
    steps:
      - name: HACS validation
        uses: "hacs/action@main"
        with:
          category: "integration"
```

将 `category` 设置为你的仓库类型：`integration`，`plugin` 用于仪表板插件，`theme`，或 `template`。该操作还接受 `appdaemon` 和 `python_script`，这些类型是 Marketplace 不会安装的。

它将在每次 push 和 pull request、每晚以及从 **Actions** 标签手动启动时运行。要将版本固定，而不是 `main`，请在 `@` 后使用标签，并让 Dependabot 保持其最新状态。

### 输入 {#inputs}

| 输入 | |
| --- | --- |
| `category` | 必填。仓库的类型。 |
| `ignore` | 要跳过的检查，用空格分隔。仅用于您自己的运行：目录不接受被忽略的检查。 |
| `repository` | 要检查的仓库的全名，如果不是此仓库。 |
| `comment` | 将结果作为评论发布到 pull request。默认情况下为 `true`。 |
| `github_token` | 要使用的令牌。默认使用工作流的令牌。 |

### 你可以跳过的检查项 {#checks-you-can-skip}

| 检查 | 检查说明 |
| --- | --- |
| `archived` | 仓库未归档。 |
| `brands` | 一个集成具有品牌图片：一个 `brand` 文件夹内含 `icon.png`，或在[品牌仓库](https://github.com/home-assistant/brands)中有图片。 |
| `description` | 仓库有描述。 |
| `hacsjson` | `hacs.json` 存在。 |
| `images` | README 中有图片。 |
| `information` | 仓库有信息文件，如 README。 |
| `integration_categories` | 集成清单中的 `categories` 有效：已知的[integration categories](/core/integrations/categories)，数量为一到三个，不重复。没有 `categories` 的清单只会收到警告。 |
| `issues` | 问题功能已开启。 |
| `topics` | 仓库有主题。 |

[catalog review](/marketplace/guides/catalog#what-the-review-checks) 会进行比这些更多的检查。

## hassfest {#hassfest}

对于集成，也运行 [hassfest](https://github.com/home-assistant/actions#hassfest)，这是核心中的集成所执行的相同验证。目录要求使用它。

```yaml title=".github/workflows/hassfest.yaml"
name: Validate with hassfest

on:
  push:
  pull_request:
  schedule:
    - cron: "0 0 * * *"

jobs:
  validate:
    runs-on: "ubuntu-latest"
    steps:
      - uses: "actions/checkout@v4"
      - uses: "home-assistant/actions/hassfest@master"
```

## 市场检查内容 {#what-the-marketplace-checks}

市场在安装前进行检查，并在撰写文档后再次检查。当写入后的检查失败时，文件会恢复到安装前的状态。| 检查 | 类型 | 失败情况 |
| --- | --- | --- |
| 根目录中的 `hacs.json` | 全部 | 没有它的仓库无法安装或更新。 |
| 未存档，未移除 | 全部 | 已存档的仓库无法安装，大多数目录移除的仓库也无法安装。 |
| 文件放置正确 | 全部 | 文件没有放在 [仓库结构](/marketplace/reference/repository-structure) 指定的位置。 |
| 最低 Home Assistant 版本 | 有发布版本的全部 | 发布版本需要的 Home Assistant 比用户的版本更新。系统将提供较旧的版本给用户。 |
| 域名 | 集成 | `manifest.json` 中的 `domain` 包含小写字母、数字、下划线和连字符之外的其他字符。 |
| 域名所有者 | 集成 | 另一个已安装的仓库拥有相同的域名。 || 替换内置集成 | 集成 | 域属于核心之一，并且用户未确认。 |
| 可加载的清单 | 集成 | 写入后：`manifest.json` 有另一个域，或者加载器接受的 `version` 不存在。 |
| 文件夹所有者 | 仪表板，主题 | 另一个已安装的仓库使用了相同的文件夹。 |
| 模块存在 | 仪表板 | 写入后：JavaScript 文件缺失。 |
| 主题 YAML | 主题 | 写入后：具有标签的 YAML 文件，或者未通过主题验证的 YAML 文件。 |
| 模板文件 | 模板 | `filename` 不是根目录下的 `.jinja` 文件，`zip_release` 已设置，或另一个仓库有同名文件。写入后：文件不是 UTF-8 编码，或者大于 5 MiB。 |
| 下载大小 | 全部 | 下载或解压的 ZIP 文件大于 100 MiB，或超过 50,000 个文件。 |这些检查存在于核心的 `marketplace` 集成中：[`homeassistant/components/marketplace/repositories/`](https://github.com/home-assistant/core/tree/dev/homeassistant/components/marketplace/repositories)。
