---
title: Android 端到端测试
description: 每晚运行的 Maestro 测试会在每个 API 级别上将 Android 应用程序与真实的 Home Assistant 进行测试，以及如何调试失败情况。
sidebarLabel: 端到端测试
sidebarGroup: 测试
order: 4
source: https://github.com/home-assistant/android/blob/main/.github/workflows/e2e.yml
lastVerified: 2026-11-05
---

# Android 端到端测试 {#android-end-to-end-tests}

最后验证于 2026-11-05，针对 https://github.com/home-assistant/android/blob/main/.github/workflows/e2e.yml.

所有其他测试都是模拟服务器。端到端（E2E）测试不是：它们运行真实应用程序对真实的 Home Assistant，就像用户一样。这样可以捕捉其他任何测试无法检测到的问题，例如核心或前端的更改导致的入门流程中断，或某个特定 Android 版本上的网页视图问题。

有两个测试：一个通过普通 HTTP 入门，另一个通过需要客户端证书的代理进行入门，称为双向 TLS（mTLS）。

## 运行时间 {#when-it-runs}

`e2e.yml` 工作流运行时间：

- 每天晚上 05:00 UTC 在 `main`，针对 Home Assistant 的 `dev` 镜像，即最新的开发版本。
- 手动运行，在任何分支上，通过 **Run workflow**。可选的 `home-assistant-version` 输入用于选择要测试的镜像标签。

它不是 pull request 检查的一部分。它会为每个受支持的 API 级别启动一个模拟器，对每次 pull request 来说成本太高。

## 它的功能 {#what-it-does}

