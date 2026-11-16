---
title: 一体化
description: 将 Home Assistant 连接到设备、 服务或协议, 或者添加自动化等功能的代码包 。
sidebarGroup: 核心和一体化
term:
  aliases:
  - integrations
  code:
  - homeassistant/components/<domain>/
  formerly:
  - component
  related:
  - domain
  - manifest
  - config-entry
  - platform
  - custom-integration
  autolink:
  - integration
  - integrations
---

# 一体化 {#integration}

- 代码 : `homeassistant/components/<domain>/`
- 还:一体化
- 原为:组件(旧名:不要在新文本中使用)

几乎所有的Home Assistant Core都是整合. 一些连接到Home Assistant之外的东西,比如飞利浦·休或Z-Wave. 其他部分是其他集成使用的组成部分,如`light`,`sensor`,或`automation`.

每个集成都生活在自己的文件夹中,以其[域名](/glossary/domain)命名,并以[显示](/glossary/manifest)描述自己. 用户在UI中添加了大多数集成,其中包含[配置流量](/glossary/config-flow).

代码在位置上仍然使用旧名:集成在 [`homeassistant/components/`](https://github.com/home-assistant/core/tree/dev/homeassistant/components) 中存在,一些函数表示组件. 在文字中,总是说融合.

## 相关条件 {#related-terms}

- [域名](/glossary/domain):一个集成的短而独特的标识符,如`hue`或`light`. 它也是每个实体身份证的第一部分。
- [声明](/glossary/manifest):一个集成的`manifest.json`文件:其域名,集成所有者,要求,以及如何发现.
- [配置条目](/glossary/config-entry):一个集成的设置实例,像一个惠桥,其配置 Home Assistant为它存储.
- 囤曙绚巷.羌盏.提供.提供.提供.提供.提供.提供.提供.提供.提供.提供.提供.提供.提供.提供.提供.提供.提供.提供.提供.提供.提供.提供.提供.提供.提供.诞.提供. Srebrenica.提供.提供嗓.提供.提供.提供.提供.还将.提供.提供.提供.提供.提供.提供.提供.提供.提供.提供.提供.提供.提供.提供.提供..提供..提供..提供.提供.提供..提供.提供.提供.提供.提供.提供..提供.提供.提供..提供....提供.提供.提供..提供.提供.提供.提供..提供.提供...提供.提供.提供........提供.提供..提供...........提供............提供.................................提供........ 也用于集成平台,插入另一个集成的文件.
- [之一就是自定义集成](/glossary/custom-integration):不是Home Assistant Core一部分的集成,由用户安装在`custom_components`文件夹中.
