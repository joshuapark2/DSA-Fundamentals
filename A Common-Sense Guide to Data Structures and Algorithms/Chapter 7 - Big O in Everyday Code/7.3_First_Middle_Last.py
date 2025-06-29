

# Third algorithm takes the first, middle, and last element of an array

def sample(array):
  first = array[0]
  middle = array[int(len(array) / 2)] 
  last = array[-1]
  return [first, middle, last]