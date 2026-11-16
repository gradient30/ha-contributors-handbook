---
title: 构建根
description: 工具 Home Assistant OS 与 。 它从源头构建了一个完整的,小型的Linux系统,而不是从Ubuntu这样的发行开始.
sidebarGroup: 安装和系统
term:
  code:
  - buildroot/
  - buildroot-external/
  related:
  - home-assistant-os
  - rauc
  autolink:
  - Buildroot
---

# 构建根 {#buildroot}

- 代码:`buildroot/`,`buildroot-external/`

home-assistant/operating-system presidents has [构建根](https://buildroot.org/) as a Git 子模块,并保留了 Home Assistant OS 所特有的一切, 如 棋盘配置和包, 在 [`buildroot-external/`](https://github.com/home-assistant/operating-system/tree/dev/buildroot-external) 中 。 见[构建 Home Assistant OS](/os/operating-system/build).

## 相关条件 {#related-terms}

- [Home Assistant OS](/glossary/home-assistant-os):为运行Home Assistant而制造的操作系统,带有Supervisor,app,和备份. 建议安装Home Assistant的方法 。
- [乌拉圭](/glossary/rauc): Home Assistant OS的更新系统. 它在运行中的系统旁边安装了整个系统的新版本,因此当更新不起作用时,一个设备可以返回.
