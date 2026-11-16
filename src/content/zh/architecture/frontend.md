---
title: 前端
description: 网页界面在整个Home Assistant中的位置，以及在哪里可以找到其详细信息。
order: 30
---


# 前端 {#the-frontend}
[前端](/glossary/frontend)是用户看到的所有内容：仪表板、设置、自动化编辑器以及每个对话框。它是一个网页应用程序，使用Lit和TypeScript构建，位于[home-assistant/frontend](https://github.com/home-assistant/frontend)仓库中。核心提供其文件，它在浏览器中运行，[伴侣应用](/architecture/platform/companion-apps)也会显示它。

## 它在整体中的位置 {#its-place-in-the-whole}
- **它本身不保存任何状态。** 它展示的所有内容都来自 Core，通过 [WebSocket API](/core/internals/websocket-api)，每一次变更都会推送给它。关闭浏览器，所有内容都不会丢失。
- **它从不直接与设备通信。** 选择一个灯光会在 Core 中执行一个操作，而 Core 的集成会与灯光通信。前端只看到实体。
- **文本来自两个来源。** 前端自身的文本来自它的翻译文件。集成的文本，如实体名称和设置步骤，来自 Core，即每个集成的 `strings.json`。
- **它分部分加载。** 页面（称为面板）和仪表板卡片只在需要时加载，因此首页加载很快。

## 详细信息 {#the-details}
[前端](/frontend) 区域解释了它是如何构建的：

- [架构](/frontend/architecture)：应用的各个部分，以及它们在仓库中的位置。
- [hass 对象和上下文](/frontend/architecture/hass-and-contexts)：组件如何获取所需的数据。
- [数据层](/frontend/architecture/data)：前端如何与核心通信。
- [路由和面板](/frontend/architecture/routing-and-panels)：页面，以及它们如何加载。

在此区域：[仪表板](/architecture/frontend/dashboards)，了解视图、卡片和策略如何组合。

组件及其设计在[设计](/design/components)区域有文档说明。

## 开始工作 {#work-on-this}
- 前端新手？先从[你的第一个前端贡献](/frontend/first-contribution)开始。
- 前端区域的[架构](/frontend/architecture)：应用是如何构建的。
- 想处理外观？[设计](/design/first-contribution)区域是起点。
