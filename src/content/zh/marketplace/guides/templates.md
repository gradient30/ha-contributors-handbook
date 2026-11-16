---
title: 发布模板宏
description: 分享 Jinja 宏，其他人可以将其导入到他们的模板中，作为 Marketplace 安装在 custom_templates 中的一个模板文件。
sidebarLabel: 模板宏
order: 4
---

# 发布模板宏 {#publish-template-macros}

一个 [template](/glossary/template) 文件包含 Jinja 宏：可重用的模板片段，其他人在他们自己的模板、自动化、脚本和模板实体中导入使用。宏的工作原理，以及用户如何导入它们，请参见 home-assistant.io 上的 [自定义模板和宏](https://www.home-assistant.io/docs/templating/custom-templates/) 页面。

这是市场中最小的一种类型：只有一个文件。目录和 HACS 操作将其称为 `template`。

## 文件 {#the-file}

在一个 `.jinja` 文件中编写你的宏：

```jinja title="battery.jinja"
{% macro battery_icon(entity_id) %}
{% set level = states(entity_id) | int(0) %}
{{ 'mdi:battery-alert' if level < 20 else 'mdi:battery' }}
{% endmacro %}
```

用户通过你的文件名导入宏：

```jinja
{% from 'battery.jinja' import battery_icon %}
{{ battery_icon('sensor.front_door_battery') }}
```

这意味着你的文件名会成为用户使用它的一部分。选择一个不太可能与他人冲突的名字，并且不要后来重命名它。当 `filename` 发生变化时，市场将在下一次更新中删除旧文件，所有导入它的模板都将失效。

## 打包它 {#package-it}

将文件放在仓库的根目录下，并使用 `hacs.json` 命名为 `filename`：

```text
battery.jinja
hacs.json
README.md
```

```json title="hacs.json"
{
  "name": "Battery macros",
  "filename": "battery.jinja"
}
```

当 `filename` 根目录下没有名为 `.jinja` 的文件时，Marketplace 会拒绝模板仓库。它只会安装那个文件到用户配置的 `custom_templates` 文件夹中，并重新加载自定义模板，因此可以立即使用。

还有一些规则，因为 Home Assistant 在启动时会读取 `custom_templates` 中的每个文件：

- 文件必须是 UTF-8 编码。Home Assistant 无法解码的文件会阻止它启动。
- 文件必须小于 5 MiB。Home Assistant 会跳过更大的文件。
- 模板不支持 `zip_release`：一个归档文件会解压到所有模板共享的文件夹中。
- 两个仓库不能安装同名文件。Marketplace 会拒绝第二个文件。HACS 需要 GitHub 模板的发布版本。每个版本都要发布一次。请参见 [发布和更新](/marketplace/guides/releases)。

## 在你的仓库中检查它 {#check-it-in-your-repository}

在每次推送和 pull request 时，使用 `category: "template"` 运行 [HACS action](https://github.com/hacs/action)。在你的 README 中添加一些宏使用示例：这是用户决定是否想要它时会阅读的内容。
