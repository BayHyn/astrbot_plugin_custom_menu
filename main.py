from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
from astrbot.api.message_components import *
from astrbot.api.event import filter, AstrMessageEvent
import os


@register("astrbot_plugin_custom_menu", "Futureppo", "自定义图片菜单", "1.0.0")
class custommenu(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    @filter.command("菜单", alias=['帮助', '功能', '你有什么功能', '你怎么用'])  # 可以自行添加指令
    async def custommenu(self, event: AstrMessageEvent):
        base_dir = os.path.dirname(os.path.abspath(__file__))

        # 菜单文件夹路径
        menu_dir = os.path.join(base_dir, "menu")

        if not os.path.exists(menu_dir) or not os.path.isdir(menu_dir):
            logger.error(f"菜单文件夹不存在或不是一个有效的目录: {menu_dir}")
            return

        # 获取菜单文件夹中的所有图片文件
        image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']  # 支持的图片扩展名
        image_paths = [
            os.path.join(menu_dir, f)
            for f in os.listdir(menu_dir)
            if os.path.isfile(os.path.join(menu_dir, f)) and os.path.splitext(f)[1].lower() in image_extensions
        ]

        if not image_paths:
            logger.error(f"菜单文件夹中没有找到任何支持的图片文件: {menu_dir}")
            return

        images = []
        for path in image_paths:
            if os.path.exists(path):
                logger.debug(f"成功加载图片: {path}")
                images.append(Image.fromFileSystem(path))
            else:
                logger.debug(f"图片文件不存在: {path}")

        node = Node(
            name="菜单",
            content=images
        )

        yield event.chain_result([node])

    async def terminate(self):
        '''可选择实现 terminate 函数，当插件被卸载/停用时会调用。'''