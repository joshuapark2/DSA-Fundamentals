'''
Sixth Algorithm: Accepts an array of arrays where the inner array contains 1s and 0s. 
The algorithm counts how many 1s there are.

Given Array:
[
  [0, 1, 1, 1, 0],
  [0, 1, 0, 1, 0, 1],
  [1, 0]
]

Returns: 7
'''

def count_ones(outer_array): 

  count = 0

  for inner_array in outer_array: 
    for number in inner_array:
      if number == 1: 
        count += 1
  return count
