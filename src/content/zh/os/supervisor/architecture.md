---
title: Supervisor 架构
description: '{H0这方面的工作}代码是如何组织起来的,是如何开始的,以及更新和备份是如何在它内部工作的.'
sidebarLabel: 架构
sidebarGroup: 工作原理
order: 1
---

# Supervisor 架构 {#supervisor-architecture}

Supervisor是一个 async Python 过程, 建立在 Ayncio 和 aiohttp 上 。 它通过它的API与Docker交谈,通过D-Bus与主机交谈,并通过HTTP与其他一切交谈. 这页是代码的地图,所以你知道该看哪里.

## CoreSys: 达到所有对象的一个对象 {#coresys-one-object-to-reach-everything}

Supervisor 中的每个管理器都会挂上一个对象, `CoreSys` 在[`supervisor/coresys.py`](https://github.com/home-assistant/supervisor/blob/main/supervisor/coresys.py) 。 需要它继承 `CoreSysAttributes` 的类, 并通过 `sys_*` 属性到达其它部分 :

```python
from ..coresys import CoreSys, CoreSysAttributes

class Example(CoreSysAttributes):
    """Do something with the system."""

    def __init__(self, coresys: CoreSys) -> None:
        """Initialize the example."""
        self.coresys = coresys

    async def check(self) -> bool:
        """Check if Core needs an update."""
        return self.sys_homeassistant.need_update
```

您将使用的大部分管理器  :

| 财产 | 它管理着提供任何 | 的 |
| --- | --- | --- |
| `sys_homeassistant` | Home Assistant Core | [`supervisor/homeassistant/`](https://github.com/home-assistant/supervisor/tree/main/supervisor/homeassistant) |
| `sys_apps` | 已安装的应用程序 | [`supervisor/apps/`](https://github.com/home-assistant/supervisor/tree/main/supervisor/apps) |
| `sys_store` | 应用程序存储器 | [`supervisor/store/`](https://github.com/home-assistant/supervisor/tree/main/supervisor/store) |
| `sys_backups` | 备份和恢复 | [`supervisor/backups/`](https://github.com/home-assistant/supervisor/tree/main/supervisor/backups) |
| `sys_plugins` | 插件 | [`supervisor/plugins/`](https://github.com/home-assistant/supervisor/tree/main/supervisor/plugins) |
| `sys_os` | Home Assistant OS,其更新和数据磁盘 | [`supervisor/os/`](https://github.com/home-assistant/supervisor/tree/main/supervisor/os) |
| `sys_host` | 主机的网络、服务、日志和硬件信息 | [`supervisor/host/`](https://github.com/home-assistant/supervisor/tree/main/supervisor/host) |
| `sys_dbus` | D- Bus 系统客户端, 网络管理器, RAUC, OS代理 | [`supervisor/dbus/`](https://github.com/home-assistant/supervisor/tree/main/supervisor/dbus) |
| `sys_docker` | 嵌入容器、图像和 `hassio` 网络 | [`supervisor/docker/`](https://github.com/home-assistant/supervisor/tree/main/supervisor/docker) |
| `sys_updater` | 现有版本 | [`supervisor/updater.py`](https://github.com/home-assistant/supervisor/blob/main/supervisor/updater.py) |
| `sys_jobs` | 运行中的工作 | [`supervisor/jobs/`](https://github.com/home-assistant/supervisor/tree/main/supervisor/jobs) |
| `sys_resolution` | 问题、建议和系统保健 | [`supervisor/resolution/`](https://github.com/home-assistant/supervisor/tree/main/supervisor/resolution) |
| `sys_api` | REST API (法语) | [`supervisor/api/`](https://github.com/home-assistant/supervisor/tree/main/supervisor/api) |

直接为 Docker 或 D- Bus 库使用这些工具。韵律:用 `self.sys_run_in_executor()` 运行屏蔽电话。

## 如何开始 {#how-it-starts}

Supervisor 通过状态移动, 定义出来了`CoreState` 在[`supervisor/const.py`](https://github.com/home-assistant/supervisor/blob/main/supervisor/const.py) :

1. **初始化**:创建`CoreSys`和每个管理器.
2. **设置**:负载配置,连接D-Bus和Docker,并评价系统.
3. **startup**:如果有较新的版本,并且自动更新正在启动,则更新自己,启动插件,然后在启动阶段开始Core和应用程序.
4. [运行**: 一切都好。 计划任务和健康检查。
5. **冻结**,**shutdown**,**stoping**,**close**:在一个冻结系统的备份中,在下行途中.

许多检查和工作只在某些州进行。 这就是为什么存在像`running`这样的工作条件。

在启动期间,Supervisor也标记了被启动的OS槽是好的. 直到它生效, 卸货者认为OS更新未经证实。 见[更新系统](/os/operating-system/update-system).

## 预定任务 {#scheduled-tasks}

百度百科,百度百科,百度百科,百度百科,百度百科,百度百科,百度百科,百度百科,百度百科,百度百科,百度百科,百度百科,百度百科,百度百科,百度百科,百度百科,百度百科,百度百科,百度百科,百度百科,百度百科,百度百科,百度百科,百度百科,百度百科,百度百科,百度百科,百度百科,百科,百度百科,百科,百科,百科,百科,百科,百科,百科,百度百科停止回应时,百科,百科,百科,百度百科,百科,百科,百科,百度百科百科,百科百科百科百科百科,百科百科百科百科,百科百科百科百科百科百科百科百科百科百科百科百科百科百科 解决中心增加了小时健康检查。 见[羚羊和猪笼草](/os/supervisor/resolution-center)。

## 最新情况 {#updates}

Supervisor从`version.home-assistant.io/<channel>.json`读取可用的版本,保存在[家庭畸各种不同的服务](https://github.com/home-assistant/version)寄存器中. 该频道为`stable`,`beta`或`dev`,用户可以用`ha supervisor options --channel`更改.

- ** Supervisor 默认自动更新。 当它运行的版本比最新版本老时,它拉动新图像并重启.
- ** 自动更新。
- QQH0}**,**apps**,以及QQH1}**在用户要求时更新,或者在用户打开自动更新一个app时更新.

A Core更新可以先进行部分备份. 更新后, Supervisor 检查核心开始 。 否则,Supervisor卷回上一个版本,在配置文件夹中将失败开始的日志写入`home-assistant-rollback.log`,并提出`update_rollback`问题.

## 备份 {#backups}

备份是一个未压缩的tar文件,其中包含 `backup.json` 描述它, 以及每个部分的一个内存归档: Home Assistant Core 及其配置, 每个应用程序, 每个文件夹( `share`, `ssl`, `media` 和本地应用程序), 以及 Supervisor 自己的配置 。 带有密码,内部档案被加密为[安全塔](https://github.com/home-assistant-libs/securetar).

一个完整的备份有每一个部分,一个部分备份被选中的部分. 备份默认在数据分区上转到`/backup`, 或者转到网络存储挂载 。 Home Assistant Core的`backup`整合基于此之上,处理上传备份到其他地方.

Apps可以说明他们希望如何被备份:停止,或运行时,使用前后命令. 当备份运行时, Supervisor 可以冻结 Core, 所以其数据库处于一致状态 。

## The API {#the-api}

[`supervisor/api/`](https://github.com/home-assistant/supervisor/tree/main/supervisor/api) 每个区域有一个模块, 如`backups.py` 或 `network.py` 。 路线注册于[`supervisor/api/__init__.py`](https://github.com/home-assistant/supervisor/blob/main/supervisor/api/__init__.py). Handlers 使用 `@api_process` 装饰器, 它将 Supervisor 错误转换成适当的错误响应, 用 `api_validate()` 验证输入 。 [`supervisor/api/middleware/`](https://github.com/home-assistant/supervisor/tree/main/supervisor/api/middleware)中的中间软件检查每个呼叫者的符号和角色. 每个端点及其有效载荷和反应都记录在[Supervisor API](/apps/supervisor-api)参考文献中。

当您更改 API 时, [(a) 营养水平](https://github.com/home-assistant/cli) 和 [Python 客户端库](https://github.com/home-assistant-libs/python-supervisor-client) 经常需要匹配的更改 。 pull request Supervisor 的模板询问这两个问题 。
