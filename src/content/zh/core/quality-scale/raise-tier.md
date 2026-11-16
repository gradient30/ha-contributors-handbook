---
title: 提高一体化水平
description: 努力提高质量水平 一次一个规则, 并获得审查 和发布新的层次。
sidebarLabel: 提高等级
order: -3
---

# 提高一体化水平 {#raise-the-tier-of-an-integration}

提升集成度是核心中最有用的事情之一。 这让每一个使用它的人的整合都更好,你们在路上学到了很多Home Assistant. 也正是工作好分:一条规则往往是一个小的pull request.

## 在你开始之前 {#before-you-start}

- 检查谁拥有整合。 `codeowners`在它的`manifest.json`是人们说话。 在一个问题或在[Discord](https://www.home-assistant.io/join-chat/)上提到它们,然后你开始一个大的变化,所以你不会与正在进行的工作相冲突。
- 读其`quality_scale.yaml`. 它告诉你哪些规则是执行的,哪些是`todo`,哪些是豁免的.
- 还没有`quality_scale.yaml`吗? 然后整合在青铜器下方,或早于文件. 从添加文件开始,每个规则都有诚实状态. 在核心复制 [`script/scaffold/templates/integration/integration/quality_scale.yaml`](https://github.com/home-assistant/core/blob/dev/script/scaffold/templates/integration/integration/quality_scale.yaml) 的模板 。

## 向上前进 {#work-your-way-up}

1. 选择一个尚未完成的最低等级的在随后的 `todo`只是个规则 。 青铜器规则在银器规则之前,因为一层需要下面的所有规则.
2. 读规则页. 它解释了规则的要求,"例外"部分告诉你,如果它可能不适用.
3. 执行规则,并进行测试。 将pull request保存在一条规则上,你可以。 小的 pull request 得到更快的审查。
4. 在同一 pull request 中, 在 `quality_scale.yaml` 中将规则设置为 `done` 。 或者设定为`exempt`,如果它不适用的话,附带注释.
5. 跑步狂欢 和测试整合之前你推。 见[自己去检查一下](/core/quality-scale/raise-tier#check-it-yourself).

重复到等级规则为 `done` 或 `exempt` 。 您不需要等待一个层次的修改来按照规则合并规则 : 每个 pull request 让集成更好, 文件会显示进度 。

> [!TIP]
> 有些规则取决于其他规则。 [动态设备](/core/quality-scale/dynamic-devices)和[固态设备](/core/quality-scale/stale-devices)需要[设备](/core/quality-scale/devices),[重新校正流量](/core/quality-scale/reauthentication-flow)需要[设置前测试](/core/quality-scale/test-before-setup)来提高`ConfigEntryAuthFailed`,黄金翻译规则建立在[有实体名称](/core/quality-scale/has-entity-name)上. 每个规则页底部的"相关规则"指出了这些链接.

## 你自己去检查一下 {#check-it-yourself}

阅读代码不足以知道某项规则得到满足. 许多规则都有CI执行的阈值或验证符,因此运行工具并读取其结果. 以下步骤遵循 `ha-quality-scale-verify` 在 [核心存储器](https://github.com/home-assistant/core) ([`.claude/skills/ha-quality-scale-verify/SKILL.md`](https://github.com/home-assistant/core/blob/dev/.claude/skills/ha-quality-scale-verify/SKILL.md) ) 中的技能, 它描述规则是如何被验证的 。

使用您的变位符 : `ruff` 从 `requirements_test_pre_commit.txt` , `syrupy` 从 `requirements_test.txt` , 和 库 从 `manifest.json` 。 不同的版本会给假通行证和假故障.

### 狂欢 {#hassfest}

验证一个集成方式:

```shell
python3 -m script.hassfest --integration-path homeassistant/components/example
```

此检查 `quality_scale.yaml` , 以及具有验证符的规则, 如 `config-flow`, `runtime-data`, `test-before-setup`, `unique-config-entry`, `discovery`, `reconfiguration-flow` 和`strict-typing` 。 有两件事要知道:

- 验证器只运行一个标记为 `done` 的规则 。 干净的跑步对`todo`或`exempt`的规则没有任何意义:你自己检查一下。
- `--integration-path` 只运行检查一个集成的插件 。 整个寄存器的检查被跳过,比如`mypy_config`,以及只运行在全`python3 -m script.hassfest`上的品牌元数据的检查.

### 严格打字 {#strict-typing}

对于 [严格打字](/core/quality-scale/strict-typing),整合必须在 `.strict-typing` 中列出,或者 mypy 运行时没有严格的设置,并且由于错误的原因通过. 在集成上运行 mypy, 请检查 `mypy.ini` 在同步中, 而不重生成它 :

```shell
python3 -m script.hassfest -p mypy_config --action validate
```

没有 `--action validate` , 将文件重新生成, 并隐藏它已经过时 。

### 测试覆盖率 {#test-coverage}

在测量覆盖度之前重现英文翻译。 测试读取生成的 `translations/en.json` 而不是 {H1凿} :

```shell
python3 -m script.translations develop --integration example
pytest tests/components/example \
  --cov=homeassistant.components.example \
  --cov-report term-missing
```

对[试验覆盖](/core/quality-scale/test-coverage)来说,每个模块必须高于95%,而不是平均整合. 看确切数字:四舍五入的95%可以是94.7%.

### 配置流量测试 {#config-flow-tests}

对于[配置- 流量- 测试- 覆盖](/core/quality-scale/config-flow-test-coverage),`config_flow.py`百分之百的线路覆盖范围单靠自己是不够的. 核查技能也用于:

- 通过错误测试到右端结果的每个流量:为用户创建的条目(`CREATE_ENTRY`),发现,和导入流量,以及用`reauth_successful`或`reconfigure_successful`进行重校正和重组的中止.
- 拒绝重复的测试: 第二次设置同一设备或账户必须在中止时结束, 如 `already_configured` 或 `single_instance_allowed` 。
- 选项流, 也生活在 `config_flow.py` 中 。

### 什么工具不检查 {#what-tools-do-not-check}

- **品牌**:繁忙不检查图标和标志. 他们住在 [品牌存储器](https://github.com/home-assistant/brands) 中: 检查他们在那里, 或者在你的 pull request 到它。
- ** 文档规则**:检查在[Home Assistant.io](https://www.home-assistant.io/)的集成页上或随您更改的文档pull request中是否有章节。

## 询问新等级 {#ask-for-the-new-tier}

当下一级规则为 `done` 或 `exempt` 时, 打开 pull request 在 `manifest.json` 中更改 `quality_scale` 。

1. 更改等级, 例如从 `"bronze"` 改为 `"silver"` 。
2. 在 pull request 的描述中, 加入 [所有规则](/core/quality-scale/rules#checklist) 对新级别及其下方的每个级别 的核对表 。 检查所有规则, 并标注豁免者为豁免 。
3. 对于每个规则,链接到执行规则的代码,或者解释豁免. 这使得审查迅速:审查者不必搜索.

Hassfest 失败了 pull request 当一个阶梯规则不是 `done` 或 `exempt` 时, 所以您很早就知道 。

### 审查 {#the-review}

复议员通过核对表,按规则检查工具无法检查的部分. 期待问题,特别是关于豁免的问题。 一旦一个核心团队的成员批准并合并了pull request,新一级舰只与下一个主要释放.

你把文档不需要单独的 pull request 。 你把Home Assistant的整合页上的级别。 io从发布时的货单上更新.

## 保持等级 {#keep-the-tier}

在到达一级后需要护理。 当您更改集成时, 请保留其规则: 测试新代码, 翻译新字符串, 以及当某事发生变化时更新的 `quality_scale.yaml` 。 数个pylint检查札和自动审查员比较pull requests与规则的整合要求,所以一个打破规则的更改通常很早就被抓住. 检查的内容见[质量尺度文件](/core/quality-scale/quality-scale-file)。

融合也可能失去层次,例如当它失去了最后的主动融合所有者时。 见[一层可以下](/core/quality-scale/tiers#a-tier-can-go-down).
