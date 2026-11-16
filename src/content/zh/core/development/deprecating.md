---
title: 弃用
description: 如何在 Home Assistant Core 中移除或改变行为而不在一夜之间打破家门 。 折旧期,修理问题,以及面向API的开发者帮助者.
sidebarGroup: 变更行为
order: 1
---



# 弃用 {#deprecating}
A [折旧](/glossary/deprecation) 是定于以后的 [向后仍处于不兼容状态的更改](/glossary/backward-incompatible-change) 。 旧行为不断发挥作用,每个受到影响的人都会得到警告,而移除发生在后来的发布中.

任何你删除的,都必须先贬值. 即使在你认为只有少数人使用它的时候,它仍然有效:一个实体,一个动作,或者一个常数可以用于自动化,脚本,仪表板,以及你无法看到的自定义集成。

## 多长时间 {#how-long}

| 谁受影响 | 最低期限 |
| --- | --- |
| 用户:YAML配置,动作,实体,属性,集成 | 6个月 |
| 开发者:常量,帮助者,实体属性,自定义集成使用的平台API | 12个月 |

当生态系统尚未赶上时,折旧期可以延长,但从未缩短。 在 [版本格式](/core/development/versioning) 中, 将清除时的释放命名为 `breaks_in_ha_version`, 如 `"2027.1.0"` 。

使用 `IssueSeverity.WARNING` 只要旧行为仍然有效。 仅在停止工作时使用 `IssueSeverity.ERROR` : 集成已消失, 或迁移失败, 而用户的配置不再有效 。 相同的拆分对于日志级别,当您删除一个面临无法引起修复问题的开发者特性时.

## 面临贬值的用户 {#user-facing-deprecations}

