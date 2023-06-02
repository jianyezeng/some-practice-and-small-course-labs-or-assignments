cars=['audi','bmw','subaru','toyota']
for car in cars:
	if car =='audi':
		print(car.upper())
	else:
		print(car.lower())

#在python中检查是否相等时区分大小写
car='Aoi'
if car=='aoi':
	print("yes")
else:
	print("no")
#如果大小写无关紧要，只想检查变量的值，可将变量的值转化为小写再比较
car='Aoi'
if car.lower()=='aoi':
	print("yes")

#判读是否不等使用！=
zim='aoi';
if zim!='jic':
	print("yes")

#数值比较较为简单
if 3==2:
	print("ok")
else:
	print("no")

a=2
if a!=1:
	print(6)

a=5
if a<0 and a>5:          #使用and可检查多个条件
	print("true")
if a<0 or a>=5:          #使用or检查多个条件
	print(2)

#检查特定值是否包含在列表中
players=['machael','jone','july','sam','tom','jerry']
if 'tom' in players:
	print("tom is in this list.")
if 'lbt' in players:
	print("lbt is in this list.")
else:
	print("lbt is't in this list.")
if 'mark' not in players:
	print("he is not there.")

#练习5—1
car='subaru'
print("Is car=='subaru'? I predict true.")
print(car=='subaru')
print(car!='subaru')