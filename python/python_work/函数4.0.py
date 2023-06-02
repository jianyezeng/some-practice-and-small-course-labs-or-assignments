#当需要传递任意数量的实参时，可使用元组
def make_pizza(*toppings):                                 #*toppings让python创建一个名为toppings的元组，并将收到的所有值都封存到这个元组中
	"""打印顾客点的所有配料"""
	for topping in toppings:
		print(topping)

make_pizza('pepperoni')
make_pizza('mushroom','green peppers','extra cheese')


def make_pizza(size,*toppings):
	"""概述要制作的比萨"""
	print(f"\nMaking a {size}-inch pizza with the following toppings: ")
	for topping in toppings:
		print(topping)

make_pizza(2,'awd','wqd','wdxca')

def build_profile(first,last,**user_info):
	user_info['first_name']=first
	user_info['last_name']=last

	return user_info

user_profile=build_profile('kdqwd','qwdqd',location = 'sacaec',field = 'acsca')
print(user_profile)


#练习8-12
def make_sandwichs(*sandwichs):
	for sandwich in sandwichs:
		print(sandwich)

make_sandwichs('eqfad')
make_sandwichs('wfqfw','wqd','qwdqd')

#练习8-13
def build_profile(first,last,**user_info):
	user_info['first_name']=first
	user_info['last_name']=last

	return user_info

user_profile=build_profile('afd','faf',fwfq='sfvw',ewff='rswf')
for a,b in user_profile.items():
	print(a+':'+b)

#练习8-14
def make_car(shopper,size,**cars):
	cars['chans']=shopper
	cars['sizes']=size

	return cars

car = make_car('subaru','outback',color = 'blue',tow_package = True)
for key,value in car.items():
	print(f"{key}:{value}")

