---
title: 重新校正
description: 当一个配置条目无法再登录,而不再次设置时,该流程会向用户询问新的证书.
sidebarGroup: 核心与集成
term:
  aliases:
  - reauth
  code:
  - async_step_reauth
  - ConfigEntryAuthFailed
  related:
  - config-flow
  - config-entry
  autolink:
  - reauthentication
  - reauth
---

# 重新校正 {#reauthentication}

- 代码:`async_step_reauth`,`ConfigEntryAuthFailed`
- 又: 复发

当密码更改或令牌过期时,集成会提高`ConfigEntryAuthFailed`. Home Assistant 然后要求用户再次登录, 并保留配置项的其他所有内容 。

## 相关条件 {#related-terms}

- [配置流量](/glossary/config-flow):UI中设置集成并创建配置条目的步骤.
- [配置条目](/glossary/config-entry):一个集成的设置实例,像一个惠桥,其配置 Home Assistant为它存储.
