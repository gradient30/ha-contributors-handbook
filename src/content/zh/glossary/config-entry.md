---
title: 配置条目
description: 一个集成的设置实例,像一个惠桥,配置 Home Assistant 存储它。
sidebarGroup: 核心与集成
term:
  aliases:
  - config entries
  - entry
  code:
  - ConfigEntry
  - async_setup_entry
  - entry.runtime_data
  ui: 融合条目
  related:
  - config-flow
  - config-subentry
  - options-flow
  - integration
  - unique-id
  autolink:
  - config entry
  - config entries
---

# 配置条目 {#config-entry}

- 在代码中:`ConfigEntry`,`async_setup_entry`,`entry.runtime_data`
- 在UI:整合条目
- 又:配置条目,条目

当用户在 UI 中添加一个集成时, [配置流量](/glossary/config-flow) 创建一个配置条目 。 添加第二座桥会生成同一集成的第二个配置条目.

一个配置条目可以禁用,重新装入,并自行删除. 设置它的代码是`async_setup_entry`,运行时集成需要的任何东西,就像API客户端一样,都在`entry.runtime_data`中.

## 相关条件 {#related-terms}

- [配置流量](/glossary/config-flow):UI中设置集成并创建配置条目的步骤.
- {am [配置子条目](/glossary/config-subentry):用户自行添加和管理的配置条目的一部分,如连接到AI服务的集成的AI代理.
- [选项流](/glossary/options-flow):UI中改变现有配置条目选项的步骤,比如它经常投票.
- [一体化](/glossary/integration):将Home Assistant连接到设备,服务,或协议,或添加自动化等特性的代码包.
- [独一无二的ID](/glossary/unique-id):一个集成给一个实体或配置项的ID,它永远不会改变,所以Home Assistant在重启后承认它.
