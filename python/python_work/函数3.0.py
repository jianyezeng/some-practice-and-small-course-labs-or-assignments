#传递列表
def greet_users(names):
	""""向列表中的每位用户发出简单的问候"""
	for name in names:
		msg = f"Hello,{name.title()}!"
		print(msg)

usernames = ['hannah','ty','margot']
greet_users(usernames)

#可使用函数修改列表
#未使用函数的情况：
unprinted_designs = ['phone case','robot pendant','dodecahedron']
completed_models = []

while unprinted_designs:
	current_design = unprinted_designs.pop()
	print(f"Printing model: {current_design}")
	completed_models.append(current_design)

print("\nThe following models have been printed: ")
for completed_model in completed_models:
	print(completed_model)
#使用函数时：
def print_models(unprinted_designs,completed_models):
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print(f"Pintting model: {current_design}")
		completed_models.append(current_design)

def show_completed_models(completed_models):
	print("\nThe following models have been printed: ")
	for completed_model in completed_models:
		print(completed_model)

unprinted_designs = ['phone case','robot pendant','dodecahedron']
completed_models=[]

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)

#当不允许函数修改列表时，实参可给定为原列表的副本
#例如lists的副本为lists[:]

#练习8-9
lists = ['scac','qdqd','qcqd','q4r43','uytgtr']
def show_message(message):
	for a in message:
		print(a)

show_message(lists)

#练习8-10
send_messages=[]
lists=['scac','qdqd','qcqd','q4r43','uytgtr']
def show_message(message_1,message_2):
	while message_1:
		message = message_1.pop()
		print(message)
		message_2.append(message)

show_message(lists,send_messages)

print(lists)
print(send_messages)

#练习8-11
send_messages=[]
lists=['scac','qdqd','qcqd','q4r43','uytgtr']

show_message(lists[:],send_messages)

print(lists)
print(send_messages)
