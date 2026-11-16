---
title: 要求
description: 一个来自 PyPI 的 Python 软件包, 一个集成需要, 在其运单中以固定版本列出 。
sidebarGroup: 核心与集成
term:
  aliases:
  - requirements
  - dependency
  code:
  - '"requirements" in manifest.json'
  related:
  - manifest
  - integration
---

# 要求 {#requirement}

- 代码 : `"requirements" in manifest.json`
- 还:需求、依赖性

向特定设备或服务说话的代码属于PyPI上的库,而不是集成中. 整合将库列为一项要求, 并在需要时安装 Home Assistant 。

要求被固定在一个准确的版本,所以每个安装都运行同一个代码.

## 相关条件 {#related-terms}

- [声明](/glossary/manifest):一个集成的`manifest.json`文件:其域名,集成所有者,要求,以及如何发现.
- [一体化](/glossary/integration):将Home Assistant连接到设备,服务,或协议,或添加自动化等特性的代码包.
