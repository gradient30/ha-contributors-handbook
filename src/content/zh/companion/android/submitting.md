---
title: 提交 Android pull request
description: 核对表,pull request模板,内置更改日志,以及Android寄存器中审查期间发生的情况.
sidebarLabel: 提交 pull request
sidebarGroup: 发布上线
order: 1
---



# 提交 Android pull request {#submit-an-android-pull-request}
你的零钱用在机器上 现在它需要一个 pull request, 一个审查,和一个合并。 本页面涵盖了审查人员的期望,因此审查顺利进行.

## 在你打开它之前 {#before-you-open-it}

- ** 格式和测试。 ** 运行 `./gradlew :build-logic:convention:ktlintFormat ktlintFormat` 和 `./gradlew test` 。 其他支票见[代码样式和折叠](/companion/android/code-style)。
- ** 建造一切。 ** 共享代码最终出现在手机,汽车,以及观看应用程序中. 请检查access-date=中的日期值 (帮助) !
- ** 添加测试** 你改变的行为。 见[测试](/companion/android/testing).
- ** 遵循准则**:[最佳做法](/companion/android/best-practices)、[UI 架构](/companion/android/ui-architecture)和[Compose 与设计系统](/companion/android/compose)。
- 保持小点声 一个想法每个pull request。 大型重修在小步的`WIPFeature`旗后,见[舰船小步变化](/companion/android/best-practices#ship-big-changes-in-small-steps).
- ** 读 [AI 政策](/start/ai-policy) 。 ** 你可以使用AI工具,但必须理解并能够解释你提交的每行. 调用自主代理的请求被关闭.

## 那个pull request {#the-pull-request}

如 [GitHub 文档](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork) 所述, 从您的叉子创建 pull request 对 `main` 。 GitHub 填写模板 。 切勿删除任何内容,除非模板告诉你,像一个不适用于你更改的部分. 填写 :

- **摘要**:你改变了什么,为什么,对用户意味着什么. 链接相关问题。
- **检查列表**:测试,代码样式,边缘大小写,向后兼容,以及AI策略. 后向不兼容的更改会在用户的更改日志中进行,或者在开发者的代码中进行,这取决于它们影响谁. 同时选择一个准确的选项来描述你是如何使用AI的.
- **Screenshots**:用于UI在前端外的变换,光线和暗模式.
- **Document**:如果您的更改添加,更改,或删除用户看到的东西,在[用户文档](https://github.com/home-assistant/companion.home-assistant)中打开pull request并将其链接. 将新特性标记为 `<span class='beta'>BETA</span>` , 直到它达到生产 。 如果它改变开发者所依赖的东西,比如如何构建,测试,或者发布应用程序,模板也要求一个pull request来更新开发者文档.

### 变化日志 {#the-changelog}

如果您的更改添加了功能, 明显改变用户的行为, 或打破他们依赖的东西, 请添加到 [`app/src/main/kotlin/io/homeassistant/companion/android/changelog/ChangelogContent.kt`](https://github.com/home-assistant/android/blob/main/app/src/main/kotlin/io/homeassistant/companion/android/changelog/ChangelogContent.kt) 中的内应用更改日志 。 小bug修正不需要自己的条目: 站立的"Bug修正和依赖性更新"条目覆盖它们.

`ChangelogContent.kt` 持有条目, 以新的, 改进的,和固定的组合, 每一个都有它应用的平台 。 每个条目的文本都是[`common/src/main/res/values/strings_changelog.xml`](https://github.com/home-assistant/android/blob/main/common/src/main/res/values/strings_changelog.xml)中的字符串,所以它得到翻译. 截图测试可以使真实的更改日志,所以更改日志也需要更新[截图引用](/companion/android/screenshot-testing).

## 草稿pull requests {#draft-pull-requests}

想要早日反馈方向时打开草稿,但工作尚未完成. 当您对 CI 本身进行修改时, 这也是有用的 。 注意CI,虽然:每次推都运行全管,这需要大量资源. 不要打开pull request, 草稿或不, 之前有东西看。 随时推叉.

如果这是你的第一个贡献, 维护者必须在每个CI运行开始前批准它。

## 审查 {#review}

任何人都可以审查 pull request, 欢迎您加入 。 哪怕是十分钟的检讨 也会有帮助的 检查代码不舒服吗? 从 pull request 安装 APK, 并报告您找到的东西: 错误、 崩溃或 UI 和 UX 反馈 。 见[测试 pull request 构建](/companion/android/get-started#test-a-pull-request-build).

对于合并,维护者必须批准. 耐心点 善良点 他们的反馈是随要求的更改而来的评论,或者作为问题。 用你自己的话回答问题,而不是用AI输出.

回答反馈和CI是绿色的时,请再做一次审查。

## 让你的分支更新 {#keep-your-branch-up-to-date}

如果您的分支落在 `main` 后面或有冲突, 您可以将 `main` 合并到您的分支 和 [解决冲突](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-using-the-command-line) , 或 [重新基质](https://docs.github.com/en/get-started/using-git/about-git-rebase) 上 :

- ** 尚未审查**:合并或重新基数,携手选择。
- ** 已审查**:合并。 重新定位可以打破现有的审查评论并失去反馈。

该寄存器使用[壁画和合并](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/about-pull-request-merges#squash-and-merge-your-commits), 因此您的分支历史不需要清理 。

## 合并 {#merging}

一旦一切都是绿色的 并且一个维护者批准, 他们合并它。 何须无作. 你的汶上换钱给内部测试员 下周末再换Beta 见[释放](/companion/android/releases).

## 拖动pull requests {#stale-pull-requests}

一个bot标记一个{H2与各物嗓音相同,30天后没有活动,90天后出现问题. 如果接下来的7天里什么都没有发生,它就会关闭它们. 标签为 `under investigation` 或 `Help wanted` 的任何东西都豁免 。
