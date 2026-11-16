---
title: Apple 发布
description: 苹果应用的更改如何从一个合并的pull request到App Store Connect,版本如何设定,Mac构建如何变成GitHub发行.
sidebarLabel: 发布
order: 8
---



# Apple 发布 {#apple-releases}
每个合并的pull request都是构建,签名,并上传到App Store Connect. 从那里开始,构建到TestFlight测试器和App Store. 本页面描述了该路径中生活在寄存器中的部分,以及如何自己构建一个发布器.

## 从合并到 App 存储连接 {#from-merge-to-app-store-connect}

### 每一次推向主线 {#every-push-to-main}

当将 pull request 合并为 `main` 时, `distribute.yml` 工作流程会用 Fastlane 构建两个应用 :

- **iOS**:`bundle exec fastlane ios build`将App Store的应用程序存档,上传至App Store Connect.
- **Mac**:`bundle exec fastlane mac build`从一个档案库中创建了两次Mac App. 一个开发者ID版本,由苹果公证,和一个Mac App Store软件包,上传到App Store Connect.

每次运行还保留其建筑为文物:iOS `.ipa`,开发者ID Mac app (`mac-developer-id.zip`),Mac App Store包,调试符号.

建设编号为`CURRENT_PROJECT_VERSION`从[`Configuration/Version.xcconfig`](https://github.com/home-assistant/iOS/blob/main/Configuration/Version.xcconfig)开始,然后是工作流程运行的编号. 这个运行号是将App Store Connect的构建 与它来自的承诺联系起来的

### 问题时光 {#testflight}

谁都能[加入测试Flight β](https://www.home-assistant.io/ios/beta/). Beta用户发现测试无法解决的问题.

还没有准备好给每个人的特性 只能飞到TestFlight,在`Current.isTestFlight`后面。 从β中取出这样的特性,就是合并其去除大门的pull request草稿. 见[每次更改的规则](/companion/apple/architecture#rules-for-every-change).

向TestFlight测试器和App Store移动一个扩展发生在App Store连接,而不是存储器中.

### 设置版本 {#setting-the-version}

用户看到的版本号是`MARKETING_VERSION`在[`Configuration/Version.xcconfig`](https://github.com/home-assistant/iOS/blob/main/Configuration/Version.xcconfig)中. 一个维护者用 ** Version: Set Version ** 工作流程 (`set_version.yml`) 来修改它,该工作流程运行 `bundle exec fastlane set_version` 并用新版本打开 pull request 。

### GitHub 上的 Mac 发布 {#mac-releases-on-github}

开发者ID Mac app也在 [GitHub 发布页面](https://github.com/home-assistant/iOS/releases) 上发布.

1. 一个维护者运行 **Tag macOS Release ** 工作流程,并带有释放标记,如`release/2026.5.0/2026.1987`,以及一个对`main`的承诺. 标记的最后一个编号是构建该任务的分布运行的运行编号.
2. 工作流程等待分配运行成功,标记承诺,并启动** Release macOS**工作流程.
3. ** Release macOS** 创建 GitHub 以生成的发布注释预发, 并附加来自 District 运行的开发者 ID app.

再次运行它一个已有的发布更新该发布, 并保持它是一个预先发布与否, 维护者离开它的方式。

### 存储列表 {#store-listing}

App Store 描述,关键词,和发布注释在 `fastlane/metadata` 中直播,每个语言一个文件夹. 它们在 [Lokalise](/translate) 上翻译, 就像应用程序的字符串 。 { { 目前正在进行 { { { { { { { { { { { { { {

## 自己建一个解禁栏 {#build-a-release-yourself}

只有ط 苹果开发团队 的项目。 两条车道都签有团队证书,上传至App Store Connect.

Fastlane从环境或`.env`文件读取其配置,如苹果ID和团队ID. 数值见[`.env.sample`](https://github.com/home-assistant/iOS/blob/main/.env.sample)。 然后说:

```bash
# Build and upload the Mac app {#build-and-upload-the-mac-app}
bundle exec fastlane mac build

# Build and upload the iOS app {#build-and-upload-the-ios-app}
bundle exec fastlane ios build
```

两者都保存他们的建筑到`build/`.

对于自己的设备,您不需要任何这样的设备: 与自己的团队一起运行 `App-Debug` 方案, 如 [开始](/companion/apple/get-started#3-set-up-code-signing) 所述 。
