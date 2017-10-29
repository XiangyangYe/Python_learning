def greet_user():
	print("Hello")

greet_user()

######################################################
def greet_user(username):
	print("Hello, " + username.title() + "!")

greet_user('VanALlen')

######################################################

def display_message(words):
	print("I have learned " + words + "!")

words = "Function"
display_message(words)

######################################################
#传递实参     位置实参
def describe_pet(animal_type, pet_name):
	"""显示宠物信息"""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

#传递实参    关键字实参
def describe_pet(animal_type, pet_name):
	"""显示宠物信息"""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type='hamster', pet_name='harry')

#传递实参    默认值
def describe_pet(pet_name, animal_type='dog'):
	"""显示宠物信息"""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='willie')

######################################################
#8.3 返回值
#8.3.1 返回简单值
def get_formatted_name(first_name, last_name):
	full_name = first_name + ' ' + last_name
	return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

#8.3.2让实参变成可选的
def get_formatted_name(first_name, last_name, middle_name=''):
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' + last_name
	return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

#8.3.3 返回字典
def build_person(first_name, last_name):
	person = {'first_name': first_name, 'last_name': last_name}
	return person

musician = build_person('jimi', 'hendrix')
print(musician)


def build_person(first_name, last_name, age=''):
	person = {'first_name': first_name, 'last_name': last_name}
	if age:
		person['age'] = age
	return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

#8.3.4 结合使用函数和while循环
# def get_formatted_name(first_name, last_name):
# 	full_name = first_name + ' ' + last_name
# 	return full_name

# system_active = True
# while system_active:
# 	print("\nPlease tell me your name.")

# 	f_name = input("First name: ")
# 	l_name = input("Last_name: ")
# 	repeat = input("Would you like to quit? (yes/no)")
# 	if repeat == 'yes':
# 		system_active = False
# 	formatted_name = get_formatted_name(f_name, l_name)
# 	print("\nHello, " + formatted_name + "!")

#############
# def get_formatted_name(first_name, last_name):
# 	full_name = first_name + ' ' + last_name
# 	return full_name

# system_active = True
# while system_active:
# 	print("\nPlease tell me your name.")
# 	print("(enter 'q' at any time to quit)")

# 	f_name = input("First name: ")
# 	if f_name == 'q':
# 		break
# 	l_name = input("Last name: ")
# 	if l_name == 'q':
# 		break

# 	formatted_name = get_formatted_name(f_name, l_name)
# 	print("\nHello, " + formatted_name + "!")

######################################################
#8.4 传递列表
def greet_users(names):
 	for name in names:
 		msg = "Hello, " + name.title() + "!"
 		print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

#8.4.1 在函数中修改列表
unprint_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprint_designs:
	current_design = unprint_designs.pop()
	print("Printing model: " + current_design)
	completed_models.append(current_design)

print("\nThe following models have been printed: ")
for completed_model in completed_models:
	print(completed_model)

############################
def print_models(unprint_designs, completed_models):
	while unprint_designs:
		current_design = unprint_designs.pop()
		print("Printing model: " + current_design)
		completed_models.append(current_design)

def show_completed_models(completed_models):
	print("\nThe following models have been printed: ")
	for completed_model in completed_models:
		print(completed_model)

unprint_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprint_designs, completed_models)
show_completed_models(completed_models)

#8.4.2 禁止函数修改列表
 #print_models(unprint_designs[:], completed_models)

######################################################
 #8.5 传递任意数量的实参
def make_pizza(*toppings):
	print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

#
def make_pizza(*toppings):
	print("\nMaking a pizza with the following toppings:")
	for topping in toppings:
		print("-" + topping)
make_pizza('peperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

#
def make_pizza(size, *toppings):
	print("\nMaking a " + str(size) + "-inch pizza with following toppings: ")
	for topping in toppings:
		print("-" + topping)
make_pizza(14, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#8.5.2 使用任意数量的关键字实参

def build_profile(first, last, **user_info):
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last 
	for key, value in user_info.items():
		profile[key] = value
	return profile

user_profile = build_profile(
				'albert', 'einstein',
				location = 'princeton',
				field = 'physics'
				)
print(user_profile)

######################################################
#8.6 将函数存储在模块中
def make_pizza(size, *toppings):
	print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
	for topping in toppings:
		print("-" + topping)
