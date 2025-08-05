def fib(n):
	if n == 0:
		return 0
	
	a = 0
	b = 1
	
	for i in range(1, n):
		temp = a
		a = b
		b = temp + a
		
	return b