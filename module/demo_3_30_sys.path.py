# -*- coding:utf-8 -*-
# @Time: 2020/3/30 22:08
# @Author: luna
# @Email: 15696756582@163.com
# @File: demo_3_30_sys.path.py

# TODO 模块搜索路径 内置模块》当前目录》程序主目录》环境目录》标准链接库》第三方库》.pth文件》sys,path.append()临时目录

import sys

sys.path.append("D:")  # 临时增加
print(sys.path)
