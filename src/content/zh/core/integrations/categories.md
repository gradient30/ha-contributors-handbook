---
title: 一体化类别
description: 人群浏览整合的类别,以及如何选择合适的整合对象.
sidebarGroup: 参考
order: 4
---

# 一体化类别 {#integration-categories}

整合类别表示整合的目的,因此人们可以通过它的工作来找到,比如在网站的整合页面上. 一个集成在它的 `categories` 键 [显示](/core/integrations/manifest#categories) 中列出了其中一到三个. 除了实体、系统和虚拟集成之外,核心中的每一个集成都需要它们。 对于自定义的集成,它们是可选的,而 " 市场目录 " 将它们纳入其数据。

## 迂回选择 {#how-to-choose}

问自己一个问题:这是什么,人们会在哪里寻找呢? 一个类别描述了产品或服务,而不是为它创建的实体Home Assistant.

1. 选择初级类别: 说出你融入的目的是什么。 一个恒温器品牌是Climate,即使它也创造了传感器和开关.
2. 当一个明显适合时使用一个子类, 如 `climate.thermostats_heating` 。 否则,自行使用分类.
3. 只有在你的整合真的如此时, 才会增加第二个或第三个类别, 在某种程度上,人们会浏览。 雪莉制造了智能插头和开关,但也有灯泡和能量计,因此它列出了所有三个.

大多数整合需要皓一类. 对经常出现皓案的一些指导:

- 带入多种设备,如Zigbee或 我们得多功能的卖家桥的枢纽或桥,在Hubs & 协议中进行. 一种产品的桥梁 属于该产品类别:飞利浦·惠是照明。
- 通用的构件, 如 MQTT, RESTFUL, 或 Modbus,这类活动在 DIY & makers 中进行 。
- 助者先进助者. 只有当帮助者明显在1左右时,才添加一个现实世界的分类,如通用度量仪,也就是Energy.
- 一个气象站测量天气,它不预报天气. 单独使用天气警报,并对实际预测的服务保持预报.

实体和系统整合,如`light`或`recorder`,不是人们浏览的东西,也没有分类. 虚拟集成也没有:它们显示了它们指向的集成的类别.

## 所有职类 {#all-categories}

下面的每个类别都列出您可以在 `categories` 中的值 。 有些类别有子类别,以缩小其范围:在您整合涵盖更多类别时,单独使用该类别,在一个适合时使用该类别。 智能自动调温器是`climate.thermostats_heating`。 一个制造恒温器,空调,风扇的品牌是`climate`.

找到一个分类,按你的整合是干什么的, 像"临时"或"池",或跳到一个。

- AI & 语音:AI模型和代理,语音助理,语音对文本,文本对语音 比如图像识别.
  - AI 语音, 一般为: `ai_voice`
  - AI 型号 : `ai_voice.ai_models`
  - 图像识别 : `ai_voice.image_recognition`
  - 演讲 : `ai_voice.speech`
  - 语音助理: `ai_voice.voice_assistants`
- 电器 & 清洁:烹饪和厨房用具(葡萄酒,咖啡机,苏维德酒,烹调温度计,酿造),洗衣,机器人真空和拖把,以及香料扩散器.
  - 电器和清洁, 一般: {提倡}
  - 正在清理 : `appliances_cleaning.cleaning`
  - 烹饪 : `appliances_cleaning.cooking`
  - 洗衣业: `appliances_cleaning.laundry`
- 盲人和窗帘:盲人、窗帘、百叶窗、乌鸦、车库门和大门。
  - 窗帘和窗帘: `blinds_curtains`
- 按钮 & 遥控器:智能按钮,遥控器,以及控制其他设备的红外或无线电爆破器.
  - 美丽 :
- 气候:加热,冷却和通风:加热器,热泵,空调,风扇,加湿器,空气净化器和水热器.
  - 气候,一般:`climate`
  - 空气净化器和加湿器: `climate.air_purifiers_humidifiers`
  - 扇形和通风: `climate.fans_ventilation`
  - 热泵和空调: `climate.heat_pumps_air_conditioning`
  - 自动调温器( G) : `climate.thermostats_heating`
  - 热水器 : `climate.water_heaters`
- 计算机 & 网络:路由器,NAS,服务器,打印机,3D打印机,云托管,开发者工具以及运行时间监控.
  - 计算机和网络, 一般: `computers_network`
  - 云开发工具( D) : `computers_network.cloud_developer_tools`
  - 监测: `computers_network.monitoring`
  - NAS 服务器( S) : `computers_network.nas_servers`
  - 打印机 : `computers_network.printers`
  - 路由器和网络 : `computers_network.routers_network`
- DIY & makers:构建自己的:固件,消息经纪人,以及网络API,数据库,序列端口和Modbus的通用连接器.
  - DIY & 制造器, 一般为: `diy_makers`
  - 板和硬件接口 : `diy_makers.boards_hardware`
  - 网络和数据连接器 : `diy_makers.web_data_connectors`
- 能源:太阳能电池板、家用电池、能源计、电压充电器、发电机、UPS、天然气和丙烷罐以及能源价格。
  - 能源,一般:`energy`
  - 备份功率 : `energy.backup_power`
  - 能源价格: `energy.energy_prices`
  - EV 充电: `energy.ev_charging`
  - 测量表( M) : `energy.meters_monitoring`
  - 太阳能电池( B) : `energy.solar_batteries`
- 财务:银行账户、预算编制工具、股票、货币汇率和密码货币。
  - 财务:`finance`
- 花园和植物:灌溉、割草机、植物传感器、水栽培和温室。
  - 花园和植物 : `garden_plants`
- 健康和福利:天平、牙刷、睡眠和健身跟踪、葡萄糖监测和婴儿护理。
  - 健康和福利:`health_wellbeing`
- 辅助工具：你自己创建的实体，没有背后的设备：切换开关、数字、计时器和时间表，以及由其他实体计算得出的数值。
  - 帮助者,一般: `helpers`
  - 计算值 : `helpers.calculate_value`
  - 存储一个值 : `helpers.store_value`
- 各有各种设备都具有哪些是哪些是哪些是哪些是哪些是哪些是哪些是哪些是哪些是哪些是哪些是哪些是哪些是哪些是哪些是哪些是哪些是哪些是哪些是哪些是哪些是哪些是哪些是哪些是哪些是哪些是哪些是哪些是哪些是哪些是哪些是哪些是哪些是哪些是哪些是哪哪是哪是是哪哪是哪是哪是哪是哪是是哪是哪是哪是哪是哪是是是哪是哪是是哪是哪是是是哪是哪是哪是哪是哪是是哪是哪是哪是哪是哪是哪是哪是哪是哪是哪是哪是哪是哪是哪是哪哪是哪是哪是哪是哪是哪是哪是哪是哪是哪是哪是哪是哪哪是哪是哪是是哪是哪是哪是哪是哪是都都都都都都都都都都都都都都都都都都都都都都都都都都都都都都都都都都都都都都都都都都都都都都都都都都都都都都都都都
  - , 一般的枢纽和协议 : `hubs_protocols`
  - 大楼自动化乃是: `hubs_protocols.building_automation`
  - 智能主机: `hubs_protocols.smart_home_hubs`
  - 237. 国家调查局在《国家调查报告》中发现,在《国家调查报告报告》中,国家调查局对《国家调查报告》进行了调查。
- 照明:智能灯泡,灯条,固定装置和照明系统.
  - 照明,一般:`lighting`
  - 散装灯具( L) : `lighting.bulbs_lamps`
  - LED 条控件( C) : `lighting.led_strips_controllers`
  - 照明系统: `lighting.lighting_systems`
- 地方服务:垃圾收集、停电、停车、燃料价格和其他城市或公用事业信息。
  - 当地服务: `local_services`
- 媒体与娱乐:电视,扬声器,流媒体,音乐服务,接收器,游戏控制台,游戏服务器和收音机.
  - 媒体娱乐,一般为:`media_entertainment`
  - 游戏: `media_entertainment.gaming`
  - 音乐和无线电服务: `media_entertainment.music_radio_services`
  - 扬声器( A) : `media_entertainment.speakers_audio`
  - 电视流线: `media_entertainment.tv_streaming`
- 消息通知( A) : 发送和接收消息: 按下通知, 电子邮件, 聊天应用, 短消息和电话 。
  - 通讯通知, 一般为: `messaging_notifications`
  - 聊天应用程序 : `messaging_notifications.chat_apps`
  - 电子邮件、 短信和电话: `messaging_notifications.email_sms_calls`
  - 按下通知 : `messaging_notifications.push_notifications`
- 新闻和社交媒体:跟随新闻和RSS的素材,跟随或贴到社交网络,博客和视频频道.
  - 新闻和社交媒体: `news_social_media`
- 其他生态系统:在Apple Home,Alexa,Google Home等平台使用您的Home Assistant设备.
  - 其他生态系统:`other_ecosystems`
- 宠物:进食器,垃圾箱,宠物门,宠物跟踪器和水族馆.
  - 宠物 : `pets`
- 插件 & 开关:智能插件,光开关,发光和继电器.
  - 插件开关( T) : `plugs_switches`
- 存在一封( R) 地址: 知道谁是家, 设备在哪里: 电话、 跟踪器和网络存在 。
  - 存在位置, 一般为: `presence_location`
  - 网络存在: `presence_location.network_presence`
  - 电话和伴侣应用程序 : `presence_location.phones_companion_apps`
  - 跟踪器 : `presence_location.trackers`
- 生产力和信息:日历、待办和购物清单、杂货交付、包裹跟踪、文件、照片和书签。
  - 生产率和信息,一般:`productivity_information`
  - 日历和待办事宜 : `productivity_information.calendars_todos`
  - 文档照片( P) : `productivity_information.documents_photos`
  - 购物杂货店: `productivity_information.shopping_groceries`
- 保安和安全:摄像头、门铃、锁、键盘、警报系统、警报器和烟雾警报器。
  - 安全保障,一般为: `security_safety`
  - 警报系统 : `security_safety.alarm_systems`
  - 摄像头 : `security_safety.cameras`
  - 门铃和对讲机: `security_safety.doorbells_intercoms`
  - 加锁访问( A) : `security_safety.locks_access`
  - 烟雾和CO 提醒 : `security_safety.smoke_co_alarms`
- 传感器:运动、门窗、温度、湿度和空气质量传感器。
  - 传感器,一般:`sensors`
  - 空气质量: `sensors.air_quality`
  - 门窗( W) : `sensors.door_window`
  - 运动存在( P) : `sensors.motion_presence`
  - 温度和湿度 : `sensors.temperature_humidity`
- 车辆与运输:汽车,EV,电子自行车,公共交通和飞行跟踪.
  - 车辆和运输,一般: `vehicles_transport`
  - 自行车( S) : `vehicles_transport.bikes_scooters`
  - Cars & EVs: `vehicles_transport.cars_evs`
  - 飞行: `vehicles_transport.flights`
  - 精灵车站:
- 水:水表,漏水检测,软化剂和过滤器,水箱,池和温泉.
  - 水,一般为:`water`
  - 仪表和漏出检测 : `water.meters_leak_detection`
  - 游泳池( S) : `water.pools_spas`
  - 水处理: `water.water_treatment`
- 天气和警报:预报,室外空气质量,花粉,以及对风暴,洪水,地震或空袭的公共警告.
  - 天气警报, 一般为 `weather_alerts`
  - 空气质量和花粉: `weather_alerts.air_quality_pollen`
  - 预测 : `weather_alerts.forecasts`
  - 公开警告 : `weather_alerts.public_warnings`
