---
title: 保护你的应用
description: 保持你的应用程序及其运行的系统安全。尽量少请求权限，添加 AppArmor 配置文件，选择正确的 API 角色，并在登录时使用 Home
  Assistant。
order: 9
---


# 保护你的应用 {#secure-your-app}
你的应用程序运行在用户的家中，就在他们的摄像头、门锁和报警器旁。用户对你有信任。Supervisor 通过将应用程序隔离，并向用户显示你的应用程序的 [安全评级](/apps/reference/security-rating) 来提供帮助。本指南涵盖了你可以做些什么来保持该评级高并将风险降低。

## 尽量少请求权限 {#ask-for-as-little-as-possible}
最有效的措施不花一分钱：只请求你的应用程序所需的访问权限。

- 除非必要，不要在主机网络上运行。
- 将文件夹映射为只读，除非你的应用程序需要写入它们。
- 优先选择 `device` 选项或 `devices`，而不是 `uart`、`usb` 或 `full_access`。
- 仅添加 `privileged` 中你的软件真正使用的功能。
- 只请求你调用的 API 访问权限，并且使用最低可行的角色。
- 对于你的网页界面，使用 ingress，而不是暴露端口。

## 保护模式 {#protection-mode}
每个应用默认都启用**保护模式**。启用该模式时，Supervisor 不会授予 `full_access`、`docker_api` 或 `host_pid`，即使你的 `config.yaml` 请求它们。用户可以在应用页面上关闭保护模式，界面会在他们操作时发出警告。通过 Supervisor API，只有具有 `admin` 角色的调用者才能更改它。这包括拥有 `hassio_api: true` 和 `hassio_role: admin` 的应用，无论是针对自身还是针对其他应用。

如果你的应用需要关闭保护模式，请在文档中说明，并解释原因。

## AppArmor {#apparmor}
AppArmor 限制了容器中进程的行为：它们可以读取和写入哪些文件，可以运行哪些程序，以及可以发送哪些信号。每个应用程序默认使用 Docker 的默认 AppArmor 配置文件，除非你设置 `apparmor: false`（这会降低安全等级）。