每次需要用户做某事的贬值都会得到[修理问题](/glossary/repair). 当一个集成可以不止 21. 一次设置时, 包括 `issue_id` 中的配置条目, 或者不同的条目互相覆盖的问题 。 设定问题的 [`config_entry_id`](/core/integrations/repairs#issues-that-belong-to-a-config-entry) , 因此它和条目一起删除 。 堕落期结束后,打开后续 pull request,删除旧行为和问题. 标为 [向后仍处于不兼容状态的更改](/releases/guides/backward-incompatible-changes#when-it-is-backward-incompatible) : 有些用户可能还没有对修复采取行动 。

在您自己领域创建的每一期都需要在整合的 `strings.json` 中的 `issues.<translation_key>` 条目 。 在 `HOMEASSISTANT_DOMAIN` 下创建的问题, 如 `deprecated_yaml` 使用核心中已经存在的文本 。

### 丢弃 YAML 支持 {#dropping-yaml-support}

要将一个集成从YAML移动到UI,请添加一个配置流程并加进步骤. 在 `async_setup` 中,导入 YAML 配置。 当导入成功时, 提出 `deprecated_yaml` 核心 问题 。 这个问题存在于 `homeassistant` 域中, 因此在 `HOMEASSISTANT_DOMAIN` 下创建, 并将 `issue_domain` 设定为您自己的域 :

```python
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the integration."""
    if DOMAIN not in config:
        return True

    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": SOURCE_IMPORT}, data=config[DOMAIN]
    )
    

# On the next start, the import aborts because the entry exists. {#single-yaml-options}
    

# That is not a failure. {#actions}
    if result.get("type") is FlowResultType.ABORT and result["reason"] not in (
        "already_configured",
        "single_instance_allowed",
    ):
        

# The import failed, so the YAML is not in effect: raise your own {#entities-and-attributes}
        

# issue with ERROR severity here, and stop. {#removing-an-integration}
        return True

    ir.async_create_issue(
        hass,
        HOMEASSISTANT_DOMAIN,
        f"deprecated_yaml_{DOMAIN}",
        breaks_in_ha_version="2027.1.0",
        is_fixable=False,
        issue_domain=DOMAIN,
        severity=ir.IssueSeverity.WARNING,
        translation_key="deprecated_yaml",
        translation_placeholders={
            "domain": DOMAIN,
            "integration_title": "Example",
        },
    )
    return True
```

仅在导入成功后加高 `deprecated_yaml` 。 否则您会告诉用户他们的配置在不导入时被导入. 由于条目已经存在而中止, 算作成功: 这是第一次导入后每次开始发生的情况 。 您的导入步骤使用什么原因取决于它如何检查一个已有的条目, 因此匹配您自己的配置流程 。

当期间结束,YAM 天呐,YAML 代码消失后,将 `CONFIG_SCHEMA` 设置为 `cv.config_entry_only_config_schema(DOMAIN)` 。 它记录了一个错误,并给任何仍然在`configuration.yaml`中拥有集成功能的人带来修复问题.

### 单 YAML 选项 {#documentation-and-tests}

要贬低一个选项,或者几个选项,在读 YAML 的 `async_setup` 中提出问题,并且只有在该选项实际使用时才会提出. 这个选项一直工作到结束。

```python
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the integration."""
    if CONF_IPV6 in config[DOMAIN]:
        ir.async_create_issue(
            hass,
            DOMAIN,
            "deprecated_ipv6",
            breaks_in_ha_version="2027.1.0",
            is_fixable=False,
            severity=ir.IssueSeverity.WARNING,
            translation_key="deprecated_ipv6",
        )
```

当期限结束时,不要从计划中删除选项。 将 `cv.removed(CONF_IPV6)` 置换到它的位置: 它告诉用户这个选项已经消失, 而不是因为通用验证错误而失败 。

### 动作 {#developer-facing-deprecations}

在行动的处理者中提出问题. 为了贬低一个行动领域,只有当这个领域通过时才会提出。

```python
async def render_image(call: ServiceCall) -> ServiceResponse:
    """Render an image."""
    ir.async_create_issue(
        call.hass,
        DOMAIN,
        "deprecated_render_image",
        breaks_in_ha_version="2027.1.0",
        is_fixable=False,
        severity=ir.IssueSeverity.WARNING,
        translation_key="deprecated_render_image",
    )
```

### 实体和属性 {#constants-aliases-and-enum-members}

当一个属性成为自己的实体时,一个实体会移动到另一个平台在国际平台上,或者一个实体会消失,首先创建新的实体,并保持旧实体在此期间工作.

向每个仍在存在和已启用的贬值实体提出问题。 使用 `automations_with_entity()` 和 `scripts_with_entity()` 来命名将中断的自动化和脚本 。 用户通过使实体丧失能力来确认贬值。 一旦被禁用而无用,则从登记簿中删除,以免再次产生.

```python
def async_deprecate_entity(
    hass: HomeAssistant,
    entity_registry: er.EntityRegistry,
    description: ExampleSwitchEntityDescription,
) -> bool:
    """Return whether the deprecated entity should still be created."""
    entity_id = entity_registry.async_get_entity_id(
        Platform.SWITCH, DOMAIN, description.unique_id
    )
    if entity_id is None:
        return False

    items = automations_with_entity(hass, entity_id) + scripts_with_entity(
        hass, entity_id
    )
    entity_entry = entity_registry.async_get(entity_id)
    if entity_entry.disabled and not items:
        entity_registry.async_remove(entity_id)
        return False

    placeholders = {
        "entity_id": entity_id,
        "new_entity_id": description.replacement_entity_id,
    }
    if items:
        placeholders["items"] = "\n".join(items)

    ir.async_create_issue(
        hass,
        DOMAIN,
        f"deprecated_entity_{entity_id}",
        breaks_in_ha_version="2027.2.0",
        config_entry_id=entity_entry.config_entry_id,
        is_fixable=False,
        severity=ir.IssueSeverity.WARNING,
        translation_key=(
            "deprecated_entity_used" if items else "deprecated_entity"
        ),
        translation_placeholders=placeholders,
    )
    return True
```

`config_entry_id` 将问题链接到实体的配置条目, 因此它被隐藏, 而该条目被禁用, 删除时被删除 。

在平台的`async_setup_entry`中调用,并让其答案决定添加哪些实体.ئار العب المل المر المر العر المل العر العر العر العر العر الع الري المر العر المر الري الري ال العي الري الري ال , الرار , الر , الر , الر , , الري , , الر , , الر , , ار , , ;

```python
async def async_setup_entry(
    hass: HomeAssistant,
    entry: ExampleConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up the switch platform."""
    coordinator = entry.runtime_data
    entity_registry = er.async_get(hass)

    entities = [
        ExampleSwitch(coordinator, description) for description in SWITCHES
    ]
    entities.extend(
        ExampleSwitch(coordinator, description)
        for description in DEPRECATED_SWITCHES
        if async_deprecate_entity(hass, entity_registry, description)
    )
    async_add_entities(entities)
```

这个问题并非长期存在:只要实体在使用中,它就会在每次开始时再次产生。 信息名称是每个实体可能使用的地方, 不仅仅是自动化和脚本, 告诉用户,

```json
{
  "issues": {
    "deprecated_entity": {
      "title": "Deprecated switch detected",
      "description": "The switch `{entity_id}` is deprecated because it has been replaced with `{new_entity_id}`.\n\nUpdate your dashboards, templates, automations, and scripts to use the replacement entity, then disable the deprecated switch and restart Home Assistant."
    }
  }
}
```

上面的代码使用第二个密钥, 当实体仍在使用时 `deprecated_entity_used` 。 在 `deprecated_entity` 旁边添加它, 标题相同, 并在描述中加一个 `{items}` 占位符: 那就是自动化和脚本列表去的地方 。 它的描述告诉用户更新这些以及任何仪表板和模板,然后禁用腐烂的实体并重新启动.

### 删除整合 {#remove-these-once-the-module-has-no-deprecated-constants-left}

当一个集成公司停止为善时,例如因为供应商关闭了其API,就去掉它. 将其拆卸到一个产生 `ERROR` 问题的树根上, 并保留一个最小的 `config_flow.py` , 因此已有的条目仍然在加载, 并且用户看到发生了什么 。 既定的翻译密钥为 `integration_removed` :

```python
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Set up the integration from a config entry."""
    ir.async_create_issue(
        hass,
        DOMAIN,
        DOMAIN,
        is_fixable=False,
        severity=ir.IssueSeverity.ERROR,
        translation_key="integration_removed",
        translation_placeholders={
            "entries": f"/config/integrations/integration/{DOMAIN}",
        },
    )

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Unload a config entry."""

async def async_remove_entry(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Remove a config entry."""
    if not hass.config_entries.async_loaded_entries(DOMAIN):
        ir.async_delete_issue(hass, DOMAIN, DOMAIN)
```

`entries` 占位符链接到用户的配置项 。 在文本中解释为什么删除整合,并且他们可以删除条目. 问题在于整合,而不是一个配置条目,所以所有条目都共享,没有`config_entry_id`. 保留一个空的 `async_unload_entry`, 这样条目仍然可以卸载和重新装入, 并在 `async_remove_entry` 中删除 。 卸载时不要删除它: 重装会带回一个被用户忽略的问题 。

当集成被后继者所取代时,它是一个贬值:使用 `WARNING` 和一个 `breaks_in_ha_version` , 并中止配置 与 `deprecated` 的原因, 所以没有人可以添加新的条目 。

### 文件和测试 {#functions-methods-and-classes}

修补问题和发行笔记宣布贬值. 在 [Home Assistant.io](https://www.home-assistant.io/)  Theodorn 晴pre 上的文档中不要添加一个 repression 通知 : 它只描述今天的工作 。

用 `issue_registry` 固定 测试是否创建了这个问题, 在删除最后一个配置条目时再次删除, 在重新装入条目时不删除 。

## ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,执行,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,执行,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,执行,,,,,,,,,,执行,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,, {#patterns}

现在我们可以看看其它集成导入或子类的任何东西都是核心 API : [`homeassistant/helpers/`](https://github.com/home-assistant/core/tree/dev/homeassistant/helpers),[`homeassistant/const.py`](https://github.com/home-assistant/core/blob/dev/homeassistant/const.py)中的一切,以及[`homeassistant/components/sensor/`](https://github.com/home-assistant/core/tree/dev/homeassistant/components/sensor)这样的实体平台. 更改一个会影响[自定义集成](/glossary/custom-integration)的作者,他们需要时间作出反应. 这些贬值时间为12个月,在[博客](https://contributors.home-assistant.io/blog/)上有一个职位,如果有的话,指定替换者,并解除撤职。

下方的帮助者登录一个警告, 以名称命名使用已贬值代码的集成 。 它们不创建修复问题:用户无法修复自定义集成的代码.

### 常数、别名和海内成员 {#tests}

以 `_DEPRECATED_` 前缀重命名旧常数,将其包起来,并添加三个模块钩. 你应当诵读旧名,然后,你应当警告:

```python
from functools import partial

from homeassistant.helpers.deprecation import (
    DeprecatedConstantEnum,
    all_with_deprecated_constants,
    check_if_deprecated_constant,
    dir_with_deprecated_constants,
)

_DEPRECATED_CONCENTRATION_GRAMS_PER_CUBIC_METER = DeprecatedConstantEnum(
    UnitOfDensity.GRAMS_PER_CUBIC_METER, "2027.8"
)

# Remove these once the module has no deprecated constants left. {#remove-these-once-the-module-has-no-deprecated-constants-left}
__getattr__ = partial(check_if_deprecated_constant, module_globals=globals())
__dir__ = partial(
    dir_with_deprecated_constants, module_globals_keys=[*globals().keys()]
)
__all__ = all_with_deprecated_constants(globals())
```

的确切值使用 `DeprecatedConstant`, `DeprecatedConstantEnum` 表示一个enum成员, 当一个类或函数移动时使用 `DeprecatedAlias` 。 使用 `EnumWithDeprecatedMembers` 元级 来贬低您所保存的缩写 :

```python
class MediaPlayerState(
    StrEnum,
    metaclass=EnumWithDeprecatedMembers,
    deprecated={
        "STANDBY": (
            "MediaPlayerState.OFF or MediaPlayerState.IDLE",
            "2026.8.0",
        ),
    },
):
    """State of media player entities."""

    OFF = "off"
    IDLE = "idle"
    STANDBY = "standby"
```

1920 折旧常数只在读取它们的代码属于集成时才会发出警告. 核心密码和测试都默读 这就是为什么下面的测试帮助者通过定制的集成.

### 知道吗将提供向工作组均已 让他 你说什么 在这,中中中中中,,中中,,,,,,,,中,,,,,,,,,,,,,中,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,中,,,,,,,,,,,,,中,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,中,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,, {#知道吗将提供向工作组均已-让他-你说什么-在这中中中中中中中中中中中中}

```python
@deprecated_function(
    "homeassistant.helpers.sun.get_astral_observer",
    breaks_in_ha_version="2027.7",
)
@callback
def get_astral_location(hass: HomeAssistant) -> tuple[Location, Elevation]:
    """Get an astral location for Home Assistant."""
```

`@deprecated_class`当类被即时警告,是保持一个重新命名的类作为别名的方式. 两者都以替换为字符串. 要对函数不再需要的主导 `hass` 论点进行贬值, 请使用 `@deprecated_hass_argument` 。 它警告,并放弃争论。

### 模式 {#patterns}

有时问题不是名字,而是使用某种东西的方式,比如设置一个想要消失的属性,或者调用一个平台现在所取代的函数. 使用来自 `homeassistant.helpers.frame` 的 `report_usage()` :

```python
report_usage(
    "calls system_health.async_register_info, which is deprecated; "
    "add a system_health platform instead",
    breaks_in_ha_version="2027.1",
    core_behavior=ReportBehavior.ERROR,
    exclude_integrations={DOMAIN},
)
```

第一个参数插入到“ 检测到集成的域” 中, 所以把它写成动词短语 。

`report_usage()`通过行走调用堆栈魄力找到负责的集成. 这在整合中称为堕落代码本身时是有效的魄力. 当核心读到之前设定的集成物时,比如一个被贬值的实体属性,则不起作用:到那时,集成物就不再堆叠了. 在这种情况下,通过`integration_domain`,从一个知道它来自哪里的物体,就像`self.platform.platform_name`在一个实体上。

三个参数决定谁得到什么。 每个都使用 `ReportBehavior` 殆尽 `IGNORE` 不说, `LOG` 记录一次每个呼叫者在 `level` 已在 `ERROR` 记录并升起 `RuntimeError` 。

| 参数假如 | proceedings 适用于 | 默认 |
| --- | --- | --- |
| `core_behavior` | 代码在 [`homeassistant/`](https://github.com/home-assistant/core/tree/dev/homeassistant) 中, 堆栈上没有集成 | `ERROR` |
| `core_integration_behavior` | 融合中构建的 | `LOG` |
| `custom_integration_behavior` | 自定义集成 | `LOG` |

默认通常是对的:核心代码在测试中响亮失败,集成得到警告. 当您仍在迁移集成中构建的, 请设置 `core_integration_behavior` 到 `IGNORE` , 因此自定义集成的作者会得到警告, 而不需要日志填充您已经修复的大小写 。

### 所面对的问题 {#所面对的问题}

{ AppleiH0}有 `import_and_test_deprecated_constant`,`import_and_test_deprecated_constant_enum`,`import_and_test_deprecated_alias`, 和 `help_test_all` 的过期名称 。 `mock_integration_frame` 固定帮助您测试 `report_usage()` 警告 。
