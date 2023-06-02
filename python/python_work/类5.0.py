# class Car:
# 	def __init__(self,make,model,year):
# 		self.make = make
# 		self.model = model
# 		self.year = year
# 		self.odometer_reading =0

# 	def get_descriptive_name(self):
# 			long_name = f"{self.year}{self.model}{self.make}"

# 			return long_name

# 	def read_odometer(self):
# 			print(f"This car has {self.odometer_reading} mileson it.")

# 	def update_odometer(self,mileage):
# 			if mileage >=  self.odometer_reading:
# 				self.odometer_reading = mileage
# 			else:
# 				print("error")

# 	def increment_odometer(self,miles):
# 			self.odometer_reading += miles

# class ElectricCar(Car):
# 	"""电动车的独特之处"""
# 	def __init__(self,make,model,year):
# 		"""
# 		先初始化父类的属性，
# 		再初始化电动汽车特有的属性
# 		"""
# 		super().__init__(make,model,year)
# 		self.battery_size = 75

# 	def describe_battery(self):
# 		print(f"This car has a {self.battery_size}-kwh battery.")

# 	def get_descriptive_name(self):
# 		print('error')
# 		return "error"

# my_tesla = ElectricCar('telsa','model s',2019)
# print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()

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

class ElectricCar(Car):

	def __init__(self,make,model,year):

		super().__init__(make,model,year)
		self.battery = Battery()

my_tesla = ElectricCar('tesla','model s',2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()