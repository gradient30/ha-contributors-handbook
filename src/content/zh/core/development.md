---
title: 开发工作流
description: 代码是如何从您的机器进入 Home Assistant 释放的 。 环境、工具、检查和审查过程。
order: 2
sidebarGroups:
- 写代码
- 调用请求
- 改变行为
---



# 开发工作流 {#development-workflow}
每次更改到 Home Assistant Core 都遵循同样的路径 。 百度百科 百度百科 百度百科 百度百科

本节涵盖该路径。 它适用于核心中的一切,从一行固定到新的整合.

## 写代码 {#write-code}

- [发展环境](/core/development/environment):开发容器,或Linux,macOS,或Windows上的手动设置.
- [代码样式](/core/development/style):格式化、docstrings、记录和公约审评员寻找。
- [类型提示](/core/development/typing):核心如何使用 mypy,如何选择严格检查.
- [运行测试](/core/development/testing):pytest,覆盖,快照,以及CI运行。
- [写作测试](/core/development/tests): 集成的测试是如何组织的,有固定装置,模拟和快照.
- [林特斯,狂欢和CI](/core/development/checks): 检查每个承诺和pull request
- [验证输入](/core/development/input-validation): 配置流、 动作和 YAML 的计划 。

## 调用请求 {#pull-requests}

- [发展清单](/core/development/checklist): 在你做出承诺之前要检查什么 。
- [提交 pull request](/core/development/submitting) : 分支、 承诺、 模板和定义您的更改 。
- [打开 pull request 后](/core/development/review-process):接下来会发生什么,如何加快速度.
- [不断更新分支](/core/development/catching-up) : 从`dev` 带来最新变化 。
- [正在审查pull requests](/core/development/reviewing): 当你审查别人的作品时需要寻找什么.
- [提示和诡计](/core/development/tips):小东西 让你的生活更容易。

## 改变行为 {#changing-behavior}

- [折旧](/core/development/deprecating):如何在一夜之间不打破人们的家 很自然地去掉或改变一些东西.
- [版本](/core/development/versioning):版本是如何建立起来的 Home Assistant.
- [实验室预览功能](/core/development/labs):在成为标准之前,

## 简本 {#the-short-version}

如果您只记得本节中的一件事: 保持 pull request 的大小 。 一个固定,一个特性,或者每个pull request一个重构. 小 pull request 得到审查的速度更快, 突破更少, 并且对每个人来说都更容易, 包括你。
