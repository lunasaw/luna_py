# -*- coding:utf-8 -*-
# @Time: 2020/3/18 0:08
# @Author: luna
# @Email: 15696756582@163.com
# @File: demo_3_17_csv.py

# csv文件操作
import csv

with open(r"3_18.csv", "r") as f:
	a_csv = csv.reader(f)  # 存在指针   调用后指向末尾
	row = list(a_csv)
	print(row[1])
# for row in a_csv:
# 	print(row)

with open(r"3_18_2.csv", "a") as w:
	b_csv = csv.writer(w)
	b_csv.writerow(["ID", "姓名", "电话"])
	b_csv.writerow(["1", "陈章月", "15696756582"])
	b_csv.writerow(["2", "Luna", "15696756582"])

	c = [["1002", "艾希", "10002"], ["1003", "蛮王", "10023"], []]
	b_csv.writerows(c)
