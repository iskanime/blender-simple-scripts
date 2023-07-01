import os,sys,subprocess

# 参考来源 https://www.bilibili.com/read/cv22355478/
# 为Blender安装需要的库
# 在blender的脚本编辑器中运行此脚本即可

# 修改需要安装的库名
package_name = 'win10toast'

# 获得当前blender环境下的python路径
python_exe = os.path.join(sys.prefix, 'bin', 'python.exe')

# 安装清华源下的库
subprocess.call([python_exe, "-m", "pip", "install", package_name,"-i","https://pypi.tuna.tsinghua.edu.cn/simple"]) 