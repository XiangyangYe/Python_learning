class Restanuart():
	"""docstring for Restanuart"""
	def __init__(self, restaurant_name, cuisine_type):
		"""初始化属性"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0
	"""两个方法"""
	def describe_restaurant(self):
		print("This restaurant name is " + self.restaurant_name.title() + ".")
		print("This restaurant's cuisine is " + self.cuisine_type + ".")

	def open_restaurant(self):
		print(self.restaurant_name.title() + " is opening.")

	def eating_number(self):
		print(str(self.number_served) + " people have eated in this restaurant.")
	"""改变就餐人数"""
	def set_number_served(self, servers):
		self.number_served = servers
	"""增加就餐人数"""
	def increment_number_served(self, add_number):
		self.number_served += add_number 


#############################################################################
#实例，调用类
my_restaurant = Restanuart('Tian Shang Ren Jian', "Shann'Xi Cai")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

#
your_restaurant = Restanuart('Fu Man Lou', 'Si Chuan Cai')
your_restaurant.describe_restaurant()
your_restaurant.open_restaurant()
your_restaurant.set_number_served(100)
your_restaurant.eating_number()
your_restaurant.increment_number_served(400)
your_restaurant.eating_number()


