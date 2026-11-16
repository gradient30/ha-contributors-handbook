---
title: 自动安全检查
description: 还为安全问题检查呐Home Assistant的代码、依赖性和工作流程的工具,以及它们运行在哪里的工具。
order: 2
sidebarLabel: 自动检查
---

# 自动安全检查 {#automated-security-checks}

这些检查都是自己进行的,所以很多问题在审阅员甚至出现之前就被抓住了. 它们不会取代审查:它们抓住已知的模式,而不是每一个错误。 他们都在[核心存储器](https://github.com/home-assistant/core)中,除非表上另有说明。

| 检查 | 在哪里运行 | 捕捉到的东西 |
| --- | --- | --- |
| 节日需求 | CI, 本地为 `python3 -m script.hassfest` | 不以`==`为基准的核心集成要求。 依赖树上不应该是运行时间依赖,或者没有保存的套件. 安装顶级 `test`,`tests`,`doc`或`docs`文件夹,或顶级 `.pth`或`.start`文件的软件包。 |
| 许可证审计 | CI, 当需求发生变化时 | 在无OSI许可的情况下安装的软件包([`script/licenses.py`](https://github.com/home-assistant/core/blob/dev/script/licenses.py)). |
| 检查要求 | 拖动更改要求文件的请求 | 在PyPI,一个私人源代码存储器,一个没有出版证明的发布,一个微弱的发布管道,源代码中明显的红旗,一个缺失的变换日志链接,以及`async`代码中阻断调用. 见[依赖性和供应链](/security/guides/dependencies#check-requirements). |
| 规则 | 承诺前钩, 也在 CI 中 | 调用 `exec` (`S102`), `eval` (`S307`), `subprocess` 与 `shell=True` (`S602`), 不安全的 XML 解析, `pickle` , 硬码临时文件, 和硬码密码作为默认值 。 完整列表在 `select` `[tool.ruff.lint]` `pyproject.toml` 下。 |
| 代码QL | 每周来一次 | 以 等一下 GitHub 扫描 Python 代码的代码 。 |
| 齐兹莫尔语Name | 承诺前钩, 也在 CI 中 | GitHub工作流程中的安全问题,用踏板模式. |
| 动作lint | [前端仓库](https://github.com/home-assistant/frontend) 的 CI 代码 | 这就是在 GitHub 工作流程中的错误 。 |
| 翻新 | 它本身的pull requests | 拖动更新依赖关系、承诺前钩和绑定的 GitHub 行动 |

## 相关 {#related}

- [依赖性和供应链](/security/guides/dependencies):这些检查对您的pull request意味着什么 。
- [检查您的 pull request](/core/development/checks):所有Core的检查, 不仅仅是安全。
