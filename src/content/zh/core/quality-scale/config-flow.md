---
title: 从用户界面设置一个配置流
description: 青铜规则配置-流:集成由UI设置,有明确的配置流将其数据存储在正确的位置.
sidebarLabel: 配置流量
sidebarGroup: 铜
order: 5
---

# 从用户界面设置一个配置流 {#set-up-from-the-ui-with-a-config-flow}

此是铜法. 在`quality_scale.yaml`中,它被称为`config-flow`.

此页面是关于规则要求的, 以及如何检查 。 如何构建一个配置流,一步步地,在建设集成中在[配置流量](/core/integrations/config-flow)上.

整合必须从UI中设置,并带有[配置流量](/glossary/config-flow). 流量必须是容易理解的:每个字段的右 [选择器](/glossary/selector),在需要的地方验证,和`strings.json`中解释每个字段的 `data_description` 。 存储 `ConfigEntry.data` 中连接所需的内容, 以及 `ConfigEntry.options` 中不需要连接的设置 。

## 为什么这很重要 {#why-it-matters}

2018年起,配置流成为设置集成的标准方式. 它给每一个集成都提供了相同的设置经验,引导用户通过步骤,意味着没有人需要编辑YAML才能启动. 配置流是用户首先看到的您整合的事物,因此应该清晰而友好.

将连接数据和选项分开,让用户稍后在选项流中更改选项,而不触及连接.

## 示例 {#example}

在 `manifest.json` 中将 `config_flow` 设定为 `true`, 并添加 `config_flow.py` , 并加一个扩展 `ConfigFlow` 的类 。 [配置流量](/core/integrations/config-flow#add-a-config-flow) 显示一个完整的示例, [教程](/core/integrations/tutorial#4-build-the-config-flow) 从脚手架上建一个 。

表格的文本存在于 `strings.json` 。 在 `data` 和 `data_description` 中给出每个字段的标签和解释 :

```json
{
  "config": {
    "step": {
      "user": {
        "data": {
          "host": "[%key:common::config_flow::data::host%]"
        },
        "data_description": {
          "host": "The hostname or IP address of your device."
        }
      }
    }
  }
}
```

真正的配置流也测试连接,防止重复. 这是他们自己的规则:[提交的文件 你还好吗?](/core/quality-scale/test-before-configure)和[唯一配置输入](/core/quality-scale/unique-config-entry)。

## 如何检查 {#how-it-is-checked}

- Hassfest, 当规则是 `done` 时 : `config_flow` 必须是 `true` 在 `manifest.json` 中, `config_flow.py` 必须存在 。
- Pylint)在配置流要求姓名(`home-assistant-config-flow-name-field`)或投票间隔(`home-assistant-config-flow-polling-field`)时发出警告. 名称来自该设备,投票间隔则取决于整合.
- 当一个配置、选项或子条目流的字段在 `strings.json` (`home-assistant-config-flow-field-not-translated`) 及其兄弟姐妹中没有翻译时, Pylint 警告 。
- 选择器的用法, `data_description` 和`data` 相对于 `options` , 都在审查中检查 。

## 例外 {#exceptions}

[ADR-0010 (英语).](https://github.com/home-assistant/architecture/blob/master/adr/0010-integration-configuration.md)豁免UI设置的集成,不受此规则的约束.

## 相关规则 {#related-rules}

- [提交的文件 你还好吗?](/core/quality-scale/test-before-configure):测试配置流中的连接.
- [唯一配置输入](/core/quality-scale/unique-config-entry) : 防止重复配置条目 。
- {L刚好} : 完全测试配置流 。
- [发现](/core/quality-scale/discovery):支持发现.
- [重新校正流量](/core/quality-scale/reauthentication-flow):从UI中重新认证.
- [重组流程](/core/quality-scale/reconfiguration-flow):从UI重新配置.
