---
title: 综合文件
description: 对于为Home Assistant添加新集成的开发者. 文档需要什么 如何与代码合并
order: 3
---

# 综合文件 {#document-an-integration}

Home Assistant中的每一集成都在[Home Assistant.io](https://www.home-assistant.io/)上有一个页面. 添加集成时,其页面是作品的一部分. 用户通过该页面找到集成,集成概况由此产生.

## 在你开始之前 {#before-you-start}

- 目标`next`分支。 您的整合尚未发布, 所以它的页面也没有 。
- 打开一个文档 pull request 每个核心 pull request, 并在 ** 此 PR 下列出每个文档 。
- 将集成的图标和标志添加到 [品牌存储器](https://github.com/home-assistant/brands) 中, 用同样的方式将 pull request 与 pull request 核心对齐 。

## 创建页面 {#create-the-page}

1. 复制[整合页面模板](https://github.com/home-assistant/home-assistant.io/blob/current/source/_integrations/_integration_docs_template.markdown) 到[`source/_integrations/`](https://github.com/home-assistant/home-assistant.io/tree/current/source/_integrations) 。
2. 在您的整合域后命名文件, 并使用 `.markdown` 扩展名, 如 `my_device.markdown` 。
3. 填前题. 它驱动集成综述,质量尺度徽章,以及更多. 每个键都在[一体化问题。](/writing/reference/front-matter)中解释.
4. 写入页面,遵循模板的结构. [整合页面结构](/writing/reference/integration-page)解释每一节的用途。
5. 将集成及其集成所有者添加到文档存储器的`CODEOWNERS`文件中. 如果您拥有该集成, 您也拥有其文档 : 您被要求审查页面的更改, 并且您会根据读者留下的反馈浏览 。
6. 在标记 pull request 以备审查之前, 删除模板中的评论 。

## 多好的整合页面覆盖 {#what-a-good-integration-page-covers}

模板引导您通过各节。 有些东西审查者寻找:

- ** 整合的作用** 以及人们可以用来做什么,在第一行。
- ** 辅助装置**,以及已知不起作用的装置。 提到你测试过的固件版本
- ** 如何获得证书**,如API密钥或访问符,一步一步地获得.
- **  如果是步骤或例子,则不采用自定义整合或自定义卡。 一切应该 如果是Home Assistant的船。
- **知道限制和排除故障**,所以用户不需要找到困难的方法.

## 当特性消失 {#when-features-go-away}

特性的文档一经贬值就删除,而非删除时:从整合页面中删除其部分,不添加折旧通知. 当一个整体整合被贬值或移除时,参见[移动、重命名或删除页面](/writing/guides/move-or-remove).
