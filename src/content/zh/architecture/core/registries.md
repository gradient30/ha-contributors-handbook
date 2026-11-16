---
title: 注册表和存储
description: Home Assistant 保存它所知道的关于实体、设备和区域的信息，用户的更改如何与集成报告的数据分开保存，以及数据的存储方式。
order: 10
---


# 注册表和存储 {#registries-and-storage}
[状态机](/core/internals/states) 知道当前什么是真实的，并在重启时忘记它。[注册表](/glossary/registry) 记住其余的内容：哪些实体和设备存在，它们在哪里，它们的名称是什么，以及用户对它们做了哪些更改。

本页是概览。集成如何与每个注册表协作，请参见下面链接的核心和集成部分。

## 简而言之 {#in-short}
- 有一个用于实体、设备、区域、楼层、标签和类别的注册表，以及一个显示在“维修”下的问题注册表。
- 集成通过其实体的唯一 ID 和提供的设备信息填充它们。
- 用户在 UI 中更改它们：名称、区域、图标。这些更改会与集成报告的信息一起保存，并且优先。
- 注册表、配置条目以及大多数其他数据存储在 `.storage` 文件夹中的 JSON 文件中。

## 两个来源，一个结果 {#two-sources-one-result}
取一个实体。集成显示它被称为“Temperature”，并且它是一个温度传感器。用户将其重命名为“Outside”，并将其放置在花园区域。两者都会保留，在不同的字段中：

| 来自集成的字段 | 来自用户的字段 |
| --- | --- |
| `original_name` | `name` |
| `original_icon` | `icon` |
| `original_device_class` | `device_class` |

当实体写入其状态时，如果用户设置了值，则用户的值优先。集成可以随时更新自己的字段，而不会覆盖用户的选择。这就是[用户的选择优先](/architecture/principles#the-users-choices-win)的原则。

## 注册表 {#the-registries}
| 注册表 | 内容 | 详细信息 |
| --- | --- | --- |
| 实体 | 每个具有[唯一 ID](/glossary/unique-id)的实体，以及用户对其所做的更改 | [实体注册表](/core/entities/registry)，供实体作者使用，以及[实体注册表](/core/integrations/entity-registry)，用于查询和迁移条目 |
| 设备 | 每个设备，从集成实体的设备信息获取 | [设备注册表](/core/integrations/device-registry) |
| 区域和楼层 | 用户如何描述他们的家 | [区域注册表](/core/integrations/area-registry) |
| 标签和分类 | 用户如何分组事物，以及如何对自动化和脚本进行排序 | 下面链接的代码 |
| 问题 | 用户需要处理的内容，显示在**设置** > **修复**下 | [修复](/core/integrations/repairs) |

没有唯一 ID 的实体仍然可以工作，但用户不能在 UI 中更改它们的任何内容。注册表遵循配置条目、设备和实体的层级结构。禁用一个配置条目，其关联的设备和实体也会被禁用。禁用一个设备，其关联的实体也会随之禁用。删除一个设备或配置条目，其所属的实体也会从注册表中移除。

注册表中启用的实体，如果当前没有任何集成提供，例如当其集成设置失败时，仍会显示在状态机中：作为`unavailable`，具有属性`restored: true`。

## 存储 {#storage}
Home Assistant 将其自身的数据存储在 `.storage` 的 JSON 文件中，在配置文件夹中：注册表、配置条目、用户、仪表板等。集成可以使用 `Store` 做同样的事情，它会版本化数据，在版本更改时进行迁移，将紧密的写入合并为一个，并且默认情况下拒绝读取比其已知版本更新的主版本数据，就像降级之后那样。

`.storage` 中的文件是内部文件。它们在不同版本之间会改变，用户不应该手动编辑它们。`configuration.yaml` 是配置存放的另一个地方。它由用户编写，Home Assistant 只会读取它。

## 在代码中 {#in-the-code}
| 什么 | 哪里 |
| --- | --- |
| 实体注册表 | [`homeassistant/helpers/entity_registry.py`](https://github.com/home-assistant/core/blob/dev/homeassistant/helpers/entity_registry.py) |
| 设备注册表, `DeviceInfo` | [`homeassistant/helpers/device_registry.py`](https://github.com/home-assistant/core/blob/dev/homeassistant/helpers/device_registry.py) |
| 区域、楼层、标签和类别注册表 | `area_registry.py`, `floor_registry.py`, `label_registry.py`, `category_registry.py` 在 [`homeassistant/helpers/`](https://github.com/home-assistant/core/tree/dev/homeassistant/helpers) |
| 问题注册表 | [`homeassistant/helpers/issue_registry.py`](https://github.com/home-assistant/core/blob/dev/homeassistant/helpers/issue_registry.py) |
| `Store` | [`homeassistant/helpers/storage.py`](https://github.com/home-assistant/core/blob/dev/homeassistant/helpers/storage.py) |

## 处理这个 {#work-on-this}
- Core 新手？从 [你对 Core 的第一次贡献](/core/first-contribution) 开始。
- 给你的实体一个唯一的 ID 和一个设备：质量等级的 [实体唯一 ID](/core/quality-scale/entity-unique-id) 和 [设备](/core/quality-scale/devices) 规则。
