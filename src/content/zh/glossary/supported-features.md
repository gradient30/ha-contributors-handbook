---
title: 支持的特性
description: 一个实体设定的数来表示它所支持的类型中的哪些特征,比如可以设置到一个位置的封面.
sidebarGroup: 实体与设备
term:
  code:
  - supported_features
  - CoverEntityFeature
  - LightEntityFeature
  related:
  - entity
  - action
  autolink:
  - supported features
---

# 支持的特性 {#supported-features}

- 在代码中:`supported_features`,`CoverEntityFeature`,`LightEntityFeature`

每个功能都有点,从像`CoverEntityFeature`这样的enum. 前端只显示支持特性的控件,而Home Assistant只允许匹配动作.

## 相关条件 {#related-terms}

- [六方会谈](/glossary/entity):有一件事Home Assistant可以显示,测量,或者控制,比如灯光,温度传感器,或者开关. 每个实体都有国家。
- [行动](/glossary/action):有些事情Home Assistant可以做,比如打开灯或者发送通知. 自动化,脚本,和仪表板执行动作.
