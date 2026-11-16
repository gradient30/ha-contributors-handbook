---
title: 依赖性和供应链
description: 每个库 Home Assistant 安装在它内部运行 。 { 等一下什么是依赖,它自动检查什么,它自己的工作流程如何保护.
sidebarLabel: 依赖性和供应链
order: 5
---

# 依赖性和供应链 {#dependencies-and-supply-chain}

整合通过图书馆与设备和服务交谈,这些图书馆来自PyPI. 每个 [所需经费](/glossary/requirement) 是代码,最终在 Home Assistant 中,在安装它的每个人的家中。 如果攻击者接管了一个库,或者将恶意包滑入它的依赖性,他们就是其中之一. 这是供应链的攻击,这就是为什么Home Assistant严格地说它的依赖来自哪里。

## Home Assistant 问图书馆什么 {#what-home-assistant-asks-of-a-library}

[依赖性透明度](/core/quality-scale/dependency-transparency)质量尺度规则设定了基准. 任何与外部依赖性有关的整合都必须满足,从青铜层到上方:

- 依据《公约》第22条第1款(a)项
- 该包可在PyPI上获得.
- PyPI上的包由公共CI管道建造并发布.
- PyPI上每个版本都匹配公共寄存器中标记的发布.

规则是存在的,这样项目就可以信任它每次释放时所携带的依附物.

## 钳线自动检查 {#what-is-checked-automatically}

你不必亲手检查这些 多个工具查看每个 pull request 更改要求 。

### 狂欢 {#hassfest}

hansfest 验证了 `requirements` 在每次整合的显示中 :

- 核心集成必须把每个要求都钉在一个准确的版本上,比如`"example-library==1.2.3"`.
- 它行走全依赖树,不仅仅是直接依赖树,以及不应该存在的旗帜包:作为运行时依赖的工具测试,构建,或docs,`types-`包,以及一些未保存的包.
- 它会标记安装顶级 `test`, `tests`, `doc` 或 `docs` 文件夹, 或顶级 `.pth` 或 `.start` 文件的包 。

### 检查要求 {#check-requirements}

一个 pull request 更改 Core 的要求文件从 ** 检查要求 ** 工作流程中获取一个注释, 每个更改的软件包有一个行 :

| 检查 | 看着什么 |
| --- | --- |
| 无顾问 | PyPI报告新版本没有已知的脆弱性. |
| 不是扬凯德 | 新的版本没有从 PyPI 中切除 。 |
| Repo 公开 | 源寄存器公开开放. |
| CI 上传 | PyPI的发布有一份证明,显示是哪个管道发布的. |
| 释放管道 | 库的出版工作流程:由标签,发行,或受保护的分支触发,最好是用OIDC而不是存储的代币发布,无法将其周围上传. |
| 警卫 | tube 快速扫描库源 明显供应链红旗. |
| PR 链接 | 一个新的软件包链接到它的源寄存器 。 一个版本凸起链接到一个变化日志或一个提及两个版本的比较. |
| 自动连接安全 | 在库内屏蔽 `async` 函数 。 |

这些检查有一部分由AI代理完成,其余部分由脚本完成. 以**Security**的行为名:便宜的第一通行证,而不是安全审查. 通行证显示为QQ,从来没有QQ,所以没有人读它作为认可印章.

### 许可证 {#licenses}

Core的CI提取了每个已安装的软件包的许可证,并检查它是否得到OSI的批准,使用[`script/licenses.py`](https://github.com/home-assistant/core/blob/dev/script/licenses.py).

## 添加或更新依赖时 {#when-you-add-or-update-a-dependency}

- 链接您几句pull request 中的源寄存蓓目, 用于新建库, 或用于更新的更改日志或两个版本的比较 。 检查要求工作流程寻找它,审查人员需要它.
- 只更改版本和重新生成的要求文件,加上代码会改变新版本的需求. 运行 `python3 -m script.gen_requirements_all` 重生成文件 。
- 如果新版本吸引了它自己的新依赖,请在您的 pull request 中这么说 。
- 如果维护库:通过公共CI管道发布,在PyPI上可信赖的发布,因此发布内容可以追溯到其来源.

没事 审阅员要通过[依赖性更新清单 你好吗?](/core/development/reviewing#dependency-updates) 没事,你打开它之前值得阅读

## GitHub 工作流程 {#github-workflows}

项目本身的CI也是供应链的一部分。 [核心存储器](https://github.com/home-assistant/core) 中的工作流程遵循您将在审查中看到的几种模式 :

- ** 行动归结为承诺SHA**,版本在评论中,如`actions/checkout@<sha> 

# v7.0.1`。 翻新使针头不断更新. {#what-went-wrong-before}
- ** 豁免从零开始。 ** 工作流程 知道了 `permissions: {}` 设置在顶端, 每个任务都列出它所需要的权限, 如 `contents: read` 。
- ** 检查不保存证书**:`persist-credentials: false`在`actions/checkout`上。
- **zizmor**,是GitHub工作流程的linter,在核心寄存器中以踏板模式运行,作为承诺前钩和CI. [前端仓库](https://github.com/home-assistant/frontend)运行 `actionlint` 的工作流程 。

如果你改变工作流程,请遵循这些模式。

### 以前发生什么了? {#related}

在2023年,GitHub号 安全实验室在 `helpers/version` 中发现了 [表达式插入](https://github.com/home-assistant/core/security/advisories/GHSA-jff5-5j3g-vhqc), 一个共享的动作在 [动作存储器](https://github.com/home-assistant/actions) 中 。 它将`${{ github.head_ref }}`,一个pull request的分支名称,直译为`run:`脚本. GitHub在 shell 运行前填入一个表达式,因此其中含有 shell 代码的分支名称成为脚本的一部分. 根据咨询,攻击者可以利用它泄露秘密并改变存储处.

从不将外部数据的表达式,如分支名称,标题,或注释,放在`run:`脚本中. 把它当作一个环境变量, 让外壳把它当作数据:

```yaml
- name: Show the branch
  env:
    HEAD_REF: ${{ github.head_ref }}
  run: echo "Branch: ${HEAD_REF}"
```

Zizmor标记这种模板注入。

## 相关 {#相关}

- [铭记安全审查](/security/guides/reviewing): 在 pull request 中要寻找什么 。
- [自动检查](/security/reference/checks):每张支票在一个表格中。
- [所需经费](/core/integrations/manifest#requirements)娇女: `requirements` 显示的密钥 。
