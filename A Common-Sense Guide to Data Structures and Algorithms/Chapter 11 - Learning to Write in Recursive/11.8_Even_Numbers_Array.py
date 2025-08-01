'''
Use recursion to write a function that accepts an array of numbers and returns a new array containing just the even numbers.
'''
# Correct answer - returning array
def select_even(array):
    # Base case: if the array is empty, return an empty list
    if len(array) == 0:
        return []

    # If the first element is even, include it in the result
    if array[0] % 2 == 0:
        return [array[0]] + select_even(array[1:])
    else:
        return select_even(array[1:])

# Returning count of array
def even_numbers(array):
    if len(array) == 0:
        return 0
    elif array[0] % 2 == 0:
        return 1 + even_numbers(array[1:])
    else:
        return even_numbers(array[1:])


even_numbers([1, 2, 3, 4, 5, 6])
'''
1. Assume it works
2. Subproblem
3. See what happens when you call function with subproblem

[1, 2, 3, 4, 5, 6]

1 and [2, 3, 4, 5, 6]
even_numbers([2,3,4,5,6]) -> returns 3

1 + even_numbers(array[1:])
'''