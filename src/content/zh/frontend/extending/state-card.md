---
title: 添加状态卡
description: 显示一个实体的图标、名称和状态或控件,以及如何为域添加一个的行。
order: 2
---

# 添加状态卡 {#add-a-state-card}

状态卡是一个实体的紧凑行:其图标,名称,最后一次更改时,以及其状态,或者一个小控制来更改. 您可以在使用旧设计的域名的更信息对话框的顶端找到它们, 并在画廊中找到它们 。

大多数域不需要自己的域. 如果没有一个,一个实体在可以打开和关闭时会得到一个切换,并显示其状态为文本。 只当一个域需要该行中不同的控件,如数字输入或选择时,才会添加状态卡.

状态卡位于[`src/state-summary/`](https://github.com/home-assistant/frontend/tree/dev/src/state-summary),每个域一个元素.

## 为域添加一个 {#add-one-for-a-domain}

此示例为名为`example`的域添加了状态卡.

1. 在 [`src/common/const.ts`](https://github.com/home-assistant/frontend/blob/dev/src/common/const.ts) 中添加 `"example"` 到 `DOMAINS_WITH_CARD` 。
2. 创建 `src/state-summary/state-card-example.ts`, 有一个元素叫做 `state-card-example` 。 它得到`hass`,`stateObj`和`inDialog`,当卡片在更多信息对话框中显示时是`true`.
3. 以 [`src/state-summary/state-card-content.ts`](https://github.com/home-assistant/frontend/blob/dev/src/state-summary/state-card-content.ts) 导入 :

```ts
   import "./state-card-example";
   ```

`state-card-content`按域选择元素:`state-card-<domain>`用于列表中的域,`state-card-toggle`用于可以切换的其他实体,其余的`state-card-display`. 不可用的实体使用 `state-card-display` 。 一个有 `custom_ui_state_card` 属性的实体跳过所有这一切: 要使用的属性名称 。

查看现有的状态卡, 如 `state-card-number.ts` 或 `state-card-select.ts` , 查看它们开始的结构和共享的 `state-info` 元素 。
