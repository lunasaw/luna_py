# 集合 底层也是字典
a = {1, 2, 3, "chen"}
print(a)

# 复制
b = set(a)

# 增加
b.add("yue")

# 　删除
b.remove(2)
print(b)

# 数学操作
# 并集 union
print(a | b)
print(a.union(b))

# 交集 intersection
print(a & b)
print(a.intersection(b))

# 差集 -
print(a - b)

# zip 迭代运行
names = {"陈章月", "李诗琪"}
ages = {"20", "18"}

for name, age in zip(names, ages):
	print("{0}-{1}".format(name, age))
# 推导式
# 　列表推导式
y = [x for x in range(0, 10)]
print(y)

y = []
for x in range(1, 60):
	if x % 5 == 0:
		y.append(x * 2)
	else:
		print(str(x) + "-", end="")
print(y)

cells = [(row, col) for row in range(1, 10) for col in range(1, 10)]
print(cells)

# 字典推导式
my_text = "lishiqi,i love you"
char_count = {c: my_text.count(c) for c in my_text}
print(char_count)

# 集合推导式
b = {x for x in range(1, 100) if x % 9 == 0}
print(b)

# 生成器推导式 生成元组
gnt = (x for x in range(1, 100) if x % 7 == 0)
# for x in gnt:
# 	print(str(x)+" ", end="")
#
# print(tuple(gnt))
# 只能使用一次 迭代器 使用后指针失效
c = tuple(gnt)
print(c)
print(tuple(gnt))

# 同心圆
import turtle

my_colors = ("red", "green", "yellow", "black")
t = turtle.Pen()
t.write(4)
t.speed(1)
for i in range(1, 100):
	t.penup()
	t.goto(0, -i * 10)
	t.pendown()
	t.color(my_colors[i % len(my_colors)])
	t.circle(15 + i * 10)
turtle.done()
