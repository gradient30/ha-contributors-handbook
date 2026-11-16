---
title: 文档排除故障
description: Gold Rules docs- troubleshooting:文档帮助用户自己解决常见问题.
sidebarLabel: 文档调试
sidebarGroup: 金
order: 10
---

# 文档排除故障 {#document-troubleshooting}

这是黄金规则 在`quality_scale.yaml`中,它被称为`docs-troubleshooting`.

[Home Assistant.io](https://www.home-assistant.io/)上的集成页面有一个排除故障的段落,用于解决用户遇到的问题,并能自行修复. 每个话题都描述了用户所看到的症状,产生的原因,以及解决的步骤.

## 为什么这很重要 {#why-it-matters}

能够自己解决问题的用户会在几分钟内备份并运行,而不是等待一个问题或一个论坛线程的日子. 你所记录的每一个常见问题都是一个支持性问题,无需再问,并再次回答.

从症状开始,用用户在屏幕上看到的话来说. 这就是他们寻找的。

## 示例 {#example}

将每个问题放在自己可碰撞的块中,并附症状,描述和解析. 当一个短的话题没有增加任何内容时,留下一部分。

```markdown
## Troubleshooting {#troubleshooting}

{% details "Can't set up the device" %}

### Symptom {#symptom}

When you set up the integration, the form shows "Failed to connect".

#### Description {#description}

The device only accepts local connections when local access is turned
on in its settings.

#### Resolution {#resolution}

1. Make sure the device is powered on, and the LED is green.
2. In the app of the manufacturer, go to **Settings** > **Local access**.
3. Turn on **Allow local connections**, and try again.

{% enddetails %}
```

参见 [写入集成文件](/writing/guides/integration) 和 [整合页面结构](/writing/reference/integration-page) 。

## 如何检查 {#how-it-is-checked}

在审查中检查过,通常在文件pull request上.

## 例外 {#exceptions}

如果集成没有已知的问题可供用户自行解决,则该规则不适用.
