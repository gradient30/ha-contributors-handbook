---
title: Linter、hassfest 与 CI
description: 检查每个承诺和每个pull request到Home Assistant Core, 以及如何自己运行。
sidebarGroup: 写代码
order: 5
---



# Linter、hassfest 与 CI {#linters-hassfest-and-ci}
在检查你的代码之前 机器会看看 Linters II检查风格, mypy检查类型,hassfest检查集成的元数据,CI再次运行,加上测试. 自己先运行 : 检查失败的 pull request 不检查 。

## Git钩子 {#the-git-hooks}

{臀部H0}安装了 [预览](https://prek.j178.dev/) 的 Git 钩子, 一个快速的投注。 每次你犯案 他们都会查你改变的文件 当钩子修正某种东西时, 如格式化, 承诺停止: 添加已修改的文件并再次执行 。

钩子配置于 `.pre-commit-config.yaml` 。 其中包括:

- **楷书**:涂上代码和格式。
- **代码spell**:发现常见的拼写错误.
- **yamllint**和**Pretier**:检查和格式YAML和JSON文件.
- ** 我知道了**:检查[类型提示](/core/development/typing)。
- **pylint**:运行为Home Assistant写的额外支票。
- ** gen  requirements all**: 当 `manifest.json` 更改时更新要求文件 。
- ** hassfest**:验证生成的文件的集成和更新.
- ** 不承诺对部门**:阻止你直接承诺`dev`。 修行处.

运行所有文件中的所有钩子 :

```shell
prek run --all-files
```

只能用你的改变来操作它们 看看它们有什么改变:

```shell
prek run --show-diff-on-failure
```

在Visual Studio代码中,这就是**Prek**任务. 您也可以在单个文件中运行一个 linter, 如 `ruff check homeassistant/components/example/sensor.py` 或 `pylint homeassistant/components/example` 。

> [!IMPORTANT]
> 钩子可以在您的整合外更改文件, 如 `CODEOWNERS`, `requirements_all.txt` 或 [`homeassistant/generated/`](https://github.com/home-assistant/core/tree/dev/homeassistant/generated) 文件 。 这些变化属于您的 pull request 。

## 狂欢 {#hassfest}

Hassfest是整合的验证符. 它读取您代码周围的文件, 如 `manifest.json`, `strings.json`, `services.yaml`, `icons.json` 和`quality_scale.yaml`, 并检查它们是否完整和一致 。 它还从它们生成文件,如`CODEOWNERS`和[`homeassistant/generated/`](https://github.com/home-assistant/core/tree/dev/homeassistant/generated)中的配置流列表,发现信息,等等.

更改文件后运行 :

```shell
python3 -m script.hassfest
```

仅检查一次整合,速度更快:

```shell
python3 -m script.hassfest --integration-path homeassistant/components/example
```

使用 `-p` 只运行其部分插件, 如 `-p mypy_config` 在您更改 `.strict-typing` 后运行 。

使用 `--skip-plugins` 来省略一些 。 一个新的整合开始于 `quality_scale.yaml` 设置为 `todo` 的每个规则, 而 `quality_scale` 插件报告说, 在每个青铜规则是 `done` 或 `exempt` 之前都是错误 。 Hassfest 只写生成的文件, 当它没有发现错误时, 所以当你仍在工作 这些规则, 运行它像这样:

```shell
python3 -m script.hassfest --skip-plugins quality_scale
```

脚手架脚本对新的整合也一样. 在打开您的 pull request 之前, 运行再次繁忙而不跳过任何东西 。

## Py {#pylint}

在标准检查旁边,核心有它自己的pylint插件,在[`packages/pylint-home-assistant/`](https://github.com/home-assistant/core/tree/dev/packages/pylint-home-assistant)中. 它的检查覆盖图案Ruff无法看到,因为它们需要类型推论或读取其他文件,比如`manifest.json`和`quality_scale.yaml`. 他们中许多人检查了用来亲手指出的规则审查员. [插件的读取ME](https://github.com/home-assistant/core/blob/dev/packages/pylint-home-assistant/README.md)解释每张支票。

如果 pylint 对您的代码有误, 仅此而已, 请禁用该行的检查, 用检查的名称而不是它的代码 :

```python
hass.data[DOMAIN] = data  

# pylint: disable=home-assistant-use-runtime-data {#ci}
```

审查者会问为什么, 所以准备解释它。

## CI {#ci}

当打开 pull request,GitHub 时 动作运行 CI 工作流程。 它运行着钩子,蜂拥, p,和 mypy,检查新依赖的要求和许可证,并对每个支持的Python版本进行测试. 为了改变为一个一体化,它只对这种一体化进行测试。 对核心的改变本身运行整个套房.

如果您的 GitHub 账户是新建的, 在您的第一个 pull request 上的 CI 在维护者批准之前不会开始 。 这是安全措施 不是判断你的密码

如果 CI 因您的更改而失败, 请将您的 pull request 转换成草稿, 修复, 并重新标记它 。 有些测试是片状的。 如果您确定失败与您的更改无关, 请在 pull request 中说, 并等待维护者 。 不要继续重新启动运行 。
