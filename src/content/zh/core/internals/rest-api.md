---
title: REST API
description: HTTP 的端点在 / api/ 下读取状态, 调用动作, 点火事件, 并渲染模板, 并有每个人所需的权限 。
sidebarGroup: API
order: 30
---

# (原始内容存档于2018-09-21) (英语). Rest API {#rest-api}

以 Supervisor 运行 Supervisor 时, 如 Home Assistant OS 运行 Supervisor , 则在 Home Assistant OS 的 Supervisor 中, 在 Supervisor 中 , 在 Supervisor 中 , 在 Supervisor 中 , 在 Supervisor 中 , 则 以 Supervisor 操作 , 则 在 Supervisor 中 使用 。 `SETUP_PORT` 环境变量覆盖默认值 。 它接受并返回JSON。 `api` 集成提供了它, 只要前端是, 它就会被加载 。

冉瑞特API对于来自脚本和其他系统的简单,一次性请求是很好的. 对于需要保持连接或跟随变化的任何东西,请使用[API (韩语)](/core/internals/websocket-api). 前端使用这个,它还有许多命令。

## 认证

每个请求都需要在 `Authorization` 页眉中有一个访问符 。 对于脚本,请在您的 profile 下创建一个长寿的访问符, 在 ** Security ** 下. 应用程序见[认证 API](/core/internals/auth-api)。

```shell
curl \
  -H "Authorization: Bearer TOKEN" \
  -H "Content-Type: application/json" \
  http://homeassistant.local:8123/api/
```

与 Python 中相同的请求, 与 `requests` :

```python
import requests

response = requests.get(
    "http://homeassistant.local:8123/api/states/sun.sun",
    headers={"Authorization": "Bearer TOKEN"},
    timeout=10,
)
print(response.json())
```

成功请求返回状态 200, 或创建某物时的201 。 常见的错误有400(错误请求),401(未经授权),404(未找到)和405(不允许的方法). 错误失败的动作返回500, 当 Home Assistant 正在关闭时, 每个端点返回 503.

一些端点需要管理员. 标记如下**admin**。 其他人只返回用户可能读到的内容, 遵循他们的[权限](/core/internals/permissions) 。

## 状况和配置 {#status-and-configuration}

### 获取 / api/ {#get-api}

返回 `{"message": "API running."}` 如果 API 上升 。 注意跟踪斜线:路径是`/api/`,而不是`/api`。

### 获取/ api/ 配置 {#get-apiconfig}

