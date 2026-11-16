---
title: 设置并行更新的数目
description: 厮守银规则并行更新:每个实体平台设置PARALEL UPDATES.
sidebarLabel: 并行更新
sidebarGroup: 银
order: 8
---

# 设置并行更新的数目 {#set-the-number-of-parallel-updates}

这是Silver的规则 在`quality_scale.yaml`中,它被称为`parallel-updates`.

整合的每个 [平台](/glossary/platform) 模块, 如 `sensor.py` 或 `light.py` , 必须明确设置 `PARALLEL_UPDATES` 。 Home Assistant同时运行的是该平台的实体更新和实体行动的最大数量。 `0`表示没有限制。

## 为什么这很重要 {#why-it-matters}

一些设备和服务无法同时处理许多请求. 一个有十个实体的小设备,当同时所有十个更新时,或者当一个场景一次打开它的十个开关时,可以窒息. `PARALLEL_UPDATES` 让我们Home Assistant 排队吧 。

明确地设定它也意味着有人在考虑它。 正确的值取决于设备,只有整合才知道.

## 示例 {#example}

为每个实体向设备说话的平台一次发出一个请求:

```python
PARALLEL_UPDATES = 1

class MySwitch(SwitchEntity):
    """A switch on the device."""
```

使用 [协调员](/glossary/coordinator) , 数据已经在一处获取, 因此实体更新不需要限制 。 在像`sensor`或`binary_sensor`这样的只读平台上,设置为`0`:

```python
# The coordinator fetches the data, so updates need no limit {#the-coordinator-fetches-the-data-so-updates-need-no-limit}
PARALLEL_UPDATES = 0
```

不过,协调员并不限制行动。 在有动作的平台上,如`switch`或`light`,考虑一下设备一次接受多少命令,并设定匹配值.

## 如何检查 {#how-it-is-checked}

- Pylint,当规则是`done`时:每个平台模块必须定义一个模块级`PARALLEL_UPDATES`(`home-assistant-missing-parallel-updates`).
- 怯场值是否与设备相符 。

## 例外 {#exceptions}

更积极地说,如果合并没有实体平台,则不适用这一规则。

## 相关规则 {#related-rules}

- [适当定价](/core/quality-scale/appropriate-polling):在适当的间隔时间进行民调.
