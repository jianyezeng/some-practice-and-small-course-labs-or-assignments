# #第一个while循环
# number=1
# while number<=5:
# 	print(number)
# 	number+=1

# #中断while循环
# prompt="Tell me something, and I will repeat it back to you: "
# prompt+="\nEnter 'quit' to end the program."
# message=''
# while message != 'quit':
# 	message =input(prompt)
# 	print(message)

# prompt="Tell me something, and I will repeat it back to you: "
# prompt+="\nEnter 'quit' to end the program."
# message=''
# while message != 'quit':
# 	message= input(prompt)
# 	if message !='quit':
# 		print(message)

# #标志
# prompt="Tell me something, and I will repeat it back to you: "
# prompt+="\nEnter 'quit' to end the program."

# active=True
# while active:
# 	message =input(prompt)

# 	if message =='quit':
# 		active=False
# 	else:
# 		print(message)


# #使用break退出循环
# prompt="Tell me something, and I will repeat it back to you: "
# prompt+="\nEnter 'quit' to end the program."

# while True:
# 	message=input(prompt)

# 	if message == 'quit':
# 		break
# 	else:
# 		print(message)

#在循环中使用continue
current_number=0
while current_number<10:
	current_number+=1
	if current_number%2==0:
		continue
	else:
		print(current_number)


#每一个while循环都必须有停止运行的途径#