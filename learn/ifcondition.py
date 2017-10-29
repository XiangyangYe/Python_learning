cars = ['audi', 'bmw', 'toyota', 'chanan']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
	print("Hold the anchovies")


#检查多个条件
# age_0 = 22
# age_1 = 18
# age_0 >= 21 and age_1 >= 21

banned_users =['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
	print(user.title() + ", you can post a response if you wish.")

#布尔表达式

car = 'subaru'
print("Is car == 'subaru' ? I predict True.")
print(car == 'subaru')

print("Is car == 'audi' ? I predict False")
print(car == 'audi')

#If 语句
age = 19;
if age >= 18:
	print("You are old enough to vote")


# if-elif-else
age = 12
if age < 4:
	print("your admission cost is $0.")
elif age < 18:
	print("your admission cost is $5.")
else:
	print("your admission cost is $10.")

age = 12
if age <4:
	price = 0
elif age <18:
	price = 5
else:
	price = 10
print("Your admission cost is " + str(price) + ".")

#使用if语句处理列表

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
	print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")



requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("Sorry, we are out of green peppers right now.")
	else:
		print("Adding " + requested_topping + ".")
print("\nFinished making your pizza")


requested_toppings = []

if requested_toppings:
	for requested_topping in requested_toppings:
		print("Adding " + requested_topping + ".")
	print("\nFinished making your pizza!")
else:
	print("Are you sure you want a plain pizza")

#使用多个列表
available_toppings = ['mushrooms', 'olives', 'green peppers',
					  'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding " + requested_topping + ".")
	else:
		print("Sorry, we don't have " + requested_topping + '.')
print("\nFinished making your pizza")


#################################################
users_names = ['VanAllen', 'admin', 'Bob', 'JayChou', 'JJ']
for users_name in users_names:
	if users_name == 'admin':
		print("Hello " + users_name + "," + "would you like to see a status report?")
	else:
		print("Hello " + users_name + "," + "thank you for logging in again.")


#########################################
numbers = range(1,10)
for number in numbers:
	if number == 1:
		print("1st")
	elif number == 2:
		print("2nd")
	elif number == 3:
		print("3rd")
	else:
		print(str(number) + "th")




