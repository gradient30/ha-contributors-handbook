---
title: 数据层
description: 前端怎么跟科雷说话的? WebSocket 命令,订阅, 和收藏在src/data, 以及组件如何使用它们 。
order: 3
---

# 数据已为层 {#the-data-layer}

前端所知道的Home Assistant都来自一个WebSocket连接,由[`home-assistant-js-websocket`](https://github.com/home-assistant/home-assistant-js-websocket)库管理. 国家的核心与实体和注册一样,通过`hass`和[背景情况](/frontend/architecture/hass-and-contexts)到达. 其他一切,一个组件要求自己。

## src/数据 {#srcdata}

所有与Core的通信通过[`src/data/`](https://github.com/home-assistant/frontend/tree/dev/src/data). 每个文件或文件夹都拥有一个话题:其类型,以及调用Core的功能. 组件导入这些函数而不是自己发送消息 。 将每个消息的形状固定在一个地方,旁边是其类型.

典型的数据模块包括: 符合要求的Central excess, 以及 符合要求的 Central excession , 以及 符合要求的 。

```ts
export interface LabelRegistryEntry extends RegistryEntry {
  label_id: string;
  name: string;
  icon: string | null;
  color: string | null;
  description: string | null;
}

export const createLabelRegistryEntry = (
  hass: HomeAssistant,
  values: LabelRegistryEntryMutableParams
) =>
  hass.callWS<LabelRegistryEntry>({
    type: "config/label_registry/create",
    ...values,
  });
```

的国家之一的 你现在 你是个的职权的案例她在充分地 史,其为为为为国际的1993年国际的1993年的1993年的1993年的为为为国际的.的.的.的.的.的.的.的.的.的.的.的.的.的.的.的.的.的为为为为的为为为的为为为的为为的为的.的.的.的.的.的.的.

## 图标 {#commands}

单已将 走恰当 让我们的自由则是 54. 秘书处的说明 对不起可供 我希望 它发出已将 走恰当 让我们的自由则是 54. 秘书处的说明 对不起可供 我希望它能继续 Core 报告失败时, 它用错误对象拒绝 。

```ts
const labels = await hass.callWS<LabelRegistryEntry[]>({
  type: "config/label_registry/list",
});
```

`hass.callService()` 呼叫 [动作](/glossary/action) , `hass.callApi()` 呼叫 REST API 。 新特性使用WebSocket命令,而不是 REST.

## 订阅 {#subscriptions}

要与改变的东西同步, 请订阅 。 然后核心将每个更改推到前端,直到您取消订阅。

```ts
export const subscribeFrontendUserData = (
  conn: Connection,
  key: string,
  onChange: (data: { value: unknown }) => void
) =>
  conn.subscribeMessage(onChange, {
    type: "frontend/subscribe_user_data",
    key,
  });
```

`subscribeMessage` 返回未订阅函数的承诺 。 当数据不再需要时,总是调用它,或者Core不断向一个已消失的组件发送更新.

## 收款 {#collections}

当多个组件需要相同数据时,一个集合在它们之间共享一个订阅. `createCollection` 从`home-assistant-js-websocket` 取一个密钥, 一个获取数据的函数, 一个订阅更新的函数 。 每个订阅者都得到相同的数据. 当最后的订阅者离开时,在5秒信守的宽限期后,对Core的订阅即告结束,所以一个直接回来的组件不会开始新的部分.

```ts
export const subscribeLabelRegistry = (
  conn: Connection,
  onChange: (labels: LabelRegistryEntry[]) => void
) =>
  createCollection<LabelRegistryEntry[]>(
    "_labelRegistry",
    fetchLabelRegistry,
    subscribeLabelRegistryUpdates,
    conn,
    onChange
  );
```

在这里, `subscribeLabelRegistryUpdates` 聆听 `label_registry_updated` 事件, 当它开火时再次获取列表 。

## 从组件订阅 {#subscribe-from-a-component}

`SubscribeMixin` 从[`src/mixins/subscribe-mixin.ts`](https://github.com/home-assistant/frontend/blob/dev/src/mixins/subscribe-mixin.ts) 处理您的生命周期 。 从 `hassSubscribe()` 返回您的订阅 。 混音在组件被连接且有`hass`时订阅,在断开时不订阅.

```ts
@customElement("ha-config-repairs-dashboard")
class HaConfigRepairsDashboard extends SubscribeMixin(LitElement) {
  @state() private _issues: RepairsIssue[] = [];

  public hassSubscribe(): UnsubscribeFunc[] {
    return [
      subscribeRepairsIssueRegistry(this.hass.connection!, (repairs) => {
        this._issues = repairs.issues;
      }),
    ];
  }
}
```

当订阅取决于另一个属性时, 请在 `hassSubscribeRequiredHostProps` 中列出该属性 。 混合剂等待到设定完成.

对于许多组件共享的数据,如标签,偏好一个[懒惰的背景](/frontend/architecture/hass-and-contexts#the-contexts)而不是每个组件的订阅.

## 核心 伙计 {#something-new-in-core}

当您需要的数据尚未可用时, Core 需要一个新的 WebSocket 命令 。 [旨在使命令添加 WebSocket](/frontend/extending/websocket-api)显示两侧。
