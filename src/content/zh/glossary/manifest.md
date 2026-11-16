---
title: 声明
description: 驸马 `manifest.json` 集成文件:其域名,集成所有者,要求,以及如何发现.
sidebarGroup: 核心和一体化
term:
  code:
  - manifest.json
  related:
  - integration
  - requirement
  - integration-owner
  - discovery
  - iot-class
  autolink:
  - manifest.json
---

# 声明 {#manifest}

- 代码 : `manifest.json`

Home Assistant在装入任何集成代码前读出该清单。 它告诉哪些其他的集成需要首先设置,哪些Python包要安装,集成是否有配置流,以及在哪些网络或公共汽车上可以发现.

运算表也是集成的[IOT 类](/glossary/iot-class)和[质量尺度](/glossary/quality-scale)的设置地点.

## 相关条件 {#related-terms}

- [一体化](/glossary/integration):将Home Assistant连接到设备,服务,或协议,或添加自动化等特性的代码包.
- [要求](/glossary/requirement):太棒了 PyPI 的 Python 软件包, 一个集成需要的, 在其表单中以固定版本列出 。
- [融合拥有者](/glossary/integration-owner):负责合并的个人或团队,列于其清单中,他们得到关于其问题的通知,并要求审查其pull request。
- [发现](/glossary/discovery): 查找设备与服务, 如在网络上或超过Bluetooth, 因此Home Assistant 可以提供设置 。
- [IOT 类](/glossary/iot-class):整合如何获得其数据:本地或从云,通过投票或推. 设于表里.
