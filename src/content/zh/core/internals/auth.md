---
title: 认证工作方式
description: Home Assistant中的用户、组、证书和令牌,以及验证某人身份的认证提供者和多要素模块。
sidebarLabel: 认证工作方式
sidebarGroup: 4.a(a)的合格后得到过合格后后得到过合格后后得到过过合格后后后得到过过过过过过等等等等等等等等等等等的合格后后才能得到过合格的合格后后后后才能得到过。等等等等等等等等合格后后才能得到合格后后后才能得到合格后后后才能得到过。等等等等等等等等等等等等等等等等等等等等等等等等等等等等等等等等、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、等等、、、、、、、、、、、、、、、、、、、、、、、、、、、、
order: 20
---

# 认证工作方式 {#how-authentication-works}

Home Assistant有自己的认证系统。 它生活在 [`homeassistant/auth/`](https://github.com/home-assistant/core/tree/dev/homeassistant/auth) 中, 而`hass.auth` 是保存它的认证管理器 。 本页解释其部分内容. 要让一个应用程序登录到 Home Assistant, 请参见 [认证 API](/core/internals/auth-api) 。 要检查用户可以做什么,请参见[权限](/core/internals/permissions).

## 各个部分 {#the-parts}

- **用户**:每个人,以及每个向Home Assistant说话的系统过程都是用户. 登机时创建的用户为**所有者**. 拥有者可以管理其他用户,并始终拥有所有许可.
- **群**:用户是一个或多个群的成员,群携带[许可政策](/core/internals/permissions). Home Assistant有三个:管理员(`system-admin`),用户(`system-users`),和只读用户(`system-read-only`).
- 梢** 认证提供者**:验证某人是谁,通常使用用户名和密码. 下更详.
- ** 证书**:证明某人经特定认证提供者认证的证据。 身份证明链接给用户。 一个用户可以拥有几个提供者的证书,但每个提供者只能有一个.
- ** 新鲜的令牌和访问令牌**:一个应用程序在登录后会得到什么. 下更详.

## 键 {#tokens}

当有人登录到一个应用软件时,该应用软件得到两个符号:

- 有效时间为30分钟。 它与每一个请求 APIs。
- 一个**新鲜的代币**,用来在旧代币到期时获得新的访问代币. 刷新令牌在90天未使用时过期,用户可以随时从他们的配置中撤销.

刷新符号分为三种类型:

- ** 正常**:当用户登录到应用程序时创建. 应用程序为用户保存.
- ** 长寿访问符**:背面是一个用户在其配置文件上创建的长寿访问符. 刷新标志本身从未向任何人展示.
- **System**:仅供系统用户使用,如Supervisor. 从不向任何人展示。

## 认证提供者 {#auth-providers}

认证提供者确认某人是谁。 它定义了一个登录流,它建立在与[配置流量](/glossary/config-flow)相同的数据输入流机制上,它要求它需要什么:一个用户名和密码,一个代码,或者什么都没有. 当流量成功时,提供者会手动Home Assistant一个`Credentials`对象.

Home Assistant这些供应商在[`homeassistant/auth/providers/`](https://github.com/home-assistant/core/tree/dev/homeassistant/auth/providers)中的船:

- `homeassistant`:存储在配置目录中的用户名和密码. 这是未配置 `auth_providers` 时使用的 Home Assistant 提供者 。
- `trusted_networks`: 登录时没有配置网络的密码 。
- `command_line`:用外部命令验证用户名和密码。
- `insecure_example`:开发与测试的典范. 配置验证在 {H1 55. 中拒绝, 因为它只用于测试 。

是一项在 `configuration.yaml` 的 `homeassistant:` 区域中, 用户配置哪些提供者在 `auth_providers:` 下活动 。 同一提供商可能有几个例子,每个都有自己的`id`. 他们不分享全权证书。

> [!NOTE]
> 仅支持内置的 auth 提供者 。 自定义集成不能添加一个 。

### 构建一个认证提供者 {#build-an-auth-provider}

提供者是 [`homeassistant/auth/providers/`](https://github.com/home-assistant/core/tree/dev/homeassistant/auth/providers) 中执行两个类的模块 。 看`insecure_example.py` 对于一个完整的,小的例子。

`AuthProvider` 子类执行 :

| 就在那时 | 要求数 | 说明 |
| --- | --- | --- |
| `async_login_flow(context)` | 对 | 返回 `LoginFlow` 供某人登录 。 |
| `async_get_or_create_credentials(flow_result)` | 对 | 返回 `Credentials` 以获取已完成的登录流量结果 。 现有或新的。 |
| `async_user_meta_for_credentials(credentials)` | No | 返回 `UserMeta` , 并附上像名称一样的新用户名 。 |

`LoginFlow` 子类执行`async_step_init` 。 流动的第一步总是`init`:

```python
async def async_step_init(
    self, user_input: dict[str, str] | None = None
) -> AuthFlowResult:
    """Ask for and check the username and password."""
    errors: dict[str, str] = {}

    if user_input is not None:
        try:
            self._auth_provider.async_validate_login(
                user_input["username"], user_input["password"]
            )
        except InvalidAuthError:
            errors["base"] = "invalid_auth"
        else:
            user_input.pop("password")
            return await self.async_finish(user_input)

    return self.async_show_form(
        step_id="init", data_schema=LOGIN_SCHEMA, errors=errors
    )
```

不要将密码传递到 `async_finish` : 流量的结果就是提供者变成证书 。

`async_finish`从那里接手:如果用户设置了多要素模块,则在创建证书之前,流量会与这些模块继续.

## 多要素认证模块 {#multi-factor-authentication-modules}

多要素认证模块(MFA)为登录增加了第二步,仅次于认证提供者. 一个用户可以设置几个模块,在登录时选择一个模块. Home Assistant这些在[`homeassistant/auth/mfa_modules/`](https://github.com/home-assistant/core/tree/dev/homeassistant/auth/mfa_modules)中的船:

- `totp`:来自认证器应用程序的基于时间的一次性密码.
- `notify`:通过通知动作发送的一次性密码.
- `insecure_example`:开发与测试的典范.

用户在 `auth_mfa_modules:` 的 `homeassistant:` 一节中配置它们 。 没有那个键, Home Assistant 负载`totp` 。 和认证提供者一样,只支持内置模块.

### 构建外交部模块 {#build-an-mfa-module}

为其模块是`MultiFactorAuthModule`在[`homeassistant/auth/mfa_modules/`](https://github.com/home-assistant/core/tree/dev/homeassistant/auth/mfa_modules)中的子类. 完整的示例见`insecure_example.py`。

| 就在那时 | 要求数 | 说明 |
| --- | --- | --- |
| `input_schema` | 对 | 用户登录时填写表单的图案属性 。 |
| `async_setup_flow(user_id)` | 对 | 返回为用户设置模块的 `SetupFlow` 。 |
| `async_setup_user(user_id, setup_data)` | 对 | 为用户设置模块. |
| `async_depose_user(user_id)` | 对 | 删除为用户存储的所有模块 。 |
| `async_is_user_setup(user_id)` | 对 | 返回模块是否为用户设置 。 |
| `async_validate(user_id, user_input)` | 对 | 返回用户输入的内容是否有效 。 |
| `async_initialize_login_mfa_step(user_id)` | No | 在登录的 MFA 步骤显示前调用, 就像 `notify` 模块发送代码一样 。 |

用户从其配置设置模块. 设置也是数据输入流,为`SetupFlow`的子类. 对于 `totp` ,墅流生成一个秘密, 显示为 QR 代码, 并请求一个代码来确认认证器的应用和时钟一致 。 只有这样,才能为用户启用模块。

MFA步骤有时间限制:当登录开始后超过5分钟时,登录流在调用`async_validate`前以`login_expired`中止. 您的模块只检查代码 。
