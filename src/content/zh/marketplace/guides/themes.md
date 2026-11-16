---
title: 发布主题
description: 编写一个主题文件，选择要设置的变量，支持明亮和黑暗模式，进行测试，并打包到市场中。
sidebarLabel: 主题
order: 3
---

# 发布主题 {#publish-a-theme}

一个 [主题](/glossary/theme) 是一个包含颜色和一些尺寸的 YAML 文件，用于 Home Assistant 界面。用户可以在他们的个人资料中选择一个主题，或者在单个仪表板视图或卡片上设置一个主题。制作一个主题不需要编程：只需要 YAML，以及对在明亮和暗色环境下看起来好的审美。  

前端如何应用主题，从代码的角度来看，可以参考 [主题和设计令牌](/frontend/architecture/theming)。此页面面向编写主题的人。

## 主题文件 {#the-theme-file}

主题文件是一个映射。键是主题的名称，就像用户在个人资料中看到的一样。在其下是变量，不包括 CSS 前面加的 `--`：

```yaml title="themes/nordic.yaml"
Nordic:
  primary-color: "#5e81ac"
  accent-color: "#d08770"
  card-background-color: "#eceff4"
  primary-background-color: "#e5e9f0"
  primary-text-color: "#2e3440"
  ha-card-border-radius: "16px"
```

引用每一个值。在 YAML 中，`#` 开始一条注释，所以未引用的颜色会丢失，而且前端无论如何都期望每个值都是字符串。

一个文件可以包含多个主题，每个主题都有自己的名称。Home Assistant 通过 `configuration.yaml` 中的这一行从用户配置的 `themes` 文件夹读取文件，创建文件时它会自己添加这一行：

```yaml title="configuration.yaml"
frontend:
  themes: !include_dir_merge_named themes
```

删除该行的用户，或者配置较旧的用户，需要将其添加回来。在你的 README 中说明：当主题没有显示时，这是首先要检查的内容。

## 设置哪些变量 {#which-variables-to-set}

前端有两层变量，一个好的主题会设置两者。

### 经典变量 {#the-classic-variables}

