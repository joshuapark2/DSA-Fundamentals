# Third algorithm takes the first, middle, and last element of an array

def sample(array):
  first = array[0]
  middle = array[int(len(array) / 2)] 
  last = array[-1]
  return [first, middle, last]

'''
int necessary due to len(array) / 2 being a float value due to division
Otherwise: TypeError: list indices must be integers or slices, not float

Note: type conversion for int doesn't round up - it simply chops off the decimals.
'''