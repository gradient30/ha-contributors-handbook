---
title: 配置流量
description: UI中设置集成并创建配置条目的步骤.
sidebarGroup: 核心与集成
term:
  aliases:
  - config flows
  code:
  - ConfigFlow
  - config_flow.py
  - async_step_user
  related:
  - config-entry
  - options-flow
  - reauthentication
  - reconfigure-flow
  - discovery
  autolink:
  - config flow
  - config flows
---

# 配置流量 {#config-flow}

- 在代码中:`ConfigFlow`,`config_flow.py`,`async_step_user`
- 又: 配置流量

一个配置流程向用户询问它需要什么,比如一个主机和一个密码,检查它,并创建一个[配置条目](/glossary/config-entry). 它设置了[唯一标识](/glossary/unique-id),所以同一设备不能被添加两次.

当一个设备是 [发现](/glossary/discovery) 时, 配置流也可以由自己开始 。 用户仅确认。

连接到设备或服务的新集成设置有配置流,而不是YAML.

## 相关条件 {#related-terms}

- [配置条目](/glossary/config-entry):一个集成的设置实例,像一个惠桥,其配置 Home Assistant为它存储.
- [选项流](/glossary/options-flow):UI中改变现有配置条目选项的步骤,比如它经常投票.
- [重新校正](/glossary/reauthentication):当一个配置条目无法再登录而未再次设置时,该流程会要求用户提供新的证书.
- [重组流量](/glossary/reconfigure-flow): 改变配置项设置的流, 如其主机, 而不删除和再次添加 。
- [发现](/glossary/discovery): 查找设备与服务, 如在网络上或超过Bluetooth, 因此Home Assistant 可以提供设置 。
