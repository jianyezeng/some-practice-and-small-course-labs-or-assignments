#在列表之间移动元素
unconfirmed_users = ['alice','brian','candance']
confirmed_users = []

while unconfirmed_users:
	current_user = unconfirmed_users.pop()

	print(f"Verifying user: {current_user.title()}")
	confirmed_users.append(current_user)

print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())

#删除为特定值的所有列表元素
pets=['dog','cat','bird','rabbit','cat']
while 'cat' in pets:
	pets.remove('cat')
print(pets)

#使用用户输入来填充字典
responses={}

active=True

while active:
	name=input("What is your name? ")
	response=input("\nWhich mountain would you like to climb someday? ")

	responses[name]=response

	repeat=input("\nWould you like to let another person respond?(yes or no) ")

	if repeat =="no":
		active = False
print("\n~~~~~~~POLL RESULTS~~~~~~~")
for name,response in responses.items():
	print(f"{name} : {response}")