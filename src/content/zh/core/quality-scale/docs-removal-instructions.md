---
title: 如何删除集成的文件
description: 青铜规则docs-move-interventions:文档解释如何去除整合.
sidebarLabel: 证件 -- -- 搬运
sidebarGroup: 青铜
order: 12
---

# 如何删除集成的文件 {#document-how-to-remove-the-integration}

此是铜法. 在`quality_scale.yaml`中,它被称为`docs-removal-instructions`.

[Home Assistant.io](https://www.home-assistant.io/)上的集成页必须解释如何去除集成. 当将它从Home Assistant中移除时,就说吧。 当有更多的东西需要清理时,如制造商的应用软件中的标志或设备上的设置,也描述这些步骤。

## 为什么这很重要 {#why-it-matters}

删除一个集成并不总是像删除Home Assistant那样简单。 云服务可能保留Home Assistant列为连接的应用程序,或设备可能不断将数据推向不再听的地址. 想要开始新鲜,或者停止使用设备的用户需要知道留下了什么.

## 示例 {#example}

绚丽在 Home Assistant 中的步骤使用标准包含, 并添加任何与您的整合相关的特定内容 :

```markdown
## Removing the integration {#removing-the-integration}

This integration follows standard integration removal.

{% include integrations/remove_device_service.md %}

After you remove the integration, open the **MyProduct** app and remove
Home Assistant from the list of connected apps.
```

查看 [写入集成文件](/writing/guides/integration) 和 [整合页面结构](/writing/reference/integration-page) , 说明该页面的走向 。

## 如何检查 {#how-it-is-checked}

查阅文件pull request。

## 例外 {#exceptions}

这一规则没有例外。

## 相关规则 {#related-rules}

- [设置文件](/core/quality-scale/docs-installation-instructions): 记录安装。
