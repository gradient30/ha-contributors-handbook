---
title: 构成部分和语文
description: 网络组件,Lit, 和共享的ha -* 组件包罗Web Aweasy。 每个屏幕的构件。
order: 1
---

# 构成部分和语文 {#components-and-lit}

界面的每一块都是自定义元素:以标签名称注册的类,其自己的模板和样式以阴影根的形式出现. 前端用 [升](https://lit.dev/) 写它们, 一个小的库, 将反应特性和高效的模板添加到标准网络组件中.

## 构成部分 {#a-component}

典型的成分是这样的:

```ts
import { css, html, LitElement, nothing } from "lit";
import { customElement, property, state } from "lit/decorators";

@customElement("ha-example-row")
export class HaExampleRow extends LitElement {
  @property() public label?: string;

  @state() private _expanded = false;

  protected render() {
    if (!this.label) {
      return nothing;
    }

    return html`
      <button @click=${this._toggle}>${this.label}</button>
      ${this._expanded ? html`<slot></slot>` : nothing}
    `;
  }

  private _toggle() {
    this._expanded = !this._expanded;
  }

  static styles = css`
    :host {
      display: block;
      padding: var(--ha-space-2);
    }
  `;
}

declare global {
  interface HTMLElementTagNameMap {
    "ha-example-row": HaExampleRow;
  }
}
```

- `@property()`是公共API,由使用该元素的人设置. `@state()`是内部的。 改变任何一个时间表 一个渲染。
- `render()` 返回模板 。 Lit只更新了DOM中变化的部分.
- 样式被阴影根范围化到组件.
- `HTMLElementTagNameMap` 声明给出了其他代码元素的类型 。

[公升文档](https://lit.dev/docs/)涵盖其余部分:生命周期、指令和反应控制器。

## 命名 {#naming}

标记名称 :

- `ha-*`:在[`src/components/`](https://github.com/home-assistant/frontend/tree/dev/src/components)中共享Home Assistant组件,如`ha-button`或`ha-entity-picker`。
- `hui-*`: [`src/panels/lovelace/`](https://github.com/home-assistant/frontend/tree/dev/src/panels/lovelace)中的仪表板组件, 如`hui-tile-card`.长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长的长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长
- `dialog-*`: 对话框。
- `more-info-*` 和 `state-card-*`: 更多信息对话框和状态卡的视图, 每个域一个 。

## 共享组件和网络真棒 {#shared-components-and-web-awesome}

[`src/components/`](https://github.com/home-assistant/frontend/tree/dev/src/components)中共享的组件是每个屏幕的构件:按钮、输入、对话框、拾取器和控件。 好啦,他们中有许多,比如`ha-button`,`ha-dialog`,`ha-dropdown`,`ha-switch`,`ha-slider`,和`ha-tooltip`,从[网络真棒](https://webawesome.com/)包裹一个组件. 前端使用自己的Web Super, `@home-assistant/webawesome`的构建.

一个包装器扩展了Web Awesome类,并添加主题和行为 Home Assistant 需要:

```ts
import Button from "@home-assistant/webawesome/dist/components/button/button";

@customElement("ha-button")
export class HaButton extends Button {
  // Home Assistant variants, styles, and theme variables
}
```

总是使用 `ha-*` 元素, 绝不直接使用 Web Super 元素 。 包装器是主题,翻译, 和修复 Home Assistant 生活的地方, 它使每个屏幕保持一致 。

前端的旧部分仍然使用材料Web组件(`mwc-*`). 他们正在被替换。 别添新.

每个共享组件在 [设计区](/design/components) 中有一个页面, 并附有使用指导, 活例, 及其属性 。 在你创造新东西之前看看

## 混合和控制器 {#mixins-and-controllers}

一些行为通过混音和反应控制器而不是基类共享:

- `SubscribeMixin` 从[`src/mixins/subscribe-mixin.ts`](https://github.com/home-assistant/frontend/blob/dev/src/mixins/subscribe-mixin.ts) 管理 WebSocket 订阅一个组件 。 见[数据层](/frontend/architecture/data)。
- `DialogMixin` 从[`src/dialogs/dialog-mixin.ts`](https://github.com/home-assistant/frontend/blob/dev/src/dialogs/dialog-mixin.ts) 处理新对话框的打开和关闭 。
- [`src/common/decorators/`](https://github.com/home-assistant/frontend/tree/dev/src/common/decorators) 拥有像 `@consume` 和 `@consumeEntityState` 那样消耗上下文的装饰器, 并像 `@transform` 那样进行转换 。 见[对象和上下文](/frontend/architecture/hass-and-contexts)。
