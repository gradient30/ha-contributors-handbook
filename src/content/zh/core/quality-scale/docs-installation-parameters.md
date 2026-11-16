---
title: 记录设置参数
description: 身身身形像像像像一样,
sidebarLabel: 文件安装参数
sidebarGroup: 银
order: 4
---

# 记录设置参数 {#document-the-setup-parameters}

这是Silver的规则 在`quality_scale.yaml`中,它被称为`docs-installation-parameters`.

[Home Assistant.io](https://www.home-assistant.io/)上的集成页面必须描述用户设置集成时填写的每个字段. 对于每个字段,请解释它是什么,以及用户可以在哪里找到值.

## 为什么这很重要 {#why-it-matters}

很少有事情比 设置形式更令人沮丧 要求的东西你没有。 "本地访问证"? 从哪里来的? 当文档列出每个字段,以及在哪里找到时,用户可以在开始前收集所有东西,并在一个段落中通过设置.

## 示例 {#example}

对于从 UI 设置的集成,请遵循 `configuration_basic` 块的标准配置文本 。 使用与设置表格中的标签完全相同的标签 :

```markdown
{% include integrations/config_flow.md %}

{% configuration_basic %}
Host:
  description: "The IP address of your bridge. You can find it in your
    router, or in the app under **Bridge settings** > **Local API**."
Local access token:
  description: "The local access token of your bridge. You can find it
    in the app under **Bridge settings** > **Local API**."
{% endconfiguration_basic %}
```

对于在YAML中设置的集成,使用 `configuration` 块代替,该块还列出是否需要变量及其类型. 两个区块见[整合页面结构](/writing/reference/integration-page#the-configuration-block), 和[写入集成文件](/writing/guides/integration) 如何打开文件 pull request 。

## 如何检查 {#how-it-is-checked}

此规则将在审查代码和文件pull request时检查。

## 例外 {#exceptions}

如果合并在设置时不需要任何要求,则该规则不适用.

## 相关规则 {#related-rules}

- [文件配置参数](/core/quality-scale/docs-configuration-parameters): 记录选项。
- [设置文件](/core/quality-scale/docs-installation-instructions): 记录安装。
