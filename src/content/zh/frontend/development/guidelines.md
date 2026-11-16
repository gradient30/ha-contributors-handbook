---
title: 编码准则
description: 前端代码是如何写入的,从TypeScript和Lit到事件,对话框,造型,以及文本. 每个 pull request 都在找什么 。
order: 4
---

# 编码准则 {#coding-guidelines}

这些是[前端仓库](https://github.com/home-assistant/frontend)的公约。 林特斯执行了一些 其余的都是审查人员要求的,所以跟随他们可以省下一轮审查.

## TypeScript {#typescript}

- TypeScript严格运行模式。 避免 `any`: 使用现有的 Home Assistant 类型, 或者写一个狭义的 。
- 将 `import type` 用于仅属于类型的导入 。 ESLint执行.
- 在拥有数据的源之后的形状类型,比如Core中的WebSocket命令,而不是在一个组件如何碰巧使用它之后.
- 在拥有它的数据模块中插入一个共享类型, 在 [`src/data/`](https://github.com/home-assistant/frontend/tree/dev/src/data) 下, 然后从那里导入 。
- 在生产代码中不要使用`console`. 显示用户错误, 或者使用已有的日志 。

## 升组件 {#lit-components}

- 元素以前缀命名 : `ha-` 用于共享的 Home Assistant 组件, `hui-` 用于仪表板 ("Lovelace") 组件, `dialog-` 用于对话框 。
- 使用 `@property()` 用于组件的 API 和 `@state()` 用于其内部状态 。
- 该项目使用Lit的TypeScript装潢机,配有`useDefineForClassFields: false`. 匹配现有的声明。 别用`accessor`关键词.
- 使用 `@query()` 用于您自己的模板中的元素, 而不是手工查询 DOM 。
- 在 `render()` 中计算廉价值。 对其它生命周期步骤需要的值使用 `willUpdate()`, 而`memoizeOne` 只当它保存了真正的工作时 。
- 在生命周期方法中,当您读取私有属性时,将更改的属性键入 `PropertyValues<this>` 或 plain `PropertyValues` 。

## 数据访问 {#data-access}

叶片组件消耗最窄l [案件的上下文](/frontend/architecture/hass-and-contexts) 覆盖它们所读的, 而不是带走整个 `hass` 对象. 一个读作 `hass`} 的组件在家庭的每个州都变了, 即使它没有显示什么变化。 拥有 `hass` 并传递它的容器可能保存它。

从 `src/common/decorators/consume` 导入 `consume`, 而不是 `@lit/context` 。 ESLint也执行这个规定.

## 傀儡 {#events}

- 使用 `fireEvent()` 从 [`src/common/dom/fire_event.ts`](https://github.com/home-assistant/frontend/blob/dev/src/common/dom/fire_event.ts) 发射事件 。 事件泡沫 和横跨阴影根 默认。
- Review.com.通过扩展`HASSDomEvents`接口来宣告每个自定义事件及其细节类型,因此`fireEvent()`检查有效载荷.
- 类型事件处理器, 由同一文件的帮助者: `HASSDomEvent<T>` 用于 `detail`, `HASSDomCurrentTargetEvent<T>` 读取收听器打开的元素, `HASSDomTargetEvent<T>` 用于发射的元素 。 使用 `ValueChangedEvent<T>` 从 [`src/types.ts`](https://github.com/home-assistant/frontend/blob/dev/src/types.ts) 到 `value-changed` 。

```ts
fireEvent(this, "item-selected", { id: item.id });

declare global {
  interface HASSDomEvents {
    "item-selected": { id: string };
  }
}
```

## 要使用的组件 {#components-to-use}

在您自写前先用 [`src/components/`](https://github.com/home-assistant/frontend/tree/dev/src/components) 共享组件构建 。一项关于 `ha-button` 、 `ha-dialog` 、 `ha-switch` 和 `ha-tooltip` 的许多组件, 都围起来 [网络真棒](https://webawesome.com/) 。 不要添加新 `mwc-*` 材料组件:正在更换。

- ** 拨号**:使用`ha-dialog` 与`DialogMixin` 从[`src/dialogs/dialog-mixin.ts`](https://github.com/home-assistant/frontend/blob/dev/src/dialogs/dialog-mixin.ts) 。 用标签、导入函数和参数打开对话框 `show-dialog` 。 在 `ha-dialog-footer` 、 `primaryAction` 和 `secondaryAction` 槽中插入动作 。
- **按钮**:`ha-button`有`variant`(`brand`,`neutral`,`danger`,`warning`,`success`,`appearance`(`accent`,`filled`,`outlined`,`plain`),和`size`。 使用 `appearance="plain"` 取消, 和`variant="danger"` 破坏行动 。
- ** 表格**: `ha-form` 从 [选择器](/glossary/selector) 的图案中生成一个形式 。 使用 `computeLabel`, `computeHelper` 和 `computeError` 来给出翻译文本 。
- ** 信**: `ha-alert` 与 `alert-type` `error`, `warning`, `info` 或 `success` 。
- ** 键盘快捷键**:`ShortcutManager`从[`src/common/keyboard/shortcuts.ts`](https://github.com/home-assistant/frontend/blob/dev/src/common/keyboard/shortcuts.ts)。

每个组件在[设计区](/design/components)中都有一页,解释何时使用以及如何使用.

## 样式 {#styling}

- 使用主题变量和 [设计符号](/frontend/architecture/theming), 绝不使用硬码颜色 。 使用 `--ha-space-*` 符号进行间隔 。
- 组件的范围样式。 不要依赖全局风格来进行组件的内部.
- 首先哎,移动设计,然后添加更大的屏幕需要的。
- 保持左右布局安全. 偏爱逻辑属性, 如 `margin-inline-start` 超过 `margin-left` 。
- 使触摸目标足够大, 并给每个控制 清晰的悬浮,焦点,活跃,和残疾状态。
- 保持运动微妙,并使用`--ha-animation-duration-*`符号。 他们尊重减少动议。

## 介绍用户的文本 {#user-facing-text}

- 每一个被人们看见的弦都通过翻译系统. 添加到 [`src/translations/en.json`](https://github.com/home-assistant/frontend/blob/dev/src/translations/en.json),并在代码中使用 `localize` 。 显示如何。
- 使用完整的句子与占位符。 从来没有胶水 翻译碎片在一起。
- 用美国英语写作,在句子情况下,用活跃的声音写作. 全文写"Home Assistant".
- 使用"退"来表示可以添加回,用"删除"来表示永远消失. 用"添加"来表示存在的东西,用"创造"来表示新的东西.

[用户界面文本](/design/ui-text)设计区一节有完整的指导.

## 国家与清理 {#states-and-cleanup}

- 处理加载、 错误、 不可用和缺少的实体 。 检查在读取前是否存在实体 。
- 删除事件收听器,计时器,观察器,以及组件断开时的订阅.
- 使每个控件都可用键盘和屏幕阅读器。

## 提交和依赖 {#commits-and-dependencies}

叮当前的钩子会运行ESLint,Pretier,以及你所承诺的文件上的Lit分析器,并修正它所能做的. 只编辑英文文本, 在 [`src/translations/en.json`](https://github.com/home-assistant/frontend/blob/dev/src/translations/en.json) 中 。 其他语言在建设时翻译为[Lokalise](/glossary/lokalise)并下载,而钩子拒绝承诺更改那些下载的文件.

在自己的 pull request 中保留依赖性更新 。
