# num = 0
# while num<=100:
#     print(num,end="\t")
#     # 循环内容
#     num += 1
#     # 改变条件

#while循环
'''
num = 0
sum_all = 0
sum_odd = 0
#所有数的累加和
sum_even = 0
#1-100 偶数的累加和 sum_odd = 0 #1-100 奇数的累加和
while num<=100:
    sum_all += num
    if num%2==0:
        sum_even += num
    else:
        sum_odd += num
    num+=1
 #迭代，改变条件表达式，使循环趋于结束
print("1-100 所有数的累加和",sum_all)
print("1-100 偶数的累加和",sum_even)
print("1-100 奇数的累加和",sum_odd)

#for 循环

for x in  (10,20,30):
    print(x*30)

for y in "abcdef":
    print(y,)

d={"name":"gaoqi","age":18,"job":"programmer"}
for x in d.keys():
    print(x)
for x in d.values():
    print(x)
for x in d.items():
#遍历字典所有的"键值对"
   print(x)

#range
sum_all = 0
#1-100 所有数的累加和
sum_even = 0
#1-100 偶数的累加和
sum_odd = 0
# 奇数的累加和
for num in range(101):
    sum_all += num
    if num%2==0:
        sum_even += num
    else:
        sum_odd += num
print("1-100累加总和{0},奇数和{1},偶数和{2}".format(sum_all,sum_odd,sum_even))


for m in range(1,10):
    for n in range(1,m+1):
        print("{0}*{1}={2}".format(m,n,(m*n)),end="\t")
    print()
'''

r1= dict(name="高小一",age=18,salary=30000,city="北京")
r2= dict(name="高小二",age=19,salary=20000,city="上海")
r3= dict(name="高小三",age=20,salary=10000,city="深圳")
tb = [r1,r2,r3]
for x in tb:
    if x.get("salary")>15000:
        print(x)