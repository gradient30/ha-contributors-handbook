---
title: 记录行动
description: 青铜规则docs-actions:文档描述了集成的动作.
sidebarLabel: 文件行动
sidebarGroup: 青铜
order: 8
---

# 记录行动 {#document-the-actions}

此是铜法. 在`quality_scale.yaml`中,它被称为`docs-actions`.

[Home Assistant.io](https://www.home-assistant.io/)上的用户文档描述每个[动作](/glossary/action)的整合添加:它做什么,以及每个字段的含义.

## 为什么这很重要 {#why-it-matters}

动作做标准实体无法做的事情, 例如获取一个调度或发送带有选项的命令 。 这使得它们强大,但也比开灯更难使用. 没有文档,用户必须猜到哪些字段ổ,哪些字段需要,以及反应是什么样子.

## 示例 {#example}

每个动作都会在Home Assistant那里得到自己的文件. io寄存器,在[`source/_actions/`](https://github.com/home-assistant/home-assistant.io/tree/current/source/_actions)中,以完整动作命名,如`my_integration.get_schedule.markdown`. 文件成为自己的页面 :

```markdown
---
title: "Get schedule"
action: my_integration.get_schedule
domain: my_integration
description: "Gets the heating schedule of a thermostat."
---

The **Get schedule** action returns the heating schedule that is stored
on your thermostat.

{% include actions/ui_header.md %}
```

然后,综合网页列出其所有行动,其中包含一项,从这些文件中建立清单:

```markdown
{% include integrations/actions.md %}
```

一个动作页面的完整布局,包含UI和YAML部分以及选项块,在[整合页面结构](/writing/reference/integration-page#triggers-conditions-and-actions)中. 关于写页本身,请参见[综合文件](/writing/guides/integration).

## 如何检查 {#how-it-is-checked}

检查过 pull request 与整合相关的文件 。

## 例外 {#exceptions}

如果合并没有增加任何自己的行动,则不适用本规则.

## 相关规则 {#related-rules}

- [文件触发](/core/quality-scale/docs-triggers):记录触发器。
- [文件条件](/core/quality-scale/docs-conditions): 记录条件。
