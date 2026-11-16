---
title: 对象和背景
description: 组件如何获得数据。 拥有所有东西的物体, 和只给出它所需要的部分的Lit上下文。
order: 2
---

# 对象和背景 {#the-hass-object-and-contexts}

前端将Home Assistant状态保存在一个对象,`hass`. 它拥有所有必然存在的实体状态,注册,配置,用户,翻译,以及调用Core的功能. 当有变化时,前端会制作一个新的 `hass` 对象,只包含更改的部分的新版本.

和和在其各自

```ts
const changed = newHass.states !== oldHass.states;
```

## 获取数据的两个方法 {#two-ways-to-get-the-data}

** `hass`财产。 ** 面板,卡片,以及许多组件被设定为 `hass` ,然后传给他们的孩子。 它很简单,是 [定制卡和面板](/frontend/custom-ui) 的公共API 。 缺点是:一个新的 `hass` 到达家里的每一个变化, 所以一个需要 `hass` 检查或重报的组件比它需要的多得多, 它隐藏了该组件实际依赖的数据 。

** 内容。 ** 根元素提供的数据与一组致力于[属性背景](https://lit.dev/docs/data/context/)相同,按主题划分. 一个组件只消耗它所读的上下文,只有在这些上下文改变时才更新.

对于前端的新代码:叶片组件消耗了涵盖其所读内容的最狭义上下文. 拥有 `hass` 并传递给它的容器可以保存财产。

## 二. 背景 {#the-contexts}

上下文在[`src/data/context/index.ts`](https://github.com/home-assistant/frontend/blob/dev/src/data/context/index.ts)中定义.

| 背景情况 | 马赛尔三方 | 豺嬷翘ý |
| --- | --- | --- |
| `statesContext` | 所有实体的状况 | `hass.states` |
| `entitiesContext` | 实体登记册,供展示 | `hass.entities` |
| `devicesContext` | 设备注册 | `hass.devices` |
| `areasContext` | 区域登记册 | `hass.areas` |
| `floorsContext` | 楼层登记册 | `hass.floors` |
| `registriesContext` | 所有四个登记册加在一起快点 | |
| `servicesContext` | 现有行动 | `hass.services` |
| `internationalizationContext` | 语言、芮语、`localize`和翻译加载器 | `hass.localize`, `hass.locale`, `hass.language` |
| `formattersContext` | 实体格式化器 | `hass.formatEntityState`和他们 |
| `configContext` | 蓉核 : | `hass.config`, `hass.user`, `hass.auth`, `hass.userData` |
| `connectionContext` | WebSocket 连接及其状态 | `hass.connection`, `hass.connected` |
| `apiContext` | 的 的 的 的 的 的 的 的 的 的 的   的  的  的  的   的  的   的               各国 | خẩ绚傍鱿嘲稳妥坛萌ẹ哔哎ẹ鬓楷,,,,,,,,,, ,                    ,                                      ,                                                                                          , |
| `uiContext` | 主题、面板、侧边栏和其他UI状态 | `hass.themes`, `hass.panels` 及其他内容 |
| `narrowViewportContext` | 主视图是否使用窄版式 | |
| `reducedMotionContext` | 也许用户喜欢减少运动 | |

一些上下文懒惰:它们只在第一个组件消耗它们时才订阅Core,在最后一个组件消失后不订阅. 这些是`labelsContext`,`fullEntitiesContext`,`configEntriesContext`,`manifestsContext`,`triggerDescriptionsContext`,和`conditionDescriptionsContext`。

旧的单值上下文,如`localizeContext`,`themesContext`,和`userContext`,都是贬值的. 使用分组的 。

## 设定上下文 {#consume-a-context}

凤凰网,网易,网易,网易,网易,网易,网易,网易,网易,网易,网易,网易,网易,网易,网易,网易,网易,网易,网易,网易,网易,网易,网易,网易,网易,网易,网易,网易,网易,网易,网易,网易,网易,网易,网易,网易,网易,网易,网易,网易,网易,网易,网易,网易,网易,网易,网易,网易,网,网易,网易,网易,网易,网易,网易,网易,网易,网易,网易,网易,网易,网易,网易,网网网网,网网网,网网,网,网,网网,网,网:F,网网网,网:F,网,网:F,网,网:F,网:F,网:F,网,网:F,网,网,网,网, `@lit/context` 版本在每一个消费上下文的每个变化上重写组件 。 前端的版本将它留给了球场,而ESLint则阻挡了另一个.

```ts
@state()
@consume({ context: labelsContext, subscribe: true })
private _labels?: LabelRegistryEntry[];
```

您如何组合装饰器决定组件何时:

- `@state()` 与 `@consume` : 当上下文发生变化时, 组件会重现 。
- `@state()` 带有 `@consume` 和 `@transform` 的 `@transform` : 组件只在转换值变化时才重新返回 。
- `@consume`独自一人:字段保持时速,但永远不会触发渲染. 用于仅在事件处理器中读取的值, 如 `apiContext` 。

要从集合上下文中取一个值, 请从 `src/common/decorators/transform` 中添加 `@transform` :

```ts
@state()
@consume({ context: uiContext, subscribe: true })
@transform<HomeAssistantUI, Themes>({
  transformer: ({ themes }) => themes,
})
private _themes!: Themes;
```

### 一个实体 {#one-entity}

对于显示一个实体的组件, [`src/common/decorators/consume-context-entry.ts`](https://github.com/home-assistant/frontend/blob/dev/src/common/decorators/consume-context-entry.ts) 有跟随该组件所持有的实体ID的助手 :

```ts
@state()
@consumeEntityState({ entityIdPath: ["_config", "entity"] })
private _stateObj?: HassEntity;

@state()
@consumeEntityRegistryEntry({ entityIdPath: ["_config", "entity"] })
private _entity?: EntityRegistryDisplayEntry;

@state() @consumeLocalize()
private _localize!: LocalizeFunc;
```

`consumeEntityStates` 对实体ID列表也这样做, 当这些实体都没有改变时, 保留以前的记录 。

[`src/panels/lovelace/cards/hui-button-card.ts`](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-button-card.ts)中的按钮卡是使用上下文而不是`hass`的组件的参考示例.

### 在反应控制器中 {#in-a-reactive-controller}

反应控制器扩展 `ContextController` 并以 `consumeContext()` 声明其字段, 既从 [`src/common/decorators/consume.ts`](https://github.com/home-assistant/frontend/blob/dev/src/common/decorators/consume.ts) . `@state()` 也从 `@transform` 不对控制器工作 : 调用 `host.requestUpdate()` 当主机需要渲染时 。 [`src/data/service-info-controller.ts`](https://github.com/home-assistant/frontend/blob/dev/src/data/service-info-controller.ts)是一个例子。

## 在前端外边 {#outside-the-frontend}

自定义卡片和面板也可以请求上下文,无需从前端导入任何内容,方法是启动 `context-request` 事件 。 显示如何。

`hass`本身的方法和属性在[对象引用](/frontend/reference/hass-object)中列出.
