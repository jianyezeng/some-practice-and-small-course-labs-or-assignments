#在这种情况下，出现了无限循环，因此需要将获得用户输入信息的过程放在while循环中
prompt="Tell me something, and I will repeat it back to you: "
prompt+="\nEnter 'quit' to end the program."
message=input(prompt)
while message != 'quit':
	print(message)