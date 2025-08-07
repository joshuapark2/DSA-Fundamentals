'''
The following function finds the “missing number” from an array of integers. 
    That is, the array is expected to have all integers from 0 up to the array’s length, but one is missing. 
    As examples, the array, [5, 2, 4, 1, 0] is missing the number 3, and the array, [9, 3, 2, 5, 6, 7, 1, 0, 4] is missing the number 8.

Use sorting to write a new implementation of this function that only takes O(N log N). 
(There are even faster implementations, but we’re focusing on using sorting as a technique to make code faster.)
'''

'''
The following function finds the “missing number” from an array of integers. 
    That is, the array is expected to have all integers from 0 up to the array’s length, but one is missing. 
    As examples, the array, [5, 2, 4, 1, 0] is missing the number 3, and the array, [9, 3, 2, 5, 6, 7, 1, 0, 4] is missing the number 8.

Use sorting to write a new implementation of this function that only takes O(N log N). 
(There are even faster implementations, but we’re focusing on using sorting as a technique to make code faster.)
'''

def missing_number(array, left, right):
    # return if the left-side is equal or overpasses the right-side
    if left >= right:
        return

    # Variable pivot_index which stores and calls the partition function
    pivot_index = partition(array, left, right)

    # Recursively decrement and increment
    missing_number(array, left, pivot_index - 1)
    missing_number(array, pivot_index + 1, right)

    # loop array and if next value isn't +1, return that value, else return array
    for i in range(len(array)):
        if i < len(array) - 1 and array[i] + 1 != array[i + 1]:
            print(array[i] + 1)
            return array[i] + 1
    return array

def partition(array, left, right):
    # Variables that creates left, right pointers and stores pivot value
    l = left
    r = right - 1
    pivot = array[right]

    # while True
    while True:

        # while left-side is less than or equal to right-side and the current left pointer value is less than pivot, increment our pointer by 1
        while l <= r and array[l] < pivot:
            l += 1

        # while right-side is greater than or equal to left-side and the current right pointer value is greater than pivot, decrement pointer by 1
        while r >= l and array[r] > pivot:
            r -= 1

        # if left pointer meets or cross-roads, break the loop
        if l >= r:
            break

        # swap left pointer and right pointer values
        array[l], array[r] = array[r], array[l]

        # increment left point by 1 to continue the loop
        l += 1

    # swap left pointer value and right variable specifically since we want to place pivot in its proper place
    array[l], array[right] = array[right], array[l]

    # return l pointer
    return l

missing_number([5, 2, 4, 1, 0], 0, 4)


# Personal step-by-step algorithm below for quick-sorting + recursion
'''
def missing_number(array, left, right):
    # return if the left-side is equal or overpasses the right-side

    # Variable pivot_index which stores and calls the partition function

    # Recursively decrement and increment


    # loop array and if next value isn't +1, return that value, else return array


def partition(array, left, right):
    # Variables that creates left, right pointers and stores pivot value

    # while True

        # while left-side is less than or equal to right-side and the current left pointer value is less than pivot, increment our pointer by 1

        # while right-side is greater than or equal to left-side and the current right pointer value is greater than pivot, decrement pointer by 1

        # if left pointer meets or cross-roads, break the loop

        # swap left pointer and right pointer values

        # increment left point by 1 to continue the loop

    # swap left pointer value and right variable specifically since we want to place pivot in its proper place
'''
