message='Please tell me your age: '
message+="\n'quit' to end questions."
active=True
while active:
	age=input(message)

	if age =="quit":
		active=False
	else:
		age=int(age)
		if age<3:
			print("It's free.")
		elif age>=3 and age<=12:
			print("$10,please.")
		else:
			print("$15,please.")
