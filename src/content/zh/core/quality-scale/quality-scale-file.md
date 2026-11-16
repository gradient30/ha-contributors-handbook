---
title: 质量尺度文件
description: 质量 尺度的格式. 查查那些能让整合者 诚实了解规则的检查
sidebarLabel: 质量缩放文件
order: -2
---

# 质量尺度文件 {#the-quality-scale-file}

每个分级的集成都会在它的`manifest.json`旁边保存一个`quality_scale.yaml`文件. 文件列出尺度的每个规则,并附有其状态. 这是关于一体化的进展报告:做了哪些工作,仍需做什么,哪些规则不适用,为什么。

## 格式 {#the-format}

文件有一个密钥, `rules`, 下方每个标尺规则 。 一条规则要么是一个普通状态,要么是一个`status`和一个`comment`的映射:

```yaml
rules:
  

# Bronze {#exemptions}
  action-setup:
    status: exempt
    comment: This integration does not provide actions.
  appropriate-polling: done
  brands: done
  config-flow: done
  test-before-setup:
    status: todo
    comment: Setup does not catch authentication errors yet.
```

有三种状态 Natalie:

- `done`:整合遵循规则.
- `todo`:现在还没有。 评论是可选的,是解释缺失内容的好地方.
- 72. `exempt`:规则不适用。  72. 需要一个`comment`,它必须说明原因。

使用规则名称与规则页上出现的完全相同,带有破折号,如`config-flow-test-coverage`. 文件必须列出比例尺的 Every  规则, 以及当前等级之上的等级规则 。 Hassfest 拒绝一个缺少或未知规则的文件.

最容易开始的方法是脚手架脚本为新集成而创建的模板: 每条规则,设置为`todo`,按层次分组. 您可以在 [`script/scaffold/templates/integration/integration/quality_scale.yaml`](https://github.com/home-assistant/core/blob/dev/script/scaffold/templates/integration/integration/quality_scale.yaml) 中找到它, 或者运行 `python3 -m script.scaffold integration` 以创建新的整合 。

### 豁免 {#what-hassfest-checks}

豁免是像`done`一样的要求。 每个规则页都有"例外"一节,列出规则不适用时的情况. 坚持这些。 如果您认为某条规则不适用于您的整合有其他原因,请在注释和pull request中解释,并期望评论者询问.

好评具体:"设备没有认证"比"不适用"好.

## 何等难堪的支票 {#what-pylint-checks}

[狂欢](/core/development/checks) 在 CI 运行在每 pull request , 您可以用 `python3 -m script.hassfest` 在本地运行 。 对于质量尺度,它检查:

- 核心的整合具有`quality_scale.yaml`。 新的集成必须到达青铜器,所以在文件缺失时会发生散乱失败. 在[`script/hassfest/quality_scale.py`](https://github.com/home-assistant/core/blob/dev/script/hassfest/quality_scale.py)中列出的不是旧的整合,而该列表只会缩短.
- 文件 gains 符合上面的格式, 符合每个规则和有效状态 。
- `manifest.json` 中的每个规则, 以及下面的每个规则, 是`done` 或`exempt` 。 如果不是的话, 狂欢会列出缺漏的规则。
- Silver和更高层次的集成在`manifest.json`中至少有一个集成所有者。
- 这种蜥蜴的虚拟集成以及被列为没有规模的内部集成没有文件。

此外,当代码被标记 `done` 时, 需要验证代码中的一些规则 :

| 规则 | {\fn黑体\fs22\bord1\shad0\3aHBE\4aH00\fscx67\fscy66\2cHFFFFFF\3cH808080}看什么? |
| ---- | ----------------------- |
| [配置流量](/core/quality-scale/config-flow) | 在清单中,和一个`config_flow.py` |
| [发现](/core/quality-scale/discovery) | 清单中的发现密钥或配置流中的发现步骤 |
| [重组流程](/core/quality-scale/reconfiguration-flow) | 配置流中的 `async_step_reconfigure` |
| [运行时间数据](/core/quality-scale/runtime-data) | `async_setup_entry` 指定 `entry.runtime_data` 。 当 `strict-typing` 也是 `done` 时, 条目函数也会使用一个输入的配置项, 如 `MyConfigEntry` |
| [严格打字](/core/quality-scale/strict-typing) | 集成在 `.strict-typing` 中, 其要求被输入 |
| [设置前测试](/core/quality-scale/test-before-setup) | 集成的模块将 `ConfigEntryNotReady`, `ConfigEntryAuthFailed` 或 `ConfigEntryError`, 或 `async_setup_entry` 等 `async_config_entry_first_refresh` 或 `async_ensure_token_valid` 提升它们。 |
| [唯一配置输入](/core/quality-scale/unique-config-entry) | `single_config_entry: true` 在列表中,或称为`_async_abort_entries_match`的配置流,或两者兼有`async_set_unique_id`和`_abort_if_unique_id_configured` |

当这样的检查失败时, 错误将规则命名在括号中, 如 `[runtime-data]` , 并链接到它的文档 。

## 什么样的平板检查 {#what-review-checks}

Core在 [核心存储器](https://github.com/home-assistant/core) 的 [`packages/pylint-home-assistant/`](https://github.com/home-assistant/core/tree/dev/packages/pylint-home-assistant) 中有自己的 pylint 插件 。 它的一些检查只用于标定规则为`done`的集成. 也当其他人后来更改代码时:

| 规则 | 检查 |
| ---- | ----- |
| [配置- 输入- 卸载](/core/quality-scale/config-entry-unloading) | `home-assistant-missing-config-entry-unloading` |
| [诊断](/core/quality-scale/diagnostics) | `home-assistant-missing-diagnostics` |
| [实体- 唯一](/core/quality-scale/entity-unique-id) | `home-assistant-missing-entity-unique-id`, `home-assistant-entity-unique-id-static` |
| [例外翻译](/core/quality-scale/exception-translations) | `home-assistant-exception-not-translated` |
| [有实体名称](/core/quality-scale/has-entity-name) | `home-assistant-missing-has-entity-name` |
| [并行更新](/core/quality-scale/parallel-updates) | `home-assistant-missing-parallel-updates` |
| [重新校正流量](/core/quality-scale/reauthentication-flow) | `home-assistant-missing-reauthentication-flow` |
| [提交的文件 你还好吗?](/core/quality-scale/test-before-configure) | `home-assistant-missing-test-before-configure` |

对插件的其他检查会运行每个集成,其中许多也会执行规则,比如`home-assistant-use-runtime-data`或`home-assistant-service-registered-in-setup-entry`. 规则页将它们列在"如何检查"下. [pylint 插件读取](https://github.com/home-assistant/core/blob/dev/packages/pylint-home-assistant/README.md) 描述每张支票 。

## 什么审查检查 {#什么审查检查}

大多数规则无法用工具检查 。 投票间隔合适吗? 文件是否解释了使用案例? 一个人决定的

- 一个自动审查器运行在 pull request 上, 以 `quality_scale.yaml` 触摸集成 。 它对照规则检查修改后的整合标记为`done`或`exempt`,并在打破规则的线条上留下评论评论 我还是会这样. 把它像其他评论一样对待:它可能是错误的,但它通常有一点.
- 审阅者检查工具无法达到的规则. 当你要求一个新的层次, 他们通过每一个规则。 见[提高一体化水平](/core/quality-scale/raise-tier).
