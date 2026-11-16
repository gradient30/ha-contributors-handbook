---
title: 光线
description: 灯光的更信息视图,带有大亮度滑动器和色和色温开关.
sidebarGroup: 灯光和气候
---

# 光线 {#light}

Live demo of `ha-demo-more-info`, 连接到一个 demo Home Assistant.

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](https://contributors.home-assistant.io/design/more-info/light/)。

```html
<ha-demo-more-info entity="light.living_room_lamp"></ha-demo-more-info>
```

## 取证结果 {#what-it-shows}

光的主要控制是亮度,因为这是人们改变最多的。 它是一个高大的垂直[控制滑动器](/design/components/controls),从底部像玻璃一样填满. 当光线有颜色时,滑动器会取下它,略微的触动,所以非常苍白的颜色会保持可见.

顶部的状态显示亮度,如**71%**,而不是仅仅**On**. 光照关中,或无光照,则显示常态.

所显示的视图取决于光线所支持的颜色模式:

- ** 只打开和关闭**:没有滑动器。 一个大开关取代它的位置,一个点亮的灯泡和一个不点亮的灯泡作为图标.
- **亮度**:滑动器,其下方有一个**Togle**按钮来开启或关闭灯光.
- ** 颜色温度**:将主控换成颜色温度滑动器的按钮,从温暖到凉爽.
- **Color**:将主控器换成彩色轮的按钮. 带有额外白色通道(RGBW或RGBWW)的灯光也会为车轮下方的颜色亮度和白色亮度获得滑动器.
- **White**:一个**Set White**按钮,用于带有单独白色通道的灯光.

上方的地板灯支撑着颜色和颜色温度,因此它得到了所有三个按钮:亮度,颜色,温度. 下面的走廊灯光只有暗色,所以它得到滑动器和**Togle**按钮. 厨房天花板灯光也暗淡,但关闭了:滑轮是空的,没有把手.

Live demo of `ha-demo-more-info`, 连接到一个 demo Home Assistant.

```html
<ha-demo-more-info entity="light.hallway"></ha-demo-more-info>
<ha-demo-more-info entity="light.kitchen_ceiling"></ha-demo-more-info>
```

当一个光线支持效果时,一个**效果**菜单坐落在控件下方. 支持颜色或颜色温度的灯光也可以在按钮下显示一行最喜爱的颜色,一拍即逝. 这些来自实体设置,不是这些演示的一部分。

## 设计说明 {#design-notes}

- 主控改变,但其位置不变. 圆形按钮的行在亮度,颜色,和色温之间切换,所选的则突出显示.
- 颜色和温度按钮显示一个小的颜色轮子和温暖至凉爽的梯度,而不是图标. 你读标签前就认出他们了
- 按钮行中的分隔符将切换从模式按钮中拆分,模式按钮从**Set White**中拆分.
- 当灯光不可用时,滑动器和每个按钮都会被禁用,但它们会留在原地,因此布局不会跳动.
- 在一个光线组中,成员灯光显示在控件下方作为瓦片卡. 它们的瓦片遵循主控:亮度滑动器,色温滑动器,或者组合设定为颜色时没有控制.

## 在代码中 {#in-code}

视图为 `more-info-light` 在 [`src/dialogs/more-info/controls/more-info-light.ts`](https://github.com/home-assistant/frontend/blob/dev/src/dialogs/more-info/controls/more-info-light.ts) 。 亮度滑动器为 `ha-state-control-light-brightness` 在 [`src/state-control/light/`](https://github.com/home-assistant/frontend/tree/dev/src/state-control/light) 。 色轮和色温滑动器为`light-color-rgb-picker`和`light-color-temp-picker`,最喜欢的颜色为`ha-more-info-light-favorite-colors`,全部在[`src/dialogs/more-info/components/lights/`](https://github.com/home-assistant/frontend/tree/dev/src/dialogs/more-info/components/lights)中. 颜色模式和特征在[`src/data/light.ts`](https://github.com/home-assistant/frontend/blob/dev/src/data/light.ts)中.

来源:[`more-info-light.ts`](https://github.com/home-assistant/frontend/blob/dev/src/dialogs/more-info/controls/more-info-light.ts)
