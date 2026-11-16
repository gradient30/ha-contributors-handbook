---
title: OAuth 2.0 与应用凭证
description: 用 OAuth 2.0 连接用户的账户, 让 Home Assistant 为您处理 。
sidebarLabel: OAuth 2.0
sidebarGroup: 设置与配置
order: 7
---

# OAuth 2.0 和应用程序证书 {#oauth-20-and-application-credentials}

许多云服务让用户将其账户链接到OAuth 2.0:用户登录在服务网站上,Home Assistant获得一个符号. Home Assistant在 `homeassistant.helpers.config_entry_oauth2_flow` 中有全局的助手: 配置流, 存储符, 刷新, 处理错误 。 你不执行任何 自己。

最快速的开始是脚手架脚本:

```shell
python3 -m script.scaffold config_flow_oauth2
```

## 如何融为一体 {#how-it-fits-together}

OAuth 2.0需要客户端ID和客户端秘密:在服务处注册的应用程序的证书. 用户有两种方式:

- ** 申请证明**:用户在服务处登记自己的申请,并在Home Assistant中输入客户身份和秘密。 每个支持OAuth 2.0的集成必须支持这一点.
- QQH0}账户链接**:Nabu Casa在服务中注册了一个应用程序,因此拥有订阅功能的用户可以在不注册任何内容的情况下链接他们的账户. 这提供了最佳的经验。 要加入您的整合, 请联系 [合作伙伴@ openhomefoundation.org](mailto:partner@openhomefoundation.org) 。

两者最终都作为执行,一个`AbstractOAuth2Implementation`的子类. 配置流程允许用户在有多个时选择一个时光,并使用它登录.

