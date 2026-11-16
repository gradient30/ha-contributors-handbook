---
title: 自定义视图
description: 写你自己的视图布局,以内置视图不能的方式安排仪表板视图的卡片.
order: 7
---

# 自定义视图 {#custom-views}

A [视图](/glossary/view) 决定其牌的排列方式 。 内置的景色类型是区段,泥瓦,侧边栏,以及面板. 自定义视图类型允许您写出自己的布局,比如自由形式的画布或固定的网格.

各种各样卡片和徽章,并不断更新。 你的观点只把它们放进去

> [!NOTE]
> 想要从代码生成视图的卡片吗 ? 那是[视图战略](/frontend/custom-ui/strategy#a-view-strategy),不是自定义视图。

## 梢一个例子 {#an-example}

```js
class MyNewView extends HTMLElement {
  setConfig(config) {
    this._config = config;
  }

  set cards(cards) {
    this._cards = cards;
    this._render();
  }

  _render() {
    this.style.display = "grid";
    this.style.gridTemplateColumns = "repeat(auto-fill, minmax(300px, 1fr))";
    this.style.gap = "8px";
    this.replaceChildren(...this._cards);
  }
}

customElements.define("my-new-view", MyNewView);
```

装入为 [资源](/frontend/custom-ui/resources) , 并将其设置为视图类型 :

```yaml
views:
  - title: Home
    type: custom:my-new-view
    cards:
      - type: tile
        entity: light.living_room
```

## 这方面的工作 {#what-a-view-gets}

| 财产 | 这是什么 |
| --- | --- |
| `setConfig(config)` | 风景的配置. |
| `hass` | Home Assistant的完整状态。 |
| `lovelace` | 仪表板:它的配置,是否处于编辑模式,以及保存它的功能. |
| `narrow` | 在狭长的屏幕上。 |
| `path` | 视图在仪表盘配置中的位置, 如 `["views", 0]` 。 |
| `cards` | 有什么事吗? |
| `badges` | 徽标元素. |

[砖荚视图](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/views/hui-masonry-view.ts) 是视图元素的内置示例 。

## 每张卡存储布局数据 {#store-layout-data-per-card}

如果您的视图需要记住每张卡的某样东西,比如位置或大小,请将其存储在卡的`view_layout`选项中. Home Assistant 保持卡片配置, 并忽略它 :

```yaml
- type: tile
  entity: light.living_room
  view_layout:
    column: 2
    row: 1
```

## 编辑、删除和添加牌 {#edit-delete-and-add-cards}

在编辑模式中,您的视图可以通过点火事件打开仪表盘编辑器的对话框. 每个事件在仪表板配置中都有卡片的`path`:您的视图的`path`,然后是`"cards"`和卡片的索引.

| 积极地濑子事件 | 茁壮 | 它会做什么 |
| --- | --- | --- |
| `ll-create-card` | `{ path: [...path, "cards"] }` | 取牌者,以加于景. |
| `ll-edit-card` | `{ path: [...path, "cards", index] }` | card卡编辑. |
| `ll-delete-card` | `{ path: [...path, "cards", index], silent: false }` | 删除卡片。 使用 `silent: false` , 随附带有撤消按钮的信件 。 |

释放他们,让他们发泡,穿过阴影的根部:

```js
this.dispatchEvent(
  new CustomEvent("ll-edit-card", {
    detail: { path: [...this.path, "cards", 3] },
    bubbles: true,
    composed: true,
  })
);
```

旧视图只发送一条数字路径,如`[0, 3]`为第一视图的第四张卡片. 现在还行
