---
title: 运行测试
description: 使用 pytest 运行 Home Assistant Core 的测试, 检查您的覆盖, 更新快照, 并知道 CI 运行 。
sidebarLabel: 运行测试
sidebarGroup: 编写代码
order: 4
---



# 运行测试 {#running-the-tests}
每一个改变为核心都经过测试. Core 使用 [测试](https://docs.pytest.org/), 而这个页面是关于运行测试的: 哪个命令,哪个选项,以及CI对他们做什么. 如何用固定装置、模拟和快照为整合写好测试,

## 运行测试 {#run-the-tests}

激活您的虚拟环境( 开发容器为您服务 ) 。 然后进行你改变的整合测试:

```shell
pytest tests/components/example
```

在激活环境之外,`uv run --no-sync pytest`也是这样。

全套测试套房需要很长时间. 如果你改变了很多整合所用的东西, 运行它, 否则测试你自己的变化就足够了。

一些有用的选项:

```shell
# Stop at the first failure {#stop-at-the-first-failure}
pytest tests/components/example -x

# Run only tests with a matching name {#run-only-tests-with-a-matching-name}
pytest tests/components/example -k test_setup

# Fail a test that runs longer than 10 seconds {#fail-a-test-that-runs-longer-than-10-seconds}
pytest tests/components/example --timeout 10

# Show the 10 slowest tests {#show-the-10-slowest-tests}
pytest tests/components/example --durations=10
```

> [!NOTE]
> 测试从将性别问题纳入生成的 `translations/en.json` 而不是从 `strings.json` 中装入英文文本 。 更改 `strings.json` 后, 在运行测试前运行 `python3 -m script.translations develop --integration example` 。

## 检查你的覆盖 {#check-your-coverage}

要查看测试尚未覆盖的行 :

```shell
pytest tests/components/example \
  --cov=homeassistant.components.example \
  --cov-report term-missing
```

报告列出了整合的每个模块,没有达到测试的线条。 质量尺度要求全覆盖的`config_flow.py`来自青铜器,超过95%来自银器的每个模块.

CI向Codecov报告覆盖范围,对于一些文件Codecov则希望每个更改的行都经过测试. 在任何集成中, 您的 pull request 文件中的行变化需要100%的覆盖, 或者 Codecov 检查失败 :

- `backup.py`
- `config_flow.py`
- `device_action.py`
- `device_condition.py`
- `device_trigger.py`
- `diagnostics.py`
- `group.py`
- `intent.py`
- `logbook.py`
- `media_source.py`
- `recorder.py`
- `scene.py`

列表存在于 [`codecov.yml`](https://github.com/home-assistant/core/blob/dev/codecov.yml) 核心寄存器中 。

## 更新快照 {#update-snapshots}

快照测试将您的代码结果与存储的 `.ambr` 文件进行比较 。 创建或更新集成的快照:

```shell
pytest tests/components/example --snapshot-update
```

以您的更改提交快照文件, 并读取其 diff 。 见[即时测试](/core/development/tests#snapshot-tests).

## 新的依赖关系 {#new-dependencies}

如果您更改了集成的要求,请更新要求文件并安装新包:

```shell
python3 -m script.gen_requirements_all
uv pip install -r requirements_all.txt -r requirements_test.txt
```

## 在视觉工作室代码中 {#in-visual-studio-code}

开发容器有所有这些任务。 打开命令调色板, 选择 ** 任务: 运行任务 **, 并选择 ** Pytest **, ** Pytest (仅更改测试) **, ** Code 覆盖**, 或 ** Update 糖浆快照 **. 见[任务](/core/development/environment#tasks).

## 线程 {#what-ci-runs}

CI运行每个pull request的测试。 当 pull request 只接触整合时, 它会运行这些整合的测试。 当您更改核心文件, 或者当维护者添加 `ci-full-run` 标签时, 它会运行完整套件 。 见[针头、狂欢和CI](/core/development/checks).
