---
title: 测试超过95%的代码
description: 银规则测试覆盖:测试覆盖整合每个模块的95%以上.
sidebarLabel: 试验覆盖
sidebarGroup: 银
order: 10
---

# 测试超过95%的代码 {#test-more-than-95-of-the-code}

这是Silver的规则 在`quality_scale.yaml`中,它被称为`test-coverage`.

整合测试必须涵盖95%以上的代码濑,在每个整合模块中.

## 为什么这很重要 {#why-it-matters}

工程中没有人拥有 Home Assistant 支持的每个设备 。 当有人修改共享代码,或者撞到你的整合库时,测试是唯一能注意到破裂的东西. 良好的报道使回归不再发生,让新的贡献者有信心地改变整合,将提供设备。

## 示例 {#example}

进行覆盖整合测试,并查看未覆盖的线路:

```shell
pytest tests/components/my_integration \
  --cov=homeassistant.components.my_integration \
  --cov-report term-missing
```

报告列出了每个模块的覆盖范围,以及没有测试的行号。 通过Home Assistant使用整合的方式写入测试:设置一个配置条目,然后检查状态和调用动作,而不是直接调用整合的功能. 如何写这些测试, 请参看[写作测试](/core/development/tests) 。

## 如何检查 {#how-it-is-checked}

- CI运行每个pull request覆盖的测试,Codecov则报告pull request中的变化覆盖.
- 受命团团动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动动
- 是否检查整合的每个模块是否超过95%。

## 例外 {#exceptions}

这一规则没有例外。

## 相关规则 {#related-rules}

- {L刚好} : 完全测试配置流 。
