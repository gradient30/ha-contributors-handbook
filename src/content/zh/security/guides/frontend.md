---
title: 前端的不可信内容
description: 实体名称,属性,Markdown,和URL都可以来自任何地方. 前端如何逃脱,消毒,检查,以及你需要做什么.
sidebarLabel: 前端
order: 2
---

# 前端的不可信内容 {#untrusted-content-in-the-frontend}

前端显示没有写入的数据 。 设备名称来自设备. 属性来自云服务. Markdown卡显示一个用户,或者一个模板,放入其中. 其中任何一种都可以包含HTML,如果前端使HTML成为-是,它运行在打开仪表板的每个人的浏览器中. 这是跨站脚本(XSS).

这不是理论上的。 XSS是[过去的建议](/security/reference/advisories#cross-site-scripting)中最常见的错误类型 Home Assistant. 见[以前发生什么了](/security/guides/frontend#what-went-wrong-before)。

规则很简单:将每一个到达前端的字符串当作数据,永远不要当作标记.

## 让Lit来逃 {#let-lit-do-the-escaping}

Lit 逃脱了您放入模板中的值, 所以一个充满 HTML 的名称会显示为文本 。 这是最安全的方法来渲染任何东西,这也是为什么前端将其图表工具提示移动到Lit模板:用户控制的字段如友好名称和设备名称自动逃脱,而不是依赖每个字符串的过滤器.

```ts
// Escaped by Lit: a name with HTML in it shows as text
return html`${entityName}: ${value}`;
```

问题始于您将 HTML 构建为字符串,然后将字符串交给一个能使其产生它的东西。

- 可否使用外部数据设置 `innerHTML` 。 设定 `textContent` 代替 。可否把地图卡修好?
- 避开`unsafeHTML`。 今天,前端只在`ha-markdown-element`中使用它,使已经消毒的Markdown化.
- 一些焰库,如图表和地图,取HTML字符串作为工具提示或弹出. 当库通过以下支持时, 优先选择 Lit 模板 。

## 当您必须构建 HTML 字符串时 {#when-you-must-build-an-html-string}

如果无法绕过字符串, 请通过 `filterXSS` 从 [`src/common/util/xss.ts`](https://github.com/home-assistant/frontend/blob/dev/src/common/util/xss.ts) 传递每个未信任的部分 :

```ts
import { filterXSS } from "../../common/util/xss";

return `${filterXSS(path.name ?? "")}<br>${formattedTime}`;
```

`filterXSS` 有一个空的许可列表, 所以没有标记可以通过 。 用于以 HTML 结尾的纯文本,而不是应当保持格式化的内容。

## 标记 {#markdown}

带有 `<ha-markdown>` 组件的 Render Markdown 。 它将Markdown转换为HTML,然后用标签和属性的允许列表过滤结果. 只有名单上的东西才能通过

`<ha-markdown>` 有 `allow-svg` 选项 。 代码对此很明确:不允许对不可信内容进行SVG,允许XSS. 在前端,它在配置流程对话框和动作编辑器等地方打开.

## 链接 {#links}

URL 也可能是危险的 : `javascript:` 链接中的 URL 在选择时运行代码 。 作为数据到达前端的每个URL,从一个集成表,一个app,一个配置流,或者一个实体属性,都应该先通过检查. 帮助者居住在 [`src/common/url/sanitize-http-url.ts`](https://github.com/home-assistant/frontend/blob/dev/src/common/url/sanitize-http-url.ts) :

- 尖端 `sanitizeHttpUrl(url)` 返回 URL 时, 只有当它是一个绝对的 `http:` 或 `https:` URL, 否则 `undefined` 。
- `sanitizeLinkUrl(url)`也接受`homeassistant://`的深层链接,把它们变成前端内部的路径. 仅拆解方案是不够的: `homeassistant:///example.com` 将变成`//example.com`, 这指向另一个站点 。

```ts
const releaseUrl = sanitizeHttpUrl(stateObj.attributes.release_url);
```

## 以前发生什么了? {#what-went-wrong-before}

- ** 工具提示中的名称。 ** [能量仪表板的图表工具提示](https://github.com/home-assistant/core/security/advisories/GHSA-mq77-rv97-285m) 中的实体名称, [算法的算法是,](https://github.com/home-assistant/core/security/advisories/GHSA-46j8-vpx8-6p72) 中的实体名称, 和[地图谢谢](https://github.com/home-assistant/core/security/advisories/GHSA-r584-6283-p7xc) 中的设备名称, 最终都出现在 HTML 字符串中 。 能量仪表板中的名称可以来自集成的云服务,而不仅仅是用户.
- *没有消毒剂的马克顿* 2017年的第一个咨询是[Markdown 输出中的 XSS](https://github.com/home-assistant/frontend/pull/514).
- ** A `javascript:` URL. ** 一个 `redirect_uri` 发布的登录客户端没有检查它的方案, 而[运行代码](https://github.com/home-assistant/core/security/advisories/GHSA-jvxq-x42r-f7mv) 在前端 。
- ** 选择服务器的 URL 参数。 ** 登录链接可以使前端 [连接到假 WebSocket 服务器](https://github.com/home-assistant/core/security/advisories/GHSA-cr83-q7r2-7f5q) , 然后发送它喜欢的 。

## 相关 {#related}

- [过去的建议](/security/reference/advisories):每一次咨询,按种类分组.
- [安全阖门](/security/reference/helpers#frontend):表里的前端助手.
- [安全融合](/security/guides/integrations):数据来自另一边。
- [前端](/frontend):前端是如何构建的.
