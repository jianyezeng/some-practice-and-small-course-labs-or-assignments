class Car:
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading =0
	def get_descriptive_name(self):
			long_name = f"{self.year}{self.model}{self.make}"
			return long_name.title()

	def read_odometer(self):
			print(f"This car has {self.odometer_reading} mileson it.")

	def update_odometer(self,mileage):
			if mileage >=  self.odometer_reading:
				self.odometer_reading = mileage
			else:
				print("error")

	def increment_odometer(self,miles):
			self.odometer_reading += miles



class ElectricCar(Car):

	def __init__(self,make,model,year):
		"""初始化父类的属性"""
		super().__init__(make,model,year)


my_tesla = ElectricCar('tesla','model s',2019)
print(my_tesla.get_descriptive_name())