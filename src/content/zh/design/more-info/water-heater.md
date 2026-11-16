---
title: 热水器
description: 向下加注,在下方加注。
sidebarGroup: 灯光和气候
sidebarGroup: 灯光与气候

---

# 热水器 {#water-heater}

Live demo of `ha-demo-more-info`, 连接到一个 demo Home Assistant.

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](https://contributors.home-assistant.io/design/more-info/water-heater/)。

```html
<ha-demo-more-info entity="water_heater.water_heater"></ha-demo-more-info>
```

## 取证结果 {#what-it-shows}

主控是水的目标温度,在[气候](/design/more-info/climate)和[增湿器](/design/more-info/humidifier)视图也使用的圆拨上:[控制循环滑动器](/design/components/controls). 环上的一个点标志着当前的温度.

在拨中 1+1+按钮。 当前温度显示为拨号上方的小标签.

那么你在拨号下面,一行菜单 保留次要设置。 那么你只看热水器支持它时:

- ** 模式**,带有设备的操作模式,如**Eco**、**Electric**、**Heat泵**和**Performanence**。 上面的热水器处于生态模式,所以这就是它的状态.
- 离开模式,打开或关闭,有一个人图标,当它打开时就离开。

## 设计说明 {#design-notes}

- 取水器的模式是它的状态. 菜单会改变状态,菜单上的标签会显示它.
- ** 模式** 选项按固定顺序排序,而不是设备报告它们的顺序排序。
- 当设备不支持目标温度时,拨号会变成带有当前温度和状态的只读环,没有按钮.
- 拨号则取州色,水热器关时则变灰.

## 在代码中 {#in-code}

视图为 `more-info-water_heater` 在 [`src/dialogs/more-info/controls/more-info-water_heater.ts`](https://github.com/home-assistant/frontend/blob/dev/src/dialogs/more-info/controls/more-info-water_heater.ts) 。 拨号是`ha-state-control-water_heater-temperature`在[`src/state-control/water_heater/`](https://github.com/home-assistant/frontend/tree/dev/src/state-control/water_heater)。 `WaterHeaterEntityFeature` enum 和模式的排序顺序在 [`src/data/water_heater.ts`](https://github.com/home-assistant/frontend/blob/dev/src/data/water_heater.ts) 中 。

来源:[`more-info-water_heater.ts`](https://github.com/home-assistant/frontend/blob/dev/src/dialogs/more-info/controls/more-info-water_heater.ts)
