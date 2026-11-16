---
title: 编写并分享蓝图
description: 编写一个具有良好输入和选择器的蓝图，对其进行测试，在不破坏他人构建内容的情况下进行更改，并分享它。
sidebarLabel: 蓝图
order: 5
---

# 编写并分享蓝图 {#write-and-share-a-blueprint}

一个 [蓝图](/glossary/blueprint) 是一种自动化、脚本或模板实体，其中有用户需要填写的空白。一个蓝图可以多次使用：可以用于走廊，也可以用于浴室，每个都可以有自己的设备和设置。

蓝图不在市场中。用户通过 URL 导入蓝图，而 Home Assistant 会记住该 URL 以便获取新版本。[工作原理](/marketplace/how-it-works#blueprints) 解释了用户可以从哪里导入。新接触蓝图？[你的第一次贡献](/marketplace/first-contribution) 会带你完成第一次蓝图的整个流程。

完整的模式和每个选择器都在 home-assistant.io 上为用户提供文档：[蓝图模式](https://www.home-assistant.io/docs/blueprint/schema/) 和 [选择器](https://www.home-assistant.io/docs/blueprint/selectors/)。本页面的内容是关于如何编写一个让其他人喜欢使用并持续使用的蓝图。

## 蓝图模块 {#the-blueprint-block}

每个蓝图以 `blueprint` 模块开始，随后是其领域的配置：自动化的触发器、条件和动作，脚本的序列，或模板实体的配置。

```yaml
blueprint:
  name: "Notify when a door stays open"
  description: >
    Sends a notification when a door has been open for too long.
    Needs a door sensor and a device with the companion app.
  domain: automation
  author: "Your name"
  homeassistant:
    min_version: "2024.6.0"
  input:
    door:
      name: "Door"
      selector:
        entity:
          filter:
            - domain: binary_sensor
              device_class: door
```

| 键 | |
| --- | --- |
| `name` | 必填。简短且说明其作用。 |
| `domain` | 必填。`automation`、`script` 或 `template`。 |
| `description` | 蓝图的功能及用户所需内容。支持 Markdown。导入对话框和编辑器会显示它。 |
| `author` | 你的名字，或你的论坛名。 |
| `homeassistant` | `min_version`：你的蓝图支持的最早 Home Assistant，作为 `major.minor.patch`。 |
| `input` | 空白项。见下文。 |
| `source_url` | 留空。Home Assistant 将其设置为用户导入的 URL。 |

## 输入项 {#inputs}

每个输入项都有一个键，你可以与 `!input` 一起使用，并带有以下选项：

- `name` 和 `description`：用户在表单中看到的内容。
- `selector`：用户获得的控件。如果没有，用户将得到一个纯文本字段，并且必须猜测要输入的内容。
- `default`：使输入项为可选。如果没有默认值，用户必须填写它。

在配置中使用每个输入项时，请使用 `!input <key>`。Home Assistant 会拒绝使用未定义`!input` 的蓝图。

输入项不是模板变量。要在模板中使用，请先将其设为变量：

```yaml
variables:
  door_entity: !input door

actions:
  - action: notify.notify
    data:
      message: "{{ state_attr(door_entity, 'friendly_name') }} is still open."
```

### 选择合适的选择器 {#choose-the-right-selector}

选择器决定了你的蓝图使用起来有多方便。一些有帮助的提示：

- 在 `domain` 和 `device_class` 上过滤实体选择器，这样用户只会看到合理的实体。列出房子里每一个传感器的门传感器选择器就是一个难题。
- 对于动作作用的对象，使用 `target` 选择器。用户可以选择实体、设备、区域、楼层或标签，然后你直接传递给 `target`。
- 给 `number` 输入一个合理的 `min`、`max` 和 `unit_of_measurement`。
- 对于用户可以开启或关闭的可选行为，使用 `boolean`。

[selectors](https://www.home-assistant.io/docs/blueprint/selectors/) 页面列出了所有选择器，而设计区的 [selector component](/design/components/selector) 则展示了每个选择器的外观。

### 将输入分组到各个部分中 {#group-inputs-in-sections}

对于大量输入，将它们分组到各个部分中。一个部分有自己独立的 `input` 键，可选地还可以有 `name`、`icon`、`description` 和 `collapsed`：

```yaml
blueprint:
  name: "Notify when a door stays open"
  domain: automation
  homeassistant:
    min_version: "2024.6.0"
  input:
    door:
      name: "Door"
      selector:
        entity:
          filter:
            - domain: binary_sensor
              device_class: door
    advanced:
      name: "Advanced"
      icon: mdi:cog
      collapsed: true
      input:
        wait_time:
          name: "Wait time"
          default: 300
          selector:
            number:
              min: 30
              max: 3600
              unit_of_measurement: seconds
```

部分只改变表单。你仍然使用它们自己的键来使用输入，例如 `!input wait_time`，所以每个键在所有部分中必须唯一。部分需要 Home Assistant 2024.6 或更新版本：使用它们时设置 `min_version`。

## 模板实体蓝图 {#template-entity-blueprints}

带有 `domain: template` 的蓝图描述一个模板实体。用户在 `configuration.yaml` 中设置它，并带有 `use_blueprint`：

```yaml
template:
  - use_blueprint:
      path: homeassistant/inverted_binary_sensor.yaml
      input:
        reference_entity: binary_sensor.front_door
    name: "Front door closed"
    unique_id: front_door_closed
```

随 Home Assistant 提供的 [反转二进制传感器](https://github.com/home-assistant/core/blob/dev/homeassistant/components/template/blueprints/inverted_binary_sensor.yaml) 是一个完整的示例。其他内置蓝图也是很好的示例：[自动化](https://github.com/home-assistant/core/tree/dev/homeassistant/components/automation/blueprints) 和 [脚本](https://github.com/home-assistant/core/tree/dev/homeassistant/components/script/blueprints)。

## 测试它 {#test-it}

按照用户获取的方式进行测试：从你将要分享的 URL 导入它。

1. 进入 **设置** > **自动化与场景** > **蓝图**，选择 **导入蓝图**，并输入你的 URL。
2. 根据它创建一个自动化或脚本。首先只填写必填输入，以便测试默认值。
3. 在你的家中运行它，并在自动化未按预期执行时查看跟踪。
4. 创建第二个自动化，将每个输入设置为其他值。

然后考虑边界情况：一个传感器是 `unavailable`，一个空的可选输入，一个目标是区域而不是实体，以及当触发器在自动化仍在运行时再次触发会发生什么。最后一个是你自动化的 `mode`：`restart` 对于类似运动灯的情况通常是正确的。

## 在不破坏它的情况下更改它 {#change-it-without-breaking-it}

每个基于你的蓝图构建的自动化都使用用户导入的副本。当用户选择 **重新导入蓝图** 时，Home Assistant 会将你的新版本下载覆盖旧版本，并且基于它构建的每个自动化都会立即使用新版本。用户没有机会先填写任何新内容。所以：- 永远不要重命名输入。之前构建的自动化仍然会使用旧名称传递它们的值。在新名称下，该输入将丢失。  
- 给每个新的输入设置一个`default`。Home Assistant会拒绝没有默认值而遗漏输入的自动化，因此如果没有默认值，基于你的模板构建的每一个自动化都会停止工作。  
- 不要更改输入期望的内容，比如选择器，或者把秒改成分钟。Home Assistant不会检查存储的值是否与新选择器匹配：旧值会原样进入。  
- 当你在Home Assistant中开始使用新内容时，抛出`min_version`。旧版本的用户会收到明确的错误提示，而不是导致自动化失败。  
- 对于较大的更改，请发布新的模板，并使用新的网址。用户可以在准备好时迁移。蓝图模式没有版本号。在你的论坛主题或存储库中说明有什么变化以及何时变化，这样用户就知道何时需要重新导入。

## 分享它 {#share-it}

用户导入的 URL 就是你的蓝图的身份：从那里重新导入。选择一个地方，并保持蓝图在那里。

- **社区论坛的一个主题。** 将它发布在 [蓝图交流](https://community.home-assistant.io/c/blueprints-exchange/53) 中。Home Assistant 会导入首帖中第一个 YAML 代码块的蓝图，因此要发布新版本，请编辑该帖子。遵循 [关于蓝图](https://community.home-assistant.io/t/about-blueprints/253788) 主题中的规则：每个蓝图一个主题，一个清晰的标题，它的功能和需求，帖子中的完整蓝图，以及一个导入徽章。
- **GitHub 上的一个文件。** 仓库会保留每次修改的历史记录，人们可以打开问题和 pull requests。共享默认分支上文件的 URL，这样重新导入就能获取最新版本。
- **GitHub gist。** 快速，并且适合小东西。一个论坛话题和一个 GitHub 文件配合得很好：将蓝图保存在 GitHub 上，并使用话题来讨论它。然后将 GitHub 的网址设为你的导入徽章上的网址。

导入徽章是一个 [我的链接](/glossary/my-link)：它会在读者自己的 Home Assistant 中打开导入对话框，并填入你的蓝图的网址。 [我的链接创建器](https://my.home-assistant.io/create-link/?redirect=blueprint_import) 会根据你的蓝图网址为你生成它。它会给你这样的 Markdown：

```markdown
[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fme%2Fmy-blueprints%2Fblob%2Fmain%2Fmotion_light.yaml)
```

`blueprint_url` 是你蓝图的网址，经过 URL 编码。导入了蓝图的用户也可以从他们的蓝图列表中通过 **共享蓝图** 来分享它：这会创建相同的链接。

为集成写文档？与集成页面配套的蓝图可以放在 home-assistant.io 上。请参见 [集成页面](/writing/reference/integration-page)。
