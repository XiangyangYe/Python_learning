def make_pizza(size, *toppings):
	print("\nMaking a " + str(size) + "-inch pizze with the following toppings:")
	for topping in toppings:
		print("-" + topping)
