'''
There is a numerical sequence known as “Triangular Numbers.” The pattern begins as 1, 3, 6, 10, 15, 21, and continues onward with the Nth number in the pattern, 
which is N plus the previous number. For example, the 7th number in the sequence is 28, since it’s 7 (which is N) plus 21 (the previous number in the sequence). 

Write a function that accepts a number for N and returns the correct number from the series. That is, if the function was passed the number 7, the function would return 28.

- 1st number -> 1 + 0 = 1
- 2nd number -> 1 + 2 = 3
- 3rd number -> 3 + 3 = 6
- 4th number -> 6 + 4 = 10
- 5th number -> 10 + 5 = 15
- 6th number -> 15 + 6 = 21
- 7th number -> 21 + 7 = 28

'''

def triangular_numbers(n):
    if n == 1:
        return 1
    return triangular_numbers(n - 1) + n

triangular_numbers(7)




'''
1. Know that the function has already been created for you
2. What is the subproblem
    triangular_numbers(n - 1) + n (where "N plus previous number")
3. What happens when you apply the function to the subproblem - rinse and repeat

N = 2:
triangular_numbers(2 - 1) + 2 -> n = 1 next
triangular_numbers(1 - 1) + 1 -> n = 0 next
n == 0 return 0
so now going backwards:
    triangular_numbers(n - 1) + n

    triangular_numbers(1 - 1) = (0) + 1 = 1 where N = 1
    triangular_numbers(2 - 1) = (1) + 2 = 3 where N = 2
    triangular_numbers(3 - 1) = (3) + 3 = 6 where N = 3
    triangular_numbers(4 - 1) = (6) + 4 = 10 where N = 4
    triangular_numbers(5 - 1) = (10) + 5 = 15 where N = 5
    triangular_numbers(6 - 1) = (15) + 6 = 21 where N = 6
    triangular_numbers(7 - 1) = (21) + 7 = 28 where N = 7
'''


