</div>

<div align="center">

![:name](https://count.getloli.com/@astrbot_plugin_custom_menu?name=astrbot_plugin_custom_menu&theme=minecraft&padding=7&offset=0&align=top&scale=1&pixelated=1&darkmode=auto)

</div>

# astrbot_plugin_custom_menu

[仅QQ]这是一个为 **AstrBot** 提供的自定义菜单图片功能的插件。用户可以通过在指定文件夹中放置图片来自定义菜单内容，支持多种图片格式。

## 功能

- 支持图片格式：`jpg, jpeg, png, gif, bmp`
- 自动检测 `data/menu` 文件夹中的图片
- 提供多个指令别名（如 `菜单`, `帮助`, `功能`, `你怎么用`）
- 动态加载图片并以合并转发形式发送
- 自动创建 `data/menu` 文件夹（如果不存在）

## 更新日志

- **1.0.0**：自定义菜单图片功能，但图片在一条消息内不便于阅读。
- **2.0.0**：每一张图片一条消息，并在合并转发内防止刷屏。

## 使用方法

1. 首次使用会在项目根目录 `data` 下创建一个名为 `menu` 的文件夹。
2. 将需要显示的图片放入项目的 `data/menu` 文件夹中（支持 `jpg, jpeg, png, gif, bmp` 格式）。
3. 在 QQ 中发送指令（如 `菜单`、`帮助`、`功能` 或 `你怎么用`），插件会自动加载并发送图片。

## 注意事项

- **图片数量限制**：测试时最高可以发送151张图片，请根据实际情况调整图片数量。
- **更新前备份**：更新插件前，请备份 `data/menu` 文件夹中的图片，以免数据丢失。
