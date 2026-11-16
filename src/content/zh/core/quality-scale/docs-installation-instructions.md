---
title: 记录安装
description: 青铜规则docs-installation-interformation:文档有分步设置指令,有先决条件.
sidebarLabel: 设置文件
sidebarGroup: 青铜
order: 11
---

# 记录安装 {#document-the-installation}

此是铜法. 在`quality_scale.yaml`中,它被称为`docs-installation-instructions`.

[Home Assistant.io](https://www.home-assistant.io/)上的集成页面必须逐级解释,如何设置集成. 如果在设置之前必须发生一些事情,比如创建账户,安装一个应用软件,或者打开设备上的本地API,页面会列出这些作为先决条件.

## 为什么这很重要 {#why-it-matters}

设置是用户在您集成方面最早的经验. 当设备需要先更改一个设置,且文档没有说时,用户最后会有一个这类活动无法连接的配置流,并且不知道为什么. 明确指示,包括准备什么,防止这种挫折感和许多支持性问题。

## 示例 {#example}

列出编号步骤的前提条件,然后使用设置本身的标准配置流程:

```markdown
## Prerequisites {#prerequisites}

1. Install the **MyProduct** app on your phone, and create an account.
2. Add your device in the app.
3. In the app, go to **Settings** and turn on **Local API**.

{% include integrations/config_flow.md %}
```

包含添加了 [我的连结](/glossary/my-link) 徽章 `{% my config_flow_start badge domain=domain %}`, 打开了您在读者自己的 Home Assistant 中整合的配置流 。 你不能自己加那个徽章

查看 [写入集成文件](/writing/guides/integration) 和 [整合页面结构](/writing/reference/integration-page) , 说明该页面的走向 。

## 如何检查 {#how-it-is-checked}

已检阅. 文件濑pull request的审阅员阅读了这些说明,理想的做法是遵循这些说明。

## 例外 {#exceptions}

这一规则没有例外。

## 相关规则 {#related-rules}

- [文件安装参数](/core/quality-scale/docs-installation-parameters): 记录设置参数。
- [证件 -- -- 搬运](/core/quality-scale/docs-removal-instructions): 文档如何删除整合 。
