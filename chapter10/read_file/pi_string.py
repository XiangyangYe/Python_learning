#-----------------------10.1.5 使用文件内容--------------------------#
filename = 'pi_digits.txt'


with open(filename) as file_object:
	lines = file_object.readlines()           #将文件内容存储在lines中

pi_string = ''
for line in lines:
	pi_string += line.strip()

print(pi_string)
print(len(pi_string))

#---------------------10.1.6 包含100万位的大型文件-------------------#

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()           #将文件内容存储在lines中

pi_string = ''
for line in lines:
	pi_string += line.strip()

print(pi_string[:52] + "...")
print(len(pi_string))

#-------------------10.1.7 圆周率包含你的生日吗 ---------------------#
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()           #将文件内容存储在lines中

pi_string = ''
for line in lines:
	pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
	print("Your birthday appears in the first million digits of pi!")
else:
	print("Your birthday does not appear in the first million digits of pi!")