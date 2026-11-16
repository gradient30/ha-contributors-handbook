---
title: 建立环境
description: 的匀,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
order: 1
---

# 建立环境 {#set-up-the-environment}

你可以在前端的脱发机上工作,也可以直接在你的机器上工作. Devcontainer是最容易开始的:它带来了正确的节点.js,pnpm,和Python,它可以在前端旁边运行Home Assistant Core.

## 拿到密码 {#get-the-code}

在 GitHub 上叉 [前端仓库](https://github.com/home-assistant/frontend) 上, 然后复制您的叉, 并添加主仓库为 `upstream` :

```shell
git clone git@github.com:YOUR_GIT_USERNAME/frontend.git
cd frontend
git remote add upstream https://github.com/home-assistant/frontend.git
```

切除 `dev` 每一次更改。 这是分支pull request去。

## 与虔诚者 {#with-the-devcontainer}

您需要与 Dev 容器扩展的 Visual Studio 代码和 Docker 或兼容的容器运行时间 。

1. 在Visual Studio代码中打开克隆寄存器.
2. 被请求时,选择**在集装箱中重新打开**。 或者打开指令调色板并运行**Dev容器:在容器中重新打开**.
3. 等待容器建造。 每次容器启动时,它都会运行`script/bootstrap`,从`.nvmrc`开始安装Node.js版本和依赖性.

容器有ESLint,Pretier,和Lit的推荐扩展,保存时格式文件.

集装箱内的8123号港作为**8124**号港在您的计算机上公布。 无论在集装箱内8123号上运行,你打开 `http://localhost:8124`。

## 在你的机器上 {#on-your-own-machine}

你需要的就是: 爱丽丝.

- **Node.js**,在[`.nvmrc`](https://github.com/home-assistant/frontend/blob/dev/.nvmrc)文件的版本中. 使用 [无](https://github.com/nvm-sh/nvm) , 在寄存器中运行 `nvm install` 并选择正确的 。
- **pnpm**,在`packageManager`字段#H1}中标注的版本. 与 Corepack 一起,该版本会自动使用:

```shell
  corepack enable pnpm
  ```

  如果您的节点.js不包括 Corepack,请用 `npm install -g corepack` 或 [直接安装 pnpm](https://pnpm.io/installation) 安装它 。

然后安装依赖性 :

```shell
nvm use
script/setup
```

`script/setup`运行 `script/bootstrap`, 运行 `pnpm install` 。 拖动触动 `package.json` 或 `pnpm-lock.yaml` 的更改后再次运行 。

## 翻译 {#translations}

没有别的,前端只用英语运行. 要获得所有语言的最新翻译,请启动一个使用 `--fetch-translations` 的开发服务器, 如 `pnpm dev --fetch-translations` 。 第一次,它要求您以 GitHub 授权, 它保存了 `translations/token.json` 中的符号 。 如果授权停止工作, 例如“ 不良证书” 错误, 删除文件并再次运行命令 。

## AI 工具 {#ai-tools}

寄存器在 `AGENTS.md` 中有 AI 编码工具的指令, 在 [`.agents/skills/`](https://github.com/home-assistant/frontend/tree/dev/.agents/skills) 中有 [`.agents/skills/`](https://github.com/home-assistant/frontend/tree/dev/.agents/skills) 的 技能, 用于组件、 样式、 用户界面文本、 测试和审查 。 Claude Code, GitHub Copilot 和Codex自己来接他们. [用AI 工具做贡献](/start/ai-tools) 列出它们, 并加一个卡的工作流程, 并解释 [AI 政策](/start/ai-policy) 对你的要求 。

## 下一步 {#next-step}

[运行前端](/frontend/development/run)对 Home Assistant 实例 。
