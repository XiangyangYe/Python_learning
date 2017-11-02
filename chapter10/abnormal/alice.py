#--------------10.3.5 处理FileNotFoundError异常-----------------#
# filename = 'alice.txt'

# try:
# 	with open(filename) as f_obj:
# 		contents = f_obj.read()
# except FileNotFoundError:
# 	msg = "Sorry, the file " + filename + " does not exist."
# 	print(msg)

#------------------------10.3.6 分析文本-------------------------#
filename = 'alice.txt'

with open(filename, 'w') as file_object:
	file_object.write("Alice in Wonderland.")

#读文件，计算文件字符数
try:
	with open(filename) as f_obj:
		contents = f_obj.read()
except FileNotFoundError:
	msg = "Sorry, the title " + filename + "does not exist."
	print(msg)
else:
	"""计算文件大致包含多少单词"""
	words = contents.split()
	num_words = len(words)
	print("The file " + filename + " has about " + str(num_words) + " words.")