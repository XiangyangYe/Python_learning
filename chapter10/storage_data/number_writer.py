
########################################################################
#10.4 存储数据
#--------------------10.4.1 json.dump()与json.load()-------------------#
import json

numbers = [2,3,5,7,11,13]
filename = 'numbers.json'
with open(filename, 'w') as f_obj:
	json.dump(numbers,f_obj)                         #需要两个形参


# import json

# filename = 'numbers.json'
with open(filename) as f_obj:
	numbers = json.load(f_obj)                      #只需要一个形参

print(numbers)
