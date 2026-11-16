---
title: 实体登记处
description: 给实体一个独特的ID,以便实体登记册能够记住它们,将它们链接到设备上,并决定它们是否启动启用、可见或分类。
sidebarLabel: 实体登记册
sidebarGroup: 基本情况
order: 7
---

# 实体登记处 {#the-entity-registry}

本页面介绍您的实体如何从实体一侧进入实体登记册。 要从您的整合代码中查找或移动注册项, 请参见 [非常大实体登记处](/core/integrations/entity-registry) 在构建整合中 。

实体 [登记](/glossary/registry) 是 Home Assistant 记得它见过的每一个实体的地方 。 它保留实体ID,它所属的设备和区域,以及用户改变的一切:名称,图标,实体ID,是否启用,以及像首选单位一样的选项. 这些设置在重新启动、重新安装设备以及更新您的集成后幸存下来。

实体只有在有 [唯一标识](/glossary/unique-id) 时才能获得登记项。 如果没有一个,用户就不能重命名它,改变它的图标,把它放在一个区域,或者从界面中禁用它. 所以给每个实体一个独特的身份

## 独一无二的ID {#unique-id}

注册处通过三件事一起找到一个实体:其域(类似`sensor`),提供它的集成(类似`hue`),以及其独特的ID. 独一无二的ID 必须是独一无二的组合。 不要将您的集成域或实体域放入其中, Home Assistant 已经跟踪这些域了 。

独特的ID绝不能改变,用户也不能改变. 当它改变时,Home Assistant看到一个全新的实体,所有用户为旧实体设置的东西都不见了.

唯一身份的好来源 :

- 设备的序列号
- 设备的MAC地址,格式化为`format_mac`,来自`homeassistant.helpers.device_registry`. 从设备API或发现中读取,从网络的ARP表格中读取
- 在设备上打印或存储在其固件中的独特标识符
- 描述某地的实体的固定位置,如纬度和经度

作为最后手段,对于从[配置条目](/glossary/config-entry)设置的实体,使用配置条目ID.

永远不要使用这些:IP地址,主机名,URL,设备名称,电子邮件地址,或用户名. 他们都变了

当一个 如果我们的设备有多个实体, 请将设备的独有的ID 和能将实体区分开的东西合并起来, 如 [实体描述](/glossary/entity-description) 的密钥 : `f"{serial}_{description.key}"` 。

## 链接到一个装置 {#linking-to-a-device}

设定 `device_info` 将一个实体链接到 [设备](/glossary/device) 。 Home Assistant 第一次看到设备时在设备登记册中创建设备, 当信息变化时更新它. 所有具有相同识别特征的实体最终都在同一设备上.

```python
from homeassistant.helpers.device_registry import DeviceInfo

self._attr_device_info = DeviceInfo(
    identifiers={(DOMAIN, device.serial)},
    manufacturer="Example",
    model="Pump 3000",
    name=device.name,
    sw_version=device.firmware,
)
```

只有拥有独有的ID并且属于一个配置条目的实体才能链接到一个设备. 尝试获得警告的其他实体,链接将在Home Assistant2027.8.

`DeviceInfo` 的字段均为可展示了, 但设备至少需要 `identifiers` 或 `connections` :

| 外地 | 说明 |
| --- | --- |
| `identifiers` | 用于识别集成中设备的 `(domain, id)` 拖拉 。 |
| `connections` | 组合 `(type, id)` tuples , 像 MAC 地址一样, 其他集成可以匹配 。 |
| `name` | 装置名. |
| `manufacturer`, `model`, `model_id` | 谁做的, 和模型名称和模型号码。 |
| `serial_number` | 序号. |
| `sw_version`, `hw_version` | 坚固的软件和硬件版本。 |
| `configuration_url` | 配置设备的 URL, 如其网络界面 。 |
| `suggested_area` | 设备刚创建时应降落的区域。 |
| `entry_type` | `DeviceEntryType.SERVICE` 对于不是物理设备的东西, 像网络服务。 |
| `via_device_id` | 这个设备的设备注册ID 连接通过,像一个中枢。 |
| `translation_key`, `translation_placeholders` | 一个翻译设备名称,来自`device` `strings.json` 的 `device` 一节 。 |

`via_device_id` 替换旧的 `via_device` 字段, 字段用了一个识别符拖转, 在 Home Assistant 2027.8 中被删除 。

