import bpy

# 参考 https://b3d.interplanety.org/en/context-overriding-in-blender-3-2-and-later/
# Blender 区域包括
# General：VIEW_3D（3D视图）,IMAGE_EDITOR（图像编辑器）,NODE_EDITOR（节点编辑器）,SEQUENCE_EDITOR（视频序列编辑器）,CLIP_EDITOR（影片剪辑编辑器）
# Animation：DOPESHEET_EDITOR（动画摄影表）,GRAPH_EDITOR（曲线编辑器）,NLA_EDITOR（非线性动画）
# Scripting：TEXT_EDITOR（文本编辑器）,CONSOLE（控制台）,INFO（信息）,TOPBAR,STATUSBAR
# Data：OUTLINER（大纲视图）,PROPERTIES（属性）,FILE_BROWSER（文件浏览器）,SPREADSHEET（电子表格）,PREFERENCES（偏好设置）
# 具体含义参考 https://docs.blender.org/api/3.6/bpy_types_enum_items/space_type_items.html#rna-enum-space-type-items

area = [area for area in bpy.context.screen.areas if area.type == "VIEW_3D"][0]
with bpy.context.temp_override(area=area):
    bpy.ops.wm.tool_set_by_id(name='builtin.select_circle')