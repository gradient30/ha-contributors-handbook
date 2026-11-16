---
title: 安全融合
description: 证书,证书,编辑,只管理权限,webhooks,以及文件路径. 保证融合安全的规律和帮助者.
sidebarLabel: 一体化
order: 1
---

# 安全融合 {#secure-integrations}

一个 [融合](/glossary/integration) 运行在 Home Assistant Core 内部, 在同一过程中, 访问所有 。 它与网络上的设备和服务交谈,它存储用户的证书,并且它可以向Home Assistant添加新的方式,比如动作,WebSocket命令,和webhooks. 每一个地方都是错的

好消息是 Home Assistant几乎每个人都有帮手 此指南显示要使用哪个, 以及原因 。 将 Home Assistant 信任的较大图片改为 [Home Assistant 如何处理信任](/security/how-it-works) 首先是 。

## 和网络安全交谈 {#talk-to-the-network-safely}

### 使用共享的网络会话 old {#use-the-shared-web-session}

从 Home Assistant 获取您的 HTTP 会话, 并将其传递到您的库 :

```python
from homeassistant.helpers.aiohttp_client import async_get_clientsession

session = async_get_clientsession(hass)
client = ExampleClient(entry.data[CONF_HOST], session=session)
```

对于HTTPX,使用`get_async_client(hass)`从`homeassistant.helpers.httpx_client`开始. 两者默认都检查SSL证书 (`verify_ssl=True`). aiohttp会话还拒绝从网络上的地址转向本地机器本身(一个回路地址),这可以防止服务器侧请求的伪造.

通过会话也是质量尺度的一条规则:[泻入网会话](/core/quality-scale/inject-websession).

### 继续检查证书 {#keep-certificate-checks-on}

不默认关闭证书检查 。 有些设备只有自签名的证书,然后用户需要一条出路. 在 [配置流量](/glossary/config-flow) 中使其成为一个选项, 并默认进行检查, 如 Core 中的多个集成 :

```python
from homeassistant.const import CONF_VERIFY_SSL

STEP_USER_DATA_SCHEMA = probatio.Schema(
    {
        probatio.Required(CONF_HOST): str,
        probatio.Required(CONF_VERIFY_SSL, default=True): bool,
    }
)
```

然后将用户的选择传递给会话 :

```python
session = async_get_clientsession(hass, entry.data[CONF_VERIFY_SSL])
```

