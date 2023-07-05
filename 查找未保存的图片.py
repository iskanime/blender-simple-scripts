import bpy

# 运行后，在控制台显示未保存的图片

for image in bpy.data.images:
    if image.is_dirty:
        print(image.name)