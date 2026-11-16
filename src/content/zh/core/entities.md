---
title: 实体
description: 实体如何在Home Assistant Core中运作,以及每个实体平台的参考,从传感器和灯光到语音和AI.
order: 20
sidebarGroups:
- 基本情况
- 传感器和状态
- 灯光和气候
- 开幕和安全
- 媒体
- 远程和信号
- 语音和AI
- 应用程序
- 投入和帮助
---



# 实体 {#entities}
一个 [实体](/glossary/entity) 是 Home Assistant 中最小的事物, 它有一个状态: 一个温度读数, 一个光, 一个锁. 用户从实体中构建自动化,仪表板,语音指令,所以它们是您所撰写的任何集成中最显著的部分.

实体来自域, 如 `sensor`, `light` 或 `climate` 。 每个域是一个实体平台:一个具有自身属性,特征和状态的基类,每个集成都以同样的方式执行. 这种共享的形状使得一个品牌的光线 与另一个品牌的光线完全一样 在界面、自动化和语音助理方面

这些页面是用于构建或维护集成,或在实体平台本身上工作的开发者. 他们假设你知道 Python 并且有一个 [发展环境](/core/development) 运行 。 要了解一个集成是如何设置其平台和创建实体的,首先从[ũ](/core/integrations)开始.

## 实体如何运作 {#how-an-entity-works}

1. 您的集成在平台模块中创建实体对象, 如 `sensor.py`, 并将其传递到 `async_add_entities` 。
2. Home Assistant 注册 [非常大实体登记处](/core/entities/registry) 中的每个实体, 将其链接到其设备, 并给出实体 ID 。
3. 该实体通过 [投票或推](/core/entities/state-updates) 不断更新数据, 并将其状态写入状态机器 。
4. 用户通过动作控制它,动作将方法调用到您的实体上, 如 `async_turn_on` 。
5. 当集成卸载时,实体被移除,和[自己收拾干净](/core/entities/lifecycle).

## 基本情况 {#basics}

先看这些 它们适用于每一个实体,无论其领域如何。

- [实体类别](/core/entities/entity-class):基础类,设置属性的三种方法,以及通用属性.
- [进取号](/core/entities/naming):`has_entity_name`,译名,友名,和实体ID.
- [更新状态](/core/entities/state-updates):投票,证实了,写州,和可用.
- [实体生命周期](/core/entities/lifecycle):当一个实体被添加、更改和删除时运行的钩子。
- [状态和属性](/core/entities/state-attributes):什么最终是状态对象,什么是远离它。
- [图标](/core/entities/icons):图标翻译和图标属性.
- [实体登记处](/core/entities/registry): 独一无二的ID,设备,实体类别,以及已禁用的实体.

## 实体平台 {#entity-platforms}

每个平台页面都有相同的结构:实体代表什么,其属性,其支持的特征,你实施的方法,状态,以及一个实例. 当前端以自己的方式显示一个域时,页面会链接到其[设计区](/design/more-info)中的更多info视图.

### 传感器和状态 {#sensors-and-status}

- [传感器](/core/entities/sensor):一个测量值或读值,如温度或功率读值.
- [二](/core/entities/binary-sensor) : 打开或关闭的东西, 如打开的门或检测到的运动。
- [积极地濑子事件](/core/entities/event):发生的事情,如按键或门铃环.
- [天气](/core/entities/weather):当前条件和预测.
- [设备跟踪器](/core/entities/device-tracker):设备在哪里,或者它是否在家。
- [地理位置](/core/entities/geo-location): 从外部种子中找到位置的事件 。
- [B. 事 项](/core/entities/calendar):有始有终的事件.
- [空气质量](/core/entities/air-quality): 腐烂,用传感器代替.

### 灯光和气候 {#lights-and-climate}

- [光线](/core/entities/light)
- [气候](/core/entities/climate)
- [风扇](/core/entities/fan)
- [湿度](/core/entities/humidifier)
- [热水器](/core/entities/water-heater)

