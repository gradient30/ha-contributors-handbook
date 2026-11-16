---
title: 开发清单
description: 在您承诺之前, 请在此列表中检查您的更改, 因此您的 pull request 已准备好接受审查 。
sidebarGroup: Pull request
order: 1
---



# 开发清单 {#development-checklist}
在你犯案前先检查一下名单 pull request模板要求您确认,审查人员检查.

## 的 {#code}

- [ ] 代码格式化为Ruff (`ruff format`), 和[巨钩](/core/development/checks)通过.
- [ ]测试通过,新代码有[Cambridge. 测试](/core/development/tests).
- [ ]没有评论出来代码。
- 你明白每一行, 你可以解释它。 这也适用于为您写的AI工具的代码.
- [ ]如果一个模块已完全输入,则在`.strict-typing`中列出.

## 图书馆和所需经费 {#libraries-and-requirements}

所有与设备和服务的通信都通过在 [PyPI 密码](https://pypi.org/) 上发布的 Python 库。 集成本身没有协议代码.

- [1] 库在PyPI上有一个源发行,不仅仅是预建的车轮.
- [1] 图书馆的来源是公开的,根据OSI核准的开源许可证,兼容Apache 2.0,核心许可证. CI用[`script/licenses.py`](https://github.com/home-assistant/core/blob/dev/script/licenses.py)检查要求的许可证,但发现没有OSI批准的许可证时失效。 少数套件在它的例外清单中,所以通行证并不是每个要求的证明. 与 Apache 2.0 的兼容性由 [审查人员](/core/development/reviewing) 检查 。
- [ ] 启用了图书馆的问题跟踪器。
- [ ] 新的或更新的要求为`requirements_all.txt`。 运行 `python3 -m script.gen_requirements_all` 更新它 。

如果您主要为 Home Assistant 维护库并拥有集成, 请考虑使用一个将用户指向 [核心问题跟踪器](https://github.com/home-assistant/core/issues) 的问题模板选择器, 如 [zwave-js- server-python 图像](https://github.com/home-assistant-libs/zwave-js-server-python/issues/new/choose) 。

## 元数据 {#metadata}

- `manifest.json`是完整和正确的。
- [ ]新整合业主在`CODEOWNERS`. 运行 `python3 -m script.hassfest` 更新它 。
- [ ]用户看到的一切都在`strings.json`,而不是代码里. 见[制造可变字符串](/translate/guides/developers).

## 用户 {#users}

- [ ]任何删除或改变现有行为的行为都遵循[折旧过程](/core/development/deprecating).
- [ ] 反向不相容的变化在pull request中描述,为使用Home Assistant的人.
- [] 如果用户能看到变化,则在[Home Assistant.io](https://www.home-assistant.io/)上的文档会在自己的pull request中更新. 见[编写文档](/writing)。
