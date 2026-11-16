---
title: 发现
description: 寻找设备和服务,比如在网络上或超过Bluetooth,所以Home Assistant可以提供设置.
sidebarGroup: 核心和一体化
term:
  aliases:
  - discovered
  code:
  - zeroconf
  - ssdp
  - dhcp
  - bluetooth
  - usb
  - async_step_zeroconf
  ui: 发现
  related:
  - config-flow
  - manifest
---

# 发现 {#discovery}

- 代码:`zeroconf`,`ssdp`,`dhcp`,`bluetooth`,`usb`,`async_step_zeroconf`
- 在UI:发现
- 还发现:

整合列表中列出了如何找到其设备,如mDNS(`zeroconf`),SSDP,DHCP,Bluetooth或USB. 当 Home Assistant 找到匹配时, 它会启动集成的配置)( config flow), 并显示发现的设备 。

## 相关条件 {#related-terms}

- [配置流量](/glossary/config-flow):UI中设置集成并创建配置条目的步骤.
- [声明](/glossary/manifest):一个集成的`manifest.json`文件:其域名,集成所有者,要求,以及如何发现.
