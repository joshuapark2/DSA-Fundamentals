def median(array):
  middle = len(array) // 2
  
  if len(array) % 2 == 0:
    return (array[middle-1] + array[middle]) / 2
  else:
    return array[middle]