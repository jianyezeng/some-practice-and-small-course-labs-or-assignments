magicians=['alice','jone','july']
for a in magicians:     #for循环
	print(a)            #可以给依次与列表中每个值相关联的临时变量指定任意名称，然而，一般选择描述单个列表元素的有意义名称

magicians=['alice','jone','july']
for a in magicians:     #在for循环中执行更多操作，需注意函数调用是否缩进
	print(a+",that was a great trick!")
	print(f"I can't wait to see your next trick,{a.title()}.\n")
	print("hello")
print("hello")

#缩进常见错误
#1.忘记缩进
#2.忘记缩进额外的代码行
#3.不必要的缩进
#4.循环后不必要的缩进
#5.遗漏了冒号

#练习4-1
foods=['pza1','pza2','pza3']
for food in foods:
	print(food)
for food in foods:
	print(f"I like pepperoni {food}.")
print("I really love pizza!")

#练习4-2
animals=['dog','cat','bird']
for animal in animals:
	print(animal)
	print(f"A {animal} would make a great pet.")
print("Any of these animals would make a great pet!")