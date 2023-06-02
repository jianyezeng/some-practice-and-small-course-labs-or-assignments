#最简单的if语句
#if conditional_test:
#	do something

age=99
#if-elif-else结构，测试通过后将跳过余下的测试
if age<4:
	print("$0")
elif age<18:
	print("$9")
elif age ==18:
	print("$13.5")
else:
	print("$18")
#在某些情况下，可省略else代码块
if age<4:
	print("$0")
elif age<18:
	print("$9")
elif age ==18:
	print("$13.5")
elif age>18 and age<100:
	print("$18")

#练习5-3
alin_color='green'
if alin_color=='green':
	print("获得5分！")
alin_color='red'
if alin_color=='green':
	print("获得5分！")

#练习5-4
alin_color="green"
if alin_color=='green':
	print("获得5分！")
else:
	print("获得10分！")

alin_color="red"
if alin_color=='green':
	print("获得5分！")
else:
	print("获得10分！")

#练习5-5
alin_color="green"
if alin_color=='green':
	print("获得5分！")
elif alin_color=='yellow':
	print("获得10分！")
else:
	print("获得15分！")

alin_color="yellow"
if alin_color=='green':
	print("获得5分！")
elif alin_color=='yellow':
	print("获得10分！")
else:
	print("获得15分！")

alin_color="red"
if alin_color=='green':
	print("获得5分！")
elif alin_color=='yellow':
	print("获得10分！")
else:
	print("获得15分！")

#练习5-6
age=5
if age <2:
	print("He is a baby!")
elif age>=2 and age<4:
	print("He is a boy!")
elif age>=4 and age<13:
	print("He is a child!")
elif age>=13 and age<20:
	print("He is a teenger!")
elif age>=20 and age<65:
	print("He is a man!")
else:
	print("He is an older!")

#练习5-7
fruits=['apple','orange','melon']
if "bananas" in fruits:
	print("You really like banbanas!")
if "apples" in fruits:
	print("You really like apples!")
if "melon" in fruits:
	print("You really like melon!")
if "bears" in fruits:
	print("You really like bears!")
if "orange" in fruits:
	print("You really like orange!")