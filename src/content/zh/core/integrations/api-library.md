---
title: 构建 {H 大家都} 库
description: 为什么集成通过单独的库与设备交谈,库必须满足什么,以及如何构建认证和数据模型.
sidebarLabel: 构建 {H 大家都} 库
sidebarGroup: 开始
order: 3
---

# 构建 {H 大家都} 库 {#build-a-python-library}

Home Assistant 没有协议代码 。 整合从不构建 HTTP 请求或剖析一个设备的包本身: 它使用在 PyPI 上发布的 Python 库, 这样做 。 该库和Home Assistant之间的集成翻译。 没什么

这保持了集成小而易于审查,让其他人自己使用和测试库. 这页是写图书馆的 这个例子是一个包含JSON的REST API,这是最常见的案例,但结构对其他协议也是有效的.

> [!TIP]
> 设计你自己产品的API? 本地,基于推力的API对Home Assistant最有效. 您的用户会立即得到最新消息, 它继续工作 没有互联网。

## 所需经费 {#requirements}

核心整合所使用的图书馆必须:

- 在PyPI上发布,并配有源发行. 只有二进制包的库不被接受.
- 从公共寄存器中发布, PyPI 上的每个发布都匹配在那里的标记发布 。
- 自动发布, 例如从 GitHub 中发布 。 动作工作流程,不是手工操作.
- 有问题追踪器,如果它与设备或服务交谈。
- 使用 [OSI核准许可证](https://opensource.org/licenses), 用于库及其所依赖的一切, 并在其元数据中声明 。

如果库主要为 Home Assistant 存在, 而您拥有该集成, 请考虑一个将人们指向 [核心问题跟踪器](https://github.com/home-assistant/core/issues) 的问题模板拾取器, 如 [zwave-js- server-python 的一个](https://github.com/home-assistant-libs/zwave-js-server-python/issues/new/choose) 。

Home Assistant更喜欢Aync库. 同步库工作,通过执行器,但每次通话都要花费一条线程. 见[显示在 Home Assistant](/core/internals/asyncio).

## 架构 {#structure}

一个图书馆有两个部分:

- ** 核证**:提出经认证的请求并退回答复。 与API说话的唯一密码.
- **数据模型**:代表API的数据,并提供对此采取行动的方法。

## 4.a(a)的合格后得到过合格后后得到过合格后后得到过过合格后后后得到过过过过过过等等等等等等等等等等等的合格后后才能得到过合格的合格后后后后才能得到过。等等等等等等等等合格后后才能得到合格后后后才能得到合格后后后才能得到过。等等等等等等等等等等等等等等等等等等等等等等等等等等等等等等等等、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、等等、、、、、、、、、、、、、、、、、、、、、、、、、、、、 {#authentication}

认证部分获得令牌,在需要时刷新,并添加到每个请求中. 它不知道这些要求是什么,它也不储存符号:这是使用图书馆的人的工作。 当返回符号时,返回JSON可序列化的东西,比如字符串和数字的`dict`,所以Home Assistant可以存储在配置条目中.

我不知道 如果API可以像本地网络上的一个设备一样在不同的地址,让呼叫者通过主机.

使用`aiohttp`,并让呼叫者通过`ClientSession`。  Home Assistant 有共享的会话, 并创建您自己的成本资源, 并在加载证书时屏蔽事件循环 。

```python
from aiohttp import ClientResponse, ClientSession

class Auth:
    """Make authenticated requests to the API."""

    def __init__(
        self, session: ClientSession, host: str, access_token: str
    ) -> None:
        """Initialize the auth."""
        self.session = session
        self.host = host
        self.access_token = access_token

    async def request(
        self, method: str, path: str, **kwargs
    ) -> ClientResponse:
        """Make a request."""
        headers = dict(kwargs.pop("headers", None) or {})
        headers["authorization"] = f"Bearer {self.access_token}"

        return await self.session.request(
            method, f"{self.host}/{path}", **kwargs, headers=headers
        )
```

使用它, 在 Home Assistant 之外 :

```python
import asyncio

import aiohttp

from my_library import Auth

async def main() -> None:
    async with aiohttp.ClientSession() as session:
        auth = Auth(session, "http://example.com/api", "secret_token")

        response = await auth.request("get", "lights")
        print(response.status, await response.json())

asyncio.run(main())
```

### 授权 2 {#oauth-2}

有了OAuth 2,访问符在短时间后过期,刷新符会得到新的. 刷新需要客户端的ID和秘密,这些用户可能完全住在别的地方:Home Assistant可以通过连接Home Assistant Link服务的账户刷新符号,所以用户不需要自己的开发者账户.

所以,让打电话者决定如何获得有效的代币. 一种抽象的方法可以做到:

```python
from abc import ABC, abstractmethod

from aiohttp import ClientResponse, ClientSession

class AbstractAuth(ABC):
    """Make authenticated requests to the API."""

    def __init__(self, session: ClientSession, host: str) -> None:
        """Initialize the auth."""
        self.session = session
        self.host = host

    @abstractmethod
    async def async_get_access_token(self) -> str:
        """Return a valid access token."""

    async def request(
        self, method: str, path: str, **kwargs
    ) -> ClientResponse:
        """Make a request."""
        headers = dict(kwargs.pop("headers", None) or {})
        access_token = await self.async_get_access_token()
        headers["authorization"] = f"Bearer {access_token}"

        return await self.session.request(
            method, f"{self.host}/{path}", **kwargs, headers=headers
        )
```

在集成中,子类从 Home Assistant 的 OAuth 2 帮助器获得符号, 必要时可以刷新. 见[整合中的 OAuth 2](/core/integrations/oauth2).

## 数据模型 {#data-models}

以 API 的方式表示数据 。 保留名称和结构,即使API设计是奇异的或者里面有打字. 阅读 API 文档的人,应该在您的图书馆中找到自己的方式,不需要翻译表.

尽量少做点 一个库代表数据,它不解释它。 例如,不要将摄氏转换成华氏:这涉及到环绕和精确性的选择,那些属于使用图书馆的人。

说API有这些终点:

- `GET /lights`: 所有灯光,作为一个列表。
- `GET /light/<id>`:一个光,像`{"id": 1234, "name": "Desk", "is_on": true}`。
- `POST /light/<id>`:用`{"is_on": false}`控制灯光。 返回新状态 。

灯的类:

```python
from typing import Any

from .auth import Auth

class Light:
    """A light of the ExampleHub API."""

    def __init__(self, raw_data: dict[str, Any], auth: Auth) -> None:
        """Initialize the light."""
        self.raw_data = raw_data
        self.auth = auth

    @property
    def id(self) -> int:
        """Return the ID of the light."""
        return self.raw_data["id"]

    @property
    def name(self) -> str:
        """Return the name of the light."""
        return self.raw_data["name"]

    @property
    def is_on(self) -> bool:
        """Return whether the light is on."""
        return self.raw_data["is_on"]

    async def async_control(self, is_on: bool) -> None:
        """Turn the light on or off."""
        response = await self.auth.request(
            "post", f"light/{self.id}", json={"is_on": is_on}
        )
        response.raise_for_status()
        self.raw_data = await response.json()

    async def async_update(self) -> None:
        """Fetch the latest data of the light."""
        response = await self.auth.request("get", f"light/{self.id}")
        response.raise_for_status()
        self.raw_data = await response.json()
```

而API的切入点:

```python
from .auth import Auth
from .light import Light

class ExampleHubAPI:
    """Talk to the ExampleHub API."""

    def __init__(self, auth: Auth) -> None:
        """Initialize the API."""
        self.auth = auth

    async def async_get_lights(self) -> list[Light]:
        """Return all lights."""
        response = await self.auth.request("get", "lights")
        response.raise_for_status()
        return [Light(data, self.auth) for data in await response.json()]

    async def async_get_light(self, light_id: int) -> Light:
        """Return one light."""
        response = await self.auth.request("get", f"light/{light_id}")
        response.raise_for_status()
        return Light(await response.json(), self.auth)
```

提高您自己对错误的例外, 如 `ExampleHubAuthenticationError` 和 `ExampleHubConnectionError` , 因此整合可以从离线的设备中分辨出错误的密码 。 整合需要这种差异才能开始重新校正或稍后再试.

## 在 Home Assistant 尝试您的库 {#try-your-library-in-home-assistant}

在发布前, 在您的[发展环境](/core/development/environment) 虚拟环境中以可编辑模式安装您的库 。 从您的核心检出中运行此选项, 并将库放在其旁边的文件夹中 :

```shell
uv pip install -e ../my-library
```

这条路用手动设置 开发容器中只挂载了您的核心检出, 所以复制容器内的库, 如 `~/my-library` , 然后从那里安装 。 [教程](/core/integrations/tutorial#1-start-with-the-library) 显示两个设置 。

然后开始 Home Assistant 而不让它在您身上安装已发布的版本 :

```shell
hass --skip-pip-packages my-library
```

一旦工作成功,就发布一个发布,并在您整合的[显示](/core/integrations/manifest)的`requirements`中设定版本.
