---
title: 分享你的第一个蓝图
description: 将已经在你家中运行的自动化转化为蓝图，自行导入以进行测试，并在蓝图交换中分享。
sidebarLabel: 你的第一次贡献
order: 1
---


# 分享你的第一个蓝图 {#share-your-first-blueprint}
共享某些内容的最快方式是使用 [blueprint](/glossary/blueprint)。你已经完成了最困难的部分：一个在你家可用的自动化。蓝图就是同样的自动化，其中特定于你家的部分，如哪个传感器和哪个灯光，留空以便其他人填写。

这大约需要半个小时。第4步需要一个 GitHub 账号。不需要编程。

已经在 GitHub 上有卡片、主题或集成吗？可以直接跳到 [发布要求](/marketplace/reference/repository-structure) 和 [HACS 操作](/marketplace/reference/validation)。完成这些检查并显示绿色也是一个很好的第一步。

## 1. 选择一个自动化 {#1-pick-an-automation}
选择一个你使用且有效的自动化。小规模的更好：一个触发器，一到两个动作。比如“当有动作时打开走廊灯，两分钟后关闭”。

在自动化编辑器中打开它，选择三点菜单，然后选择 **在 YAML 中编辑**。将 YAML 复制到文本编辑器中。

## 2. 添加蓝图块 {#2-add-the-blueprint-block}
在顶部放置一个 `blueprint` 块。它需要一个 `name` 和一个 `domain`。此处的域为 `automation`：蓝图也可以为脚本和模板实体创建。

```yaml
blueprint:
  name: "Motion light with a timeout"
  description: >
    Turns on a light when motion is detected, and turns it off
    again when there has been no motion for a while.
  domain: automation
  author: "Your name"
```

移除你的自动化的 `id` 和 `alias`。每个从你的蓝图创建的自动化都有自己的。

## 3. 将特定部分转化为输入 {#3-turn-the-specific-parts-into-inputs}
每个特定于你家的实体 ID、区域或数字都应成为一个输入。在 `input` 下定义每个输入，并使用 [选择器](/glossary/selector)，以便用户获得正确的选择器，并在自动化中使用 `!input`：

```yaml
blueprint:
  name: "Motion light with a timeout"
  description: >
    Turns on a light when motion is detected, and turns it off
    again when there has been no motion for a while.
  domain: automation
  author: "Your name"
  input:
    motion_sensor:
      name: "Motion sensor"
      selector:
        entity:
          filter:
            - domain: binary_sensor
              device_class: motion
    light:
      name: "Light"
      selector:
        target:
          entity:
            - domain: light
    wait_time:
      name: "Wait time"
      description: "How long to keep the light on after the last motion."
      default: 120
      selector:
        number:
          min: 0
          max: 3600
          unit_of_measurement: seconds

mode: restart
max_exceeded: silent

triggers:
  - trigger: state
    entity_id: !input motion_sensor
    from: "off"
    to: "on"

actions:
  - action: light.turn_on
    target: !input light
  - wait_for_trigger:
      - trigger: state
        entity_id: !input motion_sensor
        from: "on"
        to: "off"
  - delay: !input wait_time
  - action: light.turn_off
    target: !input light
```

Home Assistant 拒绝使用其未定义的 `!input` 的蓝图。每个带有 `default` 的输入对用户来说都是可选的。这个示例接近随 Home Assistant 提供的运动灯蓝图，[`motion_light.yaml`](https://github.com/home-assistant/core/blob/dev/homeassistant/components/automation/blueprints/motion_light.yaml) 在核心中。将它与你的蓝图对照阅读是一个很好的检查。

## 4. 将其作为 Gist 发布 {#4-publish-it-as-a-gist}
1. 前往 [GitHub Gists](https://gist.github.com/)。
2. 将文件命名为你的蓝图名称，文件后缀为 `.yaml`，例如 `motion_light_timeout.yaml`。
3. 粘贴你的蓝图，并将 Gist 创建为公开 Gist。
4. 复制 Gist 的 URL。

## 5. 自己导入它 {#5-import-it-yourself}
以用户获取的方式测试它：

1. 在 Home Assistant 中，进入 **设置** > **自动化和场景** > **蓝图**。
2. 选择 **导入蓝图**，粘贴你的 gist 的 URL，然后选择 **预览**。
3. 选择 **导入蓝图**。
4. 选择你的蓝图，然后选择 **创建自动化**。
5. 填写输入内容，保存，并检查自动化是否按预期工作。

修复 gist 中不工作的问题，然后再次导入。Home Assistant 会提示覆盖你之前导入的蓝图。

当它工作时，关闭你原来的自动化，以免两个自动化互相争夺同一个灯。

## 6. 分享它 {#6-share-it}
在社区论坛的 [Blueprint Exchange](https://community.home-assistant.io/c/blueprints-exchange/53) 蓝图分类中发布你的蓝图。先阅读其 [关于蓝图](https://community.home-assistant.io/t/about-blueprints/253788) 主题。简而言之：

- 每个蓝图一个主题，标题说明其功能。
- 描述蓝图的作用以及所需的设备。
- 在首帖中以 YAML 代码块形式包含完整蓝图。Home Assistant 可以直接从主题导入。
- 添加一个导入徽章。在 [my.home-assistant.io](https://my.home-assistant.io/create-link/?redirect=blueprint_import) 上创建一个，使用你主题的 URL。
- 从你自己的主题导入一次，以检查是否可用。

就这样：你已分享了你的第一个蓝图。当别人使用它时，他们会在你的主题中提问并建议改进。[蓝图](/marketplace/guides/blueprints) 解释了如何在不破坏别人基于它建立的自动化的情况下更改蓝图。
