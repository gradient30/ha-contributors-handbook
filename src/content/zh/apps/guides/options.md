---
title: 添加选项
description: 让用户配置你的应用。定义选项及其类型，在脚本中读取它们，并为它们提供翻译后的标签。
order: 3
---

# 添加选项 {#add-options}

选项是用户在其 ** 配置 ** 标签上更改的应用程序的设置 。 在 协商一致意见 `config.yaml` 中豺狼 中, 劳工市场 中 , 已经 了 。 。 。 。 。

## 选项和计划 {#options-and-schema}

两个关键是共同工作:

- { 为什么你 Sugare? 这些是 为什么你 Sugare的新用户开始。
- {H 我们会抓住每个选项的类型。 由各处各处乍发各不同,而各处各处各处各处,各处各处ằ-各处以及各处的 我可不是各处的,各处各处各处各处各处各处各处各处,各处各处----各处各处各处各处,各处各处各处各处,各处各处各处各处各处,各处各各处各处各处,各各处各处竿不同,各处各处各处恣不同,各处各缇,各处各处各处各处,各处各处各处各处,各处各处各处各处各处各处各处各处各处,各处 让我看看,各处各处各处,各处各处各处各处各适合于各处各处,各处各处 grandparents不同厕,各处,各处各处,各处各以及向各处各抨处几分钟的各处,各处,各处各处各处,各处各处各处,各处的也受到各处各处各处各处各处各处各处各处各向它们提供,各处

```yaml
options:
  message: "Hello world"
  port: 8080
  logins:
    - username: "beer"
      password: "123456"
  log_level: "info"
schema:
  message: str
  port: port
  logins:
    - username: str
      password: password
  log_level: "list(debug|info|warning|error)"
  api_key: "str?"
```

需要`schema`中的每个密钥,除非其类型求助于`?`。 这里:

- 需要{曾多次的所作所为}、 我有预设。
- `api_key`是可选的。 它没有默认,所以不在`options`中。

如果您给出了一个所需的选项, 或默认为 `null` , 用户必须在应用程序启动前填写 。 在 `options` 中保留可选选项, 因此在用户填充之前它们不会被设置 。

选项可以嵌入:一个数值列表,一个映射列表,或者一个映射. 列表不能直接包含另一个列表 。

设定 `schema: false` 完全关闭验证 。 应用程序然后获得原样的选项,而UI则没有显示形式.

## 外观类型 {#schema-types}

| 类型 | 接受 | 窗体字段 |
| --- | --- | --- |
| `str` | 任何文本 | 文本 |
| `str(min,max)` | 文字最小, 不行提供技术支助。 保留一个没有 不行提供技术支助, 像`str(3,)` | 文本 |
| `password` | 文本, 显示为隐藏 。 还取 `(min,max)` | 密码 |
| `bool` | `true` or `false` | 切换 |
| `int` | 整个数字 也取 `(min,max)`, 如 `int(1,10)` | 数目 |
| `float` | 一个数字。 也取 `(min,max)`, 如 `float(0.5,)` | 数目 |
| `email` | 电子邮件地址 | 电子邮件 |
| `url` | 一个 URL | 網址 |
| `port` | 一个网络端口,1至65535 | 数目 |
| `match(regex)` | 匹配正则表达式的文本 | 文本 |
| `list(a\|b\|c)` | 列出的数值之一 | 下拉菜单 |
| `device` | 主机上的设备路径 | 设备的所提供的设备 |
| `device(subsystem=tty)` | 类似串行端口的子系统设备 | 设备的所提供的设备 |

Supervisor 检查每个 `password` 值的散列值与数据库的“ 我被扭曲了 ” , 并警告用户如果出现在那里 。

## 秘诀 {#secrets}

用户可以引用`secrets.yaml` Home Assistant `secrets.yaml` 的密语, 而不是输入一个值, 与 `!secret name` 。 Supervisor 查看并验证真实值 。 您的应用程序在 `options.json` 中收到解析值, 因此您不需要为此做任何事情 。

## 读取选项 {#read-the-options}

Supervisor 将已验证的选项写入`/data/options.json` 每次您的应用程序启动时 :

```json
{
  "message": "Hello world",
  "port": 8080,
  "logins": [{ "username": "beer", "password": "123456" }],
  "log_level": "info"
}
```

在 shell 脚本中，用 [Bashio](/apps/bashio/config/) 读取这些选项。Bashio 并不直接读文件：它向 Supervisor API 请求同样的选项，所以请用 `with-contenv` 启动脚本，以便拿到所需令牌。

```bash
#!/command/with-contenv bashio

message=$(bashio::config 'message')
first_user=$(bashio::config 'logins[0].username')

if bashio::config.has_value 'api_key'; then
  api_key=$(bashio::config 'api_key')
fi
```

关键是jq路径,所以嵌套选项也有效. 在任何其他语言中,读作`/data/options.json`作为JSON.

选项仅在用户保存时更改, 且 Supervisor 在您的应用程序启动前撰写文档 。 因此在启动时读取它们; 用户必须重新启动您的应用程序才能应用新值 。

## 翻译选项 {#translate-the-options}

没有翻译,表单会显示原始选项密钥, 如 `log_level` 。 添加一个翻译文件给每个选项一个可读名称和描述 :

```yaml
# translations/en.yaml {#translationsenyaml}
configuration:
  message:
    name: "Message"
    description: "The message to show in the log at startup."
  log_level:
    name: "Log level"
    description: "How much detail to write to the log."
  logins:
    name: "Logins"
    description: "The users that can log in."
    fields:
      username:
        name: "Username"
      password:
        name: "Password"
```

`configuration` 下的密钥与您的 `schema` 的密钥匹配; `fields` 对嵌入式选项也一样 。 每个语言添加文件, 如 `nl.yaml` 或 `de.yaml` 。 格式为[应用文件](/apps/reference/files#translation-file).

## 删除一个选项 {#remove-an-option}

当您从 `schema` 中丢弃一个选项时, 已经安装您的应用程序的用户仍然保存着 。 Supervisor 然后在每次验证选项时登录类似 `Option 'old_key' does not exist in the schema for My app (local_my_app)` 的警告 。

要清理, 在启动时从保存的选项中删除选项 。 与 Bashio, `bashio::app.option` 无值删除密钥 :

```bash
#!/command/with-contenv bashio

if bashio::jq.exists "$(bashio::app.options)" ".old_key"; then
  bashio::log.info "Removing old option old_key"
  bashio::app.option 'old_key'
fi
```

这叫 Supervisor API 在 `/addons/self/options` 上, 每个应用程序不用 `hassio_api` 就可以使用 。

## 用户配置文件 {#configuration-files-for-users}

一些软件更容易用自己的配置文件配置,而不是用窗体配置. 想想一个复杂的列表,表单不能表达,像 我们得证明的条款一样的二进制文件,或者软件在变化时重新加载的文件.

对于这些情况,地图`app_config`:

```yaml
map:
  - type: app_config
    read_only: false
```

每个应用程序然后获得自己的公共配置文件夹. 在你的容器里,它是`/config`。 用户在 `app_configs` 文件夹( 通过 Samba, SSH, 或文件编辑器应用) 中找到它, 在以 app ID 命名的子文件夹中, 如 `app_configs/local_my_app` 。

告诉文档中的用户要放哪个文件, 或者添加一个带有文件名的选项 。 如果用户需要, 也将文件写入此文件夹: 日志、 生成的配置或检查的数据库 。 该文件夹是您的应用程序备份的一部分, 如果用户选择删除其数据, 当应用程序未安装时会被删除 。
