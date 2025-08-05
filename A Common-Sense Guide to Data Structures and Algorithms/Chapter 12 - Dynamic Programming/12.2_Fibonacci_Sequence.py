# Implementing Memorization
def fib(n, memo):
	if n == 0 or n == 1:
		return n
	
	if not memo.get(n):
		memo[n] = fib(n - 2, memo) + fib(n - 1, memo)
	
	return memo[n]


# Thought Process
def fibonnaci_sequence(number):
    if number == 0:
        return 0

    print(fibonnaci_sequence(number - 1))
    return fibonnaci_sequence(number - 1)

fibonnaci_sequence(2)

'''
1. Assume the function already works
2. What is the N - 1 situation?
3. Rinse and Repeat


0, 1, 1, 2, 3, 5, 8

It's the last two previous summed together:

fibonnaci_sequence(5) = 2 + 3 -> fibonnaci_sequence(4) = 5
    where fibonnaci_sequence(4) is 1 + 2 = 3 
    where fibonnaci_sequence(3) is 1 + 1 = 2

fibonnaci_sequence(5) = fibonacci_sequence(4) + fibonacci_sequence(3)
                   5  = 3 + 2

fibonnaci_sequence(N) = fibonacci_sequence(N - 1) + fibonacci_sequence(N - 2)



if number == 0, return 0

0 + 1 = 1
1 + 1 - 2
1 + 2 = 3
2 + 3 = 5
'''
