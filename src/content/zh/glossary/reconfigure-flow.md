---
title: 重组流量
description: 改变配置条目的设置的流, 如其主机, 而不删除并再次添加它 。
sidebarGroup: 核心和一体化
term:
  aliases:
  - reconfigure
  code:
  - async_step_reconfigure
  ui: 重新配置
  related:
  - config-flow
  - options-flow
  - config-entry
  autolink:
  - reconfigure flow
  - reconfigure flows
---

# 重组流量 {#reconfigure-flow}

- 代码 : `async_step_reconfigure`
- 在UI中:重新配置
- 另外: 重新配置

删除和添加一个配置项再次丢失用户给其实体和设备的名称、区域和其他设置。 重新配置的流能保持它们

## 相关条件 {#related-terms}

- [配置流量](/glossary/config-flow):UI中设置集成并创建配置条目的步骤.
- [选项流](/glossary/options-flow):UI中改变现有配置条目选项的步骤,比如它经常投票.
- [配置条目](/glossary/config-entry):一个集成的设置实例,像一个惠桥,其配置 Home Assistant为它存储.
