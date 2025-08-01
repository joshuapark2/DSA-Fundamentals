def factorial(number, index=1, product=1):
	if index > number:
		return product
	else:
		return factorial(number, index + 1, product * index)