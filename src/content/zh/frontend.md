---
title: 前端
description: Home Assistant的网页界面. 如何建造,如何进行,以及如何用自己的卡片,面板和仪表板来扩展.
---

# 前端 {#frontend}

前端是人们在Home Assistant中看到和触摸的一切:仪表板,设置页面,自动化编辑器,更多信息对话框,以及所有其他屏幕. 同样的代码在浏览器中运行,在[辅助应用程序](/glossary/companion-app)中运行,在某人的走廊的墙板上运行. 它住在自己的仓库里:[Home Assistant/前端](https://github.com/home-assistant/frontend).

这是一个 TypeScript 应用程序, 由 [升](https://lit.dev/) 的 Web 组件构建 。 它通过一个 WebSocket 连接与 [Home Assistant Core](/glossary/core) 交谈, 并保持同步, 随着家庭事物的变化。

## 这个区域是给谁的 {#who-this-area-is-for}

- **Frontend 贡献者**,他们想要修复一个bug,擦亮一个屏幕,或者在前端本身构建一个新的功能.
- ** 集成开发者** 其后端更改需要界面中的新内容,比如一个更信息视图或WebSocket命令.
- **第三方开发者**,他们构建[定制卡](/glossary/custom-card),卡片的现有特征,徽章,仪表板策略,或者人们自行安装的面板.
- **Concanion应用程序开发者**将前端嵌入本地应用程序.

您需要熟悉在 TypeScript 或 JavaScript 、 HTML 和 CSS 周围的路 。 Lit和Web组件很容易被捡起来

## 很快,到处都是 {#fast-and-everywhere}

前端是一个进步的网络应用,设计为移动先. 它必须对其他没有记忆的Android手机的预算快速,它必须继续工作在几年前停止更新的老牌匾上. 为了做到这两点,每艘释放船都会建造两艘:

- ** Modern**:用于过去两年发行的浏览器. 少转经络,少复经络,如经之速.
- 103. **Legacy**:对于更古老的浏览器,下至被钉在[`.browserslistrc`](https://github.com/home-assistant/frontend/blob/dev/.browserslistrc)的地板,如旧iPads上的Safari 12和旧Fire平板电脑上的Chrome 59。

Home Assistant 为每个浏览器服务它可以运行的构建. 在添加依赖性或新浏览器 API 时,同时记住两者.

## 从这里开始 {#start-here}

- [您的第一个前端贡献](/frontend/first-contribution):设置环境,选择一个问题,打开一个pull request.
- [自定义卡片及其他](/frontend/custom-ui):为您的仪表板打造自己的卡片. 不需要开发环境 : 您 Home Assistant 中的 JavaScript 文件足以启动 。
- 拂晓 [打开 pull request](/frontend/development/pull-requests): 您的pull request 需要什么才能得到审查 。
- [审查和发布](/frontend/development/review-and-release) : 您的pull request 会发生什么, 以及它是如何到达用户的 。

## 指南和参考 {#guides-and-reference}

- [开发](/frontend/development):开发环境,运行前端,画廊和演示,编码指南,以及测试.
- [架构](/frontend/architecture):前端是如何组合的. Lit 和 `ha-*` 组件, `hass` 对象和上下文, 数据层, 翻译, 主题, 路由, 和面板 。
- [自定义卡片及其他](/frontend/custom-ui):构建卡片,卡片特征,徽章,视图,策略,以及人们加载到自己Home Assistant的面板.
- [扩展前端](/frontend/extending): 添加一个域名的更多信息视图或状态卡, 或您的整合命令 WebSocket 。
- [参考](/frontend/reference):命令,`hass`对象,外部认证,以及伴侣应用所使用的外部总线.

## 相关领域 {#related-areas}

- [设计](/design):界面背后的原则和基础. [组件](/design/components)、[仪表板卡](/design/dashboards)和[啊 更多信息视图](/design/more-info) 都有一个页面, 供设计者和开发人员使用, 上面有现场实例和每个实例的代码侧面 。
- 凛 [翻译](/translate):前端的英文文本由社区翻译. [让你的弦可变](/translate/guides/developers)解释如何写出翻译可以合作的字符串.
- [核心与集成](/core): 后端的前端对白
- [伴侣应用](/companion):包裹前端的Android和iOS应用程序.

## 谁说话 {#who-to-talk-to}

- [* * 前端**](https://discord.com/channels/330944238910963714/1475552784278360176) [Home Assistant Discord](https://www.home-assistant.io/join-chat/) 上的频道是前端的提问地点 。 看不到频道吗? 在 **ỗnels & 角色**----下,选择 ** 我想贡献 dev 技能给 Home Assistant**>.
- 界面中的臭虫和 pull request 生活在 [前端仓库](https://github.com/home-assistant/frontend) 。 新特性的想法会转到 [讨论](https://github.com/orgs/home-assistant/discussions) 。
- 设计和UX问题到[UX设计讨论](https://github.com/OpenHomeFoundation/ux-design/discussions),或[设计人员**](https://discord.com/channels/330944238910963714/1463606665311158284)频道在Discord来吧.archive. 产品和UX讨论发生在[产品和工具**](https://discord.com/channels/330944238910963714/1475553148847526123).

当向前推进时,将自己的作品推向一个分支并共享链接. 当人们看到密码时 帮助你的速度要快得多
