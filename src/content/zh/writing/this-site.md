---
title: 改进这个贡献网站
sidebarLabel: 这个贡献网站
description: 修复或添加关于贡献者. home-assistant.io的页面,在自己的机器上预览,并保持链接和重定向工作.
---

# 改进这个贡献网站 {#improve-this-contributor-site}

此领域的其它一切都是关于[Home Assistant.io](https://www.home-assistant.io/)上的用户文档. 这页是关于你正在读的网站。 它也是开源的,它也得到了更好的方法:有人发现一些错误或缺失的东西,并修正它。

源头位于[撰稿人. home-assistant.io寄存器](https://github.com/home-assistant/contributors.home-assistant.io). 它的README是维护者的指南,其中包含每个脚本以及移动部分如何组合在一起. 此页面覆盖您需要的页面 。

## 修点小东西 {#fix-something-small}

每页都有一个**编辑本页**链接在底部. 它打开了GitHub上的页面,您可以在浏览器中更改并打开pull request. 对于打字,破句,或过时的事实,都只须如此.

页面为Markdown, in `src/content/docs/`. 写规则在寄存器的[`.github/copilot-instructions.md`](https://github.com/home-assistant/contributors.home-assistant.io/blob/main/.github/copilot-instructions.md)中:语言,马克当和YAML风格,以及网站的结构.

## 使用AI 工具 {#work-with-an-ai-tool}

写法规则为AI工具的指令双倍: `AGENTS.md`和`CLAUDE.md`链接到它们. 工作流程作为 我也是在 `.github/skills/` (也可达到 `.claude/skills/` ) 中生存,比如 `write-page` 添加或更改一个页面, `fact-check` 对照源寄存器检查页面, `review` 审查更改 。 副驾驶代码审查也遵循`.github/instructions/`中的核对表,一个用于页面,一个用于站点代码.

在其中最重要的规则: 永远不要发明任何东西。 这个网站的每个声明都需要有人能读到的来源. [用AI 工具做贡献](/start/ai-tools#what-to-check-yourself-every-time) 列出最经常发现的错误检查。

## 本地预览网站 {#preview-the-site-locally}

任何比小的修补器更大的东西 都用你自己的机器运行

最简单的方式是dev容器:网站需要的一切都是现成的,在Windows,macOS和Linux上都一样. 在[VS 代码](https://code.visualstudio.com/docs/devcontainers/containers)中打开仓库,安装Docker和**Dev集装箱**扩展,并选择**在集装箱中重新打开**。 或者在寄存器上启动 [GitHub 代码空间](https://docs.github.com/en/codespaces) , 它运行在您的浏览器中, 而不需要在您的机器上 。 无论哪种方式,在创建容器时都会安装依赖性,您只运行 `pnpm dev` 。 要运行与 pull request 相同的检查, 请在 VS 代码中选择 ** Terminal ** > ** Run Task **, 然后选择 ** Pull 请求检查 ** 。

没有dev容器,您需要节点24(版本为`.node-version`)和pnpm. 然后安装并启动网站:

```shell
pnpm install
pnpm dev
```

网站现在为`http://localhost:4321`,保存页面时会重新加载. 搜索只在一个建筑上工作 :

```shell
pnpm build
pnpm preview
```

在打开 pull request 之前, 请运行 `pnpm check` 。 它检查每页的代码和头条

## 添加页面 {#add-a-page}

网站分为一些区域,如Core和集成,或Design. 每个区域都是`src/content/docs/`中的文件夹,每个页面都进入它所属区域的文件夹. 子文件夹成为侧边栏中的组 。 页面最多可深入一个子文件夹。

每页以前题开头:

```yaml
---
title: "Fetch data"
description: "How your integration gets data from a device or a service."
order: 3
---
```

- {H 你要我说吗? 使用句 你要我说什么?
- `description` 在标题协调一致地显示, 在搜索结果和链接预览中。
- `order` 将页面放在侧边栏, 最低第一 。 无页的页数最后, 按标题排序 。
- `sidebarLabel` 是侧边栏的较短标签, 当标题是长的 。
- `sidebarGroup` 将页面放在边栏的命名组中, 不更改其 URL 。 文件夹的 `index.md` 可以使用 `sidebarGroups` 设置这些组的顺序 。

文件夹的 `index.md` 是其概览页 。 每个领域都有相同的形状:概述,第一贡献,向导,参考,和谁说话. 先看看邻居的页面,再加一个,然后跟着它做什么。

## 术语表 {#glossary-terms}

Home Assistant中有特定含义的单词,如[配置条目](/glossary/config-entry),在[,](/glossary)中有页面. 使用这些术语,当一个术语缺失时,添加到那里而不是在你的页面上解释.

一个术语可以自己链接:其页面的`autolink`列表中的单词在一页首次使用时就成为链接. 在那里只添加指无论出现在哪里的词语. 当见本报告 `pnpm dev` 运行时, 更改为 `autolink` 列表会重新启动服务器, 所以每个页面都会拾取新单词 。

## 现场演示 {#live-demos}

[设计区](/design) 显示 Home Assistant 前端的真实组件, 在页面上直播, 在 MDX 页面中有一个 `<Demo>` 块 。 从已有组件页面复制演示开始 。 组件本身是从前端源头构建并致力于的,因此不需要前端在页面上工作. 添加一个尚未构建的组件是维护者的任务: README解释如何构建.

## 检查您的链接 {#check-your-links}

链接到其他页面, 并带有完整的路径, 以及一条线索的斜线, 如 `/design/foundations/color/` 。 要检查网站的每个链接, 构建并运行链接检查 :

```shell
pnpm build
pnpm links
```

它列出了一个不存在的页面或标题的每一个链接,并附有它所在的页面. 每个 pull request 都进行同样的检查 。

## 移动或重命名一页 {#move-or-rename-a-page}

移动或重新命名某一页会修改其 URL, 以及连接到其他站点的 URL 、 书签 、 搜索引擎 。 因此:

1. 移动页面,并更新该网站上的链接. 找到那些你错过的
2. 在您的pull request 中提及每一个移动的页面 。

然后,一个维护者会为旧的 URL 添加方向调整 。 重定向在寄存器的 `redirects/` 文件夹中直播, 作为每个区域的一个小表, 并且构建将它们变成网站的重定向 。

重新命名一个标题会改变它的锚, 链接到页面顶端的这个标题区域。 当它使页面更好时重新命名标题,但知道旧链接会失去位置.
