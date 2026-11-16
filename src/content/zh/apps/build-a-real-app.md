---
title: 构建一个真正的应用
description: 完整地演示一个应用程序，就像有经验的应用开发者设置它一样。包含 S6 覆盖的服务、使用 Bashio 的选项、翻译、文档、持续集成（CI）和发布。
order: 3
---


# 构建一个真正的应用 {#build-a-real-app}
[你的第一个应用](/apps/first-app) 展示了一个应用所需的最少内容。一个真正的应用需要更多：以正确顺序启动的服务，并在服务崩溃时停止容器，带有验证的选项，带有级别的日志，文档，代码检查，每种架构的镜像，以及发布版本。

学习这一点的最好方法是阅读一个真实的应用。[hassio-addons/app-example](https://github.com/hassio-addons/app-example) 是 Home Assistant 社区应用的示例应用，该项目维护一组社区应用，以及 [Bashio](/apps/bashio)。它每隔几秒在日志中显示一个随机引用。它本身并没有太大用处，但周围的一切都是按照维护良好的应用应有的方式设置的。本教程将逐文件地讲解它。打开此页面旁边的仓库。你不需要构建任何东西就可以跟随学习，但你可以安装示例以查看其运行情况，并将其复制作为你自己应用的起点。

## 先尝试一下 {#try-it-first}
示例应用已发布在 [Home Assistant 社区应用仓库](https://github.com/hassio-addons/repository)。安装方法：

1. 添加仓库：在 **设置** > **应用** 下，打开 **应用商店**，在右上角菜单中选择 **仓库**。添加 `https://github.com/hassio-addons/repository`。
2. 在商店中找到 **示例** 并选择 **安装**。
3. 选择 **启动**，然后打开 **日志** 标签。

你将看到显示应用名称和版本及你的系统的横幅，每五秒显示一条引用，每十秒显示第二个服务的一条信息。在 **配置** 标签中更改 **引用间隔秒数**，重启应用，然后查看日志。

## 1. 仓库 {#1-the-repository}
Home Assistant Community Apps 为每个应用提供自己的 Git 仓库。一个单独的仓库，即你刚刚添加的那个，列出了用户可用的已发布应用。应用仓库看起来像这样，省略了一些文件，如 GitHub，比如问题模板和行为准则：

```text
app-example/
├── .github/
│   ├── workflows/
│   │   ├── ci.yaml
│   │   ├── deploy.yaml
│   │   ├── labels.yaml
│   │   ├── pr-labels.yaml
│   │   └── release-drafter.yaml
│   └── renovate.json
├── example/
│   ├── rootfs/
│   ├── translations/
│   │   └── en.yaml
│   ├── .README.j2
│   ├── build.yaml
│   ├── config.yaml
│   ├── Dockerfile
│   ├── DOCS.md
│   ├── icon.png
│   └── logo.png
├── .yamllint
├── LICENSE.md
└── README.md
```

应用本身是 `example` 文件夹。它之外的所有内容都是为开发该应用的人准备的：工作流、代码检查器设置和许可证。

你不必将你的应用拆开保存。你也可以将所有应用保存在一个仓库中，并在顶部放置一个 `repository.yaml`，以便用户直接添加该仓库。[home-assistant/apps-example](https://github.com/home-assistant/apps-example) 就是这种设置。[创建和共享仓库](/apps/guides/repository) 解释了该设置。`example` 文件夹在两种方式下的作用相同。

## 2. 配置 {#2-the-configuration}
[`example/config.yaml`](https://github.com/hassio-addons/app-example/blob/main/example/config.yaml) 告诉 Supervisor 应用是什么以及用户可以设置什么：

```yaml
---
name: Example
version: dev
slug: example
description: Example app by Home Assistant Community Apps
url: https://github.com/hassio-addons/app-example
init: false
arch:
  - aarch64
  - amd64
options:
  log_level: info
  seconds_between_quotes: 5
schema:
  log_level: list(trace|debug|info|notice|warning|error|fatal)
  seconds_between_quotes: int(1,120)
```

需要注意的几件事：- `version: dev` 是一个占位符。当发布版本时，Home Assistant Community Apps 的工具会将实际的版本号和 `image` 写入用户添加的应用仓库副本文件中。在你自己的仓库中，将实际版本写在这里，并在发布镜像后添加 `image`。参见 [发布你的应用](/apps/guides/publishing)。
- `init: false` 是基础镜像所必需的，因为 S6 覆盖层必须是容器中的第一个进程。[使用 S6 覆盖层运行服务](/apps/guides/s6-overlay#what-the-base-images-set-up) 解释了原因。
- 该模式会为你进行验证。`int(1,120)` 意味着 Supervisor 会拒绝 1 到 120 之外的任何值，因此脚本无需检查。`list(...)` 显示一个下拉菜单。
- `log_level` 是一个常见约定：当出现问题时，用户自己开启调试日志，无需发布应用的新版本。每个键都在 [应用配置](/apps/reference/configuration) 参考中。选项及其类型在 [添加选项](/apps/guides/options) 中。

## 3. Dockerfile {#3-the-dockerfile}
`example/Dockerfile`，简化版：

```dockerfile
ARG BUILD_FROM=ghcr.io/hassio-addons/base:21.0.8
# hadolint ignore=DL3006 {#hadolint-ignoredl3006}
FROM ${BUILD_FROM}

# Copy root filesystem {#copy-root-filesystem}
COPY rootfs /

# Setup base {#setup-base}
RUN apk add --no-cache \
    coreutils=9.11-r0 \
    wget=1.25.0-r3

# Build arguments {#build-arguments}
ARG BUILD_ARCH
ARG BUILD_VERSION

# Labels {#labels}
LABEL \
    io.hass.arch="${BUILD_ARCH}" \
    io.hass.version=${BUILD_VERSION}
```

完整文件添加了更多的构建参数和标签：名称、描述、构建日期、Git 提交，以及像 `org.opencontainers.image.source` 这样的开放容器倡议标签。构建工作流会填写这些信息；Supervisor 仅传递 `BUILD_ARCH`、`BUILD_VERSION`，并且使用 `build.yaml` 时，还会传递 `BUILD_FROM` 以及你在该文件 `args:` 下列出的任何构建参数。它还设置了 `io.hass.type="app"`。该标签的历史值是 `addon`。参见 [labels](/apps/guides/dockerfile#labels)。

从中可以得出：- **基础镜像。** 该示例从 Home Assistant 社区应用的基础镜像开始。像 [Home Assistant 基础镜像](/apps/guides/dockerfile#base-images) 一样，它是带有 S6 覆盖、Bashio 和 Tempio 的 Alpine Linux。它在日志中添加了启动横幅，并根据 `log_level` 选项设置 Bashio 日志级别。你可以使用任意一个。
- **`build.yaml`。** 该示例还包含一个针对每种架构的基础镜像 `build.yaml`。它的构建工作流程从该文件读取 `build_from`。Supervisor 仍然读取它，但会记录其已弃用。在你自己的应用中，将基础镜像放在 `Dockerfile` 中，并为 `BUILD_FROM` 设置默认值，如这里的第一行所示，并省略 `build.yaml`。参见 [build.yaml](/apps/guides/dockerfile#buildyaml)。

- **固定版本。** 基础镜像和每个 Alpine 包都有一个具体版本。构建是可重复的，[Renovate](https://docs.renovatebot.com/) 在新版本发布时会打开一个 pull request。[例子中的 `.github/renovate.json`](https://github.com/hassio-addons/app-example/blob/main/.github/renovate.json) 有找到这些版本的 `Dockerfile` 的规则。
- **`COPY rootfs /`。** 应用程序的所有文件都存放在 `rootfs`，在镜像中的位置就是它们应该去的地方。没有 `CMD`，也没有 `ENTRYPOINT`：S6 覆盖会启动 `rootfs` 中的内容。
- **hadolint。** 注释 `

# hadolint ignore=DL3006` 会在 CI 中运行的 Dockerfile linter 中屏蔽一条规则，因为基础镜像标签来自一个参数。 {#4-services-with-s6-overlay}
## 4. 带有 S6 覆盖的服务 {#shellcheck-shellbash}
[`example/rootfs/etc/s6-overlay/`](https://github.com/hassio-addons/app-example/tree/main/example/rootfs/etc/s6-overlay) 有三个服务：

| 服务 | 类型 | 依赖于 | 功能 |
| --- | --- | --- | --- |
| `init-example` | oneshot | `base` | 启动时运行一次并记录问候。在实际应用中，这里用于编写配置文件。 |
| `example1` | longrun | `init-example` | 运行 `/usr/bin/example1.sh`，即报价循环。 |
| `example2` | longrun | `example1` | 运行 `/usr/bin/example2.sh`，第二个循环。 |

longrun 的 `run` 脚本会记录一行日志，然后通过 `exec` 将控制权交给程序：

```bash
#!/command/with-contenv bashio
# shellcheck shell=bash {#5-read-options-with-bashio}
bashio::log.info "Starting Example1..."

exec /usr/bin/example1.sh
```

每个 longrun 都有一个 `finish` 脚本，当程序崩溃时会停止整个容器，因此 Supervisor 能看到失败。所有三个都在 `user` 包中，通过 `user-bundles.d/user/contents.d/` 中的空文件实现。文件夹、`type`、`up` 和 `finish` 文件以及依赖是如何工作的，请参阅 [使用 S6 覆盖运行服务](/apps/guides/s6-overlay)。在查看示例之后阅读该指南；它使用的正是这个布局。

## 5. 使用 Bashio 读取选项 {#shellcheck-shellbash-1}
`rootfs/usr/bin/example1.sh` 中的 quote 循环在启动时只读取一次其选项：

```bash
#!/command/with-contenv bashio
# shellcheck shell=bash {#is-an-optional-option-set}
main() {
    local sleep

    bashio::log.trace "${FUNCNAME[0]}"

    sleep=$(bashio::config 'seconds_between_quotes')
    bashio::log.info "Seconds between each quotes is set to: ${sleep}"

    while true; do
        display_quote
        sleep "${sleep}"
    done
}
main "$@"
```

`bashio::config` 从 Supervisor API 获取选项，这就是脚本以 `with-contenv` 开头的原因：它提供了所需的令牌。选项只有在用户保存并重启应用时才会更改，所以只读取一次就足够了。

你用于选项的其他函数：

```bash
# Is an optional option set? {#stop-with-a-clear-message-when-a-required-option-is-empty}
if bashio::config.has_value 'username'; then
  bashio::log.info "Logging in as $(bashio::config 'username')"
fi

# Stop with a clear message when a required option is empty {#a-boolean-option}
bashio::config.require 'password'

# A boolean option {#6-log-with-levels}
if bashio::config.true 'ssl'; then
  bashio::config.require.ssl
fi
```

所有这些都在 [Bashio 选项参考](/apps/bashio/config) 中。

## 6. 带等级的日志 {#the-page-might-not-contain-a-quote-at-all-in-which-case-grep-exits}
示例以不同的等级记录日志。`bashio::log.info`用于普通事件，`bashio::log.notice`在回退到离线报价时记录，`bashio::log.trace`在每个函数开始时记录，以便有人需要查看所有内容。

用户通过`log_level`选项选择日志等级。社区基础镜像会在你的服务启动前应用它，所以`bashio::log.debug`和`bashio::log.trace`将保持静默，除非用户要求。在Home Assistant基础镜像上，请在第一个服务启动时自行设置：

```bash
if bashio::config.has_value 'log_level'; then
  bashio::log.level "$(bashio::config 'log_level')"
fi
```

示例还展示了另一件事。Bashio在命令失败时会停止脚本。示例使用`grep`获取报价，当找不到内容时，`grep`会失败。因此示例添加了`|
| true`，并附上了说明原因的注释：

```bash
# The page might not contain a quote at all, in which case grep exits {#non-zero-bashio-runs-with-errexit-and-inheriterrexit-so-swallow}
# non-zero. Bashio runs with errexit (and inherit_errexit), so swallow {#that-here-and-let-the-caller-deal-with-an-empty-quote-instead}
# that here and let the caller deal with an empty quote instead. {#7-translations-and-documentation}
quote=$(grep -e "<dt>" -e "</dd>" <<< "${html}" | ...) || true
```

日志记录、日志等级和错误处理可以参考[Bashio日志参考](/apps/bashio/logging)。

## 7. 翻译和文档 {#8-continuous-integration}
用户在应用中看到的内容，除了日志之外：

- `translations/en.yaml` 在 **配置** 标签上为选项提供可读的名称和描述。如果没有它，用户会看到 `seconds_between_quotes`。
- `DOCS.md` 是 **文档** 标签：如何安装应用、每个选项以及在哪里获取帮助。
- `icon.png` 和 `logo.png` 会出现在应用商店和应用页面上。
- `.README.j2` 是用户添加到仓库中应用的 `README.md` 的模板。Home Assistant 社区应用的发布工具会渲染它，包括版本信息，对于测试版和边缘版本渠道，还会显示警告。如果你将应用保存在一个仓库中，请直接编写一个普通的 `README.md`。

示例的翻译文件：

```yaml
---
configuration:
  log_level:
    name: Log level
    description: The amount of logging the app should do.
  seconds_between_quotes:
    name: Seconds between quotes
    description: >-
      The number of seconds the app waits until showing a new quote in the
      app log.
```

[/apps/guides/presentation/ 展示你的应用] 涵盖了这些文件的每一个。

## 8. 持续集成 {#9-releases-and-versions}
每个 pull request 都会运行 [`.github/workflows/ci.yaml`](https://github.com/hassio-addons/app-example/blob/main/.github/workflows/ci.yaml)。它会调用来自 [hassio-addons/workflows](https://github.com/hassio-addons/workflows) 的共享工作流，并固定到一个提交。该工作流：1. 从 `config.yaml` 和 `build.yaml` 读取应用信息：slug、架构和基础镜像。
2. 运行静态检查工具，每个作为独立的任务：
   - 应用静态检查工具 [frenck/action-app-linter](https://github.com/frenck/action-app-linter)，用于验证 `config.yaml` 并提示可省略的默认值。
   - [Hadolint](https://github.com/hadolint/hadolint) 用于 `Dockerfile`。
   - [ShellCheck](https://www.shellcheck.net/) 用于脚本，包括 S6 服务的 `run` 和 `finish` 文件。
   - yamllint，使用 `.yamllint` 中的规则，并在每个 JSON 文件上使用 `jq`。
   - Prettier，用于 JSON、JavaScript、Markdown 和 YAML。
   - [zizmor](https://github.com/zizmorcore/zizmor)，用于检查工作流本身的安全问题。
3. 审查 pull request 变更的依赖项。
4. 为每种架构构建镜像，每个架构在其对应的运行器上构建，不进行推送。每个脚本中的 `

# shellcheck shell=bash` 行是为了 ShellCheck：它不了解 `bashio` 解释器，这一行告诉它将脚本作为 Bash 进行检查。 {#make-it-your-own}
其他工作流保持仓库整洁：`labels.yaml` 将仓库的标签与共享列表同步，`pr-labels.yaml` 检查每个 pull request 是否有描述更改的标签，例如 `bugfix` 或 `new-feature`，`release-drafter.yaml` 保持下一版发行说明的草稿更新。

> [!注意]
> hassio-addons/workflows 的 README 表示这些工作流可能会更改且没有版本控制，在其他项目中使用是可能的，但不推荐。对于你自己的仓库，复制你想要的 lint 任务，并使用 Home Assistant 的 [builder actions](/apps/guides/publishing#build-with-github-actions) 进行构建和发布。

## 9. 版本和发布 {#what-is-next}
[`.github/workflows/deploy.yaml`](https://github.com/hassio-addons/app-example/blob/main/.github/workflows/deploy.yaml) 在每次推送到 `main` 时运行，以及在 GitHub 上发布发布版本时运行。它首先运行与 CI 相同的检查，然后为每种架构构建镜像，将其推送到 GitHub 容器注册表，并将这些镜像组合成一个多架构镜像，如 `ghcr.io/hassio-addons/example`。

最终的版本和渠道取决于触发它的操作：

| 触发 | 版本 | 渠道 |
| --- | --- | --- |
| 推送到 `main` | 简短的 Git 提交，如 `6b6b1f1` | edge |
| GitHub 上的预发行 | 标签，小写且不带前导 `v` | beta |
| GitHub 上的发布 | 标签，小写且不带前导 `v` | stable |稳定版本也会进入测试频道。构建完成后，工作流程会通知 Home Assistant 社区应用的匹配应用仓库有新版本。然后它的工具会复制应用文件，将 `version` 和 `image` 写入 `config.yaml`，渲染 README，并提交这些更改。该频道的用户会收到更新。

所以一次发布就是一次 GitHub 发布。Release Drafter 会保留发布说明的草稿，并通过类似 `v1.2.0` 的标签发布，它会开始构建。版本遵循 [语义化版本](https://semver.org/)，正如`DOCS.md` 的示例向用户解释的：主版本用于重大变更，次版本用于新功能，修补版本用于修复。该发布流程特定于 Home Assistant 社区应用程序。其背后的规则适用于每个应用程序，并在 [发布你的应用程序](/apps/guides/publishing#versions) 中说明：在用户可以看到新版本之前发布镜像，并且永远不要重复使用一个版本。

## 自定义你的应用 {#自定义你的应用}
要从示例开始创建你自己的应用：

1. 将 `example` 文件夹复制到你的仓库中，并将其重命名为你的应用名称。
2. 在 `config.yaml` 中，更改 `name`、`slug`、`description`、`url` 以及选项。将 `version` 设置为实际版本。
3. 在 `Dockerfile` 中，选择你的基础镜像：保留社区基础镜像，或使用 [Home Assistant 基础镜像](/apps/guides/dockerfile#base-images)。将其放在 `ARG BUILD_FROM`，并删除 `build.yaml`。
4. 在 `Dockerfile` 中安装你的软件，并用你自己的服务替换 `rootfs/etc/s6-overlay/` 中的服务。保留 `finish` 脚本。
5. 更新 `translations/en.yaml`、`DOCS.md`、图标和徽标。
6. 添加工作流：从示例中选择你想要的 lint 任务，以及用于构建和发布镜像的 [构建器操作](/apps/guides/publishing)。
7. 测试它：将文件夹复制到 `local_apps` 中的 Home Assistant，或从 [测试你的应用](/apps/guides/testing) 使用 devcontainer。

## 接下来做什么 {#接下来做什么}
- [应用如何工作](/apps/how-apps-work)：Supervisor 对你的应用从仓库到运行容器的处理方式。下一步阅读它。
- [使用 S6 覆盖运行服务](/apps/guides/s6-overlay)：关于 `rootfs` 中服务的所有内容。
- [Bashio 参考](/apps/bashio)：每个函数，从选项到 Supervisor API。
- [保护你的应用](/apps/guides/security)：添加 AppArmor 配置文件，并尽可能少请求权限。
- [通过 ingress 添加 Web 界面](/apps/guides/ingress)：在 Home Assistant 中显示你的应用。
