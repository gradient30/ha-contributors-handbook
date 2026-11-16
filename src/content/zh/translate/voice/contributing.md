---
title: 提供判刑和答复
description: 如何更改您语言在意向寄存器中的句子,响应和测试,检查您的工作,并打开 pull request 。
order: 2
sidebarLabel: 贡献句子
---

# 提供判刑和答复 {#contribute-sentences-and-responses}

所有句子,回复和测试都以[意图存储器](https://github.com/OHF-Voice/intents)在GitHub上直播. 您用 pull request 来更改它们, 您语言的语言领袖会评论它 。 这页让你通过。

## 在浏览器中添加一句 {#add-one-sentence-in-your-browser}

最小的有用变化是说 Assist 已经知道的命令的新方式 。 您可以在 GitHub 上, 在浏览器上, 不安装任何东西 。 新建到 GitHub ? [使用 GitHub,](/start/github)覆盖基础。

每个句子都需要一个测试,所以你的修改总是用相同的路径触及两个文件:句子文件及其测试文件. 教荷兰人用新的方法 打开它的名字,例如:

1. 打开 [`sentences/nl/HassTurnOn/name_only.yaml`](https://github.com/OHF-Voice/intents/blob/main/sentences/nl/HassTurnOn/name_only.yaml) 并选择用于编辑的铅笔图标 。
2. 将您的句子模板添加到它所属的块的`sentences`列表中.
3. 选择 ** 承诺更改 ** 并创建一个新分支 。 如果您无法写入寄存器, GitHub 为您制作一个副本( a fork) , 并将分支放在那里 。
4. 在打开 pull request 主要打开 [`tests/nl/HassTurnOn/name_only.yaml`](https://github.com/OHF-Voice/intents/blob/main/tests/nl/HassTurnOn/name_only.yaml) 之前, 请在同一分支上打开 [`tests/nl/HassTurnOn/name_only.yaml`](https://github.com/OHF-Voice/intents/blob/main/tests/nl/HassTurnOn/name_only.yaml) 并用同样的方式编辑它 。 添加一个使用您新模板的测试句子到具有相同插槽和响应的测试组,并将其输入分支.
5. 打开pull request。

你pull request的支票,然后告诉你,如果有问题。 当一个句子文件没有测试文件,当一个文件的测试句子比句子模板少,当一个句子模板没有被任何测试句子使用,当一个测试句子不符合预期的意向,槽,或响应时,它们就会失败. 他们还检查您的 YAML 格式 。 之后,你语言的语言领袖评论你的变化.

准备好超过一句话了吗? 读吧

## 这是什么地方? {#what-is-where}

每个语言都有自己的文件夹. 将 `<language>` 替换为语言代码, 如 `nl` 或 `pt-BR` :

| 文件夹 | 它所持有的 |
| --- | --- |
| `sentences/<language>/<intent>/<slot_combination>.yaml` | 一个意图和插槽组合的句子模板 |
| `sentences/<language>/_common.yaml` | 错误响应、 跳过单词和整个语言的设置 |
| `responses/<language>/<intent>.yaml` | 一种意图的反应 |
| `lists/<language>/` | 颜色或状态等槽列表 |
| `rules/<language>/` | 扩展规则,像动词 转换的东西 |
| `tests/<language>/<intent>/<slot_combination>.yaml` | 测试一个意图和插槽组合 |

根部有两个文件适用于每种语言:

- [`intents.yaml`](https://github.com/OHF-Voice/intents/blob/main/intents.yaml) 声明意图和它们的槽组合 。
- [`languages.yaml`](https://github.com/OHF-Voice/intents/blob/main/languages.yaml) 列出语言及其领导人。

因此,如果你想改进荷兰语使用者如何用名字打开和关闭东西,你就可以改变这四个文件:

- [`sentences/nl/HassTurnOn/name_only.yaml`](https://github.com/OHF-Voice/intents/blob/main/sentences/nl/HassTurnOn/name_only.yaml)
- [`sentences/nl/HassTurnOff/name_only.yaml`](https://github.com/OHF-Voice/intents/blob/main/sentences/nl/HassTurnOff/name_only.yaml)
- [`tests/nl/HassTurnOn/name_only.yaml`](https://github.com/OHF-Voice/intents/blob/main/tests/nl/HassTurnOn/name_only.yaml)
- [`tests/nl/HassTurnOff/name_only.yaml`](https://github.com/OHF-Voice/intents/blob/main/tests/nl/HassTurnOff/name_only.yaml)

## 谁拥有什么 {#who-owns-what}

语言的文件夹属于语言领袖。 从 `languages.yaml` 国际义务生成的 [`CODEOWNERS`](https://github.com/OHF-Voice/intents/blob/main/CODEOWNERS) 文件会自动要求它们审查 。

这是不同的。 那里的变化会同时影响每种语言,所以只有寄存器维护者可以更改. 一个pull request来自任何人 谁碰它 失败`guard-core-files`检查。 如果缺少一个槽组合, 标记错误, 或不符合您的语言, [打开一个问题](https://github.com/OHF-Voice/intents/issues) 这解释了您需要什么 。

> [!NOTE]
> 拉丁字母中的塞尔维亚语(`sr-Latn`)由西里尔字母中的塞尔维亚语生成(`sr`). 在 `sr` 中进行修改 。 两人分开时支票失败.

## 小一点 {#keep-it-small}

将每个 pull request 限制在一个语言和一个意图上 。 e. e. e. e. e. e. e. 十小pull request击败了一个巨大的。

## 捡起你的布置 {#pick-your-setup}

宝藏有三种方法. 选一个适合你变化大小的

### 在 GitHub 上编辑 {#edit-on-github}

对于一个文件中的小修补,就像一个响应中的打字,你不需要安装任何东西. 新建到 GitHub ? {\fn黑体\fs22\bord1\shad0\3aHBE\4aH00\fscx67\fscy66\2cHFFFFFF\3cH808080}你走过同样的台阶 {\fn黑体\fs22\bord1\shad0\3aHBE\4aH00\fscx67\fscy66\2cHFFFFFF\3cH 马修

1. 在 GitHub 上打开文件并选择用于编辑的铅笔图标 。
2. 做你的零钱。
3. 选择 ** 承诺更改 **, 选择创建新分支并启动 pull request, 并描述您更改了什么 。

检查运行在您的pull request,所以你仍然 发现有什么问题。

### 使用编码空间 {#use-a-codespace}

对于任何更大的, [GitHub 代码空间](https://docs.github.com/codespaces/overview) 会在浏览器中给您一个完整的环境, 有编辑器和终端 。 没什么要安装的

1. 在 [仓库页面](https://github.com/OHF-Voice/intents) 上, 选择 **Code ** > ** Codespaces ** > ** 主机上创建代码空间**. 开始需要一两分钟
2. 在底部状态栏中选择分支名称,并创建一个新的分支。
3. 做你的改变。
4. 运行您打开的文件的检查: 打开菜单, 选择 ** Terminal ** > **Run Task**,并选择当前文件的**Run测试**.
5. 在 **Source Control** 中,将您的更改输入并选择 **Create Pull Request。

[代码空间走过](https://github.com/OHF-Voice/intents/blob/main/docs/codespace/README.md)在寄存器內。

### 当地工作 {#work-locally}

如果你更喜欢自己的机器,叉子和克隆寄存器,那么设置它:

```shell
git clone https://github.com/<your-username>/intents
cd intents
script/setup
```

`script/setup` 在 `venv/` 中创建 Python 虚拟环境, 并安装您需要的一切 。 在运行下面的命令之前, 用 `source venv/bin/activate` 激活它 。 该寄存器也作为 [调试器](https://containers.dev/) 工作, 如果您的编辑器支持这些 。

创建分支, 做您的修改, 并把它们推到叉 对不起, 打开 pull request 。

## 检查你的工作 {#check-your-work}

运行在您的 pull request 上的检查也可以运行在您的机器或代码空间中 。 在您打开 pull request 之前运行它们, 它可以节省您一次往返 。

验证您语言的文件 :

```shell
python3 -m script.intentfest validate --language nl
```

验证检查每个文件匹配`intents.yaml`中的槽组合,您使用的每个列表和规则都存在,所有`required`槽组合都有句子.

运行语言测试 :

```shell
pytest tests --language nl
```

添加 `-k HassTurnOn` 只担当测试一个意图, 而 `-n auto` 进行平行测试 。 测试检查每个句子是否匹配正确的意图,填充正确的插槽,给出正确的响应. 当一个句子模板从未被任何测试句使用时,它们也会失败.

`script/test`同时运行:验证和所有测试. 您可以通过相同的选项, 如 `script/test --language nl` 。

## 试试看 {#try-things-out}

写作时还要用一些工具

Vicenten series. 看看你的语句是怎样的

```shell
python3 -m script.intentfest parse --language en \
  --sentence 'turn on the lights in the kitchen'
```

它印出意向 和它匹配的插槽,作为JSON。

查看模板生成的句子 :

```shell
python3 -m script.intentfest sample_template 'turn on [the] light[s]'
```

您可以给出列表值, 数字范围, 以及规则, 如 `--values color red green`, `--range brightness 1 2` 或 `--rule color '[the] {color}'` 。

举例来说,你的语言接受一些意图:

```shell
python3 -m script.intentfest sample --language nl \
  --intents HassTurnOn HassTurnOff -n 5
```

计算您模板加起来的几句话:

```shell
python3 -m script.intentfest count_sentences --language nl --summary
```

可选的词和替代词成倍增加。 一种配有数百万句子的语言在小设备上会变得缓慢. 离开 `--summary` 查看每个模板的计数, 这样你就可以找到 生长过大的 。

## 什么pull request检查 {#what-the-pull-request-checks}

在验证和测试之外,一个pull request还检查:

- 无心窃取别意之句. 用于播放媒体的贪婪模板不应该捕获"将光设为最大",例如.
- 您的语言没有规则或列表 剩下的没有用。
- `CODEOWNERS` 仍然匹配 `languages.yaml` 。
- 您的 YAML 文件格式化为 [高级](https://prettier.io/) 格式化 。 运行此检查, 和 Python 检查, 本地 。

A pull request 只有在所有检查通过时才能合并 。

## 合并之后 {#after-the-merge}

在 `home-assistant-intents` 软件包的下一次发行中发布新的句子. Home Assistant 更新到新发布的软件包, 从那时起, 您的句子与Home Assistant 。
