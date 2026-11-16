---
title: 前端架构
description: 如何组合前端,从装入的第一个脚本到面板,对话框,以及流经它们的数据.
order: 20
sidebarLabel: 架构
---

# 前端架构 {#frontend-architecture}

前端是一个由网络组件制作的单页应用程序. 每个组件将它的模板,样式,逻辑捆绑在一起,并在浏览器中以HTML标签的形式出现,如`<ha-button>`或`<hui-tile-card>`. 组件由更大的组件组成,一直到应用程序本身.

## 各个部分 {#the-parts}

前端负载分为四层.

### 诱饵 {#bootstrap}

[`src/entrypoints/core.ts`](https://github.com/home-assistant/frontend/blob/dev/src/entrypoints/core.ts) 是一个小脚本, 可以先装入 。 它检查登录证书并打开 WebSocket 连接到 Home Assistant Core 。 由于数据太小,所以数据开始流动,而其余的界面仍在下载.

### 应用程序外壳 {#app-shell}

[`src/entrypoints/app.ts`](https://github.com/home-assistant/frontend/blob/dev/src/entrypoints/app.ts) 装入根元素, `<home-assistant>` 在[`src/layouts/home-assistant.ts`](https://github.com/home-assistant/frontend/blob/dev/src/layouts/home-assistant.ts) 中, 以及全局样式 。 根元素通过 [`src/state/`](https://github.com/home-assistant/frontend/tree/dev/src/state) 中的一叠混音器来设置应用程序的状态: 连接, 翻译, 主题, 对话框, 侧边栏等 。 然后它使 [`src/layouts/home-assistant-main.ts`](https://github.com/home-assistant/frontend/blob/dev/src/layouts/home-assistant-main.ts) 绘制侧边栏, 并将当前 URL 交给面板解析器 。

### 的小组 {#panels}

Home Assistant中的每一页都是[面板](/glossary/panel):仪表板,地图,历史,设置. 面板生活在 [`src/panels/`](https://github.com/home-assistant/frontend/tree/dev/src/panels) 中, 只有在有人打开时才会加载 。 核心决定哪些小组存在,整合可以增加自己的小组. 解释一下

### 对话框 {#dialogs}

对话框在 [`src/dialogs/`](https://github.com/home-assistant/frontend/tree/dev/src/dialogs) 中存在, 可以在任何页面的顶端打开 。 最著名的是[更多信息对话框](/glossary/more-info-dialog),它显示一个实体的状态,历史和设置.

## 生活之地 生活之地 {#where-things-live}

| 文件夹 | 里面有什么东西? |
| --- | --- |
| [`src/components/`](https://github.com/home-assistant/frontend/tree/dev/src/components) | 共享 `ha-*` 组件, 随处使用 。 |
| [`src/panels/`](https://github.com/home-assistant/frontend/tree/dev/src/panels) | 每个面板一个文件夹。 盘子在[`src/panels/lovelace/`](https://github.com/home-assistant/frontend/tree/dev/src/panels/lovelace)中. |
| [`src/dialogs/`](https://github.com/home-assistant/frontend/tree/dev/src/dialogs) | 对话框,包括更多信息对话框 。 |
| [`src/data/`](https://github.com/home-assistant/frontend/tree/dev/src/data) | 对 Core 说话的类型和函数 : WebSocket 命令、 订阅和上下文 。 |
| [`src/common/`](https://github.com/home-assistant/frontend/tree/dev/src/common) | 没有UI的小助手:格式化,实体助手,装饰师,以及DOM公用事业. |
| [`src/state/`](https://github.com/home-assistant/frontend/tree/dev/src/state) | 构成根元素的应用状态的混合剂. |
| [`src/layouts/`](https://github.com/home-assistant/frontend/tree/dev/src/layouts) | 根元素,主布局,面板解析器,以及页面布局. |
| [`src/resources/`](https://github.com/home-assistant/frontend/tree/dev/src/resources) | 全球风格和主题定义. |
| [`src/translations/`](https://github.com/home-assistant/frontend/tree/dev/src/translations) | `en.json`,所有前端文本的英文来源. |
| [`src/external_app/`](https://github.com/home-assistant/frontend/tree/dev/src/external_app) | 桥到伴应用. |

## 数据流动情况 {#how-data-flows}

前端与Core的会谈大多在[API (韩语)](https://github.com/home-assistant/home-assistant-js-websocket)上,少数地方在REST API上.

数据流动方式之一。 当Core的某事发生改变时,像灯光开启一样,根元素会收到更新并生成一个新的 `hass` 对象,变化会从组件树下流到每一个需要它的组件. 当一个组件想要改变某种东西时,它会叫Core,并等待变化的回落.

仅需要部分数据的组件会消耗 [案件的上下文](/frontend/architecture/hass-and-contexts) 而不是整个 `hass` 对象 。 不在 `hass` 中的数据, 像标签注册或备份列表一样, 是通过 [订阅和命令](/frontend/architecture/data) 装入的, 使其与 Core 同步 。

## 页面 {#pages}

- [构成部分和语文](/frontend/architecture/components):web 组件,Lit,和 `ha-*` 在Web Super上构建的组件.
- [对象和背景](/frontend/architecture/hass-and-contexts): 组件如何获得数据 。
- [数据已为层](/frontend/architecture/data):WebSocket命令、订阅和收藏。
- [前端的翻译](/frontend/architecture/translations): 如何翻译文本 。
- 所从事的 {L050} : 主题变量和符号, 以及主题如何应用 。
- [路线和面板](/frontend/architecture/routing-and-panels): URL如何成为页面 。
