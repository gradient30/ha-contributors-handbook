---
title: 更多信息ppe
description: 当您选择一个实体时打开的对话框, 以及每种实体类型的视图 。
order: 26
sidebarGroups:
- 灯光和气候
- 开幕和安全
- 媒体
- 应用程序
- 帮助者
- 信息
---

# 更多信息ppe {#more-info}

在 Home Assistant 中选择一个几乎在任何地方的实体, 并打开更多信息对话框 。 它是一个地方, 你干嘛看到关于一个单一实体 你需要看到的一切: 它的状态, 改变它的控制, 它以前所做的, 以及它的设置。 由于它从仪表板,搜索,实体表,以及其他对话框中打开,它是人们所看到的屏幕中最丰富的之一.

对话框对每个实体都是相同的 。 其内部的坐落取决于域:光得到亮度滑动器,恒温器得到圆拨,定时器得到持续场. 这些页面显示这些域名的每个视图,这些域名是由假家庭上真正的前端实现的直播.

## 构成 {#anatomy}

对话框有一个标题和您移动的一些视图 。

- **header**:一个关闭的按钮,实体名称,上面有一个面包屑,上面有它所属的区域和装置. 右边坐着一个**历史**按钮,一个**定居**按钮,以及菜单. 菜单持有**Add to...**,拥有它们的实体最喜爱的选项,与设备的链接,**关联**和**细节**. ** 设置 ** 按钮和菜单显示仅供管理员使用。
- ** 信息视图**:默认视图。 对于新设计的域,它从一个大的状态开始,如**71%**或**Locked**,以及它最后一次改变的时间. 选择相对时间和绝对时间之间的切换时间。 下面是主要控制,下面是次要控制。 旧域显示顶端的状态行 。 没有自己视野的域,像传感器一样,也得到历史图和下面的活动列表.
- **历史**:该实体的历史图表和活动。 对于拥有自己视图的域,历史生活在标题按钮后面,因此信息视图保留关于控制设备的内容.
- ** 设置**:实体设置,如其名称,图标,区域,以及是否启用.
- ** 关联**:实体的上下文,如其地板,区域,设备,集成,和标签,然后是它与之相关的其他项目,如使用它的自动化和脚本.
- ** 细节**:实体ID,原始状态,当它最后一次修改和更新时,以及每个属性. 头部的代码按钮切换到YAML.

当一个实体是其它实体的组合,如光组或场景时,信息视图将控件下方的成员列为牌,这样就可以逐一控制它们.

## 设计原则 {#design-principles}

较新的信息视图遵循相同的模式,因此一个灯光,一个锁,一个粉丝感觉像一个家庭.

- ** 一个大控制器。 ** 每个视图都有一个控制器来完成实体的主要工作,它得到大部分房间:垂直滑动,大开关,圆拨. 这些来自 [控件](/design/components/controls) 家族, 被制成 用手指和鼠标。
- ** 以下二级控制。 ** 模式,预设等设置坐落在主控下的紧凑[选择菜单](/design/components/select-menu)一行. 小型模式开关,如亮度或亮度用于灯光的颜色,坐在它下面的一排圆形图标按钮中.
- ** 国家第一。 ** 在你触摸任何东西之前 顶端的大州会告诉你发生了什么 视图在的规划帮助下重新拼写: 亮光显示它的亮度, 封面显示 ** Open ~ 70 Q.
- ** 只有设备能做什么。 ** 每个控制检查实体的支持特性。 当一个设备不能做什么时,控制器就不存在了. 未显示为已禁用, 它已消失 。 控件只有在实体不可用时,或者在当前状态下某个动作毫无意义时,比如关闭一个已经关闭的门时,才会被禁用.
- 页:1 控件采用实体状态的颜色,如琥珀用于一个开着的灯光或锁锁的绿色,使用与[状态图标](/design/components/state-icon)相同的颜色.

## 视图 {#views}

### 灯光和气候 {#lights-and-climate}

- [光线](/design/more-info/light)
- [气候](/design/more-info/climate)
- [风扇](/design/more-info/fan)
- [湿度](/design/more-info/humidifier)
- [热水器](/design/more-info/water-heater)

### 开幕和安全 {#openings-and-security}

- [覆盖](/design/more-info/cover)
- [阀门](/design/more-info/valve)
- [锁定](/design/more-info/lock)
- [警报控制面板](/design/more-info/alarm-control-panel)

### 媒体 {#media}

- [媒体播放器](/design/more-info/media-player)

### 应用程序 {#appliances}

- [真空](/design/more-info/vacuum)
- [割草机](/design/more-info/lawn-mower)
- [开关](/design/more-info/switch)
- [知道了 更新](/design/more-info/update)

### 帮助者 {#helpers}

- [输入编号](/design/more-info/input-number)
- [数目](/design/more-info/number)
- [输入文本](/design/more-info/input-text)
- [计时器](/design/more-info/timer)
- [场景](/design/more-info/scene)

### 信息 {#information}

- [天气](/design/more-info/weather)
- [加 进](/design/more-info/person)
- [太阳](/design/more-info/sun)

## 在代码中 {#in-code}

对话框是 `ha-more-info-dialog`, 在 [`src/dialogs/more-info/`](https://github.com/home-assistant/frontend/tree/dev/src/dialogs/more-info) 中 。 信息视图是 `ha-more-info-info`, 这使得 `more-info-content` 。 该元素从 [`src/dialogs/more-info/controls/`](https://github.com/home-assistant/frontend/tree/dev/src/dialogs/more-info/controls) 中选择实体域的视图 `more-info-<domain>` 。 具有较新设计的域列表为`DOMAINS_WITH_NEW_MORE_INFO`在[`src/dialogs/more-info/const.ts`](https://github.com/home-assistant/frontend/blob/dev/src/dialogs/more-info/const.ts)中.

顶端的大状态为`ha-more-info-state-header`,副控件的行为`ha-more-info-control-select-container`,均在[`src/dialogs/more-info/components/`](https://github.com/home-assistant/frontend/tree/dev/src/dialogs/more-info/components)中. 大多数主控件都生活在[`src/state-control/`](https://github.com/home-assistant/frontend/tree/dev/src/state-control),每个域一个文件夹.

来源:[`src/dialogs/more-info/`](https://github.com/home-assistant/frontend/tree/dev/src/dialogs/more-info)
