---
title: 那个 Supervisor
description: 在Home Assistant OS上运行Home Assistant Core、应用程序、备份和更新的程序，每个都在自己的容器中。
order: 3
---


# 那个 Supervisor {#the-supervisor}
在 Home Assistant OS，Home Assistant Core 本身不会运行。Supervisor 来运行它。Supervisor 启动 Core，更新它，备份它，并恢复它。它还运行 [apps](/apps/how-apps-work)，以及一些自己的辅助程序。

Core、每个应用程序、每个辅助程序以及 Supervisor 本身都作为 Docker 容器运行。

## 简而言之 {#in-short}
- Supervisor 是一个 Python 程序，位于 [home-assistant/supervisor](https://github.com/home-assistant/supervisor) 仓库中。
- 它以容器方式运行 Core、应用程序和插件。它们的网络连接方式详见 [Supervisor 运行内容](/os/supervisor#what-the-supervisor-runs)。
- 它有一个 REST API，位于 `http://supervisor`。Core、应用程序以及命令行使用它。
- 它进行备份，安装更新，并检查系统问题。

## Home Assistant OS 上运行的内容 {#what-runs-on-home-assistant-os}
除了核心和应用程序之外，Supervisor 还运行一些自己的插件：用于 DNS、音频、`ha` 命令行、多播发现，以及在其他所有功能都停用时仍然可工作的状态页面。[Supervisor 运行的内容](/os/supervisor#what-the-supervisor-runs) 列出了每个容器及其名称和网络。

## 它的功能 {#what-it-does}
- **Supervisor API**：核心、应用程序和 `ha` 命令行通过 `http://supervisor` 上的 REST API 与 Supervisor 通信。调用者可以执行的操作取决于其角色。请参见 [Supervisor API](/apps/supervisor-api) 以及核心如何在 [与核心的连接](/os/supervisor/core-connection) 中使用它。
- **Ingress**：显示位于 Home Assistant 内、受登录保护的应用程序的 Web 界面，无需打开端口。请参见 [ingress](/apps/guides/ingress)。
- **备份与更新**：Supervisor 会备份核心、应用程序和文件夹，并从 `version.home-assistant.io` 安装新版本。请参见 [Supervisor 的工作方式](/os/supervisor/architecture)。
- **保持系统健康**：它会持续检查系统，发现的问题会显示为修复问题。请参见 [解决中心](/os/supervisor/resolution-center)。

## 深入了解 {#go-deeper}
- [Supervisor 的工作原理](/os/supervisor/architecture)：它如何启动、工作和代码布局
- [插件](/os/supervisor/plugins)：DNS、音频、CLI、多播和观察者容器
- [开发 Supervisor](/os/supervisor/development)：运行并测试你的更改
- [应用程序如何工作](/apps/how-apps-work)：从应用程序的角度看 Supervisor

## 处理这个 {#work-on-this}
- 从 [你对 Supervisor 的第一次贡献](/os/first-contribution) 开始。它可以在你自己的机器上运行完整的系统。
- 想要构建一个应用程序吗？前往应用区域的 [你的第一个应用](/apps/first-app)。
