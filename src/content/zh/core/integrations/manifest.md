---
title: 整合表
description: 每一个显式的钥匙 Json,它做什么, 以及它所接受的价值。
sidebarLabel: 声明
sidebarGroup: 参考
order: 1
---

# 整合表 {#the-integration-manifest}

每个集成都有一个[显示](/glossary/manifest):一个`manifest.json`文件在集成文件夹中,告诉Home Assistant集成是什么,需要什么,如何发现. Home Assistant在装入任何代码前读它。

以下是"空中升降机"整合表:

```json
{
  "domain": "airgradient",
  "name": "AirGradient",
  "codeowners": ["@airgradienthq", "@joostlek"],
  "config_flow": true,
  "documentation": "https://www.home-assistant.io/integrations/airgradient",
  "integration_type": "device",
  "iot_class": "local_polling",
  "quality_scale": "platinum",
  "requirements": ["airgradient==0.10.0"],
  "zeroconf": ["_airgradient._tcp.local."]
}
```

Hassfest,核核的验证脚本,检查每一份清单. 它要求按键排序:`domain`,然后`name`,然后按字母顺序排列其他一切. 运行 `python3 -m script.hassfest` 检查您的键, 它排序您的键 。

## 需要的密钥 {#required-keys}

### 域名 {#domain}

集成的短而独特的名称,由小写字母,数字,和下划线组成,如`mobile_app`. 它必须匹配列表所在的文件夹名称,它永远不能改变:配置条目,实体ID,用户自动化都参考它.

### 名称 {#name}

名字使用者见. 使用产品或服务的名称,并遵循这些规则:

- 如果一个产品或/59/736服务同时具有局部和云集,则云集在名称上加上"云",如**LIFX云**.
- 本地的(或支持本地和云的)使用平原名称,如**LIFQQ. 不要添加“ 本地” 。
- 以云为主的产品或服务的集成,自然使用其名称,如**iCloud**,而非**iCloud云**.

### 代码所有者 {#codeowners}

GitHub用户名或团队名称列表,如`["@frenck"]`负责整合的人员. 他们被告知问题和pull request。 至少加上你一个人 质量等级及以上银级的集成必须至少有一个集成所有者.

### 文档 {#documentation}

文件的URL. 对于核心中的整合,这是`https://www.home-assistant.io/integrations/<domain>`. 自定义集成必须指向自己的文档,服务于`https`.

### 中枢 {#iotclass}

[IOT 类](/glossary/iot-class) : 整合如何与设备或服务交谈 。 每个连接到某物的集成都必需.

| 数值 | 含义 |
| --- | --- |
| `local_polling` | 直接与设备交谈, 并请求间隔更新 |
| `local_push` | 直接与设备交谈, 设备告诉 Home Assistant 当有变化时 |
| `cloud_polling` | 匀经云,请按时间间隔更新 |
| `cloud_push` | 穿过云,它告诉Home Assistant 当事物改变 |
| `assumed_state` | Home Assistant 无法获得状态, 所以它假设最后一个命令状态 |
| `calculated` | 不要说话,它计算结果 |

## 设置和类型 {#setup-and-type}

### 集成类型 {#integrationtype}

融为何事. 核心与配置流的融合必须设置它. 当它缺失时, Home Assistant 将集成处理为 `hub`, 但无论如何设置它 。

