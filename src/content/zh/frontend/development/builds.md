---
title: 构建
description: 制作前端的制作构的可行性,或运行在真实的Home Assistant上,没有开发设置的pull request的构件.
order: 6
---

# 构建 {#builds}

大多数时候,开发服务器都是你所需要的. 这些是用于其他时间的:当您在前端如何包装时,或者当您想要在真实的Home Assistant上测试一个pull request时.

## 做一个生产建设 {#make-a-production-build}

```shell
pnpm build
```

这使得生产完全建成了`hass_frontend/`:现代建筑和遗产建筑、精密化和压缩,并有服务工人。 这需要一段时间。

当您只需要现代构建, 例如比较捆绑大小或测量性能时, 跳过遗留的 :

```shell
pnpm build --modern
```

生产建筑接受与`--background`,`--status`,`--logs`,和`--stop`旗帜相同的`--background`,[开发服务器](/frontend/development/run#keep-a-server-running-in-the-background). 构建和开发服务器不能同时运行,因为它们会写入同一个文件夹.

### 使用您在 Home Assistant 中的构建 {#use-your-build-in-home-assistant}

要用您的构建来运行 Core 而不是它通常安装的前端, 请将 [前端仓库](https://github.com/home-assistant/frontend) 安装为 Python 软件包,并告诉 Home Assistant 不替换它:

```shell
pip3 install -e /path/to/frontend --config-settings editable_mode=compat
hass --skip-pip-packages home-assistant-frontend
```

## 尝试 pull request {#try-out-a-pull-request}

您可以自行运行任何打开的前端 pull request 的构建, 无需克隆或构建任何东西 。 这在每一个安装类型上都有效,包括Home Assistant OS. 检查一个修补是否在您的硬件,浏览器或设置上有效是有用的.

### 创建 GitHub 令牌 {#create-a-github-token}

派代表出席 Home Assistant 从 GitHub 下载该建筑, 这需要一个符号 :

1. In GitHub, go to [** 安排** > ** 开发者设置** > ** 个人访问标志** > ** 罚款的代币**](https://github.com/settings/personal-access-tokens).
2. 选择**Generate新令牌**,并给它一个您识别的名称,如"Home Assistant前端测试".
3. 选个短寿,如九十日.
4. **聪库**,选择**公共库**。 留空权限.
5. 选择 ** Generate 令牌 ** 并复制它 。 你不会再看到它。

### 配置 Home Assistant {#configure-home-assistant}

将 pull request 和您的令牌的号码添加到您的 Home Assistant 的 `configuration.yaml` 中, 并重新启动它 :

```yaml
frontend:
  development_pr: 12345
  github_token: !secret github_token
```

箴言本身保存在 `secrets.yaml` 中, 永远不要在您共享的文件中 。

在启动时, Home Assistant 下载 pull request 的构建并使用它, 而不是内置的前端 。 它保存着副本,之后它重新开始检查pull request是否有尤其在新的承诺,如果有的话下载新的构建. 如果下载失败, Home Assistant 回到内置的前端并记录原因 。

如果 `development_repo` 被设定, 那将胜出, 而 pull request 会被忽略 。

要返回,请移除 我们走吧。 Home Assistant 我们走吧。

### 限制 {#limits}

- pull request  闭嘴 !
- 这些建筑要维持7天 后须再造. 作者可以通过更新分支来做到这一点,例如将`dev`合并到其中. 如果你不是作者,请问他们。
- Vicente. 这是测试用的 Vicentey. 别忘了穿
