---
title: 一体化问题。
description: 在集成页面的顶部可以使用的每一个键,它做什么,以及它接受的哪个值.
order: 5
---

# 一体化问题。 {#integration-front-matter}

每个集成页都从前题开始:两条`---`行之间的一个块YAML. 这不仅仅是元数据。 它驱动[一体化概览](https://www.home-assistant.io/integrations/),设置按钮,发现文本,质量尺度徽章,以及页面的侧边栏.

许多密钥反映了 Home Assistant Core 中显示的整合 。 这些必须和清单完全一致。 其中一些,比如`ha_quality_scale`,是通过从核心代码库的文档同步来更新的,所以在第一个版本之后你很少需要触摸它们. 让他们在新的一页仍然在你身上。

## 示例 {#example}

一个从UI设置的集成的典型页面:

```yaml
---
title: Awesome Lights
description: Control your Awesome Lights from Home Assistant.
ha_release: 2026.11
ha_categories:
  - lighting.lighting_systems
ha_iot_class: Local Push
ha_config_flow: true
ha_codeowners:
  - "@your-github-username"
ha_domain: awesome_lights
ha_integration_type: hub
ha_platforms:
  - light
  - sensor
ha_quality_scale: bronze
ha_zeroconf: true
related:
  - docs: /docs/automation/
    title: Automations
  - url: https://www.example.com/awesome-lights/manual
    title: Awesome Lights user manual
---
```

下文按目的分类。 不适用于您的整合的密钥被忽略 。 不要设置 `false` 的密钥以表示“ 否 ” 。

## 基本知识 {#the-basics}

这些密钥属于每个集成ث 的页面 。

- `title`:整合的名称. 使用上面写的表上的`name`。
- ệ { { { { ệnh nghĩa)和链接预览显示.
- `ha_domain`: 整合的领域. 它必须匹配列表中的`domain`和页面的文件名. 以上例为`source/_integrations/awesome_lights.markdown`.
- `ha_release`: 第一次运出集成的 Home Assistant 释放, 格式为 `YYYY.M` 。 对于新的整合,即下一次发布:如果当前发布的是2026.10,使用2026.11. 如果缺少此密钥, 站点构建失败 。
- `ha_codeowners`: GitHub负责集成的用户名或团队,每组从`@`开始. 匹配列表中的 `codeowners` 。 引用每个条目, 因为光 `@` 在 YAML 值开始时无效 。

> [!IMPORTANT]
> 引文在0中释放,如`ha_release: "2025.10"`. "Universits","Universits","Universits","Universits","Universits","Universits","Universits","Universits","Universits","Universit","Usur","Usur","Usur","Usur","Usur","Usur","Usur","Ussur","Ussur","Usur","Ussur","Usel","Uses","Us's","Us","Us",","Us's","Uss","Us","Us","U","U","U"U",",",",",","U"U",",",","U"",","

## 分类 {#classification}

这些键来描述整合是做什么的. 它们在整合概览上为过滤器提供动力.

- `ha_categories`:一个一到三个类别标识符的列表. 为了与自己的核心执行进行整合,使用与该表的`categories`相同的识别符。 类别描述的是产品或服务,而不是它所提供的实体平台. 第1个条目为主类.
  - 使用类,如`lighting`,或子类,如`lighting.lighting_systems`.
  - 不要将重复或一个类别连同它自己的一个子类别一并列出。
  - 标识符和选择方法参见[一体化类别](/core/integrations/categories) 。
  - 没有 `ha_categories` 的页面没有出现在集成概览中 。 实体和系统页面故意将此密钥放出.
  - 旧 `ha_category` 密钥不再被接受 。
- `ha_integration_type`:整合的类型. 它必须在表单中匹配`integration_type`:`device`,`entity`,`hardware`,`helper`,`hub`,`service`,`system`,或`virtual`. 如果列表没有设置一个,则类型为`hub`.
- `ha_iot_class`:整合如何与设备或服务交谈. 使用`Local Polling`,`Local Push`,`Cloud Polling`,`Cloud Push`,`Assumed State`,或`Calculated`,在清单中匹配`iot_class`. 整合取决于设置用途 `Configurable`。 [IoT类博客文章](https://www.home-assistant.io/blog/2016/02/12/classifying-the-internet-of-things/)解释每个班级。
- `ha_platforms`:实体平台集成工具,如`light`和`sensor`. 同时列出`diagnostics` 当整合支持下载诊断时.
- `ha_config_flow` : 如果集成从 UI 设置到 `true` 。 这将设置按钮添加到页面的侧边栏中 。 否则把钥匙放下
- `ha_quality_scale`:质量尺度上的整合等级:`bronze`,`silver`,`gold`,或`platinum`. 内部为 Home Assistant 的集成使用 `internal`, 和尚未得分的旧集成使用 `legacy`. 新的整合,请使用`bronze`. 此密钥由来自核心代码库的文档同步更新, 因此您通常不会手动编辑 。

### 协议和连接器 {#protocols-and-connectors}

按整合的目的选择类别。 带入多种设备的枢纽和无线电协议使用`hubs_protocols`. 串行端口的通用连接器,Modbus 没事的,或者网络API使用`diy_makers`. 特定产品的集成使用该产品的类别,而不论其使用何种协议. 见[如何选择整合类别](/core/integrations/categories#how-to-choose).

## 发现 {#discovery}

设定为 `true` 当可以这样发现集成时 。 它们必须与清单中的发现条目相符。 别管那些不适用的了

- `ha_bluetooth`:发现于Bluetooth。
- `ha_dhcp`:通过DHCP发现.
- `ha_homekit`:通过HomeKit发现.
- `ha_mqtt`:通过MQTT发现的.
- `ha_ssdp`:通过SSDP发现.
- `ha_zeroconf`:通过mDNS发现,又名Zeroconf.

当 `ha_dhcp`,`ha_homekit`,`ha_mqtt`,`ha_ssdp`,或`ha_zeroconf` 被设定时,页面上的标准配置文本告诉读者,Home Assistant可以自动找到他们的设备. 见[整合页面结构](/writing/reference/integration-page#reusable-text).

## 相关 兄弟 {#related-links}

`related` 在页末添加链接 。 每個項目都是一個連結:

- (原始内容存档于2017-09-09). a path on home. 它可能包括一个锚。 这些都出现在**相关专题之下**。 `title`是可选的:没有一条,则使用链接页面的标题.
- `url`:另一个网站的充实链接. 这些凄焰 nó 在 ** 相关链接 ** 下出现,并在新标签中打开。 总是添加`title`, 否则充实的 URL 会被显示 。

```yaml
related:
  - docs: /voice_control/s3_box_voice_assistant/
    title: Create an ESP32-S3-BOX-3 voice assistant
  - url: https://esphome.io/projects/
    title: ESPHome projects
```

指诸位不存在的页面的 `docs` 条目被悄悄地删除, 所以检查您的路径 。

## 虚拟集成和品牌 {#virtual-integrations-and-brands}

有些页面不记录与自己的代码的集成。 它们的存在是为了人们可以找到一个产品 以它的品牌。

*虚拟一体化*是一种通过另一种一体化发挥作用的产品。 它的显式用途为`integration_type: virtual`,有两种.

请问信守力争的主要内容各项人权 请问信守力争的主要内容各项人权

- 她在游戏中扮演的角色: { 它必须匹配`supported_by`在虚拟集成 西安的表单中. 页面上的设置按钮和链接使用此域. 西安
- 上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上 生成的页面使用它告诉读者要设置哪个集成.

"IOT标准"类型是一个品牌,其设备使用标准协议:

- `ha_iot_standard`:产品使用的标准 `zigbee`,`zwave`,或`homekit`。 它必须匹配 `iot_standards` 在清单中。 Matter产品品牌页面使用`matter`. 对于 Zigbee 和 Z-Wave , 页面显示一个按钮, 它开始用该标准添加设备 。

*brand* 页面以一个名称将来自同一制造商的若干集成物或产品分组. 例如,Google品牌页面分组Google集成,Inovelli品牌页面指向Zigbee和Z-Wave标准其设备使用. 一个品牌与虚拟集成并不相同.

- `ha_brand`:如果页面代表品牌而非实际整合,则设置为`true`. 该页面随后从品牌图像中取用其标志,而不是集成图像. 将密钥放在常规整合页面上 。

与 `ha_supporting_domain` 虚拟集成在不设置 `ha_categories` 本身时继承其支持集成的类别 。 没有支持整合的品牌页面,如Matter,Zigbee和Z-Wave品牌,不会继承类别,需要自己的`ha_categories`.

## 等等所提 我来 不会再 哇 比如 37. 给我案件的包括为的各个日期 {#maintainer-only}

不要自己加这些钥匙。 一个维护者设置的

- `works_with`:标记一个品牌,作为[工作与 Home Assistant](https://works-with.home-assistant.io/)伙伴程序的一部分. 它添加了程序徽章,并在页面上生成有关程序的文本. 每个值都是产品认证的连接方法.夙 在适用时列出一个以上, 如  所以你要同时 `zigbee` 和 `matter` 。
  - `zwave`:显示为Z-Wave,并添加Z-Wave徽章和登机文本。
  - `zigbee`:显示为Zigbee,并添加Zigbee徽章和登机文本。
  - `matter`:显示为Matter,并添加Matter徽章和登机文本。
  - `bluetooth`:产品通过Bluetooth连接。
  - `local`:产品在当地工作,例如通过当地网络。
  - 任何其它价值都殆以书面表示,并给予首字母给予选择。
- `featured`:设置为`true`,以便在集成概览上突出集成. 嘞 注意此密钥没有 `ha_` 前缀 。
