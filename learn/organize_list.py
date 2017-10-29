
#使用sort()对列表进行排序,永久修改顺序

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
#反向
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

#使用sorted()对列表进行临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the origianl list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the origianl list again:")
print(cars)

#倒着打印列表 reverse()，永久性改变
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)

#确定列表长度
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars_length = len(cars)
print(cars_length)
