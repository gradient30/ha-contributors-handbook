---
title: 探索你自己的数据
description: 设置 JupyterLab，将其连接到你的 Home Assistant 数据库，并运行你的第一个报表。大约十五分钟。
order: 2
source: https://github.com/home-assistant/home-assistant-notebooks/blob/master/GETTING_STARTED.ipynb
lastVerified: 2026-10-16
---


# 探索你自己的数据 {#explore-your-own-data}
最后核实于2026-10-16，相对于https://github.com/home-assistant/home-assistant-notebooks/blob/master/GETTING_STARTED.ipynb.

Home Assistant 会将你家中发生的所有事情记录在数据库中：每一次状态变化、每一个事件，以及随时间变化的统计数据。这些数据属于你自己，你可以从中学到很多东西。供暖什么时候运行？哪些灯开得时间最长？你的能源使用量如何随季节变化？

本指南将安装 [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/)，这是全球数据科学家常用的工具，并在你的数据上运行第一个报告。你的数据始终保存在你自己的硬件上。

## 如何组合在一起 {#how-it-fits-together}
- **JupyterLab** 运行笔记本：混合了文本、代码和图表的文档。可以把笔记本看作是一个可以计算的文档。
- **HASS 数据侦探** 是一个 Python 库，可以读取 Home Assistant 数据库，并将其转换为可操作的表格。
- **Home Assistant 笔记本** 是现成的笔记本，可从 [home-assistant-notebooks 仓库](https://github.com/home-assistant/home-assistant-notebooks) 开始使用。

## 选项 1：作为 Home Assistant OS 上的应用程序 {#option-1-as-an-app-on-home-assistant-os}
如果你运行 Home Assistant OS，最简单的方法是从 Home Assistant 社区应用中获取 JupyterLab 应用程序。

1. 打开 [你 Home Assistant 上的 JupyterLab 应用](https://my.home-assistant.io/redirect/supervisor_app/?app=a0d7b954_jupyterlablite&repository_url=https%3A%2F%2Fgithub.com%2Fhassio-addons%2Frepository)。如果你还没有社区应用仓库，这也会添加它。
2. 安装应用程序并启动它。
3. 打开应用程序的网页界面。第一次启动可能需要一分钟。

该应用程序可以访问你的配置文件夹，其中存放默认数据库 `home-assistant_v2.db`。第一次启动时，它还会将 Home Assistant 笔记本克隆到该文件夹中的 `notebooks/home-assistant`，因此你可以跳过接下来获取笔记本的步骤。

## 选项 2：在你自己的电脑上 {#option-2-on-your-own-computer}
如果你以另一种方式运行 Home Assistant，或者希望在独立电脑上操作，请使用 Python 安装 JupyterLab：

```bash
mkdir ~/notebooks
cd ~/notebooks
python3 -m venv .venv
source .venv/bin/activate
pip install jupyterlab HASS-data-detective seaborn
jupyter lab
```

JupyterLab 会在你的浏览器中打开。Data Detective 读取数据库，seaborn 绘制图表。

在 Python 3.13 或更新版本中，pip 会安装 HASS Data Detective 3.2，因为后续版本需要较旧的 Python。该笔记本适用于 3.2。

你需要能够访问数据库。对于默认的 SQLite 数据库，请将 `home-assistant_v2.db` 从你的配置文件夹复制到你的电脑。在 Home Assistant 停止运行时或从备份复制，以避免获得不完整的文件。

如果你使用 MariaDB、MySQL 或 PostgreSQL 作为记录器，请直接连接到它。为此创建一个具有只读权限的独立数据库用户。你的笔记本仅需读取数据。Python 也需要该数据库的驱动程序。在相同的虚拟环境中安装它，并使用匹配前缀启动数据库 URL：

- **MariaDB 或 MySQL**: `pip install pymysql`，并且 URL 以 `mysql+pymysql://` 开头。如果你复制的 `db_url` 从 `mysql://` 开始，请更改该部分。
- **PostgreSQL**: `pip install "psycopg[binary]"`，并且 URL 以 `postgresql://` 开头。

在 PostgreSQL 服务器上，一个名为 `hass` 的记录器数据库的只读用户如下所示：

```sql
CREATE USER datascience WITH PASSWORD 'my_secret_password';
GRANT CONNECT ON DATABASE hass TO datascience;
GRANT USAGE ON SCHEMA public TO datascience;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO datascience;
ALTER DEFAULT PRIVILEGES IN SCHEMA public
  GRANT SELECT ON TABLES TO datascience;
```

`ALTER DEFAULT PRIVILEGES` 语句仅适用于由运行它的用户创建的表。以 Home Assistant 连接的用户身份运行它，新用户也可以读取未来模式迁移创建的表。

## 获取笔记本 {#get-the-notebooks}
在你自己的电脑上，从 JupyterLab 启动器打开一个终端，并克隆笔记本：

```bash
git clone https://github.com/home-assistant/home-assistant-notebooks.git
```

## 运行你的第一个报告 {#run-your-first-report}
1. 在左侧的文件浏览器中，打开 notebooks 文件夹（在你自己的电脑上是 `home-assistant-notebooks`，在应用中是 `notebooks/home-assistant`），然后 `GETTING_STARTED.ipynb`。
2. 找到含有 `db = detective.db_from_hass_config()` 的代码单元。在应用中，保持原样：它会通过你的配置找到数据库。在你自己的电脑上，它无法找到数据库，因此用你自己的副本连接替换该行。对于放在与笔记本相同文件夹中的 `home-assistant_v2.db` 副本：

   ```python
   db = detective.HassDatabase("sqlite:///home-assistant_v2.db")
   ```

   对于 MariaDB、MySQL 或 PostgreSQL，请传入与你的记录器 `db_url` 相同类型的数据库 URL。
3. 从上到下运行单元：选择第一个代码单元，按 <kbd>Shift</kbd>   <kbd>Enter</kbd> 来运行并跳到下一个单元。笔记本将你的传感器数据读取到表格中，并进行绘图。它可以与 SQLite、MariaDB、MySQL 和 PostgreSQL 一起使用，点击 **运行** > **运行所有单元格** 可以一次性运行所有单元格。在大型数据库上，这需要一些时间。一个仍在运行的单元格旁边会显示 `[*]`。完成后，星号会变成一个数字。

## 使用 pandas 读取数据库 {#read-the-database-with-pandas}
要从头开始，或者查看笔记本的底层操作：[pandas](https://pandas.pydata.org/) 和 SQLAlchemy，前面提到的 `pip install` 已经引入，可以直接读取数据库。在笔记本的新单元格中粘贴以下内容，放在你的 `home-assistant_v2.db` 旁边：

```python
import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine("sqlite:///home-assistant_v2.db")

query = sqlalchemy.text("""
    SELECT states_meta.entity_id, states.state, states.last_updated_ts
    FROM states
    JOIN states_meta ON states.metadata_id = states_meta.metadata_id
    WHERE states_meta.entity_id LIKE 'sensor.%'
""")

df = pd.read_sql(query, engine)
df["last_updated"] = pd.to_datetime(
    df["last_updated_ts"], unit="s", utc=True
)
df["state"] = pd.to_numeric(df["state"], errors="coerce")
df = df.dropna(subset=["state"])

print(df.groupby("entity_id")["state"].describe())
```

这会读取所有传感器的状态，将时间戳转换为日期，只保留数值状态，并打印每个传感器的计数、平均值、最小值和最大值。从这里，`df` 是一个常规的 pandas 表，你可以进行筛选、分组和绘图。

查询是普通的 SQL，与笔记本在每个数据库上使用的查询相同，所以对于 MariaDB、MySQL 或 PostgreSQL，你只需更改数据库 URL。

## 自定义你的内容 {#make-it-your-own}
最棒的部分是：笔记本中的所有内容都可以更改。编辑一个单元格，只运行该单元格，即可立即看到新的结果。你不需要再次运行整个笔记本。

当你想进一步探索时：

- [HASS 数据侦探示例](https://github.com/robmarkcole/HASS-data-detective) 展示了更多查询和绘制数据的方法。
- [数据模型](/data/reference/data-model) 和 [数据库架构](/data/reference/database-schema) 解释了数据库中的内容。
- [查询数据库](/data/guides/query-the-database) 提供了可供起步的 SQL 查询。

## 分享你的学习成果 {#share-what-you-learn}
做了一个其他人可以使用的笔记本吗？分享不带输出的笔记本，这样它就不会包含你家的任何数据，别人可以在自己的数据上运行它。[社区论坛](https://community.home-assistant.io/) 是展示它的好地方。
