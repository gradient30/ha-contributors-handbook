---
title: 应用文件
description: Supervisor 从应用程序文件夹和存储库中读取的文件，以及每个文件的用途。
order: 3
---


# 应用文件 {#app-files}
Supervisor 会从你的应用程序文件夹中读取一组固定的文件名。文件夹中的其他所有内容仅由你的 `Dockerfile` 使用。

## 应用程序文件夹 {#app-folder}
```text
hello_world/
  translations/
    en.yaml
  rootfs/
  apparmor.txt
  CHANGELOG.md
  config.yaml
  Dockerfile
  DOCS.md
  icon.png
  logo.png
  README.md
```| 文件 | 是否必须 | Supervisor 会如何处理 |
| --- | --- | --- |
| `config.yaml` | 是 | [应用配置](/apps/reference/configuration)。也可以接受为 `config.yml` 或 `config.json`。 |
| `Dockerfile` | 用于本地构建 | 当 `config.yaml` 没有 `image` 时构建镜像。对于该架构，`Dockerfile.aarch64` 或 `Dockerfile.amd64` 优先。 |
| `README.md` | 否 | 应用商店中的应用介绍。 |
| `DOCS.md` | 否 | 应用的 **文档** 标签页。 |
| `CHANGELOG.md` | 否 | 当有更新时显示的更改内容。 |
| `icon.png` | 否 | 应用的方形图标。 |
| `logo.png` | 否 | 应用页面上显示的标志。 |
| `apparmor.txt` | 否 | 自定义 AppArmor 配置文件，用于替代默认配置文件。 |
| `translations/` | 否 | 选项和端口的名称及描述翻译，每种语言一个文件，如 `en.yaml`。支持 YAML 或 JSON。 |
| `build.yaml` | 否 | 已弃用。请参见 [构建容器镜像](/apps/guides/dockerfile#buildyaml)。 |

`rootfs/` 对于 Supervisor 并不特殊，但在示例和官方应用中这是惯例：一个 `Dockerfile` 使用 `COPY rootfs /` 复制到镜像中的文件夹。Supervisor 在查找 `config.yaml` 文件时会跳过名为 `rootfs` 的文件夹，因此其中的配置文件是安全的。

文档文件、图标和徽标的内容请参见 [展示你的应用](/apps/guides/presentation)。

## 翻译文件 {#translation-file}
一个翻译文件有两个键：`configuration` 用于选项，`network` 用于端口。

```yaml
configuration:
  ssl:
    name: "Enable SSL"
    description: "Use SSL for the web server of the app."
  ssh:
    name: "SSH options"
    description: "Configure SSH authentication."
    fields:
      public_key:
        name: "Public key"
        description: "The public key of your client."
network:
  80/tcp: "The web server port (not used for ingress)"
```

| 键 | 描述 |
| --- | --- |
| `configuration.<option>.name` | 必填。选项的标签。`<option>` 对应 `schema` 中的一个键。|
| `configuration.<option>.description` | 选项下方的帮助文本。|
| `configuration.<option>.fields` | 相同的结构，用于嵌套选项的键。|
| `network.<port>` | 端口的描述。`<port>` 对应 `ports` 中的一个键。|

文件名是语言代码，如 `en.yaml` 或 `pt-BR.yaml`。当缺少某种语言时，界面会回退到英语。有关如何使用，请参见 [添加选项](/apps/guides/options#translate-the-options)。

## 仓库 {#repository}
仓库是一个 Git 仓库，在根目录下有一个 `repository.yaml`（或 `repository.yml`，或 `repository.json`），每个应用程序一个文件夹。

```text
my-apps/
  hello_world/
    config.yaml
    Dockerfile
  another_app/
    config.yaml
  repository.yaml
```

```yaml
name: "My apps"
url: "https://github.com/me/my-apps"
maintainer: "Jane Doe <jane@example.com>"
```

| 键 | 必填 | 描述 |
| --- | --- | --- |
| `name` | 是 | 仓库的名称，在应用商店中显示。 |
| `url` | 否 | 仓库的主页。 |
| `maintainer` | 否 | 谁维护仓库以及如何联系他们。 |

没有有效的 `repository.yaml`，Supervisor 无法加载仓库。请参阅 [创建和共享仓库](/apps/guides/repository)。
