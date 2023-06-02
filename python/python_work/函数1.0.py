def greet_user():
	"""显示简单的问候语"""
	print("hello!")
greet_user()

def greet_user(username):
	"""显示简单的问候语"""
	print(f"hello!{username}")
greet_user('lihua')

#练习8-1
def display_message():
	"""显示一个简单的句子"""
	print("Hello world!")

display_message()

#练习8-2
def favorite_book(title):
	"""显示一个简单的句子"""
	print(f"One of my favorite books is {title}.")

favorite_book("Alice in Wonderland")

#位置实参(顺序很重要)
def describe_pet(animal_type,pet_name):
	"""显示宠物的信息"""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet("hamster",'harry')
describe_pet('harry',"hamster")


#关键字实参(顺序无影响，但务必准确指定函数定义中的形参名)
def describe_pet(animal_type,pet_name):
	"""显示宠物的信息"""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type="hamster",pet_name='harry')
describe_pet(pet_name='harry',animal_type="hamster")

#在定义函数时，可给每个形参指定默认值
#若调用函数时，给了实参，将使用给定的实参，否则，将使用默认值
def describe_pet(pet_name,animal_type='dog'):#当
	"""显示宠物的信息"""
	print(f"I have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='harry',animal_type='hamster')


#等效的函数调用
def describe_pet(pet_name,animal_type='dog'):

#示例一：	
	"""一条名为willie的狗"""
	describe_pet('willie')
	describe_pet(pet_name='willie')
#示例二：
	"""一只名为Harry的仓鼠"""
	describe_pet('harry','hamster')
	describe_pet(pet_name='harry',animal_type='hamster')
	describe_pet(animal_type='hamster',pet_name='harry')

#练习8-3
def make_shirt(chum,ziya):
	"""概要说明T恤的尺码和字样"""
	print(f"\nThis is a T-shirt of {chum} with '{ziya}' on it .")
make_shirt("XXL",'Chinese')

#练习8-4
def make_shirt(chum='big',ziya='I love python'):
	"""概要说明T恤的尺码和字样"""
	print(f"\nThis is a T-shirt of {chum} with '{ziya}' on it .")
make_shirt()
make_shirt(chum='middle')
make_shirt(ziya='cxahsc')

#练习8-5
def describe_city(name='reykjavik',country='iceland'):
	"""显示城市名及其国家"""
	print(f"{name.title()} is in {country.title()}.")

describe_city('Chengdu','China')
describe_city()
describe_city(country='USA',name='New York')