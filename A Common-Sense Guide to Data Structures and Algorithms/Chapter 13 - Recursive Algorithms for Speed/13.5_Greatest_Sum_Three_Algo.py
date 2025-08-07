'''
Write three different implementations of a function that finds the greatest number within an array. 
Write one function that is O(N2), one that is O(N log N), and one that is O(N).
'''

# O(N2)
def greatest_num_n2(array):
    greatest = 0

    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] + array[j] > greatest and array[i] != array[j]:
                greatest = array[i] + array[j]

greatest_num_n2([5, 2, 4, 1, 0])

# O(N log N)
def greatest_num_nlogn(array, left, right):
    if left >= right:
        return

    pivot_index = partition(array, left, right)
    greatest_num_nlogn(array, left, pivot_index - 1)
    greatest_num_nlogn(array, pivot_index + 1, right)
    return(array[right] + array[right - 1])

def partition(array, left, right):
    l = left
    r = right - 1
    pivot = array[right]

    while True:
        while l <= r and array[l] < pivot:
            l += 1
        while r >= l and array[r] > pivot:
            r -= 1
        if l > r:
            break

        array[l], array[r] = array[r], array[l]
        l += 1

    array[l], array[right] = array[right], array[l]
    return l

'''
! We're swapping index[right] instead of index[pivot] because pivot gives us the value of the array, not the index

Partition 1:
[5, 2, 4, 1, 0], pivot = 0, l = 0, r = 3, right = 4
[5, 2, 4, 1, 0], pivot = 0, l = 0, r = 2, right = 4
[5, 2, 4, 1, 0], pivot = 0, l = 0, r = 1, right = 4
[5, 2, 4, 1, 0], pivot = 0, l = 0, r = 0, right = 4
[5, 2, 4, 1, 0], pivot = 0, l = 0, r = -1, right = 4 - break
[0, 2, 4, 1, 5], pivot = 0, l = 0, r = -1, right = 4 - swapped index[l], index[right]

Partition 2:
[0, 2, 4, 1], pivot = 1, l = 0, r = 2, right = 3
[0, 1, 4, 2], pivot = 1, l = 1, r = 2, right = 3
[0, 1, 4, 2], pivot = 1, l = 2, r = 2, right = 3
[0, 1, 2, 4], pivot = 1, l = 3, r = 2, right = 3 - break
[0, 1, 2, 4], pivot = 1, l = 3, r = 2, right = 3 - swapped index[l], index[right]

Partition 3:
[0, 1, 2], pivot = 2, l = 0, r = 1 - everything is sorted now
'''
greatest_num_nlogn([5, 2, 4, 1, 0], 0, 4)

# O(N)
def greatest_num_n(array):
    l, r = 0, 1
    greatest_r = 0
    greatest_l = 0

    while r < len(array):
        if r + 1 < len(array) and array[r] < array[r + 1]:
            greatest_r = r + 1
        r += 1
    r = greatest_r

    while l < r:
        if l + 1 < r and array[l] < array[l + 1]:
            greatest_l = l + 1
        l += 1

    print(array[greatest_r] + array[greatest_l])

greatest_num_n([2, 4, 1, 5, 0])
'''
r - greater than curr

[5, 2, 4, 1, 0], return 9

[4, 2, 1, 5, 0], return 9

[2, 4, 1, 5, 0], return 9

1. increment r til the end and save highest
2. increment l til the end and save the highest
index r + index l = greatest num
'''
