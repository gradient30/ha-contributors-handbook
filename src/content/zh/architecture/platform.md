---
title: 围绕核心
description: 运行在 Home Assistant Core 旁边的软件，或者从其他地方与其通信的软件，以及它们如何整合在一起。
order: 40
---


# 围绕核心 {#around-core}
Home Assistant Core 是核心，但它并不独自完成所有任务。在 Home Assistant OS 上，Supervisor 运行它、更新它并进行备份，旁边还有添加更多软件的应用程序。伴侣应用程序将 Home Assistant 引入手机、手表和汽车。Home Assistant Link 使其从任何地方都可访问，而语音从厨房的卫星传输到其他地方的语音引擎。

## Home Assistant 的运行方式 {#how-home-assistant-runs}
有两种支持的 Home Assistant 运行方式，请参见 [安装类型](/os/installation-types)：

- **Home Assistant OS**：为了 Home Assistant 制作的操作系统。[[Supervisor]](/architecture/platform/supervisor/) 运行 Core 和 [应用](/apps/how-apps-work)，每个都在自己的容器中，并安装所有内容的更新，包括操作系统本身。几乎适合所有人使用。
- **Home Assistant Container**：在用户管理的系统上以容器形式运行 Core。没有 Supervisor，也没有应用。

两者运行相同的 Core：Home Assistant OS 使用的镜像是建立在 Home Assistant Container 运行的相同容器镜像之上的。几乎所有你构建的内容在两者中都能以相同方式运行。

## 组成部分 {#the-pieces}
- [Supervisor](/architecture/platform/supervisor)：运行 Home Assistant OS 上的核心、应用程序、备份和更新。
- [Home Assistant OS](/os/operating-system)：操作系统，它如何构建以及如何安全更新。
- [应用程序](/apps/how-apps-work)：除了 Home Assistant 之外的额外软件，以容器形式运行。
- [伴生应用](/architecture/platform/companion-apps)：在 Android 和 Apple 设备上的 Home Assistant。
- [Home Assistant Link](/architecture/platform/cloud)：远程访问、语音助手等功能，无需打开你的住宅。
- [语音](/architecture/platform/voice)：一句口语如何转化为一个动作。

## 完成此任务 {#work-on-this}
- [你对 Supervisor](/os/first-contribution) 的首次贡献，或对操作系统的贡献。
- 在应用程序领域的 [首次贡献](/apps/first-contribution)：构建一个应用，或帮助官方应用。
- [首次伴侣应用贡献](/companion/first-contribution)：Android 或 Apple。
- 语音：为你的语言在 [语音翻译](/translate/voice) 中编写句子，或在 Core 中处理 [Assist 流水线](/core/internals/assist-pipelines)。
