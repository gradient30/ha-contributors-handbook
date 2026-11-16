---
title: 自定义卡特性
description: 将自己的快速控制器添加到瓦片卡和其他支持特性的卡片中.
order: 4
---

# 自定义卡特性 {#custom-card-features}

[卡片特性](/glossary/card-feature)是牌底部的小控件:亮度滑动器,一行扇速,启动真空的按钮. 内置的涵盖许多实体,你可以加入自己的实体. 一个特性是一个自定义元素,很像[定制卡](/frontend/custom-ui/card),但较小.

## 梢一个例子 {#an-example}

此特性为 [按钮实体](/core/entities/button) 添加了 ** press** 按钮 :

```js
const supportsButtonPress = (hass, context) => {
  const entityId = context.entity_id;
  return Boolean(entityId?.startsWith("button.") && hass.states[entityId]);
};

class ButtonPressCardFeature extends HTMLElement {
  setConfig(config) {
    if (!config) {
      throw new Error("Invalid configuration");
    }
    this._config = config;
    this._render();
  }

  set hass(hass) {
    this._hass = hass;
    this._render();
  }

  set context(context) {
    this._context = context;
    this._render();
  }

  static getStubConfig() {
    return { type: "custom:button-press-card-feature", label: "Press" };
  }

  _render() {
    if (!this._config || !this._hass || !this._context) {
      return;
    }
    if (!supportsButtonPress(this._hass, this._context)) {
      // Forget the button, so it is created again when the entity is back
      this.replaceChildren();
      this._button = undefined;
      return;
    }
    if (!this._button) {
      this._button = document.createElement("button");
      this._button.style.cssText =
        "width: 100%; height: var(--feature-height, 42px);" +
        "border: none; border-radius: var(--feature-border-radius, 12px);";
      this._button.addEventListener("click", (ev) => this._press(ev));
      this.replaceChildren(this._button);
    }
    this._button.textContent = this._config.label || "Press";
  }

  _press(ev) {
    ev.stopPropagation();
    this._hass.callService("button", "press", {
      entity_id: this._context.entity_id,
    });
  }
}

customElements.define(
  "button-press-card-feature",
  ButtonPressCardFeature
);

window.customCardFeatures = window.customCardFeatures || [];
window.customCardFeatures.push({
  type: "button-press-card-feature",
  name: "Button press",
  isSupported: supportsButtonPress,
  configurable: true,
});
```

将文件装入 [资源](/frontend/custom-ui/resources) , 并将此特性添加到瓷砖卡中 :

```yaml
type: tile
entity: button.restart_router
features:
  - type: custom:button-press-card-feature
    label: Restart
```

停止事件卷起, 如 `_press()` , 或下面的卡片也处理它并打开更多信息对话框 。

## 有个什么特点 {#what-a-feature-gets}

- `setConfig(config)`:特性的配置,带有它的`type`.
- `hass`: Home Assistant的完整状态, 设定在每次更改上 。
- `context`:该功能所居住的卡片的内容. 当卡片显示一个实体时,它有一个`entity_id`,当它显示一个区域时,它有一个`area_id`。

## 西西西西西西西西西西西西西西西西西西西西西西西西西西西西西西西西西西西西西西南西西西西南西西西西南西西西西西西西西南西南西西西西西南西南西西南西南西西西南西南西南西南西南西南西南西西南西南西南西南西南西南西南西南西南西南西西南西南西南西南西南西南西南西南西南西南西南西南西南西南西南西南西南西南西南西南西南西南西南西南西南西南西南西南西南西南西南西南西南西南西南西南西南西南西南西南西南西西南西南西南西南西南西南西西南西南西南西西南西南西南西南西南西南西南西南西西南西南西南西南西南西南西南西南西南西南西南西南西 {#register-the-feature}

要在卡片编辑器的特性拾取器中显示您的特性, 请将一个条目推到 `window.customCardFeatures` :

| 密钥 | 要求数 | 含义 |
| --- | --- | --- |
| `type` | 对 | 您特性的标签名称, 不包含 `custom:` 。 |
| `name` | | 采者中名 The. |
| `isSupported(hass, context)` | | 返回该功能是否适用于它将要进入的卡片 。 拾取器仅在返回 `true` 时才会提供 。 |
| `configurable` | | 设定为 `true` 当特性有选项需要编辑时 。 默认为 `false` 。 |

总是定义`isSupported`. 没有它,就向每个实体提供这种特征,包括它不为那些实体服务。

一个功能可以有一个视觉编辑器,就像一个卡: 静止的 `getConfigElement()` 和 `getConfigForm()` 与 [定制卡](/frontend/custom-ui/card-editor) 的功能相同. `getStubConfig(hass, context)` 返回开始的配置, 包括其`type` 。

## 适应于 {#fit-in}

特质坐落在紧凑的空间中. 使用与内置功能相同的变量,所以你的行与它们:

| 变量 | 默认 | 用它 Is it for |
| --- | --- | --- |
| `--feature-height` | `42px` | 你控制得这么高 |
| `--feature-border-radius` | `12px` | 按钮和滑块的角落。 |
| `--feature-button-spacing` | `12px` | 按钮之间的空间 。 |
