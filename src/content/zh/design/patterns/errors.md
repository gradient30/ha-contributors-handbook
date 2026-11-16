---
title: 错误和消息
description: 如何Home Assistant告诉人们 事情出了问题,或是正确的。 警报、土司和修理 以及何时使用
order: 4
---

# 错误和消息 {#errors-and-messages}

在智能家庭里事情会出错作法:一个设备是离线的,一个密码已经更改,一个值是超出范围的. 界面如何这样说,使得一个混乱的时刻与一个快速解决的不同. 好消息也是如此:人们想知道,他们的变革得到了拯救。

## 何时使用 {#when-to-use}

选择需要停留多长时间的信息, 以及需要多近的问题:

- **挚约一个字段**:该字段的一个错误。 见挚 [形式和鉴定](/design/patterns/forms) 。
- ** 关于页面或对话框,人们正在查看**,直到解开为止:一个[警报](/design/components/alert)。
- **简短确认某事发生**,如"成功保存":在屏幕底部敬酒. 自行消灭.
- ** 在人们可以继续前进之前需要决定的东西**: [对话框](/design/components/dialog)。 见[确认和撤消](/design/patterns/confirmations)。
- ** 人们即使不看问题,也需要解决的设置中的一个问题**:由整合引起的修复问题。 它出现在**Settings** > **System** > **Repairs**下.

## 工作原理 {#how-it-works}

### 警报 {#alerts}

警报有四种类型之一。 每个都有自己的颜色和图标,所以类型也清晰无色.

现场演示 `ha-alert`.

```html
<ha-alert alert-type="error">The device did not respond. Check that it is powered on.</ha-alert>
<ha-alert alert-type="warning">This integration will stop working in a future release.</ha-alert>
<ha-alert alert-type="info">Changes take effect after a restart.</ha-alert>
<ha-alert alert-type="success">The backup is complete.</ha-alert>
```

- 警报可以有一个标题。 不得无描述使用标题.
- 一个警报可以解除,或者有动作,比如一个按钮来立即解决问题.

现场演示 `ha-alert`,`ha-button`。

```html
<ha-alert alert-type="warning">
  The token of this account has expired.
  <ha-button slot="action">Reauthenticate</ha-button>
</ha-alert>
```

### 面包 {#toasts}

敬酒是屏幕底部的短信息. 它至少停留4秒,并且可以有一个动作,比如**Undo**. 用它来反馈人们刚刚所做的 当他们不需要采取行动的时候

例如,在自动化编辑器中,删除一个块显示 ** 已成功删除 **,并带有** Undo** 按钮.

举杯就消失了 永远不要在敬酒里放东西 人们必须读 解决问题。

### 修复项 {#repairs}

当出现用户可以自行解决的问题时，集成会提出一个 [修复项（repair）](/glossary/repair/)。修复项应当：

- 说明问题是什么，以及为什么重要
- 给出确切的修复步骤；若有多步，使用编号列表
- 说明按步骤操作后会出现什么结果
- 只针对用户确实能解决的问题提出

修复项的文案来自集成。[核心](/core/) 区域说明了如何提出修复项。

### 动作错误 {#errors-from-actions}

当一个动作失败时,像打开一个不回答的光线一样,集成会引起一个错误,其消息在界面中显示. 一体化可以像任何其他文本一样翻译这一信息。

## 写入信件 {#writing-the-message}

一个好的消息说出了发生了什么,人们可以做些什么。 此模式中的每类消息都遵循相同的[用户界面文本](/design/ui-text/messages)指南.

## 无障碍 {#accessibility}

- 警报有`role="alert"`。 大多数屏幕读者一出现就立即宣布. 当页面加载通常不宣布时已经存在的提醒 。
- 敬酒有`role="status"`,在不中断的情况下宣布。
- 单色从来不说这是一个错误。 图标和文字也一样。
- 提示中的动作必须可用键盘达到.

## 组件 {#components}

- [警报](/design/components/alert)
- [对话](/design/components/dialog)
- [表格](/design/components/form),用于一个字段的错误
- [进度按钮](/design/components/progress-button),一个行动的结果

## 在代码中 {#in-code}

```ts
html`
  <ha-alert alert-type="error">
    ${this.hass.localize("ui.example.error")}
  </ha-alert>
`;

showToast(this, {
  message: this.hass.localize("ui.common.successfully_saved"),
});
```

`showToast()` 住在[`src/util/toast.ts`](https://github.com/home-assistant/frontend/blob/dev/src/util/toast.ts) 。 。 4秒以下的长度提高到4秒。 以 `text` 和 `action` 的调用通过 `action` 来添加像 ** Undo ** 的按钮 。
