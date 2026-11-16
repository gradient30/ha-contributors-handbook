---
title: 选项流
description: UI中改变现有配置条目选项的步骤,
sidebarGroup: 核心和一体化
term:
  code:
  - OptionsFlow
  - entry.options
  ui: 配置
  related:
  - config-flow
  - config-entry
  - reconfigure-flow
  autolink:
  - options flow
  - options flows
---

# 选项流 {#options-flow}

- 代码:`OptionsFlow`,`entry.options`
- 在用户界面中: 配置

选项是用户可以随时更改而无需再次设置集成的设置. 连接所需的设置, 像主机一样, 属于配置项本身, 用 [重新配置流量](/glossary/reconfigure-flow) 更改 。

## 相关条件 {#related-terms}

- [配置流量](/glossary/config-flow):UI中设置集成并创建配置条目的步骤.
- [配置条目](/glossary/config-entry):一个集成的设置实例,像一个惠桥,其配置 Home Assistant为它存储.
- [重组流量](/glossary/reconfigure-flow): 改变配置项设置的流, 如其主机, 而不删除和再次添加 。
