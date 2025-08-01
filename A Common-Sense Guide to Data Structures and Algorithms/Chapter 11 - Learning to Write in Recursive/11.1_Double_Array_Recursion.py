def double_array(array, index=0):
  # Base Case
  if index >= len(array):
    return
  array[index] *= 2
  double_array(array, index + 1)

double_array([1, 2, 3, 4, 5])

'''
[2, 2, 3, 4, 5]
[2, 4, 3, 4, 5]
[2, 4, 6, 4, 5]
[2, 4, 6, 8, 5]
[2, 4, 6, 8, 10]
'''