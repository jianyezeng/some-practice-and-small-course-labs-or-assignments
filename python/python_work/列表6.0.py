#元组即不可改变的列表
dimensions=(0.1,1)                     #定义元组时，元组是由逗号标识的，但若定义只含一个元素的元组，括号不可省略
print(dimensions) 
print(dimensions[0])

zim=2,3
print(zim[0])

#若需修改元组变量，可重新定义整个元组
dimensions=40,50
for dimension in dimensions:
	print(dimension)
dimensions=0,0
for dimension in dimensions:
	print(dimension)

#练习4-13
foods=('meat','duck','fish','egg','milk')
for food in foods:
	print(food)
foods=("meat",'duck0','fish','tea','cola')
for food in foods:
	print(food)