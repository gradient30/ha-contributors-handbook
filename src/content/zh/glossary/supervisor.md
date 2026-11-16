---
title: Supervisor
description: 好啊 Home Assistant OS 运行 Home Assistant Core 和 apps 的部分, 都在自己的容器里, 并处理它们的更新和备份
  。
sidebarGroup: 安装和系统
term:
  code:
  - home-assistant/supervisor
  - hassio
  related:
  - home-assistant-os
  - app
  - supervisor-api
  - supervisor-plugin
  - resolution-center
  autolink:
  - Supervisor
---



# Supervisor {#supervisor}
- 代码:`home-assistant/supervisor`,`hassio`

Supervisor有一个API,[Supervisor API](/glossary/supervisor-api),那个核心,前端,以及应用软件用来安装更新,制作备份,管理应用.

## 相关条件 {#related-terms}

- [Home Assistant OS](/glossary/home-assistant-os):为运行Home Assistant而制造的操作系统,带有Supervisor,app,和备份. 建议安装Home Assistant的方法 。
- [应用](/glossary/app):在 Home Assistant OS 上运行于 Home Assistant 旁边的额外软件, 如 MQTT 经纪人或文件编辑器 。
- [Supervisor API](/glossary/supervisor-api): Supervisor的REST API,即Home Assistant Core,命令行,以及用于管理系统,应用程序,备份,和更新的应用程序.
- [Supervisor 插件](/glossary/supervisor-plugin): A container the Supervisor runs for the system itself, like DNS or audio, that Home Assistant Core and apps share.
- [分辨率中心](/glossary/resolution-center): Supervisor 中发现系统问题的部分, 如低磁盘空间, 并为它们建议修正 。
