---
title: Supervisor 插件
description: Supervisor 运行于系统本身的容器, 如 DNS 或 音频 Home Assistant Core 和 apps 共享 。
sidebarGroup: 安装和系统
term:
  aliases:
  - plugin
  - plugins
  code:
  - supervisor/plugins/
  - plugin-dns
  - plugin-audio
  related:
  - supervisor
  - home-assistant-os
  autolink:
  - Supervisor plugin
  - Supervisor plugins
---

# Supervisor 插件 {#supervisor-plugin}

- 在代码中:`supervisor/plugins/`,`plugin-dns`,`plugin-audio`
- 还有:插件、插件

有五个:DNS,音频,命令行(CLI),多播,以及观察者. 每一个都拥有自己的仓库,如Home Assistant/插座。 用户不安装或移除它们,并且 Supervisor 不断更新它们 。 见[插件](/os/supervisor/plugins).

## 相关条件 {#related-terms}

- [Supervisor](/glossary/supervisor): Home Assistant OS中运行Home Assistant Core和apps的部分,各自在自己的容器内,并处理它们的更新和备份.
- [Home Assistant OS](/glossary/home-assistant-os):为运行Home Assistant而制造的操作系统,带有Supervisor,app,和备份. 建议安装Home Assistant的方法 。
