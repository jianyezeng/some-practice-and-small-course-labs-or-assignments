for value in range(1,5):      #编程语言中常见的差一行为，在指定的第二个值停止，因此输出不包含该值
	print(value)

numbers=list(range(1,6))      #创建数字列表，list()函数可将range()的结果直接转换为列表
print(numbers)

numbers=list(range(2,11,2))   #使用range()函数时，可确定步长
print(numbers)

zims=[]                       #将前10个整数的平方加入一个列表中
for zim in range(1,11):
	zim=zim**2
	zims.append(zim)
print(zims)

digits=[1,2,3,4,5,6,7,8,9,0]  #对数字列表进行简单的统计计算
print(min(digits))
print(max(digits))
print(sum(digits))

squares=[value**2 for value in range(1,11)] #列表解析
print(squares)

#练习4-3
for value in range(1,21):
	print(value)
#练习4-4
numbers=[]
for value in range(1,1_000_001):
	numbers.append(value)
print(numbers)

numbers=list(range(1,1000001))
print(numbers)
#练习4-5
numbers=[value for value in range(1,1_000_001)]
print(numbers)
print(sum(numbers))
#练习4-6
numbers=[value for value in range(1,21,2)]
for value in numbers:
	print(value)
#练习4-7
numbers=[value for value in range(3,31,3)]
for value in numbers:
	print(value)
#练习4-8
numbers=[value**3 for value in range(1,11)]
for value in numbers:
	print(value)
#练习4-9
numbers=[value**3 for value in range(1,11)]
print(numbers)
