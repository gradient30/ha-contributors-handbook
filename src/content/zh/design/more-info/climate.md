---
title: 气候
description: 猥亵器或空调器的更多信息视图,围绕圆形温度拨号建造.
sidebarGroup: 灯光和气候
sidebarGroup: 灯光与气候

---

# 气候 {#climate}

Live demo of `ha-demo-more-info`, 连接到一个 demo Home Assistant.

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](https://contributors.home-assistant.io/design/more-info/climate/)。

```html
<ha-demo-more-info entity="climate.thermostat"></ha-demo-more-info>
<ha-demo-more-info entity="climate.bedroom_air_conditioner"></ha-demo-more-info>
```

## 取证结果 {#what-it-shows}

气候实体的主要控制是目标温度,在圆盘上:[控制循环滑动器](/design/components/controls). 拨号读得像壁上的恒温器,它符合一个具有当前值的射程和一个形状的目标. 环上的一个小点标志着当前的温度.

在你找到的拨号内 从上到下

- 设备正在做的,比如加热或冷却, 颜色匹配。 当它报告没有动作时,标签会显示模式。
- 目标温度,大数字。
- 减和加键,可以一步一步改变目标.

在拨号上方,电流温度以及设备报告时,电流湿度显示为小标签. 此视图在顶端没有大的状态:拨号已经说了全部.

在拨号下方,一行菜单持有次要设置. **Mode**总是在那里,设备的HVAC模式,如**Off**,**Heat**和**Cool**,每个都有自己的图标. 其他只显示设备支持它们时:

- 预设,像生态或远离。
- 风扇模式.
- 摆动模式,以及水平摆动模式.

恒温器正在加热,所以环是橙色的,目标设定了. 空调机支持风扇模式和摇摆模式,因此获得两个额外的菜单. 它关闭了,所以拨号是灰色和不活跃的。

## 变体 {#variants}

- **目标温度范围**:将温度保持在低值和高值之间的设备得到一个带有两个手柄的拨号. 两个值都显示在中心,你选择一个用按钮所开展的工作来调整. 低手ụ取暖色,高手取冷色.
- **目标湿度**:一个也可以保持湿度水平的装置在拨号下有两个圆形按钮,用于温度和湿度. 他们在两个拨号之间互换主控.
- **没有目标**:一个只报告温度的设备得到一个只读的环,有当前温度,没有按钮.

## 设计说明 {#design-notes}

- 颜色来自该州:热为橙色,冷为蓝色,设备关闭时戒指会变灰. 目前的动作,像加热, 叮叮拨号。
- 戒指填充以匹配模式. 在热量中,它从启动到目标,在冷却中,它从目标到终点都填满,所以你可以看到设备在目标上工作的哪一边. 仅加热或仅冷却的设备也填入**off**和**Auto**。
- 小数位数跟随设备的台阶. 带有半度阶梯的设备显示为**211.0**,从未显示为**21**.
- **Mode** 选项按固定顺序排序,而不是设备报告它们的顺序,所以每个自动调温器都以同样的方式列出其模式.
- 拨号会在你放手时发出新目标,而不是拖动时发出. 减和的主要目标 等待一秒钟 后,最后的聪动, 所以敲加三次 发送一个变化,而不是三个。
- 莹带射程,低靶永远不能通过高靶,反之亦然.

## 在代码中 {#in-code}

视图为 `more-info-climate` 在 [`src/dialogs/more-info/controls/more-info-climate.ts`](https://github.com/home-assistant/frontend/blob/dev/src/dialogs/more-info/controls/more-info-climate.ts) 。 拨号是`ha-state-control-climate-temperature`和`ha-state-control-climate-humidity`在[`src/state-control/climate/`](https://github.com/home-assistant/frontend/tree/dev/src/state-control/climate)。 菜单为 [选择菜单](/design/components/select-menu) 在 `ha-more-info-control-select-container` 中公民资格 。 其特征见于[`src/data/feature/climate_entity_feature.ts`](https://github.com/home-assistant/frontend/blob/dev/src/data/feature/climate_entity_feature.ts).

来源:[`more-info-climate.ts`](https://github.com/home-assistant/frontend/blob/dev/src/dialogs/more-info/controls/more-info-climate.ts)
