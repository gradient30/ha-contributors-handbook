---
title: S6 重叠
description: Home Assistant基础图像中的 init 系统 。 它在其容器内启动、监视和停止应用程序的程序。
sidebarGroup: 安装和系统
term:
  aliases:
  - s6-overlay
  - S6
  code:
  - /init
  - /etc/s6-overlay/s6-rc.d/
  related:
  - app
  - bashio
  autolink:
  - S6 overlay
---

# S6 重叠 {#s6-overlay}

- 代码:`/init`,`/etc/s6-overlay/s6-rc.d/`
- 另外:S6重叠,S6

Docker每个容器运行一个命令. [S6 重叠](https://github.com/just-containers/s6-overlay) 让一个 实际上按正确的顺序运行几个程序: 首先设置一个步骤,然后程序崩溃时重新启动 。 碱性图像使其`/init`成为切入点,所以一个app只添加其服务定义. 见[使用 S6 覆盖运行服务](/apps/guides/s6-overlay)。

## 相关条件 {#related-terms}

- [应用](/glossary/app):在 Home Assistant OS 上运行于 Home Assistant 旁边的额外软件, 如 MQTT 经纪人或文件编辑器 。
- [芭蕉](/glossary/bashio):用于应用的Bash函数库,有帮助者用于读取应用的选项,记录,和与Supervisor API交谈.
