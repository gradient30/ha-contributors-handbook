---
title: 自及其家庭徽章
description: 为仪表板视图的顶端建造自己的徽章.
order: 5
---

# 自及其家庭徽章 {#custom-badges}

[徽章](/glossary/badge)是一景上方的小丸,在牌上方. 它们一眼就显示出一个状态, 就像外面的温度或者有多少灯光。 定制徽章的构造方式与[定制卡](/frontend/custom-ui/card)相同,只是较小.

## 梢一个例子 {#an-example}

```js
class TextBadge extends HTMLElement {
  setConfig(config) {
    if (!config.entity) {
      throw new Error("You need to define an entity");
    }
    this._config = config;
    this._render();
  }

  set hass(hass) {
    this._hass = hass;
    this._render();
  }

  _render() {
    if (!this._config || !this._hass) {
      return;
    }
    const stateObj = this._hass.states[this._config.entity];
    this.textContent = stateObj
      ? this._hass.formatEntityState(stateObj)
      : "Unavailable";
  }
}

customElements.define("text-badge", TextBadge);
```

装入为 [资源](/frontend/custom-ui/resources),并添加到视图中:

```yaml
views:
  - title: Home
    badges:
      - type: custom:text-badge
        entity: sensor.outside_temperature
```

## 警徽会怎样? {#what-a-badge-gets}

- `setConfig(config)`:徽章的配置. 丢弃无效配置错误, 而 Home Assistant 显示错误徽章 。
- `hass`: Home Assistant的完整状态, 设定在每次更改上 。
- `preview`:`true`当徽章在徽章编辑器中显示时.

## 徽章拾取者和编辑器 {#badge-picker-and-editor}

在警徽选手中显示您的警徽, 推入 `window.customBadges` :

```js
window.customBadges = window.customBadges || [];
window.customBadges.push({
  type: "text-badge",
  name: "Text badge",
  description: "Shows the state of an entity as text.",
  preview: true,
  documentationURL: "https://example.com/text-badge",
});
```

键与[选牌员的牌](/frontend/custom-ui/card-editor#show-up-in-the-card-picker)的键相同,一个徽章也可以为拥有`getEntitySuggestion`的实体暗示自己.

徽章也可以有视觉编辑器和默认配置. 静态的 `getStubConfig()` , `getConfigForm()` 和 `getConfigElement()` 工作与 [定制卡](/frontend/custom-ui/card-editor) 完全一样 。
