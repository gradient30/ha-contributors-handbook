---
title: 安全
description: 报告一个弱点, 并建造软件 保护它运行的家园。
---

# 安全 {#security}

锁、警报器、摄像头 和暖气的人。 Home Assistant中的安全错误是某人前门的缺陷. 这就是为什么这里的安全不是一个单独的团队的问题:它出现在每一个集成,每一个卡片,每一个应用程序,每一个依赖性突起中.

这个领域是每个贡献者的。 你会发现如何报告一个弱点, 在你写或审查的代码中要注意什么, 哪些检查已经有你的背心。

> [!IMPORTANT]
> 发现弱点了吗? 不要打开一个公有问题, pull request 或聊天信息 。 通过[安全咨询](https://github.com/home-assistant/core/security/advisories/new)私下报告。 见[报告脆弱性](/security/report-a-vulnerability) 包含什么和接下来会发生什么 。

## 这是给谁的 {#who-this-is-for}

- **娇安研究者和用户**谁发现的东西:从[报告脆弱性](/security/report-a-vulnerability)开始.
- **集成开发者**:您所写的代码运行在Core内部,可以访问一切. [融合指南](/security/guides/integrations) 覆盖证书、 证书、 编辑、 仅限管理员访问、 webhooks 和文件路径 。
- **Frontend开发者**:到达接口的名称,属性,和Markdown都可以来自任何地方. 见[前端未信任的内容](/security/guides/frontend).
- **App开发者**:您的应用程序在自己的容器中运行,在系统的其他部分旁边.见下表 [保护你的应用](/apps/guides/security) 和 [安全评级](/apps/reference/security-rating) 以及 [如果他们是安全的应用程序](/security/guides/apps) 中从过去的建议中吸取的教训 。
- 的进展情况 **companyion app开发者**:该应用程序持有用户的登录,所以任何能够让其自行行动的东西都是风险. 见[安全附带应用程序](/security/guides/companion-apps).
- **评论家**:在密码传到人们家之前,你是最后一双眼睛. 见[铭记安全审查](/security/guides/reviewing).

## 从这里开始 {#start-here}

- [你的第一次贡献](/security/first-contribution) : 请检查您对数据使用的整合的诊断, 这些数据不应该在其中 。
- [Home Assistant 如何处理信任](/security/how-it-works):谁Home Assistant信任,在哪里可以攻击,系统已经为你做什么了.
- [报告脆弱性](/security/report-a-vulnerability):如何报告,什么合格,什么预期。

## 指南 {#guides}

- 瑰([安全融合](/security/guides/integrations)):保证整合安全的图案和帮助者.
- [前端的不可信内容](/security/guides/frontend):逃跑,消毒,安全的联系。
- [安全应用程序](/security/guides/apps):关于应用和Supervisor的提示是什么。
- [安全伴侣应用程序](/security/guides/companion-apps):链接、导出组件、WebView和JavaScript桥。
- [依赖性和供应链](/security/guides/dependencies):什么Home Assistant问一个库,它如何检查。
- [铭记安全审查](/security/guides/reviewing): 在 pull request 中要寻找什么 。

## 参考 {#reference}

- [安全阖门](/security/reference/helpers):一页的每一个助手,为Core和前端.
- [自动安全检查](/security/reference/checks):检查代码、依赖和工作流程的工具。
- [过去的建议](/security/reference/advisories):每一次公开的咨询,按种类分组,有出错和教训.

## 相关 {#related}

- [认证](/core/internals/auth)和[权限](/core/internals/permissions):用户,符号,以及如何检查某人可以做什么.
- [诊断](/core/integrations/diagnostics):让用户共享数据,没有秘密.
- [保证您的 Home Assistant](https://www.home-assistant.io/docs/configuration/securing/):用户端,从密码到远程访问.

## 谁说话 {#who-to-talk-to}

- 淑薛:通过{抒叟遐磐寐几句倡,从不公开. 项目的[安全性.txt](https://www.home-assistant.io/.well-known/security.txt) 将`security@home-assistant.io` 列为联系人 。
- ** 写到 Home Assistant 的安全性: [安全政策](https://www.home-assistant.io/security/) 请您联系 [你好艰辛,](mailto:hello@home-assistant.io) 首先,可以检查所有的索赔。
- ** 关于写安全代码的问题** 这不是朔方: 在[Home Assistant Discord](https://www.home-assistant.io/join-chat/) 上的 [发展中国家**](https://discord.com/channels/330944238910963714/554842238073700352) 频道中, 或在您的 pull request 中 。 看不到频道吗? 在 **Channels & 角色** 下,选择 ** 我想贡献 dev 技能给 Home Assistant**}.
