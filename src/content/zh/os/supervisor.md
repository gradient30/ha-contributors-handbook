---
title: Supervisor
description: Supervisor做什么,它运行, 和它如何联系 apps和Supervisor API。
order: 4
sidebarGroups:
- 它是如何运作的
- 指南
---



# Supervisor {#supervisor}
[Supervisor](/glossary/supervisor) 是让用户从 Home Assistant 管理整个系统的方法 。 它是一个Python程序,在[Home Assistant/监督员](https://github.com/home-assistant/supervisor)寄存器中,作为容器运行在Home Assistant OS上. 其工作:

- 运行 Home Assistant Core 并更新它 。 当更新失败启动时, 它会回滚 。
- 安装、 运行并更新 [应用程序](/glossary/app) 。
- 制作并恢复备份.
- 更新 Home Assistant OS 和本身 。
- 运行提供D身亡,音频,多播,命令行,以及状态页面的插件.
- 管理主机:网络,主机名,磁盘,和时间,通过D-Bus和OS代理.
- 检查系统是否有问题,并提供修正。

## Supervisor 运行中 {#what-the-supervisor-runs}

Supervisor运行的一切都是一个多克容器。 大部分在私人桥网中被称为`hassio`,`172.30.32.0/23`. Core和多播插件使用主机网络代替,要求它的应用程序也使用:

| 集装箱 | 这是什么 | 地址 |
| --- | --- | --- |
| `hassio_supervisor` | 那个Supervisor | `172.30.32.2` |
| `homeassistant` | Home Assistant Core | 主机网络 |
| `hassio_dns` | [DNS 插件](/os/supervisor/plugins#dns) | `172.30.32.3` |
| `hassio_audio` | [音频插件](/os/supervisor/plugins#audio) | `172.30.32.4` |
| `hassio_cli` | [C箴言插件](/os/supervisor/plugins#cli) | `172.30.32.5` |
| `hassio_observer` | [观察器插件](/os/supervisor/plugins#observer) | `172.30.32.6` |
| `hassio_multicast` | [多播插件](/os/supervisor/plugins#multicast) | 主机网络 |
| `app_<slug>` | 一个应用 | 从 `172.30.33.0/24` 或主机网络 |

Supervisor容器本身由`haos-supervisor.service`在主机上启动,参见[Home Assistant OS](/os/operating-system#how-it-boots). 其他一切都由Supervisor开始。

## 应用程序和 Supervisor API {#apps-and-the-supervisor-api}

Supervisor在`http://supervisor`,在`hassio`网络上有一个REST API。 Home Assistant Core通过`hassio`集成使用它,`ha`命令行通过CLI插件使用它,在他们要求在其配置中访问时应用它. 每位来电者都会得到自己的信物,以及限制自己可能做的工作的角色.

Apps是大多数人遇到Supervisor的地方. Supervisor 从应用程序寄存器中安装它们, 构建或拉动它们的图像, 并运行它们的选项、 端口和访问它们的配置 。 建筑应用,以及完整的 Supervisor API 参考文献在 [应用程序](/apps) 区域中记录 。

## 下一个去哪? {#where-to-go-next}

- [建立发展环境](/os/supervisor/development)用自己的机器运行Supervisor。
- [架构](/os/supervisor/architecture)解释代码是如何组织的.
- [工作](/os/supervisor/jobs) 和 适合于 [解析中心](/os/supervisor/resolution-center) 是 两种最能改变触觉的机制 。

## 本节所有页 {#all-pages-in-this-section}

### 工作原理 {#how-it-works}

- 呻吟( 谢谢) [Supervisor 架构](/os/supervisor/architecture): Supervisor 代码是怎样排列的, 是如何开始的, 以及更新和备份如何在它内部工作 。
- [工作](/os/supervisor/jobs): Supervisor 如何作为工作运行, 附带条件, 货币限制, 节奏, 以及客户可以遵循的进展 。
- [解析中心](/os/supervisor/resolution-center): Supervisor 如何发现检查和评价的问题, 把它们当作问题跟踪, 并用建议来修正它们 。
- [插件](/os/supervisor/plugins): Supervisor 的五个插件运行在 Home Assistant Core 旁边, 每个插件都做什么, 以及它的代码住在哪里 。

### 指南 {#guides}

- [建立发展环境](/os/supervisor/development) : 从源头运行 Supervisor 在其开发容器中运行, 运行测试和linters, 并尝试在真正的系统上构建 。
- [调试为解决 Supervisor](/os/supervisor/debugging): 将 Python 调试器附加到运行中的 Supervisor , 本地或远程设备上, 并查找其日志 。
- [连接核心到 Supervisor](/os/supervisor/core-connection): 运行 Home Assistant Core 从您的开发环境对一个真实的 Supervisor, 来进行散列集成 。
