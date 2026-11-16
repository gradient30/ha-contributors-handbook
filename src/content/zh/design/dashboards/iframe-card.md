---
title: 网页卡
description: 珂拉卡在仪表板上嵌入另一个网页,一个iframe.
sidebarGroup: 不用 页所提供的就有业已协商 为什么 就是的支持支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援
  支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援
  支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援支援
---

# 网页卡 {#webpage-card}

盘 联卡的现场演示,从Home Assistant演示的嵌入,连接到这个站点的样本主场.

```html
<ha-embed-provider
  style="
    display: grid;
    grid-template-columns: repeat(12, minmax(0, 1fr));
    gap: 8px;
    align-items: start;
    max-width: 500px;
  "
>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "iframe",
        "url": "https://www.home-assistant.io",
        "aspect_ratio": "50%"
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

## 使用量 {#usage}

网页卡在仪表板内显示另一个网页. 在拾卡器中它被称为**Webpage**,在YAML中它的类型是`iframe`,因为这就是它:一个卡片中的iframe.

用于 Home Assistant 没有卡片的事物,但是在网页上直播的:本地天气雷达,网络上另一个系统的仪表板,或者设备的状态页. 只要有名片,就选一张 一张卡跟随主题,语言,和Home Assistant状态. 一个嵌入式的页面不做这些, 它自己滚动,在仪表盘内。

该卡没有贴纸,默认没有标题. 页面从边端填满,卡片的圆角.

### 标题 {#title}

使用`title`,卡片在页面上方获得一个头. 页面本身未明确内容时使用.

盘 联卡的现场演示,从Home Assistant演示的嵌入,连接到这个站点的样本主场.

```html
<ha-embed-provider
  style="
    display: grid;
    grid-template-columns: repeat(12, minmax(0, 1fr));
    gap: 8px;
    align-items: start;
    max-width: 500px;
  "
>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "iframe",
        "title": "Home Assistant",
        "url": "https://www.home-assistant.io",
        "aspect_ratio": "75%"
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

### 光谱比 {#aspect-ratio}

在区段视图之外,卡的高度来自`aspect_ratio`:高度与宽度的百分比,如`50%`,或如`16:9`的比例. 没有它,卡片的一半是宽的。 在各节视图中,网格决定大小,宽比被忽略.

### 隐藏背景 {#hide-background}

有了`hide_background`,卡片没有背景,边框,或者阴影. 用于一个有自己背景的页面,因此看起来像是仪表板的一部分,而不是一个框中的页面.

### 可能出错的事 {#things-that-can-go-wrong}

不是每个页面都可以嵌入. 许多网站告诉浏览器不要在iframe中显示它们,然后卡片保持空白. 卡片对此无能为力。

当Home Assistant通过HTTPS服务时,页面也必须使用HTTPS. 浏览器屏蔽了混音,因此该卡没有空卡,而是显示一个错误来解释原因.

### 内容 {#content}

- ắn 选择一个能用到卡片大小的页面 理想的是一个被嵌入的
- 记住页面运行在 Home Assistant 内部 。 只有你信任的网页

## 配置 {#configuration}

- `url`(字符串,需要):要显示的页面地址.
- `title` (字符串):页上的一个标题.
- `aspect_ratio`(字符串):卡的高度,作为宽度的百分比或比例. 默认为 `50%` 。 在章节视图和面板视图中被忽略 。
- `hide_background`(boolean):删除卡片的背景,边框和阴影. 默认为 `false` 。
- `allow` (字符串): iframe的权限政策, 如 `fullscreen; camera`. 默认为 `fullscreen` 。
- `allow_open_top_navigation` (boolean): 让页面中的链接,由用户选择,在整个窗口中打开. 默认为 `false` 。
- `disable_sandbox` (boolean):去掉iframe的沙盒. 默认为 `false` 。

```yaml
type: iframe
url: "https://www.home-assistant.io"
aspect_ratio: "75%"
```

## 在代码中 {#in-code}

牌居于[`src/panels/lovelace/cards/hui-iframe-card.ts`](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-iframe-card.ts),元素为`<hui-iframe-card>`. 它使 `<iframe>` 在 `<ha-card>` 内部。 宽比在包装上变成 `padding-top`, iframe 绝对位于顶部 。

iframe 默认为沙盒,其权限来自 `IFRAME_SANDBOX` [`src/util/iframe.ts`](https://github.com/home-assistant/frontend/blob/dev/src/util/iframe.ts) : 窗体, 弹出, 脚本, 以及其中相同的来源 。 牌投 `Invalid URL` 用于将 `about:blank` 消毒到 `about:blank` 的地址, 如 `javascript:` URL,因为沙盒保持相同的来源.

在片段视图中,卡片取全宽和4行,可以缩到3列和2行.

[来源](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-iframe-card.ts)
