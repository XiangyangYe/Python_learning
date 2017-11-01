#--------------10.3.5 处理FileNotFoundError异常-----------------#
filename = 'alice.txt'

try:
	with open(filename) as f_obj:
		contents = f_obj.read()
except FileNotFoundError:
	msg = "Sorry, the file " + filename + " does not exist."
	print(msg)