#创建的第一个类
class Dog:
	"""docstring for Dog"""
	def __init__(self,name,age):
		"""初始化属性name和age"""
		self.name = name
		self.age = age

	def sit(self):
		"""模拟小狗收到命令时蹲下"""
		print(f"{self.name} is now sitting.")

	def roll_over(self):
		"""模拟小狗收到命令时打滚"""
		print(f"{self.name} rolled over! ")

#访问属性
my_dog = Dog('Willie',6)
print(f"{my_dog.name} {my_dog.age}")
#调用方法
my_dog.sit()

#可根据类创建任意数量的实例

your_dog = Dog('Lucy',5)

your_dog.roll_over()

#练习9-1
class Restaurant:
	"""创建一个餐馆的类"""
	def __init__(self,restaurant_name,cuisine_type):
		"""初始化属性"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(self.restaurant_name)
		print(self.cuisine_type)

	def open_restaurant(self):
		print(f"{self.restaurant_name.title()} is opening. ")

restaurant_0 = Restaurant('axc','adq')
restaurant_0.describe_restaurant()
restaurant_0.open_restaurant()

#练习9-2
restaurant_1 = Restaurant('HnA','ACXA')
restaurant_2 = Restaurant('bzc','axa')
restaurant_3 = Restaurant('acca','qwdd')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

#练习9-3
class User(object):
	"""docstring for User"""
	def __init__(self,first_name,last_name,age,tel):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.tel = tel

	def describe_user(self):
		print(f"{self.first_name} {self.last_name} {self.age} {self.tel}")

	def greet_user(self):
		print(f"Hello,{self.first_name} {self.last_name}")

user_0 = User("K",'sawq',25,'1522 8852 558')

user_0.describe_user()

user_0.greet_user()

