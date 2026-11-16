---
title: 路线和面板
description: URL如何成为页面. 由Core注册的面板,面板解析器,以及每个面板内的路由器.
order: 6
---

# 路线和面板 {#routing-and-panels}

Home Assistant中的每一页都是[面板](/glossary/panel):仪表板,地图,日志,设置,或集成后添加的面板. 侧边栏列出它们,URL的第一部分选择一个.

## 面板来自核心 {#panels-come-from-core}

核心决定了哪些小组。 集成从 `frontend` 集成中以 `async_register_built_in_panel()` 注册它们, 集成取出使面板, URL 路径, 侧边栏标题和图标的前端组件的名称, 以及是否只有管理员可以看到它 :

```python
from homeassistant.components import frontend

frontend.async_register_built_in_panel(
    hass,
    component_name="logbook",
    sidebar_title="logbook",
    sidebar_icon="mdi:format-list-bulleted-type",
)
```

没有充实 `frontend_url_path`, URL 路径就是组件名称, 所以此面板在 `/logbook` 打开 。 内置面板的侧边栏标题是翻译密钥.

前端在启动时获取面板列表, 它以 `hass.panels` 或 `uiContext` 提供 。

`component_name` 是指前端所建的面板. 要在不改变前端的情况下添加一个面板,集成和用户会注册一个自定义面板. 见[自定义面板](/frontend/custom-ui/panel).

## 从 URL 到面板 {#from-url-to-panel}

前端的运行是分散的. 每个关卡只知道自己在 URL 中的一部分, 并传递其余部分。

1. [`src/layouts/partial-panel-resolver.ts`](https://github.com/home-assistant/frontend/blob/dev/src/layouts/partial-panel-resolver.ts) 查看 URL 的第一部分, 找到注册的面板, 并加载其组件的代码 。 将组件名称映射到代码的地图位于该文件的顶部,所以添加一个内置面板意味着添加到那里.
2. 面板得到 `route` 属性 : 具有 `prefix` 的对象, 已经处理的 URL 部分, 其余的 `path` 。
3. 一个有自己网页的面板 将剩下的路线传到他们身上,等等。

楠格只有有人打开时才会加载.

## 面板内的路由器 {#routers-inside-a-panel}

一个有多个页面的面板从 [`src/layouts/hass-router-page.ts`](https://github.com/home-assistant/frontend/blob/dev/src/layouts/hass-router-page.ts) 延伸 `HassRouterPage` 。 其使用方式是,在使用时,使用其使用方式。

```ts
@customElement("ha-panel-profile")
class HaPanelProfile extends HassRouterPage {
  @property({ attribute: false }) public hass!: HomeAssistant;

  @property({ type: Boolean }) public narrow = false;

  protected routerOptions: RouterOptions = {
    defaultPage: "dashboard",
    routes: {
      dashboard: {
        tag: "ha-profile-dashboard",
        load: () => import("./ha-profile-dashboard"),
      },
      security: {
        tag: "ha-profile-section-security",
        load: () => import("./ha-profile-section-security"),
      },
    },
  };

  protected updatePageEl(el) {
    el.route = this.routeTail;
    el.hass = this.hass;
    el.narrow = this.narrow;
  }
}
```

`updatePageEl()`通过页面需要的数据,包括`routeTail`,该页面剩下的路由部分. `RouterOptions` 有更多的选项, 如 `cacheAll` 将页面保存在内存中, 和`beforeRender` 重定向 。

## 导航 {#navigate}

要转到另一页, 请使用 `navigate()` 从 [`src/common/navigate.ts`](https://github.com/home-assistant/frontend/blob/dev/src/common/navigate.ts) 开始, 永远不要 `history.pushState` 直接 :

```ts
navigate("/config/areas/dashboard");
navigate("/config/areas/dashboard", { replace: true });
```

`navigate()` 更新历史, 告诉应用更改位置, 并尊重未保存的更改 。
