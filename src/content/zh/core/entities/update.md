---
title: 更新实体
description: 构建一个更新实体,告诉用户新的固件或软件版本是可用的,让他们安装.
sidebarLabel: 知道了 更新
sidebarGroup: 家电
---

# 更新实体 {#update-entity}

一个更新实体告诉用户,一个设备或服务有较新的版本,例如灯泡或路由器的固件,或应用程序或容器的软件。 它也可以从 Home Assistant 安装该更新, 显示发布注释, 并在安装时报告进度 。 从`UpdateEntity` 继承到`homeassistant.components.update` 。

用户在 Home Assistant 本身的更新旁边的 **Settings ** 中找到可用的更新. 前端如何显示 [更新更多信息视图](/design/more-info/update) 。

## 的临时议程 {#properties}

更新实体在 [一般实体属性](/core/entities/entity-class) 上方有这些属性 。 每个属性都可以以其`_attr_`属性设定,如`_attr_installed_version`.

| 名称 | 类型 | 默认 | 说明 |
| ---- | ---- | ------- | ----------- |
| `installed_version` | `str \| None` | `None` | 现在安装和使用的版本. |
| `latest_version` | `str \| None` | `None` | 最新版本可用. |
| `title` | `str \| None` | `None` | 软件的名称, 如`Tasmota`, 当它与设备或实体名称不同时 。 |
| `release_summary` | `str \| None` | `None` | 发行笔记的简短摘录. 以255字符剪辑. |
| `release_url` | `str \| None` | `None` | 链接到完整发布注释. |
| `auto_update` | `bool` | `False` | 设备或服务自我更新 。 用户不能跳过此实体的版本 。 |
| `in_progress` | `bool \| None` | `False` | 安装是否正在运行 。 需要 `UpdateEntityFeature.PROGRESS` 。 |
| `update_percentage` | `int \| float \| None` | `None` | 安装距离有多远,从0到100. 要求 `UpdateEntityFeature.PROGRESS`, 并且只在 `in_progress` 是 `True` 时显示 。 |
| `display_precision` | `int` | `0` | `update_percentage` 的十进制数 。 |
| `device_class` | `UpdateDeviceClass \| None` | `None` | 那种更新。 见[设备类](/core/entities/update#device-classes). |
| `restart_required` | `bool` | `False` | Home Assistant 此更新安装后需要重新启动 。 见[安装](/core/entities/update#install). |
| `has_update` | `bool` | 比较版本 | 是否有更新。 见[决定是否有更新](/core/entities/update#decide-whether-an-update-is-available). |

更新实体更改一些通用默认 :

- 当实体支持 `INSTALL` 和 `EntityCategory.DIAGNOSTIC` 时, `entity_category` 是 `EntityCategory.CONFIG` 。 自己来控制它 当实体有实体描述时,则使用描述的`entity_category`代替. `UpdateEntityDescription` 默认为`EntityCategory.CONFIG` 。
- `entity_picture`是您整合的品牌图标 。
- 一个没有名字但带有设备类的实体,以其设备类命名,如**Firmware**.

## 支持的特性 {#supported-features}

将 `UpdateEntityFeature` 的值与位符或 (`|`) 运算符合并 。 Home Assistant 当需要`update.install` 动作时检查它们, 拒绝实体不支持的东西 。

| 数值 | 说明 |
| ----- | ----------- |
| `INSTALL` | 书面材料的更新诠释可以各种各样。 书面材料 |
| `SPECIFIC_VERSION` | 一个特定的版本可以安装,以`version`传递到`install`. |
| `BACKUP` | 当 `backup` 是 `True` 时, 设备或服务可以在安装前进行备份 。 |
| `PROGRESS` | 实体报告安装进度为 `in_progress` 和`update_percentage` 。 |
| `RELEASE_NOTES` | 实体可以获取完整的释放笔记. 执行`release_notes`。 |

没有 `PROGRESS`, Home Assistant 仍然显示一个安装正在运行: 它将 `in_progress` 自己设置, 只要您的安装方法运行即可 。 设定 `PROGRESS` 当设备报告真实进展时, 它会给用户一个更好的图片 。

## 设备类 {#device-classes}

| 数值 | 说明 |
| ----- | ----------- |
| `UpdateDeviceClass.FIRMWARE` | 更新是设备的固件 。 |

## 方法 {#methods}

### 安装 {#install}

需要`UpdateEntityFeature.INSTALL`. 执行`install`或`async_install`。

```python
async def async_install(
    self, version: str | None, backup: bool, **kwargs: Any
) -> None:
    """Install an update."""
```

`version` 是要安装的版本, 或 `None` 为最新版本 。 `backup`先请求备份。 当 `update.install` 动作调用它时, Home Assistant 已经检查过有要安装的东西, 没有安装正在运行, 并且实体支持请求的版本和备份 。

安装完成后返回, 或启动 `HomeAssistantError` 失败时返回 。 不管结局如何, Home Assistant 然后将 `_attr_in_progress` 重排到 `False` 并写入状态 。 如果您超过 `in_progress` 属性, 请确保它届时报告 `False` 。

如果彗星更新只在 Home Assistant 重新启动后生效, 则设置 `restart_required` 到 `True` 。 一旦安装完成而不提升,实体[请求重启](/core/integrations/restart-required)代表您的整合. 安装失败不会 。

### 的一点是 {#release-notes}

需要 `UpdateEntityFeature.RELEASE_NOTES` 。 执行`release_notes`或`async_release_notes`,并返回最新版本的完整发布注释。 前端在用户安装前在更多信息对话框中显示它们,并让Markdown.

```python
async def async_release_notes(self) -> str | None:
    """Return the release notes."""
```

### 比较版本 {#compare-versions}

默认情况下, 当 [厉害的版本](https://github.com/ludeeus/awesomeversion) 说到此时, 版本会算为更新 。 如果您的版本比较不理想, 请覆盖 `version_is_newer` 。

```python
def version_is_newer(
    self, latest_version: str, installed_version: str
) -> bool:
    """Return True if latest_version is newer than installed_version."""
```

### 决定是否有更新 {#decide-whether-an-update-is-available}

一些设备或服务直接告诉你是否有更新可用,而不是给出版本Home Assistant可以比较. 覆盖这些 `has_update` 的财产 。

```python
@property
def has_update(self) -> bool:
    """Return whether an update is available."""
    return self.device.update_available
```

Home Assistant只读 `has_update` 当 `installed_version` 和 `latest_version` 都已知和不同时, 而用户没有跳过最新版本 。 默认情况下,它会呼叫`version_is_newer`.

## 状态 {#states}

状态是 `on` 当有更新可用 `off` 当安装的版本是最新版本 。 Home Assistant从 `installed_version` 和 `latest_version` 来研究这个问题; `state` 属性是最终的 。

- 当任一版本为`None`时,状态为`unknown`.
- 两个版本相同时,状态日第`off`.
- 当用户跳过最新版本时,状态是 `off` 直至更新版本出来 。
- 否则,该州就跟着`has_update`. 默认情况下,当最新版本更新时,也就是`on`,以及当版本无法比较时.

跳过和清除跳过版本由 Home Assistant 处理 。 你不执行它们。

## 示例 {#example}

```python
from typing import Any

from homeassistant.components.update import (
    UpdateDeviceClass,
    UpdateEntity,
    UpdateEntityFeature,
)

class MyFirmwareUpdate(MyEntity, UpdateEntity):
    """Firmware updates for the device."""

    _attr_device_class = UpdateDeviceClass.FIRMWARE
    _attr_supported_features = (
        UpdateEntityFeature.INSTALL | UpdateEntityFeature.PROGRESS
    )

    def __init__(self, coordinator: MyCoordinator) -> None:
        """Set up the entity."""
        super().__init__(coordinator)
        self._attr_unique_id = f"{coordinator.device.serial}_firmware"

    @property
    def installed_version(self) -> str | None:
        """Return the installed firmware version."""
        return self.coordinator.data.firmware

    @property
    def latest_version(self) -> str | None:
        """Return the newest firmware version."""
        return self.coordinator.data.latest_firmware

    @property
    def in_progress(self) -> bool:
        """Return whether the firmware is being installed."""
        return self.coordinator.data.updating

    @property
    def update_percentage(self) -> int | None:
        """Return the install progress."""
        return self.coordinator.data.update_progress

    async def async_install(
        self, version: str | None, backup: bool, **kwargs: Any
    ) -> None:
        """Install the latest firmware."""
        await self.coordinator.device.install_firmware()
        await self.coordinator.async_request_refresh()
```

`MyEntity` 是集成的共享基础实体, 一个 `CoordinatorEntity` 设置 `_attr_has_entity_name = True` 和设备信息 。 该实体没有它自己的名字,因此它被命名为**Firmware**,以它的设备类.
