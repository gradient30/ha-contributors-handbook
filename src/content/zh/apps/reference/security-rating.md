---
title: 安全评级
description: Supervisor 如何计算应用程序的安全评级，从1到8，以及哪些选择会使其上升或下降。
order: 5
---

# 安全评级 {#security-rating}

每个应用都有一个安全评分，在其页面上显示为1到8的数字。数字越高越好。用户在安装你的应用之前会查看这个评分，因此在发布之前值得检查一下。Supervisor 根据你的配置计算它（在 Supervisor 代码中为 [`rating_security`](https://github.com/home-assistant/supervisor/blob/main/supervisor/apps/utils.py)）。

## 计算方式 {#how-it-is-computed}

每个应用程序起始分数为5。然后：

| 条件 | 变动 |
| --- | --- |
| 加载了自定义的 AppArmor 配置文件 (`apparmor.txt`) | 1 |
| `apparmor: false` | -1 |
| `ingress: true` | 2 |
| 没有入口，但也没有主机网络且没有映射到主机的端口 | 2 |
| 没有入口，但 `auth_api: true`（且有主机网络或映射端口） | 1 |
| 在 `privileged` 中拥有 `BPF`、`CHECKPOINT_RESTORE`、`DAC_READ_SEARCH`、`NET_ADMIN`、`NET_RAW`、`PERFMON`、`SYS_ADMIN`、`SYS_MODULE`、`SYS_PTRACE` 或 `SYS_RAWIO` 的任意能力，或者 `kernel_modules: true` | -1，仅一次 |
| `hassio_role: manager` | -1 |
| `hassio_role: admin` | -2 |
| `host_network: true` | -1 |
| `host_pid: true` | -2 |
| `host_uts: true` 与 `SYS_ADMIN` 一起出现在 `privileged` 中 | -1 |
| `docker_api: true` 或 `full_access: true` | 分数为1，不论其他情况 |

结果保持在1到8之间。只有入口、无暴露和 `auth_api` 奖励中的一项计入，按此顺序优先。

需要注意的几点事项：- AppArmor 奖励在您的配置文件加载后才计算，这发生在应用程序安装时。在此之前，应用商店显示的评分不包含该奖励。
- 在 `config.yaml` 中，主机端口为 `null` 的端口默认是关闭的，并不算作已映射。评分查看的是您的配置，而不是用户开启的端口。
- 代码对已签名镜像有奖励，但该奖励未被使用：今天没有应用获得该奖励。
- `AUDIT_WRITE`、`MKNOD`、`SETFCAP`、`IPC_LOCK`、`SYS_NICE`、`SYS_RESOURCE` 和 `SYS_TIME` 不会改变评分。

## 示例 {#example}

一个带有入口、自定义 AppArmor 配置文件且没有其他权限的应用得分为 5 2 1 = 8。相同的应用有 `host_network: true` 和 `NET_ADMIN` 得分为 5 2 1 - 1 - 1 = 6。

要提高应用的评分，请参见 [保护您的应用](/apps/guides/security)。
