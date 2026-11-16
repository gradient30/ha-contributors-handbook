---
title: 仪表板如何工作
description: 仪表板是如何由视图、部分、卡片和徽章组成的，策略如何生成它们，以及自定义卡片如何适应其中。
order: 3
sidebarLabel: 仪表盘
---


# 仪表板如何工作 {#how-dashboards-work}
一个 [仪表板](/glossary/dashboard) 是由 [卡片](/glossary/card) 组成的页面，是大多数人最常看到的前端部分。在其背后，它是由视图、区块、卡片和徽章组成的配置，前端将其转换为元素。

> [!注意]
> 仪表板以前被称为 Lovelace，代码仍然使用这个名称：面板是 `lovelace`，仪表板元素以 `hui-` 开头。在文本中，请说仪表板。

## 简而言之 {#in-short}
- 一个仪表板有视图。一个视图有区块，区块里有卡片，或者根据视图类型直接有卡片。
- 每种卡片类型都是一个网页组件，比如 `hui-tile-card`，在仪表板使用时加载。
- 一个仪表板存储在 Home Assistant，或者用 YAML 编写。
- 一种策略可以直接从主页生成仪表板或视图。
- 自定义卡片是从 JavaScript 文件加载的网页组件。

## 从配置到元素 {#from-configuration-to-elements}
仪表板就是一种配置，例如：

```yaml
views:
  - title: Home
    type: sections
    sections:
      - type: grid
        cards:
          - type: tile
            entity: light.kitchen
```

前端读取它，并为每个部分创建一个元素：一个视图、一个部分、一个`hui-tile-card`及其配置。卡片类型在仪表板首次使用它们时加载。

## 视图 {#views}
| 视图类型 | 布局 |
| --- | --- |
| `sections` | 网格中的各个部分，每个部分都有自己的卡片。新仪表板的默认布局。 |
| `masonry` | 按列排列的卡片，根据高度放置 |
| `sidebar` | 一列宽卡片，一列窄卡片 |
| `panel` | 单张卡片，覆盖整个页面 |

## 卡片、徽章和功能 {#cards-badges-and-features}
- **卡片** 显示和控制事物。其配置决定显示内容。许多卡片都有可视化编辑器。
- **徽章** 是视图顶部的小标签。
- **[卡片功能](/glossary/card-feature)** 为卡片添加控制，比如亮度滑块。

卡片及其配置选项见 [仪表板卡片](/design/dashboards)，附有实时示例。

## 仪表板的存储位置 {#where-a-dashboard-is-stored}
- **在存储中**：默认方式。用户可以在 UI 中编辑，Home Assistant 用 WebSocket API 保存。
- **在 YAML 文件中**：用户在文件中编写它。UI 无法编辑。

## 策略和自定义元素 {#strategies-and-custom-elements}
一个 [策略](/glossary/strategy) 是生成仪表盘、视图或某个部分的代码，而不是固定的配置。当用户第一次打开 Home Assistant 时看到的仪表盘就是一个策略示例：它会根据区域和设备自动构建，并在添加新内容时保持更新。用户可以接管生成的仪表盘，并从那里编辑其配置。

卡片、徽章、视图和策略也可以来自前端之外的来源，作为从 JavaScript 文件加载的 Web 组件，并与 `custom:` 类型一起使用，例如 `custom:my-card`。它们获得与内置组件相同的 `hass` 对象和配置。如何构建它们请参见 [自定义卡片及更多](/frontend/custom-ui)。

## 在代码中 {#in-the-code}
| 什么 | 哪里 |
| --- | --- |
| 仪表板面板 | [`src/panels/lovelace/`](https://github.com/home-assistant/frontend/tree/dev/src/panels/lovelace) |
| 视图、部分、卡片、徽章、功能 | 仪表板面板中的 `views/`, `sections/`, `cards/`, `badges/`, `card-features/` |
| 策略 | 仪表板面板中的 `strategies/` |
| 从配置创建元素 | 仪表板面板中的 `create-element/` |
| 编辑器 | 仪表板面板中的 `editor/` |

## 进行此操作 {#work-on-this}
- 从 [你的第一个前端贡献](/frontend/first-contribution) 开始。
- 构建你自己的卡片、徽章或策略：[自定义卡片及更多](/frontend/custom-ui)。
- 内置卡片及其应有的外观和行为：设计区中的 [仪表板卡片](/design/dashboards)。
