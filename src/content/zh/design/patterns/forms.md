---
title: 形式和鉴定
description: Home Assistant如何收集输入,标记什么是需要的,并显示什么是错的,因此人们可以修复.
order: 1
---

# 形式和鉴定 {#forms-and-validation}

表格在Home Assistant中随处可见:设置集成,编辑自动化,改变一个实体的设置. 他们都遵循同样的模式,所以人们知道在哪里寻找标签,提示和问题.

## 何时使用 {#when-to-use}

每当向人们询问一个或多个值时使用此模式 。 对于一个立即生效的单一设定,像打开或关闭一个特性一样,一个[切换](/design/components/switch)自己就可以了.

## 工作原理 {#how-it-works}

前端的大多数窗体都是用[窗体](/design/components/form)组件构建的. 您描述字段, 它通过 [选择器](/design/components/selector) 选择每个值的正确控制 : 名称的文本字段, 实体的拾取符, 是或否的切换符 。 集成的设置和选项对话框也一样。 这就是为什么他们看起来和行为都一样。

Live demo of `ha-form`, 连接到一个 demo Home Assistant.

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](https://contributors.home-assistant.io/design/patterns/forms/)。

```html
<ha-form data-props='{"schema": [{"name": "Name", "required": true, "selector": {"text": {}}}, {"name": "Light", "selector": {"entity": {"filter": {"domain": "light"}}}}, {"name": "Notify me", "selector": {"boolean": {}}}], "data": {"Name": "Hallway"}}'></ha-form>
```

### 标签和帮助文本 {#labels-and-helper-text}

- 每个字段都有明显的标签. 必然会消失。
- 当一个字段需要解释时,请添加帮助文本. 其坐于田间下. 在`ha-form`中,它来自`computeHelper`.
- 使用既定的字段布局和共享组件,而不是您自己构建的原始输入或控件.

做和不做,作为现场演示。

** Do:** 保持可见的标签,在字段下方提示.

```html
<ha-input label="Host" hint="The IP address or hostname of the device"></ha-input>
```

别... ** 只有一个占位符。 只要有人打字就不见了

```html
<ha-input placeholder="Host"></ha-input>
```

### 所需和可选 {#required-and-optional}

- 需要的字段在标签后显示 `*` 。
- 如果有道理,请选择字段,并给它们一个合理的默认值。 一个好的默认有帮助, 不阻碍人们谁想要别的东西。

### 验证 {#validation}

提交表单时检查一个字段。 与 `auto-validate` 一起的 [文本输入](/design/components/input) 会被检查, 当人们离开 。

当一个值无效时 :

- 字段被标记为开展的无效,其验证消息取代了帮助文本.
- 在`ha-form`中,关于一个字段的错误显示在该字段的正上方。 关于整个窗体的错误,像失败的连接一样,显示在顶部.
- 焦点移动到第一个有问题的领域,所以键盘和屏幕阅读器用户就在上面降落.

Live demo of `ha-form`, 连接到一个 demo Home Assistant.

```html
<ha-form data-props='{"schema": [{"name": "Host", "required": true, "selector": {"text": {}}}, {"name": "Port", "selector": {"number": {"min": 1, "max": 65535, "mode": "box"}}}], "data": {"Host": "192.168.1.200", "Port": 8080}, "error": {"base": "Could not connect to the device.", "Host": "No device answers on this address."}}'></ha-form>
```

错误以 [警报](/design/components/alert) 显示, 因此它们有图标和文本, 而不仅仅是红色 。 关于如何表达,见[信件](/design/ui-text/messages)。

### 对话框中的窗体 {#forms-in-dialogs}

- 对话框打开时窗体会焦点梢: 给它`autofocus`属性 。
- 主要动作与**拯救**一样,坐落在右下方,旁边是**Cancel**.
- 一旦有人改变了某样东西,该对话框不会与"逃逸"或通过在它之外选择来关闭. 见[确认和撤消](/design/patterns/confirmations).

### 密码 {#passwords}

表格标记不应使方面的努力被密码管理者误认为不是。

## 无障碍 {#accessibility}

- 一个字段的标签是其可访问的名称. 保持它, 也当空间紧。
- 无效的 [文本输入](/design/components/input) 设置 `aria-invalid`, 并宣布其验证消息 。
- 关于WCAG一方,请参见[标签和可访问名称](/design/foundations/accessibility#labels-and-accessible-names).

## 组件 {#components}

- [表格](/design/components/form) 和[选择器](/design/components/selector) (韩语)
- [文本输入](/design/components/input) 和[文本区域](/design/components/textarea) (韩语)
- [开关](/design/components/switch),[选择框](/design/components/select-box),和[珉 选择菜单](/design/components/select-menu) 。
- [实体选择器](/design/components/entity-picker),[设备拾取器](/design/components/device-picker),和[区域拾取器](/design/components/area-picker) 。
- [警报](/design/components/alert),用于错误和警告

## 在代码中 {#in-code}

使用 `ha-form` 的图案 。 `computeLabel`,`computeHelper`和`computeError` 将名称和错误键转换成翻译文本 。 将 `error` 设定为按字段名键的对象, 整个窗体为 `base` 。 工作方式相同,没有 `base`。 [窗体](/design/components/form) 页面有细节 。
