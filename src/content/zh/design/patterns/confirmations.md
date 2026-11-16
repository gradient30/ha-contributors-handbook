---
title: 确认和撤消
description: 何时在做某事之前询问,何时提供倒数,以及Home Assistant如何防止人们失去未保存的更改 。
order: 5
---

# 确认和撤消 {#confirmations-and-undo}

有些行动是不能收回的. 删除仪表板,删除备份,丢弃一个小时的自动化工作. 对于这些,Home Assistant先问. 对于可以恢复的行动来说,它会让路,并提出取消。

## 何时使用 {#when-to-use}

- ** 动作无法撤销**, 如删除某些内容: 使用确认对话框询问 。
- ** 行动可以立即取消**:做到这一点,并提供**Undo**。 自动化编辑器在您删除块时会这样做 。
- ** 人们即将失去他们没有保存的更改**:询问是保存还是丢弃。

这些话也在这里有所帮助。 ** 删除**表示它永远消失,**删除**表示它可以回来. 见[删除、删除、添加或创建](/design/ui-text/remove-delete).

## 工作原理 {#how-it-works}

### 确认对话框 {#confirmation-dialogs}

确认对话框是 [对话框](/design/components/dialog) , 有标题、 简短描述和两个按钮 。

- **Title**:人们大多阅读标题和按钮,所以把重要的东西放在那里. 没有标题,对话框会回到“你确定吗?” 上面没有说明会发生什么。
- ** 描述**:对于不确定的人,请解释会发生什么。
- **按钮**:**Cancel**,以及一个主按钮,表示它所做的:**Delete**,而不是**OK**. 破坏行动使用危险变体,所以是红色的.
- ** 无法绕过它**:确认对话框没有关闭按钮,在外部选择时不关闭。 人们从两个按钮中选择一个.

对话框指南中的例子 :

> ** 删除仪表板? **
>
> Dashboard Kitchen将在Home Assistant中永久删除。
>
> ** 撤销** / ** 删除**

做和不做,作为现场演示。

页:1 按钮上写着会发生什么, 红色的,因为它不能被撤销。

```html
<ha-button appearance="plain">Cancel</ha-button>
<ha-button variant="danger">Delete</ha-button>
```

别... ** 一个通用的OK。 人须读文以知其义.

```html
<ha-button appearance="plain">Cancel</ha-button>
<ha-button>OK</ha-button>
```

当动作具有破坏性时,焦点开始于 **Cancel **,所以通过反射按 <kbd> Enter</kbd> 不删除任何内容 。 对于其他确认,焦点从主按钮开始. 动作运行时,主按钮显示其繁忙.

### 撤销 {#undo}

有了逆境,人们就一步步地做他们想做的事,仍然可以改变主意. 与 ** Undo** 一起的 [祝酒词](/design/patterns/errors#toasts) 停留至少4 秒 。

### 未保存的更改 {#unsaved-changes}

编辑器会跟踪自上次保存以来是否有变化 。 当时:

- 离开编辑先问. 举例来说,Andomic interness 问及“安非他明”和“安非他明”等“安非他明” 你可以保存这些更改,或者丢弃它们然后离开. 你不能取消这个行动。"
- 关闭或重新加载浏览器标签会显示浏览器的警告.
- 变换窗体的对话框不会关闭 Escape 或选择其外部 。 反而会有点摇摆

## 无障碍 {#accessibility}

- 一个确认对话框被宣布为对话,其标题为它的名称,其描述与之相关联.
- 当对话打开时,焦点会移动到对话中,安全选择会成为破坏性行动的焦点.
- 危险按钮的红色并不是唯一的信号. 标签上写着**Delete**.

## 组件 {#components}

- [对话](/design/components/dialog)
- [按钮](/design/components/button),带有危险变体
- [错误和消息](/design/patterns/errors),为吐司与撤销

## 在代码中 {#in-code}

```ts
const confirmed = await showConfirmationDialog(this, {
  title: this.hass.localize("ui.example.delete_title"),
  text: this.hass.localize("ui.example.delete_text"),
  confirmText: this.hass.localize("ui.common.delete"),
  destructive: true,
});
```

`showConfirmationDialog()` 和 `showAlertDialog()` 住在 [`src/dialogs/generic/show-dialog-box.ts`](https://github.com/home-assistant/frontend/blob/dev/src/dialogs/generic/show-dialog-box.ts) 。 通过 `action` 而不是等待结果 当主按钮显示工作运行时的进展 。 第 15 条,第 20 条,第
