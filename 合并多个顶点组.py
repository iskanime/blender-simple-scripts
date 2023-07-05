import bpy

# 手动将所有需要合并的顶点组名称添加到列表中
# 例如：vgroup_list = ["vgroup_A_name", "vgroup_B_name", "vgroup_C_name"]
# 合并后的顶点组名称为：第一个顶点组名称+

# 需要合并的顶点组名称列表
vgroup_list = [""]

# 获得活动对象
ob = bpy.context.active_object

# 新建空的顶点组，用于储存合并的结果,使用第一个顶点组的名称
vgroup = ob.vertex_groups.new(name = vgroup_list[0] + "+")

# 循环每一个顶点组名称
for vgroup_name in vgroup_list:
    # 检查指定的顶点组名称是否存在
    if vgroup_name in ob.vertex_groups:
        # 循环每一个顶点
        for id, vert in enumerate(ob.data.vertices):
            # 获得当前顶点所属的所有顶点组的编号
            available_groups = [v_group_elem.group for v_group_elem in vert.groups]
            A = 0
            # 如果当前顶点属于顶点组 vgroup_A_name
            if ob.vertex_groups[vgroup_name].index in available_groups:
                A = ob.vertex_groups[vgroup_name].weight(id)

            # 如果权重A+B大于0，才把该顶点和合并权重加入新的顶点组。
            if A > 0:
                vgroup.add([id], A ,'REPLACE')



