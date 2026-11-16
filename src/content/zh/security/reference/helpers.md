---
title: 安全阖门
description: Home Assistant Core 的助手和处理证书、 编辑、 管理员访问、 网路、 路径和不可信内容的前端 。
order: 1
---

# 安全阖门 {#security-helpers}

所有与安保有关的助手在一页. 指南解释使用时间和原因:[ũ](/security/guides/integrations)和[前端](/security/guides/frontend)。

## 核心 {#core}

### 网络 {#network}

| 帮助者 | 何处 | 它会做什么 |
| --- | --- | --- |
| `async_get_clientsession(hass, verify_ssl=True)` | `homeassistant.helpers.aiohttp_client` | (原始内容存档于2019-09-21). share aiohttp session. 默认检查证书, 并拒绝从网络重定向到回路地址 。 |
| `async_create_clientsession(hass, verify_ssl=True)` | `homeassistant.helpers.aiohttp_client` | 新的aiohttp会话有同样的保护, 因为当你需要自己的, 像饼干。 |
| `get_async_client(hass, verify_ssl=True)` | `homeassistant.helpers.httpx_client` | 共享的HTTPX客户端. 默认检查证书 。 |
| `CONF_VERIFY_SSL` | `homeassistant.const` | 关闭证书检查选项的标准密钥 。 |

### 编辑 {#redaction}

| 帮助者 | 何处 | 它会做什么 |
| --- | --- | --- |
| `async_redact_data(data, to_redact)` | `homeassistant.components.diagnostics` | 将列表中键的值替换为 {H绮}, 也替换为嵌入词典和列表中的值 。 空值和 `None` 保持不变 。 |
| `async_redact_data(data, to_redact)` | `homeassistant.helpers.redact` | 睬一样,但`to_redact`也可以将一个密钥映射到遮蔽值的函数. |
| `partial_redact(value, unmasked_prefix=4, unmasked_suffix=4)` | `homeassistant.helpers.redact` | 保留第一个和最后一个字符,其余的则替换为`***`。 非字符串的短值和值变为 `**REDACTED**` 。 |

### 访问 {#access}

| 帮助者 | 何处 | 它会做什么 |
| --- | --- | --- |
| `async_register_admin_service(hass, domain, service, handler)` | `homeassistant.helpers.service` | 登记一个只有管理员可以调用的动作。 |
| `@websocket_api.require_admin` | `homeassistant.components.websocket_api` | 使命令只管理 WebSocket 。 |
| `@require_admin` | `homeassistant.components.http` | 使 HTTP 视图只能管理的方法 。 |
| `requires_auth` | `HomeAssistantView` | `True` 默认: 视图需要登录用户 。 |

关于实体的检查,见[权限](/core/internals/permissions)。

### 现在我们的 我应该 伙计并作为的投诉开始进行 你还好吗所开展的 这是我们 真的吗嬷以便对在特定 你知道吗 没什么 兄弟可以为呻吟 {#webhooks}

| 帮助者 | 何处 | 它会做什么 |
| --- | --- | --- |
| `async_generate_id()` | `homeassistant.components.webhook` | 由64个随机十六进制字符组成的 Webhook ID. |
| `async_register(..., local_only=True)` | `homeassistant.components.webhook` | 巷道 Home Assistant Link 忽略本地网络以外的请求 。 |
| `async_register(..., allowed_methods=...)` | `homeassistant.components.webhook` | HTTP 方法为 webhook 接受. `POST`和`PUT`默认。 |

### 文件与 URL {#files-and-urls}

| 帮助者 | 何处 | 它会做什么 |
| --- | --- | --- |
| `hass.config.is_allowed_path(path)` | `homeassistant.core_config` | 用户允许的文件夹中是否有路径 。 先决定路径. 屏蔽 I/O : 在执行器中运行 。 |
| `hass.config.is_allowed_external_url(url)` | `homeassistant.core_config` | URL是否从用户允许的外部 URL 开始 。 |

## 前端 {#frontend}

| 帮助者 | 何处 | 它会做什么 |
| --- | --- | --- |
| `filterXSS(html)` | [`src/common/util/xss.ts`](https://github.com/home-assistant/frontend/blob/dev/src/common/util/xss.ts) | 从字符串中删除所有标记,用于必须输入 HTML 字符串的文本。 |
| `sanitizeHttpUrl(url)` | [`src/common/url/sanitize-http-url.ts`](https://github.com/home-assistant/frontend/blob/dev/src/common/url/sanitize-http-url.ts) | 较早的 URL 返回 URL 只有当它是绝对 `http:` 或 `https:` URL 。 |
| `sanitizeLinkUrl(url)` | [`src/common/url/sanitize-http-url.ts`](https://github.com/home-assistant/frontend/blob/dev/src/common/url/sanitize-http-url.ts) | 如 `sanitizeHttpUrl` , 同时也将 `homeassistant://` 的深链接变成前端内部的安全路径 。 |
| `<ha-markdown>` | [`src/components/ha-markdown.ts`](https://github.com/home-assistant/frontend/blob/dev/src/components/ha-markdown.ts) | Renders Markdown,通过标签和属性许可列表过滤. 只用于信任的内容 `allow-svg` 。 |
