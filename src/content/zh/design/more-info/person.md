---
title: 加 进
description: 一个人的更信息视图,在地图上的位置.
sidebarGroup: 信息
---

# 加 进 {#person}

Live demo of `ha-demo-more-info`, 连接到一个 demo Home Assistant.

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](https://contributors.home-assistant.io/design/more-info/person/)。

```html
<ha-demo-more-info entity="person.alex"></ha-demo-more-info>
<ha-demo-more-info entity="person.sam"></ha-demo-more-info>
```

## 取证结果 {#what-it-shows}

你对一个人的疑问是 "他们在哪里?" 景色用地图回答. 顶端是州立排,人物所在的区域,如**Home**或**Work**. 在下面,一张地图放大了人的位置, 并有一个标记显示他们的初始或图片。

亚历克斯在家 被电话跟踪 萨姆在工作

对于管理员,从当前位置** 按钮下方的** 创建区将人物所在位置变为新区域. 这不是这些演示的一部分。

## 设计说明 {#design-notes}

- 地图只显示在知道人的位置时:从他们自己的坐标,或者从他们所在的区域. 一个人没有 要么就只得到州立排。
- ** 从当前位置产生区域** 仅显示该人拥有自己的坐标时,因为一个区域需要从一个点开始。
- 地图在人周围很合适,所以你不需要放大或平板就可以找到它们.
- 州是该区的名称,而不是坐标. 人们思考的地方,比如**Home**或**Work**.

## 在代码中 {#in-code}

视图为 `more-info-person` 在 [`src/dialogs/more-info/controls/more-info-person.ts`](https://github.com/home-assistant/frontend/blob/dev/src/dialogs/more-info/controls/more-info-person.ts) 。 地图是`ha-map` 从[`src/components/map/`](https://github.com/home-assistant/frontend/tree/dev/src/components/map)。 人物域没有更新的信息设计,因此对话框也显示顶部的状态行.

来源:[`more-info-person.ts`](https://github.com/home-assistant/frontend/blob/dev/src/dialogs/more-info/controls/more-info-person.ts)
