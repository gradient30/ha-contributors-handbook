---
title: 解析中心
description: Supervisor如何发现在检查和评价方面有问题,将它们作为问题跟踪,并用建议加以纠正。
sidebarGroup: 工作原理
order: 3
---

# 解析中心 {#the-resolution-center}

666  resolution  resolution  resolution 它发现问题,记录它们, 和它可以提供一个固定。 用户将结果视为[维修](/glossary/repair) in Home Assistant : Core的 `hassio` 整合使它们变成了修理问题.

代码为[`supervisor/resolution/`](https://github.com/home-assistant/supervisor/tree/main/supervisor/resolution),管理器为`sys_resolution`.

## 概念 {#the-concepts}

| 概念 | 这是什么 | 定义为 |
| --- | --- | --- |
| 雌性 | 一个被找到共同努力的问题,比如低磁盘空间 | `IssueType` |
| 建议 | 指出了一个或多个问题,比如创建备份 | `SuggestionType` |
| 背景情况 | 问题在于:`system`,`core`,`addon`,`plugin`,`mount`,以及更多 | `ContextType` |
| 不支持的理由 | 为什么系统不被支持, 像一个修改的 Docker 设置 | `UnsupportedReason` |
| 不健康的原因 | 为什么这个系统不能像一个破烂的Docker那样被信任来运作 | `UnhealthyReason` |

它们都是在[`supervisor/resolution/const.py`](https://github.com/home-assistant/supervisor/blob/main/supervisor/resolution/const.py)的enums.

一个问题有一个类型,一个上下文,以及一个可选的引用,比如一个app的swit. 一项建议是相同的,它指出了它所解决的问题。

## 支助和健康 {#supported-and-healthy}

这是两件事:

- ** 不支持** 表示系统工作,但设置方式不支持项目,就像一个不是Home Assistant OS的主机. 用户看到一个通知,但一切都继续工作.
- **不健康**表示系统处于Supervisor无法安全工作状态. 带有 `healthy` 条件的工作拒绝运行, 这会阻碍大多数更新 。

不支持的理由在home-Assistant.io上有一个页面向用户解释,在`https://www.home-assistant.io/more-info/unsupported/<reason>`. 连接到警告的 Supervisor 日志 。

## 检查、评价和固定 {#checks-evaluations-and-fixups}

解析中心有三种插件,每个插件都在自己的文件夹中. 这些文件夹中的每个模块都通过它的`setup()`功能自动加载.

- ** 检查** (`checks/`) 查找问题并创建它们。 每一次检查还重新验证它早先提出的问题,并在这些问题消失后予以驳回。
- ** 评估** (`evaluations/`) 决定系统是否得到支持。 每个都添加或清除了一个没有支持的理由.
- ** Fixups**(`fixups/`)执行一项建议。 有些自动运行,有些则等待用户应用.

每个小时,在应用一个建议后,Supervisor会运行所有检查,然后是所有评价,然后是可能自动运行的固定装置.

## 写一张支票 {#write-a-check}

检查子类 `CheckBase` 。 这是从 [`supervisor/resolution/checks/free_space.py`](https://github.com/home-assistant/supervisor/blob/main/supervisor/resolution/checks/free_space.py) 开始的空格检查, 略微缩短 :

```python
class CheckFreeSpace(CheckBase):
    """Check for low free space."""

    async def run_check(self) -> None:
        """Create the issue when the system is affected."""
        if await self.approve_check(Issue(self.issue, self.context)):
            self.sys_resolution.create_issue(
                IssueType.FREE_SPACE, ContextType.SYSTEM
            )

    async def approve_check(self, issue: Issue) -> bool:
        """Return True while the issue still exists."""
        free_space = await self.sys_host.info.free_space()
        return free_space <= MINIMUM_FREE_SPACE_THRESHOLD

    @property
    def issue(self) -> IssueType:
        return IssueType.FREE_SPACE

    @property
    def context(self) -> ContextType:
        return ContextType.SYSTEM

    @property
    def states(self) -> list[CoreState]:
        return [CoreState.RUNNING, CoreState.STARTUP]
```

- `run_check`寻找问题,并创建问题,经常有建议.
- `approve_check` 回答一个现有问题是否仍然适用 。 基础课用它来解除那些消失的问题.
- 检查运行时限制 。

模块还需要返回检查的 `setup(coresys)` 函数 。 评价和固定模式相同,分别为`EvaluateBase`和`FixupBase`。

当添加新一期或建议类型时,Core需要为其翻译,所以前端可以显示有意义的修复. 这是一个单独的 pull request 到 `hassio` 整合在核心。

## 从命令行 {#from-the-command-line}

`ha resolution info`显示当前的问题、建议和理由。 `ha resolution suggestion apply <uuid>` 应用固定, `ha resolution healthcheck` 立刻运行检查 。 个人支票可以用`ha resolution check options <slug> --enabled=false`关闭.
