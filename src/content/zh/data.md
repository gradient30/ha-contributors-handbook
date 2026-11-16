---
title: 数据
description: Home Assistant从数据中学到的东西，它在学习过程中如何尊重你的隐私，以及如何探索你自己家的数据。
---


# 数据 {#data}
Home Assistant 的设计初衷是私密的。你的数据存储在你的家中，除非你决定，否则不会被外传。不过，该项目仍然需要一些数据来做出正确的决策：人们使用了哪些集成、运行了哪些版本、哪些设备运行良好。本部分解释了 Home Assistant 如何在不牺牲隐私的情况下获取这些数据，以及你如何自己使用数据。

你不需要成为数据科学家也能提供帮助。在你自己的安装中开启分析功能已经是一种贡献。如果你喜欢分析数据，你自己的家庭数据和公开数据集都在等待你去探索。

## 从这里开始 {#start-here}
- [你的第一个贡献](/data/first-contribution)：分享你安装的分析数据，并准确查看你发送了什么。
- [隐私原则](/data/privacy)：Home Assistant 对收集的任何数据遵循的规则。
- [分析工作原理](/data/how-it-works)：从你的安装到公共分析网站。

## 指南 {#guides}
- [使用公共数据](/data/guides/public-data)：下载分析数据集，或将其抓取到你自己的工具中。
- [探索你自己的数据](/data/guides/explore-your-data)：设置 JupyterLab 并运行你第一个关于你家中数据的报告。
- [查询数据库](/data/guides/query-the-database)：关于状态、事件和上下文的 SQL 查询示例。
- [在你的集成中进行分析](/data/guides/integration-analytics)：对于开发者，控制设备数据库从你的集成接收的数据。

## 参考 {#reference}
- [分析共享了什么](/data/reference/analytics-data)：每个选项的所有字段。
- [数据模型](/data/reference/data-model)：事件、状态和上下文，是所有 Home Assistant 记录的构建块。
- [数据库架构](/data/reference/database-schema)：记录器数据库的表结构。
- [统计信息](/data/reference/statistics)：短期和长期统计，以及它们的存储方式。

## 联系对象 {#who-to-talk-to}
- 关于分析网站或其数据的问题？在 [analytics.home-assistant.io 仓库](https://github.com/home-assistant/analytics.home-assistant.io) 中提出问题或讨论。
- 关于设备数据库的问题？加入 Home Assistant Discord 服务器上的 [设备数据库项目频道](https://discord.com/channels/330944238910963714/1463602457924997236)。
- 关于记录器数据库的问题？在 [社区论坛](https://community.home-assistant.io/) 提问。
