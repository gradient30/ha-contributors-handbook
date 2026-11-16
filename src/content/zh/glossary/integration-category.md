---
title: 一体化类别
description: 集成是为了什么,比如照明或能源,所以人们可以通过它做什么来找到它,比如在网站上的集成页面上.
sidebarGroup: 核心和一体化
term:
  aliases:
  - integration categories
  code:
  - categories
  - ha_categories
  related:
  - integration
  - manifest
  - custom-integration
  - entity-category
  autolink:
  - integration category
  - integration categories
---

# 一体化类别 {#integration-category}

- 代码:`categories`,`ha_categories`
- 此外:一体化类别

集成在 `categories` 密钥 [显示](/core/integrations/manifest#categories) 中列出一个至三个类别 。 除了实体,系统和虚拟集成之外,核心中的每一个集成都有它们. 对于定制融合,它们是可选的。 核心整合的文档页在 `ha_categories` 和 [现在我先说](/writing/reference/front-matter) 的 {home-assistant.io 上列出了相同的文件页。 一个类可以有子类,比如`energy.ev_charging`. [一体化类别](/core/integrations/categories)都有,如何选择。

Home Assistant 其他东西也使用单词分类 。 两者不同:

- 在 Home Assistant 本身中创建的类别, 用于组织自动化, 脚本, 场景, 和帮助 。 这些人生活在类别登记册中,对于使用Home Assistant的每一个人来说都是一样。
- [实体类别](/glossary/entity-category) 标记一个实体为配置或诊断 。
- 在市场和HACS动作中,`category`是寄存器的类型:集成,仪表板插件,主题,或模板.

## 相关条件 {#related-terms}

- [一体化](/glossary/integration):将Home Assistant连接到设备,服务,或协议,或添加自动化等特性的代码包.
- [声明](/glossary/manifest):一个集成的`manifest.json`文件:其域名,集成所有者,要求,以及如何发现.
- [之一就是自定义集成](/glossary/custom-integration):不是Home Assistant Core一部分的集成,由用户安装在`custom_components`文件夹中.
- [实体类别](/glossary/entity-category):将一个实体标记为配置或诊断,所以它不会出现在设备的主要控制器旁边.
