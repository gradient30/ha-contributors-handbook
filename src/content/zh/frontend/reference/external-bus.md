---
title: 外部总线
description: 前端和嵌入它的应用程序之间的信息总线,就像伴行的应用程序. 信息是如何发送的, 和每一个信息都是。
order: 4
---

# 外部总线 {#external-bus}

嵌入前端的应用程序,如[辅助应用程序](/companion),可以做浏览器不能做的事情:扫描条码,写NFC标签,委托Matter设备,或者显示本地屏幕. 外部巴士是前端和应用程序如何谈论的. 它在[外部认证](/frontend/reference/external-auth)旁边工作,并使用同样的桥梁. 代码位于[`src/external_app/`](https://github.com/home-assistant/frontend/tree/dev/src/external_app).

## 发送信件 {#sending-messages}

(一) 与《公约》和《公约》有关系;

**从前端到app**,前端使用可用的桥:

```js
// Android, V2: the message is wrapped and serialized
window.externalAppV2.postMessage(
  JSON.stringify({ type: "externalBus", payload: message })
);

// Android, V1: the message is serialized
window.externalApp.externalBus(JSON.stringify(message));

// iOS and macOS: the message is passed as an object
window.webkit.messageHandlers.externalBus.postMessage(message);
```

** 从应用程序到前端**,该应用程序调用前端定义的函数:

```js
window.externalBus(message);
```

## 所开展的工作格式 {#message-format}

每个消息都有 `id` 和 `type`, 当类型需要时有 `payload` :

```ts
interface Message {
  id: number;
  type: string;
  payload?: unknown;
}
```

有些信息需要答案。 答案是 `result` 发一个相同的 `id` 消息 :

```ts
interface SuccessResult {
  id: number;
  type: "result";
  success: true;
  result: unknown;
}

interface ErrorResult {
  id: number;
  type: "result";
  success: false;
  error: { code: string; message: string };
}
```

应用程序到前端的信件是命令,有`type: "command"`,命令名称在`command`中:

```json
{
  "id": 5,
  "type": "command",
  "command": "navigate",
  "payload": { "path": "/config/areas/dashboard" }
}
```

前端以结果回答每个命令. 当两个一般错误代码被发送时, 而不是仅仅用他们的名字:

- `unknown_command`:前端还没有命令处理器,因为它仍在启动中. 命令本身可能很清楚。
- `not_ready`: 命令处理器已经到位, 但是它不处理这个命令 。

两者均由`receiveMessage`在[`src/external_app/external_messaging.ts`](https://github.com/home-assistant/frontend/blob/dev/src/external_app/external_messaging.ts)中发送.

## 从前端到应用程序 {#from-the-frontend-to-the-app}

### 需要答案的信件 {#messages-that-expect-an-answer}

#### 配置/ 获取 {#configget}

前端询问应用程序在连接后能做什么. 有效载荷:无。 应用程序用对象来回答 。 所有密钥都是可选的 :

| 密钥 | 类型 | 含义 |
| --- | --- | --- |
| `hasSettingsScreen` | 布尔 | 该应用程序在 `config_screen/show` 上显示自己的设置 。 |
| `hasSidebar` | 布尔 | 应用程序有自己的侧边栏. |
| `canWriteTag` | 布尔 | 该设备可以写入NFC标记. |
| `hasExoPlayer` | 布尔 | 该应用程序可以使用ExoPlayer在本地播放HLS视频. |
| `canCommissionMatter` | 布尔 | 该应用程序可以委托Matter设备. |
| `hasMatterStatusReport` | 布尔 | 应用程序报告 Matter 用 `matter/commission/finish` 委托结束 。 |
| `canShareMatterDeviceToAppleHome` | 布尔 | 该应用程序可以添加一个Matter设备,该设备在Apple Home中已经拥有,并带有`matter/share_device`. |
| `canShareMatterDeviceToOtherApps` | 布尔 | 该应用程序可以共享 Matter 设备, 该设备 Home Assistant 已经与用户在 Matter 平台的共享工作表中选择的 app , 共享 `matter/share_device` 。 |
| `canImportThreadCredentials` | 布尔 | 该应用程序可以导入Thread证书 。 |
| `canTransferThreadCredentialsToKeychain` | 布尔 | 该应用程序可以在平台的键链中存储Thread证书. 仅限苹果. |
| `hasAssist` | 布尔 | 该应用程序有本地的Assist接口,而不是前端的接口。 |
| `hasAssistSettings` | 布尔 | 该应用程序有设备的 Assist 设置, 在语音助理设置中显示 。 |
| `hasBarCodeScanner` | 编号 | 当应用程序可以扫描条码时, `0` 否则。 |
| `canSetupImprov` | 布尔 | 该应用程序可以设置Improv Wi-Fi设备. |
| `hasEntityAddTo` | 布尔 | 该应用程序可以 有些实体从更多信息对话框中添加到自己的位置, 如部件 。 |
| `hasSplashscreen` | 布尔 | 该兢兢业业的应用程序用自己的加载屏幕覆盖前端,直到`frontend/loaded`. |
| `appVersion` | 字符串 | 应用的版本. |

#### 坛元/ 添加  to/ get  actions {#entityaddtogetactions}

前端询问一个实体在哪里可以添加,比如家用屏幕部件或表面.

有效载荷 :

```ts
{ entity_id: string }
```

答复:

```ts
{
  actions: Array<{
    enabled: boolean;
    name: string;
    details?: string;
    mdi_icon: string;
    app_payload: string;
  }>;
}
```

`name`和`details`按原样显示,所以在应用程序中翻译它们。`mdi_icon`像`mdi:car`一样是一个图标名称。 `app_payload` 是任意字符串, 当用户选择动作时, 前端会随 `entity/add_to` 发回 。

#### 物质/份额 设备 {#mattersharedevice}

前端要求应用程序与另一个平台共享一个Matter设备,如Apple Home. 设备已经设置稠密于 Home Assistant , 而 Home Assistant 为它打开了委托窗口 : 一个很短的时间, 另一个平台也可以添加设备 。 前端在打开窗口的对话框中提供这个.

前端仅在应用程序支持时发送此消息 :

- 有了`canShareMatterDeviceToAppleHome`,它总是提出将设备添加到Apple Home. 当应用程序设置两个键时,这个就赢了.
- 使用 `canShareMatterDeviceToOtherApps` , 它只在 Matter 服务器报告 `discriminator` 和窗口超时时时提供共享工作表 。 股票单打开了自己的窗口,两者都需要。

有效载荷 :

```ts
{
  setup_qr_code: string;
  setup_pin_code: number;
  discriminator?: number;
  vendor_id?: number;
  product_id?: number;
  device_name?: string;
  remaining_seconds?: number;
}
```

| 密钥 | 含义 |
| --- | --- |
| `setup_qr_code` | 调试窗口的QR码有效载荷,从`MT:`开始. 总是发送。 |
| `setup_pin_code` | 委托窗口 很显然是密码 总是送 很显然 |
| `discriminator` | 歧视器件在窗口打开时发布广告, 当 Matter 服务器报告时 。 |
| `vendor_id` | 羚羊  device  vendor  vendor |
| `product_id` | 设备的产品ID, 当 Matter 服务器报告时 。 |
| `device_name` | Home Assistant中的设备名称,向另一个平台推荐. |
| `remaining_seconds` | 估计在窗口关闭前秒, 当 Matter 服务器报告其超时 。 当剩下30秒或更少时,前端将代码视为过期,不发送消息,并请求您获得新的代码. 发送时,此值大于30. |

答:平台流量完成后即为空物体. 失败时, 请用错误结果回答 :

- `canceled`:用户关闭了平台的工作表. 前端将此视为选择,而非错误.
- 其它任何代码, 如 提出的报告 `failed` : 前端显示共享失败, 并有自己的文本 。 它没有显示您的 `message` 。

### 没有答案的信件 {#messages-without-an-answer}

| 类型 | 有效载荷 | 含义 |
| --- | --- | --- |
| `assist/settings` | | 打开应用程序的 Assist 设置 。 |
| `assist/show` | `{ pipeline_id, start_listening }`,可选 | 显示本地 Assist 界面 。 阐释为 `pipeline_id` 是 ID, `"preferred"` 或 `"last_used"` 。 |
| `bar_code/scan` | `{ title, description, alternative_option_label? }` | 斧头扫描仪打开斧头没有 `alternative_option_label`, 请隐藏选项的按钮 。 |
| `bar_code/notify` | `{ message }` | 在条码扫描仪中显示消息 。 |
| `bar_code/close` | | 关闭条码扫描仪 |
| `config_screen/show` | | 打开应用程序的设置 。 |
| `connection-status` | `{ event }` | 连接到 Home Assistant 已更改 。 Illinois `event`是`"connected"`、`"disconnected"`或`"auth-invalid"`。 |
| `entity/add_to` | `{ entity_id, app_payload }` | 添加实体, 由 `app_payload` 从 `entity/add_to/get_actions` 开始 。 |
| `entity/controlled` | `{ entity_ids, domain, service }` | 用户在前端对这些实体做了动作. |
| `exoplayer/play_hls` | `{ url, muted }` | 在本地播放一个 HLS 流 。 |
| `exoplayer/resize` | `{ left, top, right, bottom }` | 将本地玩家移动到这些坐标. |
| `exoplayer/stop` | | 拦住本地玩家. |
| `focus_element` | `{ element_id }` | 聚焦元素 |
| `frontend/loaded` | | 前端已拆除其发射屏. 与`hasSplashscreen`,即第1页之后的版本。 |
| `frontend/reload_and_clear_cache` | | 清除网络视图的缓存并重新装入 。 发送到iOS和macOS只当前端检测到过时的构造时. |
| `haptic` | `{ hapticType }` | 给出随机反馈: `"success"`,`"warning"`,`"failure"`,`"light"`,`"medium"`,`"heavy"`,或`"selection"`。 |
| `improv/scan` | | 扫描Improv Wi-Fi励志设备. |
| `improv/configure_device` | `{ name }` | 用这个名字设置Improv Wi-Fi设备. |
| `matter/commission` | `{ mac_extended_address, extended_pan_id, border_agent_id, active_operational_dataset }`,可选 | 开始启用 Matter 设备 。 有效载荷描述首选的Thread网络. 每个值可以是`null`. |
| `more_info/opened` | `{ entity_id }` | 为此实体打开的更多信息对话框 。 |
| `more_info/closed` | `{ entity_id }` | 向上方的对话框关闭 。 |
| `sidebar/show` | | 显示应用程序的侧边栏 。 |
| `tag/write` | `{ tag, name }` | 打开屏幕来写 NFC 标签 。 `name` 是 `null` 当用户没有给标签命名时 。 |
| `theme-update` | | 主题变了. 更新状态栏和导航栏的颜色。 |
| `thread/import_credentials` | | 从设备中导入 Thread 证书, 然后通过 WebSocket API 发送给 Home Assistant 。 |
| `thread/store_in_platform_keychain` | `{ mac_extended_address, border_agent_id, active_operational_dataset, extended_pan_id }` | 在平台的密钥链中存储 Thread 证书 。 |

## 从应用程序到前端 {#from-the-app-to-the-frontend}

所有命令都会得到结果 成功时 `result` 是 `null` 。

| 命令 | 有效载荷 | 含义 |
| --- | --- | --- |
| `automation/editor/show` | `{ config? }`,可选 | 打开自动化编辑器进行新的自动化. `config`可以填写为`alias`,`description`,`triggers`,`conditions`,`actions`,`mode`和`max`。 |
| `bar_code/scan_result` | `{ rawValue, format }` | 扫描条码 耸起 `format` 是 [条码检测 API 格式](https://developer.mozilla.org/docs/Web/API/Barcode_Detection_API#supported_barcode_formats) 之一, 或 `"unknown"` 。 |
| `bar_code/aborted` | `{ reason }` | 扫描停止了  爸爸 `reason` 是 `"canceled"` 或 `"alternative_options"` 。 |
| `improv/discovered_device` | `{ name }` | 发现了一个Improv Wi-Fi设备. |
| `improv/device_setup_done` | | 安装Improv Wi-Fi设备的工作已经完成. |
| `kiosk_mode/set` | `{ enable }` | 打开或关闭工作站模式 。 |
| `matter/commission/finish` | `{ name, success }` | 启用 Matter 设备结束 。 `name`,当不是`null`时,被提议为新设备的名称.注重 `success: false` , 前端关闭对话框并显示添加设备失败, 除非设备已经出现 。 |
| `navigate` | `{ path, options? }` | 转到一页。 `path` 以 `/` 开头, 如 `/config/voice-assistants/assistants`. `options.replace` 替换当前历史条目, `options.data` 保存在历史状态 。 |
| `notifications/show` | | 打开通知 |
| `restart` | | 重新连接前端到 Home Assistant 。 |
| `sidebar/show` | | 打开侧边栏。 当对话框打开时 `not_allowed` 失败 。 |
| `sidebar/toggle` | | 打开或关闭侧边栏。 当对话框打开时 `not_allowed` 失败 。 |
