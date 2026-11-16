---
title: 天气
description: 天气实体的鬣狗视图, 我认为有当前的情况,细节,还有预测。
sidebarGroup: 信息
---

# 天气 {#weather}

Live demo of `ha-demo-more-info`, 连接到一个 demo Home Assistant.

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](https://contributors.home-assistant.io/design/more-info/weather/)。

```html
<ha-demo-more-info entity="weather.home"></ha-demo-more-info>
```

## 取证结果 {#what-it-shows}

对一个气象实体没有什么可控制的,所以它的观点都是关于阅读的. 从上到下:

- **当前条件**:天气图,条件,如**部分云**,以及多久前变化. 在右边,温度以大文本表示,当预报有温度时,今天的温度和低温度都低于它。
- ** 详情**:列出当前气压,湿度,风速与方向,能见度各有图标. 气象部门不报告的细节被忽略了.
- **预告**:一行一日或数小时,每行有天气图标,温度,低.
- ** 归属**:数据来源于底部的一条线,如**元时的织物预测。

当气象服务有不止一种预测时,其之间的预测开关上方的标签:**Daily**,**Hourly**和**每日两次**。 上面的天气有每日和小时的预报,因此它得到两个标签.

## 设计说明 {#design-notes}

- 超过条件以下的时间,可以查看状态最后一次变化的时间以及最后一次更新的时间.
- 每一个值都以气象服务的单位显示,如°C和km/h.
- 小时预报和每日两次预报按日分列其物品,每天有一个标题。
- 预报在柜台打开时进行,一个旋转器在到达前会显示。

## 在代码中 {#in-code}

视图为 `more-info-weather` 在 [`src/dialogs/more-info/controls/more-info-weather.ts`](https://github.com/home-assistant/frontend/blob/dev/src/dialogs/more-info/controls/more-info-weather.ts) 。 预测订阅、单位和帮助者如`getSecondaryWeatherAttribute`都在[`src/data/weather.ts`](https://github.com/home-assistant/frontend/blob/dev/src/data/weather.ts)中。

来源:[`more-info-weather.ts`](https://github.com/home-assistant/frontend/blob/dev/src/dialogs/more-info/controls/more-info-weather.ts)
