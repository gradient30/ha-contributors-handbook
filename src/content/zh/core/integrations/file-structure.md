---
title: 集成文件结构
description: 一个集成的文档,每个集成的,以及 Home Assistant 在哪里寻找集成.
sidebarLabel: 文件结构
sidebarGroup: 开始
order: 5
---

# 集成文件结构 {#integration-file-structure}

每个集成都生活在以 [域名](/glossary/domain) 命名的文件夹中 。 移动应用程序集成有域名`mobile_app`,因此其所有文件都在`mobile_app/`中. Home Assistant通过文件名找到一个集成的大部分特征,所以下面的名字是matter.

## 所需文件 {#the-required-files}

- `manifest.json`:描述整合,其要求,以及如何发现. 见[显示](/core/integrations/manifest).
- `__init__.py`:整合本身,及其设置功能. 如果集成只提供平台,这个文件可以限于docstring,比如`"""The Mobile App integration."""`.

## 常见文件 {#common-files}

| 文件 | 它所持有的 |
| --- | --- |
| `const.py` | 常数, 如 `DOMAIN` |
| `config_flow.py` | [配置流量](/core/integrations/config-flow) 和[选项流动](/core/integrations/options-flow) 。 |
| `coordinator.py` | [数据更新协调员](/core/integrations/fetching-data),如果你下级 |
| `entity.py` | 您的平台共享的基础实体类 |
| `light.py` , `sensor.py` 等 。 | 每个实体类型一个[平台](/glossary/platform)。见[实体和平台](/core/entities)。 |
| `strings.json` | 所有与用户相遇的文本,英语. 见[使您的字符串可转换](/translate/guides/developers). |
| `icons.json` | 实体、行动和窗体部分的图标 |
| `services.yaml` | [动作](/core/integrations/actions) 您的整合登记册的描述 |
| `quality_scale.yaml` | 每个 [质量尺度](/core/quality-scale) 规则的整合状态 |

## 平台文件 {#platform-files}

有些文件 有什么集成平台: Home Assistant 当需要它们提供的特性时, 按名称加载它们. 您添加了文件, 特性会出现 。

| 文件 | 特性 |
| --- | --- |
| `diagnostics.py` | [诊断](/core/integrations/diagnostics) |
| `system_health.py` | [系统保健](/core/integrations/system-health) |
| `repairs.py` | [修复流量](/core/integrations/repairs) |
| `reproduce_state.py` | [教益](/core/integrations/reproduce-state) 用于场景 |
| `significant_change.py` | [重大变化](/core/integrations/significant-change) |
| `backup.py` | [备份代理和钩子](/core/integrations/backup) |
| `media_source.py` | [媒体来源](/core/integrations/media-source) |
| `application_credentials.py` | [申请证书](/core/integrations/oauth2#application-credentials) 给 OAuth 2.0 |
| `device_trigger.py`, `device_condition.py`, `device_action.py` | [设备自动化](/core/integrations/device-automations) |

## Home Assistant 寻找集成的地方 {#where-home-assistant-looks-for-integrations}

Home Assistant 当一个配置条目或`configuration.yaml`引用其域时,或者当另一个集成依赖于它时,寻找一个集成. 它看起来有两个地方:

- `<config directory>/custom_components/<domain>`
- `homeassistant/components/<domain>`(船与Home Assistant的融合)

与内置域相同的自定义集成会压倒它. 这行得通,但用户随后停止获取该集成的更新,且显示需要`version`. 为自定义集成选择一个独有域, 除非你真的想替换一个内置域 。

## 自定义集成中的品牌图像 {#brand-images-in-custom-integrations}

自定义集成可以在集成文件夹内的 {H屌} 文件夹中传送自己的图标和标志. 在核心中的集成将它们放在[品牌存储器](https://github.com/home-assistant/brands)中。 见[一体化品牌和形象](/core/integrations/brands)。

## 所面对的问题 {#tests}

测试在集成文件夹外直播, 在 `tests/components/<domain>/` 。 见[写作测试](/core/development/tests).
