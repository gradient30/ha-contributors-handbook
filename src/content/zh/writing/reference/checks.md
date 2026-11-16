---
title: 自动文件检查
description: 其自始至终的自始至始的自始至始的自始至始的自始至始的自始至始的自始至始的自始至始的自始至始的自始至始的自始至始的自始至始至始的自始至始的自始至始至始的自始至始至始的自始至始至始的自始至终的自始至始至始至始至始至始至始至始的自始至始至始至始至始至始至始至始至的自始至始至始自始至始至始至始至始至始至始至始至始至始至始至始至始至的自始至始至始至的自始至始至始至始至始至始至始至始至始至的自始至始至始至始至的自始至始至始至始始至始至始至始至始至始至始至始至始始至始至始至始至始至始至始至始至始至始至始至始至始至始至始
order: 4
sidebarLabel: 自动检查
---

# 自动文件检查 {#automated-documentation-checks}

每 pull request 到 [Home Assistant.io仓库](https://github.com/home-assistant/home-assistant.io) 运行一组自动检查 。 它们捕捉到小东西,比如没有语言或拼错产品名称的代码块,因此审查人员可以专注于内容.

在 [`test.yml`](https://github.com/home-assistant/home-assistant.io/blob/current/.github/workflows/test.yml) GitHub 动作工作流程中运行的检查 。 有两个是关于你的写作:

- ** L 是呀, 请所得到的信息 。
- ** Lint Text** 检查拼写、术语和措辞,加上[文本链接](https://textlint.github.io/)。

Markdown 任务还检查 {L0的工作人员} 中的集成页使用 `.markdown` 文件扩展名 。 文件 `.md` 检查失败 。

第三项工作是 ** Build Astro site ** 在 `astro` 文件夹中构建了网站的部分 。 它不看你的写作,但它也必须通过。

## 对了 {#run-the-checks-locally}

您需要 [节点.js](https://nodejs.org/) 。 CI中的lint任务使用20版本. 寄存器的`.nvmrc`文件以及编解码器使用第26版.

1. 在您的仓库克隆中, 安装依赖性 :

```shell
   npm install
   ```

2. 运行Markdown检查 :

```shell
   npm run markdown:lint
   ```

3. 运行文本检查 :

```shell
   npm run textlint
   ```

这些命令与CI运行的命令相同. 它们在[`package.json`](https://github.com/home-assistant/home-assistant.io/blob/current/package.json)中定义。

要检查您工作的单个页面, 请直接运行该文件上的工具 :

```shell
npx remark --quiet --frail source/_integrations/my_integration.markdown
npx textlint source/_integrations/my_integration.markdown
```

> [!TIP]
> 寄存器推荐了Visual Studio代码的文本lint和markdownlint扩展. 安装这些设备后,您在输入时会在编辑器中看到大多数问题.

## 标记检查 {#markdown-checks}

`markdown:lint` 脚本运行于整个寄存器 `remark --quiet --frail .` 。 `--frail` 旗帜将警告变成失败, 所以每个发现都会阻碍检查 。

规则位于[`.remarkrc.js`](https://github.com/home-assistant/home-assistant.io/blob/current/.remarkrc.js). 他们检查:

- **代码块**:每个有栅栏的代码块命名其语言. Shell 示例不会以 `$` 开始每行, 因为这样会打破复制和粘贴 。 `$` 当您需要告诉命令与其输出不同时, 它就很好 。
- **标题**:标题使用`#`样式,一次只下一层。 不能从 `##` 跳到 `####` 。
- **列表**:未排序列表使用`-`. 订购清单使用数字之后的一段时间,如`1.`,并一致地为项目编号。 计数上,`1.`,`2.`,`3.`,是公约.
- ** 拼写名称**:禁止字符串列表,如`GitHub`而不是`GitHub`,`websocket`或`Websocket`而不是`WebSocket`,`Speech-To-Text`而不是`Speech-to-text`。
- **链接到网站本身**:一个完整的`https://www.home-assistant.io/`链接应该是一个相对路径,就像`/integrations/hue/`.

一些文件被故意跳过,比如博客文章和更改日志. 它们列于[`.remarkignore`](https://github.com/home-assistant/home-assistant.io/blob/current/.remarkignore)。

### 添加注释规则 {#add-a-remark-rule}

1. 安装规则包, 更新 `package.json` 和 `package-lock.json` :

```shell
   npm install --save-dev remark-lint-some-rule
   ```

2. 启用并配置 `.remarkrc.js` 中的规则 。
3. 运行`npm run markdown:lint`。
4. 纠正拇指已存在的侵权行为,或在`.remarkignore`中添加一个沧桑。

## 文本检查 {#text-checks}

`textlint` 脚本检查这些文件夹 :

- `source/_docs`
- `source/_faq`
- `source/_integrations`
- `source/_dashboards`
- `source/cloud`
- `source/getting-started`
- `source/hassio`
- `source/dashboards`

其他的文件夹,如博客,不受CI检查. 在 `source` 下检查一切, 运行`npm run textlint:all` 。

规则位于 [`.textlintrc.json`](https://github.com/home-assistant/home-assistant.io/blob/current/.textlintrc.json) :

- 发现常见的拼写错误。
- `terminology`执行产品名称,首选术语和措辞. 它跳过块状参数中的文本 。
- `comments` 过滤器允许您关闭部分页面的文本lint 。
- `allowlist` 过滤器忽略了本来会给出假正数的文本, 如 YAML 密钥, 如 `mqtt:` 或 `homeassistant:` 。

### 添加术语条目 {#add-a-terminology-entry}

术语存在于 `terms` 规则列表 `terminology` 规则, 在 `.textlintrc.json` 中 。 一个条目有两种形式之一。

一个简单的字符串是一个必须准确保留这种拼写和资本化的术语:

```json
"Home Assistant",
"Z-Wave",
"GitHub"
```

一对旗子一拼,建议另一面. 第一个值是匹配模式,第二个值是向贡献者提出的建议:

```json
["addon", "add-on"],
["colour", "color"],
["repo\\b", "repository"]
```

该图案是JSON字符串内的正则表达式. 逃逸字符在任意一种中都有特殊的含义,比如上面`\\b`中的反弹.

在 我听说的附近放置新条目 。 然后 我听说了这些变化

### 禁用页面部分的文本lint {#disable-textlint-for-a-part-of-a-page}

有时文字林会标出正确的东西. 在此情况下,请在 HTML 注释中将文本包裹 :

```html
<!-- textlint-disable -->

Text that textlint should skip.

<!-- textlint-enable -->
```

仅关闭一条规则,请添加其名称:

```html
<!-- textlint-disable terminology -->

Text that the terminology rule should skip.

<!-- textlint-enable terminology -->
```

一些准则:

- 尽可能少地保留残疾人。
- 在每个评论前后已将空白行前后前后后后后后后后后后后后后加行行行后后后后后后加行行行行行行行行行行行位置.行行行..行行行行行行行行行行行.....的............................的..........的.....................的...........的的的.........的的的的...的.................的的的的的的................的的的的的的的的的的的的.....的的的的的...............的的的的的的的的的的的的的........
- 不要将这些注释放在 [文本框](/writing/reference/liquid#text-boxes) 中 。

### 添加文本林特规则 {#add-a-textlint-rule}

1. 将规则包添加到 `package.json` , 并更新 `package-lock.json` 。
2. 启用并配置 `.textlintrc.json` 中的规则 。
3. 运行`npm run textlint`。
4. 修正现有的违法行为,或在`.textlintrc.json`中的`allowlist`中加入狭义的排除。

## 马克唐林特 {#markdownlint}

该寄存器还有一个 [`.markdownlint.json`](https://github.com/home-assistant/home-assistant.io/blob/current/.markdownlint.json) 文件 。 它为编辑者配置 [降级](https://github.com/DavidAnson/markdownlint) :

- 一个页面的第一个标题是二级(`MD002`),因为标题来自前题.
- 没有行长度限制(`MD013`),所以可以写流文本.
- 同一文本的标题是允许的,只要他们不是同一父母的兄弟姐妹(`MD024`)。
- 允许内置 HTML (`MD033`).

Gong. Markdownlint 扩展位于推荐的 [`.vscode/extensions.json`](https://github.com/home-assistant/home-assistant.io/blob/current/.vscode/extensions.json) 扩展中, 因此您可以在 Visual Studio 代码中看到它的警告 。

> [!NOTE]
> Markdownlint在CI中不运行,也没有`package.json`的脚本. 它的警告是暗示,而不是阻断器. 如果必须执行 pull request 的 markdownlint 规则, 它也需要一个脚本和工作流程中的一个步骤 。
