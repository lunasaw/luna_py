#break语句可用于 while 和for 循环，用来结束整个循环。
# 当有嵌套循环时，break 语句只 能跳出最近一层的循环。
'''
while True:
    a = input("请输入一个字符（输入 Q或 q结束）")
    if a.upper()=='Q':
        print("循环结束，退出")
        break
    else:
        print()
'''
# continue 语句用于结束本次循环，继续下一次。
# 多个循环嵌套时，continue 也是应用于最 近的一层循环。

empNum = 0
salarySum= 0
salarys = []
while True:
    s = input("请输入员工的薪资（按 Q或q结束）")
    if s.upper()=='Q':
        print("录入完成，退出")
        break
    if float(s)<0:
        continue
    empNum +=1
    salarys.append(float(s))
    salarySum += float(s)
print("员工数{0}".format(empNum))
print("录入薪资：",salarys)
print("平均薪资{0}".format(salarySum/empNum))

# 循环里带的else
# while、for 循环可以附带一个 else 语句（可选）。
# 如果for、while 语句没有被break 语句 结束，则会执行else 子句，否则不执行