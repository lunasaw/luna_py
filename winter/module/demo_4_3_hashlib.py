# -*- coding:utf-8 -*-
# @Time: 2020/4/3 21:57
# @Author: luna
# @Email: 15696756582@163.com
# @File: demo_4_3_hashlib.py

# 加密算法
import hashlib

msg = "中午一起吃饭!"
md5 = hashlib.md5(msg.encode("utf-8"))  # 字符串转编码后传入
print(md5.hexdigest())

sha256 = hashlib.sha256(msg.encode("utf-8"))
print(sha256.hexdigest())

msg = "好呀!"
newsha256 = hashlib.sha256(msg.encode("utf-8"))
print(newsha256.hexdigest())