| 数值 | 用它 Is it for |
| --- | --- |
| `device` | 每个配置 非单设备, 如 ESPHome |
| `hub` | 像飞利浦· 哈哈在以下方面向它们提供多种设备或服务的网关 |
| `service` | 比 我叫比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比年年比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比比仙仙的年年年年年比比比比比比比比比比比比比比比的年年年年年比比比比比比比比比比比比的年年年年年年年比比比的年比比比比比比比比比比比比比比的年年年年年年年年年比比比比比比比比比比比比比比比比比比比比比比比的比比比比的年年年比比比比比比比比比比比比比比比比比比比比比比比的比比比比比比比比比比 |
| `helper` | 帮助用户实现自动化的实体,如衍生工具或组 |
| `entity` | 一个基本实体平台,如`sensor`或`light`. 一般不应使用。 |
| `hardware` | 像Raspberry Pi一样的硬件集成,一般不应使用. |
| `system` | 预留系统集成. 一般不应使用。 |
| `virtual` | 完全不是整合 而是指向另一个 见[虚拟集成](/core/integrations/manifest#virtual-integrations). |

`hub`和`device`或`service`的区别在于,一个配置条目代表的是:一个枢机可以访问许多设备或服务,而其他的则提供完全一个.

### 类别 {#categories}

分类人员通过网站集成页面、应用程序和市场找到整合。 每个条目都是类,如{H适用范围},或者有子类的类别,如`energy.meters_monitoring`. 第一个条目是初级类别:最能说明融合的目的。

以下是Shelly整合的类别:

```json title="manifest.json"
{
  "categories": [
    "plugs_switches",
    "lighting.bulbs_lamps",
    "energy.meters_monitoring"
  ]
}
```

检查:

- 有1至3个条目,不重复.
- 每个条目都是已知的类别或子类别.
- 一个类别不在其子类别旁边列出, 如 `energy` 与 `energy.meters_monitoring` 。
- 实体,系统和虚拟集成没有关键.
- 核心中的所有其他整合都有关键。 对于定制整合,它是可选的.

多数这些检查需要核心的类别列表,所以只有在核心检查内部验证时才会运行. 忙碌 GitHub 实现自定义整合的动作 。 对于自定义集成来说,未知的分类是匆忙中的一种警告而不是错误,因此核心变化不会在您的寄存器中失败的分类. [动作 HACS](/marketplace/reference/validation) 在未知的类别上失败 。

见[融合类别](/core/integrations/categories) 对于每一个类别, 以及如何选择正确的类别 。

### 配置( F) {#configflow}

设定 `"config_flow": true` 当集成有 `config_flow.py` 时, 用户可以从 UI 中添加 。 见[配置流量](/core/integrations/config-flow).

### 单位配置  输入 {#singleconfigentry}

当集成只支持一个配置条目时设定 `"single_config_entry": true` 。 Home Assistant 然后阻止用户添加第二个 。

## 依赖性和要求 {#dependencies-and-requirements}

### 所需经费 {#requirements}

84. 一个 Python 列表, 以 `pip` 格式包装集成需要, 并固定在精确的版本上, 如 `["airgradient==0.10.0"]` 。 Home Assistant 在装入集成之前安装它们 。 如果安装失败, 集成不会加载 。

自定义集成只应列出尚未对Home Assistant本身的要求。

在库中工作时,您可以测试尚未在PyPI上的版本的整合. 自己安装, 告诉 Home Assistant 不要替换它 。 从您的核心检出中运行此选项, 并将库放在其旁边的文件夹中 :

```shell
uv pip install -e ../my-library
hass --skip-pip-packages my-library
```

要让 Home Assistant 完全不安装或替换任何软件包, 请从 `hass --skip-pip` 开始 。

在开发容器中,您退出的旁边的文件夹不存在 : 见 [在 Home Assistant 尝试您的库](/core/integrations/api-library#try-your-library-in-home-assistant) 。

或将要求指向一个 git 引用,它可以是分支,标记,或承诺:

```json
{
  "requirements": [
    "my-library@git+https://github.com/me/my-library.git@my-branch"
  ]
}
```

不要提交带有 git 要求的 pull request 。 先在PyPI上发布库.

### 依赖关系 {#dependencies}

在此加载之前必须建立的其他整合。 当您的集成不能没有另一个时使用它,例如因为它需要webhooks(`webhook`)或MQTT连接(`mqtt`). 它不能保证其他整合的配置条目尚未设置.

### 属性后( D) {#afterdependencies}

整合可以使用,但不需要。 如果它们被配置, Home Assistant 首先设置它们 。 无论哪种方式,他们的要求都安装了,这样你就可以安全地从它们进口. 例如,`camera`列出`media_player`:如果`media_player`被配置,它就会在`camera`之前加载,如果没有,那么`camera`无论如何加载.

Hassfest 检查您从 `dependencies` 或 `after_dependencies` 中导入的集成项, 例外 。 您可以从实体平台集成中导入,比如`sensor`或`light`,也可以从一组内部集成中导入,比如`webhook`或`zone`,而不列出它们. 完整列表为`ALLOWED_USED_COMPONENTS`在[`script/hassfest/dependencies.py`](https://github.com/home-assistant/core/blob/dev/script/hassfest/dependencies.py)中. 这只涵盖导入: 如果您的整合需要设置其中之一, 如 `webhook` , 列出它 。 从不列出`homeassistant`或`persistent_notification`在`dependencies`中。 他们总是满载, 和烦恼拒绝他们在那里。 核心中的整合只能列出核心中的其他整合. 自定义集成也可以列出自定义集成.

### 日志 {#loggers}

日志名列表中您在 `logging.getLogger` 呼叫中使用的要求, 如 `["aiohue"]`. Home Assistant 使用它将库的日志信件与您的集成连接起来, 例如当用户允许调试日志时 。

## 质量和 这个状况 {#quality-and-status}

### 质量 尺度 {#qualityscale}

[整合质量尺度](/core/quality-scale) 整合的层次达到: `bronze`, `silver`, `gold` 或`platinum` 。 新集成必须至少达到 `bronze` 。 值 `internal`, `legacy`,`custom` 和`no_score` 都保留给特殊可通过的 。

### 已禁用 {#disabled}

使集成无法加载的简短原因, 如 `"Library is broken with the latest firmware"`. Home Assistant 记录原因 。

### 预览( F) {#previewfeatures}

实验室 我不喜欢这样的功能 实验室预览中包含持久的解决办法: 实验性功能 用户在成为集成的正常部分之前打开自己. 每个关键是特征的闪点,有反馈、更多信息和报告问题的可选链接。 整个工作流程见[实验室](/core/development/labs)。

```json
{
  "preview_features": {
    "my_preview_feature": {
      "feedback_url": "https://community.home-assistant.io/t/12345",
      "learn_more_url": "https://www.home-assistant.io/integrations/example",
      "report_issue_url": "https://github.com/home-assistant/core/issues"
    }
  }
}
```

## 仅自定义集成 {#custom-integrations-only}

这些密钥只在自定义集成中有效 :

- `version`: 必需。 一个[厉害的版本](https://github.com/ludeeus/awesomeversion)理解的版本,如`"1.2.0"`(SemVer)或`"2026.10.1"`(CalVer).
- `issue_tracker`:用户报告问题的URL. 核心中的集成将其排除在外,Home Assistant与核心寄存器的链接.
- `import_executor` : Home Assistant 导入执行器中的集成, 所以缓慢的导入不会阻断 [事件循环](/glossary/event-loop) 。 设定为 `false` 前提是您的集成必须在事件循环中导入 。

## 发现 {#discovery}

这些密钥告诉 Home Assistant 如何识别您的设备, 当找到时启动您的配置流 。 值必须遵循一些规则(有些小写,有些大写),这导致检查出现问题。 解释接下来会发生什么。

### 蓝牙 {#bluetooth}

选手名单. 一个设备匹配至少一个匹配器供大会审议的每个密钥 。

| 密钥 | 匹配 |
| --- | --- |
| `local_name` | 广告名. 支持通配符,但不在前三个字符中. |
| `service_uuid` | 小写中的128位服务 UUID |
| `service_data_uuid` | 128位服务数据 UUID, 小写 |
| `manufacturer_id` | 作为整数的制造商标识 |
| `manufacturer_data_start` | (a) 由制造厂商的一栏所列从0到2 5 |
| `connectable` | 如果设备只需要广告, 则设定为 `false` 。 默认为 `true` 。 |

```json
{
  "bluetooth": [
    { "local_name": "Prodigio_*" },
    { "manufacturer_id": 76, "manufacturer_data_start": [6] }
  ]
}
```

为了匹配一个16位的UUID,把它变成128位的1:用它替换`00000000-0000-1000-8000-00805f9b34fb`的第三和第四字节. 16 位 UUID `0xfd3d` 成为 `0000fd3d-0000-1000-8000-00805f9b34fb` 。

### 零配置 {#zeroconf}

mDNS服务类型列表. 一个项目要么是一个字符串,要么是一个有 `type` 和过滤器的对象。 对 `_http._tcp.local.` 等通用类型使用过滤器, 这样您就不会在网络上获得每个网络服务器 。

```json
{
  "zeroconf": [
    "_googlecast._tcp.local.",
    { "type": "_http._tcp.local.", "name": "example*" },
    {
      "type": "_axis-video._tcp.local.",
      "properties": { "macaddress": "00408c*" }
    }
  ]
}
```

`name`和`properties`中的过滤器必须是小写,并可以使用通配符。 某个项目的顶级过滤器 `macaddress`特别是最不发达国家的 `model` 和 `manufacturer` 已贬值 : 使用 {H正处于 `properties` 代替 。

### 密码 {#ssdp}

之间的互动 我们去依循仍处于ام Anh rồi của各种不同的之后才在其各自 我发誓显现以及其他有关 你有什么、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、携手、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、向其提供、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、 设备匹配至少一个匹配器的每个密钥时匹配 。

```json
{
  "ssdp": [
    {
      "st": "roku:ecp",
      "manufacturer": "Roku",
      "deviceType": "urn:roku-com:device:player:1-0"
    }
  ]
}
```

### 亲子关系 {#homekit}

HomeKit设备的模型名称. 当一个设备的完整模型名称,或者它的第一个单词(最多一个空格或连字符)出现在列表中时,它就匹配了. 一个模型也可以是带有通配符的图案,比如`LIFX*`. 您不需要说 HomeKit 协议: 您可以任意方式与设备交谈 。 一旦您的集成与模型匹配, 不与 HomeKit 配对的设备的发现信息就不再用于听 HomeKit 零conf 类型的集成 。

```json
{
  "homekit": {
    "models": ["LIFX"]
  }
}
```

### 卢拉旺 {#lorawan}

LORAWAN选手名单. 每个匹配器是一对堆栈,如`"chirpstack"`或`"tts"`,网络服务器为您的供应商使用的品牌ID,作为字符串或整数. 您的集成需要 `config_flow` 设定为 `true` , 而 `lorawan` 在它的 `dependencies` 中 。

```json
{
  "config_flow": true,
  "dependencies": ["lorawan"],
  "lorawan": [["chirpstack", 744], ["tts", "sensecap"]]
}
```

国安国安国安国安国安 有什么也应 妈妈 我没有以便为你仍有 页 怎么 好吗则是 我来应与都将 小 :: 匹配者只选择您的整合: 您的库决定它所支持的模型 。 见[LoRAWAN 设备](/core/internals/lorawan).

### 百万吨 {#mqtt}

MQTT 要订阅以进行发现的话题列表 。 将 `mqtt` 添加到 `dependencies` (或 `after_dependencies`) 。

```json
{
  "mqtt": ["tasmota/discovery/#"]
}
```

在您的集成订阅话题之前, 请等待 MQTT 客户端 `await mqtt.async_wait_for_mqtt_client(hass)` 。 它在 MQTT 正在设置时等待, 并在客户端可用时返回 `True` 或 `False` 当 MQTT 未设置或没有及时可用 。

### 数据 {#dhcp}

DHCP流量的匹配者列表. `hostname`必须是小写,而`macaddress`(MAC地址的第一部分,没有结肠)必须是大写,并包含通配符. 匹配使用 [取消文件名模式](https://docs.python.org/3/library/fnmatch.html) 。

```json
{
  "dhcp": [
    { "hostname": "rachio-*", "macaddress": "009D6B*" },
    { "hostname": "[dp]achio-*", "macaddress": "009D6B*" },
    { "registered_devices": true }
  ]
}
```

匹配 `"registered_devices": true` 的设备的匹配器, 您的集成在 [设备注册](/core/integrations/device-registry) 中已经注册了 MAC 地址连接 。 在主机名称或MAC前缀匹配太宽时,用它来了解已知设备的新IP地址.

8. 宽宽的宽宽的宽宽的宽宽的宽宽的宽宽宽的宽宽的宽宽的宽宽的宽宽的宽宽的宽宽宽的宽宽的宽宽的宽宽的宽宽的宽宽宽的宽宽的宽宽的宽宽的宽宽的宽宽的宽宽的宽宽的宽宽的宽宽的宽宽的宽宽的宽宽的宽的宽宽的宽宽的宽宽的宽的ý宽的宽宽的宽宽的宽宽的宽宽的宽宽宽的宽宽的宽宽的宽的宽的宽的宽宽宽的宽宽的宽的宽的宽宽的宽宽的宽的宽宽的宽的宽宽的宽的宽的宽宽的宽的宽宽宽的宽的宽宽的宽的宽的宽的宽的宽的宽的宽宽宽的宽宽的宽宽宽的宽的宽宽的宽的宽的宽的宽的宽宽的宽小的宽的宽的宽的宽小的宽的宽的宽的宽的宽的宽的宽的宽的宽的宽的宽的宽的 它们一般比DHCP提供更好的经验.

### 单位b {#usb}

USB设备上的匹配者列表: `vid` 和 `pid`(上),以及 `serial_number`, `manufacturer`, 和 `description`(允许使用小写,通配符) 。 [Debian 维基文库](https://wiki.debian.org/HowToIdentifyADevice/USB) 解释如何找到这些值 。 `known_devices`是一个包含匹配者封面的产品名称列表. 它不用于匹配 。

```json
{
  "usb": [
    { "vid": "10C4", "pid": "EA60", "description": "*zigbee*" }
  ]
}
```

> [!WARNING]
> 一些VID和PID组合被许多不相关的设备使用. 带有PID `EA60`的VID `10C4`是任何硅实验室 CP2102 USB对序列芯片. 匹配 `description` 或其他值, 或用户为不属于您的设备获取发现消息 。

## 虚拟一体化 {#virtual-integrations}

有些产品使用一种不以它们命名的集成方式。 8月 Bluetooth 锁定与耶鲁访问 Bluetooth 集成的工作, 有些产品只使用类似 Z-Wave 的标准. 虚拟集成帮助用户找到正确的集成:它只是一个表征,没有任何代码,只有核心中的集成才能提供.

虚拟集成有一个 `domain`, 一个 `name`, `"integration_type": "virtual"` , 以及这两个密钥中的一个 :

- 其为历史历史,以历史为历史,以历史为历史,以历史为历史. ......
- 深入人心 `iot_standards`:产品使用的标准列表 `homekit`,`zigbee`,或`zwave`.

```json
{
  "domain": "august_ble",
  "name": "August Bluetooth",
  "integration_type": "virtual",
  "supported_by": "yalexs_ble"
}
```

用户在添加集成时会找到产品,并且Home Assistant将它们发送到正确的配置流. 产品还在[Home Assistant.io](https://www.home-assistant.io/)上获得一个生成的页面. 将产品的标志添加到 [品牌存储器](/core/integrations/brands) 。

> [!TIP]
> 如果一个品牌制作的产品使用像Zigbee这样的标准,则在[品牌](/core/integrations/brands#brand-files)上设定IOT标准. 只使用虚拟集成,如果这会迷惑用户的话.
