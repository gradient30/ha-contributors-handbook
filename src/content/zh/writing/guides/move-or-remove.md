---
title: 移动、重命名或删除页面
description: 页面从各地链接. 这是如何在不破坏这些联系的情况下改变它们。
order: 4
---

# 移动、重命名或删除页面 {#move-rename-or-remove-a-page}

文件页面由论坛帖、博客帖、其他网站和Home Assistant本身链接。 当一个URL改变时,这些链接应该继续工作.

## 移动或重命名一页 {#move-or-rename-a-page}

在 `source/_redirects` 中将旧的 URL 添加到新的 URL 中 :

```text
/integrations/old_name  /integrations/new_name  301
```

当将一节移动到另一页时,同样适用:将旧地址发送到内容现在居住的地方.

## 删除整合页面 {#remove-an-integration-page}

当一个集成从Home Assistant中移除,或者整个集成被贬值时,其文件也会:

1. 删除 `source/_integrations` 中的页面, 连同其触发器、 条件和行动 `source/_triggers`、 `source/_conditions` 和`source/_actions` 中, 如果有的话 。
2. 从 [品牌存储器](https://github.com/home-assistant/brands) 中删除其图标和标志 。
3. 从 `CODEOWNERS` 文件中删除其条目 。
4. 在 `source/_redirects` 中为已删除的集成添加重定向 。 删除的整合都指向同一页,这向访问者解释了发生了什么:

```text
   /integrations/old_name  /more-info/removed-integration  301
   ```

## 折旧特征 {#deprecated-features}

不要等到一个特性被删除。 [文献储存库](https://github.com/home-assistant/home-assistant.io)中的规则是:"当一个特性被贬值或者从Home Assistant中删除一个集成时,删除它的文档".

- 如果一个特性被贬值,则从集成页面中删除其部分.
- 在文件上不要添加折旧通知。
- 如果整个集成被折旧,请删除在[删除整合页面](/writing/guides/move-or-remove#remove-an-integration-page)中描述的页面.
