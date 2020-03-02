import os

'''
os.system("ping baidu.com")
#os.system("regedit")

#直接调用可执行程序
#os.startfile(r"C:\Program Files\Mozilla Firefox\firefox.exe")
'''
# 得到操作系统信息
print(os.name)  # win->nt linux 和 unix-> posix
print(os.sep)  # win->\   linux 和 unix->/
print(repr(os.linesep))  # win->\r\n linux-> \n\

# 获取文件信息
# print(os.stat("a.txt"))

# 获取当前工作目录
print(os.getcwd())

# 更改工作空间
os.chdir("D:")

# 创建目录
os.mkdir("书籍")

# 删除目录 相对路径是相对于当前工作空间下
os.rmdir("书籍")

# 创建多级目录
os.makedirs("电影/港台/周星驰")

# 删除多级目录 只能删除空的
os.removedirs("电影/港台/周星驰")

# os.makedirs("../音乐/港台/刘德华")
# 删除指定文件
# os.remove("a.txt")

# 重命名文件
# os.rename("a.txt","zychen.txt")

# 返回文件索引下的名称
# dirs=os.listdir("movie")
# print(dirs)
