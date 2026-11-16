---
title: 乌拉圭
description: Home Assistant OS的更新系统. 它在运行中的系统旁边安装了整个系统的新版本,因此当更新不起作用时,一个设备可以返回.
sidebarGroup: 安装与系统
term:
  aliases:
  - update bundle
  code:
  - .raucb
  - buildroot-external/ota/
  related:
  - home-assistant-os
  - buildroot
  - supervisor
  autolink:
  - RAUC
---

# 乌拉圭 {#rauc}

- 代码:`.raucb`,`buildroot-external/ota/`
- 还: 更新捆绑

Home Assistant OS有两个系统插槽。 [乌拉圭](https://rauc.io/) 写一个更新捆绑到未运行的插槽, 设备靴子插进去 我已经打开了 。 如果这样行不通,它就会回到它从哪里来的档位。 Supervisor 开始这些更新 。 见[更新系统](/os/operating-system/update-system)。

## 相关条件 {#related-terms}

- [Home Assistant OS](/glossary/home-assistant-os):为运行Home Assistant而制造的操作系统,带有Supervisor,app,和备份. 建议安装Home Assistant的方法 。
- [构建根](/glossary/buildroot): 工具Home Assistant OS是用它建的。 它从源头构建了一个完整的,小型的Linux系统,而不是从Ubuntu这样的发行开始.
- [Supervisor](/glossary/supervisor): Home Assistant OS中运行Home Assistant Core和apps的部分,各自在自己的容器内,并处理它们的更新和备份.
