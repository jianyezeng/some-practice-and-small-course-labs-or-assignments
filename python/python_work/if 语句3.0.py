tips=['mushrooms','green peppers','extra cheese']
for tip in tips:
	if tip=='green peppers':
		print("Sorry,we are out of green peppers right now.")
	else:
		print(f"Adding {tip}.")
print("\nFinished making your pizza!")

#确定列表不是空的
if tips:
	print(1)
else:
	print(2)

fitips=['mushrooms','green peppers','extra cheese','pineapple']
setips=['mushrooms','french fries','extra cheese']
for setip in setips:
	if setip in fitips:
		print(f"Adding {setip}.")
	else:
		print(f"Sorry,we are out of {setip}.")
print("\nFinished making your pizza!")

#练习5-8
names=['admin','july','june','tim','sam']
for name in names:
	if name =='admin':
		print(f"Hello {name},would you like to see a status report?")
	else:
		print(f"Hello {name},thank you for logging in again.")

#练习5-9
if names:
	print("\0")
else:
	print("We need to find some users!")
names=[]
if names:
	print("\0")
else:
	print("We need to find some users!")

#练习5-10
current_users=['july','tim','steve','Jerry','amy']
names=[]
for current_user in current_users:
	names.append(current_user.lower())
new_users=['amy','steve','Tim','jone','mark']
for new_user in new_users:
	if new_user.lower() in names:
		print("需输入其他用户名")
	else:
		print("该用户名未被使用")

#练习5-11
numbers=list(range(1,10))
for number in numbers:
	if number==1:
		print("1st")
	elif number==2:
		print("2nd")
	else:
		print(f"{number}th")