### 儿童装置 {#child-devices}

有些设备是由逻辑部件制造的,比如电源带的插座. 使用 `ChildDeviceInfo` 以您已经注册的设备的孩子身份注册此部分 。 它需要孩子的`identifiers`,`parent_device_id`(父母的装置注册ID),以及可选的`name`,`suggested_area`,和一个带有占位符的翻译密钥. 父母必须在同一配置条目注册,并属于同一配置子条目.

## 实体类别 {#entity-categories}

并不是每个实体都是其装置的主要特征. 以 [实体类别](/glossary/entity-category) 从 `homeassistant.const` 标记其他 。 值列是您在 YAML 中设置的内容, 例如 `entity_category` 的 [切换](https://www.home-assistant.io/integrations/switch.mqtt/) 。

| 实体类别 | 数值 | 用它 Is it for |
| --- | --- | --- |
| `EntityCategory.CONFIG` | `config` | 实体改变设备的设置,如状态LED的开关,或运动传感器敏感度的编号. |
| `EntityCategory.DIAGNOSTIC` | `diagnostic` | 该实体在不改变设备的情况下显示设备信息,如信号强度或IP地址. 还用它来做一个使设备自我识别的按钮. |

被分类的实体在设备页面上显示在自己的章节中,不加入自动生成的仪表板,默认不会接触到语音助理,当一个动作针对整个设备或区域时,也不成为目标. 传感器和二进制传感器不能使用 `CONFIG` 类别.

## 默认启用和可见 {#enabled-and-visible-by-default}

有些实体对少数人有用,对其他人也有噪音,如信号强度传感器或每秒变化的传感器. 为那些设定 `entity_registry_enabled_default` 到`False` 。 该实体被注册为禁用:它不运行,不写入状态,也不填充数据库,直到用户启用.

`entity_registry_visible_default` 设定为`False` 将实体登记为隐藏 。 其无法无天,但无法无天,无法无天,无法无天,无法无天,无法无天,无法无天,无法无天,无法无天,无法无天,无法无天,无法无天,无法无天,无法无天,无法无天,无法无天地无天,无法无天地无天地无天地无天. 用它来对付那些参与大事情的实体 比如一个集团的成员

两者仅在该实体首次登记时适用。 后由用户决定.

## 残疾实体 {#disabled-entities}

注册项的 `disabled_by` 字段说明一个实体被禁用的原因 。 当您的整合通过 `async_add_entities` 时, 禁用实体不添加到 Home Assistant 。

| 数值 | 含义 |
| --- | --- |
| `user` | 用户在界面中将其禁用. |
| `integration` | 集成以 `entity_registry_enabled_default` 注册为禁用之间关系, 或用户关闭 ** 可新建的实体 ** 用于配置项 。 |
| `config_entry` | 配置条目已禁用 。 |
| `device` | 实体的设备已禁用 。 |
| `hass` | Home Assistant 将其禁用。 |

当用户禁用一个实体时, Home Assistant 立即删除它 。 当用户允许配置项的实体时, Home Assistant 重新装入配置项可以添加它 。 它等待在最后一个实体被启用后30秒,所以一个允许多个实体的用户会导致一个重载. 您的整合必须支持卸载, 以便不重启操作 。

确保您的整合能与从未添加的实体相适应。 如果您保留对实体对象的引用, 请在 `async_added_to_hass` 中注册, 它只运行为实际添加的实体 。 见[实体生命周期](/core/entities/lifecycle).

如果您的集劳资制允许用户选择创建哪些实体, 如在 [选项流动](/glossary/options-flow) 中, 请不要使用 `disabled_by` 。 不要创建用户解选的实体, 并把它们从实体和设备注册中删除 。

单个配置条目最多可拥有10,000个启用实体。 除此之外,Home Assistant没有添加新的,并且登录一个警告,因此行为不端的集成不能使整个系统下沉. 少数管理大型网络的集成,比如Z-Wave和Matter,是免责的.

## 实体选项 {#entity-options}

登记册还按域组存储每个实体的选项。 用户将大部分设置在实体设置中,如显示精度或传感器的单位,或日历的颜色. 平台基础课从 `self.registry_entry.options` 读取, 并为您处理 。 您的整合通常不需要读或写.
