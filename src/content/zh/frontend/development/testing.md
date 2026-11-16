---
title: B. 定式和测试
description: 开始执行linters,类型检查,单位测试,以及前端的端到端测试,以及何时写测试.
order: 5
---

# B. 定式和测试 {#linting-and-tests}

CI在您的 pull request 上运行所有这些 。 先自己跑,比等线人告诉你还快

## 图标和格式 {#lint-and-format}

```shell
pnpm lint
pnpm format
```

`pnpm lint` 运行 ESLint, Prettier, TypeScript 编译器, 和 Lit 分析器, 用于对照其中元素的属性检查您的模板 。 `pnpm format` 修正ESLint和Prettier自己可以修正的东西。

只运行类型检查 :

```shell
pnpm lint:types
```

> [!WARNING]
> 从不通过文件到`pnpm lint:types`或`tsc`。 使用文件参数,编译器忽略`tsconfig.json`,可以将`.js`文件写入[`src/`](https://github.com/home-assistant/frontend/tree/dev/src). 如果发生这种情况, 在您承诺之前删除生成的文件 。 对于一个文件的快速反馈,请使用编辑器中的诊断.

## 单位测试 {#unit-tests}

单位测试运行 [维特](https://vitest.dev/) 。 他们生活在 [`test/`](https://github.com/home-assistant/frontend/tree/dev/test) 中, 在一个反映 [`src/`](https://github.com/home-assistant/frontend/tree/dev/src) 的文件夹结构中 :

```shell
pnpm test
pnpm test:coverage
```

这样的测试文件 :

```ts
import { describe, expect, it } from "vitest";
import { ensureArray } from "../../../src/common/array/ensure-array";

describe("ensureArray", () => {
  it("wraps a single value in an array", () => {
    expect(ensureArray("light.kitchen")).toEqual(["light.kitchen"]);
  });
});
```

### 何时写测试 {#when-to-write-a-test}

为计算某物的代码写 哇 写一个测试, 别这样, 错误可能会从不注意的地方溜走: 数据处理,ivility, config验证, 和仪表板策略。

不要写测试来检查某物是如何生成的:一个组件的文本、样式或槽,或者一个面板显示它获得的数据。 这些突破与每一个设计改变 并保护很少。 如果视觉改变,则在您的 pull request 中添加截图 。

测试从不和真正的 Home Assistant 说话 。 替换 `callWS`, `callApi` 和与假件的连接 。 在联想出新的固定器或帮助器之前 看看测试套房已经有的那些

## 端到端测试 {#end-to-end-tests}

端对端测试以[剧作家](https://playwright.dev/)运行,在三个套房. 每个套件都有自己的开发服务器:

| 套间 | 开发服务器 | 端口 | 测试命令 |
| --- | --- | --- | --- |
| 应用 | `pnpm test:e2e:app:dev` | 8095 | `pnpm test:e2e:app` |
| 演示 | `pnpm dev:demo` | 8090 | `pnpm test:e2e:demo` |
| 图片库 | `pnpm dev:gallery` | 8100 | `pnpm test:e2e:gallery` |

应用套件测试 应用测试 与剥落的带 为这些测试。 演示和画廊套房使用其正常的开发服务器.

在背景中启动一个套件的开发服务器,然后运行套件. Playwright 重用已经运行的服务器,而不是做一个缓慢的完整构建,服务器在保存时会重建,这样就可以再次运行测试而无需重启任何操作:

```shell
pnpm test:e2e:app:dev --background
pnpm test:e2e:app
```

将测试名称的 `-g` 和浏览器的 `--project` 缩小运行范围 。 项目为`chromium`和`mobile-chrome`:

```shell
pnpm test:e2e:app -g "more-info" --project=chromium
```

`pnpm test:e2e`运行所有三个套房, `pnpm test:e2e:show-report`打开合并报告。

本地运行对一个开发服务器不同于干净的构建 CI 使用. 使各处各处各处各处各处各处各处各处各处各处,各处各处各处各处,各处各处各处各处各处,各处各处各处,各处各处各处各处各处,各处各处各处各处,各处各处各处各处,各处各处各处,各处各处各处,各处各处各处各处,各处各处各处各处,各处各处各处各处各处,各处各处各处,各处各处各处各处,各处各处,各处各处各处,各处各处各处各处,各处各处各处,各处各处各处各处,各处各处各处,各处各处各处,各处各处,各处各处各处,各处各处,各处各处,各处各处各处各处,各处各处各处各处,各处各处各处各处各处,各处各处各处各处各处,各处各处各

## 基准 {#benchmarks}

数据在图表后面变换,如历史、统计和能源都有基准。 在优化一个前,请在[`test/benchmarks/README.md`](https://github.com/home-assistant/frontend/blob/dev/test/benchmarks/README.md)中读取工作流程 。 优化必须保持输出完全相同:从不更新快照或固定装置以通过一个.

## 什么时候跑? {#what-to-run-when}

- ** 一个工具或数据变化**:相关的单元测试,然后是`pnpm lint:types`。
- **A组件变化**:`pnpm lint`,以及包含其中逻辑的单位测试.
- ** 改为有端到端测试的流量**:相关套房,缩小至受影响的测试。
- ** 大致重构**:`pnpm lint`和`pnpm test`。
