# #练习9-6
# class Restaurant:

# 	def __init__(self,restaurant_name,cuisine_type):

# 		self.restaurant_name = restaurant_name
# 		self.cuisine_type = cuisine_type

# 	def describe_restaurant(self):
# 		print(self.restaurant_name)
# 		print(self.cuisine_type)
# 	def open_restaurant(self):
# 		print(f"{self.restaurant_name.title()} is opening.")

# class IceCreamStand(Restaurant):

# 	def __init__(self,restaurant_name,cuisine_type):

# 		super().__init__(restaurant_name,cuisine_type)

# 		self.flavors = ['apple','bear']

# 	def record(self):

# 		for flavor in self.flavors:
# 			print(flavor)

# ice = IceCreamStand('nick','dcsca')
# ice.record()

#练习9-7
# class User:
# 	def __init__(self,first_name,last_name,age,sex):

# 		self.first_name = first_name
# 		self.last_name = last_name
# 		self.age = age
# 		self.sex = sex

# 	def describe_user(self):
# 		print(f"{self.first_name} {self.last_name}  {self.age} {self.sex}")

# 	def greet_user(self):
# 		print(f"Hello,{self.first_name} {self.last_name}")

# class Admin(User):

# 	def __init__(self,first_name,last_name,age,sex):

# 		super().__init__(first_name,last_name,age,sex)

# 		self.privileges = ['can add post','can delete post','can ban user']

# 	def show_privileges(self):

# 		for privilege in self.privileges:
# 			print(privilege)

# adi = Admin('sdwdq','qwd',17,'asx')

# adi.show_privileges()

#练习9-8
class User:
	def __init__(self,first_name,last_name,age,sex):

		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.sex = sex

	def describe_user(self):
		print(f"{self.first_name} {self.last_name}  {self.age} {self.sex}")

	def greet_user(self):
		print(f"Hello,{self.first_name} {self.last_name}")

class Privileges:
	def __init__(self,*privilege):
		self.privileges = ['can add post','can delete post','can ban user']

	def show_privileges(self):
		for privilege in self.privileges:
			print(privilege)

class Admin(User):
	def __init__(self,first_name,last_name,age,sex):
		super().__init__(first_name,last_name,age,sex)

		self.privileges = Privileges()

adi =Admin('add','dqw',26,'qwd')

adi.privileges.show_privileges()

#练习9-9
class Car:
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading =0

	def get_descriptive_name(self):
			long_name = f"{self.year}{self.model}{self.make}"

			return long_name

	def read_odometer(self):
			print(f"This car has {self.odometer_reading} mileson it.")

	def update_odometer(self,mileage):
			if mileage >=  self.odometer_reading:
				self.odometer_reading = mileage
			else:
				print("error")

	def increment_odometer(self,miles):
			self.odometer_reading += miles

class Battery:

	def __init__(self,battery_size = 75):

		self.battery_size = battery_size


	def describe_battery(self):
		print(f"This car has a {self.battery_size}-kwh battery.")

	def get_range(self):
		if self.battery_size == 75:
			print("260km")
		else :
			print("300km")

	def upgrate_battery(self):

		self.battery_size = 100

class ElectricCar(Car):

	def __init__(self,make,model,year):

		super().__init__(make,model,year)
		self.battery = Battery()

car_0 = ElectricCar('qws','ds','dqwd')
car_0.battery.get_range()

car_0.battery.upgrate_battery()
car_0.battery.get_range()