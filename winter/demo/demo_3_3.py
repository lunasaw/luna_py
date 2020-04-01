account = 0
while account < 3:
	temp = input("不妨猜测一下程序现在所想的数字呢?")
	guess = int(temp)
	if guess == 9:
		print("你就是一个程序")
		print("猜中了也没奖励噢")
		break
	else:
		print("还没猜中噢!")
		if guess < 8:
			print("小啦")
		else:
			print("大啦")
	account += 1
print("游戏结束")