证书检查问题。 2025年的咨询在Core及其使用的图书馆中约为[SSL 向外请求的验证](https://github.com/home-assistant/core/security/advisories/GHSA-m3pm-rpgg-5wj6).

## 保密 保密 {#keep-secrets-secret}

### 在配置条目中存储证书 {#store-credentials-in-the-config-entry}

全权证书和连接细节属于`data`的`data`,而不是它的`options`。 选项用于在 [选项流动](/glossary/options-flow) 中用户稍后更改的设置 。

当证书停止在这一问题上工作时,请向用户询问使用 [重新校正流量](/glossary/reauthentication) 的新证书,而不再次设置集成 。

### 校正诊断 {#redact-diagnostics}

用户在公共议题中贴出[诊断](/glossary/diagnostics). 通过 `async_redact_data` 将所有私密文件传递给 `**REDACTED**`, 它将您列出的密钥的值替换为 `**REDACTED**`, 也可以在嵌入词典和列表中 :

```python
from homeassistant.components.diagnostics import async_redact_data

TO_REDACT = {CONF_API_KEY, CONF_PASSWORD, "serial_number"}

return {"entry_data": async_redact_data(entry.data, TO_REDACT)}
```

超越密码思考:符号,坐标,地址,姓名,电子邮件地址,以及序列号. 包括测试在内的全景请参见[诊断](/core/integrations/diagnostics).

### 保存日志中的秘密 {#keep-secrets-out-of-logs}

用户在报告问题时也会对问题附加调试日志. 当一个日志行需要识别一个密钥或一个ID时,用`homeassistant.helpers.redact`的`partial_redact`遮盖它的大部分. 它保留了前4和后4个字符,并完全替换短值:

```python
from homeassistant.helpers.redact import partial_redact

_LOGGER.debug("Using API key %s", partial_redact(api_key))
```

同一模块有自己的`async_redact_data`. 它还一间接受从密钥到函数方面的努力,这样你就可以遮掩部分的值而不是去除它.

## 把进来的东西当不信任的东西 {#treat-what-comes-in-as-untrusted}

从设备中获取的数据,云服务,或用户可以被错误地用到,也可以是故意设计的。

- 用计划验证用户的输入. 参见 [正在验证输入](/core/development/input-validation). Home Assistant 在您的处理器运行前检查一个动作相对于其策略的数据, 所以你不需要再次检查这些字段 。
- 车站的车站和车站 查一下,你到底在说什么?
- 当一个值进入一个URL或一个文件路径时,首先对照一个严格的模式来检查它,就像一个swit. 否则其中的 `../` 或 `?` 可以指向其它地方 。
- 永远不要将外部数据传递给`eval()`,`exec()`,或者一个 shell. Ruff, 核心的linter, 旗帜 `exec` (`S102`), `eval` (`S307`), 和 `subprocess` 与 `shell=True` (`S602`), 以及其他危险电话.

với这个界面:设备名称或实体名称到达仪表板和卡片。 前端必须视之为无信. 见[前端未信任的内容](/security/guides/frontend).

## 守住这里 {#guard-the-ways-in}

每个动作,WebSocket命令,HTTP视图,和webhook,你加进Home Assistant的新门. 决定谁可以使用它。

### 仅管理动作 {#admin-only-actions}

改变配置或具有其他安全影响的动作,应当需要管理员用户. 以 `async_register_admin_service` 注册, 检查此选项 :

```python
from homeassistant.helpers.service import async_register_admin_service

async_register_admin_service(
    hass, DOMAIN, "clear_cache", async_handle_clear_cache
)
```

对实体采取行动的行为也需要检查许可。 见[权限](/core/internals/permissions).

### 仅管理 WebSocket 命令 {#admin-only-websocket-commands}

把 `require_admin` 装饰器放在上面 :

```python
@websocket_api.require_admin
@websocket_api.websocket_command({probatio.Required("type"): "example/info"})
@websocket_api.async_response
async def handle_info(
    hass: HomeAssistant,
    connection: websocket_api.ActiveConnection,
    msg: dict[str, Any],
) -> None:
    """Return information about the example."""
```

### HTTP 视图 {#http-views}

a `HomeAssistantView` 默认需要登录用户 (`requires_auth = True`) 。 只在没有其他方法时设定 `requires_auth = False`, 然后赃物自己检查请求, 在视图的每一种方法中 必须: `get` 最多 `post` 和 `put` 。 对于只有管理员才能使用的视图,将处理器装饰为`require_admin`从`homeassistant.components.http`调来的`require_admin`:

```python
from homeassistant.components.http import HomeAssistantView, require_admin

class ExampleUploadView(HomeAssistantView):
    """Accept an upload from an admin."""

    url = "/api/example/upload"
    name = "api:example:upload"

    @require_admin
    async def post(self, request: web.Request) -> web.Response:
        """Handle the upload."""
```

### 现在我们的 我应该 伙计并作为的投诉开始进行 你还好吗所开展的 这是我们 真的吗嬷以便对在特定 你知道吗 没什么 兄弟可以为呻吟 {#webhooks}

只有 表 这是个 什么是 过来 知道吗 ―的各项活动有助于实现并制定 原来广泛地 没事的能够获得是按照 这让身份证成为秘密 用 `webhook.async_generate_id()` 生成它, 它返回64 个随机十六进制字符 。

当调用您的 Webhook 的设备或服务在本地网络上时, 仅将其注册为本地 :

```python
webhook.async_register(
    hass, DOMAIN, entry.title, entry.entry_id, handle_webhook, local_only=True
)
```

Home Assistant 然后忽略来自本地网络以外的请求, 或者通过Home Assistant Link 。 它用 `200 OK` 记录一个警告和答案, 所以呼叫者不会学到任何东西。 Webhooks默认接受`POST`和`PUT`. 如果您需要其它东西, 请使用 `allowed_methods` 。

2023年的咨询大约是[从外部可到达的仅本地的网点](https://github.com/home-assistant/core/security/advisories/GHSA-wx3j-3v2j-rf45),通过Home Assistant Link的远程连接.

## 检查文件路径 {#check-file-paths}

当用户给您一个读写路径时, 如要保存快照的文件夹, 对照配置为 `hass.config.is_allowed_path()` 的用户的许可列表检查它 。 它首先解决了路径,所以`..`的诡计无法通过. 它确实屏蔽了I/O,所以在执行器中运行:

```python
allowed = await hass.async_add_executor_job(
    hass.config.is_allowed_path, file_path
)
if not allowed:
    raise ServiceValidationError(
        translation_domain=DOMAIN,
        translation_key="path_not_allowed",
        translation_placeholders={"path": file_path},
    )
```

对于 URL,`hass.config.is_allowed_external_url()` 对允许的外部 URL 做同样的事情.

## 以前发生什么了? {#what-went-wrong-before}

这些[过去的建议](/security/reference/advisories)是关于整合和核心的。 每张地图都映射到本指南的一个部分。

- ** HTTP 视图没有登录,只检查一些方法。 ** 遗留的 Konnected 集成在 `POST` 和 `PUT` 上检查了一个符号, 但是 [(原始内容存档于2019-09-05) (中文(简体) ).](https://github.com/home-assistant/core/security/advisories/GHSA-x84v-g949-293w) 。 见 [HTTP 视图](/security/guides/integrations#http-views) 。
- ** 登录前的信息。 ** 登录页面向本地网络上的任何人显示 [所有用户账户](https://github.com/home-assistant/core/security/advisories/GHSA-jqpc-rc7g-vf83) 。
- ** 当地人员与信任人员不同。 ** 本地唯一的webhooks是[可从互联网上获取](https://github.com/home-assistant/core/security/advisories/GHSA-wx3j-3v2j-rf45)通过Home Assistant Cloud的远程连接,现在是Home Assistant Link。见[网点](/security/guides/integrations#webhooks)。
- ** 请求路径中的外部数据。 ** 一个动作域最终在 [请求 Supervisor API](https://github.com/home-assistant/core/security/advisories/GHSA-4r74-h49q-rr3h) 的路径中 。 见[把进来的东西当作不信任](/security/guides/integrations#treat-what-comes-in-as-untrusted)。
- ** 注销的证明支票无人注意到。 ** a50k 参数为 {طار العب المل المل المل المل المل المل العر العر المر ال ال ال العار الري ال البار الري ال الري ال .

## 相关 {#related}

- [安全阖门](/security/reference/helpers):所有帮助者在一页.
- 世界 [依赖性和供应链](/security/guides/dependencies) : Home Assistant 向库询问您的整合用途 。
- [4.a(a)的合格后得到过合格后后得到过合格后后得到过过合格后后后得到过过过过过过等等等等等等等等等等等的合格后后才能得到过合格的合格后后后后才能得到过。等等等等等等等等合格后后才能得到合格后后后才能得到合格后后后才能得到过。等等等等等等等等等等等等等等等等等等等等等等等等等等等等等等等等、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、等等、、、、、、、、、、、、、、、、、、、、、、、、、、、、](/core/internals/auth)和[权限](/core/internals/permissions):用户、组和权限检查。
