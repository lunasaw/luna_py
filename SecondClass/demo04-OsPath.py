import os.path

# from os import path

# 判断绝对路径
print(os.path.isabs("d:/a.txt"))

# 判断是不是目录
print(os.path.isdir("d:/a.txt"))

# 判断是不是文件
print(os.path.isfile("d:/a.txt"))

# 文件是否存在
print(os.path.exists("d:/a.txt"))

# 获得文件基本信息->文件大小
print(os.path.getsize("mygirl.gif"))
# 获取绝对路径
print(os.path.abspath("mygirl.gif"))
# 获取所在目录
print(os.path.dirname("mygirl.gif"))

# 获取创建时间  时间是1970年1月1日做为0刻度 一毫秒一刻度
print(os.path.getctime("mygirl.gif"))
# 获取最后访问时间
print(os.path.getatime("mygirl.gif"))
# 获取最后修改时间
print(os.path.getmtime("mygirl.gif"))

# 路径
path = os.path.abspath("mygirl.gif")
print(os.path.split(path))  # 返回一个元祖  按路径切割
print(os.path.splitext(path))  # 返回一个元祖  按 点 切割

print(os.path.join("aa", "bb", "cc"))  # 路径连接

# 遍历子目录 子文件

path = os.getcwd()
list_files = os.walk(path)
for dirpath, dirname, filenames in list_files:
    for dir in dirname:
        print(dir)
    for files in filenames:
        print(files)
