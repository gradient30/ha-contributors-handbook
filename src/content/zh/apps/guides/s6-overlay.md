---
title: 使用 S6 覆盖运行服务
description: 基础镜像如何使用 S6 覆盖启动你的应用。单次和长时间运行的服务、依赖项、停止容器的完成脚本以及环境。
sidebarLabel: 使用 S6 覆盖运行服务
order: 2
---


# 使用 S6 覆盖运行服务 {#run-services-with-s6-overlay}
每个 Home Assistant 基础镜像都以 [S6 overlay](https://github.com/just-containers/s6-overlay) 作为其初始化系统开头。它是容器中的第一个进程：运行你的设置步骤，启动你的程序，在它们崩溃时重启它们，并在应用停止时按顺序关闭所有内容。本指南说明了它在应用中如何工作，以及如何像 [hassio-addons/app-example](https://github.com/hassio-addons/app-example) 那样设置你的服务。

所有这些都是关于 S6 overlay 版本 3 的，这是当前基础镜像中的版本。

## 为什么应用程序使用它 {#why-apps-use-it}
一个应用程序通常需要多个进程。你的程序前面有一个使用 nginx 的网页界面，旁边有一个数据库，或者在程序启动前需要写配置文件的步骤。Docker 每个容器只运行一个命令，而 S6 overlay 可以运行多个命令，并且顺序正确。

它还做了一个好的进程1应该做的事情：清理僵尸进程、传递信号，并给容器一个有意义的退出代码。S6 overlay 项目这样描述它的策略：一个容器只做一件事情，当这件事情失败时，容器也应该失败。这非常适合应用程序。当你的容器因错误停止时，Supervisor 的守护进程会监控到它并重启你的应用程序。

## 基础镜像的设置内容 {#what-the-base-images-set-up}
基础镜像安装了 S6 覆盖层，并将 `/init` 设置为入口点。请保留该入口点：不要设置你自己的 `ENTRYPOINT`。要启动你的程序，可以将其作为 `CMD` 提供，或者向镜像中添加服务定义。`/init` 会同时启动两者，参见 [启动应用的三种方式](/apps/guides/s6-overlay#three-ways-to-start-your-app)。

在 `config.yaml` 中，设置 `init: false`。S6 覆盖层必须作为进程 1 运行。使用默认的 `init: true` 时，Docker 会在其前面放置自己的 init 进程，容器会立即以 `s6-overlay-suexec: fatal: can only run as pid 1` 停止。

基础镜像还为 S6 覆盖层设置了一些环境变量：| 变量 | 基础镜像中的值 | 功能 |
| --- | --- | --- |
| `S6_BEHAVIOUR_IF_STAGE2_FAILS` | `2` | 当设置步骤或一次性服务失败时停止容器。S6覆盖的默认值 `0` 会静默继续。 |
| `S6_CMD_WAIT_FOR_SERVICES` | `1` | 在启动 `CMD` 之前，等待 `/etc/services.d` 中的服务准备就绪。 |
| `S6_CMD_WAIT_FOR_SERVICES_MAXTIME` | `0` | 启动服务没有时间限制。这也是 3.1.6.2 之后版本的 S6 覆盖默认值；在该版本之前，会在五秒后放弃。 |
| `S6_SERVICES_READYTIME` | `50` | 检查 `/etc/services.d` 中的服务是否就绪前的等待时间（毫秒）。仅 Home Assistant 基础镜像会将此值设置为 S6 覆盖默认值。 |Home Assistant 基础镜像和 Home Assistant Community Apps 的基础镜像也会在 `/usr/bin` 中安装可选链接。这就是为什么带有 `#!/usr/bin/with-contenv` 的脚本仍然可以工作，同时旁边还有 S6 覆盖版本 3 使用的 `#!/command/with-contenv`。

Home Assistant Community Apps 的基础镜像增加了两个自身的瞬时服务：一个在应用启动时记录应用名称、版本和系统的横幅，另一个根据 `log_level` 选项设置 Bashio 日志级别。Home Assistant 基础镜像没有这些功能。

## 启动应用程序的三种方式 {#three-ways-to-start-your-app}
S6 overlay 提供了三种运行程序的方式。选择一种即可。

| 方式 | 位置 | 何时使用 |
| --- | --- | --- |
| `CMD` | `CMD` 在 `Dockerfile` 中 | 一个程序，当程序停止时应用也停止。用于 [你的第一个应用](/apps/first-app)。 |
| 传统服务 | `/etc/cont-init.d/` 和 `/etc/services.d/` | 仍然受支持。许多现有应用使用它，包括 [home-assistant/apps-example](https://github.com/home-assistant/apps-example)。 |
| s6-rc 服务 | `/etc/s6-overlay/s6-rc.d/` | S6 overlay 推荐的格式。支持服务之间的依赖关系。用于 [hassio-addons/app-example](https://github.com/hassio-addons/app-example)。 |

在传统格式中，`/etc/cont-init.d/` 中的可执行脚本会依次运行，然后才启动服务。`/etc/services.d/` 中的每个文件夹都是一个服务，包含一个 `run` 脚本和一个可选的 `finish` 脚本。对于简单应用，这样的方式完全可以使用。本指南的其余部分是关于 s6-rc 格式的。它完成了传统格式所做的一切，而且你可以指定某个启动在另一个之后。

## s6-rc 布局 {#the-s6-rc-layout}
你的服务定义放在应用程序的 `rootfs` 文件夹中，`Dockerfile` 会使用 `COPY rootfs /` 将其复制到镜像中。这是 Home Assistant 社区应用示例应用的布局，包括一个设置步骤和两个程序：

```text
rootfs/etc/s6-overlay/
├── s6-rc.d/
│   ├── init-example/
│   │   ├── dependencies.d/
│   │   │   └── base
│   │   ├── run
│   │   ├── type
│   │   └── up
│   ├── example1/
│   │   ├── dependencies.d/
│   │   │   └── init-example
│   │   ├── finish
│   │   ├── run
│   │   └── type
│   └── example2/
│       ├── dependencies.d/
│       │   └── example1
│       ├── finish
│       ├── run
│       └── type
└── user-bundles.d/
    └── user/
        └── contents.d/
            ├── example1
            ├── example2
            └── init-example
```

`s6-rc.d` 中的每个文件夹都是一个服务。文件夹的名称就是服务的名称。里面放什么取决于服务的类型。

### 类型文件 {#the-type-file}
`type` 包含一个单词，`oneshot` 或 `longrun`，然后是换行符：

- **oneshot** 会运行一次然后退出。用于设置：写配置文件、创建文件夹、检查选项。
- **longrun** 是一个持续运行的程序。S6 会监督它，并在它退出时重新启动它。

你的主程序是一个 longrun。所有在它之前必须发生的事情，都应该是 oneshot 类型。

### 长期运行的服务 {#a-longrun-service}
长期运行的服务需要一个 `run` 脚本。它会被执行，因此需要一行 shebang 并且必须可执行：

```bash
#!/command/with-contenv bashio
# rootfs/etc/s6-overlay/s6-rc.d/example1/run {#rootfsetcs6-overlays6-rcdexample1run}
bashio::log.info "Starting Example1..."

exec /usr/bin/example1.sh
```

这里有两个细节很重要：

- 用 `exec` 启动你的程序。然后程序会替换脚本，因此 S6 直接监督你的程序本身，而不是它周围的 shell。
- 保持你的程序在前台运行。一个进入后台的程序在 S6 看来已经退出，S6 会一遍又一遍地重新启动它。S6 overlay README 因此使用 `nginx -g "daemon off;"` 来运行 nginx。

长期运行的服务还可以有一个 `finish` 脚本，它会在程序每次退出时执行。参见 [服务失败时停止容器](/apps/guides/s6-overlay#stop-the-container-when-a-service-fails) 。

### 一次性服务 {#a-oneshot-service}
一次性服务需要一个 `up` 文件。这个文件不是脚本：它包含一行命令，S6 使用 execline 解析器读取它。最简单的使用方法是将它指向一个脚本：

```text
/etc/s6-overlay/s6-rc.d/init-example/run
```

然后将你的设置放在该脚本中，并使其可执行：

```bash
#!/command/with-contenv bashio
# rootfs/etc/s6-overlay/s6-rc.d/init-example/run {#rootfsetcs6-overlays6-rcdinit-examplerun}
bashio::log.info "Writing the configuration..."

mkdir -p /data/config
```

脚本的名称 `run` 只是示例应用的一个约定。对于一次性服务，S6 只查看 `up`，以及可选的 `down`，该文件在应用停止时运行。

如果一次性服务失败，基础镜像会因为 `S6_BEHAVIOUR_IF_STAGE2_FAILS=2` 而停止容器。因此，一次性服务也是检查选项的地方：当 `bashio::config.require` 退出时，你的应用会在日志中以清晰的消息停止。

### 依赖关系 {#dependencies}
服务的 `dependencies.d` 文件夹中为每个必须先启动的服务保存了一个空文件。在示例中：

- `init-example` 依赖于 `base`。这是一个 S6 overlay 本身的捆绑包，它包含了容器的基本设置。S6 overlay 建议每个服务都依赖于 `base`，无论是直接依赖还是通过其他服务。否则，服务可能在容器完全设置好之前启动。
- `example1` 依赖于 `init-example`，因此它在设置步骤完成后才启动。
- `example2` 依赖于 `example1`。

S6 按照该顺序启动服务。当应用停止时，它按相反顺序停止服务：`example2` 最先停止，`base` 最后停止。

### 用户捆绑包 {#the-user-bundle}
服务只有在它位于`user`捆绑包中时才会启动。将一个空文件以服务名称命名并添加到`user-bundles.d/user/contents.d/`中。如果忘记了，服务永远不会启动，也不会出现任何错误。

## 当服务失败时停止容器 {#stop-the-container-when-a-service-fails}
S6 每次退出时都会重新启动 longrun。这并不总是你想要的。如果你的程序崩溃，通常最好停止整个容器：Supervisor 会检测到容器已停止，如果用户启用了看门狗，它会重新启动应用程序。

为此，可以向服务添加 `finish` 脚本。每次程序退出时，S6 都会运行该脚本，并传入两个参数：

- `$1`：程序的退出代码，如果是信号终止，则为 `256`。
- `$2`：信号编号，如果有的话。

脚本决定接下来发生的事情。要停止容器，它会将容器应该返回的退出代码写入 `/run/s6-linux-init-container-results/exitcode`，然后运行 `/run/s6/basedir/bin/halt`。这是示例应用的 `finish` 脚本，略有缩短：

```bash
#!/command/with-contenv bashio
# rootfs/etc/s6-overlay/s6-rc.d/example1/finish {#rootfsetcs6-overlays6-rcdexample1finish}
readonly results="/run/s6-linux-init-container-results/exitcode"
readonly exit_code_service="${1}"
readonly exit_code_signal="${2}"
exit_code_container=$(<"${results}")

bashio::log.info "Service example1 exited with code ${exit_code_service}"

if [[ "${exit_code_service}" -eq 256 ]]; then
  

# Killed by a signal. Keep the exit code of the first service that failed. {#the-container-environment}
  if [[ "${exit_code_container}" -eq 0 ]]; then
    echo $((128 + exit_code_signal)) > "${results}"
  fi

  

# SIGTERM means the container is stopping: take everything down. {#tune-s6-overlay}
  [[ "${exit_code_signal}" -eq 15 ]] && exec /run/s6/basedir/bin/halt

elif [[ "${exit_code_service}" -ne 0 ]]; then
  

# The program crashed: stop the container with its exit code. {#common-mistakes}
  if [[ "${exit_code_container}" -eq 0 ]]; then
    echo "${exit_code_service}" > "${results}"
  fi

  exec /run/s6/basedir/bin/halt

else
  

# A clean exit: let S6 start it again. {#learn-more}
  bashio::log.info "Service example1 restarting..."
fi
````exit_code_container` 的检查会保留第一个退出代码。当一个服务崩溃且其他服务因此被停止时，容器仍然会以引发问题的服务的代码退出。

一个更简短的版本，来自 [home-assistant/apps-example](https://github.com/home-assistant/apps-example)，只在崩溃时停止，并让 S6 处理其他所有事务：

```bash
#!/usr/bin/env bashio

if [[ "${1}" -ne 0 ]] && [[ "${1}" -ne 256 ]]; then
  bashio::log.warning "Halt app with exit code ${1}"
  echo "${1}" > /run/s6-linux-init-container-results/exitcode
  exec /run/s6/basedir/bin/halt
fi
```

## 容器环境 {#容器环境}
S6 使用最小环境启动每个服务和 `CMD`。容器的变量，比如 `SUPERVISOR_TOKEN` 以及你 `config.yaml` 中来自 `environment` 的变量，会被分开。`with-contenv` 会在运行你的脚本之前加载它们。

因此，启动每个与 Supervisor 交互的脚本时都要使用 `#!/command/with-contenv bashio`。这包括每个使用 [Bashio](/apps/bashio) 读取选项的脚本，因为 `bashio::config` 会从 Supervisor API 获取它们。

一个一次性脚本还可以为之后的服务添加变量。将值写入以变量命名的文件中，位于 `/var/run/s6/container_environment/`。Home Assistant Community Apps 的基础镜像就是以这种方式设置 `LOG_LEVEL` 的：

```bash
echo -n "${log_level}" > /var/run/s6/container_environment/LOG_LEVEL
```

之后每个以 `with-contenv` 开始的脚本都能看到新的值。

## Tune S6 覆盖层 {#tune-s6-覆盖层}
S6 覆盖层比基础镜像读取更多的环境变量。可以在你的 `Dockerfile` 中使用 `ENV` 设置它们。一些在应用中有用的变量：

| 变量 | 默认值 | 作用 |
| --- | --- | --- |
| `S6_VERBOSITY` | `2` | S6 在启动和停止时记录日志的多少。`1` 仅记录警告和错误，`0` 仅记录错误。 |
| `S6_KILL_GRACETIME` | `3000` | S6 在关机时等待的毫秒数，然后才终止未停止的进程。 |
| `S6_SERVICES_GRACETIME` | `3000` | S6 等待 `/etc/services.d` 中的服务停止的毫秒数。 |
| `S6_KILL_FINISH_MAXTIME` | `5000` | `/etc/cont-finish.d` 中的脚本在关机时可能花费的毫秒数。 |

完整列表请参阅 [S6 overlay README](https://github.com/just-containers/s6-overlay#customizing-s6-overlay-behaviour)。

## 常见错误- **`init: true`。** 容器会在 `can only run as pid 1` 停止。在 `config.yaml` 中设置 `init: false`。 {#常见错误-init-true。-容器会在-can-only-run-as-pid-1-停止。在-configyaml-中设置-init-false。}
- **不可执行的脚本。** S6 覆盖版本 3 会执行脚本，而不是将它们传递给 shell。在 Git 中使它们可执行，或在 `Dockerfile` 中为它们添加 `RUN chmod a+x`。
- **Windows 行结尾。** 使用 CRLF 行结尾保存的脚本无法启动，通常会出现一个根本不提及行结尾的错误。请使用 LF 保存脚本。
- **没有 `with-contenv`。** 脚本没有 `SUPERVISOR_TOKEN`，并且对 Supervisor 的每个 Bashio 调用都会失败，包括 `bashio::config`。
- **用户包中缺少服务。** 它永远不会启动。在 `user-bundles.d/user/contents.d/` 中为它添加一个空文件。
- **`up` 文件中的脚本。** `up` 只包含一条命令行。将脚本放入自己的文件中，并将 `up` 指向该文件。

- **一个会派生子进程的守护进程。** S6 认为它已经退出，然后再次启动它。在前台运行它。
- **不依赖 `base`。** 服务可能在容器准备好之前启动。添加 `dependencies.d/base`，或者依赖一个已经做到的服务。
- **`host_pid: true`。** S6 覆盖在主机的 PID 命名空间中不起作用。

## 了解更多 {#了解更多}
- [S6 overlay README](https://github.com/just-containers/s6-overlay)：初始化阶段、传统格式、日志记录以及每个环境变量。
- [s6-rc 源格式](https://skarnet.org/software/s6-rc/s6-rc-compile.html#source)：服务定义可以拥有的每个文件。
- [构建一个真实应用](/apps/build-a-real-app)：Home Assistant 社区应用的示例应用，逐步指导。
