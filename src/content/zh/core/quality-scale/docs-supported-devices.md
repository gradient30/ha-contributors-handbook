---
title: 文档支持设备
description: 安全理事会呗。
sidebarLabel: 文档辅助设备
sidebarGroup: 黄金
order: 8
---

# 文档支持设备 {#document-supported-devices}

这是黄金规则 在`quality_scale.yaml`中,它被称为`docs-supported-devices`.

[Home Assistant.io](https://www.home-assistant.io/)上的集成页面列出已知能工作的设备,以及已知不能工作的设备. 当一个模型列表不实用时,描述组,如"每个运行固件2.0或更新的设备".

## 为什么这很重要 {#why-it-matters}

许多人购买设备是因为Home Assistant支持它们. 如果文档 Madison没有说明哪种型号可行,则在购买后发现,何时设置失败. 一个明确的列表可以防止这种情况发生,它可以将你从一个从未支持过的设备的人身上节省下来.

## 示例 {#example}

```markdown
## Supported devices {#supported-devices}

These devices are known to work with the integration:

- My Thermostat 2 and 3
- My Hub, with firmware 4.1 or newer
- Every device that runs MyOS

## Unsupported devices {#unsupported-devices}

These devices do not work with the integration:

- My Thermostat 1: it has no local API
- Devices made before 2015
```

参见 [写入集成文件](/writing/guides/integration) 和 [整合页面结构](/writing/reference/integration-page) 。

## 如何检查 {#how-it-is-checked}

在审查中检查过,通常在文件pull request上.

## 例外 {#exceptions}

如果集成没有连接到一个设备或服务,或者没有集成物理设备,则该规则不适用.
