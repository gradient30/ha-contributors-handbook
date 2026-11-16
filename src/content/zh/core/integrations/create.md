---
title: 创建集成
description: 与脚手架脚本产生新的整合,并学习最小可能的整合是什么样子.
sidebarGroup: 开始
order: 4
---

# 创建集成 {#create-an-integration}

启动新整合的最快方式是[核心存储器](https://github.com/home-assistant/core)中的脚手架脚本. 它向您提出几个问题,并生成一个工作集成,包含一个配置流,测试,和翻译,这样您就可以从设备或服务特有的部分开始.

本 Stevens是脚手架和集成部分的参考文献. 换句话说,想走过去吗? 跟着[教程](/core/integrations/tutorial)。

## 它属于核心吗? {#does-it-belong-in-core}

写代码前先检查一下

对于新的整合,项目建议您首先在 [市场](/marketplace) 中作为 [自定义集成](/glossary/custom-integration) 发布 。 你积累经验,你可以更快地运动。 一旦它成熟并拥有用户基础,请在[发展中国家**](https://discord.com/channels/330944238910963714/554842238073700352)频道中查询[Discord](https://www.home-assistant.io/join-chat/) 是否应该飞船建造。 [发布自定义集成](/marketplace/guides/integrations)解释什么是不同的外核。

船舶的建造必须满足这些要求:

- 产品或服务必须在今天供人们购买和使用。 尚未释放的产品、私人β和众筹项目没有资格。
- 必须建立这一系统,并有实际用户基础。 Home Assistant不是新产品的营销平台.
- 所有通信都通过符合[依赖透明度](/core/quality-scale/dependency-transparency) 那么规则的 PyPI 上的 Python 库 。 见[创建 Python 库](/core/integrations/api-library)。

不知你的合身之处? 在开始前询问 [发展中国家**](https://discord.com/channels/330944238910963714/554842238073700352) 。

## 保持第一个 pull request 小 {#keep-the-first-pull-request-small}

新的整合必须达到 [整合质量尺度](/core/quality-scale) 的青铜级, 仅此而已 。 审查者要求最小的第一 pull request :

- 只有一个平台,就像 `sensor`。
- 没有诊断,自定义动作,重新校正流,或者重新配置流.
- 没有选项流, 除非没有选项, 整合真的无法工作 。
- 留下较硬的规则, 如 `dynamic-devices` 和 `stale-devices` , 供以后使用 。

其他的都跟着pull requests,一个一个。 大 pull request 一次丢掉很多代码可能会被关闭 。 [提交 pull request](/core/development/submitting#new-integrations)解释在描述中写什么。

此页面的其余部分需要 [发展环境](/core/development/environment) 。 运行您核心检出根的每个命令 。

## 运行脚手架脚本 {#run-the-scaffold-script}

```shell
python3 -m script.scaffold integration
```

剧本要求已列入:

- **域 **:您整合的短而独特的名称,如`airgradient`. 它成为文件夹名称,永远无法更改. 见[显示](/core/integrations/manifest#domain).
- ** Name **:名称使用者见,如"AirGradient".
- 手柄**:你成为第一个[融合拥有者](/glossary/integration-owner).
- ** Py 即使PI 软件包 ** : 与您的设备或服务交谈的库, 被 `==` 绑定 。 如果你还没有,就留空吧
- **IoT类**:集成如何获得数据,如`local_polling`或`cloud_push`.
- ** 认证、发现、 OAuth 2.0 和集成类型**:这些决定了脚本生成的配置。

根据你的答案, 跟剧本一起选择一个配置流程模板:

| 氮 | 模板 |
| --- | --- |
| 集成类型为 `helper` | `config_flow_helper` |
| 用户登录 OAuth 2.0 | `config_flow_oauth2` |
| 可有助于对设备进行认证, | `config_flow` |
| 可发现, 无认证 | `config_flow_discovery` |

完成后,脚本运行繁忙,更新所需文件,并从`strings.json`生成英文译文. 您最后会在 `homeassistant/components/<domain>/` 中找到一个文件夹, 在 `tests/components/<domain>/` 中找到匹配的测试文件夹 。

> [!NOTE]
> 脚手架会留下`TODO` 注释您的代码所在位置, 以及您用您的库替换的占位符类 。 在打开 pull request 之前搜索 `TODO` 。

## 其他脚手架模板 {#other-scaffold-templates}

相同的脚本为已经存在的集成添加了块. 用模板的名称运行它,它询问要修改哪个集成:

| 模板 | 添加数 |
| --- | --- |
| `config_flow` | 带有窗体的配置 |
| `config_flow_discovery` | 用于不认证可发现设备的配置流程 |
| `config_flow_oauth2` | 使用 [奥奥特2.0](/core/integrations/oauth2) 的配置流程 |
| `config_flow_helper` | 助手的配置流程 |
| `device_trigger` | [设备触发器](/core/integrations/device-automations) |
| `device_condition` | [设备条件](/core/integrations/device-automations) |
| `device_action` | [设备动作](/core/integrations/device-automations) |
| `reproduce_state` | [教益](/core/integrations/reproduce-state) 的所作所为 |
| `significant_change` | [重大变化](/core/integrations/significant-change) 的所作所为 |
| `backup` | A [备份平台](/core/integrations/backup) |

例如,要添加设备触发器:

```shell
python3 -m script.scaffold device_trigger
```

## 最小的一体化 {#the-smallest-possible-integration}

脚手架的生成量超过了最小值. 它有助于知道需要什么, 所以你知道什么是可选的。 一体化需要两件事:

- A `manifest.json` 至少有 `domain` 和 `name` 。
- 一个 `__init__.py` 有设置函数, 返回设置是否成功 。

```json
{
  "domain": "hello_state",
  "name": "Hello, state!"
}
```

```python
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

DOMAIN = "hello_state"

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the integration."""
    hass.states.async_set("hello_state.world", "Paulus")

    return True
```

此集成负载当 `hello_state:` 在 `configuration.yaml` 中 。 这可以学习,但与设备或服务交谈的集成是从UI设置的 [配置流量](/core/integrations/config-flow),而不是从YAML. 规则见[YAML 配置](/core/integrations/yaml)。

## 平台:您整合的实体 {#platforms-the-entities-of-your-integration}

您的集成通过为其支持的每个实体类型添加一个 [平台](/glossary/platform) 来提供 [实体](/glossary/entity) 。 要提供灯,请添加`light.py`。 要提供传感器,请添加`sensor.py`。 每个平台文件都有一个 `async_setup_entry` 函数创建实体, 您的集成向它们转发其配置条目 :

```python
from homeassistant.const import Platform

PLATFORMS = [Platform.LIGHT, Platform.SENSOR]

async def async_setup_entry(hass: HomeAssistant, entry: MyConfigEntry) -> None:
    """Set up the integration from a config entry."""
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
```

完整设置和卸载流量参见[配置条目](/core/integrations/config-entries#set-up-the-platforms), 以及[实体和平台](/core/entities) 每个实体类型支持的内容 。

## 通向设备的聊天 {#talk-to-devices-through-a-library}

您的整合从不直接对设备或服务说话. 所有协议和API代码都生活在一个单独的 Python 库中, 它发布在 PyPI 上, 您的集成列表为 [所需经费](/core/integrations/manifest#requirements) 。 这使得 Home Assistant 可以维护, 让 Python 社区的其他部分也使用该代码 。

集成翻译了该库和Home Assistant:它设置了库,将其数据转换为实体,并将用户动作转换为库呼叫. 解释如何写一个。

## 核心和定制整合 {#core-and-custom-integrations}

核心寄存器中的集成在 [`homeassistant/components/`](https://github.com/home-assistant/core/tree/dev/homeassistant/components) 中。 一个 [自定义集成](/glossary/custom-integration) 住在用户配置目录的 `custom_components/` 文件夹中 。 它们都是以同样的方式构建的,在运单上有两个不同之处:一个定制集成需要`version`,它的`documentation`指它自己的文件,而不是Home Assistant.io.

[示例- 客户配置仓库](https://github.com/home-assistant/example-custom-config/tree/master/custom_components/)有小的示例集成,比如从一个配置条目设置平台. 它们是自定义的集成,所以包括 `version` 。

## 下一步 {#next-steps}

- 在 [教程](/core/integrations/tutorial) 中逐步建立完整的整合步骤 。
- 看看整合的[文件结构](/core/integrations/file-structure)。
- 填写 [显示](/core/integrations/manifest) 。
- 构建 { 我给你 [配置流量](/core/integrations/config-flow) , 用 [协调员](/core/integrations/fetching-data) 获取数据 。
- 请检查质量尺度 [见下文B节。](/core/quality-scale/rules#bronze) 。
