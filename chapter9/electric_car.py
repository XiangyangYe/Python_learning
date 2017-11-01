class Car(object):
	"""docstring for Car"""
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 25

	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + " miles on it.")

	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You Can't roll back an odometer")

	def increment_odometer(self, miles):
		self.odometer_reading += miles

class ElectricCar(Car):
	"""电动汽车的独特之处"""
	def __init__(self, make, model, year):
		"""初始化父类的属性"""
		super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
##############################################################################
#给子类定义属性和方法
class Car(object):
	"""docstring for Car"""
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 25

	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + " miles on it.")

	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You Can't roll back an odometer")

	def increment_odometer(self, miles):
		self.odometer_reading += miles

class ElectricCar(Car):
	"""电动汽车的独特之处"""
	def __init__(self, make, model, year):
		"""初始化父类的属性"""
		super().__init__(make, model, year)
		self.battery_size = 70

	def describe_battery(self):
		print("This car has a " + str(self.battery_size) + "-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery() 

#9.3.4重写父类的方法
class Car(object):
	"""docstring for Car"""
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 25

	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + " miles on it.")

	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You Can't roll back an odometer")

	def increment_odometer(self, miles):
		self.odometer_reading += miles




class ElectricCar(Car):
	"""电动汽车的独特之处"""
	def __init__(self, make, model, year):
		"""初始化父类的属性"""
		super().__init__(make, model, year)
		self.battery_size = 70

	def describe_battery(self):
		print("This car has a " + str(self.battery_size) + "-kWh battery.")



my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery() 


 