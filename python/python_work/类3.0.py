#练习9-4
class make_restaurant(object):
	"""docstring for make_restaurant"""
	def __init__(self, restaurant_name,cuisine_type,):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_severed = 0

	def number_uodate(self,mittle):		
		self.number_severed = mittle
	def increment_number_severed(self,num):
		self.number_severed += num


restaurant_0 = make_restaurant('asa','adqd')
restaurant_0.number_uodate(50)

print(restaurant_0.number_severed)

restaurant_0.number_severed = 10

print(restaurant_0.number_severed)

restaurant_0.increment_number_severed(2)

print(restaurant_0.number_severed)

#练习9-5
class User:
	def __init__(self,first,last,age,login_attempts):

		self.first = first
		self.last = last
		self.age = age
		self.login_attempts = login_attempts

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

user_0 = User('sas','ac',32,3)

user_0.increment_login_attempts()
user_0.increment_login_attempts()

print(user_0.login_attempts)

user_0.reset_login_attempts()

print(user_0.login_attempts)
