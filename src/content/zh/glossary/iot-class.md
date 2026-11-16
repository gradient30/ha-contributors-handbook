---
title: IOT 类
description: 集成如何获得其数据:本地或从云,通过投票或推. 设于表里.
sidebarGroup: 核心与集成
term:
  code:
  - '"iot_class" in manifest.json'
  related:
  - manifest
  - polling
  autolink:
  - IoT class
  - IoT classes
---

# IOT 类 {#iot-class}

- 代码 : `"iot_class" in manifest.json`

IOT课告诉用户在建立集成之前, 最常见的是`local_push`,`local_polling`,`cloud_push`和`cloud_polling`.

## 相关条件 {#related-terms}

- [声明](/glossary/manifest):一个集成的`manifest.json`文件:其域名,集成所有者,要求,以及如何发现.
- [投票](/glossary/polling):询问设备或服务在一个间隔上的新数据. 与此相反的是推,当某事发生变化时设备会在那里发送更新.
