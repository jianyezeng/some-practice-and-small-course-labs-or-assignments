#使用try-except代码块与else代码块

# print('Give me two numbers,and I will divide them. ')
# print("Enter 'q' to quit."

# while True:
# 	first_number = input("\nFirst number: ")
# 	if first_number == 'q':
# 		break
# 	second_number = input("Second number: ")
# 	if second_number == 'q':
# 		break
# 	try:
# 		answer = int(first_number)/int(second_number)
# 	except ZeroDivisionError:
# 		print("error")
# 	else:
# 		print(answer)

#open()函数常用三个参数：
#file ：文件路径
#mode ：使用文件方式
#encoding ：返回数据的编码方式

filename = 'alice.txt'

# try:
# 	with open(filename,encoding = 'utf-8') as f:
# 		contents = f.read()
# except FileNotFoundError:
# 	pass

# title = 'Alice in wonderland in'
# words = title.split()

# for i in range(len(words)):
# 	j = i+1
# 	if j >= len(words):
# 		break
# 	while True:

# 		if j<len(words):
# 			if words[i] == words[j]:
# 				del words[i]
# 			else:
# 				j += 1
# 		else:
# 			break

# print(words)