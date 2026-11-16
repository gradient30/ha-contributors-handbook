---
title: 连接核心到 Supervisor
description: 运行 Home Assistant Core 从您的开发环境对一个真实的 Supervisor , 来进行散列集成 。
sidebarGroup: 指南
order: 3
---

# 连接核心到 Supervisor {#connect-core-to-a-supervisor}

Home Assistant Core通过 `hassio` 集成 Supervisor 与 Supervisor 交谈, 在 [`homeassistant/components/hassio/`](https://github.com/home-assistant/core/tree/dev/homeassistant/components/hassio) 。 要进行这种整合,你需要从你的发展环境中找到一个真正的Supervisor。 [核心发展环境](/core/development/environment)有前半部分。 此页面添加 Supervisor 。

## 访问 Supervisor API {#get-access-to-the-supervisor-api}

Supervisor API 需要一个符号 。 **Remote API 代理** app给你一个,并让API从设备外部到达:

1. 将 [开发应用程序存储器](https://github.com/home-assistant/apps-development) 添加到运行 Supervisor 的设备的应用商店 。 可以是测试设备,也可以是[Supervisor 开发容器](/os/supervisor/development)。
2. 安装 **Remote API 代理** app,并选择 **Start**.
3. 代币出现在应用程序的日志中.

应用程序需要在工作期间继续运行. 它在东道主的8880号港口听.

代理代币拥有比代币Core在制作中获得的权利略少. 如果您需要真实的,请在主机外壳上看到 [调试主机](/os/operating-system/debugging) :

```shell
docker inspect homeassistant | grep SUPERVISOR_TOKEN
```

任何符号在重启或更新后都可以改变 。

## 启动核心对它 {#start-core-against-it}

`hassio` 集成通过两个环境变量找到Supervisor 。 启动 Core 时设定 :

```shell
SUPERVISOR=192.168.1.100:8880 SUPERVISOR_TOKEN=abcdefgh1234 hass
```

- `SUPERVISOR`是设备的地址,带有代理应用程序的端口.
- `SUPERVISOR_TOKEN` 是应用程序日志上的符号 。

您的核心正在装入 `hassio` 集成, 并显示该设备的应用程序、 备份和系统设置 。

## 前端 {#the-frontend}

前端通过 Core 到达 Supervisor,该核心为管理员用户代理 Supervisor API. 因此,用这样连接的Core,一个[前端开发设置](/frontend)也指向了您与Supervisor的Kore的作品.
