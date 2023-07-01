import bpy

# 进入姿态模式后运行脚本，可以选择所有带有骨骼约束的骨骼
# 通常是为了选择所有带有物理约束的骨骼，方便关闭约束，从而停止物理模拟

# 获取当前活动的骨架对象
armature_obj = bpy.context.active_object

# 获取当前活动的3D视图区域，用于临时覆盖
area = [area for area in bpy.context.screen.areas if area.type == "VIEW_3D"][0]

with bpy.context.temp_override(area=area):
    # 全选骨骼
    bpy.ops.pose.select_all(action='SELECT')


# 获取当前显示的骨骼列表
visible_bones = [bone for bone in armature_obj.pose.bones if bone.bone.select]

# 清除选择
bpy.ops.pose.select_all(action='DESELECT')

# 遍历显示的骨骼
for bone in visible_bones:
    # 检查骨骼是否具有约束
    if len(bone.constraints) > 0:
        # 选择具有骨骼约束的骨骼
        bone.bone.select = True
