# a=input("输入一个小于10的数字")
# if int(a)<10:
#     print(a)
b = []
if not b:
    print("false")
c = "false"
if c:
    print("c")
d = 10
if d:
    print("d")
# if 3<c and (c=20):
#     print("赋值符不能出现在条件表达式中")  不能出现赋值运算  py直接否定了这种写法

# 分支结构
num = input("输入一个数字：")
if int(num) < 10:
    print(num)
else:
    print("数字太大")

# 三元条件
num = input("请输入一个数字")
print(num if int(num) < 10 else "数字太大")

# 多分枝结构
score = int(input("请输入分数"))
grade = ''
if (score < 60): grade = "不及格"
if (60 <= score < 80): grade = "及格"
if (80 <= score < 90): grade = "良好"
if (90 <= score <= 100): grade = "优秀"
print("分数是{0},等级是{1}".format(score, grade))

score = int(input("请输入分数"))
grade = ''
if score < 60:
    grade = "不及格"
elif score < 80:
    grade = "及格"
elif score < 90:
    grade = "良好"
elif score <= 100:
    grade = "优秀"
print("分数是{0},等级是{1}".format(score, grade))

x = int(input("请输入 x坐标"))
y = int(input("请输入 y坐标"))
if (x == 0 and y == 0):
    print("原点")
elif (x == 0):
    print("y 轴")
elif (y == 0):
    print("x 轴")
elif (x > 0 and y > 0):
    print("第一象限")
elif (x < 0 and y > 0):
    print("第二象限")
elif (x < 0 and y < 0):
    print("第三象限")
else:
    print("第四象限")
