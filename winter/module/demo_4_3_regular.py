# -*- coding:utf-8 -*-
# @Time: 2020/4/3 22:20
# @Author: luna
# @Email: 15696756582@163.com
# @File: demo_4_3_regular.py

# 第三方模块

import requests
import PIL  # pillow已不维护 改为PIL

# reponse = requests.get("http://iszychen.club")
# print(reponse.text)

# 正则 re 模块
import re

msg = "lunew832a4uo123weu923ji1sa92u39123weu321rweia"  # <== 待过滤的字符串
pattern = re.compile("l")  # 正则
find = pattern.match(msg)  # match从头开始匹配 返回第一个Match对象 不成功返回None
print(find)

# search
search = re.search("u", msg)  # search 查找 头没有则继续往下匹配 返回匹配的位置和内容
print(search)
print(search.span())
print(search.group())  # 拿到匹配的值
print(search.groups())

#  正则符号
reSearch = re.search('[0-9][a-z]', msg)
print(reSearch.group())  # 找到第一个符合表达式的值

#  正则符号
reSearch = re.search('[a-z][0-9][a-z]', msg)
if reSearch == None:
	print("未找到")
else:
	print(reSearch.group())  # 找到第一个符合表达式的值 search只匹配第一个符合条件的值

findall = re.findall('[a-z][a-z]', msg)  # finall 找到所有符合的值放入列表返回
print(findall)

findall = re.findall('[a-z][0-9]+[a-z]', msg)  # + 表示>=1 个数字出现在字母中间都是符合的
print(findall)

qq = re.match('^[1-9][0-9]{9}$', '1173282254')  # qq号码的验证 5~11 位 正则验证的都是字符串 开头不能是0
print(qq)
'''
[0-9]{4}=> 0-9 任意四位
^ 表示从头匹配
$ 表示结尾
{m,} 用于验证m次或者多次 >=m 次
{m,n}  m<= x <=n 字数限制
'''
qq = re.match('^[1-9][0-9]{1,9}$', '1173282254')  # {m,n}  m<= x <=n 字数限制
print(qq)

qq = re.match('^[1-9][0-9]{9,}$', '11732822542131231231')  # {m,} 用于验证m次或者多次 >=m 次
print(qq)
