---
title: 文件自动化实例
description: Gold rule docs-examples:文档给出了自动化实例或蓝图.
sidebarLabel: 文件实例
sidebarGroup: 黄金
order: 6
---

# 文件自动化实例 {#document-automation-examples}

这是黄金规则 在`quality_scale.yaml`中,它被称为`docs-examples`.

[Home Assistant.io](https://www.home-assistant.io/)上的集成页面显示几种与集成自动化的常见或有用的方法. 把它们作为 YAML [自动化](/glossary/automation) 示例, 或链接到 [蓝图](/glossary/blueprint) 。 蓝图可以生活在`source/blueprints/integrations`文件夹中的[Home Assistant.io仓库](https://github.com/home-assistant/home-assistant.io/tree/current/source/blueprints/integrations),也可以在论坛的[蓝图交换](https://community.home-assistant.io/c/blueprints-exchange)上.

保持它一小块。 集成页面不是每个自动化的集合 曾经有人写。

## 为什么这很重要 {#why-it-matters}

例子让用户从"它被设置"到"它做了一些有用的事情". 一个好的例子还表明,整合的实体和行动如何相互配合,这不仅仅是一个实体清单所能做到的。

## 示例 {#example}

````markdown
## Examples {#examples}

### Turn off the status LEDs at night {#turn-off-the-status-leds-at-night}

The status LEDs of the device are bright. This automation turns them off
at sunset.

{% details "Example YAML configuration" %}

```

雅姆尔
自动化 :
  - 十分重视这个,
    触发 :
      - 触发:太阳
        事件:日落
    动作 :
      - 簧片
        目标 :
          谚语

```

{% enddetails %}
```

`

参见 [写入集成文件](/writing/guides/integration) 和 [整合页面结构](/writing/reference/integration-page) 。

## 如何检查 {#how-it-is-checked}

在审查中检查过,通常在文件pull request上.

## 例外 {#exceptions}

不创建 Spec实体或提供动作的集成,或只扩展核心特性的集成,像备份位置一样,不受此规则的限制.
