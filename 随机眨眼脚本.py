import bpy
import random

# 眨眼形态键默认为'まばたき'
# 眨眼帧数默认为30帧，如果是60帧的话，暂时只能自己将关键帧缩放2倍，后面会改进
# 目前只有单纯的眨眼，遇到其他表情干扰的情况还要自己修改

# 设定起始关键帧
start = 1
# 设定结束关键帧
end = 2000


# 获得当前选择的物体
obj = bpy.context.selected_objects[0]

# 获取形态键 "まばたき"
shape_key = obj.data.shape_keys.key_blocks['まばたき']

# 定义眨眼动作
def blink(shape_key, frame):
    shape_key.value = 0
    shape_key.keyframe_insert('value', frame=frame)
    shape_key.value = 1
    shape_key.keyframe_insert('value', frame=frame + 4)
    shape_key.value = 1
    shape_key.keyframe_insert('value', frame=frame + 6) 
    shape_key.value = 0
    shape_key.keyframe_insert('value', frame=frame + 9)

# 在每个间隔插入眨眼动作
frame = start
while frame < end:
    interval = random.randint(40, 100)
    choices = [1, 2]
    weights = [5, 1]
    rounds = random.choices(choices, weights=weights, k=1)[0]
    for i in range(rounds):
        blink(shape_key, frame + i * 9)
    frame += interval
