---
title: 保持分支最新
description: 将 Home Assistant Core dev 分支的最新更改带入您的分支, 并解决冲突 。
sidebarLabel: 不断更新
sidebarGroup: 调用请求
order: 4
---



# 保持分支最新 {#keeping-your-branch-up-to-date}
`dev`分支动作快。 如果您的工作需要一段时间, 或者您的 pull request 等待审查, 请偶尔带来最新的更改 。 它避免了冲突,失败只有在您的更改符合最新代码时才会出现.

使用`git merge`,而不是`git rebase`,一旦您的pull request打开。 重写承诺审查者已经看到。

## 合并最新的 dev {#merge-the-latest-dev}

请确定您有 Home Assistant 寄存器为远程 `upstream` 。 如果你跟着[环境设置](/core/development/environment),你会的。 否则,加上:

```shell
git remote add upstream https://github.com/home-assistant/core.git
```

然后,从你的分支:

```shell
git fetch upstream dev
git merge upstream/dev
```

## 解决冲突 {#resolve-conflicts}

如果 Git 报告冲突 :

1. 运行 `git status` 以查看哪些文件冲突 。
2. 编辑每个文件,并解决`<<<<<<<`和`>>>>>>>`标记之间的部分。
3. 将已解析的文件添加到 `git add` 。
4. 完成與 `git commit` 的合并。 默认的訊息是罚款的.

再次运行测试 : 没有冲突的合并仍然可以破解您的代码 。

## 推开 {#push}

```shell
git push
```

如果 Git 回答上游分支与您的分支名称不符, 您的分支仍然遵循 `upstream/dev` 。 用 `git push -u origin HEAD` 推动一次, 然后使用 `git push` 和 `git pull` 的叉 。

如果推力被拒绝,有人 推到你的分支 同时。 可能是你从另一台电脑, 或者一个应用建议的评论员。 拉这些变化,并再次推:

```shell
git pull --no-rebase
git push
```

## 保证结果片干净 {#make-sure-the-result-is-clean}

如果您的 pull request 突然显示来自其他人的承诺, 合并失败 。 与承诺无关的pull request不能复审。 最简单的修补是最新`dev`的新鲜分支,只有您的更改,还有新的pull request.
