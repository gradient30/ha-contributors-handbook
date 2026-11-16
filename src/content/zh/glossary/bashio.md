---
title: Bashio
description: 用于应用的 Bash 函数库, 用于读取应用的选项、 日志和与 Supervisor API 交谈的助手 。
sidebarGroup: 安装与系统
term:
  code:
  - 'bashio::'
  - hassio-addons/bashio
  related:
  - app
  - supervisor-api
  - s6-overlay
  autolink:
  - Bashio
---

# Bashio {#bashio}

- 代码:`bashio::`,`hassio-addons/bashio`

Bashio将大多数应用程序需要的东西捆绑起来,所以他们不再各自写,比如`bashio::config`读取一个选项. 它是官方Home Assistant基础图像和Home Assistant的一部分 社区 Apps 基础图像, 并生活在 [hassio-addons/bashio](https://github.com/hassio-addons/bashio) 寄存器 。 见[时尚参考](/apps/bashio)。

## 相关条件 {#related-terms}

- [应用](/glossary/app):在 Home Assistant OS 上运行于 Home Assistant 旁边的额外软件, 如 MQTT 经纪人或文件编辑器 。
- [Supervisor API](/glossary/supervisor-api): Supervisor的REST API,即Home Assistant Core,命令行,以及用于管理系统,应用程序,备份,和更新的应用程序.
- [S6 重叠](/glossary/s6-overlay): Home Assistant基础图像中的 init 系统。 它在其容器内启动、监视和停止应用程序的程序。
