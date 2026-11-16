---
title: 工作
description: Supervisor 如何运行作为工作, 条件, 货币限制, 节奏, 以及客户可以遵循的进步 。
sidebarGroup: 它是如何运作的
order: 2
---

# 工作 {#jobs}

几乎所有 Supervisor 需要时间做的都是工作: 安装一个应用程序, 更新 Core, 制作备份 。 工作是与 `@Job` 装饰器的同步方法 。 装饰者处理很有可能在任何地方重复的东西:检查系统是否处于工作可能运行的状态,防止一次两次运行,并报告进度.

代码为[`supervisor/jobs/`](https://github.com/home-assistant/supervisor/tree/main/supervisor/jobs).

## 一个工作 {#a-job}

```python
from ..jobs.const import JobConcurrency, JobCondition
from ..jobs.decorator import Job

class HomeAssistantCore(JobGroup):
    @Job(
        name="home_assistant_core_update",
        conditions=[
            JobCondition.FREE_SPACE,
            JobCondition.HEALTHY,
            JobCondition.INTERNET_HOST,
        ],
        on_condition=HomeAssistantJobError,
        concurrency=JobConcurrency.GROUP_REJECT,
    )
    async def update(self, version: AwesomeVersion | None = None) -> None:
        """Update Home Assistant Core."""
```

此从 [`supervisor/homeassistant/core.py`](https://github.com/home-assistant/supervisor/blob/main/supervisor/homeassistant/core.py) 缩短 。 这些部分:

- `name`: 唯一横跨 Supervisor. 它出现在API和日志中.
- `conditions`:在工作开始前,什么必须是真实的。
- `on_condition`: 当一个条件失败时, 提高的例外 。 没有它,工作记录失败和返回。
- 强权: 强权:

## 条件 {#conditions}

条件定义为`JobCondition`在[`supervisor/jobs/const.py`](https://github.com/home-assistant/supervisor/blob/main/supervisor/jobs/const.py)中. 一些常见的:

| ụ nó 翎恣梢凛咀徘آ滔颐几句鸠凹 周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周 | 过时 |
| --- | --- |
| `healthy` | 系统不健康 |
| `free_space` | 数据磁盘有足够的空闲空间 |
| `internet_host`, `internet_system` | 主机或Supervisor本身有互联网 |
| `running` | Supervisor tube在运行状态中 |
| `haos` | 系统运行 Home Assistant OS |
| `os_agent` | 操作系统代理已可用 |
| `supervisor_updated` | Supervisor 运行最新版本 |
| `plugins_updated` | 每个插件运行其最新版本 |
| `auto_update` | 自动更新已打开 |
| `mount_available` | 主机支持网络存储挂载 |

对于调试,可以通过`ha jobs options --ignore-conditions <condition>`忽略条件. 一个系统,它被标记为不支持,有 `job_conditions` 理由 。 以 `ha jobs reset` 撤消它 。

## 货币和节奏 {#concurrency-and-throttling}

`JobConcurrency` 控制一个工作在运行时被调用时会发生什么 :

- `REJECT`: 马上失败。
- `QUEUE`:等待运行的完成,然后运行。
- `GROUP_REJECT`和`GROUP_QUEUE`:相同,但对同一组的任何工作。

他们会从 `JobGroup` 继承一个类, 如 app 或 Home Assistant Core 。 一个实例上的所有工作都共享一个锁定,所以一个应用程序在备份时无法更新. 一个工作可以在自己的群体中调用其他工作而不陷入僵局.

`JobThrottle`限制工作运行的频率 。 `THROTTLE` 在一个周期内跳过调用, `RATE_LIMIT` 每个周期允许一些调用, 之后失败 。 两者都有组变种. 他们需要 `throttle_period` , 和 速率限制 `throttle_max_calls` 。

## 进步与童工 {#progress-and-child-jobs}

每个工作都有UUID,一个阶段,一个进度百分比,以及它的错误. 工作从工作内部开始,就成为孩子。 在 `child_job_syncs` 中, 工作可以从孩子身上获取进步, 就像从拖动图像中获取进步的更新。

客户端通过 API 跟踪任务, 包含 `/jobs/info` 和 `/jobs/<uuid>`, 并通过 Core 接收的事件 。 前端就是这样显示更新进度的。 有 `internal=True` 的工作没有曝光 。 配有 `cleanup=False` 的作业完成后仍可读取, 因此客户端可以稍后取取结果 。
