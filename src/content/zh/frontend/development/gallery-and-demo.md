---
title: 画廊和演示
description: 两种没有 Home Assistant 运行真实前端的方法 。 组件和卡片的画廊,整个应用程序的演示.
order: 3
---

# 画廊和演示 {#the-gallery-and-the-demo}

并非所有更改都需要运行 Home Assistant 。 [前端仓库](https://github.com/home-assistant/frontend)有两种应用来运行真实的前端代码以对抗假数据:画廊和演示.

## 画廊 {#the-gallery}

画廊显示组件,仪表板卡,以及更多的信息视图在每一个重要状态上 October, off, unchable, loading, in light and dark, and right to left. 它是一个开发工具: 在当地运行以构建和检查一个没有 Home Assistant 的组件 。

8100端口本地运行:

```shell
pnpm dev:gallery
```

画廊位于 [`gallery/`](https://github.com/home-assistant/frontend/tree/dev/gallery) 文件夹中 :

- `gallery/src/pages/<category>/<page>.markdown`:一个页面的描述,有`title`和`subtitle`的可选前题.
- `gallery/src/pages/<category>/<page>.ts`:同页的现场演示. 它定义了一个以页面命名的自定义元素,比如`demo-components-ha-button`对`components/ha-button`的自定义.
- [`gallery/sidebar.js`](https://github.com/home-assistant/frontend/blob/dev/gallery/sidebar.js):侧边栏的章节和其中的页面顺序.
- [`gallery/src/data/`](https://github.com/home-assistant/frontend/tree/dev/gallery/src/data)和[`gallery/src/components/`](https://github.com/home-assistant/frontend/tree/dev/gallery/src/components):假的`hass`对象,样本状态,以及像`demo-cards`和`demo-more-infos`这样的帮助者,可以生成一张卡片配置或实体列表.

图片库页面使用来自[`src/`](https://github.com/home-assistant/frontend/tree/dev/src) 的真实组件, 而不是副本 。 当您的 HIVe 更改一个文档组件的行为时, 请在 pull request 中更新其画廊页面 。 维护者可以添加 `needs design preview`的确切标签,为您的 pull request 配置图片库的预览 。

> [!NOTE]
> 已出版的设计指南生活在这个网站的[设计](/design)区域,而不是画廊. 它取代了设计 Home Assistant [组件](/design/components)、[仪表板卡](/design/dashboards)和[啊 更多信息视图](/design/more-info) 都有一个页面, 上面有用法、 规格、 可访问性和活例 。 当您的更改改变一个组件的外观或行为时, 用 pull request 更新到 [这个网站](https://github.com/home-assistant/contributors.home-assistant.io) 。

## 演示 {#the-demo}

演示是完整的 Home Assistant 前端, 运行在您的浏览器中一个被嘲笑的后端 。 发表于[演示. home-assistant.io](https://demo.home-assistant.io/). 它是最容易在没有服务器的情况下加载完整应用程序的方法,例如检查一个仪表板或进行截图.

在8090端口就地运行:

```shell
pnpm dev:demo
```

演示有好几个家可以选择. 选择一个带有 `demo` 查询参数, 以及 `#` 后面的页:

```text
http://localhost:8090/?demo=<slug>#/energy
```

弹壳在[`demo/src/configs/demo-configs.ts`](https://github.com/home-assistant/frontend/blob/dev/demo/src/configs/demo-configs.ts)。 每个坛主都有自己的文件夹在[`demo/src/configs/`](https://github.com/home-assistant/frontend/tree/dev/demo/src/configs),有它的实体,仪表板,和主题. 被嘲笑的WebSocket和REST APIs生活在[`demo/src/stubs/`](https://github.com/home-assistant/frontend/tree/dev/demo/src/stubs).

美术馆也进口了一些树枝 当您更换一个字节时, 请检查演示和使用的画廊页 。

一些演示数据来自Core:[`src/fake_data/demo_services.ts`](https://github.com/home-assistant/frontend/blob/dev/src/fake_data/demo_services.ts)中的动作描述,以及[`demo/src/stubs/`](https://github.com/home-assistant/frontend/tree/dev/demo/src/stubs)中的触发和条件描述. 别用手来编辑 运行 `script/gen_demo_core_data` 从 Core 的 `dev` 分支重生它们 。

## 其他站点嵌入卡 {#embed-cards-on-other-sites}

演示还构建了 `embed.js` , 它将 仪表卡 放在任何网页上 , 包含 `<ha-embed-provider>` 和 `<ha-embed-card>` 元素 。 卡片作者将其用于[他们的卡片现场演示](/frontend/custom-ui/demo). 它的代码在 `demo/src/embed/` 中, `demo/src/html/components.html.template` 是在演示的 `/components.html` 中记录它的页面 。

提供者登记自己的一套模拟器。 多数来自[`demo/src/stubs/`](https://github.com/home-assistant/frontend/tree/dev/demo/src/stubs)中的根茎,少数像能量一样在`ha-embed-provider.ts`中定义. 每个演示、嵌入层和 导入槽的画廊页 都无法全部导入相同的 例如,被嵌入体和画廊使用的是日历根,而不是演示. 用于新建根, 请导入 `ha-embed-provider.ts` 并在构造器中调用 。

剧本的制作构件从它来自的网址上加载了它的其他文件,因此它也在其他网址上工作. 开发和遗产是从网页的网址上加载的,因此尝试需要用生产建筑在其他网址上工作的改动。

## 画廊中的翻译和演示 {#translations-in-the-gallery-and-the-demo}

两者都以英语开头. 添加 `--fetch-translations` 来装入最新的翻译, 如 `pnpm dev:demo --fetch-translations` 。 两者也接受[背景标记](/frontend/development/run#keep-a-server-running-in-the-background).
