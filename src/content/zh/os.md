---
title: 操作系统和Supervisor
description: 研究Home Assistant OS和Supervisor，这两部分将一块板或虚拟机变成一个Home Assistant系统，该系统能够运行、更新和自我修复。
---

# 操作系统和Supervisor {#os-and-supervisor}

大多数人在 [Home Assistant OS](/glossary/home-assistant-os) 上运行 Home Assistant。他们闪烁一个镜像，插入设备，然后再也不考虑 Linux。这之所以可行，是因为两个项目协同工作：- **Home Assistant OS** 是一个小型只读 Linux 系统，使用 Buildroot 构建，Buildroot 是一个从源代码构建完整嵌入式 Linux 系统的工具。它启动设备、运行 Docker，并通过 A/B 方案自我更新：系统有两个副本，A 和 B，将更新写入未运行的副本，如果更新未能启动，则回退到另一个副本。RAUC 是嵌入式 Linux 的更新系统，可以完成这个工作。操作系统代理（OS Agent）是主机上的一个小程序，为 Supervisor 执行主机任务，例如移动数据盘。
- **Supervisor** 是一个 Python 程序，在其上层的容器中运行。它运行 Home Assistant Core、应用程序及其自身插件，进行备份、安装更新，并监控系统的健康状态。此区域适用于希望开发其中任意一个的开发者。对于操作系统，您将使用嵌入式 Linux：Buildroot、内核、引导加载程序和板级支持。对于Supervisor，您将使用异步Python、Docker 和 D-Bus，这是 Linux 服务之间用于相互通信的消息总线。两者都不需要您了解另一个。

## 各部分如何配合 {#how-the-pieces-fit}

图表。从上到下：什么运行在什么上。点击一个框以查看更多关于它的信息。

- 由Supervisor运行，每个在自己的容器中  
  - [Home Assistant Core](/core)：Home Assistant 本身  
  - [应用程序](/apps/how-apps-work)：位于核心旁的软件  
  - [插件](/os/supervisor/plugins)：DNS、音频、CLI 等  
- 管理上述所有内容，在自己的容器中  
  - [Supervisor](/os/supervisor/architecture)：运行、更新并备份所有内容  
- [Home Assistant OS](/os/operating-system)（本页主题）  
  - Docker：运行容器  
  - [NetworkManager](/os/operating-system/networking)：网络管理  
  - [RAUC](/os/operating-system/update-system)：更新，带有两个系统槽  
  - OS Agent：为Supervisor处理主机任务  
  - [Buildroot](/os/operating-system/build)：从源码构建，只读  
- [硬件板](/os/operating-system/boards)  
  - [绿色和黄色](/os/operating-system/boards)：Home Assistant 硬件  
  - [树莓派](/os/operating-system/raspberry-pi)：Pi 3、4 和 5  
  - [ODROID](/os/operating-system/odroid)：Hardkernel 板  
  - [个人电脑](/os/operating-system/generic)：通用 x86-64 和 aarch64  
  - [虚拟机](/os/operating-system/virtual-machine)：OVA、QCOW2 等[架构](/architecture/platform) 区域解释了整体情况。此区域深入说明了你需要更改事物的细节。

## 从这里开始 {#start-here}

- [你的第一次贡献](/os/first-contribution)：在其开发容器中运行 Supervisor，进行更改，并打开一个 pull request。
- [安装类型](/os/installation-types)：OS 与 Supervisor 的使用情况，以及它们未被使用的地方。

## Home Assistant OS {#home-assistant-os}

- [概览](/os/operating-system)：操作系统的内容、启动方式以及仓库的组织结构。
- [构建镜像](/os/operating-system/build)：设置构建容器并为板卡构建镜像。
- [测试你的构建](/os/operating-system/test)：在 QEMU 中启动它，运行测试，并将其安装到设备上。
- [配置主机](/os/operating-system/configuration)：`CONFIG` USB 驱动器、内核模块、udev 规则以及时间服务器。
- [配置网络](/os/operating-system/networking)：NetworkManager 连接、Wi-Fi 和静态地址。
- [调试主机](/os/operating-system/debugging)：通过 22222 端口的 SSH、串口控制台和日志。
- [版本发布与构建](/os/operating-system/releases)：分支、版本号以及构建流水线。
- 参考资料：[分区](/os/operating-system/partitions)、[更新系统](/os/operating-system/update-system)、[板卡元数据](/os/operating-system/board-metadata) 以及 [支持的板卡](/os/operating-system/boards)。

## Supervisor {#supervisor}

- [概览](/os/supervisor)：Supervisor 的功能以及它运行的内容。
- [设置开发环境](/os/supervisor/development)：在开发容器中运行 Supervisor，并在真实系统上进行测试。
- [调试 Supervisor](/os/supervisor/debugging)：附加 Python 调试器并读取日志。
- [将核心连接到 Supervisor](/os/supervisor/core-connection)：针对真实的 Supervisor 进行 `hassio` 集成工作。
- 工作原理：[架构](/os/supervisor/architecture)、[任务](/os/supervisor/jobs)、[决议中心](/os/supervisor/resolution-center)以及[插件](/os/supervisor/plugins)。

Supervisor 也是运行 [应用程序](/glossary/app) 的平台。构建应用程序以及它们使用的 Supervisor API 参考，都位于 [应用](/apps) 区域。

## 联系对象 {#who-to-talk-to}

- 关于 Home Assistant OS 和 Supervisor 的问题，请在 [Home Assistant Discord](https://www.home-assistant.io/join-chat/) 的 [**#operating-system**](https://discord.com/channels/330944238910963714/1475552965954900018) 频道中提问。看不到该频道？在 **频道与角色** 中选择 **我想为 Home Assistant 提供开发技能**。
- 问题和 pull request 存在于 [home-assistant/operating-system](https://github.com/home-assistant/operating-system) 和 [home-assistant/supervisor](https://github.com/home-assistant/supervisor) 中。每个插件都有自己的仓库，列在 [plugins](/os/supervisor/plugins) 页面上。
- 添加对新板子的支持是一个架构决策。请阅读 [ADR-0015](https://github.com/home-assistant/architecture/blob/master/adr/0015-home-assistant-os.md) 和 [ADR-0017](https://github.com/home-assistant/architecture/blob/master/adr/0017-hardware-screening-os.md)，然后在开始编写代码之前，在 [架构仓库](https://github.com/home-assistant/architecture) 中发起讨论。
