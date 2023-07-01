import bpy

# 将所有选中的布料保存为形态键，目的是为了保存布料初始状态
# 创建布料模拟后，将一段时间后的布料模拟的形态保存为形态键，然后将形态键的值设为1
# 这样回到第一帧依然可以保持布料模拟的状态，从这个状态开始模拟更加自然
# 一般是配合Bone Dynamics Pro快速创建头发或者衣服的布料模拟

# 获取当前选中的物体列表
selected_objects = bpy.context.selected_objects

# 遍历选中的物体
for obj in selected_objects:
    # 将物体设为活动物体
    bpy.context.view_layer.objects.active = obj
    
    # 检查物体是否具有布料修改器
    cloth_modifiers = [modifier for modifier in obj.modifiers if modifier.type == 'CLOTH']
    if cloth_modifiers:
        # 添加形态键
        for modifier in obj.modifiers:
            if modifier.type == 'CLOTH':
                bpy.ops.object.modifier_apply_as_shapekey(
                    keep_modifier=True,
                    modifier=modifier.name
                    )
                
        # 将形态键的值设为1
        shape_keys = obj.data.shape_keys
        last_key_block = shape_keys.key_blocks[-1]
        last_key_block.value = 1.0
    
    

