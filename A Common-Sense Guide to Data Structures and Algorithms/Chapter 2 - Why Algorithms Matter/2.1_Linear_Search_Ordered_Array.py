def linear_search(array, search_value):
  # We iterate through every element in the array:
  for index, element in enumerate(array):
    # If we find the value we're looking for, we return its index:
    if element == search_value:
      print(index)
      return index
    # If we reach an element that is greater than the value 
    # # we're looking for, we can exit the loop early:
    elif element > search_value:
      break
  
  return None

linear_search([3, 17, 75, 80, 202], 22)
