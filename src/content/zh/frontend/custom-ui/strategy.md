---
title: 自定义策略
description: 生成一个完整的仪表盘,一个视图,或者从代码中生成一节,并在仪表盘编辑器中提供.
order: 6
---

# 自定义策略 {#custom-strategies}

[战略](/glossary/strategy) 是写一个仪表板配置的代码 。 仪表板没有列出卡片,而是说"使用这个策略",策略从家里的东西产生卡片,每次仪表板加载. ** 概览** 仪表板Home Assistant 为你建造的仪表板、区域仪表板、地图和能量仪表板都是战略。

有三个类型:

- 一个** dashboard 策略** 生成整个仪表板,并带有所有视图.
- ** 视图战略** 产生一种观点。
- ** 节战略** 在一节视图中产生一节。

他们一起工作。 仪表盘策略常常生成一个视图列表,每个视图都使用一个视图策略,所以每个视图只有在有人打开时才会构建.

## 战略如何运作 {#how-a-strategy-works}

策略是带有静态`generate()`方法的自定义元素. 它获得策略配置和`hass`,并返回它生成的东西的配置:一个仪表板,一个视图,或者一个部分.

标记名称决定类型 : `ll-strategy-dashboard-<name>`, `ll-strategy-view-<name>`, 或 `ll-strategy-section-<name>` 。 `<name>` 是配置中后面的 `custom:` 。 `strategy` 区域中的所有东西, 包括您自己的选项, 都传递到 `generate()` 作为 `config` 。

将您的策略装入 [资源](/frontend/custom-ui/resources), 如定制卡 。

[内置战略](https://github.com/home-assistant/frontend/tree/dev/src/panels/lovelace/strategies)是很好的例子。 [地图仪表板战略](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/strategies/map/map-dashboard-strategy.ts)是一个小的。

## 仪表板战略 Agendaa {#a-dashboard-strategy}

仪表盘策略返回整个仪表盘配置:

```js
class MyDemoDashboardStrategy extends HTMLElement {
  static async generate(config, hass) {
    const name = hass.config.location_name || "Home Assistant";

    return {
      title: config.title || "My demo dashboard",
      views: [
        {
          title: "Home",
          path: "home",
          cards: [
            { type: "markdown", content: `

# Welcome to ${name}` }, {#suggest-a-title-and-icon}
            { type: "entities", entities: ["sun.sun"] },
          ],
        },
      ],
    };
  }
}

customElements.define(
  "ll-strategy-dashboard-my-demo",
  MyDemoDashboardStrategy
);
```

用作仪表板的配置 :

```yaml
strategy:
  type: custom:my-demo
  title: Generated dashboard
```

提供了关于 `strategyType: "dashboard"` 的 [登记](/frontend/custom-ui/strategy#register-your-strategy) , 用户可以在对话框中的 **Community 仪表板 ** 下选择, 添加一个仪表板 。

### 69. 提议标题和图标 {#a-view-strategy}

一个仪表盘策略可以以静态的`getCreateSuggestions(hass)`建议新仪表盘的标题和图标. 用户在创建之前仍然可以同时改变两者.

```js
static getCreateSuggestions(hass) {
  return { title: "My demo dashboard", icon: "mdi:view-dashboard" };
}
```

## 观点战略 {#a-section-strategy}

一个视图的策略返回一个视图的配置. 在任何的仪表板视图中使用:

```yaml
views:
  - strategy:
      type: custom:my-area
      area: living_room
```

以下观点战略显示一个领域的实体。 上面的仪表板战略为每个领域创造了一种视野。 `hass.areas`,{H 87.},和`hass.entities` 持有登记册,所以不需要拿任何东西。

```js
class MyAreaDashboardStrategy extends HTMLElement {
  static async generate(config, hass) {
    return {
      title: config.title || "Areas",
      views: Object.values(hass.areas).map((area) => ({
        title: area.name,
        path: area.area_id,
        strategy: { type: "custom:my-area", area: area.area_id },
      })),
    };
  }
}

class MyAreaViewStrategy extends HTMLElement {
  static async generate(config, hass) {
    const areaId = config.area;
    const areaDevices = new Set(
      Object.values(hass.devices)
        .filter((device) => device.area_id === areaId)
        .map((device) => device.id)
    );

    const cards = Object.values(hass.entities)
      .filter(
        (entity) =>
          entity.area_id === areaId ||
          (!entity.area_id && areaDevices.has(entity.device_id))
      )
      .map((entity) => ({ type: "tile", entity: entity.entity_id }));

    return { cards: [{ type: "grid", cards }] };
  }
}

customElements.define(
  "ll-strategy-dashboard-my-area",
  MyAreaDashboardStrategy
);
customElements.define("ll-strategy-view-my-area", MyAreaViewStrategy);
```

两者都使用名称`my-area`:一个作为仪表板策略,一个作为视图策略. 这很好,因为那种是标记名称的一部分。

## 款次战略 {#show-a-preview}

区块策略返回一个区块的配置,带有它的牌. 在常规部分旁边的一节视图中使用:

```yaml
views:
  - type: sections
    sections:
      - strategy:
          type: custom:my-domain
          domain: light
