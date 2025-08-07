'''
Given an array of positive numbers, write a function that returns the greatest product of any three numbers. 
The approach of using three nested loops would clock in at O(N3), 
which is very slow. Use sorting to implement the function in a way that it computes at O(N log N) speed. 
(There are even faster implementations, but we’re focusing on using sorting as a technique to make code faster.)
'''

def greatest_product(array, left, right):
    if left >= right:
        print((array[len(array) - 1]) + (array[len(array) - 2]) + (array[len(array) - 3]))
        return

    pivot_index = partition(array, left, right)
    greatest_product(array, left, pivot_index - 1)
    greatest_product(array, pivot_index + 1, right)
    print(array)
    print((array[len(array) - 1]) + (array[len(array) - 2]) + (array[len(array) - 3]))
    return(array[len(array) - 1]) + (array[len(array) - 2]) + (array[len(array) - 3])



def partition(array, left, right):
    # 1. Establish left, right pointers and pivot
    l = left
    r = right - 1 # or len(array) - 2
    pivot = array[right] # or len(array) - 1

    # 2. while True
    while True:
        # increment left pointer while left is less than right pointer and value is less than pivot
        while l <= r and array[l] < pivot:
            l += 1
        # decrement right pointer while right is greater than left pointer and value is greater than pointer
        while r >= l and array[r] > pivot:
            r -= 1

        # If we reach a crossroad, exit the loop
        if l >= r:
            break

        # Swap left and right values and increment our left pointer by 1 to either continue the algo or break
        array[l], array[r] = array[r], array[l]
        l += 1

    # Swap the left pointer with the pivot and return l
    array[l], array[right] = array[right], array[l] # Must be array right, not pivot
    return l

greatest_product([3, 1, 2, 5, 4], 0, 4)

'''
[1, 2, 3, 4, 5] -> [3, 1, 2, 5, 4]
return -> 5 + 4 + 3 = 12
----------------------------

Partition:
Step 1:
     - [3, 1, 2, 5, 4] l = 0, r = len(array) - 1, pivot = len(array) -> l = left, r = right - 1, pivot = array[right]
    Note: 
     - len(array) = right
     - pivot is the value we want to compare so we need the array value

Step 2: 
    - 1. left less than right and pivot decrement
    - 2. right greater than left and pivot increment
        [3, 1, 2, 5, 4], l = 3, r = 4, pivot = 4
        [3, 1, 2, 5, 4], l = 1, r = 4, pivot = 4
        [3, 1, 2, 5, 4], l = 2, r = 4, pivot = 4
        [3, 1, 2, 5, 4], l = 5, r = 4, pivot = 4

step 3: Swap left and right
    [3, 1, 2, 5, 4], l = 5, r = 4, pivot = 4 -> [3, 1, 2, 4, 5], l = 4, r = 5, pivot = 4
    l += 1 to break the loop

    return l = 5 -> Pivot index = 5

Step 4: Quick Sort Recursion
    1. quicksort(arr, left, pivot_index - 1)
        - [3, 1, 2, 4, 5], l = 3, r = 5, pivot = 4
        - [3, 1, 2, 4, 5], l = 4, r = 5, pivot = 4 - recursion 1 done
        - [3, 1, 2, 4, 5], l = 3, r = 5, pivot = 3
        - [3, 1, 2, 4, 5], l = 3, r = 2, pivot = 3
        - [2, 1, 3, 4, 5], l = 3, r = 2, pivot = 3 - Recursion 2 done
        - [2, 1, 3, 4, 5], l = 2, r = 5, pivot = 2
        - [2, 1, 3, 4, 5], l = 2, r = 1, pivot = 2
        - [1, 2, 3, 4, 5], l = 2, r = 1, pivot = 2 - Recursion 3 done
    2. quicksort(arr, pivot_index + 1, right)
        - [1, 2, 3, 4, 5], l = 1, r = 5, pivot = 6
        - [1, 2, 3, 4, 5], l = 5, r = 5, pivot = 6 - Recursion 1 done
    3. return(len(array) - 1 + len(array) - 2 + len(array) - 3)




----------------------------
1. Partition and Sort
[1, 2, 3, 4, 5]
return(len(array) - 1 + len(array) - 2 + len(array) - 3)
'''