---
title: 发布自定义集成
description: 当你的集成存在于自己的代码库而不是核心中时，有什么不同，以及市场需要它提供什么。
sidebarLabel: 自定义集成
order: 1
---

# 发布自定义集成 {#publish-a-custom-integration}

一个 [自定义集成](/glossary/custom-integration) 的构建方式与核心中的集成相同。[构建集成](/core/integrations) 中的所有内容都适用：清单、配置流程、实体、数据获取和测试。本页仅涉及自行发布时的不同之处。

对于新的集成，推荐从 Marketplace 开始，即使你希望将来它进入核心。请参见 [它是否属于核心](/core/integrations/create#does-it-belong-in-core)。

## 放在自己的仓库中 {#put-it-in-its-own-repository}

一个仓库只包含一个集成，如 `custom_components/<domain>/`：

```text
custom_components/my_integration/__init__.py
custom_components/my_integration/manifest.json
custom_components/my_integration/sensor.py
custom_components/my_integration/translations/en.json
custom_components/my_integration/brand/icon.png
hacs.json
README.md
```

Marketplace 会安装它在 `custom_components/` 下找到的第一个文件夹到用户配置文件夹的 `custom_components/<domain>/`。集成所需的所有文件必须在该文件夹内。[仓库结构](/marketplace/reference/repository-structure#integrations) 包含它接受的其他布局。

## 清单 {#the-manifest}

自定义集成需要两个核心集成中未包含的密钥：

- `version`：必填。如果没有加载器可接受的版本，市场将拒绝安装。请使用与你发布的标签相同的版本。
- `issue_tracker`：用户报告错误的地方。HACS 要求在目录中提供它。

`documentation` 指向你自己的文档，如你的 README。[清单参考](/core/integrations/manifest#custom-integrations-only) 有详细信息。

只列出那些尚未成为 Home Assistant 本身要求的 `requirements`。

## 类别 {#categories}

在你的清单中添加 `categories`：一到三个 [集成类别](/glossary/integration-category)，说明你的集成的用途。自定义集成不需要这些类别，但目录会在发布到市场的数据中包含它们。

```json title="manifest.json"
{
  "categories": ["energy.ev_charging"]
}
```

选择它们的方式与核心中的集成相同。[集成类别](/core/integrations/categories) 包含所有类别以及如何选择它们。HACS 操作会检查这些类别：缺失的键会发出警告，未知类别会导致检查失败。

## 选择一个属于你的域名 {#pick-a-domain-that-is-yours}

`domain` 是文件夹名称，Home Assistant 是你用来识别集成的名称。选择一个核心中没有使用的域名。

带有内置域名的自定义集成会替换它。Home Assistant 允许这样做，但用户会失去内置集成的更新，并且市场会在安装前要求用户确认。目录不接受替换核心集成的集成。用户仍然可以通过链接添加它们。

两个仓库不能安装同一个域名。当用户安装了一个后，市场会拒绝另一个。

## 翻译 {#translations}

自定义集成不使用 `strings.json`，并且不会在 Lokalise 上进行翻译。将完成的文件以 `translations/` 的形式发送，并附上完整的 `en.json`。请参见 [自定义集成的翻译](/core/integrations/translations#custom-integrations)。

## 品牌图片 {#brand-images}

将您的图标和徽标放在集成文件夹内的 `brand/` 文件夹中。Home Assistant 会在您的集成安装后显示它们。Marketplace 在此之前也会显示它们：品牌网站会从目录中每个集成的最新版本中获取它们。

不要使用 Home Assistant 品牌图片。用户可能会将您的集成误认为是官方集成。[品牌页面](/core/integrations/brands#brand-images-for-custom-integrations) 提供了图片名称和尺寸。

## 在更新中保留用户文件 {#keep-user-files-across-updates}

更新会替换整个集成文件夹。如果你的集成程序在其中写入用户需要保留的文件，请将它们放在一个子文件夹中，并将其命名为 `hacs.json`：

```json
{
  "name": "My integration",
  "persistent_directory": "userfiles"
}
```

在更新过程中，市场会将该文件夹移开，并在更新后将其放回。

## 重启 {#restarts}

在第一次安装时，带有配置流程的集成会立即加载，因此用户可以在不重启的情况下添加它。使用 YAML 设置的集成需要重启，已经加载的集成的每次更新或移除也需要重启。市场为此提供了一个修复按钮，可以重启。

## 设置链接 {#link-to-the-setup}

安装集成后，[我的链接](/glossary/my-link) 可以直接将用户带到其设置页面。`config_flow_start` 链接会在用户自己的 Home Assistant 中启动所提供域的 [配置流程](/glossary/config-flow)。[我的链接创建器](https://my.home-assistant.io/create-link/?redirect=config_flow_start) 为你的 README 制作徽章：

```markdown
[![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=my_integration)
```

要在市场中链接到你的仓库，以便用户可以先安装，请参阅 [你的仓库链接](/marketplace/guides/catalog#the-link-to-your-repository)。

## 在你的仓库中检查它 {#check-it-in-your-repository}

在每次推送和 pull request 时运行两个 GitHub Actions：

- [hassfest](https://github.com/home-assistant/actions#hassfest) 检查你的集成的清单、翻译和其他文件。
- 带有 `category: "integration"` 的 [HACS action](https://github.com/hacs/action) 检查目录所需的内容。请参见 [验证检查](/marketplace/reference/validation)。

两者都必须通过才能 [进入目录](/marketplace/guides/catalog)。

## 跟上 Home Assistant 的步伐 {#keep-up-with-home-assistant}

核心的变化可能会破坏自定义集成。核心中自定义集成所使用的内容，如助手、常量和实体属性的更改，会在最初 12 个月内被标记为弃用，并在[博客](https://contributors.home-assistant.io/blog/)上宣布。[弃用政策](/core/development/deprecating#developer-facing-deprecations)有详细信息。在[测试版](/releases)上测试您的集成，并在发布需要更新 Home Assistant 时在 `hacs.json` 中设置 `homeassistant`。请参阅[版本和更新](/marketplace/guides/releases)。

[集成质量等级](/core/quality-scale)没有为自定义集成设置等级，但其规则仍然是一个很好的指南。

## 带入核心 {#bring-it-to-core}

一旦你的集成成熟并拥有用户基础，可以在 [**#developers**](https://discord.com/channels/330944238910963714/554842238073700352) 频道[Discord](https://www.home-assistant.io/join-chat/) 上询问是否应内置于核心。[是否属于核心](/core/integrations/create#does-it-belong-in-core) 列出了核心所需的要求，每个新的核心集成都需要遵守质量等级的 [青铜规则](/core/quality-scale/rules#bronze)。

本页上的一些差异在核心中会有所调整。例如，品牌图片会放到 [brands repository](/core/integrations/brands)，翻译内容则来自 `strings.json`。
