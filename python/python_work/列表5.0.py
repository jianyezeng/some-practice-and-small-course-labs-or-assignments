players=['charles','maetina','machael','florence','eli']
print(players[0:3])                      #创建一个切片
print(players[1:5])
print(players[0:5])

print(players[:2])                       #未指定第一个索引，python将自动从列表开头开始

print(players[2:])                       #要使切片终止于列表结尾，可省略终止索引

print(players[-3:])                      #可使用负数索引

players=['charles','maetina','machael','florence','eli']             #遍历列表的部分元素
print("Here are the first three players on our team:")
for player in players[0:3]:
	print(player.title())

#复制列表
my_foods=['fish','pizza','egg','bread','milk']
friend_foods=my_foods[:]
print(my_foods)
print(friend_foods)
another_foods=friend_foods[0:2]
print(another_foods)
my_foods.append("meat")
friend_foods.append("tea")
print(my_foods)
print(friend_foods)

#这行不通
my_foods=['fish','pizza','egg','bread','milk']
friend_foods=my_foods
my_foods.append("meat")
friend_foods.append("tea")
print(my_foods)
print(friend_foods)

#练习4-10
players=['charles','maetina','machael','florence','eli']
print("The first three items in the list are:")
print(players[:3])
print(players[1:4])
print(players[2:])

#练习4-11
foods=['pza1','pza2','pza3']
otfoods=foods[:]
foods.append('pza4')
otfoods.append("pza5")
print("My favorite pizzas are:")
for food in foods:
	print(food)
print("My friend's favorite pizzas are:")
for otfood in otfoods:
	print(otfood)