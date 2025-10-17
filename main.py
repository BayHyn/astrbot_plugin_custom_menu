import os
import re
import json
import aiohttp
from typing import List
from astrbot.api import logger
from astrbot.api.message_components import *
from astrbot.api.star import Context, Star, register
from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult

@register("astrbot_plugin_custom_menu", "Futureppo", "自定义图片菜单。", "v2.0.2")
class custommenu(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    @filter.command("菜单", alias=['帮助', '功能', '你怎么用'])  # 可以自行添加指令
    async def custommenu(self, event: AstrMessageEvent):
        base_dir = os.path.dirname(os.path.abspath(__file__))


        repo_root = os.path.abspath(os.path.join(base_dir, os.pardir, os.pardir, os.pardir))
        data_dir = os.path.join(repo_root, "data")
        menu_dir = os.path.join(data_dir, "menu")

        # 检查并创建菜单文件夹
        if not os.path.exists(menu_dir) or not os.path.isdir(menu_dir):
            logger.debug(f"menu文件夹不存在或不是一个有效的目录，尝试创建: {menu_dir}")
            try:
                os.makedirs(menu_dir, exist_ok=True)  
                logger.debug(f"menu文件夹已成功创建: {menu_dir}")
            except Exception as e:
                logger.error(f"无法创建menu文件夹: {menu_dir}, 错误信息: {e}")
                return

        # 获取菜单文件夹中的所有图片文件
        image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp'] 
        image_paths = [
            os.path.join(menu_dir, f)
            for f in os.listdir(menu_dir)
            if os.path.isfile(os.path.join(menu_dir, f)) and os.path.splitext(f)[1].lower() in image_extensions
        ]

        if not image_paths:
            logger.warning(f"menu文件夹中没有找到任何图片: {menu_dir}")
            return

        # 每次发送的最大图片数量
        batch_size = 100

        # 分批处理图片
        for i in range(0, len(image_paths), batch_size):
            batch_paths = image_paths[i:i + batch_size]
            nodes_list = []

            for idx, path in enumerate(batch_paths):
                if not os.path.exists(path):
                    logger.info(f"图片不存在: {path}")
                    continue

                # 合并转发外显内容
                nickname = f"菜单" 

                # 加载图片
                image = Image.fromFileSystem(path)
                logger.debug(f"成功加载图片: {path}")

                node = Node(
                    name=nickname,
                    content=[image]
                )
                nodes_list.append(node)

            # 发送当前批次的图片
            if nodes_list:
                nodes = Nodes(nodes=nodes_list)
                yield event.chain_result([nodes])
            else:
                yield event.plain_result("发送失败，请检查data/menu文件夹中的图片。")