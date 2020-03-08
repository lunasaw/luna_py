names = ("高淇","高老二","高老三","高老四")
ages = (18,16,20,25)
jobs = ("老师","程序员","公务员")
for name,age,job in zip(names,ages,jobs):
    print("{0}--{1}--{2}".format(name,age,job))

for i in range(3):
    print("{0}--{1}--{2}".format(names[i],ages[i],jobs[i]))