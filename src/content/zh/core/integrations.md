---
title: 构建集成
description: 所有的东西都是从表和图 流到收集数据、发现和诊断
order: 10
sidebarGroups:
- 开始
- 设置和配置
- 数据和更新
- 发现
- 装置和登记册
- 融合特征
- 参考
---

# 构建集成 {#building-integrations}

[融合](/glossary/integration)将Home Assistant连接到设备、服务或一个想法。 它生活在自己的文件夹中,在一个表单中描述自己,从一个配置条目设置自己,并将其数据交给Home Assistant作为实体.

这部分网站贯穿了所有内容,任务逐项完成. 这是为写Python的人写的。 您不需要从前到后读: 从教程开始, 当您需要整合时, 请回来 。

> [!TIP]
> 要添加对新设备或服务的支持吗 ? 读 [如何融入](/core/integrations/concepts),然后在 [教程](/core/integrations/tutorial) 中创建 。 首先检查它是否[属于核心](/core/integrations/create#does-it-belong-in-core):项目建议在[市场](/marketplace)第一中发布新的集成,以及核心需要的新集成至少达到[质量尺度](/core/quality-scale)的青铜级.

## 开始 {#getting-started}

- [如何融入](/core/integrations/concepts): 集成, 配置条目, 平台, 实体, 设备, 协调员, 以及事件循环, 用纯语言 。
- [你要我怎样?](/core/integrations/tutorial):一个完整的整合,一步步的,从脚手架到pull request.
- {L增进}: 库中每一个集成都用来与其设备或服务交谈.
- *L0创设:核心中接受的内容,脚手架脚本,以及最小可能的整合.
- [文件结构](/core/integrations/file-structure):哪个文件做什么,在哪里Home Assistant寻找集成.
- [写作测试](/core/development/tests),在开发工作流程中:如何测试集成,有固定装置,模拟和快照.

## 设置和配置 {#setup-and-configuration}

- [配置条目](/core/integrations/config-entries): 设置、卸载和迁移集成,并保存其运行时间数据。
- [配置流量](/core/integrations/config-flow): 让用户从 UI 添加您的整合 。
- [格式、菜单和进度](/core/integrations/flow-steps):每条流的构件.
- [选项流](/core/integrations/options-flow):让用户改变集成行为.
- 这样就可以在配置条目中在全球存储可重复的部分,比如位置。
- [重整和重组](/core/integrations/reauth-reconfigure): và连接细节固定,而不移除整合.
- [OAuth 2.0 和应用程序证书](/core/integrations/oauth2):在云服务中链接用户账户.
- [YAML 配置](/core/integrations/yaml):当它仍然被允许时,它是如何工作的.
- [设置失败和例外](/core/integrations/setup-failures):设备下线时重试,并提升正确的错误.

## 数据和更新 {#data-and-updates}

- [获取数据](/core/integrations/fetching-data):投票,推,和数据更新协调员.
- [傀儡](/core/integrations/events): 火灾事件,并听 Home Assistant中发生的事情。
- [实例 URL](/core/integrations/instance-url): 找到一个设备或服务可以到达的 Home Assistant 的 URL 。

## 发现 {#discovery}

- [发现](/core/integrations/discovery) : 如何找到设备并启动配置流 。
- [网络发现](/core/integrations/network-discovery): 零conf, SSDP, DHCP, USB, 和网络 API.
- [Bluetooth 整合](/core/integrations/bluetooth):最佳做法和BluetoothAPI。
- [正在获取 Bluetooth 数据](/core/integrations/bluetooth-data):由广告驱动的协调员。

## 装置和登记册 {#devices-and-registries}

- [设备注册](/core/integrations/device-registry) : 注册设备, 并链接和分割 。
- 闸门 [实体登记册](/core/integrations/entity-registry) : 向上看并迁移您整合的实体 。
- [区域登记册](/core/integrations/area-registry):什么Home Assistant对区域的了解。

## 融合特征 {#integration-features}

- [动作](/core/integrations/actions):注册用户可以从自动化和脚本调用的动作.
- [设备自动化](/core/integrations/device-automations):设备触发器,条件,和行动.
- [B. 触发因素和条件](/core/integrations/triggers-and-conditions):提供自动化触发器和条件.
- [诊断](/core/integrations/diagnostics):让用户下载数据进行故障排除.
- [系统保健](/core/integrations/system-health):在系统信息页面上显示您的整合状态 。
- [修理费](/core/integrations/repairs):告诉用户问题,并帮助他们解决.
- [请求重新启动](/core/integrations/restart-required) : 告诉Home Assistant 它需要重新启动才能应用更改 。
- [教益](/core/integrations/reproduce-state) : 使场景与您的实体一起工作 。
- [重大变化](/core/integrations/significant-change) : 告诉哪些国家有改变。
- [备份](/core/integrations/backup): 将备份存放在某处, 或者准备一个 。
- [媒体来源](/core/integrations/media-source):曝光可浏览和可播放的媒体.

## 参考 {#reference}

- [名单](/core/integrations/manifest): `manifest.json`的每个密钥.
- [一体化品牌和形象](/core/integrations/brands):一个品牌下的图标,标志,和分组集成.
- [翻译](/core/integrations/translations):`strings.json`的每个部分,参考文献和占位符。

## 相关专题 {#related-topics}

- [实体和平台](/core/entities): 您的集成类型, 如传感器和灯光 。
- [发展工作流程](/core/development):环境,测试,代码样式,并提交您的作品.
- [核心如何运作](/core/internals) : `hass` 对象, 事件环, 以及您整合下的 API 。
- [让你的弦可变](/translate/guides/developers):如何写出翻译可以使用的字符串 。
- [记录您的整合](/writing/guides/integration):每个集成在[Home Assistant.io](https://www.home-assistant.io/)上都有一页.

## 谁说话 {#who-to-talk-to}

- 有技术问题吗? 在 [编码支持**](https://discord.com/channels/330944238910963714/1257019582112334014) 上启动一条线程 。 和你的分支 小心分享一个链接 这样人们就能看到你所问的代码了
- 观察一个保持良好的整合, 做类似的事情。 质量尺度的白金级的许多整合,如`airgradient`,是当前模式的好例子.
- 不知道你的想法是否适合Home Assistant吗? 在写大量代码之前, 在 [架构存储器](https://github.com/home-assistant/architecture/discussions) 打开讨论 。
