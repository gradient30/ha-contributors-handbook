---
title: 空状态
description: 当屏幕或名单里什么都没有时,该展示什么诘问,如何帮助人们从那里继续前进.
order: 3
---

# 空状态 {#empty-states}

迟早,每个列表都是空的. 有人刚安装 Home Assistant, 搜索找不到任何信息, 过滤器会隐藏一切 。 一个空虚的状态把空白的空间变成了一个明确的信息:正在发生什么,人们能够做些什么.

## 何时使用 {#when-to-use}

当屏幕、面板或列表已完成装入且无任何可显示时使用空状态 。 有两种,他们需要不同的词:

- **还没有**:人们没有选择或创造任何东西。 告诉他们如何开始。
- ** 无结果**:有数据,但当前搜索或过滤器没有匹配。 告诉他们要改变什么

历史面板显示了两者. 在你选东西之前 上面写着: "选择区域,设备,实体或标签来查看展现其历史". 当您的选择没有历史时, 它说 ** 找不到结果 ** :"没有历史为当前选择。 尝试改变目标,过滤器,或时间范围".

Pickers 进行相同的拆分:一个文本用于一个完全没有项目的列表,另一个文本用于一个没有匹配的搜索.

在内容仍在装入时不要显示空状态 。 在知道列表为空之前显示 [装入状态](/design/patterns/loading) 。

## 工作原理 {#how-it-works}

前端有一个组件用于此: `ha-empty-state`. 它将葱的含量集中在它负责处理的空间,最多500像素宽度,有:

- 在ỗb 文本颜色中上方的图标, 64 像素
- 说到底是怎么回事
- 一个可选的描述 说为什么,或者下一步要做什么
- 下方的可选动作, 如添加第一个项目的按钮

现场演示  考虑到 `ha-empty-state`. 历史面板 考虑到真实文字的空虚状态.

```html
<ha-empty-state
  icon="M9 17H7V10H9V17M13 17H11V7H13V17M17 17H15V13H17V17M19 19H5V5H19V19.1M19 3H5C3.9 3 3 3.9 3 5V19C3 20.1 3.9 21 5 21H19C20.1 21 21 20.1 21 19V5C21 3.9 20.1 3 19 3Z"
  heading="No results found"
  description="No history for the current selection. Try changing the targets, filters, or time range."
></ha-empty-state>
```

### 写入文本 {#writing-the-text}

- 标题很短很平坦:** 没有发现结果**,** 还没有显示**。
- 描述说人们可以做什么:"尝试改变目标,过滤器,或者时间范围".
- 当有一个清晰的下一步, 把它作为一个按钮, 并有一个标签说它做什么。

见[信件](/design/ui-text/messages) 更多词。

## 无障碍 {#accessibility}

- 标题是一个真实的标题(`h2`),所以屏幕阅读器用户可以找到它.
- 图标是装饰. 标题和描述独自携带信息.

## 组件 {#components}

- `ha-empty-state`,在前端的[`src/components/ha-empty-state.ts`](https://github.com/home-assistant/frontend/blob/dev/src/components/ha-empty-state.ts)中。
- [按钮](/design/components/button), for the next step
- [实体选择器](/design/components/entity-picker) 和其他选手, 他们自己空的, 没有匹配的文本

## 在代码中 {#in-code}

```ts
html`
  <ha-empty-state
    .icon=${mdiChartBoxOutline}
    .heading=${this.hass.localize("ui.panel.history.no_results_title")}
    .description=${this.hass.localize("ui.panel.history.no_results")}
  ></ha-empty-state>
`;
```

将动作像 `ha-button` 一样放在默认的槽中 。 设定 `--ha-empty-state-icon-size` 以改变图标的大小 。