返回 [核心配置作出有效调整](/core/internals/hass#the-core-configuration): 位置、 单位、 时区、 版本、 装入的组件等 。

```json
{
  "location_name": "Home",
  "latitude": 52.37,
  "longitude": 4.89,
  "elevation": 0,
  "unit_system": {
    "length": "km",
    "mass": "g",
    "temperature": "°C",
    "volume": "L"
  },
  "time_zone": "Europe/Amsterdam",
  "version": "2026.10.0",
  "components": ["api", "frontend", "http", "sun"],
  "state": "RUNNING"
}
```

造福于人的例子有所缩短。 造福于人类,

### 获取/api/ 核心/状态 {#get-apicorestate}

返回核心是否运行,数据库迁移是否正在进行中。 作为快速健康检查,例如Supervisor。

```json
{
  "state": "RUNNING",
  "recorder_state": {
    "migration_in_progress": false,
    "migration_is_live": false
  }
}
```

### 获取/ api/ 组件 {#get-apicomponents}

返回已加载组件的列表。

### POST / api/ 配置/ 核心/ 检查  config {#post-apiconfigcorecheckconfig}

同时还返回了 `result` (`valid` 或 `invalid`) , 和 `errors` 和 `warnings` 作为文本, 或 `null` 。

## 状态 {#states}

### 与时局不同。 {#get-apistates}

返回用户可能读取的所有状态, 作为 [状态对象](/core/internals/states#the-state-object) 列表 。

### 获取/ api/ states/ &lt; 实体  id&gt; {#get-apistatesltentityidgt}

返回一个实体的状况,或404。

```json
{
  "entity_id": "sun.sun",
  "state": "below_horizon",
  "attributes": {
    "friendly_name": "Sun",
    "elevation": -17.67
  },
  "last_changed": "2026-10-10T21:43:29.204838+00:00",
  "last_reported": "2026-10-10T21:50:30.529465+00:00",
  "last_updated": "2026-10-10T21:50:30.529465+00:00",
  "context": {
    "id": "01J9Z7K1M3S8TQ0Y6E4H2B5N7C",
    "parent_id": null,
    "user_id": null
  }
}
```

### POST / api/ states/ &lt; 实体  id&gt; 主题 {#post-apistatesltentityidgt}

页:1 创建或替换一个状态。 身体需要 `state` , 可以有 `attributes` :

```json
{
  "state": "25",
  "attributes": {
    "unit_of_measurement": "°C"
  }
}
```

如果状态是新状态,则返回201,如果存在的话返回200,身体中的新状态和一个`Location`头指向它. 添加 `"force_update": true` 以启动状态变化, 即使没有改变 。

> [!IMPORTANT]
> 这只会改变 Home Assistant 显示的内容 。 它不会对设备说话,实体的下一次更新会覆盖它. 要控制一个设备,请叫动作.

### DELETE / api/ states/ &lt; 实体  id&gt; {#delete-apistatesltentityidgt}

页:1 删除状态。 如果不存在,则返回404。

## 动作 {#actions}

### 获取/api/服务 {#get-apiservices}

轩 返回按域分类的已注册动作。轩路仍然使用旧名,服务.

### POST / api/ services/ &lt; domain&gt;/&lt; service&gt; 存档副本. {#post-apiservicesltdomaingtltservicegt}

要求行动,等待行动完成。 主体是动作数据,可以包括目标:

```shell
curl \
  -H "Authorization: Bearer TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"entity_id": "light.kitchen"}' \
  http://homeassistant.local:8123/api/services/light/turn_on
```

返回因此调用而更改的状态列表 。 要获取 [响应数据](/core/integrations/actions#return-response-data), 请在 URL 中添加 `?return_response` 。 反应是这样的:

```json
{
  "changed_states": [],
  "service_response": {
    "weather.forecast_home": {
      "forecast": []
    }
  }
}
```

使用 `?return_response` 用于支持它的行动, 只用于那些 。 留到一个只返回数据的动作,或者添加到一个没有响应数据的动作,就可以得到一个400.

## 傀儡 {#events}

### 获取/api/事件 {#get-apievents}

返回有听众的事件类型,以及每个听众的数量。

### POST / api/ events/ &lt; event  type&gt; 请检查url=值 (帮助). {#post-apieventslteventtypegt}

页:1 开一活动. 可选主体是事件数据:

```json
{
  "button_id": "front_door"
}
```

返回 `{"message": "Event front_door_pressed fired."}`, 消息中包含您的事件类型 。 事件被存储在数据库中,所以要注意你发射的东西.

### 获取/api/流 {#get-apistream}

页:1 作为服务器发送事件的所有事件流 。 通过 `?restrict=state_changed,call_service` 将其限制在一些事件类型 。 WebSocket API的`subscribe_events` 是新代码的更好选择 。

## 模板 {#templates}

### POST / api/ 模板 {#post-apitemplate}

页:1 渲染 [以用用为为的用用为的用为为的用用为的用用为的用用为的用用为的用用用为的用用用的用用用的用用用的用用的用用用的用用用的用用

```json
{
  "template": "It is {{ states('sensor.temperature') }} degrees."
}
```

## 历史和日志 {#history-and-logbook}

这些来自 {H 听着} 和 `logbook` 集成, 它们是默认配置的一部分 。

### 获取/api/ 历史/ 期间/ &lt;timestamp&gt; {#get-apihistoryperiodlttimestampgt}

返回实体的状态历史。 时间戳和`2026-10-01T00:00:00+02:00`一样,是周期的开始,是可选的:它默认为一天前. 查询参数 :

- `filter_entity_id`: 必需。 一个或多个实体ID,用逗号分隔.
- `end_time`:期末有助于加强,URL编码. 默认为开始后的一天.
- `minimal_response`:只返回`state`和`last_changed`,用于第一和最后两个状态。 远快婿
- `no_attributes`: 跳过属性 。 还有更快。
- `significant_changes_only=0`: 返回每一个变化。 默认情况下, 您只能得到显著的更改 。
- `skip_initial_state`:期初时省去州.

答复是每个实体一份国家名单。

### 获取 /api/ logbook/ &lt;timestamp&gt; {#get-apilogbooklttimestampgt}

返回日志条目,从可选时间戳开始。 没有时间戳,它从今天的开始,从当地时间开始。 查询参数 :

- `entity`: 一个或多个实体ID,用逗号分隔.
- `end_time`:期末,URL编码.
- `period`:没有`end_time`时返回的天数。 默认为 1 。
- `context_id`:只有一个上下文的条目。 无法与 `entity` 合并 。

## 其他整合 {#other-integrations}

几个集成点增加了自己的终点:

- `GET /api/error_log`(**Admin**):本届会议的日志,作为纯文本。
- `GET /api/camera_proxy/<entity_id>`:相机的当前图像.
- `GET /api/calendars`:日历实体。 `GET /api/calendars/<entity_id>?start=<timestamp>&end=<timestamp>` 返回该期间一个日历的事件 。
- ổ:处理 [意图](/core/internals/intents#fire-an-intent)。
- `POST /api/conversation/process` : 向对话代理发送文本 。 见[对话框 API](/core/internals/conversation-api).

## 添加自己的终点 {#add-your-own-endpoint}

一个集成可以以 `HomeAssistantView` 从 `homeassistant.helpers.http` 添加端点, 注册于 `hass.http.register_view(MyView())` 。蛊设 `url` 和 `name` , 并执行 我们现在的 `get` 、 `post` 或其他方法 。 视图需要认证, 除非您设置 `requires_auth = False` 。 例见[权限](/core/internals/permissions#in-an-http-view).

先想两想 大多数特性属于 WebSocket 前端可以直接使用的API. 当 Home Assistant 外面的东西需要调用时, 或当您服务文件时, HTTP 视图才合适 。
