---
title: 太阳
description: 太阳的更宽广的视线 日出和日落 高度 方位角
sidebarGroup: 信息
---

# 太阳 {#sun}

Live demo of `ha-demo-more-info`, 连接到一个 demo Home Assistant.

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](https://contributors.home-assistant.io/design/more-info/sun/)。

```html
<ha-demo-more-info entity="sun.sun"></ha-demo-more-info>
```

## 取证结果 {#what-it-shows}

太阳实体告诉你太阳在哪里,它接下来会做什么。 其观点是州行之一是下方的短列表,上面写着太阳是**Above地平线**还是**Below地平线**.

- **Rising**和**Setting**: 史上下一次日出和日落,每个日出和日落都有持续到左边的时间,右边的时间. 凡先入者先列.
- **Elevation**:太阳在地平线之上的高度,以度数表示.
- ** Azimuth**:太阳的指南针方向,以度数表示.

上面的太阳在几个小时后落下, 所以** 安排** 来之前** Rising**。

## 设计说明 {#design-notes}

- 时间跟随用户的时间格式,比如24小时或AM和PM.
- 排序接下来会是什么 保持最有用的线 在顶部, 所以你从来没有读明日出 在今晚的日落之前。
- 太阳没有更新的信息设计,所以对话框显示顶端的状态行,如[人员](/design/more-info/person)视图.

## 在代码中 {#in-code}

视图为 `more-info-sun` 在 [`src/dialogs/more-info/controls/more-info-sun.ts`](https://github.com/home-assistant/frontend/blob/dev/src/dialogs/more-info/controls/more-info-sun.ts) 。

来源:[`more-info-sun.ts`](https://github.com/home-assistant/frontend/blob/dev/src/dialogs/more-info/controls/more-info-sun.ts)
