---
title: Home Assistant 如何处理信任
description: 谁Home Assistant信任,哪里可以攻击它, 和系统已经做 保护它运行的家园。
sidebarLabel: 工作原理
order: 2
---

# Home Assistant 如何处理信任 {#how-home-assistant-handles-trust}

控制锁、警报器、摄像头和暖气, Home Assistant的安全问题是某人前门的问题。 此页面解释了下面酥皮姥姥的模型适用范围: 谁 Home Assistant 信任, 在哪里可以攻击, 在代码运行前, 哪些保护已经到位 。 [指南](/security/guides) 把它变成你写代码的练习 。

## 谁Home Assistant信任 {#who-home-assistant-trusts}

| 谁 | 信任过 |
| --- | --- |
| ** 行政人员** | 一切减缓贫穷。 他们并行安装自定义集成已提交的日关于运行代码的应用程序,并阅读每个设置. |
| ** 用户** | 利用家:看国家,执行行动. 不改变设置 。 |
| ** 只读用户** | 见诸州. |
| ** 任何其他人** | 没什么 除了一个网路识别码,这是自己的许可. 见[网点](/architecture/connections). |

这些角色塑造了界面和API提供的内容,但它们并不是安全边界. {ئاري { { [安全政策](https://www.home-assistant.io/security/)表示 Home Assistant 假设每个登录用户都是信任的,不执行用户权限,所以登录用户获得更多权利的,不会算作一种脆弱性.

在 Home Assistant 内运行的代码是完全信任的 。 A [自定义集成](/glossary/custom-integration) 是 Python 在和 Core 相同的过程中, 可以做 Core 能做的 。 [应用](/apps/how-apps-work)在自己的容器中运行,但可以要求广泛的访问. 安装其中任一是管理员的选择, Home Assistant 为此警告用户自定义集成 。

代码中最重要的线是管理员和其他人之间的线条. 见[认证](/core/internals/auth)和[权限](/core/internals/permissions)。

## Home Assistant 可以攻击的地方 {#where-home-assistant-can-be-attacked}

- ** 它是网络服务器。 ** 许多家庭通过互联网可以到达Home Assistant。 不需要登录的每一个端点,每个端点都做一个门.
- ** 来自设备和服务的数据。 ** 一个集成读取来自网络,云服务或设备的数据. 这些数据可能是错误的,或者是故意的。
- ** 附属关系。 ** 每个 [所需经费](/glossary/requirement) 是运行在 Core 中的代码 。 一个已妥协的库 Home Assistant 。
- **用户自己的设置**,像一个向错误标题转发的反向代理. Home Assistant不能修复这些,但它可以拒绝相信它不应该相信的东西.

## 已经做什么 Home Assistant {#what-home-assistant-already-does}

- 每个请求都需要一个有效的代号,除了webhooks和一些故意公开的端点,比如登录页面.
- 失败的登录会被报告给用户,从一个地址重复失败的登录会导致禁用,当用户打开时.
- 使用路径诡计或可疑字节的请求在达到任何整合之前都会被拒绝.
- 在反向代理后,转发地址只能从用户配置的代理中信任.
- 共享的网络会话, 从`async_get_clientsession` 检查 SSL 证书, 并拒绝从 Internet 重定向到本地机器 。
- 在用户给出的路径上读取或撰写文档的特征,如拍摄相机快照或将文件附加到通知中,对照用户允许的文件夹(`allowlist_external_dirs`)检查路径. 这是一个检查这些特性的调用,而不是沙盒:一个集成运行与Core相同的文件访问.

这些保护被构建为Home Assistant. 它们不涵盖你自己的代码 用它得到的数据, 或它的访问。 该部分由你决定, [安全](/security)区域显示如何, 每一种贡献。