您的库必须建立, 这样 Home Assistant 可以刷新符号 : 它在每次请求前要一个有效的符号, 而不是处理刷新本身 。 如何构建, 请参见 [在您的 API 库中的 OAuth 2](/core/integrations/api-library#oauth-2) 。

## 申请证书 {#application-credentials}

在您的 [显示](/core/integrations/manifest#dependencies) 中添加 `application_credentials` 到 `dependencies` , 用服务授权服务器的 URL 创建 `application_credentials.py` :

```python
from homeassistant.components.application_credentials import (
    AuthorizationServer,
)
from homeassistant.core import HomeAssistant

async def async_get_authorization_server(
    hass: HomeAssistant,
) -> AuthorizationServer:
    """Return the authorization server."""
    return AuthorizationServer(
        authorize_url="https://example.com/oauth/authorize",
        token_url="https://example.com/oauth/token",
    )
```

`authorize_url`是用户登录的地方。 `token_url`是 Home Assistant 得到和刷新符号的地方 。

### 自定义执行 {#a-custom-implementation}

如果服务做了特殊的事情, 请从 `async_get_auth_implementation` 返回您自己的执行 。 例如,对于需要[捷克](https://www.rfc-editor.org/rfc/rfc7636)的服务:

```python
from homeassistant.components.application_credentials import (
    ClientCredential,
)
from homeassistant.helpers.config_entry_oauth2_flow import (
    AbstractOAuth2Implementation,
    LocalOAuth2ImplementationWithPkce,
)

async def async_get_auth_implementation(
    hass: HomeAssistant, auth_domain: str, credential: ClientCredential
) -> AbstractOAuth2Implementation:
    """Return an implementation that uses PKCE."""
    return LocalOAuth2ImplementationWithPkce(
        hass,
        auth_domain,
        credential.client_id,
        authorize_url="https://example.com/oauth/authorize",
        token_url="https://example.com/oauth/token",
        

# Optional, defaults to an empty string {#help-users-create-credentials}
        client_secret=credential.client_secret,
        

# Optional, between 43 and 128, defaults to 128 {#credentials-from-yaml}
        code_verifier_length=128,
    )
```

对于其他更改, 应用证书集成的子类 `AuthImplementation` 并覆盖您需要的 。

### 帮助平等原则本身就是一个问题。 {#the-config-flow}

协助发展中国家在 `strings.json` 和 `application_credentials` 下创建证书 :

```json
{
  "application_credentials": {
    "description": "Create credentials in the [console]({console_url})."
  }
}
```

在 `application_credentials.py` 中将 `console_url` 等占位符填充为 `async_get_description_placeholders`, 所以 URL 不被翻译 :

```python
async def async_get_description_placeholders(
    hass: HomeAssistant,
) -> dict[str, str]:
    """Return the placeholders for the credentials dialog."""
    return {"console_url": "https://example.com/developers"}
```

### YAML 的全权证书 {#reauthentication}

新集成在 `configuration.yaml` 中不能接受证书: 用户在 UI 中输入它们. 用于接受它们的整合可以以 `async_import_client_credential` 移动它们 :

```python
from homeassistant.components.application_credentials import (
    ClientCredential,
    async_import_client_credential,
)

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Import credentials from YAML."""
    if DOMAIN in config:
        await async_import_client_credential(
            hass,
            DOMAIN,
            ClientCredential(
                config[DOMAIN][CONF_CLIENT_ID],
                config[DOMAIN][CONF_CLIENT_SECRET],
            ),
        )

    return True
```

## 配置流 : {#make-authenticated-requests}

扩展`AbstractOAuth2FlowHandler`。 它已经拥有 `user` 步骤, 选择执行, 发送用户到服务, 并接收符号 。 您设置了域和一个日志, 并添加 `extra_authorize_data` 中需要的服务范围和其他参数 :

```python
import logging
from typing import Any

from homeassistant.helpers import config_entry_oauth2_flow

class OAuth2FlowHandler(
    config_entry_oauth2_flow.AbstractOAuth2FlowHandler, domain=DOMAIN
):
    """Handle the OAuth 2.0 config flow of Example."""

    DOMAIN = DOMAIN

    @property
    def logger(self) -> logging.Logger:
        """Return the logger."""
        return logging.getLogger(__name__)

    @property
    def extra_authorize_data(self) -> dict[str, Any]:
        """Return extra parameters for the authorize URL."""
        return {"scope": "read write offline_access"}
```

当登录成功时,帮助者会用数据调用`async_oauth_create_entry`,包括符号. 默认情况下,它会创建一个以执行名称为标题的条目。 覆盖它设置一个独特的ID,一个更好的标题,或者为[处理重校正](/core/integrations/oauth2#reauthentication).

### 重新校正 {#errors}

Tokens可以永远变得无效,例如当用户在服务中取消访问时. Home Assistant 然后启动 [重新校正流量](/core/integrations/reauth-reconfigure#reauthentication) 。 对于OAuth 2.0,这意味着再次登录:

```python
from collections.abc import Mapping

from homeassistant.config_entries import SOURCE_REAUTH, ConfigFlowResult

async def async_step_reauth(
    self, entry_data: Mapping[str, Any]
) -> ConfigFlowResult:
    """Start reauthentication."""
    return await self.async_step_reauth_confirm()

async def async_step_reauth_confirm(
    self, user_input: dict[str, Any] | None = None
) -> ConfigFlowResult:
    """Tell the user they need to log in again."""
    if user_input is None:
        return self.async_show_form(step_id="reauth_confirm")

    return await self.async_step_user()

async def async_oauth_create_entry(
    self, data: dict[str, Any]
) -> ConfigFlowResult:
    """Create an entry, or update it during reauthentication."""
    account = await get_account(self.hass, data["token"])
    await self.async_set_unique_id(account.id)

    if self.source == SOURCE_REAUTH:
        self._abort_if_unique_id_mismatch()
        return self.async_update_reload_and_abort(
            self._get_reauth_entry(), data_updates=data
        )

    self._abort_if_unique_id_configured()

    return self.async_create_entry(title=account.name, data=data)
```

总是执行重新校正,这样用户就可以再次链接他们的账户,而不移除集成.

## 提出经认证的请求 {#提出经认证的请求}

在 `async_setup_entry` 中创建 `OAuth2Session` 。 它保持了符号的有效性,并在配置条目中存储刷新符号:

```python
from homeassistant.helpers.config_entry_oauth2_flow import (
    OAuth2Session,
    async_get_config_entry_implementation,
)

async def async_setup_entry(
    hass: HomeAssistant, entry: ExampleConfigEntry
) -> None:
    """Set up Example from a config entry."""
    implementation = await async_get_config_entry_implementation(
        hass, entry
    )
    session = OAuth2Session(hass, entry, implementation)

    coordinator = ExampleCoordinator(
        hass, entry, ExampleClient(session)
    )
    await coordinator.async_config_entry_first_refresh()

    entry.runtime_data = coordinator

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
```

每次请求前,库会拨打`await session.async_ensure_token_valid()`,必要时会刷新符号,然后从`session.token["access_token"]`读取符号. 在库中保留符号处理,设置,或协调器,从不在实体代码中.

## 错误 {#错误}

当一个令牌请求失败时, 帮助者会从 `homeassistant.exceptions` 中提出一个例外 。 每个也都是一个配置条目例外,其中说明应该发生什么,并附有一个翻译消息,所以你不必将其映射或添加到`strings.json`中.

| 例外 | 原因 | 还a |
| --- | --- | --- |
| `OAuth2TokenRequestReauthError` | HTTP 状态 400 到غار 499, 429除外 | `ConfigEntryAuthFailed` |
| `OAuth2TokenRequestTransientError` | HTTP 状态 429 或 500至 599 | `ConfigEntryNotReady` |
| `OAuth2TokenRequestError` | 其他HTTP状态. 以上二门之基类. | `ConfigEntryNotReady` |
| `OAuth2TokenRequestConnectionError` | 没有反应,或者没有可用信号的响应 | `ConfigEntryNotReady` |

`async_get_config_entry_implementation`工作方式相同:它提高了`ImplementationUnavailableError`(a `ConfigEntryNotReady`)或`UnknownImplementationError`(a `ConfigEntryAuthFailed`). 对于后向兼容性,令牌请求例外也继承了`aiohttp.ClientResponseError`,和`OAuth2TokenRequestConnectionError`继承了`aiohttp.ClientError`. 当 `async_ensure_token_valid` 升起 `OAuth2TokenRequestReauthError` 时, 它已经开始重新校正流 。

因此,让这些例外宣传:

- ** 与协调员**合作,你不需要处理任何错误。 `OAuth2TokenRequestReauthError` 开始重新校正, 其他人则算作一个已重试的失败更新 。 在 `async_setup_entry` 中进行第一次刷新, 如上面的例子一样, 因此在实体设置前会检查符号 。
- ** 没有协调员**,请在`async_setup_entry`中拨打`await session.async_ensure_token_valid()`。 Home Assistant 然后重试设置, 或者开始重新校正 。

只有当您的整合需要不同行为时, 才会抓住其中之一, 例如提高 `ConfigEntryError` 的状态, 对于此服务是永久的 。 抓住最具体的例外 让剩下的人过去
