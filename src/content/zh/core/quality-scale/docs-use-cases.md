---
title: 文件使用案例
description: 'Gold 规则 Docs- use- cases: 文档显示您可以在整合中做些什么 。'
sidebarLabel: 文档使用文件
sidebarGroup: 金
order: 11
---

# 文件使用案例 {#document-use-cases}

这是黄金规则 在`quality_scale.yaml`中,它被称为`docs-use-cases`.

[Home Assistant.io](https://www.home-assistant.io/)上的集成页面描述了少数使用例:一旦设备或服务在Home Assistant中,您可以做什么,以及您为什么想要它在那里.

## 为什么这很重要 {#why-it-matters}

对于一些整合,价值是显而易见的:聪明的光是用来开启光线的. 对其他人来说,一个用户审视整合,并想知道他们为什么要烦恼. 几个具体的应用案例回答了这个问题,并经常给人他们本不会有的想法.

使用案件是为什么。 [文件实例](/core/quality-scale/docs-examples)是关于如何, 自动化可以复制。

## 示例 {#example}

```markdown
## Use cases {#use-cases}

The water meter of My Company reports your water usage every minute.
In Home Assistant, you can:

- Track your water usage in the energy dashboard, next to electricity
  and gas.
- Get a notification when water keeps running for an hour, which often
  means a leak or a running toilet.
- Compare your usage per day, to see what the garden sprinklers cost.
```

参见 [写入集成文件](/writing/guides/integration) 和 [整合页面结构](/writing/reference/integration-page) 。

## 如何检查 {#how-it-is-checked}

在审查中检查过,通常在文件pull request上.

## 例外 {#exceptions}

这一规则没有例外。
