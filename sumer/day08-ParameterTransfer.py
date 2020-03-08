# python中都是引用传递  不是值传递 可变对象
b = [10, 20]


def f2(m):
	print("m:", id(m))
	# b和m是同一个对象
	m.append(30)


# 由于 m是可变对象，不创建对象拷贝，直接修改这个对象


f2(b)  # b的地址给m
print("b:", id(b))
print(b)

# 传递参数是不可变对象（例如：int、float、字符串、元组、布尔值），实际传递的还是
# 对 象的引用。在”赋值操作”时，由于不可变对象无法修改，系统会新创建一个对象。
a = 100


def f1(n):
	print("n:", id(n))
	# 传递进来的是a 对象的地址
	n = n + 200
	# 由于 a是不可变对象，因此创建新的对象n
	print("n:", id(n))
	# n已经变成了新的对象
	print(n)


f1(a)
print("a:", id(a))
print(a)
