---
title: 隐私原则
description: Home Assistant 对其收集的每一条数据遵循的规则，以及原因。
order: 3
---


# 隐私原则 {#privacy-principles}
Home Assistant 建立在这样一个信念之上：你的数据是你的，所有数据都是你的，而且你无需分享数据就能从中学习。拥有 Home Assistant 的 [Open Home Foundation](/glossary/open-home-foundation) 将隐私与选择和可持续性并列为其核心原则。这个领域中的一切都源于此原则。

## 你的数据留在本地 {#your-data-stays-home}
Home Assistant 记录的关于你家庭的一切数据，比如设备状态、历史记录和能源使用情况，都存储在你自己的硬件上，在你自己的数据库中。除非你设置了将数据发送到其他地方的功能，否则数据绝不会离开你的家。这也是该项目不知道有多少人在运行 Home Assistant 的原因：它无法统计未选择加入的安装数量。

## 选择加入，永不自动退出 {#opt-in-never-opt-out}
除非你开启，否则不会与项目共享任何内容。在你选择启用之前（在入门或之后的设置中），分析功能是关闭的。设备数据库也是同样情况，这是一个单独的选择。

## 你可以选择分享内容 {#you-choose-what-to-share}
分析数据分为不同的选项，从基本的系统信息到使用情况、数量和崩溃报告。你可以随时开关每个选项，并随时更改决定。关闭选项会立即生效。

## 你可以查看你分享的内容 {#you-can-see-what-you-share}
每次 Home Assistant 发送分析数据时，都会将发送的确切数据记录到你的日志中。没有隐藏部分。对于设备数据库，你可以从分析设置中下载将要分享内容的预览。

## 只统计数量，不统计个人 {#only-counts-never-people}
共享的数据不包含姓名、实体ID、地址，也不包含你自己命名的任何内容。每个安装都会发送一个随机标识符，仅用于确保其被统计一次，即使它每天都会报告数据。国家信息是根据数据到达时的IP地址推断的。IP地址本身不会与分析数据一起存储。

只发布汇总总数。单个安装的数据绝不公开，你无法在公开数据中找到单个安装的信息。

## 数据不会永久保存 {#data-does-not-stay-forever}
分析接收器会在安装程序最后一次报告后最多保留 60 天的数据。停止共享后，你的安装程序在该期限后将从数据中消失。

## 完全开放 {#open-all-the-way}
收集分析数据的代码是 Home Assistant 本身的一部分，位于 [分析集成](https://github.com/home-assistant/core/tree/dev/homeassistant/components/analytics) 中。接收和处理这些数据的代码也是开源的，位于 [analytics.home-assistant.io 仓库](https://github.com/home-assistant/analytics.home-assistant.io)。任何人都可以查看数据的处理情况。

Open Home Foundation 的网站遵循同样的理念：它们使用 [Plausible](https://www.openhomefoundation.org/blog/making-our-web-analytics-open-source-with-plausible/)，这是一款不开启个人数据收集或追踪的开源分析工具。

## 关于设备数据库 {#for-the-device-database}
设备数据库有其自己的[数据使用声明](https://www.openhomefoundation.org/device-database-data-use-statement)，详细说明了设备数据的处理方式。它只包括关于设备的详细信息，如制造商和型号，从不包括任何个人身份信息，例如你为设备命名的名称。
