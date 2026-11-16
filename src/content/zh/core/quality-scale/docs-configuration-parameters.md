---
title: 文档选项
description: 银规则docs-configation-参数:文档描述了选项流的每个选项.
sidebarLabel: 文件配置参数
sidebarGroup: 银
order: 3
---

# 文档选项 {#document-the-options}

这是Silver的规则 在`quality_scale.yaml`中,它被称为`docs-configuration-parameters`.

[Home Assistant.io](https://www.home-assistant.io/) 上的集成页面必须描述用户在集成的[选项流动](/glossary/options-flow)中设置后可以更改的每个选项. 对于每个选项,请解释它做了什么,什么价值是有意义的。

## 为什么这很重要 {#why-it-matters}

一个没有解释的选项就是猜测. 用户打开选项,看到像"Timeframe"这样的字段,不知道是选5还是选120,或者做时会有什么变化. 整合页面上的简短描述可以保存他们的试题和错误,并保存支持问题.

## 示例 {#example}

添加标准选项文本, 然后是 `configuration_basic` 块, 每个选项有一个条目 。 使用 UI 中的标签 :

```markdown
{% include integrations/option_flow.md %}

{% configuration_basic %}
Country code:
  description: "The country (NL or BE) to show on the radar camera."
Timeframe:
  description: "How many minutes ahead the precipitation forecast
    looks. From 5 to 120 minutes."
{% endconfiguration_basic %}
```

关于块,请参见[整合页面结构](/writing/reference/integration-page#the-configuration_basic-block),关于如何打开文件pull request,请参见[写入集成文件](/writing/guides/integration)。

## 如何检查 {#how-it-is-checked}

此规则将在审查代码和文件pull request时检查。

## 例外 {#exceptions}

如果整合没有选项流,则该规则不适用.

## 相关规则 {#related-rules}

- [文件安装参数](/core/quality-scale/docs-installation-parameters): 记录设置参数。