在你的应用程序文件夹中放置一个 `apparmor.txt`，Supervisor 会将其作为你的应用程序的配置文件加载。为你的应用程序量身定制的配置文件是强有力的第二道防线：即使攻击者发现了你的软件漏洞，他们也只能执行配置文件允许的操作。同时，它还会提高安全等级。该文件必须恰好包含一个顶级 `profile` 行。Supervisor 会在加载配置文件时将该行上的名称替换为你的应用程序的 ID，就像 `local_example` 一样，因此请使用你的应用程序的 slug 作为名称。这个示例适用于一个 slug 为 `example` 的应用程序，它在带有 S6 覆盖层的 `/usr/bin/my_program` 上运行。`/etc/services.d`、`/etc/cont-init.d` 和 `/etc/cont-finish.d` 的规则涵盖了传统服务格式，而 `/etc/s6-overlay` 的规则涵盖了 [s6-rc 格式](/apps/guides/s6-overlay#the-s6-rc-layout)。该规则包括写入权限：如果你的应用程序将 `user` 包保存在 `s6-rc.d` 而不是 `user-bundles.d` 中，S6 覆盖层将在启动时写入该文件夹。

```text
#include <tunables/global>

profile example flags=(attach_disconnected,mediate_deleted) {
  #include <abstractions/base>

  

# Capabilities {#api-roles}
  file,
  signal (send) set=(kill,term,int,hup,cont),

  

# S6 overlay {#use-home-assistant-users}
  /init ix,
  /bin/** ix,
  /usr/bin/** ix,
  /run/{s6,s6-rc*,service}/** ix,
  /package/** ix,
  /command/** ix,
  /etc/services.d/** rwix,
  /etc/cont-init.d/** rwix,
  /etc/cont-finish.d/** rwix,
  /etc/s6-overlay/** rwix,
  /run/{,**} rwk,
  /dev/tty rw,

  

# Bashio {#sign-your-images}
  /usr/lib/bashio/** ix,
  /tmp/** rwk,

  

# Options and other files of the app {#options-and-other-files-of-the-app}
  /data/** rw,

  

# Run the program in its own, stricter profile {#run-the-program-in-its-own-stricter-profile}
  /usr/bin/my_program cx -> my_program,

  profile my_program flags=(attach_disconnected,mediate_deleted) {
    #include <abstractions/base>

    

# Receive signals from S6 overlay {#receive-signals-from-s6-overlay}
    signal (receive) peer=*_example,

    

# Files the program needs {#files-the-program-needs}
    /data/** rw,
    /share/** rw,
    /usr/bin/my_program r,
    /bin/bash rix,
    /bin/echo ix,
    /etc/passwd r,
    /dev/tty rw,
  }
}
```

为你自己的应用程序编写配置文件：1. 从示例开始。S6 覆盖部分对于使用基础镜像的每个应用都是相同的；如果你的启动脚本需要更多内容可以添加，但不要删除任何内容。
2. 如果你打包的软件附带 AppArmor 配置文件，请使用其进程的该配置文件。软件开发者提供的配置文件比你自己猜测的要好。
3. 否则，添加你已知的软件所需的访问权限，并在配置文件的标志中添加 `complain`。
4. 运行应用并使用所有功能。在抱怨模式下，AppArmor 会记录它本来会阻止的内容，而不是阻止它。在主机上用 `journalctl _TRANSPORT="audit" -g 'apparmor="ALLOWED"'` 阅读日志。
5. 添加缺失的内容，直到使用应用不再记录警告为止。
6. 移除 `complain`，这样 AppArmor 就会阻止其他所有内容。

每次更新软件时都重复此操作，因为新版本可能需要新的访问权限。

## API 角色 {#api-角色}
使用 `hassio_api: true`，你的应用可以调用 Supervisor API 超出基本端点的范围。`hassio_role` 决定了可以调用的范围：

| 角色 | 可以调用 |
| --- | --- |
| `default` | 所有 `info` 端点，如 `/supervisor/info` 或 `/addons/<app>/info` |
| `homeassistant` | 上述所有端点，以及所有 `/core` 端点 |
| `backup` | 上述 `info` 端点，以及所有 `/backups` 端点 |
| `manager` | API 大部分功能：应用、商店、备份、核心、主机、操作系统和插件。但不能访问应用的安全设置、清除数据盘或主机的 SSH 密钥 |
| `admin` | 所有功能，包括任何应用的保护模式，也包括它自身的保护模式 |

`manager` 和 `admin` 会降低安全等级，分别降低 1 和 2。它们适用于管理系统的应用，如终端或 Supervisor 的仪表板。没有 `hassio_api`，你的应用仍然可以使用它自己大部分的 `/addons/self` 端点（不包括 `security` 或 `update`）、`/info`、服务、发现和认证。请参阅 [与 Home Assistant 和 Supervisor 对话](/apps/guides/communication#the-supervisor-api)。

`homeassistant_api` 与这些角色是分开的：它控制对 Home Assistant Core API 代理在 `/core/api` 的访问。通过该代理，你的应用作为 Home Assistant 的管理员操作，因此它可以调用管理员可以执行的所有操作，包括管理用户。上面提到的角色对此没有限制。请参阅 [Home Assistant Core](/apps/guides/communication#home-assistant-core)。

## 使用 Home Assistant 用户 {#使用-home-assistant-用户}
如果你的应用有一个不通过入口的登录，请不要在应用选项中发明自己的带密码的用户数据库。请检查用户的 Home Assistant 凭证。添加 `auth_api: true`，并将用户名和密码发送到 Supervisor。在这里将你的令牌发送到 `X-Supervisor-Token` 头，而不是 `Authorization`：该端点将 `Authorization` 头读取为用户的 HTTP 基本身份验证，那里 `Bearer` 令牌会得到 `401`。

```bash
curl -sSL -X POST \
  -H "X-Supervisor-Token: ${SUPERVISOR_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"username": "jane", "password": "secret"}' \
  http://supervisor/auth
```

`200` 响应意味着凭证有效；其他任何响应都表示无效。该端点也接受表单数据，以及在 `Authorization` 头中使用用户凭证进行的 HTTP 基本身份验证。

使用入口时，通常不需要这个：Home Assistant 已经登录了用户，[用户头信息](/apps/guides/ingress#know-who-is-there) 会在入口会话中告诉你是谁。

## 为你的镜像签名 {#为你的镜像签名}
[构建器](/apps/guides/publishing) 的 `build-image` 和 `publish-multi-arch-manifest` 操作可以使用 Cosign 为你的镜像签名。签名让任何人都可以验证镜像是否来自你仓库的工作流。Supervisor 目前不会检查签名，签名也不会改变安全评级，但开启它成本很低。
