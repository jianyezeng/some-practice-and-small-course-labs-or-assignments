# from random import randint

# print(randint(1,6))

# from random import choice

# players = ['Jack','Ben','July','Jone','Mark']

# num = len(players)
# print(num)
#练习9-13
# from random import randint

# class Dies:

# 	def __init__(self,sides = 6):
# 		self.sides = sides
# 	def roll_die(self):
# 		print(randint(1,self.sides))

# die_0 = Dies(6)
# i=0
# while i != 10:
# 	die_0.roll_die()
# 	i += 1

# die_1 = Dies(10)
# i=0
# while i != 10:
# 	die_1.roll_die()
# 	i += 1

# die_2 = Dies(20)
# i=0
# while i != 10:
# 	die_2.roll_die()
# 	i += 1

#练习9-14
# from random import choice

# nums = [1,2,3,4,5,6,7,8,9,0,'a','b','c','d']
# num = []

# i = 0
# while i != 4:
# 	zim = choice(nums)
# 	nums.remove(zim)
# 	num.append(zim)
# 	i += 1
# print(f"{num[0]}{num[1]}{num[2]}{num[3]}")

#练习9-15
from random import choice
def get_winning_ticket(possibilities):
 	"""摇出中奖组合。"""
 	winning_ticket = []
 	# 中奖组合中不能包含重复的数字或字母，因此使用了 while 循环。
 	while len(winning_ticket) < 4:

 		pulled_item = choice(possibilities)
 		# 仅当摇出的数字或字母不在组合中时，才将其添加到组合中。 
 		if pulled_item not in winning_ticket:
 			winning_ticket.append(pulled_item)
 	return winning_ticket

def check_ticket(played_ticket, winning_ticket):
 	# 检查彩票的每个数字或字母，只要有一个不在中奖组合中，就返回 False。
 	for element in played_ticket:
 		if element not in winning_ticket:
 			return False

 		# 如果代码执行到这里，就说明中奖了！
 	return True


def make_random_ticket(possibilities):
 	"""随机地生成彩票。"""
 	ticket = []
 	# 彩票不能包含重复的数字或字母，因此使用了 while 循环。
 	while len(ticket) < 4:
 		pulled_item = choice(possibilities)
 		# 仅当随机生成的数字或字母不在彩票中时，才将其添加到彩票中。
 		if pulled_item not in ticket:
 			ticket.append(pulled_item)

 	return ticket

possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
winning_ticket = get_winning_ticket(possibilities)
plays = 0
won = False
# 为避免程序执行时间太长，设置最多随机生成多少张彩票。

max_tries = 1_000_000
while not won:
 	new_ticket = make_random_ticket(possibilities)
 	won = check_ticket(new_ticket, winning_ticket)
 	plays += 1
 	if plays >= max_tries:
 		break
if won:
 	print("We have a winning ticket!")
 	print(f"Your ticket: {new_ticket}")
 	print(f"Winning ticket: {winning_ticket}")
 	print(f"It only took {plays} tries to win!")
else:
 	print(f"Tried {plays} times, without pulling a winner. :(")
 	print(f"Your ticket: {new_ticket}")
 	print(f"Winning ticket: {winning_ticket}")