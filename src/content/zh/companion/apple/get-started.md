---
title: 开始使用 Apple
description: 安装 Xcode 和 Ruby 工具, 设置代码签名, 并在模拟器或您自己的设备上运行 Home Assistant 应用程序 。
sidebarLabel: 开始
order: 1
---



# 开始使用 Apple {#get-started-with-apple}
你需要一个麦克。 本页面将您从新克隆到模拟器运行的应用程序.

## 所需经费 {#requirements}

- QQcode**:项目目前需要的版本在[读取](https://github.com/home-assistant/iOS#getting-started)中. 工程跟随新的Xcode快速释放,因此有时从[抒情器下载](https://developer.apple.com/download/)中会有一个β.
- ** Ruby**:为Bundler和Fastlane服务,它们运行着电闸和测试。 版本为`.ruby-version`.
- **苹果开发团队ID**,用于代码签名.

第三方图书馆是Swift软件包. Xcode自行解决.

## 1.  叉、 克隆和分支 {#1-fork-clone-and-branch}

1. 叉 [Home Assistant/iOS](https://github.com/home-assistant/iOS) 在 GitHub 上 。
2. 建立分支:

```bash
   git clone https://github.com/<your-github-username>/iOS.git
   cd iOS
   git checkout -b fix-widget-refresh
   ```

## 插入 Ruby 励志工具 {#2-install-the-ruby-tooling}

选择一种方法去抓Ruby 然后安装宝石 使用 [纲领](https://mise.jdx.dev/) :

```bash
brew install mise
mise install
bundle install
```

使用 [里贝夫](https://github.com/rbenv/rbenv) :

```bash
brew install rbenv ruby-build
rbenv install
bundle install
```

鲁比版本在`.ruby-version`中. 如果您已经有一个匹配的Ruby, `bundle install` 就够了 。

## 3.  设置代码签名 {#3-set-up-code-signing}

该应用程序使用需要代码签名的权益,甚至在模拟器中也是如此. 调试构建使用自动提供,但需要告诉Xcode哪个团队和捆绑ID使用.

创建 曙光 `Configuration/HomeAssistant.overrides.xcconfig` :

```text
DEVELOPMENT_TEAM = YourTeamID
BUNDLE_ID_PREFIX = some.bundle.prefix
```

- `DEVELOPMENT_TEAM`是你的团队身份,从[苹果开发者门户网站](https://developer.apple.com/account)。 它看起来像`ABCDEFG123`。
- `BUNDLE_ID_PREFIX` 是您控制的一个前缀,所以Xcode可以为此创建提供配置文件.

Git 忽略了此文件 。 Xcode为您的团队生成配置文件,特性您的团队没有像关键提示一样被关闭.

## 运行应用程序 {#4-run-the-app}

1. 在 Xcode  伙计 打开 `HomeAssistant.xcodeproj` 。
2. 选择 **App-Debug**方案。
3. 选择模拟器或您的设备 。
4. 建设与 怎么跑.

如果您可以, 请将其连接到 Home Assistant 的测试实例 : 登机者在服务器上注册新设备 。

## 手动命令 {#handy-commands}

```bash
# Check formatting and lint, without changing files {#check-formatting-and-lint-without-changing-files}
bundle exec fastlane lint

# Fix what can be fixed automatically {#fix-what-can-be-fixed-automatically}
bundle exec fastlane autocorrect

# Run the unit tests {#run-the-unit-tests}
bundle exec fastlane test

# Run autocorrect before every commit {#run-autocorrect-before-every-commit}
bundle exec fastlane install_git_hooks
```

## 只测试前端 {#only-testing-the-frontend}

正在研究 [前端](/frontend) 想要在应用程序中看到它吗 ? 您不需要构建应用程序 :

1. 安装 Xcode,并从 QQcode ** > ** 打开开发工具 ** ** 打开模拟器 **.
2. 从 `main` 上的 [CI 工作流程](https://github.com/home-assistant/iOS/actions/workflows/ci.yml) 的最近运行中下载 `ios-simulator` 文物 。
3. 将 `.app` 拖到模拟器上并启动它 。
4. 在Safari中,在高级设置中打开**Develop**菜单。 然后使用**Develop** > **模拟器**在应用的网页视图上打开Web Victor.

## AI 工具 {#ai-tools}

该寄存器在`AGENTS.md`中有AI编码工具的指令,在[`.agents/skills/`](https://github.com/home-assistant/iOS/tree/main/.agents/skills)中有技能,如`ha-ios-architecture`,`ha-ios-testing`和`ha-ios-workflow-ci`. pull request模板询问您是否使用AI, 以及如何使用 。 [用AI 工具做贡献](/start/ai-tools) 列出每种技能, 并解释 [AI 政策](/start/ai-policy) 对你的要求 。

## 接下来是什么 {#what-is-next}

- 读 [结构](/companion/apple/architecture) 和 [开放供衡量的目标](/companion/apple/targets) 。
- 请检查{L0能够在您的第一个pull request 之前 。
