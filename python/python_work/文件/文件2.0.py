filename = 'programming.txt'

#读取模式：r    写入模式：w
#附加模式：a    读写模式：r+

with open(filename,'w') as file_object:
	file_object.write('I love programming.\n')
	file_object.write('I love python.\n')

with open(filename,'a') as file_object:
	file_object.write("I love C.")

#练习10-3 + 10-4
# while True:
# 	name = input("Please tell me your name. ")
# 	print(f"Hello {name.title()}!")
# 	with open('my_name_0.txt','a') as names:
# 		names.write(f"{name.title()} once visited there.\n")
# 	message = input("Do you want another person answer this question? (yes or no) ")
# 	if message == 'no':
# 		break

#练习10-5
active = True
while active:

	answer = input('Why do you like programming?  ')
	print('Thanks for your answer.')
	with open('questions.txt','a') as quest:
		quest.write(answer+'\n')

	message = input("Do you want another person answer this question? (yes or no)  ")

	if message == 'no':
		active = False