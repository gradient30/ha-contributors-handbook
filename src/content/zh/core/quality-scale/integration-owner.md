---
title: 有个融合的主人
description: '这一部分包括: 银规则集成所有者:集成至少有一个集成所有者.'
sidebarLabel: 融合所有人
sidebarGroup: 银
order: 6
---

# 有个融合的主人 {#have-an-integration-owner}

这是Silver的规则 在`quality_scale.yaml`中,它被称为`integration-owner`.

集成必须至少有一个[融合拥有者](/glossary/integration-owner),列在其`manifest.json`的`codeowners`字段中. 一体化可以不止一个。

## 为什么这很重要 {#why-it-matters}

大多数整合都是由核心团队以外的人所写,他们比任何人都更了解设备或服务. 融合业主会长期照顾融合. 他们被通知每个新问题和pull request,他们对其问题和pull request的处理方式有更多的发言权,而审查者视之为专家:他们对变化的意见更为重要。

更好地维持与业主的融合。 这就是为什么从Silver向上的每一层都需要一个,为什么没有主动拥有者的整合可以降级为Bronze,即使它满足了更高层的所有其他规则.

## 示例 {#example}

添加您的 GitHub 用户名, 加上 `@` , 到 :

```json
{
  "domain": "my_integration",
  "name": "My integration",
  "codeowners": ["@my-github-username"]
}
```

然后运行 `python3 -m script.hassfest` 更新寄存器的 `CODEOWNERS` 文件, 并输入两个文件 。

要成为现有整合的拥有者, 请打开 早先添加您的 pull request 。 它有助于首先促进一体化。

## 如何检查 {#how-it-is-checked}

- 如果与表中所列的银、金或白金级的融合没有一体化所有人,那么这种融合就会失败。
- Hassfest 也检查 `CODEOWNERS` 文件是否匹配 。
- 检查所有者是否仍在活动 。

## 例外 {#exceptions}

这一规则没有例外。
