---
title: 融合拥有者
description: 负责列入清单的整编人员或小组,他们得到有关其问题的通知,并要求审查其pull request。
sidebarGroup: 核心与集成
term:
  aliases:
  - integration owners
  code:
  - codeowners (manifest)
  - CODEOWNERS
  formerly:
  - code owner
  related:
  - integration
  - manifest
  - pull-request
  - maintainer
  autolink:
  - integration owner
  - integration owners
---

# 融合拥有者 {#integration-owner}

- 代码:`codeowners (manifest)`,`CODEOWNERS`
- 此外:融合所有人
- 原为:代码所有者(旧名:别在新文本中使用).

整合所有者在整合表的 `codeowners` 字段中以 GitHub 手柄列出。 Hassfest 从这些列表生成 `CODEOWNERS` 文件 Home Assistant Core, 用于要求它们审查 。 当一个问题得到了他们的整合的标签, 机器人提到他们。

代码称它们为代码所有者:`codeowners`字段,`CODEOWNERS`文件,以及像`by-code-owner`这样的标签. 在关于融合的文本中,说融合所有者. "代码所有者"仍然符合一个不涉及集成的寄存器的`CODEOWNERS`文件,就像拥有前端部分的团队.

## 相关条件 {#related-terms}

- [一体化](/glossary/integration):将Home Assistant连接到设备,服务,或协议,或添加自动化等特性的代码包.
- [声明](/glossary/manifest):一个集成的`manifest.json`文件:其域名,集成所有者,要求,以及如何发现.
- [调用请求](/glossary/pull-request):在GitHub上请求将一个更改合并到一个寄存器中,在它进入之前要经过审查.
- [维护者](/glossary/maintainer): 可以在寄存器中批准和合并pull request的捐献者 。
