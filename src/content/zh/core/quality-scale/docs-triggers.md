---
title: 记录触发器
description: 青铜规则docs-triggers:文档描述了集成的触发器.
sidebarLabel: 文件触发
sidebarGroup: 铜
order: 13
---

# 记录触发器 {#document-the-triggers}

此是铜法. 在`quality_scale.yaml`中,它被称为`docs-triggers`.

当集成提供了自己的[触发](/glossary/trigger)时,每个触发器都必须被记录. 每个触发器在 [Home Assistant.io](https://www.home-assistant.io/) 上获得自己的页面, 集成页面链接到它们 。 一个触发页解释触发的作用,列出其选项,并显示如何从UI和YAML中使用.

## 为什么这很重要 {#why-it-matters}

融合触发器比标准触发器更不熟悉,如状态变化. 没有文件,用户不知道它们的存在,选项的含义,或触发点火时. 每个触发器的页面保持集成页面的可读性,并给每个触发器提供实例空间.

## 示例 {#example}

每个触发器是家用助手.io的[`source/_triggers/`](https://github.com/home-assistant/home-assistant.io/tree/current/source/_triggers)文件,以触发器命名,类似`my_integration.co2_changed.markdown`. 一个简短的例子:

```markdown
---
title: "Carbon dioxide level changed"
trigger: my_integration.co2_changed
domain: my_integration
description: "Triggers after the carbon dioxide level changes."
---

The **Carbon dioxide level changed** trigger fires after the CO2 reading
of one or more sensors changes by a meaningful amount. Use it to turn on
ventilation when a room gets stuffy.

{% include triggers/ui_header.md %}

1. Go to **Settings** > **Automations & scenes**.
2. Open an automation, and in the **When** section, select **Add trigger**.
3. Pick the area or sensor, then select **Carbon dioxide level changed**.

{% include triggers/yaml_header.md %}

{% example %}
trigger: |
  trigger: my_integration.co2_changed
  target:
    entity_id: sensor.bedroom_co2
  options:
    threshold: 50
{% endexample %}
```

在整合页面上,`{% include integrations/triggers.md %}`列出了整合的触发器. [整合页面结构](/writing/reference/integration-page#triggers-conditions-and-actions) 描述一个触发页面的全部布局, 并包含全部内容 。 另见[写入集成文件](/writing/guides/integration)。

## 如何检查 {#how-it-is-checked}

已检阅. Hassfest 验证了 `triggers.yaml` 中的触发描述, 但不验证文档 。

## 例外 {#exceptions}

如果合并不提供任何触发因素,则不适用这一规则。

## 相关规则 {#related-rules}

- [文件行动](/core/quality-scale/docs-actions): 记录动作 。
- [文件条件](/core/quality-scale/docs-conditions): 记录条件。
