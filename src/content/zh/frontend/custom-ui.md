---
title: 自定义卡片及其他
description: 构建卡片,卡片特征,徽章,视图,仪表板策略,以及人们加载到自己的Home Assistant的面板,而不改变前端.
order: 30
sidebarLabel: 自定义卡片及其他
---

# 自定义卡片及其他 {#custom-cards-and-more}

内置的卡片覆盖很多,但并非一切. 您可以在不触碰[前端仓库](https://github.com/home-assistant/frontend) 时将自己的构件添加到界面: 写入 JavaScript 文件, 加载到 Home Assistant 中, 像内置文件一样使用 。 数千张社区卡是用这种方式制作的。

## 你能造出来的脸 {#what-you-can-build}

| 什麽? | 它出现的地方 | 页次 |
| --- | --- | --- |
| [纸牌](/glossary/card) | 在仪表盘上ىلع ال ال ال ال . | [自定义卡](/frontend/custom-ui/card) |
| [卡片特性](/glossary/card-feature) | 瓷砖卡或支持特性的另一张卡 | [自定义卡特性](/frontend/custom-ui/card-feature) |
| [徽章](/glossary/badge) | 在风景的顶端 | [自及其家庭徽章](/frontend/custom-ui/badge) |
| [战略](/glossary/strategy) | 从代码生成整个仪表板、视图或一节 | [自定义策略](/frontend/custom-ui/strategy) |
| [视图](/glossary/view) 版式 | 用自己的方式排列视图的牌 | [自定义视图](/frontend/custom-ui/view) |
| [小组讨论会](/glossary/panel) | 自己的完整页面,在侧边栏有链接 | [自定义面板](/frontend/custom-ui/panel) |

## 工作原理 {#how-it-works}

每个都是一个 [自定义元素](https://developer.mozilla.org/docs/Web/API/Web_components/Using_custom_elements): 一个用标签名注册的 JavaScript 类 。 Home Assistant 创建元素, 设置属性, 如 `hass` 和配置, 并放在页面上 。 元素意味着什么 取决于你。

1. ** 在 JavaScript 模块中写入元素**, 用 `customElements.define()` 注册它 。
2. ** 将模块** 输入 Home Assistant 作为 [仪表板资源](/frontend/custom-ui/resources) 。 面板由自己的配置加载。
3. 和平和安全,如 `type: custom:my-card`。

为了方便查找,您也可以注册您的元素,这样它就出现在名片拾单器、名片拾单器和新的仪表板对话框中,并配有可视化编辑器。

## 要使用的工具 {#which-tools-to-use}

您可以使用任何生成标准自定义元素的库, 或者根本不使用 。 这些页面上的例子使用plain JavaScript , 这样您就可以复制它们, 并看到它们工作, 而无需一个构建步骤 。

对于任何更大的,[升](https://lit.dev/)是一个很好的选择:这是前端本身使用的东西,所以[结构](/frontend/architecture)页面上的图案会结转. 将你自己的 Lit 复制本, 或任何其他库, 装入您的模块 。

前端没有用于定制卡的公共组件库. 前端寄存器中没有列表 `ha-*` 元素作为支持, 或者承诺它们保持不变 。 只有在前端需要它们时它们才会被装入,并且它们可以在任何释放中改变. 如果你的卡取决于一个, 它可以打破不警告。

`ha-card`是实践中唯一的例外,不是在纸上。 它是内置的 138.卡的容器,它使用 `--ha-card-background` 和 `--ha-card-border-radius` 等卡片主题变量, 并且大多数自定义卡片将内容包裹在其中, 如 [自定义卡例](/frontend/custom-ui/card) 一样. 使用它让你的卡适合, 但知道它带有 同样的缺乏承诺 与其余。 对于其他任何事物,如拾荒者或表型场,建造或捆绑你自己. 要显示卡片内置的卡片或卡片内的标准对话框之一,请使用[纸牌助手](/frontend/custom-ui/card#card-helpers),前端故意为自定义卡加载该卡片.

## 共同的概念 {#shared-concepts}

- QQH0}**:完全状态为Home Assistant的天体. 你的元素每变一次都会有新的 [有对象引用](/frontend/reference/hass-object) 列出里面的内容 。
- XondaH0}**:以您的卡,徽章或特征的YAML配置调用. 当配置无效时丢出错误, Home Assistant 向用户显示 。
- ** `custom:` 前缀**:将你的元素与内置元素分离。 您的元素 `my-card` 用作 `type: custom:my-card` 。

## 设计 {#design}

符合内置卡的定制卡看起来最好. 使用 [主题变量](/frontend/architecture/theming), 如 `--card-background-color` 和 `--primary-text-color`, 所以您的卡会遵循用户的主题和暗模式 。 设计区[仪表板](/design/dashboards)的页面解释了内置卡片的设计方式和原因.

## 分给大家 {#share-it}

要发布你建造的东西,其他人可以从市场安装,参见[仪表板卡和插件](/marketplace/guides/dashboard). 让人们先在网页上尝试你的卡片,参见[现场演示](/frontend/custom-ui/demo).

你以为你的卡属于前端本身吗? 项目建议您先在 [市场](/marketplace) 中发布新卡 。 你积累经验,你可以更快地运动。 一旦它成熟并拥有用户基础,就联系维护者,比如在[Discord](https://www.home-assistant.io/join-chat/)上的[* * 前端**](https://discord.com/channels/330944238910963714/1475552784278360176)频道,看看它是否应该飞船建造.
