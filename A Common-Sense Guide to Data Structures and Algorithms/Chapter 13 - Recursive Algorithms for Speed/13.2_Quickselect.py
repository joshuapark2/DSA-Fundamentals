def quickselect(arr, k, left, right):
    # Base case: only one element
    if left == right:
        return arr[left]

    # Partition the array and get the pivot index
    pivot_index = partition(arr, left, right)

    # Recursively search in the left or right part based on the kth_lowest_value
    if k < pivot_index:
        return quickselect(arr, k, left, pivot_index - 1)
    elif k > pivot_index:
        return quickselect(arr, k, pivot_index + 1, right)
    else:
        print(arr, arr[pivot_index])
        return arr[pivot_index]

def partition(arr, left, right):
    # Establish pointers and pivot
    pivot = arr[right]
    l = left
    r = right - 1

    while True:
        # increment left pointer while left is less than right pointer and value is less than pivot
        # decrement right pointer while right is greater than left pointer and value is greater than pointer
        while l <= r and arr[l] < pivot:
            l += 1
        while r >= l and arr[r] > pivot:
            r -= 1

        # If we reach a crossroad, exit the loop
        if l >= r:
            break

        # Swap left and right values and increment our left pointer by 1 to either continue the algo or break
        arr[l], arr[r] = arr[r], arr[l]
        l += 1

    # Swap the left pointer with the pivot 
    arr[l], arr[right] = arr[right], arr[l]
    return l

    
array = [0, 50, 20, 10, 60, 30]
quickselect(array, 2, 0, len(array)-1)