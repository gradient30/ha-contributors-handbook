---
title: 记录条件
description: 青铜规则docs-条件:文档描述了整合的条件.
sidebarLabel: 文件条件
sidebarGroup: 铜
order: 9
---

# 记录条件 {#document-the-conditions}

此是铜法. 在`quality_scale.yaml`中,它被称为`docs-conditions`.

[Home Assistant.io](https://www.home-assistant.io/)上的用户文档描述每个[条件](/glossary/condition)提供的集成. 每个条件都得到自己的一页,从集成页面链接. 该页面解释条件检查内容,列出其选项,并显示如何从UI和YAML中使用.

## 为什么这很重要 {#why-it-matters}

一体化的条件比标准条件更具体,这使得没有帮助就难以使用。 每个条件单独一页保持集成页的可读性,同时仍然给每个条件空间用于其选项,其行为与多个目标,以及真实的例子.

## 示例 {#example}

每个条件都有自己的档案 在家里助理。 io寄存器, 在 [`source/_conditions/`](https://github.com/home-assistant/home-assistant.io/tree/current/source/_conditions) 中, 以全部条件命名, 如 `my_integration.is_door_open.markdown` :

```markdown
---
title: "Door is open"
condition: my_integration.is_door_open
domain: my_integration
description: "Tests if one or more doors are open."
---

The **Door is open** condition passes when one or more of your doors
are open. Use it to make sure an automation only runs while a door is
actually open, like turning off the heating.

{% include conditions/ui_header.md %}
```

引入后,页面会使用UI中的条件行走,其选项在UI中,在YAML中使用,在YAML中则使用. 其结尾为"好知"部分和真实的自动化实例. 整合页列出所有条件,其中一项条件包括:

```markdown
{% include integrations/conditions.md %}
```

包含所有选项块的完整页面布局在 [整合页面结构](/writing/reference/integration-page#triggers-conditions-and-actions) 中。 关于写页本身,请参见[综合文件](/writing/guides/integration).

## 如何检查 {#how-it-is-checked}

检查过 pull request 与整合相关的文件 。

## 例外 {#exceptions}

如果合并不提供任何条件,则不适用这一规则。

## 相关规则 {#related-rules}

- [文件行动](/core/quality-scale/docs-actions): 记录动作 。
- [文件触发](/core/quality-scale/docs-triggers):记录触发器。
