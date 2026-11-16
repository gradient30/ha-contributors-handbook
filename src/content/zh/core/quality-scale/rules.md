---
title: 所有规则
description: 每一级集成质量等级的每个规则,都有一份核对表复制到您的 pull request 。
order: -4
---

# 所有规则 {#all-rules}

质量尺度有54条规则:铜牌20条,银牌10条,金牌21条,白金牌3条. 等级需要该等级及其以下各级的每一项规则。 此列表遵循了核心 [`script/hassfest/quality_scale.py`](https://github.com/home-assistant/core/blob/dev/script/hassfest/quality_scale.py) 中最熟悉的规则 。

## 铜 {#bronze}

每一次核心整合的基准. 二十条.

| 规则 | 它问的是什么 |
| ---- | ------------ |
| [动作设置](/core/quality-scale/action-setup) | 动作在集成负载时被注册,而不是每个配置条目. |
| [适当定价](/core/quality-scale/appropriate-polling) | 投票一体化使用与其数据相符的间隔。 |
| [品牌](/core/quality-scale/brands) | 整合在 [品牌存储器](https://github.com/home-assistant/brands) 中有一个标志和图标 。 |
| [常用模块](/core/quality-scale/common-modules) | 协调员住在协调员.py和实体.py中的基础实体。 |
| [配置流量](/core/quality-scale/config-flow) | 该集成是从用户界面设置的，具有清晰的配置流程。 |
| [配置- 流量- 测试- 覆盖](/core/quality-scale/config-flow-test-coverage) | 配置流有全测试覆盖,包括从错误中恢复. |
| [依赖透明度](/core/quality-scale/dependency-transparency) | 依赖是开源的,在PyPI上,并在公共CI中建立和发布. |
| [文件行动](/core/quality-scale/docs-actions) | 文件介绍了一体化的行动。 |
| [文件条件](/core/quality-scale/docs-conditions) | 文件描述了合并的条件。 |
| [高层次文件描述](/core/quality-scale/docs-high-level-description) | 文档描述了集成连接的内容. |
| [设置文件](/core/quality-scale/docs-installation-instructions) | 文件有分步设置的指示,并附有先决条件. |
| [证件 -- -- 搬运](/core/quality-scale/docs-removal-instructions) | 文件解释了如何取消合并。 |
| [文件触发](/core/quality-scale/docs-triggers) | 解脱解脱门. |
| [实体活动设置](/core/quality-scale/entity-event-setup) | 实体在 async add to has 中订阅,并在删除时取消订阅。 |
| [实体- 唯一](/core/quality-scale/entity-unique-id) | 每个实体都有独特的ID,因此用户可以自定义. |
| [有实体名称](/core/quality-scale/has-entity-name) | 设置的实体有 entity name to True, 并在其设备上下文命名 。 |
| [运行时间数据](/core/quality-scale/runtime-data) | 运行时间数据存储于ConfigEntry. 运行时间 数据. |
| [提交的文件 你还好吗?](/core/quality-scale/test-before-configure) | 配置流在创建条目前测试连接. |
| [设置前测试](/core/quality-scale/test-before-setup) | 设置检查它有效, 并提出正确的例外 当它无效。 |
| [唯一配置输入](/core/quality-scale/unique-config-entry) | 同一设备或服务不能设置两次 。 |

## 银 {#silver}

可靠性:错误、离线设备、重新校正和所有权。 十条.

| 规则 | 它问的是什么 |
| ---- | ------------ |
| [动作例外](/core/quality-scale/action-exceptions) | 动作在失败时提高服务Validation Error 或 HomeAssist ant Error 。 |
| [配置- 输入- 卸载](/core/quality-scale/config-entry-unloading) | 集成可以不重启而卸下并重新装入. |
| [文件配置参数](/core/quality-scale/docs-configuration-parameters) | 文件 这是我们每个选项流的每个选项。 |
| [文件安装参数](/core/quality-scale/docs-installation-parameters) | 文档描述了设置时需要的每个字段. |
| [无法获取的实体的人数](/core/quality-scale/entity-unavailable) | 当设备或服务评述不到时,实体便无法进入。 |
| [融合所有人](/core/quality-scale/integration-owner) | 综合体至少有一个综合体所有者。 |
| [不可用时日志](/core/quality-scale/log-when-unavailable) | 集成记录了一个丢失的连接一次,一次当它回来. |
| [并行更新](/core/quality-scale/parallel-updates) | 每个实体平台设置PARALLEL UPDATES. |
| [重新校正流量](/core/quality-scale/reauthentication-flow) | 用户可以在不移除整合的情况下输入新的证书. |
| [试验覆盖](/core/quality-scale/test-coverage) | 测试涵盖整合每个单元的95%以上。 |

## 黄金 {#gold}

畔最优秀的用户体验:发现,设备,翻译,以及用户的文档.畔21条.

| 规则 | 它问的是什么 |
| ---- | ------------ |
| [设备](/core/quality-scale/devices) | 实体被分组在设备中,有完整的设备信息. |
| [诊断](/core/quality-scale/diagnostics) | 用户可以下载诊断,敏感数据进行编辑. |
| [发现](/core/quality-scale/discovery) | 设备被发现,所以用户不需要进行查询. |
| [发现- 更新- info](/core/quality-scale/discovery-update-info) | 发现器在变换时更新已知设备的地址. |
| [文档数据更新](/core/quality-scale/docs-data-update) | 文件解释了数据更新的方式和频率。 |
| [文件实例](/core/quality-scale/docs-examples) | 相应地,以国家为最高。 |
| [已知文件限制](/core/quality-scale/docs-known-limitations) | 文件列出了已知的局限性。 |
| [文档辅助设备](/core/quality-scale/docs-supported-devices) | 文档列出已知的支持和不支持的设备。 |
| [文档辅助功能](/core/quality-scale/docs-supported-functions) | 文件描述了它所提供的实体和功能。 |
| [文档调试](/core/quality-scale/docs-troubleshooting) | 文档帮助用户自己解决共同的问题. |
| [文档使用文件](/core/quality-scale/docs-use-cases) | 文档显示您在整合过程中可以做些什么 。 |
| [动态设备](/core/quality-scale/dynamic-devices) | 泌入设置后出现的设备无需重新装入即可添加. |
| [实体类别](/core/quality-scale/entity-category) | 配置和诊断实体有一个实体类别。 |
| [实体设备类](/core/quality-scale/entity-device-class) | 实体在任何适合的地方都会使用设备类. |
| [实体因违约而伤残](/core/quality-scale/entity-disabled-by-default) | 很少用户需要的实体默认被禁用. |
| [实体翻译](/core/quality-scale/entity-translations) | 实体名称来自字符串.json,因此可以翻译. |
| [例外翻译](/core/quality-scale/exception-translations) | 向用户显示的错误来自字符串.json,因此可以翻译. |
| [图标翻译](/core/quality-scale/icon-translations) | 实体图标在图标.json中定义. |
| [重组流程](/core/quality-scale/reconfiguration-flow) | 用户可以更改一个条目的设置,而无需删除该内容册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册册 |
| [修理问题](/core/quality-scale/repair-issues) | 这种整合对用户能够解决的问题提出了修理问题。 |
| [固态设备](/core/quality-scale/stale-devices) | 已消失的装置被移除,或者可以被用户移除. |

## 铂 {#platinum}

技术优异:协同,高效,严格打字. 三则.

| 规则 | 它问的是什么 |
| ---- | ------------ |
| [关联依赖性](/core/quality-scale/async-dependency) | 集成图书馆使用Ayn consistentio. |
| [泻入网会话](/core/quality-scale/inject-websession) | 库接受袍 {H. |
| [严格打字](/core/quality-scale/strict-typing) | 集成被完全输入,并使用严格的神秘设置检查. |

## 核对清单 {#checklist}

当您要求新的等级时, 请将该等级及其下方每个等级的核对表复制到您 pull request 的描述中。 检查完成的每个规则,在豁免规则后面写"免",并链接每个规则的代码. 见[提高一体化水平](/core/quality-scale/raise-tier).

```markdown
## Bronze {#bronze-1}

- [ ] `action-setup`: Register actions in async_setup
- [ ] `appropriate-polling`: Poll at an appropriate interval
- [ ] `brands`: Provide brand assets
- [ ] `common-modules`: Put common patterns in common modules
- [ ] `config-flow`: Set up from the UI with a config flow
  - [ ] Uses `data_description` to give context to fields
  - [ ] Uses `ConfigEntry.data` and `ConfigEntry.options` correctly
- [ ] `config-flow-test-coverage`: Test the config flow fully
- [ ] `dependency-transparency`: Use transparent dependencies
- [ ] `docs-actions`: Document the actions
- [ ] `docs-conditions`: Document the conditions
- [ ] `docs-high-level-description`: Describe the brand, product, or service
- [ ] `docs-installation-instructions`: Document the installation
- [ ] `docs-removal-instructions`: Document how to remove the integration
- [ ] `docs-triggers`: Document the triggers
- [ ] `entity-event-setup`: Subscribe to events in the entity lifecycle
- [ ] `entity-unique-id`: Give entities a unique ID
- [ ] `has-entity-name`: Use has_entity_name
- [ ] `runtime-data`: Store runtime data in runtime_data
- [ ] `test-before-configure`: Test the connection in the config flow
- [ ] `test-before-setup`: Check the connection during setup
- [ ] `unique-config-entry`: Prevent duplicate config entries

## Silver {#silver-1}

- [ ] `action-exceptions`: Raise exceptions when actions fail
- [ ] `config-entry-unloading`: Support unloading the config entry
- [ ] `docs-configuration-parameters`: Document the options
- [ ] `docs-installation-parameters`: Document the setup parameters
- [ ] `entity-unavailable`: Mark entities unavailable when appropriate
- [ ] `integration-owner`: Have an integration owner
- [ ] `log-when-unavailable`: Log once when unavailable, and once when back
- [ ] `parallel-updates`: Set the number of parallel updates
- [ ] `reauthentication-flow`: Reauthenticate from the UI
- [ ] `test-coverage`: Test more than 95% of the code

## Gold {#gold-1}

- [ ] `devices`: Create devices
- [ ] `diagnostics`: Implement diagnostics
- [ ] `discovery`: Support discovery
- [ ] `discovery-update-info`: Update network information from discovery
- [ ] `docs-data-update`: Document how data is updated
- [ ] `docs-examples`: Document automation examples
- [ ] `docs-known-limitations`: Document known limitations
- [ ] `docs-supported-devices`: Document supported devices
- [ ] `docs-supported-functions`: Document supported functionality
- [ ] `docs-troubleshooting`: Document troubleshooting
- [ ] `docs-use-cases`: Document use cases
- [ ] `dynamic-devices`: Add new devices automatically
- [ ] `entity-category`: Assign entity categories
- [ ] `entity-device-class`: Use device classes
- [ ] `entity-disabled-by-default`: Disable noisy or less popular entities
- [ ] `entity-translations`: Translate entity names
- [ ] `exception-translations`: Translate exception messages
- [ ] `icon-translations`: Use icon translations
- [ ] `reconfiguration-flow`: Reconfigure from the UI
- [ ] `repair-issues`: Raise repair issues when the user needs to act
- [ ] `stale-devices`: Remove stale devices

## Platinum {#platinum-1}

- [ ] `async-dependency`: Use an async dependency
- [ ] `inject-websession`: Pass in the web session
- [ ] `strict-typing`: Use strict typing
```
