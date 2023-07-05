bl_info = {
    "name": "Clear System Console",
    "author": "Robert Guetzkow",
    "version": (1, 0, 0),
    "blender": (2, 81, 0),
    "location": "Text Editor Header",
    "description": "Clear the system console.",
    "wiki_url": "",
    "category": "Text Editor"}

import bpy
import os

# 插件会在文本编辑器的头部添加一个按钮，点击后清空控制台
# 插件安装方法和其他插件一样，在用户偏好设置中点击安装插件，选择本文件即可。

class CLEARCONSOLE_OT_clear(bpy.types.Operator):
    bl_idname = "clearconsole.clear"
    bl_label = "清空控制台"
    bl_description = "This operator clears the system console."
    bl_options = {"REGISTER"}

    def execute(self, context):
        if os.name == "nt":
            os.system("cls") 
        else:
            os.system("clear") 
        return {"FINISHED"}


def draw(self, context):
    self.layout.operator(CLEARCONSOLE_OT_clear.bl_idname)


classes = (CLEARCONSOLE_OT_clear,)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        
    bpy.types.TEXT_HT_header.append(draw)


def unregister():
    bpy.types.TEXT_HT_header.remove(draw)
    
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()