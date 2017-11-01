################################################################
#--------------------------10.3 异常---------------------------#
#----------------10.3.1 处理zerodivisionerror异常--------------#
#print(5/0)

#----------------10.3.2 使用try-except代码块-------------------#
# try:
# 	print(5/0)
# except ZeroDivisionError:
# 	print("You can't divid by zero!")

# #-------------------10.3.3 使用异常避免崩溃--------------------#
# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")

# while True:
# 	first_number = input("\nFirst number: ")
# 	if first_number == 'q':
# 		break
# 	second_number = input("\nSecond number: ")
# 	if second_number == 'q':
# 		break
# 	answer = int(first_number) / int(second_number)
# 	print("answer is: " + str(answer))

#----------------------10.3.4 else代码块-----------------------#
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break
	second_number = input("\nSecond number: ")
	try:
		answer = int(first_number) / int(second_number)
	except ZeroDivisionError:
		print("You can't divide by 0!")
	else:
		print(answer)



