---
title: 运行前端
description: 运行您的开发前端 Home Assistant 或 Home Assistant 您已经拥有 。
order: 2
---

# 运行前端 {#run-the-frontend}

前端需要一个 Home Assistant Core 来和它说话 。 有两种方式可以连接它们:

- ** 核心服务于前端。 ** 您运行一个开发核心并告诉它使用您的 [前端仓库](https://github.com/home-assistant/frontend) 而不是内置的 。 这就是它在生产中的运作方式,所以一切工作都奏效,包括登录页和登机.
- ** 您的前端连接到一个核心。 ** 你亲自为前端服务,并指向任何Home Assistant,甚至跑家的人。 快速设置和离开 Home Assistant独自。 捕捉:有些部分,如登录页,总是来自你所连接的核心.

> [!CAUTION]
> 生产中永远不要使用开发模式. Home Assistant 快速地缓存前端 开发模式关闭了它,所以不需要在变化之间重启.

## 核心服务您的前端 {#core-serves-your-frontend}

景象开发笃信器将ẽ的前端构建到寄存器的`hass_frontend`文件夹中,并在保存时重建. 当 `development_repo` 的 `frontend` 集成点 的 `development_repo` 选项在您的寄存器中时, Core 为它服务 。

### 在前端的剪贴机上 {#in-the-frontend-devcontainer}

修饰者可以为你运行 Core:

1. 在终端中,运行`script/core`. 它第一次安装了Core的 `dev` 分支, 并创建了 `config` 文件夹 `development_repo` 已经设置了 `demo` , 和 `demo` 集成, 供一些实体玩 。 使用 `script/core -r <ref>` 安装另一个分支或标记, 或 `script/core -s` 跳过安装 。
2. 在第二个终端中,启动开发服务器:

```shell
   pnpm dev
   ```

3. 当日志说`Build done`时,打开`http://localhost:8124`.

### 以你自己的核心发展环境 {#with-your-own-core-development-environment}

如果您已经在 Core 上工作, 请将其配置指向您的前端克隆 。 在您的开发核心 `configuration.yaml` 中:

```yaml
frontend:
  development_repo: /path/to/frontend
```

如果路径错误或无法访问,前端不会加载. 然后启动Core,在前端寄存器中运行`pnpm dev`,并照常在端口8123上打开Home Assistant.

当您使用 Core 调试器时, 前端寄存器必须在容器内可见 。 通过这一观点添加到[核心储存库](https://github.com/home-assistant/core)中的[`.devcontainer/devcontainer.json`](https://github.com/home-assistant/frontend/blob/dev/.devcontainer/devcontainer.json)上架,并用**Dev容器重建容器:重建容器**:

```json
"mounts": [
  "source=/path/to/frontend,target=/workspaces/frontend,type=bind"
]
```

然后使用容器内的路径 `/workspaces/frontend`,用于 `development_repo` 。

> [!WARNING]
> 不要将 `mounts` 更改为 Core : 它有一个路径 。 此设置只有在容器建成时才被读取, 这样重建完成后您就可以取消它 。

[核心发展环境](/core/development/environment)解释如何建立核心本身。

## 您的前端连接到一个核心 {#your-frontend-connects-to-a-core}

`pnpm dev:serve` 构建前端并在8124端口上服务, 在`http://localhost:8123` 上连接到核心:

```shell
pnpm dev:serve
```

要连接到另一个 Home Assistant,请通过 `-c` 的 URL 。 它不必是一个开发版本:

```shell
pnpm dev:serve -c http://homeassistant.local:8123
```

Home Assistant必须接受您开发前端的请求。 将其地址添加到 `http` `configuration.yaml` Home Assistant 的 `configuration.yaml` 区域中, 您可以连接并重新启动它 :

```yaml
http:
  cors_allowed_origins:
    - http://localhost:8124
```

有几个事情要知道:

- 使用 `-p` 在另一个端口服务, 如 `pnpm dev:serve -p 8654` 。 将地址添加到 `cors_allowed_origins` 。
- 在Devcontainer内部,前端服务于容器中的8123号端口,这是你电脑上的8124号端口. 您用 `-c` 通过的 URL 由您的浏览器打开, 而不是由容器打开, 因此 `localhost` 表示您的计算机 。
- 前端记得您登录的 Home Assistant 。 当您更改 `-c` 时, 请先登录, 或者继续使用旧的 。

## 保持服务器在背景中运行 {#keep-a-server-running-in-the-background}

所有开发服务器都接受相同的旗帜来管理它们,而不保留终端开放:

| 旗帜 | 它会做什么 |
| --- | --- |
| `--background` | 启动服务器脱 我给你解开, 等待它准备好, 打印它的 URL 并处理 ID, 然后退出 。 |
| `--status` | 报告服务器是否运行 。 |
| `--logs` | 打印服务器日志 。 添加 `--follow` 继续观看 。 |
| `--stop` | 停止在背景中运行的服务器 。 |

例如:

```shell
pnpm dev:serve --background
pnpm dev:serve --logs --follow
pnpm dev:serve --stop
```

一次只能运行一个开发服务器或生产构建,因为他们共享构建输出. 开始第二场 告诉你哪个在跑 如何阻止它 寒冷的建筑要等180秒才能准备好 将 `HA_DEV_SERVER_TIMEOUT` 设定为数秒以更改它 。

当服务器在背景中运行时,其日志会写入`node_modules/.cache/ha-dev-server/`. 当脚本检测到一个编码代理启动时,一个普通的 `pnpm dev` 或 `pnpm dev:*` 自己去到背景, 所以它不会阻断代理. 设定 `HA_DEV_BACKGROUND=0` 将其保存在前景中 。

## 浏览器设置 {#browser-settings}

前端使用服务工和缓存,可显示变化后的旧建筑. 在您的浏览器的开发工具中 :

1. 在 **Network ** 标签上,启用 ** 残疾缓存**.
2. ** 申请** > ** 服务人员**,启用**网络通道**。

这些是Chrome和其他Chrome浏览器中的名称. 其他浏览器也有类似的设置.

## 看这堆东西 {#look-at-the-hass-object}

前端的每个部分都从一个对象得到数据,`hass`. 要查看里面的内容, 打开开发工具, 在 ** Elements ** 标签上选择 `<home-assistant>` 元素, 在控制台中运行 :

```js
$0.hass
```

这只是为了探索 在编码中,利用你的部分获得数据。 [对象和背景](/frontend/architecture/hass-and-contexts) 如何解释。
