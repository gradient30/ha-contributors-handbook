---
title: 备份
description: 添加一个存储 Home Assistant 备份的备份代理, 或者准备您的集成备份 。
sidebarGroup: 集成功能
order: 9
---

# 备份 {#backup}

一个集成可以以两种方式参与备份,两种方式都是在 `backup.py` 平台文件中:

- **一个备份代理**存储备份某处:一个网络共享,一个云存储服务,或者其他任何东西. 用户在备份设置中选择代理 。
- ** Pre and Post hooks ** 在备份前暂停或准备您的整合,并在备份后恢复。

## 添加备份代理 {#add-a-backup-agent}

备份代理从 `homeassistant.components.backup` 延伸 `BackupAgent` , 并执行五种方法 :

```python
from collections.abc import AsyncIterator, Callable, Coroutine
from typing import Any

from homeassistant.components.backup import (
    AgentBackup,
    BackupAgent,
    BackupAgentError,
    BackupNotFound,
    OnProgressCallback,
)

class ExampleBackupAgent(BackupAgent):
    """Store backups at Example."""

    domain = DOMAIN

    def __init__(self, entry: ExampleConfigEntry) -> None:
        """Initialize the agent."""
        super().__init__()
        self._client = entry.runtime_data
        self.name = entry.title
        self.unique_id = entry.entry_id

    async def async_upload_backup(
        self,
        *,
        open_stream: Callable[[], Coroutine[Any, Any, AsyncIterator[bytes]]],
        backup: AgentBackup,
        on_progress: OnProgressCallback,
        **kwargs: Any,
    ) -> None:
        """Upload a backup."""

    async def async_download_backup(
        self, backup_id: str, **kwargs: Any
    ) -> AsyncIterator[bytes]:
        """Download a backup."""

    async def async_delete_backup(self, backup_id: str, **kwargs: Any) -> None:
        """Delete a backup."""

    async def async_list_backups(self, **kwargs: Any) -> list[AgentBackup]:
        """List the backups."""

    async def async_get_backup(
        self, backup_id: str, **kwargs: Any
    ) -> AgentBackup:
        """Return one backup."""
```

- `domain`, `name` 和`unique_id` 识别代理 。 保持`unique_id`稳定。
- `async_upload_backup` 获得一个打开备份流的函数, 以及 `backup` 中的备份元数据 。
- 当备份不存在时, `async_download_backup`, `async_delete_backup` 和`async_get_backup` 提高`BackupNotFound` 。
- 在其它任何错误上, 提升 `BackupAgentError` , 或扩展它的例外 。 其他例外情况预计不会离开代理人。

### 报告上传进度 {#report-upload-progress}

在您上传时拨打 `on_progress`, 例如在每个块后, 上面传的字节总数 。 Home Assistant 用它来显示UI中上传的进展.

```python
on_progress(bytes_uploaded=bytes_sent)
```

### 告诉Home Assistant关于你的特工 {#tell-home-assistant-about-your-agents}

Home Assistant 从 `backup.py` 中的两个函数获取您的代理 :

```python
from homeassistant.core import HomeAssistant, callback

async def async_get_backup_agents(hass: HomeAssistant) -> list[BackupAgent]:
    """Return the backup agents."""
    return [
        ExampleBackupAgent(entry)
        for entry in hass.config_entries.async_loaded_entries(DOMAIN)
    ]

@callback
def async_register_backup_agents_listener(
    hass: HomeAssistant,
    *,
    listener: Callable[[], None],
    **kwargs: Any,
) -> Callable[[], None]:
    """Register a listener for when agents are added or removed."""
    hass.data.setdefault(DATA_BACKUP_AGENT_LISTENERS, []).append(listener)

    @callback
    def remove_listener() -> None:
        """Remove the listener."""
        hass.data[DATA_BACKUP_AGENT_LISTENERS].remove(listener)

    return remove_listener
```

当你的代理人改变时, 给听众打电话, 所以Home Assistant 再次要求他们。 对于遵循配置条目的代理,在 `async_setup_entry` 中,在装入或卸下条目时拨打:

```python
def _notify_backup_listeners() -> None:
    for listener in hass.data.get(DATA_BACKUP_AGENT_LISTENERS, []):
        listener()

entry.async_on_unload(entry.async_on_state_change(_notify_backup_listeners))
```

`DATA_BACKUP_AGENT_LISTENERS` 是您定义的密钥, 在 `const.py` 中 。

### 重命名代理服务器 {#rename-an-agent}

代理的ID为`<domain>.<unique_id>`,由代理的`unique_id`建立. 在配置条目上不需要匹配任何内容. 如果您的集成新版本设置不同 `unique_id`, 用户会失去代理服务器的备份设置 。 调用 `async_rename_agent` 一次将它们移动到新ID, 例如在配置输入迁移中 :

```python
from homeassistant.components.backup import async_get_manager

async def async_migrate_entry(hass: HomeAssistant, entry: ExampleConfigEntry) -> None:
    """Migrate old entry."""
    if entry.version == 1 and entry.minor_version == 1:
        

# The agent used the config entry ID, now it uses the account ID {#prepare-for-a-backup}
        async_get_manager(hass).async_rename_agent(
            f"{DOMAIN}.{entry.entry_id}", f"{DOMAIN}.{entry.data[CONF_ACCOUNT_ID]}"
        )
        hass.config_entries.async_update_entry(entry, minor_version=2)
```

- 稳妥地移动了代理器的设置,无论是自动 备份使用它还是失败的上传到它. 代理店的备份不被触摸.
- 在 `manifest.json` 中添加 `backup` 到 `after_dependencies`, 所以备份集成是在您的迁移运行前设置的 。
- 只有在ID改变时才叫它.

## 准备支援 {#准备支援}

一些集成在备份莺之前需要暂停或写下它们的数据,这样可以正常恢复. 将这两个函数添加到 `backup.py` 或运行 `python3 -m script.scaffold backup` :

```python
from homeassistant.core import HomeAssistant

async def async_pre_backup(hass: HomeAssistant) -> None:
    """Prepare for a backup."""

async def async_post_backup(hass: HomeAssistant) -> None:
    """Resume after a backup."""
```
