alien_0 = {'color':'green', 'points':5}
print(alien_0['color'])
print(alien_0['points'])


####################################################
alien_0 = {'color':'green', 'points':5}
new_points = alien_0['points']
print("Your just earned " + str(new_points) + " points!")

###################################################
#添加键-值对
alien_0 = {'color':'green', 'points':5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

########################################################
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
########################################################
alien_0 = {'color':'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0 = {'color':'yellow'}
print("The alien is " + alien_0['color'] + ".")
########################################################
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x_position: " + str(alien_0['x_position']))

#向右移动外星人
#根据外星人当前速度决定将其移动多远
#alien_0['speed'] = 'fast'
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3
#新位置等于老位置加上增量
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x_position: " + str(alien_0['x_position']))
########################################################
#删除键-值对
alien_0 = {'color':'green', 'points':5}
print(alien_0)
del alien_0['points']
print(alien_0)
########################################################
favorite_languages = {
	'jen'   :'python',
	'sarah' :'c',
	'edward':'ruby',
	'phil'  :'python',
}

print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")
########################################################
info_ids = {
	'name': 'VanAllen',
	'age' : '24',
	'city': 'beijing',
	'tel' : '15600115366',
}
print(info_ids)


########################################################
#遍历
user_0 ={
	'username' : 'efermi',
	'first' : 'enrico',
	'last' : 'fermi',
}

for key, value in user_0.items():
	print("\nkey: " + key)
	print("value: " + value)
########################################################
favorite_languages = {
	'jen'   :'python',
	'sarah' :'c',
	'edward':'ruby',
	'phil'  :'python',
}
for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " + language.title() + ".")


########################################################
#遍历所有的键  keys()
favorite_languages = {
	'jen'   :'python',
	'sarah' :'c',
	'edward':'ruby',
	'phil'  :'python',
}
for name in favorite_languages.keys():
	print(name.title())
########################################################
favorite_languages = {
	'jen'   :'python',
	'sarah' :'c',
	'edward':'ruby',
	'phil'  :'python',
}
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(name.title())

	if name in friends:
		print(" Hi " + name.title() + 
			", I see your favorite language is "
			+ favorite_languages[name].title() + "!")

########################################################
favorite_languages = {
	'jen'   :'python',
	'sarah' :'c',
	'edward':'ruby',
	'phil'  :'python',
}
if 'erin' not in favorite_languages.keys():
	print("Erin, please take your poll")
########################################################
#按顺序遍历字典中的所有键
favorite_languages = {
	'jen'   :'python',
	'sarah' :'c',
	'edward':'ruby',
	'phil'  :'python',
}
for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking the poll.")
########################################################
#遍历所有的值
favorite_languages = {
	'jen'   :'python',
	'sarah' :'c',
	'edward':'ruby',
	'phil'  :'python',
}
print("The following languages have been mentioned:")
for language in favorite_languages.values():
	print(language.title())
#遍历所有的值，去除重复项
favorite_languages = {
	'jen'   :'python',
	'sarah' :'c',
	'edward':'ruby',
	'phil'  :'python',
}
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
	print(language.title())

########################################################
#嵌套 字典与列表嵌套使用
#1.在列表中存储字典
alien_0 = {'color':'green', 'points':5}
alien_1 = {'color':'yellow', 'points':10}
alien_3 = {'color':'red', 'points':15}
aliens = [alien_0, alien_1, alien_3]
for alien in aliens:
	print(alien)
########################################################
aliens = []

for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

for alien in aliens[:5]:
	print(alien)
print("...")
print("Title of number of aliens: " + str(len(aliens)))
########################################################
#对前三个alien进行修改
aliens = []

for alien_number in range(0,30):
	new_alien = {'color':'green', 'points':5, 'speed':'slow'}
	aliens.append(new_alien)
for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['points'] = 5
		alien['speed'] = 'medium'
for alien in aliens[0:5]:
	print(alien)
print("...")
########################################################
#2.在字典中存储列表
pizza = {
	'crust':'thick',
	'toppings':['mushrooms','extra cheese']
}

print("You ordered a " + pizza['crust'] + "-crust pizza " +
	"with the following toppings:")
for topping in pizza['toppings']:
	print("\t" + topping)
########################################################

favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell']
}
for name, languages in favorite_languages.items():
	print("\n" + name.title() + "'s favorite languages are:")
	for language in languages:
		print("\t" + language.title())
########################################################

#字典中嵌套字典
users = {
	'aeinstein':{
	'first': 'albert',
	'last':	'einstein',
	'location': 'princeton',
	},

	'mcurie':{
	'first': 'marie',
	'last' : 'curie',
	'location': 'paris'
	},

}

for username, user_info in users.items():
	print("\nUsername: " + username)
	full_name = user_info['first'] + " " + user_info['last']
	location = user_info['location']

	print("\tFull name: " + full_name.title())
	print("\tLocation: " + location.title())