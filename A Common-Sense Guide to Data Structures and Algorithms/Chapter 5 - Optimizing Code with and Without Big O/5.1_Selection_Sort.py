

def selectionSort(array):
  for i in range(len(array) - 1):
    lowest_number_index = i
    for j in range(i + 1, len(array)):
      if array[j] < array[lowest_number_index]:
        lowest_number_index = j
    if lowest_number_index != i:
      temp = array[i]
      array[i] = array[lowest_number_index]
      array[lowest_number_index] = temp
  return array

print(selectionSort([5, 2, 8, 1, 3]))
# Output: [1, 2, 3, 5, 8]





def myVersion(nums):
  for i in range(len(nums) - 1):
    lowest = i
    for j in range(i + 1, len(nums)):
        if nums[j] < nums[lowest]:
            lowest = j
    
    temp = nums[i]
    nums[i] = nums[lowest]
    nums[lowest] = temp
  return nums

print(myVersion([5, 2, 8, 1, 3]))

'''
[4, 2, 7, 1, 3] -> lowest value at 4, which is at index 0

step 1: Compare the 2 lowest value thus far
  [4, 2, 7, 1, 3] -> 2 < 4, so 2 becomes lowest value at index 1
  [4, 2, 7, 1, 3] -> 7 < 2
  [4, 2, 7, 1, 3] -> 1 < 2, lowest value is 1 at index 3
  [4, 2, 7, 1, 3] -> 3 < 1
  - We have reach the end of the array and determined lowest = 1 at index 3
  - We swap 4 and 1

  [1, 2, 7, 4, 3]
  - Rinse and Repeat
'''