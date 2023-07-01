import bpy

# 起因是在使用Simplicage插件的时候，发现删除模拟体的时候，自定义属性没有删除
# 于是写了这个脚本，用于删除物体的自定义属性（Api Defined）

# 需要删除的自定义属性
property = "Simplicage_CageSettings"

# 选择中的物体
obj = bpy.context.selected_objects[0]

del obj[property]

