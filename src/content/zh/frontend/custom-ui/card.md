---
title: 自定义卡
description: 建立自己的仪表板卡. 元素,它的配置,大小在各段和泥瓦视图,帮助者前端提供.
order: 2
---

# 自定义卡 {#custom-cards}

定制卡是Home Assistant放在仪表板上的定制元素,就像内置卡一样. 它得到它的配置和 Home Assistant 状态, 并做出任何你想要的。

## 第一张牌 {#a-first-card}

在配置文件夹中创建 `www/state-card-example.js` :

```js
class StateCardExample extends HTMLElement {
  // Called with the YAML configuration of the card. Throw an
  // error and Home Assistant shows it instead of the card.
  setConfig(config) {
    if (!config.entity) {
      throw new Error("You need to define an entity");
    }
    this._config = config;
    this._render();
  }

  // Called with a new hass object on every change in the home.
  set hass(hass) {
    this._hass = hass;
    this._render();
  }

  _render() {
    if (!this._config || !this._hass) {
      return;
    }

    const stateObj = this._hass.states[this._config.entity];
    const state = stateObj
      ? this._hass.formatEntityState(stateObj)
      : "not found";

    if (!this._content) {
      this.innerHTML = `<ha-card><div class="content"></div></ha-card>`;
      this._content = this.querySelector(".content");
      this._content.style.padding = "16px";
    }
    this._content.textContent = `${this._config.entity} is ${state}`;
  }

  // Height in the masonry view, in units of 50 pixels.
  getCardSize() {
    return 1;
  }

  // Size in the grid of the sections view.
  getGridOptions() {
    return { columns: 6, rows: 1, min_rows: 1 };
  }
}

customElements.define("state-card-example", StateCardExample);
```

[注册为资源](/frontend/custom-ui/resources) 带有 URL `/local/state-card-example.js` 和 JavaScript 类型的模块 ** 。 然后加入YAML的仪表板:

```yaml
type: custom:state-card-example
entity: light.living_room
```

您注册的标签名称 `state-card-example` 成为 `custom:state-card-example` 类型 。

`ha-card`是内置的卡片用于背景,边框和阴影的元素. 用它,所以你的卡 看起来像其他人,并遵循主题。 和每个 `ha-*` 元素一样, 它不是一个承诺的 API, 见 [用于哪些工具](/frontend/custom-ui#which-tools-to-use) 。

## 人称"人称" {#the-card-api}

| 成员 | 要求数 | 它会做什么 |
| --- | --- | --- |
| `setConfig(config)` | 对 | 接收配置。 很少践行召唤:当卡片创建时,以及配置改变时. 丢践 `Error` 为无效配置 。 |
| `hass` | | 当 Home Assistant 状态发生变化时, 用新 `hass` 对象设定 。 这是经常的。 只有更新改变的东西。 |
| `getCardSize()` | | 砖木景观中的卡片高度,作为数字或承诺数字. 1为50像素. 默认为 1 。 |
| `getGridOptions()` | | 章节视图中的卡片大小 。 |
| `preview` | | 当卡片显示在卡片编辑器中时设定为`true`. |

`hass` 对象在 [有对象引用](/frontend/reference/hass-object) 中描述 。 其格式化器,如`hass.formatEntityState()`和`hass.formatEntityName()`,在用户的语言和单位中将状态和名称变为文本. 用它们而不是显示原始状态。

## 区域视图大小 {#sizing-in-the-sections-view}

一节是12列的网格. 行高56像素,中间有8像素.  10. `getGridOptions()` 告诉网格默认您的卡有多大, 用户可以调整多大大小 :

| 选项 | 默认 | 含义 |
| --- | --- | --- |
| `columns` | `12` | 全宽的列数, 或 `"full"` 。 |
| `rows` | `"auto"` | 行数. 有了`"auto"`,卡片与内容一样高,不能在高度上调整大小. |
| `min_columns`, `max_columns` | | 宽度的限制。 |
| `min_rows`, `max_rows` | | 对高度的限制。 |

没有`getGridOptions()`,卡片会占用部分的全宽,其高度会跟随内容.

对 `columns` 使用 3 的倍数, 如 3、 6、 9 或 12 。 那些与其他的牌排成一行。 `rows: 2`的提供技术咨询卡为120像素高:两行56像素,一个缺口8.

```js
getGridOptions() {
  return { columns: 6, rows: 2, min_rows: 2 };
}
```

## 砖石景观中的大小 {#sizing-in-the-masonry-view}

砖木景观将卡片放在列中,并使用`getCardSize()`进行均匀分布. 当询问另一个元素的大小时, 请等待到定义它, 因为卡片是懒散加载的 :

```js
await customElements.whenDefined(element.localName);
return element.getCardSize();
```

## 仅获得所需数据 {#get-only-the-data-you-need}

`hass` 家里每个州都变了 即使你的卡片都变了 一张卡可以通过请求 [上下文](/frontend/architecture/hass-and-contexts) 来获取数据的一部分。 将牌添加到页面时点火 `context-request` 事件 :

```js
connectedCallback() {
  const event = new CustomEvent("context-request", {
    bubbles: true,
    composed: true,
  });
  event.context = "states";
  event.subscribe = true;
  event.callback = (states, unsubscribe) => {
    this._unsubscribe = unsubscribe;
    this._states = states;
    this._render();
  };
  this.dispatchEvent(event);
}

disconnectedCallback() {
  this._unsubscribe?.();
  this._unsubscribe = undefined;
}
```

回调得到上下文的值,在 `subscribe` 设置后, 它再次被调用到每个更改上 。 删除牌时总是不订阅. 上下文的密钥,如`states`,`entities`,`hassApi`和`hassInternationalization`,在[`src/data/context/index.ts`](https://github.com/home-assistant/frontend/blob/dev/src/data/context/index.ts)中定义.

## 卡片助手 {#card-helpers}

前端为定制卡提供少数帮手,比如在您内部创建内置卡:

```js
const helpers = await window.loadCardHelpers();
const card = helpers.createCardElement({
  type: "tile",
  entity: "light.living_room",
});
card.hass = this._hass;
```

`loadCardHelpers()` 一旦装入仪表盘面板就可使用 。 它返回 `createCardElement`,`createBadgeElement`,`createRowElement`,`createHeaderFooterElement`和`createHuiElement`,对话框 `showAlertDialog`,`showConfirmationDialog`,`showPromptDialog`,和`showEnterCodeDialog`和`importMoreInfoControl`。 一张卡是这样创建的 需要 `hass` 设定, 和你一样。

## 下一步 {#next-steps}

- 添加可视化编辑器,并将您的卡片放入拾卡器: [卡片编辑器和拾卡器](/frontend/custom-ui/card-editor).
- 在平板卡上添加快速控件 : [自定义卡特性](/frontend/custom-ui/card-feature).
