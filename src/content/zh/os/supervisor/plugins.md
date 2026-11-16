---
title: 插件
description: Supervisor 的五个插件运行在 Home Assistant Core 旁边, 每个插件都做什么, 以及它的代码住在哪里 。
sidebarGroup: 它是如何运作的
order: 4
---

# 插件 {#plugins}

插件是为系统本身运行的 Supervisor 的容器, 而不是用户 。 它们提供Core和app共享的服务,如DNS和音频. 用户不安装或删除它们,而 Supervisor 自动更新它们 。

在 Supervisor 一侧, 每个插件都是 [`supervisor/plugins/`](https://github.com/home-assistant/supervisor/tree/main/supervisor/plugins) 中的一个类, 基于 `PluginBase` 。 它处理容器的安装、启动、更新和修理,并在停止时由监督员重新启动。 每个插件的图像是`ghcr.io/home-assistant/<arch>-hassio-<plugin>`,版本来自与其它文件相同的版本文件.

| 插头 | 集装箱 | 仓库 | 这是什么 |
| --- | --- | --- | --- |
| DNS 数据 | `hassio_dns` | [插件点数](https://github.com/home-assistant/plugin-dns) | CoreDNS,用于容器中的名称解析 |
| 音频 | `hassio_audio` | [插件自动](https://github.com/home-assistant/plugin-audio) | PulseAudio, 用于 声音 出入 |
| 国 际 | `hassio_cli` | [插件- cli](https://github.com/home-assistant/plugin-cli) | `ha` 命令行 |
| 多播 | `hassio_multicast` | [插件多播](https://github.com/home-assistant/plugin-multicast) | MDNS 中继器 |
| 观察员 | `hassio_observer` | [插件观测器](https://github.com/home-assistant/plugin-observer) | 状态页面,当其他不起作用时有效 |

## DNS 数据 {#dns}

`hassio`网络上的每一个容器都使用 DNS 插件作为其名称服务器. 它用自己的两个插件运行 [核心DNA](https://coredns.io/) :

- ** mdns** 解析`.local`名称,通过在主机上询问系统解析到D-Bus.
- **回落** 在回落开始时,Cloudflare的DNS对TLS的检索失败.

Supervisor 写一个主机文件, 上面有容器的名称, 如 `supervisor` 和 `homeassistant`, 这样它们就可以用名字联系到对方 。 其他的浏览到主机的 DNS 服务器, 或是用户设置的 `ha dns options` 。 配置模板为 `rootfs/usr/share/tempio/corefile` 在插件仓库中 。

## 音频 {#audio}

音频插件在ALSA顶端运行PulseAudio,因此Core和需要音频的应用共享一个声音系统. Apps的配置要求音频时即可获得访问. 所有音频配置都生活在这个容器中,这使得用户可以在不接触主机的情况下调整PulseAudio. `ha audio` 显示设备并设置默认值 。

## 国 际 {#cli}

CLI插件是`ha`命令行,由[Home Assistant/护理](https://github.com/home-assistant/cli)寄存器构建. 在 Home Assistant OS 是控制台上的登录 shell : 主机在登录时运行, 见 [调试主机](/os/operating-system/debugging#the-local-console) 。 插件寄存器只包 CLI 。 命令本身的更改会转到 cli 寄存器 。

## 多播 {#multicast}

多播插件在主机网络上运行[复制器](https://github.com/pvizeli/mdns-repeater). 它重复了主机网络和`hassio`网络之间的mDNS流量,因此发现工作跨越了这个边界. 可通过Supervisor API关闭。

## 观察员 {#observer}

观察者是一个小型的网络服务器,写于Go,位于主机4357号端口. 它显示 Supervisor 是否运行健康, 及其日志 。 它和 Supervisor 故意分开运行 : 当 Supervisor 或 Core 已下线时, 观察者就是用户如何仍然看到发生了什么.

## 正在处理插件 {#working-on-a-plugin}

每个插件寄存器都会构建一个容器图像,大多来自`Dockerfile`和一个`rootfs/`文件夹,几个有开发容器. 大多数插件都有`ha <plugin>`的命令固然可以显示它们的日志,重新启动它们,或者更新它们,比如`ha dns logs`或者`ha audio restart`.

要尝试自己会带来一个设备,为设备的架构构建图像,并用图像名称标记它,并 史上插件运行的版本(`docker ps`在主机上显示). 然后重新启动插件 。 方法与[在真实系统中测试 Supervisor](/os/supervisor/development#test-on-a-real-system)相同. 记住 Supervisor 自动更新插件, 当新版本出来时会替换您的构建 。
