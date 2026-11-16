---
title: Compose 与设计系统
description: 使用 Jetpack Compose、HATheme 和 `HA*` 组件构建 Android UI。预览、Compose 目录、部件和导航。
sidebarLabel: 组成和设计系统
sidebarGroup: 写代码
order: 1
---

# Compose 与设计系统 {#compose-and-the-design-system}

Android 应用中的所有新用户界面都是 [Jetpack Compose](https://developer.android.com/compose)。没有新的 XML 布局、数据绑定或视图绑定。新小部件使用 [Jetpack Glance](https://developer.android.com/develop/ui/compose/glance)；旧的 RemoteViews 小部件不再扩展。

## 设计系统 {#the-design-system}

该应用在 Material 3 之上有其自己的设计系统，在 `:common` 下的 `io.homeassistant.companion.android.common.compose` 中：

- **`HATheme`** 在亮色和暗色模式下应用 Home Assistant 颜色。在 `setContent` 中只需应用一次，而不是在你的屏幕可组合函数内部。
- **`HA*` 组件**，如 `HAAccentButton`、`HAFilledButton`、`HATextField`、`HACheckbox`、`HASwitch`、`HALoading`、`HADropdownMenu` 和 `HAModalBottomSheet`。它们位于主题旁边的 `composable` 包中。请使用它们而不是 Material 组件。
- **`LocalHAColorScheme.current`** 用于颜色。不要硬编码颜色。
- **`HATextStyle`** 用于排版，**`HADimens.SPACE*`** 用于间距和尺寸。填充中不要使用随意数字。

原生 Material 3 组件在亮色或暗色模式下会显示错误颜色。如果你需要的 `HA*` 包装器尚不存在，请先创建它，在它自己的 pull request 中，进行截图测试并在 Compose 目录中创建一个页面。> [!注意]
> 您还会发现 `HomeAssistantAppTheme`，这是一个基于 Material 2 的主题。它已被弃用，仅保留用于迁移剩余使用它的屏幕。不要在新的 UI 中使用它，也不要在同一屏幕中混合使用 Material 2 和 Material 3。

### Compose 目录 {#the-compose-catalog}

调试版本包含所有 `HA*` 组件的目录。可以从 [开发者游乐场](/companion/android/debugging#the-developer-playground) 打开它，点击 **启动 HA Compose 目录**。在构建新内容之前，请先检查它。

## 编写一个屏幕 {#writing-a-screen}

遵循 [UI 架构](/companion/android/ui-architecture)：一个有状态的屏幕用于收集 ViewModel 状态，以及一个无状态的内容可组合函数用于渲染它。这就是 [状态提升](https://developer.android.com/develop/ui/compose/state-hoisting)，它可以保持你的可组合函数可复用且易于预览。在此基础上：- **保持可组合函数小巧。** 将大型界面拆分为小型私有可组合函数，当文件变大时，将它们移到自己的文件中。
- **只传递可组合函数需要的内容**，而不是整个状态。
- **UI中不要包含逻辑。** 可组合函数中不要进行排序、过滤或映射。状态应该携带可显示的数据。如果必须在组合期间计算某些内容，请 `remember` 它。
- **文件命名要以组件命名**，例如 `SettingsScreen.kt` 或 `UserCard.kt`。无状态层是 `*Screen` 或 `*Content`。`*View` 是遗留的。
- **无障碍性**：在自定义可点击行上设置语义 `Role`，如 `Modifier.clickable(role = Role.Checkbox)`，并为图片提供内容描述。
- **错误和反馈** 显示在 snackbar 中，而不是 toast。
- **文本** 来自 `stringResource(R.string.*)`，字符串在 [`common/src/main/res/values/strings.xml`](https://github.com/home-assistant/android/blob/main/common/src/main/res/values/strings.xml) 中。

## 预览 {#previews}

为每个主要可组合项添加一个 `@Preview`，并用 `HAThemeForPreview` 包裹，同时绘制正确的背景：

```kotlin
@Preview
@Composable
private fun SettingsScreenPreview() {
    HAThemeForPreview {
        SettingsScreenContent(
            uiState = SettingsUiState.Default,
            onToggleSetting = {},
        )
    }
}
```

预览是迭代的最快方式：无需构建、无需服务器、无需上手指导。为每个有意义的状态、多种明暗模式以及不同屏幕尺寸添加多个预览。截图测试渲染相同的可组合项，所以一个好的预览就是到达 [截图测试](/companion/android/screenshot-testing) 的一半路程。

一旦应用运行，Android Studio 的 Compose 实时编辑和热重载可以在无需重建的情况下显示许多更改。结构性更改仍然需要重建。

## 导航 {#navigation}

应用使用 Navigation Compose，并正在迁移到一个活动使用一个导航图，由功能子图构建。新屏幕加入导航图；旧活动会随时间迁移。

使用类型安全的路由：

```kotlin
@Serializable
data class FeatureRoute(val value: Int)

fun NavGraphBuilder.featureNavGraph(navController: NavController) {
    composable<FeatureRoute> {
        FeatureScreen(
            value = it.toRoute<FeatureRoute>().value,
            onNavigateBack = { navController.popBackStack() },
        )
    }
}
```

导航需要测试，包括返回栈。
