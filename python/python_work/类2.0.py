# class Car(object):
# 	"""docstring for Car"""
# 	def __init__(self,make,model,year):
# 		"""初始化描述汽车的属性"""
# 		self.make = make
# 		self.model = model
# 		self.year = year
# 	def get_descriptive_name(self):
# 		"""返回整洁的描述性信息"""
# 		long_name = f"{self.year} {self.make} {self.model}"
# 		return long_name.title()

# my_new_car = Car('audi','a4',2019)
# print(my_new_car.get_descriptive_name())

#创建实例时，有些属性无需通过形参来定义，可在方法_int_中为其指定默认值
# class Car:
# 	"""docstring for Car"""
# 	def __init__(self,make,model,year):
# 		"""初始化描述汽车的属性"""
# 		self.make = make
# 		self.model = model
# 		self.year = year
# 		self.odometer_reading = 0

# 	def get_descriptive_name(self):
# 		"""返回整洁的描述性信息"""
# 		long_name = f"{self.year} {self.make} {self.model}"
# 		return long_name.title()

# 	def read_odometer(self):
# 		"""打印一条指出汽车里程的消息"""
# 		print(f"This car has {self.odometer_reading} miles on it .")

# my_new_car = Car('audi','a4',2019)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()

# #修改属性的值
# #直接修改属性的值
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

#通过方法修改属性的值
# class Car:
# 	"""docstring for Car"""
# 	def __init__(self,make,model,year):
# 		"""初始化描述汽车的属性"""
# 		self.make = make
# 		self.model = model
# 		self.year = year
# 		self.odometer_reading = 0

# 	def get_descriptive_name(self):
# 		"""返回整洁的描述性信息"""
# 		long_name = f"{self.year} {self.make} {self.model}"
# 		return long_name.title()

# 	def read_odometer(self):
# 		"""打印一条指出汽车里程的消息"""
# 		print(f"This car has {self.odometer_reading} miles on it .")
# 	def update_odometer(self,mileage):
# 		"""
# 		将里程表读数设置为指定的值，
# 		禁止将里程表数往回调
# 		"""
# 		if mileage > self.odometer_reading:			
# 			self.odometer_reading = mileage
# 		else:
# 			print("error!")
# my_new_car = Car('audi','a4',2019)
# print(my_new_car.get_descriptive_name())
# print(my_new_car.year)
# print(my_new_car.odometer_reading)

# my_new_car.update_odometer(2020)
# print(my_new_car.odometer_reading)
# my_new_car.update_odometer(2018)
# my_new_car.update_odometer(2021)
# print(my_new_car.odometer_reading)

#通过方法对属性的值进行递增
class Car:
	"""docstring for Car"""
	def __init__(self,make,model,year):
		"""初始化描述汽车的属性"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""返回整洁的描述性信息"""
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

	def read_odometer(self):
		"""打印一条指出汽车里程的消息"""
		print(f"This car has {self.odometer_reading} miles on it .")
	def update_odometer(self,mileage):
		"""
		将里程表读数设置为指定的值，
		禁止将里程表数往回调
		"""
		if mileage > self.odometer_reading:			
			self.odometer_reading = mileage
		else:
			print("error!")
	def increment_odometer(self,miles):
		if miles > 0:
			self.odometer_reading += miles
		else:
			print("error")

my_new_car = Car('subaru','a4','2015')
my_new_car.update_odometer(2010)
my_new_car.read_odometer()

my_new_car.increment_odometer(10)
my_new_car.read_odometer()

my_new_car.increment_odometer(-10)
my_new_car.read_odometer()