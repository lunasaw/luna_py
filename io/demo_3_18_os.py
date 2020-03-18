# -*- coding:utf-8 -*-
# @Time: 2020/3/18 22:52
# @Author: luna
# @Email: 15696756582@163.com
# @File: demo_3_18_os.py

# os 模块
import os

# 调用命令
# os.system("notepad.exe")
# os.system("ping luna.com")
# os.system("cmd")
# 直接调用程序
# os.startfile(r"D:\notebook\notepad++.exe")

'''获取文件和文件夹相关信息'''
print(os.name)  # win 返回nt  linux 返回posix
print(os.sep)  # 返回分隔符 win ->\ linux ->/
print(repr(os.linesep))  # repr返回一个对象的 string 格式。  win -> \r\n linux ->\n\
print(os.stat("demo_3_18_os.py"))  # 文件相关信息 大小 时间 权限
'''工作目录
os.mkdir("demo")
os.chdir("demo")  # 改变工作空间
os.mkdir("demo_os")
print(os.getcwd())  # 当前工作目录
'''
'''创建目录,创建多级目录,删除'''
os.mkdir("demo_os")
os.rmdir("demo_os")  # 相对路径 相对于当前工作目录
# os.makedirs("movie/hongkong/Stephen Chow")
# os.removedirs("movie/hongkong/Stephen Chow")  # 不是空的则不能删除
os.chdir("movie/hongkong/Stephen Chow")
# os.makedirs("../Andy Lau")
# os.rename("功夫.mp4", "Kung fu.mp4")
dirs = os.listdir("D:\\")  # 返回目录List
print(dirs)
