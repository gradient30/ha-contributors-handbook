---
title: 之一就是自定义集成
description: 一个不属于Home Assistant Core的集成,由用户安装在`custom_components`文件夹中.
sidebarGroup: 核心和一体化
term:
  aliases:
  - custom integrations
  - custom component
  code:
  - custom_components/
  related:
  - integration
  - backward-incompatible-change
  - custom-card
  - marketplace
  autolink:
  - custom integration
  - custom integrations
---

# 之一就是自定义集成 {#custom-integration}

- 代码 : `custom_components/`
- 另外:自定义集成,自定义组件

任何人都可以写一个自定义的集成,它与其他的集成一样有效. 该项目不审查它们,在Home Assistant Core中的变化可以打破它们,这就是为什么在博客上宣布开发者向后兼容的更改的原因.

自定义集成需要 `version` 在其表单中 。 用户从2026.11开始,通过[市场](/glossary/marketplace)找到并安装了其中的许多,它们被建在Home Assistant中. 在此之前,市场是[HACS](/glossary/hacs),一个自定义整合本身. 要发布一个,请参见 [自定义集成](/marketplace/guides/integrations) 在市场区。 这也是开始新整合的建议方式,见[我发誓它属于核心](/core/integrations/create#does-it-belong-in-core)。

## 相关条件 {#related-terms}

- [一体化](/glossary/integration):将Home Assistant连接到设备,服务,或协议,或添加自动化等特性的代码包.
- [向后兼容的更改](/glossary/backward-incompatible-change):一个需要用户或开发者改变自己侧面的东西的更改,比如他们的配置或他们的自定义集成.
- [自定义卡](/glossary/custom-card):不是前端部分的卡,由用户从JavaScript文件中加载.
- [市场](/glossary/marketplace): Home Assistant中用户找到并安装社区定制集成,仪表盘卡,主题,模板宏的地方. 始建于2026.11路.
