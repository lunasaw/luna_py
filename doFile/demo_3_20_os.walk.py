# -*- coding:utf-8 -*-
# @Time: 2020/3/21 0:32
# @Author: luna
# @Email: 15696756582@163.com
# @File: demo_3_20_os.walk.py

# 使用os.walk 遍历
import os

path = os.getcwd()
listFile = os.walk(path)
allFiles = []

for dirPath, dirNames, fileNames in listFile:
	# 遍历目录
	for dir in dirNames:
		allFiles.append(os.path.join(dirPath, dir))
		print(os.path.join(dirPath, dir))
	# 遍历文件
	for fileName in fileNames:
		allFiles.append(os.path.join(dirPath, fileName))
		print(os.path.join(dirPath, fileName))

print("========分隔符=========")
# 输出子目录和子文件
for file in allFiles:
	print(file)

# shutil 模块
import shutil
import zipfile

# shutil.copy("a.txt", "copy.txt")
# shutil.copytree("movie/hongkong", "香港")  # 香港目录不存在才能拷贝
# shutil.copytree("movie/hongkong/Andy Lau", "刘德华", ignore=shutil.ignore_patterns("*.txt", "*.html"))  # 指定不拷贝文件

# 压缩
# shutil.make_archive("刘德华", "zip", "香港/Andy Lau")  # 1.压缩完成的路径 2.压缩格式 3.压缩内容
# zip = zipfile.ZipFile("luna.zip", "w")  # 生成压缩包
# zip.write("a.txt")
# zip.write("pukeCopy.gif")
# zip.close()

# 解压缩
zip2 = zipfile.ZipFile("luna.zip", "r")
zip2.extractall("movie")
zip2.close()
