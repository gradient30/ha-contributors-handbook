---
title: 添加一个带有入口的网页界面
description: 在 Home Assistant 中显示你应用程序的网页界面，由 Home Assistant 负责身份验证。
order: 6
---


# 添加一个带有入口的网页界面 {#add-a-web-interface-with-ingress}
Ingress 在 Home Assistant 用户界面中显示应用的网页界面，如果用户需要的话，还可以有自己的侧边栏入口。Home Assistant 处理登录，所以用户不需要单独的密码，你也不需要在主机上开放端口。它还为你的应用提供最佳的[安全评分](/apps/reference/security-rating)。

如果你的应用有网页界面，请使用 Ingress。

## 工作原理 {#how-it-works}
浏览器通过类似 `/api/hassio_ingress/<token>/` 的 URL 与 Home Assistant 通信。Home Assistant 检查用户的会话，并将请求传递给 Supervisor，后者将其转发到内部网络上的应用。你的 Web 服务器只会看到来自 Supervisor 的请求，位于 `172.30.32.2`。

该代理支持 HTTP/1.x、流式响应和 WebSocket。

## 设置它 {#set-it-up}
1. 在 `config.yaml` 中启用入口：

   ```yaml
   ingress: true
   ```

2. 在容器中将你的 Web 服务器运行在 8099 端口，或者将 `ingress_port` 设置为它使用的端口。
3. 仅接受来自 `172.30.32.2` 的连接。拒绝所有其他连接。
4. 不要要求登录。用户已经登录到 Home Assistant。

安装后，应用页面显示 **打开 Web UI**，用户可以开启 **在侧边栏显示**。使用 `panel_icon` 和 `panel_title` 设置该条目的图标和标题。使用 `panel_admin: false`，非管理员用户也能看到它。

## 使用相对 URL {#work-with-relative-urls}
你的网页界面在每次安装时的路径可能会变化，例如 `/api/hassio_ingress/Xs3V.../`。大多数入口问题都是由此产生的。绝对链接，例如 `/static/app.js` 或重定向到 `/login`，指向的是 Home Assistant，而不是你的应用，因此会失败。

- 在所有地方使用相对 URL：`static/app.js`，而不是 `/static/app.js`。
- Home Assistant 会在每个请求中添加头部 `X-Ingress-Path`，路径为你的应用所服务的路径。当你需要构建绝对 URL 或在支持的软​​件中设置基本路径时使用它。
- 入口 URL 也可以通过 Supervisor API 获取，作为 `ingress_url` 和 `ingress_entry` 位于 `GET /addons/self/info`。

如果你的应用起始页不在 `/`，请将 `ingress_entry` 设置为其路径。

## 了解谁在此处 {#know-who-is-there}
当 Home Assistant 为已登录用户开启 ingress 会话时，Supervisor 会向该会话的请求添加标识该用户的头信息：

| 头信息 | 内容 |
| --- | --- |
| `X-Remote-User-Id` | 用户的 ID |
| `X-Remote-User-Name` | 用户名 |
| `X-Remote-User-Display-Name` | 显示名称 |

这些头信息并非保证存在。Supervisor 仅在找到会话用户时才会设置它们，如果用户没有用户名或显示名称，则会省略这些字段。在明确需要时，要处理没有这些头信息的请求，尤其是当你的应用根据每个用户决定其权限时：应将其视为未知用户，而非默认用户。

Supervisor 会从传入请求中移除这些头信息，并自行设置它们，因此只要你的应用仅接受来自 `172.30.32.2` 的连接，就可以信任这些头信息。

## 大文件上传 {#large-uploads}
默认情况下，Supervisor 会在转发请求之前完全读取请求体。对于接收大文件上传的应用，请设置 `ingress_stream: true` 将 POST 请求体以流的方式传递给应用。

## 主机网络上的应用 {#apps-on-the-host-network}
在主机网络上的应用会与主机及其他应用共享端口。固定的 `ingress_port` 可能会产生冲突。设置 `ingress_port: 0`，Supervisor 会在应用启动时选择 62000 到 65500 之间的空闲端口。可以在启动时使用 Bashio 读取它：

```bash
#!/command/with-contenv bashio

port=$(bashio::app.ingress_port)
exec my-web-server --port "${port}"
```

不要在 `ports` 中映射该范围内的任何端口；Supervisor 会拒绝该配置。

## nginx 示例 {#example-with-nginx}
一个通过 nginx 提供页面的最小应用。`Dockerfile`：

```dockerfile
FROM ghcr.io/home-assistant/base:3.24

RUN apk add --no-cache nginx && mkdir -p /run/nginx

COPY ingress.conf /etc/nginx/http.d/

CMD [ "nginx", "-g", "daemon off; error_log /dev/stdout info;" ]
```

nginx 配置 `ingress.conf` 只允许 Supervisor：

```nginx
server {
    listen 8099;
    allow  172.30.32.2;
    deny   all;
}
```

以及 `config.yaml`：

```yaml
name: "Ingress example"
version: "1.0.0"
slug: "ingress_example"
description: "Ingress testing"
arch:
  - aarch64
  - amd64
init: false
ingress: true
```

安装它，启动它，然后在应用页面选择 **打开 Web UI**。

## 无需入口 {#without-ingress}
如果你的网页界面无法在变化的路径下运行，或者用户需要从外部 Home Assistant 访问它，请使用 `ports` 暴露一个端口并设置 `webui`，这样应用页面就会有一个 **打开网页界面** 按钮，可以直接打开它。然后你的应用必须自行处理认证。可以考虑使用 [`auth_api`](/apps/guides/security#use-home-assistant-users) 来根据 Home Assistant 用户检查登录。