1. 为 mTLS 测试生成证书。这些证书仅在本次运行中存在。
2. 构建 `fullDebug` APK，关闭 [StrictMode](/companion/android/debugging#strictmode)，并信任本次运行的证书颁发机构 (CA)。
3. 安装 [Maestro](https://maestro.dev/) CLI，并根据其公布的校验和检查下载内容。
4. 根据 `.github/e2e/homeassistant` 中的配置启动 Home Assistant，并检查 `mobile_app` 是否已加载。
5. 在 Home Assistant 前启动 mTLS 代理，并检查其是否拒绝没有客户端证书的请求。
6. 在 Emulator.wtf 上为每个 API 级别启动一个模拟器，从 API 29 到 `androidSdk-target`，并安装应用。
7. 在所有模拟器上并行运行普通流程。
8. 在模拟器上打开证书安装程序，并运行 mTLS 流程。仅当普通流程成功时才会执行此步骤。
9. 上传调试所需的文件，无论结果如何。设备列表从 API 29 开始，尽管该应用支持更早的版本。在较旧的镜像上，Web 视图可以渲染前端，但其内容从未出现在 Maestro 能看到的范围内，因此对其的每一个检查都会失败。pull request 上的 [仪器测试](/companion/android/instrumentation-testing) 仍然覆盖完整范围，直到应用的最低 API 级别。

Home Assistant 容器和代理运行在 GitHub 运行器上，而模拟器运行在 Emulator.wtf 上。它们之间通过一个隧道连接，在模拟器内 `homeassistant.internal` 解析到运行器：端口 8123 是 Home Assistant，端口 8443 是代理。

## mTLS 测试的工作原理 {#how-the-mtls-test-works}

`.github/e2e/mtls` 中的代理是位于 Home Assistant 前的 nginx。没有客户端证书，它会拒绝所有请求，从入门的第一页开始。

其服务器证书由一个仅在此运行期间存在的 CA 签发。为了让应用程序信任它，工作流程使用 Gradle 属性 `debugExtraResDir` 构建。这会用 `.github/e2e/mtls` 中的副本替换应用程序的网络安全配置，该副本在可调试的构建中信任该 CA。不使用该属性的构建保持不变。

客户端证书的安装方式与用户的一样：工作流程会打开系统证书安装程序，并通过其完成整个流程。

> [!重要]
> [`.github/e2e/mtls/network_security_config.xml`](https://github.com/home-assistant/android/blob/main/.github/e2e/mtls/network_security_config.xml) 是 [`app/src/main/res/xml/network_security_config.xml`](https://github.com/home-assistant/android/blob/main/app/src/main/res/xml/network_security_config.xml) 的副本，只额外添加了一个部分。当你更改应用程序的配置时，也请在副本中做相同的更改。

## 流程 {#the-flows}

这些流程存放在仓库根目录的 `.maestro` 文件夹中，每个测试步骤都写在那里：

- [`.maestro/onboarding.yaml`](https://github.com/home-assistant/android/blob/main/.maestro/onboarding.yaml) 通过普通 HTTP 进行注册。
- [`.maestro/onboarding-mtls.yaml`](https://github.com/home-assistant/android/blob/main/.maestro/onboarding-mtls.yaml) 安装客户端证书，然后通过代理进行注册。

它们通过 `.maestro/subflows` 共享步骤，并涵盖应用程序中最关键的路径：- **登录**：真实的登录页面，使用真实凭证，通过整个授权流程。
- **注册**：应用向 `mobile_app` 自行注册，其他所有功能都依赖于此。
- **前端渲染**：到达概览仪表盘证明在该 API 级别上 Web 视图可正常工作。
- **外部总线双向工作**：只有在应用通过 [外部总线](/frontend/reference/external-bus) 宣告自己后，前端才会在设置中显示 **Companion 应用** 条目，选择它会让前端请求应用打开其原生设置。

这些流程从三个参数 `HOME_ASSISTANT_URL`、`HOME_ASSISTANT_USERNAME` 和 `HOME_ASSISTANT_PASSWORD` 获取要测试的实例。mTLS 流程还需要两个参数 `MTLS_P12_PASSWORD` 和 `MTLS_CERT_ALIAS`：证书文件的密码，以及用于证书的名称。

当你更改一个流程时：- 它驱动调试应用程序，`io.homeassistant.companion.android.debug`。不要更改 `appId`。
- 它适用于所有 API 级别，因此任何特定版本的操作都必须是有条件的，就像现有的权限对话框步骤一样。
- 步骤会匹配屏幕上的文本。如果你重命名应用程序中的标签，请在同一 pull request 中更新流程。
- 将多个流程需要的步骤放入子流程中。

[Maestro 文档](https://docs.maestro.dev/api-reference/commands) 列出了所有命令。

## 本地运行 {#run-it-locally}

安装 [Maestro CLI](https://docs.maestro.dev/getting-started/installing-maestro)，启动模拟器或连接设备，然后运行：

```bash
./gradlew :app:installFullDebug
maestro test \
  -e HOME_ASSISTANT_URL=http://homeassistant.local:8123 \
  -e HOME_ASSISTANT_USERNAME=<username> \
  -e HOME_ASSISTANT_PASSWORD=<password> \
  .maestro/onboarding.yaml
```

该流程会先清除应用状态，因此总是从全新的入门流程开始。使用一次性实例：每次运行都会在其上注册一个新设备。

### 运行 mTLS 流程 {#run-the-mtls-flow}

要运行 mTLS 测试，您需要在 Home Assistant 前面配置一个要求 mTLS 的反向代理，并打开用于您的证书文件的证书安装对话框。达到此状态的最简单方法是使用下面描述的步骤，这些步骤也适用于 GitHub Actions。您需要使用模拟器、Docker 和运行在您机器 8123 端口的 Home Assistant。从模拟器来看，您的机器是 `10.0.2.2`。

1. 生成证书，在服务器证书中使用该地址：

   ```bash
   OUT=/tmp/mtls
   .github/e2e/mtls/generate-certs.sh "$OUT" \
     "DNS:homeassistant.internal,IP:10.0.2.2"
   ```

2. 启动代理。使用 Docker Desktop 时，`host.docker.internal` 是您的机器：

   ```bash
   TEMPLATE=/etc/nginx/templates/default.conf.template
   docker run -d --name e2e-mtls-proxy -p 8443:8443 \
     -e E2E_MTLS_UPSTREAM=host.docker.internal:8123 \
     -v "$OUT:/etc/nginx/certs:ro" \
     -v "$PWD/.github/e2e/mtls/nginx.conf.template:$TEMPLATE:ro" \
     nginx:stable-alpine
   ```

3. 安装应用，构建为信任 CA：

   ```bash
   ./gradlew :app:installFullDebug -PdebugExtraResDir="$OUT/res"
   ```

4. 在模拟器上打开证书安装程序：

   ```bash
   .github/e2e/mtls/open-cert-installer.sh emulator-5554 "$OUT/client.p12"
   ```在 API 32 及以下版本中，脚本会改为从同一文件夹安装 `client_legacy.p12`，因为这些版本的证书安装程序无法读取 `client.p12`。要使用其他旧文件，请将其路径作为可选的第三个参数传入。

5. 使用 `generate-certs.sh` 的默认密码和名称运行流程：

   ```bash
   maestro test \
     -e HOME_ASSISTANT_URL=https://10.0.2.2:8443 \
     -e HOME_ASSISTANT_USERNAME=<username> \
     -e HOME_ASSISTANT_PASSWORD=<password> \
     -e MTLS_P12_PASSWORD=e2ep12pass \
     -e MTLS_CERT_ALIAS=e2eclient \
     .maestro/onboarding-mtls.yaml
   ```

## 调试失败 {#debug-a-failure}

每次运行都会上传一个 `e2e-artifacts` 工件：

| 文件 | 内容 |
| --- | --- |
| `maestro-results/` | 每个流程和分片的命令跟踪，`maestro.log`，以及失败的截图 |
| `logcat-*.txt` | 完整的 logcat，每个模拟器一个文件 |
| `mtls-proxy.log` | mTLS 代理的日志，每个请求一行 |
| `homeassistant.log` | Home Assistant 日志 |
| `homeassistant-config.json` | `/api/config` 响应，包含版本和已加载的组件 |
| `homeassistant-container.json` | 容器详情，包括确切的镜像 |

按照这个顺序阅读，并在第一个解释失败的文件处停止。大多数失败都显示在失败的 Maestro 命令及其截图中：这可以分辨出屏幕损坏与 Maestro 无法看到的元素。通常从 Home Assistant 日志开始会浪费时间。在代理日志中，`400` 是没有客户端证书的请求。只有在排除了应用程序和流程之后，才向上游查看。`dev` 图像每晚都会变化，所以与上一次通过的运行进行比较：两个 `homeassistant-config.json` 文件提供了断点两边的 Home Assistant 版本。然后查看在此期间落入 [Core](https://github.com/home-assistant/core) 或 [frontend](https://github.com/home-assistant/frontend) 中的内容。

## 自动分诊 {#automated-triage}

失败的夜间运行会启动一个 `e2e-triage` 工作流。AI 代理下载失败运行和最后一次成功运行的产物，并按照 `.agents/skills/ha-android-e2e-debugging` 技能中的流程操作。它只进行诊断：从不更改文件或打开 pull request。它会在 Android 仓库中通过一个 `e2e-failure` issue 进行报告，包括上游发现的内容，以便维护者提交给 Core 或前端。下一次成功的运行会关闭该 issue。
