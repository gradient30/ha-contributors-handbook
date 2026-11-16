---
title: 安全应用程序
description: 关于嬷嬷和 Supervisor 的咨询 , 在 apps 区域的安全指南之上 。
sidebarLabel: 应用程序
order: 3
---

# 安全应用程序 {#secure-apps}

一个 [应用](/glossary/app) 在自己的容器中运行, 旁边是 Home Assistant 和 [Supervisor](/glossary/supervisor) 。 应用程序区域已经覆盖了如何保护应用程序安全:[保护你的应用](/apps/guides/security) 解释要问什么, AppArmor, 保护模式, API 角色和登录, [安全评级](/apps/reference/security-rating) 显示用户如何看待您的选择 。 从那里开始。

本页面添加了来自 [过去的建议](/security/reference/advisories#apps-and-the-supervisor) 的关于应用和 Supervisor 的教训 。

## 不要只相信网络 {#do-not-trust-the-network-alone}

apps中常见的模式:运行在主机网络上,并在Supervisor,`hassio`的内部网络中提供没有登录的端点. 设想是只有其他集装箱才能到达该地址。 2026年,一项咨询显示这个[事实并非如此](https://github.com/home-assistant/core/security/advisories/GHSA-gh5m-4m97-c95h). 本地网络上的设备可以通过主机向内部地址添加一个路径,直接到达这些端点. 咨询在终端应用中命名 shell, 以及 WebSocket 另外两个的API.

Supervisor 202.6.03.2 为每次安装都固定了这一点:它增加了关于将流量降低到网络网关地址的主机的防火墙规则,除非它来自网络本身或主机.

教训超越了那一个固定。 当一个结束点听不是登录时。

- 在每一个端点上登入可以改变某种东西,或者显示某种隐私的东西. 使用 [Home Assistant 用户](/apps/guides/security#use-home-assistant-users) 代替自己的 。
- 对于网页接口,请使用[入侵](/apps/guides/ingress),并且只接受Supervisor在`172.30.32.2`的连接。Home Assistant然后处理登录。
- 只当您的应用程序真的需要时使用主机网络 。 这也降低了[安全评级](/apps/reference/security-rating)。

## Supervisor API 绕行 {#the-supervisor-api-bypass}

2023年,一个咨询显示攻击者可以绕过认证并通过Home Assistant,远程到达[Supervisor API](https://github.com/home-assistant/core/security/advisories/GHSA-2j8f-h4mr-qr25). API可以安装更新,管理应用程序和备份. [通知](https://www.home-assistant.io/blog/2023/03/08/supervisor-security-disclosure/)表示问题自2017年Supervisor推出以来就一直存在.

Core 和 Supervisor 中的修正显示两种模式, 适用于任何转发请求的应用程序 :

- ** 只向清单上的内容前进。 ** Core 中的 Supervisor API 的代理服务器现在只转发匹配明确列表的路径, 一个没有登录的请求列表和一个管理员列表 。 其他的都被拒绝了
- 检查前的十进制 Core拒绝解码时更改的路径. Supervisor 解码路径和查询字符串, 必要时, 在它检查它们像`../` 这样的模式之前。

同年的相关咨询显示一条 联合国外部数据构建的路径: `addon` `hassio.addon_stdin` 的 `addon` 字段 `hassio.addon_stdin` 的动作最终在 [请求 Supervisor API](https://github.com/home-assistant/core/security/advisories/GHSA-4r74-h49q-rr3h) 的路径中 。 核心现在检查球场 与严格的模式的弹壳。 如果您的应用程序从输入中构建了 URL 或路径, 请以同样的方式检查该输入 。

## 询问最小的角色 {#ask-for-the-smallest-role}

Supervisor API保护自己,但你的应用 持有它的一个标志。 如果你的应用被接管了 攻击者会得到那个标志允许的 选择最小的 [API 角色](/apps/guides/security#api-roles) 有效, 只打开 `hassio_api` 、 `homeassistant_api` 或 `auth_api` 。

## 相关 {#related}

- [保护你的应用](/apps/guides/security):应用区全向导.
- [安全评级](/apps/reference/security-rating):每个选择如何改变评分.
- [过去的建议](/security/reference/advisories):每一次咨询,按种类分组.
