---
title: 你的第一次安全贡献
description: 请检查您用于瓷器整合的诊断, 并修复您找到的数据。
sidebarLabel: 你的第一次贡献
order: 1
---

# 你的第一次安全贡献 {#your-first-security-contribution}

你不需要做安全研究员来让Home Assistant更安全 一个良好的第一步使用你已有的东西:你自己的Home Assistant,以及你每天使用的集成.

用户在公共 GitHub 问题上附加 [诊断](/glossary/diagnostics) 文件, 因此整合必须先从它们中删除密码, 令牌, 和其他私有数据 。 它有一份要编辑的密钥清单。 当该列表中缺少一个密钥时,私人数据最终会公开. 检查是具体的,小的,有用的。

## 1.  卸载诊断文件 {#1-download-a-diagnostics-file}

1. 转到** 安排** > ** 设备和服务**。
2. 选择您使用的集成 。 与云服务交谈或需要登录的人是一个很好的选择,因为它有需要保护的秘密.
3. 打开三点菜单并选择**Download诊断**.

并不是每个融合都有诊断。 当它没有时, 选项不显示: 选择另一个 。

## 读它 {#2-read-it}

在文本编辑器中打开文件 。 删除的值显示 没事 `**REDACTED**` 。 寻找本该 没事的东西:

- 密码、 API 密钥和令牌, 包括访问和刷新令牌
- 位置数据,如坐标和地址
- 个人信息,如姓名和电子邮件地址
- 徘徊在您或您的设备上的标识符, 如序列号或账户ID

来自multiculturalismo API的数据往往比集成作者预期的要多,所以也看看嵌入的数据.

## ,                                                                                                           不 {#3-decide-what-it-is}

大多数时候,你什么也找不到。 这是一个很好的结果,你学到了诊断方法。

如果你发现什么, 想想谁能看到它。 如果数据不应该出现在用户公开分享的文件中,则需要修复. 如果你认为这会以另一种方式给用户带来风险,或者你不确定,那么把它视为一种脆弱性和[私下报告](/security/report-a-vulnerability). 一份私人报告 证明是无害的 成本很小。 公众的弱势地位使家庭面临危险。

## 动起来 {#4-fix-it}

固定通常为单线. 诊断器位于 `diagnostics.py` 的整合文件夹中, 位于 [核心存储器](https://github.com/home-assistant/core) 。应当是大多数集成保存一组密钥,通常称为`TO_REDACT`,并通过`async_redact_data`传递数据:

```python
TO_REDACT = {CONF_API_KEY, CONF_PASSWORD, "serial_number"}
```

将缺失的密钥添加到集中 。 然后更新诊断测试的快照, 因此审查人员看到值变化为 `**REDACTED**` :

```bash
pytest tests/components/example --snapshot-update
```

新到Core吗? [您的首次贡献为核心](/core/first-contribution)为您设定一个开发环境,并让你通过您的第一个pull request. [诊断](/core/integrations/diagnostics)更详细地解释代码.

## 接下来是什么 {#what-is-next}

- 读 [安全融合](/security/guides/integrations) , 用于保存整合安全的其他模式 。
- 与 [安全考虑](/security/guides/reviewing) 审查 pull request 。 依赖性更新是一个很好的开始地点: [清单](/core/development/reviewing#dependency-updates)是短的, 风险是真实的.
