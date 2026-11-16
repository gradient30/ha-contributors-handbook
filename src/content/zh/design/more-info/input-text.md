---
title: 输入文本
description: 文本帮助器的更多信息, 状态行中的文本字段 。
sidebarGroup: 帮助者
sidebarGroup: 助手

---

# 输入文本 {#input-text}

Live demo of `ha-demo-more-info`, 连接到一个 demo Home Assistant.

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](https://contributors.home-assistant.io/design/more-info/input-text/)。

```html
<ha-demo-more-info entity="input_text.welcome_message"></ha-demo-more-info>
```

## 取证结果 {#what-it-shows}

文本帮助器 (`input_text`) 持有短片文本, 如上面的欢迎信息 。 它没有更新的信息设计. 它的控制生活在对话框的顶端的状态行中:左侧的图标和名称,右侧是当前文本的[文本输入](/design/components/input).

在状态行下方,对话框显示帮助者的历史及其活动. 演示只显示状态行.

## 设计说明 {#design-notes}

- 字段遵循帮助器的设置:最小和最大长度,文字必须匹配的图案,以及模式. 在密码模式下,文本被隐藏.
- 当文本为空时,字段会显示一个占位符,所以看起来不会断裂.
- 新文本在确认字段时保存, 并且只在字段更改时保存 。 单打字一无所获

## 在代码中 {#in-code}

状态行是 `state-card-input_text` 在 [`src/state-summary/state-card-input_text.ts`](https://github.com/home-assistant/frontend/blob/dev/src/state-summary/state-card-input_text.ts) 。 没有 `more-info-input_text` : 域在 `DOMAINS_HIDE_DEFAULT_MORE_INFO` [`src/dialogs/more-info/const.ts`](https://github.com/home-assistant/frontend/blob/dev/src/dialogs/more-info/const.ts) 中, 所以对话框只显示行和历史 。

来源:[`state-card-input_text.ts`](https://github.com/home-assistant/frontend/blob/dev/src/state-summary/state-card-input_text.ts)
