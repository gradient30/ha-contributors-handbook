---
title: 数据模型
description: 事件、状态、上下文和动作，是 Home Assistant 记录的一切的构建块。
order: 2
---


# 数据模型 {#the-data-model}
Home Assistant 做了很多事情，但其底层是建立在一个小而简单的数据模型上：事件、状态和上下文。一旦你了解了这些，数据库中的数据就变得有意义了。

## 事件 {#events}
Home Assistant 是事件驱动的。发生的一切都是事件：灯亮了、运动传感器检测到运动、自动化被触发。每个事件都有一个类型、一部分数据、一个时间和一个上下文。

你会经常看到的一些内置事件：| 事件类型 | 触发时间 | 数据 |
| --- | --- | --- |
| `state_changed` | 实体的状态发生变化时触发。 | `entity_id`、`old_state` 和 `new_state`。当 `old_state` 缺失时，该实体是新的。当 `new_state` 缺失时，该实体已被移除。 |
| `call_service` | 执行某个动作时触发，例如 `light.turn_on`。 | `domain`、动作作为 `service` 以及其数据作为 `service_data`。 |
| `automation_triggered` | 自动化被触发时。 | 自动化的 `name` 和 `entity_id`。 |
| `script_started` | 脚本开始运行时。 | 脚本的 `name` 和 `entity_id`。 |
| `service_registered` | 集成注册新动作时。 | `domain`，以及动作作为 `service`。 |
| `homeassistant_start` 和 `homeassistant_stop` | Home Assistant 开始和停止时。 | 无。 |

事件名称和字段仍然使用旧的“service”一词，而它现在被称为 [action](/glossary/action)。不要依赖 `homeassistant_stop` 来查找 Home Assistant 何时停止：如果没有干净关闭，该事件永远不会触发。`recorder_runs` 表更可靠。请参见 [数据库模式](/data/reference/database-schema#recorder-runs)。

## 状态 {#states}
每个 [实体](/glossary/entity) 都有一个 [状态](/glossary/state)。状态包括：

- 实体 ID，格式为 `<domain>.<object_id>`，例如 `light.kitchen`。域名告诉你它是什么类型的实体，以及可以预期哪些属性。
- 状态本身，例如 `on` 或 `21.5`。
- 进一步描述它的属性，例如灯光的亮度和颜色。
- 时间戳：`last_changed`、`last_updated` 和 `last_reported`。

三个时间戳的意义不同：

- `last_changed` 仅在状态值变化时改变。灯光开关会改变它，但灯光颜色变化不会。
- `last_updated` 在状态值或任何属性变化时改变。灯光开关、灯光颜色变化都能改变它。
- `last_reported` 每次集成报告状态时都改变，即使没有任何变化也会改变。使用`last_changed`，你可以判断灯亮了多久。使用`last_updated`，你可以判断它保持当前颜色多久。

## 上下文 {#context}
上下文将事件和状态连接在一起。每当某事引发变化时，例如 UI 中的人、自动化或设备，就会创建一个新的上下文。随后发生的每个事件和状态变化都带有该上下文。因此，你总是可以追溯变化的来源。

上下文有三个字段：

| 字段 | 含义 |
| --- | --- |
| `id` | 上下文的唯一 ID。 |
| `user_id` | 启动更改的用户，如果 Home Assistant 知道的话。大多数情况下在更改来自 UI 时填写。 |
| `parent_id` | 导致此上下文的上下文。即使触发器已有上下文，自动化也会创建自己的上下文，并在此指向触发器的上下文。这保持了自动化操作与触发它的用户权限的分离。 |

例如，当 Paulus 回家时：1. `device_tracker.paulus_phone` 从 `not_home` 变为 `home`。
2. 自动化“Paulus 回家”被触发，并用一个新的上下文触发 `automation_triggered`，其父级上下文为步骤 1 的上下文。
3. 自动化执行 `light.turn_on`，触发 `call_service`，上下文为步骤 2 的上下文。
4. `light.living_room` 打开，其新状态也继承步骤 2 的上下文。

日志簿使用此方法显示导致更改的原因。并非每个触发器都会创建上下文，并且在自动化或模板中没有内置方法来查找上下文的原始原因。

## 操作 {#actions}
集成提供操作，例如 `light.turn_on` 或 `notify.send_message`。操作由其域和名称标识，并接受指示要执行内容的数据，例如要打开哪个灯。

操作不会单独存储在表中。你可以从 `service_registered` 事件中找到存在的操作，从 `call_service` 事件中找到已执行的操作。

## 存储位置 {#where-it-is-stored}
[记录器](/glossary/recorder) 将事件和状态写入数据库。[数据库架构](/data/reference/database-schema) 解释了各个表，[统计](/data/reference/statistics) 解释了 Home Assistant 为长期存储维护的汇总。