大多数主题都会设置下面的变量。它们在前端的 [`src/resources/theme/color/color.globals.ts`](https://github.com/home-assistant/frontend/blob/dev/src/resources/theme/color/color.globals.ts) 中定义，许多组件都会使用它们。[主题变量](/marketplace/reference/theme-variables) 列出了所有变量，并提供了明暗模式下的默认值：复制你想更改的变量即可。| 变量 | 用途 |
| --- | --- |
| `primary-color` | 主要强调色。其他变量，如 `sidebar-selected-icon-color`，默认使用它。 |
| `accent-color` | 第二强调色 |
| `primary-background-color` | 页面背景 |
| `secondary-background-color` | 第二背景，用于区别于页面的表面 |
| `card-background-color` | 卡片。`sidebar-background-color` 和 `ha-card-background` 默认使用它。 |
| `primary-text-color` | 大多数文本 |
| `secondary-text-color` | 不太重要的文本，如描述 |
| `text-primary-color` | 位于 `primary-color` 上的文本 |
| `divider-color` | 项目之间的线条 |
| `error-color`, `warning-color`, `success-color`, `info-color` | 状态消息和警告 |
| `sidebar-background-color`, `sidebar-text-color`, `sidebar-icon-color`, `sidebar-selected-icon-color`, `sidebar-selected-text-color` | 侧边栏 |
| `app-header-background-color`, `app-header-text-color` | 仪表板及其他页面顶部的标题 |
| `state-icon-color` | 实体图标 |卡片本身有自己的变量，从 `ha-card` 开始，即内置卡片的容器。其他组件也有一些变量，比如 sections 视图的间距：它们在 [组件变量](/marketplace/reference/theme-variables#component-variables) 下。

| 变量 | 作用 |
| --- | --- |
| `ha-card-background` | 卡片的背景。若无则回退到 `card-background-color`。 |
| `ha-card-border-radius` | 角的圆角度 |
| `ha-card-border-width`, `ha-card-border-color` | 边框 |
| `ha-card-box-shadow` | 阴影。默认无阴影。 |
| `ha-card-header-color`, `ha-card-header-font-size` | 卡片的标题 |

实体状态的颜色也有变量，比如 `state-light-active-color` 或 `state-lock-locked-color`。它们都在 [实体状态](/marketplace/reference/theme-variables#entity-states) 下。

### 设计代币 {#the-design-tokens}

较新的组件使用 [设计代币](/glossary/design-token)，其名称以 `ha-` 开头。它们的颜色不来自 `primary-color`。例如，开关的颜色来自 `ha-color-fill-primary-normal-resting`，它指向 `ha-color-primary-90`，这是主色调的一个步骤。因此，仅设置 `primary-color` 的主题会将这些组件保持为默认蓝色。

要为它们设置你的颜色，也需要设置主色调：共十一步，从 `ha-color-primary-05`（最深）到 `ha-color-primary-95`（最浅）。

```yaml title="themes/nordic.yaml"
Nordic:
  primary-color: "#5e81ac"
  ha-color-primary-05: "#0d1520"
  ha-color-primary-10: "#18263a"
  ha-color-primary-20: "#25384f"
  ha-color-primary-30: "#3a5577"
  ha-color-primary-40: "#5e81ac"
  ha-color-primary-50: "#7896bb"
  ha-color-primary-60: "#90a9c8"
  ha-color-primary-70: "#a9bdd5"
  ha-color-primary-80: "#c4d2e3"
  ha-color-primary-90: "#dfe7f0"
  ha-color-primary-95: "#eff3f8"
```

`ha-color-primary-40` 是默认主题中 `primary-color` 的值，因此从这里开始。语义代币，如 `ha-color-fill-primary-normal-resting`，会为暗模式自行选择其他步骤。代币及其默认值可在设计区域的 [颜色](/design/foundations/color) 页面上查看。默认主题为用户执行以下操作：当用户在其个人资料中选择自己的主色时，前端会根据该颜色计算调色板。自定义主题则没有这样的帮助，必须自己设置调色板。

### RGB 变体 {#rgb-variants}

某些组件需要带透明度的颜色，并使用变量的 RGB 变体，例如 `rgb-primary-color`。当你将变量设置为十六进制颜色时，例如 `"#5e81ac"`，前端会为你创建其 RGB 变体。对于任何其他格式的颜色，例如 `rgb(94, 129, 172)`，你需要自己设置 RGB 变体，作为三个数字：

```yaml
Nordic:
  primary-color: "rgb(94, 129, 172)"
  rgb-primary-color: "94, 129, 172"
```

### 变量变动 {#variables-change}

前端不保证哪些变量会保留。变量可能会被重命名，或在任何版本中停止使用。请在每个测试版中测试你的主题。

## 明暗模式 {#light-and-dark}

主题可以为明模式和暗模式设置不同的值，在`modes`下：

```yaml title="themes/nordic.yaml"
Nordic:
  primary-color: "#5e81ac"
  accent-color: "#d08770"
  modes:
    light:
      primary-background-color: "#e5e9f0"
      card-background-color: "#eceff4"
      primary-text-color: "#2e3440"
    dark:
      primary-background-color: "#2e3440"
      card-background-color: "#3b4252"
      primary-text-color: "#eceff4"
```

`modes`之外的变量在两种模式下都适用。`modes`至少需要`light`或`dark`其中之一。前端如何处理它：

- 同时有`light`和`dark`时，主题会遵循用户或其设备的设置。
- 只有`dark`时，主题总是暗色模式。没有`dark`，或者完全没有`modes`时，主题总是亮色模式。
- 在暗模式下，前端首先应用其自身的暗色，然后是你的变量，最后是你的`dark`值。你只需设置你想要不同的内容。

## 测试它 {#test-it}

1. 将您的主题文件复制到配置的 `themes` 文件夹中，放在 `configuration.yaml` 旁边。
2. 运行 `frontend.reload_themes` 操作，或重新启动 Home Assistant。有错误的主题无法加载，日志会说明原因。
3. 在您的个人资料中，选择您的主题。如果您的主题同时有明亮和黑暗模式，也可以在那里切换。
4. 浏览用户最常看到的地方：包含多种卡片的仪表板、更多信息对话框、设置页面以及带有输入的表单。
5. 检查每个背景上的文本是否可读。[辅助功能](/design/foundations/accessibility) 页面列出了内置主题达到的对比度比率，以及应达到的目标。

也在手机上检查：窄屏布局会以不同方式显示页眉和侧边栏。

## 打包它 {#package-it}

将文件放入你仓库中的 `themes` 文件夹：

```text
themes/nordic.yaml
hacs.json
README.md
```

市场会将 `themes` 文件夹中的所有内容安装到用户配置中的 `themes/<name of your theme file>/`，并重新加载主题。在调用安装完成之前，它会检查每个安装的 YAML 文件：

- 它必须是没有标签的有效 YAML。`!include`、`!secret` 和其他标签会被拒绝：主题会提供给每个用户，而标签可能引入任何文件。
- 它必须通过与 `configuration.yaml` 中主题相同的验证。损坏的主题会导致 Home Assistant 在下次启动时无法加载其配置。

在你的 README 中放置截图，包括亮色和暗色：目录会检查主题的 README 是否有图片。[仓库结构](/marketplace/reference/repository-structure#themes) 有详细信息，[HACS 操作](https://github.com/hacs/action) 与 `category: "theme"` 一起会进行检查。
