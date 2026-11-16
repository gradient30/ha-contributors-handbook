---
title: YAML 配置
description: 当一个集成仍可能配置在配置中时 。 Yaml, 以及 Home Assistant 如何验证此配置 。
sidebarGroup: 设置和配置
order: 8
---

# YAML 配置 {#yaml-configuration}

`configuration.yaml` 是配置文件用户自写 。 长期以来,每次整合都是如此。 今天,大多数整合是在UI中设置的,有一个[配置流量](/core/integrations/config-flow).

## 当YAML被允许时 {#when-yaml-is-allowed}

该规则来自[ADR-0010 (英语).](https://github.com/home-assistant/architecture/blob/master/adr/0010-integration-configuration.md) :

- 与设备或服务是否能交谈的集成仅在UI中配置. 在极少数情况下,是否能例外。
- 所有其他集成,如只处理数据的帮助者或集成,都可以在YAML中配置,在UI中配置,或者两者兼而有之.

这适用于所有新的一体化。 鼓励与设备或服务交谈且仍有YAML的现有集成添加一个配置流并删除YAML支持. 不再接受对其YAML配置的修改.

## 没有YAML 的整合 {#integrations-without-yaml}

即使没有 YAML 支持,您的 `__init__.py` 也经常有 `async_setup` 的功能, 例如到 [注册动作](/core/integrations/actions) 。 Hassfest 需要 `async_setup` 或 `setup` 在 `__init__.py` 中的每个函数的整合来定义 `CONFIG_SCHEMA` 。 它还接受一个`PLATFORM_SCHEMA`或`PLATFORM_SCHEMA_BASE`,像`sensor`这样的实体集成定义,或`async_validate_config`在`config.py`中的函数. 如果没有 YAML 支持, 请使用 `homeassistant.helpers.config_validation` 的其中一个帮助 :

```python
from homeassistant.helpers import config_validation as cv

CONFIG_SCHEMA = cv.config_entry_only_config_schema(DOMAIN)
```

| 帮助者 | 用它的时候 |
| --- | --- |
| `config_entry_only_config_schema` | 整合只从配置条目设置. 如果用户将域添加到 YAML 中, Home Assistant 登录一个错误, 并创建一个修复问题, 指出在 UI 中添加集成 。 |
| `platform_only_config_schema` | 集成仅在 YAML方面取得了重大进展平台配置, 没有在自己的密钥下配置 |
| `empty_config_schema` | 集成可以用YAML 键设置, 但不选择 |

## YAML 如何验证 {#how-yaml-is-validated}

当 Home Assistant 装入一个在 YAML 中配置的集成时, 它首先用 `CONFIG_SCHEMA` 的集成来验证配置 。 `config` 您的设置功能是验证的结果 。

```python
import probatio

from homeassistant.helpers import config_validation as cv

CONFIG_SCHEMA = probatio.Schema(
    {
        DOMAIN: probatio.Schema(
            {
                probatio.Required(CONF_NAME): cv.string,
                probatio.Optional(CONF_PORT, default=80): cv.port,
            }
        )
    },
    extra=probatio.ALLOW_EXTRA,
)

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the integration from YAML."""
    if DOMAIN not in config:
        return True

    name = config[DOMAIN][CONF_NAME]
    ...
    return True
```

schema获得整个配置,所以使用`extra=probatio.ALLOW_EXTRA`将其他集成的密钥单独留下.

## YAML 中的平台 {#platforms-in-yaml}

旧的集成将其配置置于实体集成的范畴下,其中键为 `platform`:

```yaml
sensor:
  - platform: example
    name: "Outside"
```

这是实体一体化的现有机制,新的一体化决不能使用这种机制。 每  这个 [ADR-0007 (英语).](https://github.com/home-assistant/architecture/blob/master/adr/0007-integration-config-yaml-structure.md) , 一个集成的所有 YAML 配置都会在它自己的域键下进行. 集成后加载其平台本身,由`async_load_platform`从`homeassistant.helpers.discovery`加载:

```python
from homeassistant.const import Platform
from homeassistant.helpers.discovery import async_load_platform

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the integration and its platforms from YAML."""
    hass.async_create_task(
        async_load_platform(
            hass, Platform.SENSOR, DOMAIN, config[DOMAIN], config
        )
    )

    return True
```

该平台在其`async_setup_platform`中以`discovery_info`收到数据。 现有集成的平台部分中的YAML配置被冻结,直到集成被重构.

对于实体集成, `PLATFORM_SCHEMA` 是在引擎盖下如何工作 。 Home Assistant 收集从域( 如 `sensor:` 和 `sensor living room:`) 开始的每个密钥的配置, 首先根据实体集成( `PLATFORM_SCHEMA_BASE` 或其他 `PLATFORM_SCHEMA` ) 的策略验证每个项目, 然后再根据它的平台的 `PLATFORM_SCHEMA` 进行验证, 如果它有一个, 并且为未知平台或配置无效 。

## 从 YAML 移动到配置流 {#move-from-yaml-to-a-config-flow}

当一个集成到一个配置流时,现有的YAML配置通常被导入一次. `async_setup` 以 `import` 源开始流量, 配置流量在 `async_step_import` 中创建条目, 集成则创建 [修理问题](/core/integrations/repairs) , 告诉用户删除 YAML 。 远离 YAML 是 [向后仍处于不兼容状态的更改](/glossary/backward-incompatible-change), 所以跟随 [折旧过程](/core/development/deprecating) 。

关于YAML中的OAuth 2.0证书,见[YAML 证书](/core/integrations/oauth2#credentials-from-yaml).
