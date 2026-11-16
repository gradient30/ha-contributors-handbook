---
title: 文档支持的功能
description: Gold 规则文件支持的函数:文档描述了它所提供的实体和功能.
sidebarLabel: 文档辅助功能
sidebarGroup: 黄金
order: 9
---

# 文档支持的功能 {#document-supported-functionality}

这是黄金规则 在`quality_scale.yaml`中,它被称为`docs-supported-functions`.

[Home Assistant.io](https://www.home-assistant.io/)上的集成页面描述了集成提供的内容:其每个平台的实体,每个平台做什么,以及在哪些设备上可以使用. 按实体类型排序列表,或者当集成支持非常不同的设备时,按设备排序列表.

## 为什么这很重要 {#why-it-matters}

用户在购买设备前想知道得到什么. 如果有人寻找冰箱,他们可以监视,在购买后发现整合只报告门是否开着,而不是温度时会失望. 一份明确的实体清单确定了正确的期望。

该列表还帮助已经understanded设备的用户找到他们正在寻找的实体,并理解它的含义.

## 示例 {#example}

按实体类型排序 :

```markdown
## Supported functionality {#supported-functionality}

### Buttons {#buttons}

- **Start backflush**
  - **Description**: Starts the backflush of the machine. Turn the
    paddle within 15 seconds after you press it.
  - **Available for machines**: all

### Sensors {#sensors}

- **Coffee temperature**
  - **Description**: Current temperature of the coffee boiler.
  - **Available for machines**: all
- **Steam temperature**
  - **Description**: Current temperature of the steam boiler.
  - **Available for machines**: Micra, GS3
  - **Remarks**: Disabled by default.
```

按设备排序 :

```markdown
## Supported functionality {#supported-functionality-1}

### Air purifier {#air-purifier}

#### Sensors {#sensors-1}

- **Filter life remaining**: The remaining life of the filter, in days.
- **Purified volume**: The volume of air the purifier cleaned, in cubic
  meters. Disabled by default.

#### Numbers {#numbers}

- **Favorite level**: The fan level of the favorite mode, from 0 to 10.
```

参见 [写入集成文件](/writing/guides/integration) 和 [整合页面结构](/writing/reference/integration-page) 。

## 如何检查 {#how-it-is-checked}

在审查中检查过,通常在文件pull request上.

## 例外 {#exceptions}

这一规则没有例外。
