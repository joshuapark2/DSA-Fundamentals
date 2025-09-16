def rotated(nums, target):
  l, r = 0, len(nums) - 1

  while l <= r:
    m = (l + r) // 2
    if nums[m] == target:
      return m

    if nums[m] >= nums[l]:
      if target < nums[l] or target > nums[m]: # Bot of range, Top of Range
        l = m + 1
      else:
        r = m - 1
    else:
      if target > nums[r] or target < nums[m]: # Still defining lower and upper bounds this way below since we're ascending
        r = m - 1
      else:
        l = m + 1

  return -1


print(rotated([4,5,6,7,0,1,2], 0))