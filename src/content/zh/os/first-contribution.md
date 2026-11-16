---
title: 你对Supervisor的首次贡献
description: 在其开发容器中运行 Supervisor，进行一个小改动，运行测试，然后打开你的第一个 pull request。
sidebarLabel: 你的第一次贡献
order: 1
---

# 你对Supervisor的首次贡献 {#your-first-contribution-to-the-supervisor}

Supervisor 是进入该区域的最简单方式。它是 Python，有一个现成的开发容器，并且可以在你自己的机器上运行完整的 Home Assistant 系统。你可以在几分钟内看到你的更改生效，而无需刷新任何东西。

安排一个晚上来做。容器的第一次构建需要一些时间，而且你只需做一次。

> [!提示]
> 更想在操作系统上工作吗？从 [构建镜像](/os/operating-system/build) 开始。预计第一次构建需要一个小时或更久，并且需要大量磁盘空间。

## 1. 打个招呼 {#1-say-hi}

加入 [Home Assistant Discord](https://www.home-assistant.io/join-chat/) 上的 [**#operating-system**](https://discord.com/channels/330944238910963714/1475552965954900018) 频道。在 **频道与角色** 下，选择 **我想将开发技能贡献给 Home Assistant** 来查看它。开始时无需许可，但知道向谁提问会很有帮助。

## 2. 打开开发容器 {#2-open-the-development-container}

你需要 [Docker](https://docs.docker.com/get-docker/)、[Visual Studio Code](https://code.visualstudio.com/) 和 [Git](https://git-scm.com/)。在 Windows 上，请在 WSL2 内工作。

1. 在 GitHub 上 [Fork Supervisor 仓库](https://github.com/home-assistant/supervisor/fork)。
2. 克隆你的 fork 并在 Visual Studio Code 中打开它：

   ```shell
   git clone https://github.com/YOUR_GitHub_USERNAME/supervisor
   cd supervisor
   code .
   ```

3. 当 Visual Studio Code 提示时，选择 **在容器中重新打开**。

## 3. 运行 Supervisor {#3-run-the-supervisor}

打开命令面板，选择 **Tasks: Run Task**，然后选择 **Run Supervisor**。该任务会从你的工作副本构建一个 Supervisor 镜像并启动它。Supervisor 随后会下载 Home Assistant Core 及其插件，因此第一次启动需要几分钟。

完成后，打开 `http://localhost:9123`。这就是由你自己的 Supervisor 运行的 Home Assistant Core。**Run Supervisor CLI** 任务会打开针对它的 `ha` 命令行。

## 4. 找一些小的事情 {#4-find-something-small}

- 浏览 [未解决的问题](https://github.com/home-assistant/supervisor/issues)，寻找一些描述清楚且规模小的任务。
- 缺失的测试也是一个很好的首次修改。测试存放在 `tests/`，并且与 [`supervisor/`](https://github.com/home-assistant/supervisor/tree/main/supervisor) 的布局相对应。
- 一个令人困惑的日志信息或你自己遇到的错误也算。你已经知道它的重要性。

在你开始处理更大的事情之前，先在问题中提出询问。对 Supervisor 的大规模修改需要方案上的一致。[Supervisor README](https://github.com/home-assistant/supervisor#development) 说明得很清楚：小改动和错误修复可以直接提交到 pull request，但对于重大修改，首先要提出 RFC（征求意见请求：让他人可以反馈的书面提案）。

## 5. 进行更改并测试它 {#5-make-the-change-and-test-it}

创建一个分支，进行更改，并运行您修改部分的测试：

```shell
git checkout -b fix-something
pytest -qsx tests/backups/
```

在提交之前运行代码检查工具：

```shell
ruff check --fix supervisor tests
ruff format supervisor tests
```

要在运行的系统中查看您的更改，请再次运行 **Run Supervisor** 任务。它会根据您的代码重新构建镜像。

## 6. 打开一个 pull request {#6-open-a-pull-request}

将您的分支推送到您的 fork 并针对 `main` 打开一个 pull request。填写 pull request 模板：描述拟议的更改，选择更改类型，并完成检查清单。维护者会进行审核。预计会有问题，这是审核的正常流程。

## 在你的 pull request 之后 {#after-your-pull-request}

在 Supervisor 仓库中：- **检查。** CI 在 `Dockerfile` 上运行 Ruff、pylint、mypy、hadolint 以及测试，每次提交都会运行。pull request 模板明确说明：除非测试通过，否则你的 pull request 不能合并。构建工作流也会从你的分支构建一个 Supervisor 镜像，并对运行中的系统进行一些测试。
- **标签。** 你的 pull request 需要一个类型标签。只要 `cla-signed` 是唯一的标签，检查就会失败。发布说明会自动起草，并且只列出带有类别标签的 pull request：`breaking-change`、`new-feature`、`bugfix`、`style`、`refactor`、`performance`、`test`、`build`、`ci`、`chore`、`revert` 或 `dependencies`。标签还决定了你的修改显示在哪个部分。
- **等待。** 30 天没有活动的 pull request 会被标记为陈旧，并在 7 天后关闭。任何更新都会移除该标记。

- **合并后。** 您的更改会被构建并发布到 `dev` 渠道。然后发布会将其带到 `beta`，随后再到 `stable`。请参见 [Supervisor 的发布方式](/os/supervisor/development#how-the-supervisor-is-released)。

在操作系统仓库中，pull request 会针对 `dev` 提交。hadolint、ShellCheck 和 Buildroot 包检查器会在每次 pull request 上运行。维护者可以添加 `run-ova-test` 标签来构建镜像并运行自动化测试。该操作仅适用于主仓库中的分支，不适用于来自叉 fork 的 pull request。超过 90 天没有活动的pull request会被标记为陈旧，并在 7 天后关闭。[发布和构建](/os/operating-system/releases) 会将更改从这里推进到发布。

## 接下来做什么 {#what-is-next}

- 阅读 [Supervisor 架构](/os/supervisor/architecture) 来熟悉代码。
- 学习 [作业](/os/supervisor/jobs) 和 [解决中心](/os/supervisor/resolution-center) 的工作原理。大多数更改都涉及其中之一。
- 在真实硬件上使用 [远程系统](/os/supervisor/development#test-on-a-real-system) 进行测试。
