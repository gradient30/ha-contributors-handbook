---
title: 本地预览网站
description: 使用自己的机器运行Home Assistant.io, 这样你可以看到更大的变化之前,你分享它们。
order: 2
---

# 本地预览网站 {#preview-the-site-locally}

对于小修正, 您 pull request 上的部署预览就够了 。 对于更大的修改,如新页面或调整后的段落,在您写作时更快看到您的本地工作.

## 带着一个装饰者 {#with-a-devcontainer}

最简单的方式是Visual Studio代码,并配有Devcontainer. 它为你设置了一切, 不在你的机器上安装Ruby。

1. 叉开[Home Assistant.io仓库](https://github.com/home-assistant/home-assistant.io),用Visual Studio代码打开.
2. 当被询问时, 打开容器中的文件夹 。
3. 打开命令调色板并运行 **任务:运行任务** > **Preview**.
4. 在浏览器中打开 `http://localhost:4000` 。

## 没有修补器 {#without-a-devcontainer}

你需要鲁比和Node.js 项目使用的版本在寄存器的[`.ruby-version`](https://github.com/home-assistant/home-assistant.io/blob/current/.ruby-version)和[`.nvmrc`](https://github.com/home-assistant/home-assistant.io/blob/current/.nvmrc)文件中 。 需要节点(Node.js),因为生成网站也会建立其Astro部分.

1. 为您的系统安装Ruby、Bundler和Node.js。 您的 Linux 发行的 Ruby 包可以比 `.ruby-version` 中的版本更老. 如果 `bundle` 失败, 请用 mise 来安装 Ruby 。 对于鲁比和邦德勒:

   - 费多拉:

```shell
     sudo dnf -y install \
       gcc-c++ ruby ruby-devel rubygem-bundler rubygem-json rubygem-rake
     ```

   - Debian 或 乌邦图 :

```shell
     sudo apt-get install \
       ruby ruby-dev ruby-bundler ruby-json g++ zlib1g-dev
     ```

   - macOS 如果随身携带的Ruby不起作用 和Homebrew:

```shell
     RUBY_FORMULA="ruby@$(cut -d . -f 1,2 .ruby-version)"
     brew install "$RUBY_FORMULA"
     export PATH="$(brew --prefix "$RUBY_FORMULA")/bin:$PATH"
     ```

   - 使用 [纲领](https://mise.jdx.dev/): 寄存器告诉 mise 从 `.ruby-version` 读取 Ruby 版本 。 运行 `mise trust` , `mise install ruby` 和 `gem install bundler` 。 错误地下载了预编译的 Ruby , 只要您系统存在, 并从其它来源构建 。 该建筑需要一个汇编器和发展图书馆。

2. 在您的仓库克隆中, 安装依赖性 :

```shell
   bundle
   npm install
   ```

3. 生成网站一次. 第一次需要一分钟:

```shell
   bundle exec rake generate
   ```

4. 开始预览 :

```shell
   bundle exec rake preview
   ```

5. 打开`http://127.0.0.1:4000`。 文件的更改会自动被取出, 刷新您的浏览器以查看它们 。

整合页面在`source/_integrations`中,一般文档在`source/_docs`中. [文档如何运作](/writing/how-it-works#where-pages-live) 列出其他文件夹 。

### 在另一个机器上 {#on-another-machine}

预览只在 `127.0.0.1` 上收听, 所以无法从另一台计算机中找到它 。 在没有屏幕的服务器上工作? 传递IP地址, 它应该听:

```shell
bundle exec rake "preview[192.168.0.123]"
```

或者把它留在原地,然后从自己的电脑上把港口移到SSH上:

```shell
ssh -L 4000:localhost:4000 user@ip-of-the-server
```

## 检查一下 {#run-the-checks}

向各机运行的相同检查 你好 他们需要Node.js:

```shell
npm install
npm run markdown:lint
npm run textlint
```

`markdown:lint`检查Markdown结构。 `textlint`检查拼写和术语。 解释他们要找什么 如何处理假警报
