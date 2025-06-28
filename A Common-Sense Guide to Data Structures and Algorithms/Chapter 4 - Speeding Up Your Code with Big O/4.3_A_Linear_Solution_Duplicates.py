def has_duplicate_value(array):
  existing_numbers = {}
  for num in array:
      if existing_numbers.get(num) == 1:
          return True
      else:
          existing_numbers[num] = 1
  return False


# Question and Answer from Chapter below

def greatestNumber(array): 
  for i in array:
    # Assume for now that i is the greatest:
    isIValTheGreatest = True
  for j in array:
    # If we find another value that is greater than i, # i is not the greatest:
    if j > i:
      isIValTheGreatest = False
      
  # If, by the time we checked all the other numbers, i
  # is still the greatest, it means that i is the greatest number: 
  if isIValTheGreatest:
	  return i

def greatestSingleNumber(array):
  greatest = 0

  for n in array:
      if n > greatest:
          greatest = n
  return greatest
    