### 开幕和安全 {#openings-and-security}

- [覆盖](/core/entities/cover): 百叶窗,遮荫窗,车库门,和大门.
- 放开我 水和气阀
- [锁定](/core/entities/lock)
- [警报控制面板](/core/entities/alarm-control-panel)
- [仍在进行的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的草的 的 的草的草的草的草的草的草的草的草的草的草的草的草的草的 的 的草的](/core/entities/siren)

### 媒体 {#media}

- 请问收集到的 你在干什么公民资格?
- 200)} 很显然减缓贫穷àn所承担的至迟在自由地向秘书处提供确实是为指导
- [图像](/core/entities/image):一个时时变化的静态图像.

### 远程和信号 {#remotes-and-signals}

- 没错 很好 谁 孩子 !
- [红外线](/core/entities/infrared):共享红外发射机和接收器.
- [无线电频率](/core/entities/radio-frequency):共享RF发射机和接收器.

### 语音和AI {#voice-and-ai}

- [来吧](/core/entities/conversation):能理解并回答人们对Assist说的话的特工.
- [语音对文本](/core/entities/stt)
- [文字对语音](/core/entities/tts)
- [醒字检测](/core/entities/wake-word)
- { 如果是 {L0 他们在听和回话的设备。
- [AI 任务](/core/entities/ai-task):用模型生成数据或图像.

### 应用程序 {#appliances}

- [真空](/core/entities/vacuum)
- [割草机](/core/entities/lawn-mower)
- [知道了 更新](/core/entities/update): 固件和软件更新。

### 投入和帮助 {#inputs-and-helpers}

- [开关](/core/entities/switch):打开或关闭一些东西。
- [按钮](/core/entities/button): 触发单个动作 。
- [数目](/core/entities/number)、[选择](/core/entities/select)和[文本](/core/entities/text):在设备上设置一个值。
- 这是你的所针对的一视同仁与与与与与与与与与与与与与与与与增长速度与与与与讲坛与与与与与与与与与与与与与与与与与与与、与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与、与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与、与与与与与与与与与与与与与与与与与与与、与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与、与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与与
- [场景](/core/entities/scene):激活存储在设备上的场景.
- 眷乍撮褒秃舜颜曙阐茸颜葵陀؟袍偃淌乍雏蕴ryl飙孰稠媲 Lili只是个嘲耿缜ẩ谚先动鸳鸯茹恬蔷萌隼酝梵乍葵供大会审议轶咩萌动动媲 nó恪先毗茸晦凤姗几句笋皈佑ء冉先动动动动动动动动动动动动动动.动动动动动动动动动动动动动动动动动.动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动
- [通知](/core/entities/notify): 发送消息。

## 选择正确的使之能够 {#picking-the-right-platform}

选择一个平台 匹配事物的真面目 而不是最容易执行的平台 开启和关闭的泵是开关,但阀门是阀门,而灯光也是灯光,即使两者只开启和关闭. 右侧平台给用户正确的控制,给语音助手正确的设备类型,并随着设备的成长而给你正确的特性. 每个平台页都说它何时合适,何时不合适。

如果没有一个平台适合,或者一个平台错过了很多设备拥有的东西,就不要用属性来绕过它. 提议先更改 [结构讨论](https://github.com/home-assistant/architecture/discussions) 。 见[提议修改实体模式](/core/entities/entity-class#proposing-changes-to-an-entity-model)。

## 谁说话 {#who-to-talk-to}

- 在建立实体时提问? 在 [编码支持**](https://discord.com/channels/330944238910963714/1257019582112334014) 上启动一条线程 。
- 想要在域中添加特性、状态或设备类吗 ? 在 [架构存储器](https://github.com/home-assistant/architecture/discussions) 中打开讨论 。 当作出决定时,将在那里记录为结构决定记录。
- 在实体平台上找到错误吗 ? 在 [核心存储器](https://github.com/home-assistant/core/issues) 中打开一期 。
