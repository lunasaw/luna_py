# score = int(input("请输入一个在 0-100 之间的数字："))
# grade = ""
# if score>100 or score<0: score = int(input("输入错误！请重新输入一个在 0-100 之间的数字："))
# else:
#     if score>=90: grade = "A"
#     elif score>=80: grade = 'B'
#     elif score>=70: grade = 'C'
#     elif score>=60: grade = 'D'
#     else: grade = 'E'
# print("分数为{0},等级为{1}".format(score,grade))

score = int(input("请输入一个在 0-100 之间的数字："))
degree = "ABCDE"
num = 0
if score>100 or score<0:
    score = int(input("输入错误！请重新输入一个在 0-100 之间的数字："))
else: num = score//10
# 双斜杠表示除
if num<6:num=5
print("分数是{0},等级是{1}".format(score,degree[9-num]))
