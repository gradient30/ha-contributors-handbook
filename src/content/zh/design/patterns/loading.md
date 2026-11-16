---
title: 正在装入
description: 如何 Home Assistant 显示有东西在路上, 从旋转器到报告其动作的按钮。
order: 2
---

# 正在装入 {#loading}

你家不总是一瞬间 一个设备需要一分钟来回答,历史必须被获取,备份需要几分钟. 一个好的等待告诉人们,事情正在发生,结果会在哪里出现.

## 何时使用 {#when-to-use}

显示装入状态, 否则人们会看到屏幕似乎卡住或空 。 选择等待地点的指标 :

- **一个整块区域负载,你不知道需要多长时间**:一个[旋转器](/design/components/spinner).
- ** 按钮启动一个在入籍时运行的动作**:按钮显示其繁忙.
- ** 动作完成后,没有其他地方显示结果**:一个[进度按钮](/design/components/progress-button)。
- / 需要使用 QT 或 QT 。
- **一项行动有几个步骤**:通过这些步骤显示进展,使人们知道进展有多远。

## 工作原理 {#how-it-works}

### 旋转器 {#spinner}

旋转器分为四个大小:`tiny`(16像素),`small`(28),`medium`(48,默认),和`large`(68).

现场演示 `ha-spinner`.

```html
<ha-spinner size="tiny"></ha-spinner>
<ha-spinner size="small"></ha-spinner>
<ha-spinner size="medium"></ha-spinner>
<ha-spinner size="large"></ha-spinner>
```

### 忙碌的按钮 {#busy-buttons}

使用 `loading` 的 [按钮](/design/components/button) 显示旋转器而不是其标签, 无法再次被选中, 因此动作不会启动两次 。 前端的确认对话框在动作运行时用主按钮进行此操作 。

进展按钮更进一步。 动作完成后,会在绿色按钮上显示检查标记,或在红色按钮上显示警示图标,时间为2秒. 它说,*某事失败了,而不是 "为什么" 当人们需要知道原因时, 还要显示 [错误](/design/patterns/errors) 。

现场演示 `ha-button`,`ha-progress-button`。

```html
<ha-button loading>Save</ha-button>
<ha-progress-button progress>Restart</ha-progress-button>
```

### 摇篮 {#skeletons}

骨架在内容加载时保持布局的布局,所以到达时没有东西会跳动. 前端有 `ha-skeleton`,为常见形状的 `ha-skeleton-text`和 `ha-skeleton-icon` 。 数据表,瓷砖,设备仪表板使用.

现场演示 `ha-skeleton-icon`,`ha-skeleton-text`。 装入时一行数据表:ha-skeleton-icon和ha-skeleton-text.

```html
<div style="display: flex; align-items: center; gap: 16px">
  <ha-skeleton-icon></ha-skeleton-icon>
  <ha-skeleton-text></ha-skeleton-text>
</div>
<div style="display: flex; align-items: center; gap: 16px">
  <ha-skeleton-icon></ha-skeleton-icon>
  <ha-skeleton-text style="--ha-skeleton-text-width: 200px"></ha-skeleton-text>
</div>
```

### 隐形 {#fading-in}

负载指标正在逐渐消失而不是浮出水面,但速度并不相同:

- 骨架在直线消失 超过300毫秒 它代表着内容,所以等待会留下一个空隙,布局应该在哪里.
- ** 一个旋转器或进度栏** 通常等待半秒后才会消失。 一些较慢的地区,如备份和更新,等待一个完整的秒. 当负载在那段时间内完成时,人们从不看到旋转器闪烁和关闭.
- ** 内容本身** 到达后立即ện,没有淡出。

### 装入结束之处 {#where-loading-ends}

装入状态总是以三个位置之一结束:内容,一个[已经空出](/design/patterns/empty-states),或者一个[错误](/design/patterns/errors). 当请求失败时, 千万不要让旋转器运行, 也永远不要显示“ 什么都没有” , 而数据还在路上 。

板牌也遵循同样的规则. 每张卡都处理加载,错误,不可用实体,以及不存在的实体.

## 无障碍 {#accessibility}

- 旋转器具有进步栏的作用,带有翻译的"Loading"标签. 给予一组骨架相同的角色和标签,而不是可见的"Loading"文本.
- 滑石和旋转石保持其意义而不动. 当人们要求减速运动时,Skeletons停止脉冲. 见[动议](/design/foundations/motion).
- 当加载在错误中结束时,显示为人们能够读取的文本,而不仅仅是红色按钮.

## 组件 {#components}

- [旋转器](/design/components/spinner)
- [按钮](/design/components/button) 和[进度按钮](/design/components/progress-button) (韩语)
- [警报](/design/components/alert), 装入失败时

## 在代码中 {#in-code}

```ts
html`
  <ha-spinner size="small"></ha-spinner>
  <ha-button .loading=${this._saving}>Save</ha-button>
  <ha-progress-button .progress=${this._running}>
    Restart
  </ha-progress-button>
`;
```

当进度按钮的动作完成时,请在它上拨打`actionSuccess()`或`actionError()`. 骨架 `ha-skeleton`,`ha-skeleton-text`和`ha-skeleton-icon`,住在[`src/components/skeleton/`](https://github.com/home-assistant/frontend/tree/dev/src/components/skeleton)。

将 ship political politics politions politions policy politics policy policy politics policy policy politics policy policy policy policy polike polike polike polike polike politic , 帮助 帮助 帮助 帮助 帮助 帮助 帮助 帮助

```ts
html`
  <ha-fade-in .duration=${300} easing="ease-in">
    <div role="progressbar" aria-label=${localize("ui.common.loading")}>
      <ha-skeleton-text></ha-skeleton-text>
    </div>
  </ha-fade-in>
  <ha-fade-in .delay=${500}><ha-spinner></ha-spinner></ha-fade-in>
`;
```
