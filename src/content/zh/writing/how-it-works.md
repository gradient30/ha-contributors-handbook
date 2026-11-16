---
title: 文档如何运作
description: 页面的住址,使用哪个分支,以及从pull request到home-assistant.io的更改方式.
order: 2
sidebarLabel: 它是如何运作的
---

# 文档如何运作 {#how-the-documentation-works}

文档和 [Home Assistant.io](https://www.home-assistant.io/) 的其余部分在一个 GitHub 寄存器 : [Home Assistant/Home Assistant.io](https://github.com/home-assistant/home-assistant.io) 。 网站以[杰基尔](https://jekyllrb.com/)建成. 页面是 Markdown 文件, 对于像 Home Assistant 接口中的链接, 有一些 [目录](/writing/reference/liquid) 。

## 页面所在 {#where-pages-live}

一切都在`source`文件夹里。 你工作的大部分部分是:

- `source/_integrations`:每集成一页,以其域名命名,如`hue.markdown`.
- `source/_docs`:一般文档,如自动化,脚本,和备份指南.
- `source/_dashboards`:仪表板和牌。
- [`source/_data/glossary.yml`](https://github.com/home-assistant/home-assistant.io/blob/current/source/_data/glossary.yml):术语工具提示背后的词汇表.
- `source/_redirects`: 移动时, 移动时, 移动时, 移动时, 移动时 , 移动时 , 移动时 , 移动时 , 移动时 , 移动时 , 移动时 , 移动时 , 移动时 , 移动时 , 移动时 , 移动时 , 移动时 , 移动时 , 移动时 , 移动时 , 移动时 , 移动时 , 移动时 , 移动时 , 移动时 , 移动时 , 移动时 , 移动时 , 移动时 , 移动时 , 移动时 移动时 , 移动时 移动时 , 移动时 移动时 , 移动时 , 移动时 , 移动时 , 移动时 移动时 , 移动时 , 移动时 , 移动时 , 移动时 移动时 , 移动时 , , 移动 移动 , , 移动 , , , 移动时 , 移动时 ,
- [`source/_includes/asides/docs_sitemap.html`](https://github.com/home-assistant/home-assistant.io/blob/current/source/_includes/asides/docs_sitemap.html):一般文档的侧边栏. 它由人工维护,所以在`source/_docs`中需要侧边栏位置的新页面在那里得到链接.

## 分支 {#branches}

该寄存器有两个分支,您在其中选择:

- QQH0}**是今日发行人使用的文档. 将它作为修正和改进现有文件的目标。
- QQH0}**是即将发布的文档. 用于记录尚未发布的新集成或新功能时设定目标 。

选择正确的分支事项: `next` 上的更改只与下一次发布一起运行 。 pull request模板提醒您,一个bot也提醒您:当基分支与您的pull request不匹配时,它会添加`needs-rebase`标签,并留下一个注释,告诉您要使用哪个分支.

从核心 pull request 记录新特性? 每个核心 pull request 打开一个文档 pull request 并将其链接 。 然后两者可以合并为同一版.

## 双亲 pull request s {#parent-pull-requests}

文档 pull request 记录代码更改的文档有  parent : pull request 带有代码更改的文档, 在像核心或前端一样的寄存器中 。 双向链接 : 在 ** 此 PR 下列出父目录与您的文档 pull request 中的 ** 一起, 您的文档 pull request 在父目录的同一行上 。

沿着这些链接的机器人,并标记您的文档 pull request :

- `has-parent`: 您的pull request 及其父列表 。 列出代码 pull request 的 pull request 预计将瞄准 `next`, 而没有的 预计将瞄准 `current` 。
- `parent-merged`:母体被合并,因此文档可以遵循.
- `needs-rebase`: pull request 瞄准错误的分支 。 改变基部分支,如果需要则重新基部.

您也可能看到 `awaits-parent`, 这意味着 pull request 正在等待其父的合并 。

机器人也保持双脚步态 当您的 pull request 拥有单亲且父母未合并而关闭时, 您的文档 pull request 也关闭 。 当父母重开时,你的也是

在 `next` 上的文档 pull request 等待它的父 。 这需要一段时间,这很好:标签的 pull request 从来没有标记为 stale 。

## 从pull request到生活 {#from-pull-request-to-live}

1. 您打开 pull request 。
2. 自动检查运行:评论检查Markdown,textlint检查拼写和术语,网站Astro部分建成. 有细节
3. Netlife 创建一个 ** 部署预览 ** 整个网站与您的更改。
4. 一个维护者审查变化。
5. 一旦合并为`current`,Netlife将发布更改为home-assistant.io. `next` 的更改随发布开始 。

60天没有活动的pull request和问题被标记为呆滞,7天后关闭,除非有事发生. 评论或新的承诺足以保持开放。
