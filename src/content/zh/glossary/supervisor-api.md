---
title: Supervisor API
description: Supervisor的REST API,即Home Assistant Core,命令行,以及用于管理系统,应用程序,备份,和更新的应用程序.
sidebarGroup: 安装与系统
term:
  code:
  - http://supervisor/
  - SUPERVISOR_TOKEN
  - hassio_api
  related:
  - supervisor
  - app
  - bashio
  autolink:
  - Supervisor API
---



# Supervisor API {#supervisor-api}
- 在代码中:`http://supervisor/`,`SUPERVISOR_TOKEN`,`hassio_api`

在应用程序内部,ئاري , API在 `http://supervisor/` , 而 Supervisor 在 `SUPERVISOR_TOKEN` 环境变量中给每个应用程序自己的令牌 。 应用程序可以调用什么取决于它在其配置中的要求,比如`hassio_api: true`.

使用过时的应用名称,如 `/addons`。 见[参考](/apps/supervisor-api).

## 相关条件 {#related-terms}

- [Supervisor](/glossary/supervisor): Home Assistant OS中运行Home Assistant Core和apps的部分,各自在自己的容器内,并处理它们的更新和备份.
- [应用](/glossary/app):在 Home Assistant OS 上运行于 Home Assistant 旁边的额外软件, 如 MQTT 经纪人或文件编辑器 。
- [Bashio](/glossary/bashio):用于应用的Bash函数库,有帮助者用于读取应用的选项,记录,和与Supervisor API交谈.
