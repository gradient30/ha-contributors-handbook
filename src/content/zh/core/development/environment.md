---
title: 搭建开发环境
description: 获得工作 Home Assistant Core 开发设置, 开发容器或手动安装在 Linux, macOS, 或 Windows 上 。
sidebarLabel: 开发环境
sidebarGroup: 编写代码
order: 1
source: https://github.com/home-assistant/core/blob/dev/pyproject.toml
lastVerified: 2026-10-12
---



# 搭建开发环境 {#set-up-your-development-environment}
2026-10-12日最后一次核实,对https://github.com/home-assistant/core/blob/dev/pyproject.toml.

您需要一个开发环境从源代码运行 Home Assistant, 运行测试, 运行 linters 。 有两种方法可以得到:

- ** 开发容器**(推荐):Visual Studio代码用右 Python 版本构建一个 Docker 容器,每个依赖,以及已经设置的 linters. Linux、macOS和Windows也有同样的设定。 例外是获得USB棒等硬件,参见下文注解.
- ** 手动设置**:您自己安装Python和系统库,并创建一个虚拟环境。 如果您不想使用 Docker 或 Visual Studio 代码, 请使用 。

## 本文件仅供参考。 {#development-container}

### 你需要的东西 {#what-you-need}

- [视觉工作室代码](https://code.visualstudio.com/)
- [图形](https://git-scm.com/)
- 杜克,你好吗? 如何安装取决于操作系统,见下文。

> [!NOTE]
> 容器更难使用 USB 棒之类的硬件 或您的计算机的 Bluetooth 适配器 。 在Linux主机上,你可以通过它们到容器. 在Windows上,Docker运行在WSL内部,WSL本身无法访问USB设备:您首先用[百合双赢](https://learn.microsoft.com/windows/wsl/connect-usb)将一个设备附加到WSL上. 在macOS上,容器不能直接访问该硬件. Docker桌面可以在网络上与 [美联储/国际投资方案](https://docs.docker.com/desktop/features/usbip/) 共享 USB 设备, 但这需要额外的设置 。

### 在 Linux 上安装嵌入器 {#install-docker-on-linux}

安装 [嵌入引擎](https://docs.docker.com/engine/install/) 和您的分发指令 。(猥)

### 在 macOS 上安装嵌入器 {#install-docker-on-macos}

安装 [Mac 的嵌入桌面](https://docs.docker.com/desktop/setup/install/mac-install/) 。

### 在窗口上安装嵌入器 {#install-docker-on-windows}

在Windows上,一切运行在WSL2内部,即Linux的Windows子系统.

1. 以默认的 Ubuntu 分布安装 WSL2 。 在 Windows 终端中,运行:

```shell
   wsl --install
   ```

2. 请检查date=中的日期值 (帮助) WSL 版本 2:

```shell
   wsl -l -v
   ```

   如果显示版本 1, 用 `wsl --set-version <distro name> 2` 转换它 。

3. Docker Engine作为系统化服务运行,因此启用系统. 用 `wsl` 启动 WSL  shell, 并将此添加到 `/etc/wsl.conf` (用 `sudo` ):

```ini
   [boot]
   systemd=true
   ```

4. 从 Windows 终端以 `wsl --shutdown` 重新启动 WSL, 然后重新开始 。
5. 在WSL内部,遵循上面的Linux指令安装Docker引擎.

从这里开始,做WSL内部的一切,包括克隆寄存器. 文件系统Windows侧的代码会遇到权限问题.

### 在容器中打开寄存器 {#open-the-repository-in-the-container}

1. [叉芯存储器](https://github.com/home-assistant/core/fork) on GitHub.
2. 克隆您的叉, 将 Home Assistant 寄存器添加为 `upstream`, 在 Visual Studio 代码中打开 :

```shell
   git clone https://github.com/YOUR_GitHub_USERNAME/core
   cd core
   git remote add upstream https://github.com/home-assistant/core.git
   code .
   ```

3. Visual Studio代码检测容器配置,并询问您是否想要**在容器中重新打开**. 选择它。 如果它要求安装Dev容器扩展,请安装.
4. 等待容器建造。 第一次需要几分钟。 完成后,它运行`script/setup`,它会安装所有要求和linters的Git钩.

要检查万事通,请打开命令调色板(<kbd>Ctrl</kbd>H3}Shift</kbd>H5}P</kbd>,或<kbd>Shift</kbd>H9}Command{H10<kbd>P</kbd>在macOS上),选择**任务:运行任务**,然后**RunHome Assistant Core。 当终端输出减速时,打开`http://localhost:8123`. 你应该看看登机屏幕

稍后回到容器,打开Visual Studio代码,在侧边栏选择**Remote Explorer**,并选择容器.

### 任务 {#tasks}

容器有你最擅长的工作 打开命令调色板,选择**任务:运行任务**,并选择一个:

| 任务 | 它会做什么 |
| --- | --- |
| ** 运行Home Assistant Core | 以 `config/` 中配置开始 Home Assistant 。 |
| ** 测试** | 运行完整的测试套房。 |
| **的决议通过。 | 只运行您更改的测试文件 。 |
| ** 守则覆盖范围** | 进行一个整合的测试,并提交覆盖报告。 |
| ** 最新糖浆快照** | 更新一个集成的快照。 |
| 页:1 | 运行您更改的插件 。 |
| ** 基因要求** | 更改依赖性后更新 `requirements_all.txt`。 |
| ** 满足所有(试验和生产)要求** | 嗡嗡声,再次安装所有要求。 |
| ** 英文译本** | 将 `strings.json` 文件转换为英文翻译 。 |
| ** 创建新的一体化** | 启动生成新集成的脚手架。 |

要重新启动仍在运行的任务, 请选择 ** 任务: 重新启动运行任务 ** 。

### 调试 {#debugging}

容器带有调试配置. 按 <kbd> F5</kbd> 在调试器中启动 Home Assistant, 它会停止在您设置的任何断点上 。 **Run和Debug**视图也有调试当前测试文件的配置,或者附加在运行中的实例上.

要调试运行在其他地方的实例, 如您的生产系统, 使用 [调试集成](https://www.home-assistant.io/integrations/debugpy/) 。

从Home Assistant2026.11开始,也可以在运行的Home Assistant内部四周查看,不设调试器,调试控制台在**Settings** > **Tools** > **调试控制台**下. 它运行 Python 代码, 可用 `hass` , 将结果显示为可以扩展的对象, 并在输入时完成代码 。 例如,看太阳的状态:

```python
hass.states.get("sun.sun")
```

调试控制台在 `configuration.yaml` 中以 `debug_console:` 启用, 而 `script/setup` 增加了此容器的配置 。 在其它地方, 请自己添加并重新启动 Home Assistant; 参见 [除错控制台集成](https://www.home-assistant.io/integrations/debug_console/) 。 代码运行于 Home Assistant 的事件循环, 所以 `await` 一个同步的呼叫, 运行 `await hass.async_add_executor_job(...)` 阻断工作 。

### 当容器不构建时 {#when-the-container-does-not-build}

一个无法建造的容器往往以过时的 希望叉为基础.

1. 确定您的叉子与 `dev` 的 Home Assistant 分支 最新 。
2. 自主权
3. 如果这样无济于事,请从调色板指令中选择 ** 打开配置在回收处理器中** ,在终端运行`git pull upstream dev`,然后选择 ** Dev 容器: 重建容器**。

## 手动设置 {#manual-setup}

Core 需要最近的 Python : `requires-python` 在它的 [`pyproject.toml`](https://github.com/home-assistant/core/blob/dev/pyproject.toml) 中要求 31.4.2 或 更新 。 您操作系统的 Python 往往比较老 。 如果您用旧的 Python 创建虚拟环境, 它不会起作用 : 安装正确的版本, 删除 `.venv` 文件夹, 再运行此设置 。

### 安装系统依赖性 {#install-the-system-dependencies}

Home Assistant及其要求需要几个系统库和构建工具.

在Ubuntu或Debian上:

```shell
sudo apt-get update
sudo apt-get install autoconf libssl-dev libxml2-dev libxslt1-dev libjpeg-dev \
  libffi-dev libudev-dev zlib1g-dev pkg-config libavformat-dev \
  libavcodec-dev libavdevice-dev libavutil-dev libswscale-dev \
  libswresample-dev libavfilter-dev ffmpeg libgammu-dev \
  build-essential
```

在费多拉:

```shell
sudo dnf update
sudo dnf install autoconf openssl-devel libxml2-devel libxslt-devel \
  libjpeg-turbo-devel libffi-devel systemd-devel zlib-devel \
  pkgconf-pkg-config libavformat-free-devel libavcodec-free-devel \
  libavdevice-free-devel libavutil-free-devel libswscale-free-devel \
  ffmpeg-free-devel libavfilter-free-devel ffmpeg-free gcc gcc-c++ \
  cmake
```

这个

```shell
sudo pacman -Sy base-devel autoconf libxml2 libxslt libjpeg-turbo \
  libffi systemd zlib pkgconf ffmpeg gcc cmake
```

在 macOS 上,安装 [乡亲](https://brew.sh/) 并使用它来安装依赖性 :

```shell
brew install autoconf ffmpeg cmake make
```

一些依附关系,如`cryptography`和`orjson`,包含Rust代码. 如果您的平台没有预建的软件包, 它们是从源头构建的, 这需要一个 Rust 工具链 。 如果设置因 `rustc` 或 `cargo` 丢失而失败, 请运行 `brew install rust` 。

在 NixOS 上, 把这个 `default.nix` 放到寄存器中并激活它, 例如使用 [格伦夫](https://direnv.net/) :

```nix
let
  pkgs = import <nixpkgs> { };
in
pkgs.mkShell {
  packages = with pkgs; [
    autoconf
    clang
    cmake
    ffmpeg
    ffmpeg.dev
    gammu
    libffi.dev
    libjpeg.dev
    libxml2.dev
    libxslt.dev
    openssl_3.dev
    pkg-config
    python314
    zlib.dev
  ];
  env = {
    LD_LIBRARY_PATH = "${pkgs.libjpeg.out}/lib";
  };
}
```

在Windows上,再见Ubuntu安装[WSL 语言](https://learn.microsoft.com/windows/wsl/install),并遵循WSL内部的Ubuntu指令. 把你的密码都放在WSL里

### 以 uv 安装 Python {#install-python-with-uv}

获得正确的Python最简单的方式是[uv](https://docs.astral.sh/uv/),软件包管理器核心使用. 用 [正式安装器](https://docs.astral.sh/uv/getting-started/installation/) 安装它 :

```shell
curl -LsSf https://astral.sh/uv/install.sh | sh
```

在此之后您无需安装 Python 。 核心寄存器有一个 `.python-version` 文件,与开发容器使用的确切版本,v读到:当设置脚本创建虚拟环境时,v下载该版本,如果你还没有. 要安装它, 在您复制后, 在仓库文件夹中运行 `uv python install` 。

如果 uv 报告说它没有发现所需的 Python 版本的下载, 您的 uv 已经太老了 。 再次运行安装器以更新它 。

在 NixOS 上, `python314` 在 `default.nix` 中提供 Python, 您不需要 uv 。

### 设置仓库 {#set-up-the-repository}

叉 [核心存储器](https://github.com/home-assistant/core/fork)载明,复制您的叉,并将 Home Assistant 仓库添加为 `upstream` :

```shell
git clone https://github.com/YOUR_GitHub_USERNAME/core
cd core
git remote add upstream https://github.com/home-assistant/core.git
```

然后运行设置脚本 :

```shell
script/setup
```

如果没有虚拟环境活动,则在 `.venv` 中创建一个,如果有,则使用 `python3 -m venv` 。 如果一个虚拟环境是活跃的,它会使用这个环境。 然后它安装所有要求,为linters安装Git钩,并在`config`文件夹中创建配置.

### 运行Home Assistant {#run-home-assistant}

激活每个新终端的虚拟环境 :

```shell
source .venv/bin/activate
```

然后从 `config` 文件夹的配置开始 Home Assistant :

```shell
hass -c config
```

打开`http://localhost:8123`看看它。

如果 `hass` 用 `SIGKILL` 在 macOS 上崩溃, 您的终端应用程序可能缺乏 Bluetooth 权限 。 在 ** 系统设置** > ** Privacy & Security** > > QQH2}**下添加.

### W通力合作 {#networking-in-wsl}

如果 `http://localhost:8123` 不从 Windows 打开, 请用 `ip addr show eth0` 找到 WSL 的地址, 并使用 `inet` 地址, 而不用剪切后的部分 。 例如,`172.20.37.6/20`成为`http://172.20.37.6:8123`.

默认情况下, WSL 使用 NAT 网络, 它使 Home Assistant 无法在您的网络中发现设备 。 [在现有模式下建立网络](https://learn.microsoft.com/en-us/windows/wsl/networking#mirrored-mode-networking)给予WSL与Windows相同的网络接口,包括多播,因此与mDNS的作品一起发现.

## 存储器中的AI工具 {#ai-tools-in-the-repository}

如果使用AI编码工具,它不必猜测核心是如何工作的. 寄存器有一个 `AGENTS.md` 文件, 包含对代理的指令, 和[`.claude/skills/`](https://github.com/home-assistant/core/tree/dev/.claude/skills) 中的技能, 如 `ha-integration-knowledge` 用于构建集成, `ha-quality-scale-verify` 用于检查质量尺度规则 。 它们对人类也是有用的。

您要对结果负责 : 见 [AI 政策](/start/ai-policy) 。 [用AI 工具做贡献](/start/ai-tools) 列出所有技能, 并走过一个错误的修复 和构建一个集成到他们。

## 接下来是什么 {#what-is-next}

- [运行测试](/core/development/testing) : 在打开 pull request 之前进行测试 。
- [林特斯,狂欢和CI](/core/development/checks): 犯罪时会运行什么 。
