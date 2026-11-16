---
title: 调试为解决 Supervisor
description: 将 Python 调试器附加到运行中的 Supervisor , 本地或远程设备上, 并查找其日志 。
sidebarLabel: 调试为解决 Supervisor
sidebarGroup: 指南
order: 2
---

# 调试为解决 Supervisor {#debug-the-supervisor}

Supervisor的船有[调试](https://github.com/microsoft/debugpy),所以你可以将Visual Studio代码调试器附在其中,设置断点,并步入代码. 这在开发容器 和一个真正的设备。

## 打开调试模式 {#turn-on-debug-mode}

调试器仅在调试模式启动时开始 。 除错模式在启动时 51. 因此在您更改后重新启动 Supervisor :

```shell
ha supervisor options --debug=true
ha supervisor restart
```

写`=true`出来。 CLI将得到一个赤色的 `--debug` 读作 `false`, 因此它会关闭调试模式 。

Supervisor 现在听一个调试器在端口 33333. 要调试启动时发生的情况, 也添加 `--debug-block=true` 。 Supervisor 然后等待一个调试器被附着后再继续 。

再次用 `ha supervisor options --debug=false` 关闭它 。

## 附加调试器 {#attach-the-debugger}

寄存器对此有一个启动配置, QQH0} 远程调试**, 在 [`.vscode/launch.json`](https://github.com/home-assistant/supervisor/blob/main/.vscode/launch.json) 中 :

```json
{
  "name": "Supervisor remote debug",
  "type": "python",
  "request": "attach",
  "port": 33333,
  "host": "172.30.32.2",
  "pathMappings": [
    {
      "localRoot": "${workspaceFolder}",
      "remoteRoot": "/usr/src/supervisor"
    }
  ]
}
```

`172.30.32.2`是Supervisor在`hassio`网络上的地址,它从开发容器内部工作. 在 **Run 和debug ** 视图中选择配置,然后启动。

## 调试远程设备 {#debug-a-remote-device}

在设备上, `hassio` 网络无法从您的计算机中到达 。 ** Remote ptvsd 调试器** app将主机的33333 移植到 Supervisor :

1. 添加 [开发应用程序存储器](https://github.com/home-assistant/apps-development) 到设备的应用商店 。
2. 安装并启动 ** Remote ptvsd 调试器** app.
3. 如上, 打开调试模式 。
4. 在您的发射配置中, 将 `host` 设定为设备的 IP 地址 。

确保工作空间中的代码与设备上的版本匹配. 否则,断点最终会落错线.

## 日志 {#logs}

以其中一种方式读取 Supervisor 的日志 :

```shell
# From the Home Assistant CLI {#from-the-home-assistant-cli}
ha supervisor logs

# From the host shell {#from-the-host-shell}
docker logs -f hassio_supervisor
```

详情请以 `ha supervisor options --logging debug` 提高日志级别 。

如果 Supervisor 根本没有开始, 请查看启动它的服务 : `journalctl -u haos-supervisor` 在主机外壳上 。 解释如何到达那里。 当Supervisor下架时,4357号港口上的观察者仍然显示其状态和日志.
