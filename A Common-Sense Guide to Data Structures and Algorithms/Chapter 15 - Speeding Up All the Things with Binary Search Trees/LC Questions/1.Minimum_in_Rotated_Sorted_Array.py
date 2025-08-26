'''
Array of length n sorted in ascending order is rotated between 1 and n times.

nums = [0,1,2,4,5,6,7]
nums = [4,5,6,7,0,1,2] (rotated 4 times)
nums = [0,1,2,4,5,6,7] (rotated 7 times)

Rotation means that everything is shifting n + 1 times

Goal: Find the minimum number in the array in O(log n) time
'''

def findMin(nums):
  l, r = 0, len(nums) - 1
  result = nums[0]

  while l <= r:
    if nums[l] < nums[r]:
      result = min(result, nums[l])
      break

    m = (l + r) // 2
    result = min(result, nums[m])

    if nums[l] <= nums[m]:
      l = m + 1
    else:
      r = m - 1
  
  print(result)