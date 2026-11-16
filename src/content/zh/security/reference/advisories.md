---
title: 过去的建议
description: 每一个公布的Home Assistant的安保咨询,按种类分类,包括出错和给贡献者的教训。
order: 3
---

# 过去的建议 {#past-advisories}

Home Assistant 为每个符合[安全政策标准](/security/report-a-vulnerability#public-disclosure-and-cve-assignment)的有效弱点发表一个建议。 这页按种类分类,在一句话中说出了什么错误,并点出教训的名字. 每个咨询都链接到GitHub的全部细节,每个课程链接到涵盖它的指南.

列表本身,带有严重性,CVE,发现者,以及带有固定的版本,生活在[安全页面](https://www.home-assistant.io/security/#past-advisories)上. 这名单是正式的 此页面只会帮助您从中学习.

同样的几处错误不断出现。 读读符合你工作代码的组.

## 跨站点脚本 {#cross-site-scripting}

到达前端的数据作为HTML提供,因此一个精心制作的名称或消息可以在浏览器中运行任何查看它的人的代码.

| 日期 | 发生什么了? | 课程 |
| --- | --- | --- |
| 2026‑03‑27 | 在 [地图谢谢](https://github.com/home-assistant/core/security/advisories/GHSA-r584-6283-p7xc) 工具提示中, HTML 中的设备名称作为代码运行 。 | 名字是数据,从不标注. 让Lit制作,或者设定 `textContent` 。 见[前端](/security/guides/frontend#let-lit-do-the-escaping). |
| 2026‑03‑27 | 一个实体名称在 体现了 [算法的算法是,](https://github.com/home-assistant/core/security/advisories/GHSA-46j8-vpx8-6p72) 的工具提示中作为代码运行 。 | 另一张卡片中同样的错误:检查每个构建HTML字符串的地方. 见[前端](/security/guides/frontend#when-you-must-build-an-html-string). |
| 2025‑10‑14 | 一个实体名称在能量仪表板的 [图表工具提示](https://github.com/home-assistant/core/security/advisories/GHSA-mq77-rv97-285m) 中作为代码运行 。 名称可能来自集成的云服务,而不仅仅是用户. | 任何名称都可以来自外部,包括一个集成集的默认名称. 见[前端](/security/guides/frontend). |
| 2017‑10‑11 | 前端没有像在持续通知中那样对 [下调输出](https://github.com/home-assistant/frontend/pull/514) 进行消毒。 | 通过一个消毒器的Render Markdown。 今天是 `<ha-markdown>`。 见[前端](/security/guides/frontend#markdown) 。 |

## 登录和前端 {#login-and-the-frontend}

[2023年Cure53审计](https://www.home-assistant.io/blog/2023/10/19/security-audits-of-home-assistant/)的四项发现,全部固定在Home Assistant Core2023.9.

| 日期 | 发生什么了? | 课程 |
| --- | --- | --- |
| 2023‑10‑19 | 登录客户端发布的 `redirect_uri` 没有检查它的方案, 因此 [真的吗?](https://github.com/home-assistant/core/security/advisories/GHSA-jvxq-x42r-f7mv) 可以运行前端的代码 。 | 每个嗓门的URL在用作链接或重定向之前都会被检查其方案. 见[前端](/security/guides/frontend#links). |
| 2023‑10‑19 | 一个登录链接可以将授权代码发送给攻击者控制的[其它地点](https://github.com/home-assistant/core/security/advisories/GHSA-qhhj-7hrc-gqj5). | 重新定向目标需要与所属客户严格匹配. |
| 2023‑10‑19 | 登录链接中的参数决定了前端打开的 WebSocket 到哪个服务器, 因此链接可以 [连接到假服务器](https://github.com/home-assistant/core/security/advisories/GHSA-cr83-q7r2-7f5q) 。 | 绝不让 URL 参数选择前端信任的服务器 。 |
| 2023‑10‑19 | Home Assistant没有设置 `X-Frame-Options` 标题, 所以其他站点可以装入 [点击劫持](https://github.com/home-assistant/core/security/advisories/GHSA-935v-rmg9-44mw) 的框架 。 | 核心默认发送 {H几分钟} 。 不要绕着它工作。 |

## 不登录的结束点 {#endpoints-without-a-login}

一个没有问谁就回答的终点 在本地网络上不是登录 。

| 日期 | 发生什么了? | 课程 |
| --- | --- | --- |
| 2026‑06‑18 | HTTP 对遗产的视图 [Konnected 整合](https://github.com/home-assistant/core/security/advisories/GHSA-x84v-g949-293w) 已有 `requires_auth = False` , 并在 `POST` 和 `PUT` 上检查了一个符号, 但没有检查 `GET` 。 网络上的任何人都可以读取警报板的状态. 合并被取消. | 用 `requires_auth = False` 查看的每一种方法都检查请求本身 。 见[ũ](/security/guides/integrations#http-views). |
| 2023‑12‑14 | 登录页面向本地网络中打开 [所有用户账户](https://github.com/home-assistant/core/security/advisories/GHSA-jqpc-rc7g-vf83) 的任何人显示 。 | 登录前不要发布用户信息,甚至不能在本地网络上发布. |
| 2023‑10‑19 | 仅标为本地的 Webhooks 是 [可从互联网上获取](https://github.com/home-assistant/core/security/advisories/GHSA-wx3j-3v2j-rf45) 通过 Home Assistant Cloud 的远程连接, 现在为 Home Assistant Link , 它使请求看起来是本地的 。 | 请求来自何处,与谁寄的不一样.娄子 使用 `local_only` 从处理此案件的 Webhook 帮助器 。 见[ũ](/security/guides/integrations#webhooks). |

## 服务器侧请求伪造 {#server-side-request-forgery}

来电者的数据最终以Home Assistant自己发出的一份请求而告终,并附有自己的证书.

| 日期 | 发生什么了? | 课程 |
| --- | --- | --- |
| 2023‑10‑19 | `addon` 动作的 `hassio.addon_stdin` 字段被放入 Supervisor API 请求的路径, 所以一个呼叫者可以到达 [其他 Supervisor 终点](https://github.com/home-assistant/core/security/advisories/GHSA-4r74-h49q-rr3h) 。 | 验证进入 URL 或 路径的每个值,并采用严格的模式。 核心现在检查这个字段与弹痕模式。 见[ũ](/security/guides/integrations#treat-what-comes-in-as-untrusted). |

## 证书检查 {#certificate-checks}

| 日期 | 发生什么了? | 课程 |
| --- | --- | --- |
| 2025‑02‑18 | 当 `verify_ssl` 的 aiohttp 选项被 `ssl` 取代时, 一些集成和库 [直接传递旧值](https://github.com/home-assistant/core/security/advisories/GHSA-m3pm-rpgg-5wj6) 。 根据咨询, 关闭了证书检查。 | 共 和 国 长 见[ũ](/security/guides/integrations#keep-certificate-checks-on). |

## 应用程序和 Supervisor {#apps-and-the-supervisor}

| 日期 | 发生什么了? | 课程 |
| --- | --- | --- |
| 2026‑03‑27 | 在主机网络上的Apps服务[没有登录的结束点](https://github.com/home-assistant/core/security/advisories/GHSA-gh5m-4m97-c95h)在Supervisor的内部网络上,假设没有别的东西能够到达它. 本地网络上的设备可以。 | 绑定内部地址不是登录. 见[应用程序](/security/guides/apps#do-not-trust-the-network-alone). |
| 2023‑03‑08 | 攻击者可以绕过认证,通过Home Assistant到达[Supervisor API](https://github.com/home-assistant/core/security/advisories/GHSA-2j8f-h4mr-qr25). | 代理只转发明确列表中的内容 。 见[应用程序](/security/guides/apps#the-supervisor-api-bypass). |

## 伴侣应用 {#companion-apps}

使用该软件的操作器。 任何可以让应用操作 自己使用它 的标志。

| 日期 | 发生什么了? | 课程 |
| --- | --- | --- |
| 2026‑07‑31 | 其他的应用程序可以在Android应用中打开标签链接,它发送[标记扫描到服务器](https://github.com/home-assistant/core/security/advisories/GHSA-2xqv-hwrf-983f)而不询问用户. | 一个来自应用以外的伎俩需要用户的批准. 见{L0伎}. |
| 2026‑07‑31 | [iOS 应用程序](https://github.com/home-assistant/core/security/advisories/GHSA-j23v-9672-677j)的相同,通过通用链接. | 同样的教训,在两个平台。 见[辅助应用程序](/security/guides/companion-apps#ask-before-acting-on-a-link). |
| 2026‑07‑26 | 一个邀请链接可以开始对 [任何服务器](https://github.com/home-assistant/core/security/advisories/GHSA-68f4-97mf-f68w) 安装 Android app, 而无需显示地址 。 然后可以收集假登录页的密码 。 | 显示用户在信任之前将链接带入何处 。 见[辅助应用程序](/security/guides/companion-apps#show-which-server-you-connect-to). |
| 2026‑06‑25 | 内部 URL 的 iOS app [忽略家用无线网络列表](https://github.com/home-assistant/core/security/advisories/GHSA-cm5v-547m-qh5h) , 这样它就可以在任意网络上通过 plain HTTP 发送它的令牌 。 | 仅使用内部 `http:` URL 在用户标记为家的网络上 。 见[辅助应用程序](/security/guides/companion-apps#keep-the-internal-url-at-home). |
| 2026‑06‑17 | Android应用程序的[导出接收器](https://github.com/home-assistant/core/security/advisories/GHSA-77r5-pw5w-mgj3)接受了任何应用程序的地址更新,并将其作为真实位置发送到服务器. | 不导出组件 。 当某些东西必须能够达到时,只接受它所需要的一个动作,并放弃随之而来的数据. 见[辅助应用程序](/security/guides/companion-apps#keep-components-private). |
| 2026‑05‑11 | 两个应用程序的 JavaScript 桥像网页卡一样, 回答 [其他来源](https://github.com/home-assistant/core/security/advisories/GHSA-7jp2-p2fw-mgvf) 的框, 并将信件的回调名称放入它运行的代码 。 框中的页面可以获得访问符. | 只有服务器主帧对桥说话,消息中没有任何内容成为代码. 见[辅助应用程序](/security/guides/companion-apps#guard-the-javascript-bridge). |
| 2023‑10‑19 | Android app可以在其 WebView 中装入 [任意 URL](https://github.com/home-assistant/core/security/advisories/GHSA-jvpm-q3hq-86rg) 。 | WebView只装入用户的服务器. 见[辅助应用程序](/security/guides/companion-apps#load-only-the-server-in-the-webview). |
| 2023‑10‑19 | 一个链接或QR代码可以使iOS和macOS应用程序[呼叫动作](https://github.com/home-assistant/core/security/advisories/GHSA-h2jp-7grc-9xpp)在服务器上不询问. | 一个来自应用以外的伎俩需要用户的批准. 见{L0伎}. |

## 工作流量 {#workflows}

| 日期 | 发生什么了? | 课程 |
| --- | --- | --- |
| 2023‑10‑19 | 迥异的 GitHub 项目的动作将 pull request 的分支名称直接放入 shell 脚本, [表达式插入](https://github.com/home-assistant/core/security/advisories/GHSA-jff5-5j3g-vhqc) 。 | 从不将`${{ }}`表达式与外部数据放在`run:`步骤中。 见[依赖性和供应链](/security/guides/dependencies#what-went-wrong-before). |

## 相关 {#related}

- [报告脆弱性](/security/report-a-vulnerability): 如何报告,什么是合格。
- [铭记安全审查](/security/guides/reviewing) : 在哪里查看 pull request 。
