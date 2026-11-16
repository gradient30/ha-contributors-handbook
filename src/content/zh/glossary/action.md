---
title: 行动
description: 有些事情Home Assistant可以做,比如打开灯或者发送通知。 自动化,脚本,和仪表板执行动作.
sidebarGroup: 自动化和组织
term:
  aliases:
  - actions
  - perform an action
  code:
  - hass.services
  - services.yaml
  - ServiceCall
  - async_register
  formerly:
  - service
  - service call
  related:
  - automation
  - script
  - target
  - selector
---

# 行动 {#action}

- 在代码中:`hass.services`,`services.yaml`,`ServiceCall`,`async_register`
- 我们需要的是,
- 原为:服务,服务呼叫(旧名:别在新文本中使用).

整合记录动作,并在 `services.yaml` 中描述它们的字段 。 一个动作可以针对实体,设备,区域,地板,或标签.

动作过去被称为服务,在Home Assistant2024.8. 代码仍然使用旧名:`hass.services`,`services.yaml`,和`ServiceCall`. 在文字中,总是说动作,和"执行一个动作",而不是"召唤一个服务".

## 相关条件 {#related-terms}

- [自动化](/glossary/automation):当触发器发生并满足其条件时执行动作的规则,比如有人在家时在日落时打开灯光.
- [脚本](/glossary/script):可以从自动化,仪表板或语音运行的命名动作序列.
- 不过是一些工具。
- [选择器](/glossary/selector):描述一个字段需要什么样的值,比如一个实体,一个数字,或者一个时间,所以UI显示正确的控制.
