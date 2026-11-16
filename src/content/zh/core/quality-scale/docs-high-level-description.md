---
title: 描述品牌、产品或服务
description: 青铜规则docs-high-level-description:文档描述了集成连接的内容.
sidebarLabel: 高层次文件描述
sidebarGroup: 铜
order: 10
---

# 描述品牌、产品或服务 {#describe-the-brand-product-or-service}

此是铜法. 在`quality_scale.yaml`中,它被称为`docs-high-level-description`.

[Home Assistant.io](https://www.home-assistant.io/)上的用户文档从品牌,产品,或服务集成连接的高级描述开始. 在可能的情况下,它会链接到品牌,产品或服务的网站.

## 为什么这很重要 {#why-it-matters}

并不是每个登上整合版的人都知道它是什么。 关于产品或服务是什么的几句话帮助用户在他们花时间进行设置之前决定集成是否适合他们. 联系给他们一个学习更多地方。

## 示例 {#example}

有代表性的是引入整合页面,紧接前题,没有标题:

```markdown
The **My integration** {% term integration %} connects Home Assistant
to the smart plugs and switches of [MyCompany](https://www.example.com).
MyCompany makes energy monitoring devices for the home, and is best
known for its MyPlug range.
```

引言中还说明了您可以对整合做些什么. 请参看 [整合页面结构](/writing/reference/integration-page) 和 [综合文件](/writing/guides/integration) 中集成页的章节, 用于写页 。

## 如何检查 {#how-it-is-checked}

检查过 pull request 与整合相关的文件 。

## 例外 {#exceptions}

与设备或服务不连接的集成,和内部集成一样,没有什么可描述的,是免责的.