```

下面的章节策略显示一个域的每个注册实体的瓦片,像所有灯光一样:

```js
class MyDomainSectionStrategy extends HTMLElement {
  static async generate(config, hass) {
    const cards = Object.keys(hass.entities)
      .filter((entityId) => entityId.startsWith(`${config.domain}.`))
      .map((entityId) => ({ type: "tile", entity: entityId }));

    return { type: "grid", cards };
  }
}

customElements.define(
  "ll-strategy-section-my-domain",
  MyDomainSectionStrategy
);
```

[登记](/frontend/custom-ui/strategy#register-your-strategy)与 `strategyType: "section"`,用户在创建一个区域并选择 **自动区域**时,可以在 **Community 区域** 下选择. 在他们选中后, 区域编辑器会用您的 [拣选](/frontend/custom-ui/strategy#settings) 打开 。

### 显示预览 {#register-your-strategy}

对话框将 好了 。 要获得一个,请添加一个静态 `getStubConfig(hass)` , 它返回带有良好默认的战略配置 。 其能 好了,我们走了 对话框将它传递到 `generate()` 以渲染预览, 而新部分则从它开始 。

```js
static getStubConfig(hass) {
  return { type: "custom:my-domain", domain: "light" };
}
```

将 `custom:` 包含在 `type` 中, 如配置 。 没有 `getStubConfig()` , 或当它抛出时, 砖块没有预览 。 选择在大多数家庭显示某种内容的默认值。

## 注册您的策略 {#when-to-generate-again}

在 `window.customStrategies` 中注册您的策略, 用户可以在仪表盘编辑器中选择它而不写入任何 YAML :

```js
window.customStrategies = window.customStrategies || [];
window.customStrategies.push({
  type: "my-demo",
  strategyType: "dashboard",
  name: "My demo dashboard",
  description: "A starter dashboard generated from JavaScript.",
  documentationURL: "https://example.com/my-demo-dashboard",
});
```

| 密钥 | 要求数 | 含义 |
| --- | --- | --- |
| `type` | 对 | 战略名称, 不包含`custom:` 。 |
| `strategyType` | 对 | `"dashboard"` or `"section"`. |
| `name` | | 对话框中的名称 。 |
| `description` | | 名字下面的简短描述. |
| `documentationURL` | | 链接到您的文档 。 前端还没有显示它在任何地方。 |

查看策略尚不能在编辑器中选择,所以不需要注册.

必须加载该资源，以便对话框能够看到它。添加或更新后，请重新加载页面并再次打开对话框。

## 何时再次生成 {#settings}

当仪表盘满载时,一个策略会运行. 默认情况下,当实体,设备,区域,或地板注册更改时,它会再次运行,所以一个新设备出现时没有重新加载. 州变不触发.

要改变这一点,请在登记册中添加一个静态的`registryDependencies`抨击您的策略取决于:`entities`,`devices`,`areas`,`floors`,`labels`和`panels`中的任何一个。 使用一个空列表用于一个不再需要运行的策略 。 要完全控制, 请添加一个静态 `shouldRegenerate(config, oldHass, newHass)` 返回 `true` 当策略再次运行时 。

```js
class MyDemoDashboardStrategy extends HTMLElement {
  static registryDependencies = ["areas"];

  static async generate(config, hass) {
    // ...
  }
}
```

## 设置 {#tips}

一个策略可以有一个视觉编辑器来进行其选项. 从静态 `getConfigElement()` 返回编辑器元素 。 它的工作原理为[纸牌编辑器](/frontend/custom-ui/card-editor#a-visual-editor-of-your-own):Home Assistant用策略配置和设置`hass`调用`setConfig()`,用新配置调用编辑器点火`config-changed`.

给每个区块策略一个编辑器:这是用户在对话框中选择你的区块后看到的第一件事. 没有一台,他们只能得到一个YAML编辑器.

```js
class MyDomainSectionStrategy extends HTMLElement {
  static getConfigElement() {
    return document.createElement("my-domain-strategy-editor");
  }

  static async generate(config, hass) {
    // ...
  }
}
```

仪表板策略还有两个静态选项:

- `configRequired = true`:没有设置,策略就无法工作. Home Assistant在编辑器创建仪表盘前显示.
- `noEditor = true`:策略没有设置可以编辑 。

## 提示 {#提示}

- 快实质内容,快点 它实质内容在每一个负载上运行,仪表板在等待它.
- `hass`已经拥有区域、装置和实体,以简略的形式存在。 对于数据,它和完整的实体注册条目一样,没有使用`hass.callWS()`. 一次,在仪表盘策略中, 将结果传递给你的视图策略 通过它们的配置。
- 策略可以使用任意卡,包括你自己的定制卡.
- 为策略写测试. 它们是从数据到配置的纯函数,这使得它们易于测试.
