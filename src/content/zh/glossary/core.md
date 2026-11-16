---
title: Home Assistant Core
description: Python 应用程序位于 Home Assistant 的核心, 及其所有集成, 在Home Assistant/ 核心存储器中 。
sidebarGroup: 核心与集成
term:
  aliases:
  - Core
  code:
  - homeassistant/
  related:
  - integration
  - event-loop
  - home-assistant-os
  - frontend
  autolink:
  - Home Assistant Core
---



# Home Assistant Core {#home-assistant-core}
- 代码 : `homeassistant/`
- 还: 核心

核心运行事件循环,状态机器,注册,以及每一个集成. Home Assistant的每一个安装都运行着Core, 不管它绕着它运行。

当人们在谈话中说"核心"时,通常是指这个寄存器和从事这项工作的人. 在文本中,第一次写Home Assistant Core.

## 相关条件 {#related-terms}

- [一体化](/glossary/integration):将Home Assistant连接到设备,服务,或协议,或添加自动化等特性的代码包.
- [事件循环](/glossary/event-loop):运行Home Assistant Core的星环. 代码屏蔽它, 就像在网络上等待没有`await`, 停止其他一切。
- [Home Assistant OS](/glossary/home-assistant-os):为运行Home Assistant而制造的操作系统,带有Supervisor,app,和备份. 建议安装Home Assistant的方法 。
- [前端](/glossary/frontend):用 Lit 和 TypeScript 建造的 Home Assistant 的网页界面, 位于家用辅助/ 前端寄存器中 。
