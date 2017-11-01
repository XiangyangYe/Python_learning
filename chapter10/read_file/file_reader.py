##################################################################

with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents)                    #read最后返回一个空字符串


with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents.rstrip())           #rstrip删除末尾空白

##################################################################
#-----------------------10.1.2 文件路径--------------------------#
with open('test_files/neo_data.txt') as file_object:  #工作目录下的相对路径
	contents = file_object.read()
	print(contents.rstrip())

#绝对路径打开
file_path = 'D:/workspace1/NewDocument/Python/chapter10/test_files/neo_data.txt'
with open(file_path) as file_object:
	contents = file_object.read()
	print(contents.rstrip())

#-----------------------10.1.3 逐行读取--------------------------#
filename = 'pi_digits.txt'

with open(filename) as file_object: 
	for line in file_object:                #读取包括末尾换行符
		print(line)

#删除末尾空白
filename = 'pi_digits.txt'

with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())

#------------10.1.4 创建一个包含文件各行内容的列表---------------#
filename = 'pi_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()
for line in lines:
	print(line.rstrip())