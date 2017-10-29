#遍历整个列表 for
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)

#在for循环中执行更多的操作
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician.title() + ", that was a great trick!")

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician.title() + ", that was a great trick!")
	print("I can't wait to see your next trick, " + magician.title() + ".\n")

#在for循环结束后执行一些操作 不缩进
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician.title() + ", that was a great trick!")
	print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")


#4.3创建数值列表
for value in range(1,5):
	print(value)

#使用range()创建数字列表
numbers = list(range(1,6))
print(numbers)

#规定步长
even_numbers = list(range(2,11,2))
print(even_numbers)

#squares.py
squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)
print(squares)

#代码简洁
squares = []
for value in range(1,10):
	squares.append(value*2)
print(squares)

#对数字列表执行简单的统计计算
digits = range(1,11)
print(min(digits))
print(max(digits))
print(sum(digits))

#列表解析
squares = [value**2 for value in range(1,11)]
print(squares)

#learning 
for value in range(1,21):
	print(value)

value = list(range(1,21))
print(value)

squares = []
for value in range(1,21):
	square = value*3
	squares.append(square)
print(squares)

#1~1000000
# for value in range(1,1000001):
# 	print(value)

digits = range(1,1000001)
print(min(digits))
print(max(digits))
print(sum(digits))

even_numbers = range(1,20,2)
result = []
for even_number in even_numbers:
	result.append(even_number)
print(result)

#
numbers = range(1,11)
list_value = []
for number in numbers:
	value = number*3
	list_value.append(value)
print(list_value)

# 立方
numbers = range(1,11)
result = []
for number in numbers:
	value = number**3
	result.append(value)
print(result)

#列表解析
result = [value**3 for value in range(1,11)]
print(result)

#使用列表的一部分
#切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) 

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4]) 

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4]) 

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:]) 

#最后3名
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:]) 

#遍历切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
for player in players[:3]:
	print(player.title())

#复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My Favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

#添加食物
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My Favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

#元组------------------不可修改
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])


#遍历
dimensions = (200,50)
for dimension in dimensions:
	print(dimension)


#不能修改，但可以重新定义
dimensions = (200,50)
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)

dimensions = (400,200)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)


######################################################
# 自助餐
foods = ('meet', 'vegetables', 'water', 'chicken', 'ice cream')
print("The Original Menu is:")
for food in foods:
	print(food)
foods = ('meet',  'water', 'chicken', 'ice cream')
print("The Changed Menu is:")
for food in foods:
	print(food)